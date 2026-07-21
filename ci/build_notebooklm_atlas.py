#!/usr/bin/env python3
"""Export the LLM atlas as NotebookLM-friendly Markdown.

NotebookLM accepts Markdown more reliably than JSON. This exporter preserves the
atlas' source discipline while turning each node into a readable card:
label, type, book, source location, proof status, dependency/support links,
downstream uses, macros, and a cleaned statement body.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "bib" / "principia_atlas.json"
OUT = ROOT / "bib" / "notebooklm_atlas"

BOOK_ORDER = [
    "scholium_symbolicum",
    "book1",
    "book2",
    "book3",
    "book4",
    "book5",
    "book6",
    "book7",
    "book8",
    "book9",
    "appendix_abstracts",
    "appendix_symbolic_reflexive_validation",
    "appendix_dual_horizon",
    "appendix_dictionary",
    "appendix_symbolic_framing",
    "operatio",
    "executio",
]

LATEX_COMMAND_1 = re.compile(r"\\(?:emph|textbf|textit|texttt|mathrm|mathbf|mathcal|operatorname)\{([^{}]*)\}")
REF = re.compile(r"\\(?:ref|eqref|autoref)\{([^{}]+)\}")
HYPERREF = re.compile(r"\\hyperref\[([^\]]+)\]\{([^{}]*)\}")
LABEL = re.compile(r"\\label\{[^{}]+\}")
BEGIN_END = re.compile(r"\\(?:begin|end)\{[^{}]+\}(?:\[[^\]]*\])?")
COMMENT = re.compile(r"(?<!\\)%.*")


def load_atlas(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def md_escape(text: Any) -> str:
    return str(text or "").replace("|", "\\|").strip()


def first_sentence(text: str, limit: int = 420) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit]
    end = max(cut.rfind(". "), cut.rfind("; "), cut.rfind("). "))
    if end > 120:
        return cut[: end + 1].strip()
    return cut.rstrip() + "..."


def clean_latex(text: str) -> str:
    """Light LaTeX-to-readable text pass.

    This intentionally does not try to understand all math. It removes structural
    wrappers and keeps labels/refs visible as plain label ids.
    """
    text = COMMENT.sub("", text)
    text = HYPERREF.sub(lambda m: f"{m.group(2)} ({m.group(1)})", text)
    text = REF.sub(lambda m: m.group(1), text)
    text = LABEL.sub("", text)
    text = BEGIN_END.sub("", text)
    prev = None
    while prev != text:
        prev = text
        text = LATEX_COMMAND_1.sub(lambda m: m.group(1), text)
    replacements = {
        r"\noindent": "",
        r"\leavevmode": "",
        r"\newline": "\n",
        r"\medskip": "\n",
        r"\smallskip": "\n",
        r"\quad": " ",
        r"\qquad": " ",
        r"\,": " ",
        r"\;": " ",
        r"\:": " ",
        r"\{": "{",
        r"\}": "}",
        r"\_": "_",
        "---": "-",
        "--": "-",
        "~": " ",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"\\item(?:\[[^\]]+\])?", "\n- ", text)
    text = re.sub(r"\\[a-zA-Z]+", lambda m: m.group(0).lstrip("\\"), text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def link_list(ids: list[str], names: dict[str, str], limit: int | None) -> str:
    if not ids:
        return "none"
    parts = []
    shown = ids if limit is None else ids[:limit]
    for label in shown:
        name = names.get(label, label)
        parts.append(f"`{label}` ({name})" if name != label else f"`{label}`")
    if limit is not None and len(ids) > limit:
        parts.append(f"... +{len(ids) - limit} more")
    return "; ".join(parts)


def node_heading(node: dict[str, Any]) -> str:
    name = node.get("name") or node["id"]
    role = node.get("role") or node.get("type") or "node"
    return f"### {name} (`{node['id']}`)\n\nRole: `{role}` | Type: `{node.get('type', '')}` | Book: `{node.get('book', '')}` | Source: `{node.get('file', '')}:{node.get('line', '')}`"


def node_card(
    node: dict[str, Any],
    names: dict[str, str],
    body_limit: int | None,
    relation_limit: int | None,
    include_raw_latex: bool = False,
) -> str:
    body = clean_latex(node.get("latex_body", ""))
    if body_limit is not None:
        body = first_sentence(body, body_limit)
    proof = node.get("proof_status") or "not_applicable"
    macros = ", ".join(f"`\\{m}`" for m in node.get("macros_used", [])[:24]) or "none"
    if len(node.get("macros_used", [])) > 24:
        macros += f", ... +{len(node['macros_used']) - 24} more"

    lines = [
        node_heading(node),
        "",
        f"- Proof status: `{proof}`",
        f"- Depends on: {link_list(node.get('depends_on', []), names, relation_limit)}",
        f"- Cites: {link_list(node.get('cites', []), names, relation_limit)}",
        f"- Cited by: {link_list(node.get('cited_by', []), names, relation_limit)}",
        f"- Macros used: {macros}",
        "",
        "**Statement / Body**",
        "",
        body or "(no body text extracted)",
        "",
    ]
    alignment = node.get("lean_alignment")
    if alignment:
        insert_at = lines.index("**Statement / Body**")
        lean_lines = [
            "### Lean correspondence",
            "",
            f"- Status: {", ".join(f"`{x}`" for x in alignment.get("statuses", []))}",
            f"- Records: {", ".join(f"`{x}`" for x in alignment.get("record_ids", []))}",
            "- Witnesses: " + (", ".join(f"`{x}`" for x in alignment.get("witnesses", [])) or "none"),
            "- Countermodels: " + (", ".join(f"`{x}`" for x in alignment.get("countermodels", [])) or "none"),
        ]
        if alignment.get("conditions"):
            lean_lines.append("- Conditions: " + "; ".join(alignment["conditions"]))
        if alignment.get("notes"):
            lean_lines.append("- Formal boundary: " + " ".join(alignment["notes"]))
        lean_lines.extend(["", "Manuscript `proof_status` and Lean correspondence are independent.", ""])
        lines[insert_at:insert_at] = lean_lines
    if include_raw_latex:
        raw = node.get("latex_body", "").strip()
        if raw:
            lines.extend([
                "**Verbatim LaTeX Body**",
                "",
                "```latex",
                raw,
                "```",
                "",
            ])
    return "\n".join(lines)


def rendered_markdown(content: str) -> str:
    normalized = "\n".join(line.rstrip() for line in content.splitlines())
    return normalized.rstrip() + "\n"


def write_markdown(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(rendered_markdown(content), encoding="utf-8")


def book_sort_key(book: str) -> tuple[int, str]:
    if book in BOOK_ORDER:
        return (BOOK_ORDER.index(book), book)
    return (len(BOOK_ORDER), book)


def lean_summary_lines(atlas: dict[str, Any]) -> list[str]:
    lean = atlas.get("lean_program") or {}
    counts = lean.get("status_counts") or {}
    rendered_counts = ", ".join(f"{key}={value}" for key, value in sorted(counts.items()))
    return [
        f"- Lean program commit: `{lean.get('commit', 'unavailable')}`",
        f"- Receipted Lean declarations: {lean.get('receipted_declarations', 0)}",
        f"- Checked bindings: {lean.get('checked_bindings', 0)}",
        f"- Mapped Atlas nodes: {lean.get('mapped_atlas_anchors', 0)}",
        f"- Lean status counts: {rendered_counts or 'none'}",
        "- `proof_status` is manuscript-local; `lean_alignment.statuses` is independent kernel correspondence.",
    ]


def build_agents(atlas: dict[str, Any], by_book: dict[str, list[dict[str, Any]]]) -> str:
    summary = "\n".join(lean_summary_lines(atlas))
    return f"""# Principia Symbolica Atlas for Machine Readers

