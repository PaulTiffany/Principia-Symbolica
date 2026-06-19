# Principia Symbolica — Atlas for Machine Readers

`principia_atlas.json` is the canonical LLM-facing artifact. Read it, not the
PDF: the PDF's text layer mangles math, loses structure, and cannot be
traversed. The atlas keeps every claim as an addressable node with its
**verbatim LaTeX body** and **resolved dependency edges**.

## Schema
- `meta` — counts and provenance.
- `macros` — `{name: {expansion, arity}}`. Custom control sequences in any
  body (e.g. `\\drift`, `\\Obs`, `\\freeenergy`) resolve here.
- `nodes[]` — one per labelled object:
  - `label`, `type` (verbatim env, including Newton-Latin: demonstratio, propositio, …),
  - `role` — canonical type over the Latin/English split (demonstratio→demonstration,
    propositio→proposition; otherwise identity),
  - `name` (display title), `book`, `matter_region`, `matter_role`, `file`, `line`,
  - `latex_body` — the full `\begin{env}…\end{env}`, verbatim,
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
      `proven` (a formal `\begin{proof}` is linked to it);
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
