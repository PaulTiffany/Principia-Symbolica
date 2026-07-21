r"""
Principia Symbolica — LLM Atlas Builder

Emits a single teleport-grade artifact for machine readers: every labelled
object in the manuscript as an addressable node carrying its *verbatim LaTeX
body*, its resolved dependency edges (cites / cited_by), its proof linkage,
and its certificate tier — plus a bundled macro/notation dictionary so each
body is self-resolving.

Why JSON-of-source teleports (and the PDF does not): math stays verbatim
LaTeX (perfect signal, not extracted glyph-soup), every claim is addressable
by label (jump, don't scan 446 pages), and the edges are resolved (traverse
the dependency graph instead of reading linearly).

Outputs:
  bib/principia_atlas.json     — the atlas (nodes + macros + meta)
  bib/README_FOR_LLMS.md       — one-screen reader's guide

Inputs:
  src/**/*.tex                 — full bodies + macro dictionary (verbatim)
  bib/label_graph.json         — resolved cites / cited_by edges
  bib/proof_report.json        — proof coverage gaps
  bib/certificate_ledger.json  — witnessed tiers (optional)

Usage:
  python ci/build_llm_atlas.py            # regenerate the atlas
  python ci/build_llm_atlas.py --check    # drift guard: exit 1 if stale,
                                           # 0 if current (no write)
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
MAIN = SRC / "main.tex"
OUT_JSON = ROOT / "bib" / "principia_atlas.json"
OUT_README = ROOT / "bib" / "README_FOR_LLMS.md"
LABEL_GRAPH = ROOT / "bib" / "label_graph.json"
PROOF_REPORT = ROOT / "bib" / "proof_report.json"
CERT_LEDGER = ROOT / "bib" / "certificate_ledger.json"
LEAN_ALIGNMENT = ROOT / "bib" / "principia_lean_alignment.json"

ENV_TYPES = (
    "theorem|lemma|corollary|proposition|definition|axiom|assumption|"
    "proof|remark|scholium|conjecture|note|demonstratio|propositio"
)
ENV_OPEN = re.compile(
    r"\\begin\{(" + ENV_TYPES + r")\}(?:\[(.*?)\])?", re.IGNORECASE | re.DOTALL
)
LABEL_PAT = re.compile(r"\\label\{([^}]+)\}")
REF_PAT = re.compile(r"\\(?:ref|autoref|cref|eqref)\{([^}]+)\}")
SECTION_PAT = re.compile(r"\\(chapter|section|subsection|subsubsection)\*?\{([^}]+)\}")
NEWCMD_PAT = re.compile(r"\\(?:new|renew)command\{\\([A-Za-z]+)\}\s*(?:\[(\d)\])?\s*\{")
MACRO_USE = re.compile(r"\\([A-Za-z]+)")

THEOREM_CLASS = {
    "theorem", "lemma", "corollary", "proposition", "propositio", "conjecture",
}

# Canonical role over the manuscript's Newton-Latin / English dual taxonomy.
# The verbatim `type` is preserved; `role` is the machine-readable collapse.
# demonstratio is a *worked demonstration / application*, not a formal proof,
# so it is kept distinct from `proof`.
ROLE_MAP = {
    "demonstratio": "demonstration",
    "propositio": "proposition",
}


def strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def char_to_line(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def book_from_filename(fname: str) -> str:
    stem = Path(fname).stem
    for n in range(1, 10):
        if f"book{n}" in stem:
            return f"book{n}"
    return stem


def matter_region_from_filename(fname: str) -> str:
    """Coarse manuscript region for LLM navigation semantics."""
    stem = Path(fname).stem
    if stem.startswith("appendix_"):
        return "appendix"
    if stem in {"book1", "book2", "book3", "book4", "book5", "book6", "book7", "book8", "book9"}:
        return "mainmatter"
    if stem == "scholium_symbolicum":
        return "mainmatter"
    if stem in {"operatio", "integratio", "temperatio", "executio"}:
        return "operator_poetry"
    if stem == "invariant_ledger":
        return "ledger"
    return "source_support"


def matter_role_from_filename(fname: str) -> str:
    """Human-facing role of a source file within the manuscript architecture."""
    stem = Path(fname).stem
    if stem.startswith("appendix_"):
        return "appendix_expansion"
    if stem.startswith("book"):
        return "canonical_book"
    if stem == "scholium_symbolicum":
        return "book1_foundational_scholium"
    if stem in {"operatio", "integratio", "temperatio", "executio"}:
        return "operator_poetry"
    if stem == "invariant_ledger":
        return "ledger"
    return "source_support"


def load_json(path: Path) -> Any:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def brace_match(text: str, open_pos: int) -> int:
    """Return index just past the '}' matching the '{' at open_pos."""
    depth = 0
    i = open_pos
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    return len(text)


def build_macros(main_text: str) -> dict[str, dict[str, Any]]:
    """name -> {expansion, arity} for every \\newcommand in main.tex."""
    macros: dict[str, dict[str, Any]] = {}
    text = strip_comments(main_text)
    for m in NEWCMD_PAT.finditer(text):
        name = m.group(1)
        arity = int(m.group(2)) if m.group(2) else 0
        body_open = m.end() - 1  # the '{' that NEWCMD_PAT ended on
        body_close = brace_match(text, body_open)
        expansion = text[body_open + 1: body_close - 1].strip()
        macros[name] = {"expansion": expansion, "arity": arity}
    return macros


def end_of_env(text: str, env: str, start: int) -> int:
    """Index just past the matching \\end{env} (envs do not self-nest here)."""
    m = re.compile(r"\\end\{" + re.escape(env) + r"\}", re.IGNORECASE).search(text, start)
    return m.end() if m else min(len(text), start + 4000)


def extract_nodes(
    fname: str, raw: str, macro_names: set[str]
) -> list[dict[str, Any]]:
    text = strip_comments(raw)
    book = book_from_filename(fname)
    matter_region = matter_region_from_filename(fname)
    matter_role = matter_role_from_filename(fname)
    nodes: list[dict[str, Any]] = []

    # Track the most recent theorem-class label, to link bare proofs.
    last_result_label = ""

    # Interleave envs and sections in source order so proof->result by
    # proximity is correct.
    events: list[tuple[int, str, Any]] = []
    for m in ENV_OPEN.finditer(text):
        events.append((m.start(), "env", m))
    for m in SECTION_PAT.finditer(text):
        events.append((m.start(), "sec", m))
    events.sort(key=lambda e: e[0])

    for pos, kind, m in events:
        if kind == "sec":
            level, title = m.group(1), m.group(2).strip()
            # A section label belongs to the heading only when it is attached
            # immediately after the command. Searching an arbitrary window can
            # steal the label from the next environment and emit duplicate ids.
            ahead = text[m.end(): m.end() + 200]
            lbl = re.match(r"\s*\\label\{([^}]+)\}", ahead)
            label = lbl.group(1) if lbl else ""
            nodes.append({
                "id": label or f"section:{fname}:{char_to_line(text, pos)}",
                "type": "section",
                "subtype": level,
                "label": label,
                "name": title,
                "book": book,
                "matter_region": matter_region,
                "matter_role": matter_role,
                "file": fname,
                "line": char_to_line(text, pos),
                "latex_body": "",
                "macros_used": [],
                "cites": [],
                "cited_by": [],
            })
            continue

        env = m.group(1).lower()
        name = (m.group(2) or "").strip()
        end = end_of_env(text, env, m.start())
        body = text[m.start(): end]

        lbl = LABEL_PAT.search(body)
        label = lbl.group(1) if lbl else ""

        node: dict[str, Any] = {
            "id": label or f"{env}:{fname}:{char_to_line(text, pos)}",
            "type": env,
            "label": label,
            "name": name,
            "book": book,
            "matter_region": matter_region,
            "matter_role": matter_role,
            "file": fname,
            "line": char_to_line(text, pos),
            "latex_body": body.strip(),
            "macros_used": sorted(
                {u for u in MACRO_USE.findall(body) if u in macro_names}
            ),
            "refs": sorted(set(REF_PAT.findall(body))),
        }

        if env == "proof":
            # Link to the result it proves: explicit \ref in the [optional],
            # else the nearest preceding theorem-class label.
            ref_in_name = REF_PAT.search(name or "")
            node["proves"] = ref_in_name.group(1) if ref_in_name else last_result_label
        elif env in THEOREM_CLASS:
            last_result_label = label or last_result_label

        nodes.append(node)

    return nodes


def graph_index(label_graph: Any) -> dict[str, dict[str, list[str]]]:
    out: dict[str, dict[str, list[str]]] = {}
    if not label_graph:
        return out
    for e in label_graph.get("entries", []):
        lbl = e.get("label")
        if lbl:
            out[lbl] = {
                "cites": e.get("cites", []),
                "cited_by": e.get("cited_by", []),
            }
    return out


def _first_tier(obj: Any) -> str | None:
    """First 'tier' string anywhere within a ledger entry (it is nested)."""
    if isinstance(obj, dict):
        t = obj.get("tier")
        if isinstance(t, str):
            return t
        for v in obj.values():
            r = _first_tier(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _first_tier(v)
            if r:
                return r
    return None


def harvest_tiers(ledger: Any) -> dict[str, str]:
    """Map live label -> tier from the certificate ledger.

    The ledger is a list of entries keyed by `label`, each carrying its tier
    nested under `certified_baseline`; reconciliation has already mapped any
    renamed witness label to its live label, so we key on `label` directly.
    """
    out: dict[str, str] = {}
    if not ledger:
        return out
    entries = ledger.get("ledger") if isinstance(ledger, dict) else ledger
    if isinstance(entries, list):
        for e in entries:
            if isinstance(e, dict) and isinstance(e.get("label"), str):
                tier = _first_tier(e)
                if tier:
                    out[e["label"]] = tier
    return out


def coverage_gaps(proof_report: Any) -> set[str]:
    if not proof_report:
        return set()
    return {
        g["label"]
        for g in proof_report.get("coverage_gaps", [])
        if isinstance(g, dict) and g.get("label")
    }


def dependency_scc_report(nodes: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, str]]:
    """Return dependency-graph SCCs and label -> nontrivial SCC id.

    The graph direction is PS dependency direction: node -> depends_on. A
    nontrivial SCC therefore means a real circular dependency in the atlas'
    logical-support graph, not merely reciprocal prose adjacency.
    """
    by_label = {n["label"]: n for n in nodes if n.get("label")}
    node_rank = {
        n["label"]: (str(n.get("book", "")), str(n.get("file", "")), int(n.get("line", 0)), n["label"])
        for n in nodes
        if n.get("label")
    }

    def label_key(label: str) -> tuple[str, str, int, str]:
        return node_rank.get(label, ("", "", 0, label))

    graph: dict[str, list[str]] = {
        label: sorted(
            {d for d in n.get("depends_on", []) if d in by_label},
            key=label_key,
        )
        for label, n in by_label.items()
    }

    index = 0
    stack: list[str] = []
    on_stack: set[str] = set()
    indices: dict[str, int] = {}
    lowlinks: dict[str, int] = {}
    components: list[list[str]] = []

    def strongconnect(v: str) -> None:
        nonlocal index
        indices[v] = index
        lowlinks[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)

        for w in graph.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif w in on_stack:
                lowlinks[v] = min(lowlinks[v], indices[w])

        if lowlinks[v] == indices[v]:
            component: list[str] = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                component.append(w)
                if w == v:
                    break
            components.append(sorted(component, key=label_key))

    for label in sorted(graph, key=label_key):
        if label not in indices:
            strongconnect(label)

    nontrivial = [
        c for c in components
        if len(c) > 1 or any(src in graph.get(src, []) for src in c)
    ]
    nontrivial.sort(key=lambda c: (-len(c), label_key(c[0])))

    label_to_scc: dict[str, str] = {}
    rendered: list[dict[str, Any]] = []
    for i, component in enumerate(nontrivial, start=1):
        scc_id = f"dependency_scc:{i:03d}"
        for label in component:
            label_to_scc[label] = scc_id
        component_set = set(component)
        internal_edges = [
            {"from": src, "to": dst}
            for src in component
            for dst in graph.get(src, [])
            if dst in component_set
        ]
        rendered.append({
            "id": scc_id,
            "size": len(component),
            "books": sorted({str(by_label[label].get("book", "")) for label in component}),
            "labels": component,
            "internal_edge_count": len(internal_edges),
            "internal_edges": internal_edges,
        })

    report = {
        "direction": "node -> depends_on (toward foundations)",
        "node_count": len(graph),
        "edge_count": sum(len(v) for v in graph.values()),
        "scc_count": len(components),
        "nontrivial_scc_count": len(rendered),
        "largest_scc_size": max((len(c) for c in components), default=0),
        "largest_nontrivial_scc_size": max((c["size"] for c in rendered), default=0),
        "components": rendered,
    }
    return report, label_to_scc


def mark_forward_refs(nodes: list[dict[str, Any]]) -> None:
    """Annotate same-file references that point to later labelled nodes.

    Forward references stay in `cites` as manuscript navigation, but are
    excluded from `depends_on` so "see below" prose does not become a logical
    support edge.
    """
    by_label = {n["label"]: n for n in nodes if n.get("label")}
    for n in nodes:
        forward = sorted(
            {
                ref for ref in n.get("cites", [])
                if ref in by_label
                and by_label[ref].get("file") == n.get("file")
                and int(by_label[ref].get("line", 0)) > int(n.get("line", 0))
            }
        )
        if forward:
            n["forward_refs"] = forward
            n["forward_ref_roles"] = [
                forward_ref_record(n, by_label[ref], ref)
                for ref in forward
            ]


def is_appendix_node(node: dict[str, Any]) -> bool:
    """True when a node lives in an appendix source file."""
    return str(node.get("file", "")).startswith("appendix_")


def mark_appendix_teaser_refs(nodes: list[dict[str, Any]]) -> None:
    """Annotate main-text references into appendices.

    These are kept in `cites` for reader navigation, but excluded from
    `depends_on`: a theorem may point forward to an appendix for an expanded
    derivation without making the main theorem logically depend on appendix
    expansion material.
    Appendix-to-main references are not affected; those are canonical anchors.
    """
    by_label = {n["label"]: n for n in nodes if n.get("label")}
    for n in nodes:
        if is_appendix_node(n):
            continue
        appendix_refs = sorted(
            {
                ref for ref in n.get("cites", [])
                if ref in by_label and is_appendix_node(by_label[ref])
            }
        )
        if appendix_refs:
            n["appendix_teaser_refs"] = appendix_refs
            n["appendix_teaser_ref_roles"] = [
                appendix_teaser_ref_record(n, by_label[ref], ref)
                for ref in appendix_refs
            ]


def ref_context(latex_body: str, label: str, window: int = 120) -> str:
    """Return compact text around the first reference to label."""
    if not latex_body:
        return ""
    pat = re.compile(
        r"\\(?:ref|autoref|cref|eqref)\{" + re.escape(label) + r"\}"
    )
    m = pat.search(latex_body)
    if not m:
        return ""
    start = max(0, m.start() - window)
    end = min(len(latex_body), m.end() + window)
    return re.sub(r"\s+", " ", latex_body[start:end]).strip()


def classify_forward_ref(source: dict[str, Any], target: dict[str, Any], context: str) -> str:
    """Heuristic role for a forward reference.

    This is reader-navigation metadata, not proof classification.
    """
    ctx = context.lower()
    target_type = target.get("type", "")

    if target_type == "section" or source.get("type") == "section":
        return "navigation"
    if target_type == "proof" or "see proof" in ctx or "proof~" in ctx:
        return "proof_below"
    if any(
        phrase in ctx
        for phrase in (
            "later formalized",
            "formalized in",
            "formalized by",
            "defined later",
            "defined below",
            "developed later",
            "developed in",
            "analyzed later",
            "below",
        )
    ):
        return "later_formalization"
    if any(
        phrase in ctx
        for phrase in (
            "downstream",
            "application",
            "applied",
            "use of",
            "used in",
            "consequence",
            "implication",
            "variant",
            "extension",
        )
    ):
        return "downstream_application"
    if any(
        phrase in ctx
        for phrase in (
            "interpret",
            "bridge",
            "resonant",
            "dialogue",
            "cf.~",
            "cf.",
            "read through",
            "in this light",
        )
    ):
        return "interpretive_bridge"
    return "teaser"


def forward_ref_record(source: dict[str, Any], target: dict[str, Any], label: str) -> dict[str, Any]:
    context = ref_context(source.get("latex_body", ""), label)
    return {
        "label": label,
        "role": classify_forward_ref(source, target, context),
        "target_type": target.get("type"),
        "target_line": target.get("line"),
        "line_distance": int(target.get("line", 0)) - int(source.get("line", 0)),
        "context": context,
    }


def appendix_teaser_ref_record(source: dict[str, Any], target: dict[str, Any], label: str) -> dict[str, Any]:
    context = ref_context(source.get("latex_body", ""), label)
    return {
        "label": label,
        "role": "appendix_teaser",
        "target_type": target.get("type"),
        "target_file": target.get("file"),
        "target_line": target.get("line"),
        "context": context,
    }


def classify_ref_role(
    source: dict[str, Any],
    target: dict[str, Any],
    label: str,
    context: str,
) -> str:
    """Heuristic intent role for any resolved reference.

    This is explanatory metadata. It does not, by itself, decide `depends_on`.
    """
    ctx = context.lower()

    if label in set(source.get("appendix_teaser_refs", [])):
        return "appendix_teaser"
    if label in set(source.get("forward_refs", [])):
        roles = {
            r.get("label"): r.get("role")
            for r in source.get("forward_ref_roles", [])
            if r.get("label")
        }
        return f"forward_{roles.get(label, 'teaser')}"
    if target.get("type") == "section" or source.get("type") == "section":
        return "navigation"
    if "cf.~" in ctx or "cf." in ctx:
        return "cf_near_match"
    if is_appendix_node(source) and not is_appendix_node(target) and any(
        phrase in ctx
        for phrase in (
            "statement of record",
            "canonical",
            "defers",
            "formal statement",
        )
    ):
        return "canonical_anchor"
    if target.get("type") == "proof":
        return "proof_support"
    if target.get("type") in {"definition", "axiom", "assumption"}:
        return "definition_anchor"
    if source.get("type") == "proof":
        return "proof_support"
    if any(
        phrase in ctx
        for phrase in (
            "application",
            "applied",
            "consequence",
            "instantiates",
            "variant",
            "extension",
        )
    ):
        return "application"
    if any(
        phrase in ctx
        for phrase in (
            "interpret",
            "bridge",
            "resonant",
            "dialogue",
            "in this light",
        )
    ):
        return "interpretive_bridge"
    return "formal_dependency"


def ref_role_record(source: dict[str, Any], target: dict[str, Any], label: str) -> dict[str, Any]:
    context = ref_context(source.get("latex_body", ""), label)
    role = classify_ref_role(source, target, label, context)
    logical_support = (
        role not in {"appendix_teaser", "navigation"}
        and not role.startswith("forward_")
        and target.get("type") != "section"
    )
    return {
        "label": label,
        "role": role,
        "target_type": target.get("type"),
        "target_file": target.get("file"),
        "target_line": target.get("line"),
        "logical_support": logical_support,
        "context": context,
    }


def mark_ref_roles(nodes: list[dict[str, Any]]) -> None:
    """Attach role records for all resolved citation edges."""
    by_label = {n["label"]: n for n in nodes if n.get("label")}
    for n in nodes:
        records = [
            ref_role_record(n, by_label[ref], ref)
            for ref in sorted(set(n.get("cites", [])))
            if ref in by_label
        ]
        if records:
            n["ref_roles"] = records


def mark_canonical_relationships(nodes: list[dict[str, Any]]) -> None:
    """Infer explicit canonical/expansion relationships from local prose."""
    by_label = {n["label"]: n for n in nodes if n.get("label")}
    for n in nodes:
        if not is_appendix_node(n):
            continue
        for record in n.get("ref_roles", []):
            if record.get("role") != "canonical_anchor":
                continue
            target_label = record.get("label")
            if not isinstance(target_label, str):
                continue
            target = by_label.get(target_label)
            if target is None:
                continue
            n["canonical_status"] = "expansion_of"
            n["canonical_target"] = target_label
            expansions = target.setdefault("canonical_expansions", [])
            if n.get("label") and n["label"] not in expansions:
                expansions.append(n["label"])
            target.setdefault("canonical_status", "canonical_statement")


def build_atlas() -> dict[str, Any]:
    main_text = MAIN.read_text(encoding="utf-8")
    macros = build_macros(main_text)
    macro_names = set(macros)

    nodes: list[dict[str, Any]] = []
    for path in sorted(SRC.rglob("*.tex")):
        # The invariant ledger is an internal artifact, distinct from Principia
        # Symbolica and not \input by main.tex. The atlas reflects PS only, so the
        # ledger/invariant index is excluded (the public and private PS coincide).
        if path.stem == "invariant_ledger":
            continue
        nodes.extend(extract_nodes(path.name, path.read_text(encoding="utf-8"), macro_names))

    # Enrich with resolved edges. Raw `refs` retain every source reference;
    # `cites` and `cited_by` contain only edges whose endpoint is an Atlas node.
    graph = graph_index(load_json(LABEL_GRAPH))
    by_label = {n["label"]: n for n in nodes if n["label"]}
    modeled_labels = set(by_label)
    for n in nodes:
        g = graph.get(n["label"])
        if g:
            n["cites"] = [label for label in g["cites"] if label in modeled_labels]
            n["cited_by"] = [label for label in g["cited_by"] if label in modeled_labels]
        else:
            n.setdefault("cites", [])
            n.setdefault("cited_by", [])

    # Proof linkage: attach proof labels back onto their result nodes.
    for n in nodes:
        if n["type"] == "proof" and n.get("proves"):
            target = by_label.get(n["proves"])
            if target is not None:
                target.setdefault("proof_labels", []).append(n["label"] or n["id"])

    mark_forward_refs(nodes)
    mark_appendix_teaser_refs(nodes)
    mark_ref_roles(nodes)
    mark_canonical_relationships(nodes)

    # Principia-direction dependency closure: what a node rests on is its own
    # references plus those of its proofs — in PS the statements are clean and
    # the dependencies live in the proofs. Following depends_on walks *toward*
    # the axiomata prima (the reference direction of the whole work).
    for n in nodes:
        non_support_refs = set(n.get("forward_refs", [])) | set(n.get("appendix_teaser_refs", []))
        deps: set[str] = set(n.get("cites", [])) - non_support_refs
        for pl in n.get("proof_labels", []):
            proof = by_label.get(pl, {})
            proof_non_support_refs = (
                set(proof.get("forward_refs", []))
                | set(proof.get("appendix_teaser_refs", []))
            )
            deps |= set(proof.get("cites", [])) - proof_non_support_refs
        deps.discard(n["label"])
        deps.difference_update(n.get("proof_labels", []))
        # depends_on is the logical closure (definitions/axioms/results), not
        # navigation: drop section pointers like "proved twice below §…".
        n["depends_on"] = sorted(
            d for d in deps
            if d in by_label and by_label[d]["type"] != "section"
        )

    # Honest proof taxonomy. We distinguish a *formal linked proof* from an
    # argument that is merely present (a demonstratio, or an inline "Proof:")
    # from a genuinely un-argued claim. A demonstratio is NEVER promoted to
    # "proven": its presence is reported as "argued" and left for human
    # rigor-classification — it may be a real proof, a worked example, or
    # circular. This is anti-masking in both directions: don't claim a proof
    # that isn't linked, don't hide an argument that is there.
    tiers = harvest_tiers(load_json(CERT_LEDGER))

    INLINE_PROOF = re.compile(r"\\(?:textbf|emph|textit|paragraph|textsc)\{\s*[Pp]roof")
    by_file: dict[str, list[dict[str, Any]]] = {}
    for n in nodes:
        by_file.setdefault(n["file"], []).append(n)
    inline_lbls: set[str] = set()
    adjacent_lbls: set[str] = set()
    for ns in by_file.values():
        ns.sort(key=lambda n: n["line"])
        for j, n in enumerate(ns):
            if n["type"] not in THEOREM_CLASS or not n["label"]:
                continue
            if INLINE_PROOF.search(n.get("latex_body", "")):
                inline_lbls.add(n["label"])
            for k in range(j + 1, len(ns)):   # next argument before next claim?
                t = ns[k]["type"]
                if t in THEOREM_CLASS:
                    break
                if t in ("proof", "demonstratio"):
                    adjacent_lbls.add(n["label"])
                    break

    for n in nodes:
        n["role"] = ROLE_MAP.get(n["type"], n["type"])
        if n["type"] in {"definition", "axiom", "assumption"}:
            n["proof_status"] = "definitional"
        elif n["type"] in THEOREM_CLASS:
            if n.get("proof_labels"):
                n["proof_status"] = "proven"              # formal \begin{proof}, linked
            elif n["label"] in inline_lbls:
                n["proof_status"] = "argued_inline"       # inline "Proof:" in the body
            elif n["label"] in adjacent_lbls:
                n["proof_status"] = "argued_demonstratio" # demonstratio/proof nearby, unlinked
            else:
                n["proof_status"] = "unproved"            # genuinely un-argued
        if n["label"] in tiers:
            n["certificate_tier"] = tiers[n["label"]]

    dependency_graph, dependency_scc_by_label = dependency_scc_report(nodes)
    for n in nodes:
        scc_id = dependency_scc_by_label.get(n.get("label", ""))
        if scc_id:
            n["dependency_scc"] = scc_id
            n["in_dependency_cycle"] = True

    if not LEAN_ALIGNMENT.is_file():
        raise RuntimeError("Lean alignment projection missing; run ci/build_lean_alignment.py first")
    alignment = load_json(LEAN_ALIGNMENT)
    if alignment.get("schema") != "principia-lean-alignment/v1":
        raise RuntimeError("unsupported Lean alignment schema")
    records_by_label: dict[str, list[dict[str, Any]]] = {}
    atlas_labels = {n.get("label") for n in nodes if n.get("label")}
    for record in alignment.get("records", []):
        label = record.get("atlas_label")
        if label not in atlas_labels:
            raise RuntimeError(f"Lean alignment label absent from Atlas: {label}")
        records_by_label.setdefault(label, []).append(record)
    for n in nodes:
        records = records_by_label.get(n.get("label", ""), [])
        if not records:
            continue
        witnesses = sorted({w["declaration"] for r in records for w in r.get("lean_witnesses", [])})
        countermodels = sorted({c for r in records for c in r.get("countermodels", [])})
        conditions = sorted({c for r in records for c in r.get("conditions", [])})
        notes = sorted({r.get("notes", "") for r in records if r.get("notes")})
        n["lean_alignment"] = {
            "record_ids": [r["id"] for r in records],
            "statuses": sorted({r["status"] for r in records}),
            "witnesses": witnesses,
            "countermodels": countermodels,
            "conditions": conditions,
            "notes": notes,
            "kernel_certified": any(r.get("kernel_certified") for r in records),
            "full_record": "bib/principia_lean_alignment.json",
        }

    nodes.sort(key=lambda n: (n["book"], n["file"], n["line"]))

    by_type: dict[str, int] = {}
    for n in nodes:
        by_type[n["type"]] = by_type.get(n["type"], 0) + 1
    by_matter_region: dict[str, int] = {}
    for n in nodes:
        region = n.get("matter_region")
        if region:
            by_matter_region[region] = by_matter_region.get(region, 0) + 1
    by_proof_status: dict[str, int] = {}
    for n in nodes:
        s = n.get("proof_status")
        if s:
            by_proof_status[s] = by_proof_status.get(s, 0) + 1
    forward_ref_count = sum(len(n.get("forward_refs", [])) for n in nodes)
    appendix_teaser_ref_count = sum(len(n.get("appendix_teaser_refs", [])) for n in nodes)
    by_forward_ref_role: dict[str, int] = {}
    for n in nodes:
        for r in n.get("forward_ref_roles", []):
            role = r.get("role")
            if role:
                by_forward_ref_role[role] = by_forward_ref_role.get(role, 0) + 1
    by_ref_role: dict[str, int] = {}
    for n in nodes:
        for r in n.get("ref_roles", []):
            role = r.get("role")
            if role:
                by_ref_role[role] = by_ref_role.get(role, 0) + 1
    canonical_relationship_count = sum(
        1 for n in nodes
        if n.get("canonical_status") == "expansion_of" and n.get("canonical_target")
    )

    lean_program = dict(alignment["lean_program"])
    lean_program.update({
        "alignment_artifact": "bib/principia_lean_alignment.json",
        "alignment_schema": alignment["schema"],
        "proof_surface_distinction": (
            "proof_status is manuscript-local LaTeX proof linkage; "
            "lean_alignment is independent kernel correspondence."
        ),
    })

    return {
        "meta": {
            "schema": "principia-atlas/1.1",
            "generated_at": datetime.datetime.now(datetime.timezone.utc)
                            .replace(microsecond=0).isoformat().replace("+00:00", "Z"),
            "total_nodes": len(nodes),
            "by_type": by_type,
            "by_matter_region": by_matter_region,
            "proof_status_counts": by_proof_status,
            "macro_count": len(macros),
            "forward_ref_count": forward_ref_count,
            "forward_ref_role_counts": by_forward_ref_role,
            "appendix_teaser_ref_count": appendix_teaser_ref_count,
            "ref_role_counts": by_ref_role,
            "canonical_relationship_count": canonical_relationship_count,
            "dependency_graph": {
                "node_count": dependency_graph["node_count"],
                "edge_count": dependency_graph["edge_count"],
                "scc_count": dependency_graph["scc_count"],
                "nontrivial_scc_count": dependency_graph["nontrivial_scc_count"],
                "largest_scc_size": dependency_graph["largest_scc_size"],
                "largest_nontrivial_scc_size": dependency_graph["largest_nontrivial_scc_size"],
            },
            "encoding": {
                "source_encoding": "UTF-8 strict",
                "json_encoding": "UTF-8",
                "unicode_policy": "Code points are preserved. Do not infer mojibake from terminal rendering; verify bytes or code points.",
                "audit": "python ci/check_encoding.py",
            },
            "note": "Math is verbatim LaTeX. Traverse by 'cites'/'cited_by'. "
                    "Resolve custom control sequences via 'macros'. Same-file references "
                    "to later labels are preserved as 'forward_refs' but excluded from "
                    "'depends_on'. Main-text references into appendices are preserved "
                    "as 'appendix_teaser_refs' but excluded from 'depends_on'. All resolved "
                    "references carry explanatory 'ref_roles'. proof_status "
                    "distinguishes proven (formal linked proof) from argued_inline / "
                    "argued_demonstratio (an argument is present but not a formal linked "
                    "proof — needs rigor classification) from unproved (un-argued).",
        },
        "macros": macros,
        "lean_program": lean_program,
        "dependency_graph": dependency_graph,
        "nodes": nodes,
    }


def normalized(atlas: dict[str, Any]) -> str:
    """Serialization for drift comparison: ignore the timestamp."""
    clone = json.loads(json.dumps(atlas))
    clone.get("meta", {}).pop("generated_at", None)
    return json.dumps(clone, sort_keys=True, ensure_ascii=False)


README = """\
# Principia Symbolica — Atlas for Machine Readers

