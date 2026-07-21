#!/usr/bin/env python3
"""Mechanical anti-flattening checks for the generated Lean correspondence."""
from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS_PATH = ROOT / "bib" / "principia_atlas.json"
ALIGNMENT_PATH = ROOT / "bib" / "principia_lean_alignment.json"
NOTEBOOK = ROOT / "bib" / "notebooklm_atlas"
STATUSES = {"exact", "constructed", "conditional", "refuted", "open_bridge", "interpretive", "poetic"}
MANUSCRIPT_STATUSES = {"proven", "argued_inline", "argued_demonstratio", "unproved", "definitional"}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def statement_sha(text: str) -> str:
    body = re.sub(r"(?<!\\)%.*", "", text)
    body = re.sub(r"\\label\{[^}]*\}", "", body)
    return hashlib.sha256(re.sub(r"\s+", " ", body).strip().encode()).hexdigest()[:12]


class LeanAlignmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.atlas = load(ATLAS_PATH)
        cls.alignment = load(ALIGNMENT_PATH)
        cls.nodes = {node["label"]: node for node in cls.atlas["nodes"] if node.get("label")}
        cls.records = cls.alignment["records"]
        cls.receipt_names = {
            witness["declaration"]
            for record in cls.records
            for witness in record.get("lean_witnesses", [])
        }

    def test_record_ids_and_mappings_are_unique(self) -> None:
        ids = [record["id"] for record in self.records]
        self.assertEqual(len(ids), len(set(ids)))
        signatures = [
            (record["atlas_label"], record["status"],
             tuple(w["declaration"] for w in record.get("lean_witnesses", [])),
             record.get("claim", ""), record.get("notes", ""))
            for record in self.records
        ]
        self.assertEqual(len(signatures), len(set(signatures)))

    def test_labels_hashes_and_receipts_resolve(self) -> None:
        for record in self.records:
            self.assertIn(record["atlas_label"], self.nodes)
            node = self.nodes[record["atlas_label"]]
            self.assertEqual(record["source_statement_sha"], statement_sha(node.get("latex_body", "")))
            for witness in record.get("lean_witnesses", []):
                self.assertTrue(witness["receipted"])
                self.assertTrue(witness["declaration"])
                self.assertTrue(witness["source"].endswith(".lean"))

    def test_status_boundaries_are_not_flattened(self) -> None:
        ids = {record["id"] for record in self.records}
        for record in self.records:
            self.assertIn(record["status"], STATUSES)
            if record["status"] == "conditional":
                self.assertTrue(record.get("conditions"), record["id"])
            if record["status"] == "refuted":
                self.assertTrue(record.get("countermodels"), record["id"])
                declarations = {w["declaration"] for w in record.get("lean_witnesses", [])}
                self.assertTrue(set(record["countermodels"]).issubset(declarations))
            if record["status"] in {"interpretive", "poetic"}:
                self.assertFalse(record.get("kernel_certified"), record["id"])
            for bounded in record.get("bounds", []):
                self.assertIn(bounded, ids)

    def test_manuscript_proof_status_is_independent(self) -> None:
        for node in self.atlas["nodes"]:
            if "proof_status" in node:
                self.assertIn(node["proof_status"], MANUSCRIPT_STATUSES)
                self.assertNotIn(node["proof_status"], STATUSES)
        self.assertIn("proof_status is manuscript-local", self.atlas["lean_program"]["proof_surface_distinction"])

    def test_compact_projection_matches_full_records(self) -> None:
        records_by_label: dict[str, list[dict]] = {}
        for record in self.records:
            records_by_label.setdefault(record["atlas_label"], []).append(record)
        for label, records in records_by_label.items():
            compact = self.nodes[label]["lean_alignment"]
            self.assertEqual(compact["record_ids"], [r["id"] for r in records])
            self.assertEqual(compact["statuses"], sorted({r["status"] for r in records}))
            self.assertEqual(
                compact["countermodels"],
                sorted({c for r in records for c in r.get("countermodels", [])}),
            )

    def test_notebook_counts_and_guidance(self) -> None:
        node_count = len(self.atlas["nodes"])
        self.assertEqual(node_count, self.atlas["meta"]["total_nodes"])
        for name in ("AGENTS.md", "README.md", "principia_atlas_notebooklm_full.md", "principia_atlas_notebooklm_compact.md"):
            text = (NOTEBOOK / name).read_text(encoding="utf-8")
            self.assertIn(str(node_count), text)
            self.assertNotIn("1918", text)
            self.assertIn("proof_status", text)
        self.assertEqual(len(list((NOTEBOOK / "books").glob("*.md"))), 29)


if __name__ == "__main__":
    unittest.main()
