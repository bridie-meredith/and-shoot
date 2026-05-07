# Phase 1 — Memory-Flags Baseline Review

Auditor review of `design/shoot-v2/phase1-memory-flags-baseline-naive.md` (rubric-blind naive baseline, 21 entries on 77 proto-lines) under V1 lenient and V2 strict per `design/shoot-v2/rubric-memory-flags.md`.

Cross-references consulted:
- `active-project/theater/facets/tensometer.md` (locked) — for tens-zone determination.
- `active-project/theater/facets/interest-narrator.md` (locked) — for narrator-interest spine co-citation check.
- `cards/dialects/taylor-hebert.card.md` §"Memory monuments" — Earth-Bet authority.
- `cards/dialects/taylor-hebert-westeros.card.md` §"Memory monuments" — Westerosi + local-current authority.

---

## Summary

| Pass | Accept | Reject | Rate |
|---|---|---|---|
| **V1 lenient** | 18 | 3 | **85.7%** |
| **V2 strict** | 4 | 17 | **19.0%** |
| **Lift gap** | | | **66.7pp** |

V1-to-V2 gap is rubric-blind contamination (licensing-layer / inverted-tens-density / spine-co-citation / sparsity discipline absent), not over-strict calibration. The author respected the variant card's hard-fence rule (no Earth-Bet proper noun in description, no Dance specifics named); the contamination lives at the licensing / discipline / curve-shape level, exactly where the rubric does its load-bearing work.

