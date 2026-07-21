# Principia Symbolica Atlas for Machine Readers

Generated from `bib/principia_atlas.json`. Nodes: 1914.
Source groups: 29.

## Two proof surfaces

`proof_status` reports only manuscript-local LaTeX proof linkage. It is not a
Lean receipt. `lean_alignment.statuses` reports the separate typed correspondence
to the committed Sketched Lean program.

- Lean program commit: `edc148696a740d319732fedd3da8e207c93ad5c3`
- Receipted Lean declarations: 1737
- Checked bindings: 1295
- Mapped Atlas nodes: 651
- Lean status counts: conditional=295, constructed=49, exact=184, interpretive=6, open_bridge=128, poetic=1, refuted=2
- `proof_status` is manuscript-local; `lean_alignment.statuses` is independent kernel correspondence.

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
