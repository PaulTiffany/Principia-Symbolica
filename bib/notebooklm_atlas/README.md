# Principia Symbolica Atlas for NotebookLM

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
- `Proof status` is local atlas status, not external acceptance.
- The statement/body is cleaned for reading; consult the LaTeX source for exact typography.

## Atlas Counts

- Nodes: 1914
- Books / source groups: 29
- Dependency components: 0

## Nodes by Source Group

| Source group | Nodes |
|---|---:|
| `scholium_symbolicum` | 264 |
| `book1` | 2 |
| `book2` | 55 |
| `book3` | 76 |
| `book4` | 389 |
| `book5` | 235 |
| `book6` | 134 |
| `book7` | 183 |
| `book8` | 130 |
| `book9` | 150 |
| `appendix_abstracts` | 7 |
| `appendix_symbolic_reflexive_validation` | 37 |
| `appendix_dual_horizon` | 123 |
| `appendix_symbolic_framing` | 55 |
| `operatio` | 3 |
| `executio` | 1 |
| `appendix_symbol_dictionary` | 1 |
| `integratio` | 1 |
| `main` | 10 |
| `temperatio` | 1 |
| `trace1` | 7 |
| `trace2` | 7 |
| `trace3` | 7 |
| `trace4` | 7 |
| `trace5` | 7 |
| `trace6` | 6 |
| `trace7` | 6 |
| `trace8` | 5 |
| `trace9` | 5 |

## Nodes by Role

| Role | Count |
|---|---:|
| `section` | 419 |
| `proof` | 400 |
| `definition` | 348 |
| `theorem` | 174 |
| `scholium` | 124 |
| `remark` | 91 |
| `proposition` | 88 |
| `lemma` | 83 |
| `corollary` | 67 |
| `axiom` | 65 |
| `demonstration` | 31 |
| `assumption` | 22 |
| `conjecture` | 2 |
