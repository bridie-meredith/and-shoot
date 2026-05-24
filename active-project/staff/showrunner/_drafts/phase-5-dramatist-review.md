# Phase 5 Dramatist Review
# project: taylor-westeros-good-intentions
# date: 2026-05-24
# reviewer: dramatist (stateless)
# subject: series.substance signature — state_axes + cost_ledger + antagonist_pressure + chunk_targets

---

DRAMATIST PHASE 5 VERDICT: REVISE

---

## ROLL-UP CHECK: FAIL

chunk_targets.book.delta_per_signature_axis is declared 3-4. b01 absorbs the entire series — there is no other book. Actual axis movement required:

  moral_framework (protagonist):     2 → 8  = 6 ranks
  capability (protagonist):          2 → 8  = 6 ranks
  relational_anchor_status:          1 → 9  = 8 ranks
  moral_legibility_to_self:          4 → 8  = 4 ranks
  political_register (protagonist):  1 → 9  = 8 ranks
  position (protagonist):            gross ~14 ranks of motion (1 → ~7 → 1)
  social_tether (protagonist):       gross ~15 ranks of motion (1 → ~8 → 1)

Five protagonist axes require 4-8 ranks net. The 3-4 band is the climax-book default from delta-targets.md, drawn for a multi-book series where a climax book handles one arc segment. Here it must contain the full series sweep. Downstream, /and-substance book Phase 3 will read 3-4 as a ceiling and produce chapter contracts that underdeliver on moral_framework, capability, relational_anchor_status, and political_register by 2-5 ranks each — a systematic structural shortfall.

The rise-then-collapse axes (position, social_tether) compound this: gross motion is ~14-15 ranks each, but net Δ is 0. A 3-4 ceiling does not encode gross motion. Chapter-level allocations will not have headroom for the full rise arc before the collapse, producing a flat version of what the signature declares.

Fix: raise chunk_targets.book.delta_per_signature_axis to 4-8 (matching the series band and the actual axis requirements). Add an explicit sub-note: "rise-then-collapse axes (position, social_tether) are tracked as gross motion at chapter level; net-zero end-state does not reduce chapter-level Δ allocation."

---

## STRUCTURAL COMMITMENT CHECK: PASS

book_count=1, chapters 18-22, scenes 3-5, bones 5-15, cyclical=false, pov=single, world_evolution=evolving, series_end_shape=tragic — all honored. Bone count floor (18×3×5=270) matches declared minimum. Tragic end: all LOCKED end states deliver negative resolution. POV: no interludes authored; single Taylor first-person enforced. No violations.

---

## TRAGIC-SHAPE COHERENCE: PASS

cl01-cl06 are sufficient to earn cl07. cl02+cl03+cl05 erode moral_framework -8 total across the arc. cl03+cl04 build the tether gain that becomes the cl07 tether -7 (the structure that cannot be dismantled is the structure that unravels). cl04's extraction-window-missed closes the exit before cl07 springs it. cl06's contempt-without-exit means Taylor already knows what she is preserving when cl07 fires. The multi-axis cascade at cl07 (tether -7, position -6, anchor at nine-worst) reads as accumulated consequence, not a tonal break. Shape is: build structure (cl01-cl05) → lock exit (cl04) → articulate contempt (cl06) → watch structure dissolve from the outside (cl07). cl07 is earned.

---

## CURVE-SHAPE INTEGRITY: FAIL

position (protagonist) and social_tether (protagonist) are declared start_rank=end_rank=1. The notes: field correctly flags "rise-then-collapse; per-chapter contracts track rise and collapse separately." The trajectory (d03, d04, d07, d10) contains explicit shift language for the peaks. The structural commitment for the peaks exists in the source material.

