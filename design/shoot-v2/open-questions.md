# Open questions

Most prior questions resolved in `decisions.md`. What remains is genuinely deferred to implementation.

## Implementation-time questions

These are fine to discover when building, not before.

- **Fork-writer scope:** does one fork per character produce all that character's outputs (dialogue + narrator-flags-if-POV + feeling-flags-if-on-screen) in a single hermetic run, or does each output type get its own fork? Both honor flushability; pick when implementing.
- **Tensometer rater identity:** dramatist runs the pass per default mapping. If dramatist's structural lens is wrong for tension scoring at the line level, swap to a dedicated rater fork at implementation time.
- **Conversion tool for s01e06:** the bullet-to-proto-line conversion needs a procedure. Manual first pass is fine for the dogfood; consider a fork-based conversion if it gets repetitive.
- **Behavior card seed corpus:** ~~for actively-used Worm/Westeros characters, where do the verbatim samples come from?~~ Resolved 2026-05-06: Worm samples harvested from `brighid-creative-writing/projects/_archive/hail-hydra-h3/draft-final.md`; Westeros samples from canon and synthesized illustrations flagged as authored. First behavior cards landed: `taylor-hebert`, `taylor-hebert-westeros`, plus shared `westeros-grrm-mannerisms`, `westeros-smallfolk`, `westeros-noble-courtly`, `westeros-maester`, `westeros-septon`, `westeros-northern`. Samples expected to grow as episodes ship.
- **Behavior card composition cap:** schema's `inherits:` chain is capped at depth 1, but full composition stack is universal × region × class × per-character (4 cards). Convention adopted: `inherits:` one parent + `references:` for the rest, with margit loading both as composition inputs. Reconsider lifting the cap if composition graphs become opaque.
- **Behavior card loading by margit:** margit needs to expose a "resolve and load behavior stack" method that the dialogue-writer fork dispatch and the auditor dispatch both call. Implementation deferred. Logic mirrors override-merge precedent.
- **Stitcher gap escalation:** when a gap is flagged for re-author, which prior phase does it route back to (proto-line / dialogue / facet)? Often answerable by inspecting the gap; codify if a pattern emerges.
- **Migration eval workflow:** s01e01 A/B against shoot-v1 needs a test harness. Defer until shoot-v2 has produced one renderable scene.

## Architectural questions still genuinely open

- **Does the impersonator agent retire entirely?** Default leaning: yes. Confirm at implementation when the dialogue-writer fork is wired up and we see whether any non-dialogue use case for impersonators survives.
- **Multi-pass review pass orchestration:** who runs the proto-line review loop? Default: orchestrator-driven, same shape as current `/and-shoot` Phase A audience+dramatist iteration. Validate when first proto-line file is produced.