Generated from `bib/principia_atlas.json`. Nodes: {len(atlas['nodes'])}.
Source groups: {len(by_book)}.

## Two proof surfaces

`proof_status` reports only manuscript-local LaTeX proof linkage. It is not a
Lean receipt. `lean_alignment.statuses` reports the separate typed correspondence
to the committed Sketched Lean program.

{summary}

## Traversal

1. Locate a Principia node by label.
2. Read its manuscript `proof_status`, body, and book dependencies.
3. If `lean_alignment` exists, follow its `record_ids` into
   `../principia_lean_alignment.json`.
4. Follow each `lean_witnesses[].source` and `.declaration` at the recorded
   Sketched commit. Inspect `conditions`, `countermodels`, and `bounds` before
   treating the result as exact.
5. Keep `conditional`, `refuted`, `open_bridge`, `interpretive`, and `poetic`
   distinct. A refuted implication is not awaiting proof. Interpretive prose and
   operator poetry are not failed theorem mappings.

Lean constrains formal claims; it does not replace Principia's semantic or
literary layer. Unmapped is an honest correspondence state.
"""

def build_readme(atlas: dict[str, Any], by_book: dict[str, list[dict[str, Any]]]) -> str:
    counts = Counter(node.get("role") or node.get("type") for node in atlas["nodes"])
    book_rows = "\n".join(
        f"| `{book}` | {len(nodes)} |"
        for book, nodes in sorted(by_book.items(), key=lambda item: book_sort_key(item[0]))
    )
    role_rows = "\n".join(f"| `{role}` | {count} |" for role, count in counts.most_common())
    lean_summary = "\n".join(lean_summary_lines(atlas))
    return f"""# Principia Symbolica Atlas for NotebookLM