The problem is encoding propagation. /and-substance book Phase 3 dispatches screen-writer with the signature block. Screen-writer reads start_rank=1, end_rank=1. Without reading notes:, these axes read as HELD. Chapter contracts will not be issued Δ allocation on position or social_tether for the rise arc (d03-d10). The d07 peak (Otto's-unofficial-instrument) and d10 lock (position-of-no-exit) will not be authored as substance events because no chapter contract will claim those axes as in_motion. The d14 collapse will then have nothing to collapse from — it will read as Taylor going from anonymity directly to expulsion without the intermediate embeddedness that makes the collapse legible.

The notes: field cannot carry structural weight that axis-level fields do not. It is a prose annotation; it does not propagate to chapter contract generation. The fix must be in the axis encoding itself.

Fix: for position (protagonist) and social_tether (protagonist), encode the rise and collapse explicitly. Options:
  (a) Add peak_rank and peak_at fields: peak_rank: 7, peak_at: d07 (position); peak_rank: 8, peak_at: d07 (social_tether). These fields must be read at /and-substance book Phase 3.
  (b) Split into two axis entries each: position-rise (start 1 → peak 7 at d07 → end 7, class: plot) and position-collapse (start 7 → end 1 at d14), with the book-level drama making explicit that the collapse arc is a second axis track.

Either fix is valid. The current encoding silently drops the rise arc at chapter contract generation. This is not a notes problem — it is a schema-level gap.

---

## COST-LEDGER GEOMETRY: PASS (with one watch-item)

cl02: position +4 / framework -3. Position is rise-then-collapse; the +4 will be zeroed at cl07. Cost is permanent. Geometry sound across arc.

cl03: capability +3, tether +4 / framework -3. Two-axis gain against one-axis cost reads as cheap-gain at entry level. The defense is arc-level: tether +4 here is the structure that becomes tether -7 at cl07 (the rope you hand the trap). Capability +3 is permanent but is the specific axis that builds the Khepri-rhyme. The geometry is sound across the arc, but the entry-level appearance of cheap-gain on cl03 will fire the auditor's SUBSTANCE-SUSPECT-cheap-gain-capability check at /and-substance book Phase 0 unless the chapter contract for d04 explicitly encodes tether gain as future-cost collateral. Flag this for the book-level chapter contract authoring brief.

cl04: relational_anchor_status +3 / opportunity-missed (extraction window foreclosed). Valid opportunity-missed pattern. No axis decrement required.

cl05: capability +2 / framework -2. 1:1. Clean.

cl06: political_register +5 / opportunity-missed (contempt with no exit). Valid. The +5 is not a win — it is the axis moving toward its worst functional state (clarity that forecloses nothing).

cl07: legibility +4 / anchor +4, tether -7, position -6. One small gain against triple-axis cascade cost. Recognition arrives at the same moment as the catastrophe. Correct tragic geometry.

Watch-item: cl07 lists relational_anchor_status +4 in the cost: field as a positive number. Elsewhere in cl07, axis deterioration uses negative numbers (tether -7, position -6). The mixed sign convention within a single cost entry will cause a downstream reader (or automated parser) to read relational_anchor_status +4 as a gain.

---

## OPENING-AS-CLIMAX SUSTAINABILITY: PASS (with downstream watch-item)

18-22 chapters at climax-book density is sustainable if density is not flat. The trajectory has a natural escalation curve: d01-d06 build (6 deltas across roughly chapters 1-9), d07-d10 lock (4 deltas across roughly chapters 10-14), d11-d14 cascade (4 deltas across roughly chapters 15-18+). Earlier chapters can run at 0.5-0.7 density; the 0.7-0.9 ceiling applies to lock and cascade zones. This is architecturally sound.

The risk already flagged by the pulp-enthusiast is the d10-d14 zone: 4-5 chapters where Taylor is non-extractable and waiting for the Dance. The structural fix is compression: the d11-d14 zone should be authored at 3-4 chapters maximum (not spread across 6+), and the d01-d06 zone should absorb the bulk of the 18-22 range so earlier chapters get time to build the embeddedness that makes the collapse land. If book-level chapter planning spreads the cascade zone across 7+ chapters, fatigue is the result.

---

## DOWNSTREAM ENCODING-AMBIGUITY FLAGS:

1. chunk_targets.book.delta_per_signature_axis: 3-4 — ceiling mismatch with actual axis Δ required (4-8 on most protagonist axes). Will propagate as systematic underdelivery at chapter contracts. [ADDRESSED IN ROLL-UP CHECK ABOVE — requires fix before /and-substance book.]

2. position (protagonist) start_rank=end_rank=1, social_tether (protagonist) start_rank=end_rank=1 — any downstream pass reading only these fields classifies both axes as HELD. Rise arc (d03-d10 peaks) will not be allocated chapter-level Δ. [ADDRESSED IN CURVE-SHAPE CHECK ABOVE — requires schema fix before /and-substance book.]

3. cl07 cost field sign convention: cost: "relational_anchor_status +4, social_tether -7, position -6" — positive number for relational_anchor_status in a cost field where other entries use negative numbers. A parser or downstream author reading cost entries will treat +4 as a gain on relational_anchor_status. Fix: annotate explicitly — "relational_anchor_status +4 [toward nine = unprotected-at-burn; HIGH = WORST]" — or adopt a consistent convention: use negative sign for all cost-field movements regardless of axis polarity, and flag axes where high rank is worst in the axis definition.

4. moral_legibility_to_self end_rank=8 — notes: explains "too-late diminishes usability" as the reason it stops at 8. Without a LOCKED annotation on end_rank=8, downstream chapter contracts may push toward 9. Add [LOCKED: end 8 — recognition at full force but too-late; 9 is narratively unavailable] to match the LOCKED annotations on other axes.

---

## FEEDBACK FOR REVISE:

The dramatic shape is sound. The signature delivers rise-peak-fall across the protagonist's moral and political axes, with a cost ledger whose cascade geometry earns the d14 burn. The antagonist's pressure is a real force with its own escalation logic. The tragic end is structurally committed.

Two encoding problems will silently corrupt the downstream chapter contract generation and must be fixed before /and-substance book proceeds:

1. chunk_targets.book.delta_per_signature_axis: raise from 3-4 to 4-8, and add a gross-motion sub-note for rise-then-collapse axes. This is a one-line fix with high downstream consequence.

2. position (protagonist) and social_tether (protagonist) rise-then-collapse encoding: the current start_rank=end_rank=1 encoding will cause both axes to be treated as held at book-level planning. The peak states (d07 position ~7, d07/d04 tether ~8) must be represented in a field that downstream dispatches read — either peak_rank/peak_at fields added to the axis schema, or explicit split into rise/collapse axis pairs. The notes: field is insufficient.

Two additional encoding corrections (cl07 sign convention, moral_legibility_to_self LOCKED annotation) are clean-up items that can be addressed in the same pass.

Shape verdict: revise encoding, not shape.
