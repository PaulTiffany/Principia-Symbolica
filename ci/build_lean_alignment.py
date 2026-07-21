#!/usr/bin/env python3
"""Generate Principia's cross-repository Lean correspondence projection."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "bib" / "principia_atlas.json"
OUT = ROOT / "bib" / "principia_lean_alignment.json"
DEFAULT_SKETCHED = Path(r"C:\src\sketched")
DEFAULT_PRINCIPIA_REPO = Path(r"C:\Users\paulc\projects\Principia-Symbolica")
STATUSES = ("exact", "constructed", "conditional", "refuted", "open_bridge", "interpretive", "poetic")
MAP_STATUS = {"proved-kernel": "exact", "proved": "exact", "definition": "constructed", "conditional": "conditional", "partial": "open_bridge"}
NEGATIVE = ("counterexample", "countermodel", "does_not", "not_force", "not_imply", "insufficient", "refute", "fails", "failure", "without_", "not_injective", "noninjective")
REGISTRIES = (
    "verification/bindings.json", "verification/leanps_ledger.json",
    "verification/source_obligations.json", "verification/ps_alignment.json",
    "verification/ps_alignment_review.json", "verification/book7_lean_map.json",
    "verification/flattening_audit.json", "selfcompile/lean_receipt.json",
)


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def registry_text(value: Any, fallback: str = '') -> str:
    """Keep corrupted legacy registry prose out of public generated artifacts."""
    text = value if isinstance(value, str) else ''
    if any(marker in text for marker in tuple(chr(code) for code in (0x00C3, 0x00C2, 0x0192, 0x00C6)) + (chr(0x00E2) + chr(0x20AC),)):
        return fallback
    return text


def statement_sha(text: str) -> str:
    body = re.sub(r"(?<!\\)%.*", "", text)
    body = re.sub(r"\\label\{[^}]*\}", "", body)
    return hashlib.sha256(re.sub(r"\s+", " ", body).strip().encode()).hexdigest()[:12]


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True,
                          text=True, encoding="utf-8").stdout.strip()


def committed_head(root: Path, paths: list[str] | None = None) -> str:
    if git(root, "rev-parse", "--is-inside-work-tree") != "true":
        raise ValueError(f"not a Git worktree: {root}")
    if paths:
        dirty = git(root, "status", "--short", "--", *paths)
        if dirty:
            raise ValueError(f"registry inputs are not committed in {root}:\n{dirty}")
    return git(root, "rev-parse", "HEAD")


def source_tree_sha() -> str:
    digest = hashlib.sha256()
    for path in sorted((ROOT / "src").rglob("*.tex")):
        if path.is_file() and path.name != "invariant_ledger.tex":
            digest.update(path.relative_to(ROOT).as_posix().encode() + b"\0" + path.read_bytes() + b"\0")
    return digest.hexdigest()


def binding_id(binding: dict[str, Any]) -> str:
    key = "\0".join(str(binding.get(k, "")) for k in ("artifact", "declares", "math_id", "statement_sha"))
    return "BIND-" + hashlib.sha256(key.encode()).hexdigest()[:16]


def role(name: str, status: str, countermodels: set[str]) -> str:
    low = name.casefold()
    if name in countermodels or any(x in low for x in NEGATIVE): return "countermodel"
    if status == "constructed" or any(x in low for x in ("construct", ".of", "to_")): return "constructor"
    if any(x in low for x in ("transport", "lower", "partialtrace")): return "transport"
    return "main_result"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sketched-root", type=Path, default=DEFAULT_SKETCHED)
    ap.add_argument("--principia-repo", type=Path, default=DEFAULT_PRINCIPIA_REPO)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    sketched, principia_repo = args.sketched_root.resolve(), args.principia_repo.resolve()
    maps = sorted((sketched / "verification").glob("*_lean_map.json"))
    registry_rels = sorted(set(REGISTRIES) | {p.relative_to(sketched).as_posix() for p in maps})
    for rel in registry_rels:
        if not (sketched / rel).is_file(): raise ValueError(f"required registry missing: {rel}")
    sketched_sha = committed_head(sketched, registry_rels)
    committed_head(principia_repo)
    principia_sha = git(principia_repo, "log", "-1", "--format=%H", "--", "src")

    atlas = load(ATLAS)
    labeled_nodes = [n for n in atlas["nodes"] if n.get("label")]
    nodes = {n["label"]: n for n in labeled_nodes}
    if len(nodes) != len(labeled_nodes): raise ValueError("duplicate nonempty Atlas labels")
    source_shas = {k: statement_sha(v.get("latex_body", "")) for k, v in nodes.items()}

    bindings_doc = load(sketched / "verification/bindings.json")
    bindings = bindings_doc["bindings"]
    by_anchor: dict[str, list[dict[str, Any]]] = defaultdict(list)
    seen_bindings: set[str] = set()
    for raw in bindings:
        bid = binding_id(raw)
        if bid in seen_bindings: raise ValueError(f"duplicate binding: {bid}")
        seen_bindings.add(bid)
        item = {**raw, "_id": bid}; by_anchor[item["math_id"]].append(item)
        if item.get("source") == "principia":
            anchor = item["math_id"]
            if anchor not in source_shas: raise ValueError(f"binding Atlas label absent: {anchor}")
            if item.get("statement_sha") != source_shas[anchor]:
                raise ValueError(f"source statement hash disagreement: {anchor}")

    receipt = load(sketched / "selfcompile/lean_receipt.json")
    rows = receipt["theorems"]
    if receipt.get("verified") != len(rows) or any(x.get("sorry") for x in rows):
        raise ValueError("invalid Lean receipt counts or sorry")
    receipt_by_name = {x["name"]: x for x in rows}
    if len(receipt_by_name) != len(rows): raise ValueError("duplicate receipt declaration")
    lean_files: dict[str, list[Path]] = defaultdict(list)
    for path in (sketched / "verification/lean").rglob("*.lean"):
        if ".lake" not in path.parts: lean_files[path.name].append(path)

    ledger = load(sketched / "verification/leanps_ledger.json")["entries"]
    ledger_by_decl: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in ledger:
        for declaration in entry.get("declares") or []: ledger_by_decl[declaration].append(entry)
    obligations_by_anchor: dict[str, list[str]] = defaultdict(list)
    for entry in load(sketched / "verification/source_obligations.json")["obligations"]:
        if entry.get("source_anchor"): obligations_by_anchor[entry["source_anchor"]].append(entry["id"])

    def ledger_rows(name: str) -> list[dict[str, Any]]:
        all_rows = ledger_by_decl.get(name, []) + ledger_by_decl.get(name.rsplit(".", 1)[-1], [])
        return list({x["id"]: x for x in all_rows}.values())

    def make_witness(name: str, status: str, cms: set[str]) -> dict[str, Any]:
        row = receipt_by_name.get(name)
        if row is None: raise ValueError(f"mapped Lean declaration absent from receipt: {name}")
        candidates = lean_files.get(row["file"], [])
        if len(candidates) != 1: raise ValueError(f"receipt source {row['file']} resolves to {len(candidates)} files")
        ledgers = ledger_rows(name)
        return {"declaration": name, "source": candidates[0].relative_to(sketched).as_posix(),
                "role": role(name, status, cms), "receipted": True,
                "receipt_status": row.get("status"), "axioms": row.get("axioms") or [],
                "ledger_ids": sorted(x["id"] for x in ledgers),
                "conditions": sorted(filter(None, (registry_text(h) for x in ledgers for h in (x.get("hypotheses") or []))))}

    records: list[dict[str, Any]] = []
    omitted: list[dict[str, Any]] = []
    for path in maps:
        for index, entry in enumerate(load(path).get("entries") or [], 1):
            anchor, coverage = entry["atlas_id"], entry.get("coverage")
            if anchor not in nodes: raise ValueError(f"coverage Atlas label absent: {anchor}")
            if coverage not in MAP_STATUS: raise ValueError(f"unknown coverage status: {coverage}")
            status = MAP_STATUS[coverage]
            names = [n for n in entry.get("lean") or [] if n in receipt_by_name]
            absent = [n for n in entry.get("lean") or [] if n not in receipt_by_name]
            if not names:
                omitted.append({"atlas_label": anchor, "map": path.name, "declarations": absent}); continue
            cms = {n for n in names if role(n, status, set()) == "countermodel"}
            witnesses = [make_witness(n, status, cms) for n in names]
            conditions = sorted({h for w in witnesses for h in w["conditions"]})
            if status == "conditional" and not conditions:
                conditions = ["See the receipted theorem statement and coverage note for explicit premises."]
            records.append({"id": f"MAP-{path.stem.upper().replace('_LEAN_MAP', '')}-{index:03d}",
                "atlas_label": anchor, "status": status, "coverage_status": coverage,
                "kernel_certified": status not in {"open_bridge", "interpretive", "poetic"},
                "binding_ids": sorted(x["_id"] for x in by_anchor.get(anchor, [])),
                "lean_witnesses": witnesses, "conditions": conditions,
                "countermodels": sorted(cms), "source_statement_sha": source_shas[anchor],
                "source_obligations": sorted(obligations_by_anchor.get(anchor, [])),
                "notes": registry_text(entry.get("note"), "See the committed source registry for the original coverage note."), "source_registry": path.relative_to(sketched).as_posix(),
                "unreceipted_supports_omitted": absent})

    alignment = load(sketched / "verification/ps_alignment.json")
    for entry in alignment["entries"]:
        anchor = entry["atlas_id"]; status = "refuted" if entry["status"] == "countermodel" else entry["status"]
        if anchor not in nodes or status not in STATUSES: raise ValueError(f"invalid reviewed mapping {entry['id']}")
        if entry.get("source_statement_sha") != source_shas[anchor]: raise ValueError(f"reviewed hash disagreement: {entry['id']}")
        cms = set(entry.get("countermodels") or [])
        names = list(dict.fromkeys((entry.get("lean_witnesses") or []) + list(cms)))
        if status == "refuted" and not cms: raise ValueError(f"refuted record lacks countermodel: {entry['id']}")
        if status == "conditional" and not entry.get("premises"): raise ValueError(f"conditional record lacks premise: {entry['id']}")
        if status in {"interpretive", "poetic"} and entry.get("kernel_certified"): raise ValueError(f"non-kernel record certified: {entry['id']}")
        records.append({"id": entry["id"], "atlas_label": anchor, "status": status,
            "kernel_certified": bool(entry.get("kernel_certified")),
            "binding_ids": sorted(x["_id"] for x in by_anchor.get(anchor, [])),
            "lean_witnesses": [make_witness(n, status, cms) for n in names],
            "conditions": [registry_text(x, "See the receipted theorem statement for the explicit premise.") for x in (entry.get("premises") or [])], "countermodels": sorted(cms),
            "bounds": entry.get("bounds") or [], "claim": registry_text(entry.get("claim")),
            "source_statement_sha": source_shas[anchor],
            "source_obligations": sorted(obligations_by_anchor.get(anchor, [])),
            "notes": registry_text(entry.get("atlas_note"), "See the committed alignment registry for the original note."), "source_registry": "verification/ps_alignment.json"})

    review = load(sketched / "verification/ps_alignment_review.json")
    for index, entry in enumerate(review["items"], 1):
        anchor, status = entry["atlas_id"], entry["current_classification"]
        if anchor not in nodes or status not in STATUSES: raise ValueError(f"invalid review item: {anchor}")
        if entry.get("source_statement_sha") != source_shas[anchor]: raise ValueError(f"review hash disagreement: {anchor}")
        names = [entry["lean_witness"]] if entry.get("lean_witness") else []
        cms = set(names if status == "refuted" else [])
        records.append({"id": f"REVIEW-{index:03d}", "atlas_label": anchor, "status": status,
            "kernel_certified": False, "binding_ids": sorted(x["_id"] for x in by_anchor.get(anchor, [])),
            "lean_witnesses": [make_witness(n, status, cms) for n in names],
            "conditions": [registry_text(entry.get("reason"), "See the receipted theorem statement for the explicit premise.")] if status == "conditional" else [],
            "countermodels": sorted(cms), "source_statement_sha": source_shas[anchor],
            "source_obligations": sorted(obligations_by_anchor.get(anchor, [])),
            "notes": registry_text(entry.get("reason"), "See the committed review registry for the original note."), "source_registry": "verification/ps_alignment_review.json"})

    ids = [x["id"] for x in records]
    if len(ids) != len(set(ids)): raise ValueError("duplicate alignment record id")
    known = set(ids)
    for item in records:
        for bound in item.get("bounds") or []:
            if bound not in known: raise ValueError(f"unknown bounded record: {bound}")
    records.sort(key=lambda x: (x["atlas_label"], x["id"]))
    counts = dict(sorted(Counter(x["status"] for x in records).items()))
    anchors = {x["atlas_label"] for x in records}
    countermodel_anchors = {x["atlas_label"] for x in records if x.get("countermodels")}
    command = f"python ci/build_lean_alignment.py --sketched-root {sketched} --principia-repo {principia_repo}"
    output = {"schema": "principia-lean-alignment/v1",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "description": "Generated correspondence; manuscript proof_status remains independent of Lean status.",
        "lean_program": {"repository": "https://github.com/PaulTiffany/sketched", "commit": sketched_sha,
            "receipted_declarations": len(rows), "checked_bindings": len(bindings),
            "mapped_atlas_anchors": len(anchors), "alignment_records": len(records),
            "status_counts": counts, "countermodel_anchor_count": len(countermodel_anchors),
            "conditional_record_count": counts.get("conditional", 0), "refuted_record_count": counts.get("refuted", 0),
            "omitted_unreceipted_coverage_rows": len(omitted)},
        "principia_source": {"repository": "https://github.com/PaulTiffany/Principia-Symbolica",
            "commit": principia_sha, "source_tree_sha256": source_tree_sha(),
            "atlas_schema": atlas["meta"].get("schema"), "atlas_nodes": len(atlas["nodes"])},
        "semantics": {"manuscript_proof_status": "Local LaTeX proof linkage only.",
            "lean_alignment_status": "Kernel correspondence for one typed claim or boundary.",
            "unmapped": "Honest absence of a receipted Lean correspondence, not a failed theorem.",
            "operator_poetry": "Intentional non-propositional material, not an unmapped theorem failure."},
        "status_vocabulary": {k: alignment["status_vocabulary"].get(k, "") for k in STATUSES},
        "source_registry_sha256": {rel: file_sha(sketched / rel) for rel in registry_rels},
        "generation_command": command, "omitted_unreceipted_coverage_rows": omitted, "records": records}

    if args.check:
        if not OUT.is_file(): print(f"STALE: {OUT} missing"); return 1
        current = load(OUT); current.pop("generated_at", None); output.pop("generated_at", None)
        if current != output: print("STALE: Lean alignment differs from committed registries"); return 1
        print(f"OK: Lean alignment current ({len(records)} records / {len(anchors)} anchors / {len(rows)} declarations)"); return 0
    OUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Lean alignment written to {OUT}")
    print(f"  Sketched commit: {sketched_sha}\n  declarations: {len(rows)}\n  bindings: {len(bindings)}\n  records: {len(records)}\n  anchors: {len(anchors)}\n  statuses: {counts}\n  countermodel anchors: {len(countermodel_anchors)}")
    return 0


if __name__ == "__main__":
    try: raise SystemExit(main())
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr); raise SystemExit(2)
