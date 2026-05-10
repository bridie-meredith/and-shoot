audit: facets-final-r2
episode: s01e01
date: 2026-05-10
mode: flag-only
status: FINDINGS-PRESENT
totals: 5 findings (2 hard flags, 3 soft flags) — down from 7 in r1 (4 hard faults remediated; 2 new soft flags introduced by remediation-adjacent inspection; 3 prior soft flags carried forward)

---

## Remediation verification (4 prior hard findings)

- [loc-state:5/6] CONTRADICTION → CLEARED — time-label sequence now reads dawn(@1) → morning(@8) → afternoon(@32) → dusk(@58) → evening(@61) → late-evening(@92) → night(@126) → late-night(@130); fully monotonic; no backward progression anywhere in the 8-entry chain.
- [vibes:5] CONSTRAINT forward-cite → CLEARED — feeling:4 stripped from licensed-by; current sources are memory:4, state-update:13, tens:2; all three resolve at or before anchor @119; no forward-citation present.
- [meta:1] CONSTRAINT tens-curve → CLEARED — metaphor.md now has zero entries; r2_audit_remediation block in the file confirms deletion; cite-index corroborates (meta: 0 entries); @69 pile-up count drops from 6 to 5, warranted.
- [tens:21] SUPERFLUOUS → CLEARED — re-rated 2 → 1 in tensometer.md (annotated comment present); cite-index confirms r=1, no back-citation; @25 proto-line no longer carries the tens:21 back-cite.

---

## CONTRADICTION findings (0)

None. Location-state time progression is monotonic post-remediation (verified above). Cross-facet state sequences (tallow-lamp: unlit→lit→guttering→dark; winter-candle: stored→drawn→lit) are internally consistent and non-contradictory.

---

## DEDUP findings (2)

- [flag-001] type: flag — **mem:5 @9 / narrator:26 @9 near-paraphrase.**
  - what: mem:5 text is "the feet land at a spread the body inside the body has not yet sized down to → cond-reincarnation-mechanics-84ac"; narrator:26 text is "the feet plant at the spread the body had not yet sized down to." Both fire on @9; both render the body-sizing-to-spread figure; both use the "had/has not yet sized down to" construction.
  - why: Memory rubric requires the callback clause to describe the callback in its own register — not to paraphrase the NI content with a target appended. The surface difference ("land at a spread the body *inside* the body" vs "plant at the spread the body") is real but thin; the semantic territory is identical. If the stitcher renders both, the same figure appears twice on the same beat. At minimum, the downstream operator receives duplicate signal on this anchor.
  - disposition: soft flag. mem:5 adds the "body inside the body" doubled-register figure absent from NI:26, and the condition-card target reference is the memory's distinct functional contribution. The canonical distinction (NI = perceptual register; memory = callback activation) holds, but the similarity is close enough to warrant author review at and-wrap.

- [flag-002] type: flag — **mem:8 @131 / narrator:25 @131 similar-language overlap.**
  - what: narrator:25 text is "the second mark closes the day the first one opened"; mem:8 text is "the second stroke closes what the first stroke opened; the day has the shape of a thing already filed → e01:99." Both fire on @131; both use the "second X closes... first X opened" construction; the NI uses "mark," memory uses "stroke" (same semantic register in context).
  - why: The memory adds a second clause ("the day has the shape of a thing already filed") and the intra-episode callback target (e01:99), which distinguishes it from pure paraphrase. However the first clause of mem:8 is a near-restatement of narrator:25. The memory rubric's content requirement is "one-clause description of the callback → target reference" — the callback description should function independently, not as a slight rephrase of the NI. At stitch, the reader encounters "the second mark closes the day the first one opened" (from NI:25) followed by equivalent semantic content (from mem:8's first clause). The callback's second clause ("the day has the shape of a thing already filed") is the only genuinely distinct content.
  - disposition: soft flag. The callback's second clause and target reference provide functional differentiation. Not a fault under mode: flag-only. Author should assess at and-wrap whether mem:8 can be reshaped to foreground the callback distinction rather than partially restating NI.

---

## SUPERFLUOUS findings (0)

No new superfluous findings. Post-remediation review confirms:
- All lonely entries (loc-state:5, loc-state:6, narrator:2, sensory:2, state:7, feel:13, feel:14) earn under their respective rubrics (time-advancement frame anchors, approach-zone fauna-feed establishment, genuine sensory delta, canonical state-change, Q1/Q2-clean somatic tells with multi-justification ≥3/5).
- vibes:19 and vibes:21 carry `@-` anchor (no on-screen beat) — correctly structured as world-build/reflective-pass entries per the vibes schema; anchor is optional for off-screen licensed entries.

---

## CONSTRAINT findings (3 — all soft, carried forward from r1)

- [flag-003] type: flag — **mem:2 @35 approach-zone quiet-beat (carried from r1).**
  - what: mem:2 fires at @35 (tens=2). The first 3-peak in the episode is @83. @35 sits in an ascending approach zone with no prior 3-peak; it is not a trailing-edge release-zone 2-beat. The memory rubric classifies approach-zone 2-beats as "contested; require explicit argument that the monument is reaching backward, not forward." No such argument appears in the file.
  - why: Approach-zone 2-beats at memory are permissible only with explicit rubric argument. Absent the argument, the entry is formally contested. Downstream: the stitcher may render a memory callback at a pressure beat where the rubric prefers quiet zones or trailing-edge release zones.
  - disposition: soft flag (carried). Functional registers remain strong (social commentary on smallfolk-under-institutional-shadow; the suppression-apparatus first-paper recognition). Not routed to fixer unless escalated to fault.

