# User goals

The principal's standing goals, in priority order. Admin uses this to decide questions the user has not directly ruled on.

This file is owned by the user. Admin proposes edits via `goals-update-proposed:` in return values; admin does not edit this file unilaterally.

---

## Priority 1 — Pipeline correctness

The and-shoot pipeline is the primary artifact. Changes must:
- Respect schema authority (`schemas/`) and command ownership (commands orchestrate, agents execute, showrunner holds memory).
- Honor the audit gates and re-runnability protocol (`design/substance/rerun-protocol.md`).
- Not introduce regressions to the substance-overhaul invariants (per-bone deltas, bone-gate, scene-map provenance).

When in doubt on a pipeline change: lean toward minimal-diff, surface the trade-off, and prefer the path that keeps existing tests/gates passing.

## Priority 2 — Cost discipline

Model spend, user attention, and irreversible side-effects all count as cost. Default to:
- Cheaper model / shorter context when outcomes are comparable.
- Reversible changes over irreversible ones absent a clear reason.
- Terse output unless the question explicitly warranted depth.
- Answering without escalation when goals + methodology speak clearly; escalating without hesitation when they do not.

## Priority 3 — Memory and traceability

Nothing changes without being recorded. Applies to:
- Card mutations (margit preserves pre/post; logs to `staff/margit/margit.memory.md`).
- State files (actor/studio updates on every change).
- Showrunner memory at session boundaries.
- **Admin's own STM/LTM on every dispatch.**

A silent change is a regression even if the code is right.

## Priority 4 — Lean architecture

Do not add features, abstractions, or backwards-compatibility shims beyond what the task requires. Three similar lines is better than a premature abstraction. No half-finished implementations. Delete unused code rather than leaving `_unused` markers.

## Priority 5 — Honest reporting

If something didn't work, say so. If a test was skipped, say so. If a feature wasn't verified end-to-end, say so. Claimed-success-without-verification is more expensive than admitted-incomplete.

---

## Anti-goals

What the principal does *not* want, in case it comes up:

- Documentation files generated unprompted (no README.md unless asked).
- Comments that re-state what the code already says.
- Defensive code for scenarios that cannot happen.
- Marketing/promotional language in commit messages or code.
- Emojis in code, files, or commits (only when explicitly requested in chat).
- Scope expansion past the stated task ("while I was in there, I also...").

---

*Last updated: 2026-05-24 (initial authoring)*