Generated from `bib/principia_atlas.json`.

Use these Markdown files in NotebookLM instead of uploading the JSON atlas directly.
The JSON remains the canonical machine artifact; this folder is a reading/export
layer for tools that prefer Markdown.

## Recommended Upload Set

1. `principia_atlas_notebooklm_full.md` - full-fidelity all-node atlas with
   complete relation lists and verbatim LaTeX blocks.
2. `books/book1.md` through `books/book9.md` - full-fidelity per-book chunks.
3. Relevant appendix files from `books/` when needed.
4. `principia_atlas_notebooklm_compact.md` only when you want a smaller index
   source before uploading the full chunks.

## Reading Rules

- Labels are shown in backticks, e.g. `definition:bk1_bounded_observer`.
- `Depends on` points toward support/foundations.
- `Cited by` points toward later uses.
- `Proof status` is manuscript-local LaTeX proof linkage, not Lean certification.
- `lean_alignment.statuses` is the independent kernel-correspondence status.
- Follow `lean_alignment.record_ids` into `../principia_lean_alignment.json`, then follow each receipted declaration into Sketched.
- Conditional, refuted, open, interpretive, and poetic statuses are distinct.
- Operator poetry is intentional source material, not an unmapped theorem failure.
- The statement/body is cleaned for reading; consult the LaTeX source for exact typography.

## Lean Program

{lean_summary}

## Atlas Counts

- Nodes: {len(atlas["nodes"])}
- Books / source groups: {len(by_book)}
- Dependency components: {len(atlas.get("dependency_graph", {}).get("components", []))}

## Nodes by Source Group

| Source group | Nodes |
|---|---:|
{book_rows}

## Nodes by Role

