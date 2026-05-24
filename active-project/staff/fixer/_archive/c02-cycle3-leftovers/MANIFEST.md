# c02-cycle3 leftover archive

Date archived: 2026-05-24
Reason: clearing the un-namespaced fixer log paths (`and-facets-cycle3-callouts.md`,
`and-facets-cycle3-fixes.md`) before the b01c01-cycle3 fixer dispatch could overwrite
them. The fixer-log naming convention (`and-facets-cycle<N>-fixes.md`) is not chapter-
namespaced; chapter b01c02 ran its own cycle 3 prior to b01c01's cycle 3, so the c02
working files were sitting on the canonical c03 path.

Contents:
- `and-facets-cycle3-callouts.md` — b01c02 cycle-2 → cycle-3 callouts (interest-narrator
  narrator:6 AP-10 cap, sensory:2 anchor-invalid)
- `and-facets-cycle3-fixes.md` — b01c02 cycle-3 fix log (Callout A FIXED-DIRECT;
  Callout B record)

Restore: `cp -n ./*.md ../../` from this directory to put them back.

Cross-chapter persistent files (e.g. `fixer-log.md`, `and-facets-cycle1-fixes.md`,
`and-facets-cycle2-fixes.md`) NOT archived — the c02-cycle3 collision was on the
cycle3-named files only; other cycle logs are chapter-specific by their cycle position
in each chapter's run.
