---
phase: B — reviewer baseline + gap analysis
date: 2026-05-10
run: and-season-tuning-r1
input: A-corpus.md + active-project/staff/auditor/season-s01-pass-*.md + season-s01-split-*
---

# Phase B — Reviewer Baseline + Gap Analysis

The nine-pass review is the existing baseline. Phase B documents (1) what the existing run actually caught on s01, (2) where it routed and how, and (3) gaps the audience attack will press. The locked rubric (`rubric-and-season.md`) and Phase A's enumerated 8 explicit gaps are the canvas; this doc adds the empirical history.

---

## What the s01 nine-pass run caught (terminal verdicts after iteration)

| Pass | Iterations on s01 | Terminal verdict | What it caught |
|---|---|---|---|
| S1 constraint | r1 + r2 | PASS | constraint coherence faults; routed to fixer |
| S2 shape | r1 + reverification | CLEAN | buildup 1–418, climax 419–519 (peak 455–474), denouement 520–912; cited specific line ranges per rubric |
| S3 trim — dark-fantasy-reader | r1 + r2 | ACCEPT | flatline ranges (e.g. 21–60, 83–135); BORED window logging |
| S3 trim — pulp-enthusiast | r1 + r2 + r3 + **r4** | ACCEPT | passive-overuse pattern; named board-change-at-beat-close demand for parental dialogue 127–130 |
| S3 trim — worm-canon-pedant | r1 + r2 | ACCEPT (after r2) | shard-cost gap (15.8% TOLERATED); passive-overuse |
| S3.5 ruleset | r1 + r2 | RULESET-CLEAN (r2) | non-action-verb deny-list violations cleared in r2 |
| S4 continuity | r1 + r2 | SEASON-CONTINUITY-OK | reachability + state + reference + POV — clean after r2 |
| S5 voice | r1 | VOICE-COHERENT | clean first pass |
| S6 vibe — dark-fantasy-reader | r1 only | **VIBE-DRIFT-procedural-recurrence** | ledger-sequence fatigue (carry-forward, never re-passed) |
| S6 vibe — pulp-enthusiast | r1 only | (vibe-aligned per file inspection) | — |
| S6 vibe — worm-canon-pedant | r1 only | **VIBE-DRIFT-shard-load-suppressed / organism-texture-underweight** | shard-load suppression late-stretch; carry-forward |
| S7 facet-readiness | r1 + r2 | FACET-READY | over-dense + under-dense stretches resolved in r2 |
| S8a character plausibility | r1 + r2 | **IMPLAUSIBLE** — 1 finding carried forward (Elara visit) | Elara persona-card information-suppression pattern violated |
| S8b event plausibility | r1 + r2 | PLAUSIBLE (r2) | reeve-as-membrane framing in cond-smallfolk-political-physics resolved 3 prior implausible-event findings |
| S9 comprehensibility — dark-fantasy-reader | r1 only | **COMPREHENSIBILITY-RISK-attention-early-baseline-gap-density** | 2 consecutive BORED windows 60–100; 30%+ gap density 60–159 |
| S9 comprehensibility — pulp-enthusiast | r1 only | (comprehensible per file inspection) | — |
| S9 comprehensibility — worm-canon-pedant | r1 only | (comprehensible per file inspection) | — |
| Phase 4 split — dramatist | r1 only | proposed 6-episode split (251/418/563/699 cuts) | within-band for e01,e02,e04,e05; e03=168 (over 160); e06=213 (over 160) |
| Phase 4 audience — dark-fantasy-reader | r1 | SPLIT-ACCEPT | — |
| Phase 4 audience — pulp-enthusiast | r1 | **SPLIT-REVISE-E02-CLOSE-AND-E05-SHAPE** | named two seams: e02 close lacks earned next-open; e05 shape reads as slice |
| Phase 4 audience — worm-canon-pedant | r1 | SPLIT-ACCEPT | — |

**Aggregate convergence call:** Phase 3 was declared CONVERGED with three live carry-forward signals (S6 dark-fantasy, S6 worm, S8a character) and one Phase 4 SPLIT-REVISE that was not re-iterated. The shipped state is "converged with named residuals" — not "fully clean."

---

## Where the existing review *did not* press

Reading the rubric and the audit reports together, the following categories of failure were under-covered or uncovered:

### Gap 1 — Episode-shape mechanic for Phase 4 Step 2

The rubric names verdicts (`OPEN-ENGAGES`, `CLOSE-EARNS-NEXT`, `SHAPE-COHERENT`) but does not formalize how to test them. Pulp surfaced "E02 close lacks earned next-open" and "E05 shape reads as slice" — both genuine observations — but the rubric gave him no mechanic for triaging or quantifying. Other personas may have had the same intuitions and not recorded them.

**Audience attack vector:** for each of e01–e06, can the persona name a specific seam at the open and at the close that *would* fail the verb in `OPEN-ENGAGES` / `CLOSE-EARNS-NEXT`?

### Gap 2 — Cross-episode continuity post-split