`principia_atlas.json` is the canonical LLM-facing artifact. Read it, not the
PDF: the PDF's text layer mangles math, loses structure, and cannot be
traversed. The atlas keeps every claim as an addressable node with its
**verbatim LaTeX body** and **resolved dependency edges**.

## Two proof surfaces

`proof_status` is manuscript-local: it reports whether the LaTeX statement has a
linked manuscript proof. It does **not** claim Lean certification.

`lean_alignment` is the independent kernel-correspondence surface. For a mapped
node, follow `lean_alignment.record_ids` into
`bib/principia_lean_alignment.json`, then follow each full record's
`lean_witnesses[].source` and `lean_witnesses[].declaration` into the Sketched
Lean program at the exact `lean_program.commit`. `conditional`, `refuted`,
`open_bridge`, `interpretive`, and `poetic` are distinct statuses. A countermodel
bounds the named implication; it is not an open proof. Interpretive prose and
operator poetry are not failed theorem mappings. Lean constrains formal claims
without replacing Principia's semantic or literary layer.

## Schema
- `meta` — counts and provenance.
- `macros` — `{name: {expansion, arity}}`. Custom control sequences in any
  body (e.g. `\\\\drift`, `\\\\Obs`, `\\\\freeenergy`) resolve here.
- `nodes[]` — one per labelled object:
  - `label`, `type` (verbatim env, including Newton-Latin: demonstratio, propositio, …),
  - `role` — canonical type over the Latin/English split (demonstratio→demonstration,
    propositio→proposition; otherwise identity),
  - `name` (display title), `book`, `matter_region`, `matter_role`, `file`, `line`,
  - `latex_body` — the full `\\begin{env}…\\end{env}`, verbatim,
  - `macros_used` — custom macros appearing in the body (look them up in `macros`),
  - `refs` — labels referenced from the body,
  - `cites` / `cited_by` — resolved dependency edges,
  - `forward_refs` — same-file references to later labels; preserved as reader
    navigation / teasers and excluded from `depends_on`,
  - `forward_ref_roles` — one record per forward ref with `role`, target type,
    line distance, and a short context snippet,
  - `appendix_teaser_refs` — main-text references into appendix files; preserved
    as reader-facing appendix pointers and excluded from `depends_on`,
  - `appendix_teaser_ref_roles` — one record per appendix teaser ref with target
    type, target file/line, and context,
  - `ref_roles` — one record per resolved reference with `role`, target
    type/file/line, `logical_support`, and a short context snippet. This is
    citation-intent metadata; it explains why an edge exists without silently
    rewriting the proof graph,
  - `depends_on` — what this node rests on (its `cites` ∪ its proofs' `cites`);
    follow it to walk toward the axiomata prima after reader-navigation refs are
    removed,
  - `canonical_status`, `canonical_target`, `canonical_expansions` — present
    when local prose explicitly marks one node as the formal statement of record
    and another as an appendix expansion/defense,
  - `proof_labels` — proofs of this result (for theorem-class nodes),
  - `proves` — the result a proof node proves,
  - `proof_status` — for theorem-class nodes, one of:
      `proven` (a formal `\\begin{proof}` is linked to it);
      `argued_inline` (the statement carries an inline "Proof:" in its own body);
      `argued_demonstratio` (a `demonstratio`/proof sits adjacent but is not a
        formally linked proof — an argument is present, rigor not yet classified;
        it may be a real proof, a worked example, or circular);
      `unproved` (genuinely un-argued);
      and `definitional` for definitions/axioms/assumptions,
  - `certificate_tier` — witnessed tier (A/B/C), when present,
  - `dependency_scc` / `in_dependency_cycle` — present only when a node belongs
    to a nontrivial strongly connected component of the `depends_on` graph.
- `dependency_graph` — graph-level dependency audit:
  - direction is `node -> depends_on` (toward foundations),
  - `components[]` lists every nontrivial strongly connected component with its
    labels and internal edges, so circularity claims can be checked directly.

## Encoding contract
The atlas is generated from strict UTF-8 source reads and written as UTF-8 JSON
with Unicode code points preserved. If a Windows terminal displays a dash,
arrow, or Greek symbol as apparent mojibake, do not edit the manuscript from
that rendering. Verify with `python ci/check_encoding.py` or inspect code points
directly.

## How to teleport
1. Jump to a node by `label` (no linear reading).
2. To understand it, pull its `latex_body`, expand any `macros_used`, then
   follow `cites` one hop for its dependency closure.
3. For a theorem, read its `proof_labels` nodes; `proof_status` tells you whether
   a formal proof is linked (`proven`), an argument is merely present but unclassified
   (`argued_inline` / `argued_demonstratio`), or the claim is un-argued (`unproved`).
4. Before accepting a circularity audit, check `dependency_graph.components`;
   those are the actual strongly connected components of the atlas dependency
   graph.

## Citation geometry (read this)
Principia Symbolica references in the *opposite* direction from most academic
work: not outward to prior literature, but inward toward the **axiomata prima**
(the first axioms). So `depends_on` / `cites` point *down* toward the
foundations, and `cited_by` points *up* toward what builds on a node. A few
references intentionally run the other way — most notably back-references to the
appendices from the main books — and are not errors. Main-text references into
appendices are `appendix_teaser_refs`: they remain in `cites` for navigation, but
do not create `depends_on` edges. Appendix-to-main references still count as
canonical anchors.

`matter_region` keeps the manuscript architecture visible to machine readers:
`mainmatter` carries the canonical books and Book I Scholium; `appendix` carries
expanded derivations and defenses; `operator_poetry` carries Operatio,
Integratio, Temperatio, and Executio as one operator-poetic mode; `ledger` carries
bookkeeping. Do not flatten these regions into one proof surface.

The poetry is not stripped and the silence is not hidden: the Latin prelude
sections (Operatio, Temperatio, Executio, …) are present as `section` nodes with
their bodies, and unproven results are marked honestly — `proof_status` separates
a formally proven claim from one that is merely `argued` from one that is
`unproved` — rather than dressed up.

Regenerated by `ci/build_llm_atlas.py` (in `make snapshot`); CI drift-guards it
with `--check`, so it never goes stale relative to `src/`.
"""


def main() -> None:
    ap = argparse.ArgumentParser(description="Build the LLM atlas for Principia Symbolica.")
    ap.add_argument("--check", action="store_true",
                    help="Drift guard: exit 1 if the on-disk atlas is stale, 0 if current.")
    args = ap.parse_args()

    if not SRC.exists():
        print(f"ERROR: src not found at {SRC}")
        sys.exit(2)

    atlas = build_atlas()

    if args.check:
        if not OUT_JSON.exists():
            print("STALE: bib/principia_atlas.json does not exist — run build_llm_atlas.py")
            sys.exit(1)
        current = load_json(OUT_JSON)
        if normalized(current) != normalized(atlas):
            print("STALE: atlas does not match current src — re-run ci/build_llm_atlas.py")
            sys.exit(1)
        print("OK: atlas is current")
        sys.exit(0)

    OUT_JSON.write_text(json.dumps(atlas, indent=2, ensure_ascii=False), encoding="utf-8")
    OUT_README.write_text(README, encoding="utf-8")

    m = atlas["meta"]
    print(f"Atlas written to {OUT_JSON}")
    print(f"  nodes : {m['total_nodes']}")
    print(f"  macros: {m['macro_count']}")
    if m.get("by_matter_region"):
        print("  matter regions:")
        for region, count in sorted(m["by_matter_region"].items(), key=lambda x: (-x[1], x[0])):
            print(f"    {region:<24} {count}")
    print(f"  forward refs: {m.get('forward_ref_count', 0)}")
    print(f"  appendix teaser refs: {m.get('appendix_teaser_ref_count', 0)}")
    print(f"  canonical expansions: {m.get('canonical_relationship_count', 0)}")
    if m.get("forward_ref_role_counts"):
        for role, count in sorted(m["forward_ref_role_counts"].items(), key=lambda x: (-x[1], x[0])):
            print(f"    {role:<24} {count}")
    if m.get("ref_role_counts"):
        print("  ref roles:")
        for role, count in sorted(m["ref_role_counts"].items(), key=lambda x: (-x[1], x[0])):
            print(f"    {role:<24} {count}")
    for t, n in sorted(m["by_type"].items(), key=lambda x: -x[1]):
        print(f"  {t:<14} {n}")
    print("  proof status:")
    for s, n in sorted(m.get("proof_status_counts", {}).items(), key=lambda x: -x[1]):
        print(f"    {s:<22} {n}")
    dg = m.get("dependency_graph", {})
    if dg:
        print("  dependency graph:")
        print(f"    edges                  {dg.get('edge_count', 0)}")
        print(f"    nontrivial SCCs        {dg.get('nontrivial_scc_count', 0)}")
        print(f"    largest nontrivial SCC {dg.get('largest_nontrivial_scc_size', 0)}")


if __name__ == "__main__":
    main()