- [flag-004] type: flag — **mem:3 @69 approach-zone quiet-beat (carried from r1).**
  - what: mem:3 fires at @69 (tens=2). @67 is also tens=2; @83 is the next 3-peak. @69 is an approach-zone 2-beat, not a release-zone. The memory rubric requires explicit argument for approach-zone fires. The file records no such argument.
  - why: Same downstream risk as flag-003. The somatic-stilling monument (Earth-Bet cape-reflex / trained-body) is activated by the stilling beat, and per-scene cap is honored. The multi-justification defense is substantially present (somatic-tell + NI:14 spine + monument-trigger + functional register ≥2). Flag rather than fault; the functional case is strong.
  - disposition: soft flag (carried).

- [flag-005] type: flag — **mem:8 @131 rising-2 at episode close (carried from r1; additional internal-consistency note).**
  - what: mem:8 fires at @131 (tens=2). @130 is tens=1 (the candle-catch beat). @131 is a rising 2-beat at episode close, not a trailing-edge release-zone. The memory rubric permits "trailing edge of tens=2 (release-zone, settling-after-the-spike)" but classes "rising-2-beat at episode-final" as contested. Additionally, the memory.md R3 round-note claims "quiet-beat anchor 8/8 (all tens=1 or tens=2-trailing-edge)" — this claim is internally inconsistent: mem:8 at @131 is tens=2 rising (not trailing), contradicting the file's own metadata assertion.
  - why: The inconsistency in the file's own round-note metadata is a traceability concern — it states all 8 memory anchors pass the trailing-edge test when mem:8 demonstrably does not. At stitch, if the stitcher weights memory fires differently based on quiet-beat vs approach-zone classification, the incorrect metadata could misdirect. The intra-episode callback target (e01:99) is a mitigating factor — this is a resolution beat, not a pressure-escalation monument, and episode-close positioning gives it structural cover.
  - disposition: soft flag (carried). The internal metadata inconsistency is the new element in r2; author should correct the round-note claim at and-wrap.

---

## PILE-UP REVIEW (7 candidates, all warranted)

Post-remediation pile-up count (>4 co-located facets):

- **@99** (15 facets) — verdict: **warranted.** Structural climax (tens=3): five simultaneous canonical field-mutations, seven vibes on distinct targets with distinct licensed-by chains, NI + feeling + tensometer close the set. Density is structurally mandated by the irreversibility and fan-out scope of the mark-setting act. No change from r1.

- **@35** (9 facets) — verdict: **warranted.** Market-slip draws the documentary mechanism to the surface for the first time; nine entries across nine distinct jobs (three-actor vibes on record-as-clock, two state-updates tracking slip movement, memory for suppression-apparatus activation, feeling on all three actors). No change from r1.

- **@119** (7 facets) — verdict: **warranted.** Intimate-cost beat fanned across two actors; six of seven entries remain clean (vibes:5 forward-cite finding was the prior r1 defect; now remediated). All sources resolve at or before @119. No residual defect.

- **@69** (5 facets, down from 6 after meta:1 deletion) — verdict: **warranted.** NI:14, mem:3, vibes:4, vibes:13, and tens:52 all independently licensed for this beat. meta:1 correctly absent. The underlying 5-facet decoration is earned.

- **@130** (6 facets) — verdict: **warranted.** Two real state-mutations + sensory inflection + loc-state frame turnover + NI + vibes:17. All independently licensed; cluster reflects genuine multi-dimensional state-change at a defined transitional beat. No change from r1.

- **@8** (5 facets) — verdict: **warranted.** Real env state-change + loc-state morning-frame + sensory inflection + NI + vibes:16. Five entries, five distinct jobs. No change from r1.

- **@83** (5 facets) — verdict: **warranted.** tens=3 peak; NI + two state-updates on distinct targets + feeling:6. Lean for a 3-beat; no over-decoration. No change from r1.

---

## Audit summary

- Total entries reviewed: 202 facet entries across 9 facet files (102 tensometer + 8 loc-state + 24 NI + 5 sensory + 22 state-updates + 8 memory + 12 feeling + 0 metaphor + 21 vibes; note: cite-index total is 202, down 1 from r1's 203 due to meta:1 deletion)
- CONTRADICTION: 0 (was 1 in r1; cleared)
- DEDUP: 2 soft flags (new in r2)
- SUPERFLUOUS: 0 hard findings (tens:21 cleared; no new superfluous entries)
- CONSTRAINT: 3 soft flags (all carried from r1; internal metadata inconsistency in mem:8 round-note is a new detail)
- PILE-UP REVIEW: 7 warranted (meta:1 deletion resolves the prior over-decoration flag at @69)

## Routing (flag-only mode — no fixer dispatch required)

- **[flag-001, flag-002]** DEDUP soft flags → taylor-hebert-jaehaerys impersonator (memory author) at and-wrap — review whether mem:5 and mem:8 can be reshaped to foreground their callback distinction from NI without increasing surface similarity.
- **[flag-003, flag-004, flag-005]** CONSTRAINT soft flags (mem:2, mem:3, mem:8) → taylor-hebert-jaehaerys impersonator (memory author) at and-wrap — unchanged routing from r1. flag-005 adds: correct the R3 round-note metadata claim ("all tens=2-trailing-edge" is false for mem:8).

## Mode note

This audit ran in flag-only mode per dispatch. No deletes executed. All findings are advisory. The 4 prior hard findings are confirmed cleared. 5 new/carried flags are advisory for and-wrap.