S4 covers continuity inside the aggregate. The rubric does **not** describe a continuity check across the post-split episode boundaries. State carryover from `s01e01.md` close → `s01e02.md` open is implicitly covered by the `aggregate_range:` contiguity check, but a reader experiencing the split as one-episode-then-pause-then-next-episode meets a different surface than a reader experiencing the aggregate continuously. No rubric pass tests this.

**Audience attack vector:** for each of the 5 boundaries (e01→e02, e02→e03, e03→e04, e04→e05, e05→e06), what state, prop, monument, or relationship would a reader expect to be carried across the cut that *isn't* visible at the open of the next episode?

### Gap 3 — Episode boundary placement quality (separate from continuity)

Same 5 boundaries, but attacked for *placement* rather than carry. Could a cut a few lines earlier or later carry a stronger close + stronger open? The rubric leaves this implicit in Step 1 dramatic-shape criterion `(b)`, with no explicit re-attack vector.

**Audience attack vector:** for each cut, is the cut at the strongest available close-line in its neighborhood (±20 lines), or is there a stronger candidate the dramatist's proposal missed?

### Gap 4 — S6 vibe-drift escalation

Two of three personas flagged drift in S6 r1; the run shipped with carry-forward notes rather than re-passing. The rubric says "≥2-persona threshold for accepting drift flags" — this was met — but the resolution path is unclear: do drift findings route to fixer? screen-writer? Or is "carry-forward" the rubric-permitted close? The rubric does not say.

**Audience attack vector:** for each S6 carry-forward (procedural-recurrence ledger-fatigue; shard-load-suppressed; organism-texture-underweight), can the persona name a specific stretch range where the drift is concentrated and a specific seam at that range?

### Gap 5 — S8a/S8b split verdicts

S8a (character) and S8b (event) on the same beat (Elara visit) returned different terminal verdicts (IMPLAUSIBLE vs PLAUSIBLE). The rubric does not describe what to do when the character and event lenses disagree. The shipped state takes both at face value.

**Audience attack vector:** is the shipped state honest? A reader doesn't compute character vs event separately — they read one beat. If S8a flagged a character implausibility and S8b cleared it, the seam is whether the character read survives in the prose downstream.

### Gap 6 — Two entertainment-density thresholds in conflict

S3 caps at "~10% of windows TOLERATED, zero BORED, two consecutive BORED → REVISE."
S9 caps at "≥30% of any 100-line stretch BORED-or-TOLERATED → COMPREHENSIBILITY-RISK."

The two are non-equivalent (S3 stricter on BORED count and consecutive runs; S9 stricter on aggregated density across 100 lines). On s01, S3 ACCEPT was reached after multiple revisions; S9 still triggered (dark-fantasy-reader). Either both thresholds are correct and serve different purposes (entertainment cap vs comprehensibility floor) — in which case the rubric should say so explicitly — or they should converge.

**Audience attack vector:** is there a stretch in the aggregate where S3 ACCEPT-clean coexists with a S9 risk that the rubric should have surfaced earlier?

### Gap 7 — Adversarial criteria at season scope

The rubric does not separately define what "season-scope adversarial" means for each of the three personas. Per-line and per-episode adversarial habits are implicit in the persona cards; season-scope habits (multi-stretch arc-fatigue, escalation-curve plausibility, monument-callback debt) are not separately documented.

**Audience attack vector:** each persona attacks the season aggregate as ONE object, looking for fatigue, repetition, and cost-deferral across the full 1–912 range — categories per-line attack does not surface.

### Gap 8 — Narrator-field anomaly on e05/e06

The /and-season Phase 4 Step 3 spec says `narrator:` is "the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch." Per the aggregate's POV markers:

- s01e05 stretch 564–699 = Taylor (564–670, 107 lines) + Mira (671–699, 29 lines). Dominant: Taylor.
- s01e06 stretch 700–912 = Taylor (700–833, 134 lines) + Elara (834–912, 79 lines). Dominant: Taylor.

The shipped per-episode files name Mira (e05) and Elara (e06) as `narrator:`. **The split appears to have applied an "interlude is the narrator" rule that the rubric does not state.** Either the rubric is wrong (the spec should say "interlude POV wins when present") or the split is wrong (the field should be Taylor). Tuning-r1 must surface this; Phase G will scan it as METADATA-INCONSISTENCY.

---

## What Phase C will produce

Each persona dispatch attacks the 18 units identified in `A-corpus.md` under the locked rubric, producing per-unit seams. The 8 gaps above are the surface area each persona is told to press.

**Persona attack lenses (from existing audience cards + season-scope extension):**

- **dark-fantasy-reader** — atmosphere drift across the season; procedural recurrence; tonal flatline; cost-not-landing.
- **pulp-enthusiast** — momentum dead zones; board-change visibility at boundaries; close-earns-next quality.
- **worm-canon-pedant** — voice-fidelity drift across multi-episode arcs; shard-load misregister; cost-language vs discipline-language.

Each persona reads ALL 18 units and produces one strongest seam per unit. Forbidden: persona may not propose deletes, may not write new bones, may not redirect to another phase. Adversarial scope is attack-only.

---

## Phase B complete

Proceed to Phase C.
