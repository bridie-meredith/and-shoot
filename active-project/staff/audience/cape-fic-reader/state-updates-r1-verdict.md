---
reviewer: cape-fic-reader
facet: state-updates
cycle: 1
episode: b01c01
date: 2026-05-19
verdict: revise
---

# Verdict reasoning

The prop and environment entries are clean — corner room, needle handoff, thermal, nets down, all track as genuine persistent mutations with clear acquisition paths. The rot is in Taylor's `knowledge.*` chain. Entries 11 and 12 (`hook-block-density-map: unmapped -> block-density-mapped-passively` at @12, `watch-patrol-cadence-hook: unknown -> patrol-pattern-read-passively` at @15) fire as canonical knowledge-state acquisitions while entry 10 says her insect-sense is in discipline-hold at @8 (`threshold-held-against-density-spike`) with no released-from-hold transition before @12. The facet is writing tactical intelligence into canonical state through a vector the same facet says is clamped. That's a who-knows-what-when break that corrupts the downstream ledger. Also entry 17 (`ward-social-geometry-hook: block-mapped -> ward-layer-deeper`) is a gradient note, not a field value — `ward-layer-deeper` cannot be applied as a clean write-back.

# Entry-level callouts

- [state:11] @12 `actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively` — entry 10 fires at @8 saying her insect-sense is `threshold-held-against-density-spike`. No hold-released transition exists between @8 and @12. She cannot have passively mapped block density while holding the threshold. The acquisition vector is not there; this is registration-as-state contamination on a beat that should be silent.

- [state:12] @15 `actor:taylor-hebert-kl-122ac.knowledge.watch-patrol-cadence-hook: unknown -> patrol-pattern-read-passively` — one Watch pass does not make a cadence. `patrol-pattern-read` implies recurrent observation across multiple passes establishing a temporal pattern. A single pass at @15 is the first data point, not a pattern registration. Persistence test: does Taylor now canonically know the Watch cadence after one sighting? That's not how pattern-reading works even under normal cognition, let alone under discipline-hold. This entry is pre-empting — it fires the knowledge state at the evidence-gathering beat, not at a pattern-confirmation beat.

- [state:17] @26 `actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper` — `ward-layer-deeper` is a direction, not a state value. What does Taylor canonically know now that she did not know before? That Wren is a Ward? That Ward presence is thicker than she thought? The new-value is ambiguous; the showrunner cannot apply this as a clean mutation against the canonical state file. Compare the rubric's anchors: `provisional-labor-eligible`, `name-on-line-with-parallel-margin-marks` — those are discrete field values. This is a vibe note dressed as state.

# Convergence trace

- [state:11] @12: Auditor did not flag this entry. The r1 auditor's CURVE-SHAPE pass cleared state-updates globally and the pile-up review covered @12 only as a narrative reference (narrator:3, vibes:8/11). Anti-pattern #1 (registration-as-state) from the rubric is adjacent, but the auditor's AP-SCAN was scoped to narrator. No direct convergence.
- [state:12] @15: Auditor found the @15 pile-up WARRANTED as a Scene-B peak. It did not evaluate whether a single-pass observation supports `patrol-pattern-read` as a canonical state value. The persistence test (§Frugality) is the rubric axis the auditor would cite; it did not apply it here. No direct convergence.
- [state:17] @26: No auditor finding. The frugality axis's loose-new-value concern is uncharted in the r1 and r2 reports. No convergence.