V2 strict baseline = **19.0% — baseline to beat**. Higher than narrator-interest's 22.2% baseline (comparable; both are perception-class facets) and meaningfully higher than state-updates' 6.7% (lower because state-updates' rubric prevents stumbling-into-compliance more aggressively). The naive author can produce a few CORRECT fires by accident on @34, @52, @63, @77 — beats where the proto-line genuinely lights a monument, the cue is plausible, and tens-zone is permissive. Most fires fail one of: peak-anchored, spineless, parasitic-on-NI, or persistent-monument.

V1 LOCKED. V2 LOCKED. No softening between rounds.

---

## V1 lenient pass — accepts 18/21

V1 criteria: form-correct (single-clause description, well-formed target-reference, anchor-to-real-proto-line) AND any monument-family is plausibly invoked at any reading. No discipline / licensing / curve / co-citation checks.

Form rejects (3):
- **Entry 11 @39** — comma-spliced two-clause structure ("the feet are set where the calculation set them, the way the body has been set in other commit-frames"). Single-clause violation.
- **Entry 12 @43** — comma-spliced ("the document comes back marked, the way every adult document she has touched has come back marked"). Single-clause violation.
- **Entry 19 @69** — semicolon-spine ("the wheel-tremor leaves and the small fauna release; she has felt a release-shape like this before"). Two-clause violation.

All 18 remaining entries pass V1. Monument plausibility is charitable; even forced-fit entries (e.g. entry 1 @4, fauna-feed-as-monument-callback) pass V1's "any reading" charity.

---

## V2 strict pass — accepts 4/21

V2 criteria: all three axes (monument-trigger, displacement-discipline, licensing-discipline) demonstrated; no anti-pattern fired; cross-facet contract honored (NI co-citation; tens-zone permitted); hard-fence held.

### Per-entry verdicts

| # | Beat | Tens | NI? | Verdict | Primary failure |
|---|---|---|---|---|---|
| 1 | @4 | 1 | yes | **REJECT** | forced-fit (anti-pattern #5): fauna-feed at @4 is base-establishing, not monument-trigger; cue too generic to license `monument-locker` target |
| 2 | @11 | 1 | yes | **REJECT** | generic monument-gloss (anti-pattern #4): "they came through other gates she has read about" — no specific monument family lit |
| 3 | @13 | 1 | NO | **REJECT** | spineless fire (anti-pattern #7): NI silent at @13 |
| 4 | @23 | 2 rising | yes | **REJECT** | quiet-beat anchor failure: rising-edge fire without backward-reaching argument; cue is forward-pointing (being-targeted), not backward (Emma-callback as resonance) |
| 5 | @24 | **3** | yes | **REJECT** | peak-fire (anti-pattern #6); licensing-discipline failure on quiet-beat anchor |
| 6 | @28 | 2 rising | NO | **REJECT** | spineless fire (NI silent at @28); also rising-edge without resonance argument |
| 7 | @30 | 2 trailing | yes | **REJECT** | generic monument-gloss: "the way the system used to write her in" — no specific Earth-Bet monument named via cue |
| 8 | @33 | 2 trailing | yes | **REJECT** | author-vocabulary leak (anti-pattern #12) / parasitic-on-NI: description verbatim duplicates NI @33's registration ("the threshold holds and what is on the other side stays the size she will not name"); not a distinct memory-flag construction |
| 9 | @34 | 1 | yes | **ACCEPT** | distinct cue ("when the door was the wrong door") lights Annette-death pattern via fauna-watch channel; spine present; quiet-beat-anchored; displacement-disciplined |
| 10 | @38 | **3** | yes | **REJECT** | peak-fire; cape-deployment displacement is parasitic on the act, not load-behind-act |
| 11 | @39 | **3** | yes | **REJECT** | peak-fire; form-fail (multi-clause); cape-pre-deployment displacement is parasitic on NI's pre-calc registration |
| 12 | @43 | 2 trailing | yes | **REJECT** | forced-fit / generic monument-gloss: "every adult document...has come back marked" stretches locker-pattern over a single officer-mark beat; form-fail (multi-clause) |
| 13 | @48 | 2 trailing | yes | **REJECT** | author-vocabulary leak / parasitic-on-NI: description verbatim duplicates NI @48 ("she has heard the shape of that word before in another tongue") |
| 14 | @52 | 1 | yes | **ACCEPT** | distinct cue ("eyes she has seen drop before, by another flagstone") lights peer-isolation / Emma-pattern; spine present; quiet-beat-anchored; displacement-disciplined; doubled-register Earth-Bet contribution |
| 15 | @57 | 2 trailing | yes | **REJECT** | persistent-monument (anti-pattern #11): @34 already fires Annette-death; @57 second fire on same monument family is over-firing the cluster |
| 16 | @60 | 2 trailing | yes | **REJECT** | persistent-monument with @52 (Emma-pattern fires twice); plus stage-named cue (anti-pattern #3): "she remembers from a hallway" labels rather than producing the cue |
| 17 | @63 | 2 rising | yes | **ACCEPT** | rising-edge fire defended on backward-reaching argument: "she has read the marks would go" produces the *reading-about* cue (foreknowledge load), not the *commit-pending* cue (forward-pointing); Westerosi-monument clamp on record-marking-convention |
| 18 | @64 | **3** | yes | **REJECT** | peak-fire (default-forbidden); resonance fires after the peak, not on it |
| 19 | @69 | 1 | yes | **REJECT** | form-fail (semicolon-spine); forced-fit (Endbringer-departure pattern stretched on a wheel-tremor; cue too generic) |
| 20 | @73 | 1 | yes | **REJECT** | author-vocabulary leak / parasitic-on-NI: "the frame's shadow holds the size it has been" near-verbatim from NI @73; form-fail (semicolon-spine); should produce distinct construction |
| 21 | @77 | 1 | yes | **ACCEPT** | distinct cue ("the cover thins inside it") lights sept-of-harrenhal monument with mask-thinning interaction; spine present (NI @77 mask-thin); quiet-beat-anchored; displacement-disciplined |

### File-level (curve-shape)

**SHAPE-FAIL** on three load-bearing tests:

1. **Sparsity violation.** 21 fires / 77 = 27.3% — far outside 5-12% target band. Density-on-flat contamination dominates the file.

2. **Inverted-tens-density inversion (load-bearing failure).** Naive baseline fires:
   - 4 fires on tens=3 beats (@24/@38/@39/@64) = 4/4 = **1.00 fires-per-beat in 3-zones.**
   - 9 fires on tens=2 beats (@23/@28/@30/@33/@43/@48/@57/@60/@63) = 9/12 = **0.75 fires-per-beat in 2-zones.**
   - 8 fires on tens=1 beats (@4/@11/@13/@34/@52/@69/@73/@77) = 8/61 = **0.13 fires-per-beat in 1-zones.**
   - Ratio 1-to-3 = 0.13 / 1.00 = **0.13×** — the file is firing **8× more densely on peaks than on quiet beats**, the **direct inverse of the rubric's required 3× minimum the other direction**. This is the file's load-bearing failure mode and the most novel / counter-intuitive finding versus prior facet baselines. The naive author defaults to peak-density (which works for narrator-interest) but breaks memory-flags' licensing-layer function entirely.

3. **Doubled-register coverage technically passes** (Earth-Bet @4/@11/@23/@34/@38/@39/@43/@52/@57/@60/@69/@73; Westerosi @13/@28/@30/@48/@63/@64/@77 — both registers fire), but the coverage is contaminated: Earth-Bet over-fires (12 entries) vs Westerosi (7 entries), and the Westerosi over-fires concentrate on peaks (@28/@30/@48/@63/@64), which is itself contaminating.

Monument-family diversity is high (locker, Annette-death, Emma-betrayal, PRT-trigger-period, cape-deployment, Conquest-charter, record-marking, Dance, Endbringer-departure, sept-of-harrenhal, institutional-arrival = ~10 families) — but this is partly density-driven; a clean file will fire fewer families more disciplined.

---

## Six systemic faults named (baseline failure modes)

1. **Density-on-flat / saturation.** 27.3% fire-rate vs 5-12% target. The naive author fires wherever a monument seems plausible, without licensing-layer sparsity discipline.

2. **Peak-density-on-tens-3 (inverted-tens-density violation).** Naive baseline concentrates fires on dramatic peaks (@24/@38/@39/@64), the inverse of the rubric's quiet-beat anchor rule. This is the most novel / counter-intuitive fault relative to prior facets — narrator-interest aligns to peaks and the naive author transfers the pattern.

3. **Spineless fires.** Fires on @13 and @28 where narrator-interest is silent. The mandatory NI spine co-citation rule is unknown to the rubric-blind author.

4. **Author-vocabulary leak from NI / parasitic duplication.** @33, @48, @73 fires duplicate NI entries verbatim or near-verbatim, producing parasitic memory-flag entries that don't add monument-pressure beyond what NI already registers. The displacement-cue construction must be *distinct from* the NI entry on the same beat — memory-flags carries the monument-content layer, not a duplicate of the registration.

5. **Persistent-monument firing.** Annette-death fires twice (@34, @57); Emma-betrayal fires twice (@52, @60); locker-pattern fires across @4 / @33 / @43 / @73 (clustered on locker-adjacent imagery). Same monument lighting on consecutive or near-consecutive beats with same cue — the monument's pressure is the file's repeated emphasis rather than the file's distributed register.

6. **Generic monument-gloss / stage-named cue.** Vague constructions like "every adult document" (@43), "institutional adult" (@11), "the way the system" (@30), "she remembers from a hallway" (@60). The displacement must produce the *shape* of a specific monument; it must not label the act of memory ("she remembers...") nor gesture at a generic class of memories ("every adult document...").

---

## Floor defense

Two NONEs are CORRECT-by-default (the naive author silently passed on these beats; verifying the silences are right):

- **Many @1-@22 beats silent in baseline.** Approach-zone is correctly sparse-or-silent; the few fires (@4, @11, @13) are all REJECTED. The default silence in this zone is correct; the over-reach into @4 / @11 / @13 is the failure.
- **Many @40-@56 beats silent.** Release-zone is eligible but not mandatory. Default silence is fine where no monument lights.

No floor-defense pushback against rejecting any of the 17 V2 rejects. All 17 fail at least one rubric axis on substantive grounds.

---

## Lock decision

V1 LOCKED. V2 LOCKED. Both pass the round-trip test (V1 gives a useful baseline rate; V2 gives a strict baseline-to-beat). The 66.7pp V1-to-V2 gap is consistent with the licensing-layer constraint adding novel filter pressure beyond hard-fence + form (which V1 already checks).

Phase 2 writer-fork target: **>50% V2 accept rate on equivalent corpus**, with curve-shape SHAPE-OK at file-level. (Prior comparable facets — narrator-interest writer-fork lifted to 88.9% at Phase 2; state-updates writer-fork lifted to 76.9% at Phase 2. Memory-flags expected to land in the 70-90% range given the licensing-layer rubric is highly explicit and the writer-fork loads it.)

Phase 1 complete. Baseline: **19.0% V2 strict** (4/21 accepted: @34 Annette-death-via-fauna; @52 Emma-pattern peer-isolation; @63 record-marking backward-reaching clamp; @77 sept-of-harrenhal mask-thin interaction). All four accepts are quiet-beat-anchored, NI-spined, displacement-disciplined, and non-parasitic on NI.