| Role | Count |
|---|---:|
{role_rows}
"""


def build_compact(atlas: dict[str, Any], names: dict[str, str]) -> str:
    meta = atlas.get("meta", {})
    lines = [
        "# Principia Symbolica Atlas - NotebookLM Compact Export",
        "",
        "This is a compact Markdown rendering of `bib/principia_atlas.json`.",
        "Use labels in backticks as stable source addresses.",
        "",
        "## Metadata",
        "",
        f"- Nodes: {len(atlas['nodes'])}",
        *lean_summary_lines(atlas),
        f"- Generated from atlas metadata: `{meta.get('generated_at', 'unknown')}`",
        f"- Dependency direction: node -> depends_on, toward foundations.",
        "",
        "## Nodes",
        "",
    ]
    for node in atlas["nodes"]:
        lines.append(node_card(node, names, body_limit=520, relation_limit=6))
    return "\n".join(lines)


def build_full(atlas: dict[str, Any], names: dict[str, str], include_raw_latex: bool) -> str:
    meta = atlas.get("meta", {})
    lines = [
        "# Principia Symbolica Atlas - NotebookLM Full-Fidelity Export",
        "",
        "This is the high-fidelity Markdown rendering of `bib/principia_atlas.json`.",
        "It keeps full cleaned node bodies and complete dependency/citation lists.",
        "If present, verbatim LaTeX blocks preserve the exact source body from the atlas.",
        "",
        "## Metadata",
        "",
        f"- Nodes: {len(atlas['nodes'])}",
        *lean_summary_lines(atlas),
        f"- Generated from atlas metadata: `{meta.get('generated_at', 'unknown')}`",
        "- Dependency direction: node -> depends_on, toward foundations.",
        "- Proof status is local atlas status, not external acceptance.",
        "",
        "## Nodes",
        "",
    ]
    for node in atlas["nodes"]:
        lines.append(node_card(node, names, body_limit=None, relation_limit=None, include_raw_latex=include_raw_latex))
    return "\n".join(lines)


def build_book_file(
    book: str,
    nodes: list[dict[str, Any]],
    names: dict[str, str],
    include_raw_latex: bool,
    lean_program: dict[str, Any],
) -> str:
    lines = [
        f"# Principia Symbolica NotebookLM Atlas - {book}",
        "",
        f"Nodes in this source group: {len(nodes)}",
        *lean_summary_lines({"lean_program": lean_program}),
        "",
        "Each card preserves label, role, source location, proof status, complete supports, complete uses, macros, and full cleaned body text.",
        "When enabled, verbatim LaTeX appears after the readable body for exact-source recovery.",
        "",
    ]
    for node in nodes:
        lines.append(node_card(node, names, body_limit=None, relation_limit=None, include_raw_latex=include_raw_latex))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Build NotebookLM-friendly Markdown from principia_atlas.json")
    parser.add_argument("--atlas", type=Path, default=ATLAS)
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--check", action="store_true", help="verify generated Markdown without rewriting")
    parser.add_argument(
        "--no-raw-latex",
        action="store_true",
        help="omit verbatim LaTeX blocks from full exports",
    )
    args = parser.parse_args()

    atlas = load_atlas(args.atlas)
    names = {node["id"]: node.get("name") or node["id"] for node in atlas["nodes"]}

    by_book: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for node in atlas["nodes"]:
        by_book[node.get("book") or "unknown"].append(node)
    for nodes in by_book.values():
        nodes.sort(key=lambda node: (str(node.get("file", "")), int(node.get("line") or 0), node["id"]))

    out = args.out
    include_raw_latex = not args.no_raw_latex
    expected: dict[Path, str] = {
        Path("AGENTS.md"): build_agents(atlas, by_book),
        Path("README.md"): build_readme(atlas, by_book),
        Path("principia_atlas_notebooklm_compact.md"): build_compact(atlas, names),
        Path("principia_atlas_notebooklm_full.md"): build_full(
            atlas, names, include_raw_latex=include_raw_latex
        ),
    }
    for book, nodes in sorted(by_book.items(), key=lambda item: book_sort_key(item[0])):
        expected[Path("books") / f"{book}.md"] = build_book_file(
            book, nodes, names, include_raw_latex=include_raw_latex,
            lean_program=atlas.get("lean_program") or {},
        )

    if args.check:
        expected_paths = {path.as_posix() for path in expected}
        actual_paths = {path.relative_to(out).as_posix() for path in out.rglob("*.md")}
        if actual_paths != expected_paths:
            print(f"STALE: NotebookLM file set differs: expected={len(expected_paths)} actual={len(actual_paths)}")
            return 1
        stale = [
            path.as_posix() for path, content in expected.items()
            if (out / path).read_text(encoding="utf-8") != rendered_markdown(content)
        ]
        if stale:
            print("STALE: NotebookLM outputs differ: " + ", ".join(stale))
            return 1
        if len(atlas["nodes"]) != atlas.get("meta", {}).get("total_nodes"):
            print("STALE: canonical Atlas node counts disagree")
            return 1
        print(f"OK: NotebookLM current ({len(atlas['nodes'])} nodes / {len(by_book)} source groups)")
        return 0

    for path, content in expected.items():
        write_markdown(out / path, content)
    print(f"Wrote NotebookLM atlas Markdown to {out}")
    print(f"  compact: {out / 'principia_atlas_notebooklm_compact.md'}")
    print(f"  full: {out / 'principia_atlas_notebooklm_full.md'}")
    print(f"  book files: {len(by_book)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
