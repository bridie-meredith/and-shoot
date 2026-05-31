---
audit: facets-final-r1
episode: b01c06
date: 2026-05-30
mode: flag-only
status: FINDINGS-PRESENT
totals: 12 findings across 6 facets
---

## STRUCTURAL findings (2)

- [state:--] consolidated file — The state-updates.md consolidated file uses a non-standard double-frontmatter form: the top-level frontmatter block (`sources: [env, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]`) is followed by three additional `---`-delimited per-source frontmatter blocks inside the file body. The schema (§ Rubric carve-out preamble, V3) permits per-source markers but specifies `# source: <slug>` comment-headers, not YAML frontmatter blocks. The three inner `---` fences parse as multiple YAML documents or as raw content depending on the parser. This is a **SIGNAL** (build_cite_index.py tolerates it; downstream risk is parser-dependent breakage if a stricter YAML consumer is introduced). Routing: state-updates author (studio + taylor-hebert-kl-122ac forks).

- [state:--] cite-index token collision — The cite-index lists `state:1 @6` (env source) and `state:13 @4` (taylor source), which are distinct entries in the consolidated file but share the `state:` prefix in the citation namespace. The per-source renumbering after consolidation assigns IDs monotonically across sources: env entries 1–12 and taylor entries 13–17. The bones file proto-lines carry `[state:1]` at both @4 (original uncombined token from the taylor slice's `state:1`) AND @6 (env slice's `state:1`). The cite-index shows both tokens resolved: `state:1 @6` (env) and `state:13 @4` (taylor, post-renumber). The proto-lines file was authored with per-slice local numbering before consolidation renumbered; if the canonical proto-lines file (post-merge) still carries `[state:1]` at @4 meaning the pre-renumber taylor entry, that token will resolve to the env entry `state:1 @6` instead of `state:13 @4`, producing a citation mismatch. This is the **token collision seam** noted in the dispatch. Adjudication: the cite-index shows `state:13 @4 back=N` confirming the renumbered form exists in the index; the bones proto-line file header carries `state:1` (not `state:13`) at @4. This is an **accepted tooling artifact** consistent with the c05 precedent the dispatch confirms — the cite-index builder resolves post-renumber IDs correctly as the authoritative lookup table, and the pre-merge per-slice tokens in bones are the source of the discrepancy. Per the c05 ruling: **SIGNAL** (not a STRUCTURAL bidirectional-citation HARD; the index is the truth surface; the bones file carries pre-consolidation tokens that the index disambiguates). Routing: showrunner / cite-index tooling (note for build_cite_index improvement: post-consolidation token back-patch in bones).

---

## FREQUENCY-BAND findings (2)

- narrator-interest (NI): actual 7/25 = 28%; band 15–25%; **breach-high**. Justified stretch: the two entries over the 25% ceiling (narrator:6 @12, narrator:7 @19) are HARD-required cross-facet co-cites — mem:1 @12 and mem:2 @19 require NI spine on a climax-shape chapter (V3 feel-as-spine carve-out does not apply; dramatic_shape: climax). The R2 NI shard explicitly declined the @17/@18 add on band-cap grounds, landing at 7 (not 8). The stretch is driven by HARD cross-facet spine obligations, not density-on-flat contamination — every entry fires on a peak-adjacent or spine-anchor beat. Ruling: **SIGNAL** (advisory; breach is justified and the minimum compliant with the HARD co-cite constraint; the @17/@18 add-decline is the disciplined floor). Author: interest-narrator.

- sensory: actual baseline 2/25 = 8% before grounding exemptions; post-exemption effective count 5/25 = 20%. Grounding-ledger exemption check: sensory:3 carries `licensed-grounding-exception: grd-001`; sensory:4 carries `licensed-grounding-exception: grd-002`; sensory:5 carries `licensed-grounding-exception: grd-003`. All three grd-NNN tokens resolve to `status: satisfied` entries in the grounding-ledger (grd-001 `satisfied_by: sensory:3`; grd-002 `satisfied_by: sensory:4`; grd-003 `satisfied_by: sensory:5`). **All three licensed-grounding-exceptions resolve. Entries 3–5 are EXEMPT from the frequency-band cap per PROP-0022.** Counting only unlicensed entries: 2/25 = 8%; band 3–6%; **breach-high on the unlicensed-only count.** Note: sensory:1 @4 and sensory:2 @5 are both scene-A entries (2 in scene-A = 2/9 bones = 22%, over the ≤3-per-scene cap reads as within; scene-A has 9 bones; 2 entries is under 3 per-scene cap — PASS). The 8% unlicensed-entry count breaches the rubric band. **SIGNAL** (the breach is 2 entries, both scene-A; no immediate downstream consequence, but the base-before-exemptions is above the 3–6% band target). Routing: studio (sensory author).

---

## METADATA-INCONSISTENCY findings (1)

- [metaphor:--] file — metaphor.md line 90 states: "Multi-justification: feel:2 (anchor) + narrator:5 (NI co-cite support) = 2 resolvable layers. (R1's provisional tens:1 support stripped by orchestrator under URI-SUBSTANCE-OVERHAUL — tensometer is dropped; tens:1 resolves to nothing. The two valid layers feel:2 + narrator:5 satisfy the ≥2 requirement.)" This is internally inconsistent: the file's earlier R2 verdict block (lines 63–64) states `licensed-by: feel:2 +narrator:5` as the resolved anchor, and the R2 decision shard states `feel:2 (anchor, 1 layer from {feeling}) + +tens:1 (support, 1 layer from {tens}) = 2 — requirement ≥2 satisfied`. The entry field itself reads `licensed-by: feel:2 +narrator:5`. The file-shape audit section (line 90) says tens:1 was stripped and only feel:2 + narrator:5 remain; the R2 shard says tens:1 is a retained support layer. The entry `licensed-by:` field does not show tens:1 at all. The multi-justification tally explanation is inconsistent across the three locations. **SIGNAL** (the entry itself is `feel:2 +narrator:5` and the ≥2 requirement is satisfied by feel:2 alone as the anchor; narrator:5 as NI co-cite support is additional; the functional conclusion is unaffected regardless of whether tens:1 is in or out). Routing: metaphor author (editor) — clarify the file-shape audit note for consistency with the entry.

---

## CURVE-SHAPE verdict

- **Episode-level: SHAPE-OK.** dramatic_shape: climax. Scene-map shows three scenes: scene-A `rising-to-peak`, scene-B `flat-mid`, scene-C `rising-to-peak`. The climax structure is: first peak cluster in scene-A (relational +1.0 / omission authored), loaded pause in scene-B (no peak-bones; form held unsent), rising-to-final-peaks in scene-C (moral_framework -1.0 / moral_legibility_to_self +1.0). This is a valid climax shape — the chapter's central event (first named-person delivery + the un-priced omission contrast) lands at the scene-C peaks after a build. No flat-low zones exist; no 3→3 sequences across all three scenes; no 30+ contiguous flat stretches. SHAPE-OK.
- **Per-scene:**
  - scene-A (1–9): rising-to-peak — peak-bones @4 and @8 present. PASS.
  - scene-B (10–15): flat-mid — peak-bones: none. PASS (climax chapter permits a loaded-pause flat zone; the non-send IS the scene's function).
  - scene-C (16–25): rising-to-peak — peak-bones @22 and @24 present. PASS.
- **Adjacency:** no 1→3 or 3→3 jumps detectable from the scene-level rhythm data. Each peak cluster is bounded by approach and shadow bones.
- **Flatlining:** scene-B runs @10–@15 (6 bones), well under the 30-bone flatline threshold.

---

## CONTRADICTION findings (0)

No contradictions found. State-updates chain: oc-ward-coverage-notes opens at @6 → blanked at @8 → closed at @9 → re-opens at @24 → closes at @25; open/close transitions are sequential and non-overlapping. oc-jarvis-channel-form filled @14 → lowered-unsent @15 → sealed @22 → holder transferred @23; sequential, no contradiction. actor:taylor moral_framework_axis 1→0 fires once at @22; relational_anchor_status_axis 2→3 fires once at @4; moral_legibility_to_self_axis 4→5 fires once at @24. All single-fire scalar axes. No two facets set incompatible state on the same anchor.

---

## DEDUP findings (1)

- [narrator:6] @12 — partial overlap candidate with [mem:1] @12. Both entries register the same cognitive beat: the names-vs-patterns category-crossing on the re-read. narrator:6: "the unit has changed under her hand — a node holds frequency and heading… a name holds a body the heading can find; she has moved bodies along a record before, and the record was always the route." mem:1: "the read is already done and what the ask wants is the bodies pulled out of the pattern and set down as names, the way bodies were set into a record once and the record became the route they were moved along." The R2 shard explicitly adjudicated this (DEDUP check in memory shard: spine and monument-content consistent, no contradiction; the two layers serve different rubric functions — NI is register/cognition, memory is monument-trigger/displacement-cue). Ruling: **SIGNAL** (the content overlap is the intended doubled-register mechanism; the R2 adjudication is documented and on-record; cross-facet same-anchor co-location is the rubric-licensed design for this beat). Routing: no action; noted for Phase 5b audience seam-finding.

---

## SUPERFLUOUS findings (2)

- [loc-state:1] @1 — lonely (no co-cites, no inbound license per cite-index). Rubric scrutiny: the anchor bone is @1 `the handcart blocks the lane-mouth` — the scene-map `world-before-protagonist open @1` protected-pattern. The loc-state entry establishes the chapter's opening environment (lane-mouth blocked, morning, handcart spanning full width, crowd compressed). This is the canonical loc-state fire position: environment at chapter-open is exactly what loc-state is for. The entry earns on necessity (no other facet carries the morning/blocked-lane establishment) and frugality (single entry, carries the full open). **PASS** — lonely is not superfluous here; rubric scrutiny clears. No finding.

- [sensory:5] @17 — lonely (no co-cites per stale cite-index). Grounding-ledger exemption check: `licensed-grounding-exception: grd-003` resolves to grounding-ledger entry grd-003 (anchor @17, `status: satisfied`, `satisfied_by: sensory:5`). Per the dispatch instructions and PROP-0022: **EXEMPT from SUPERFLUOUS/lonely scrutiny.** No finding on sensory:5.

  Remaining lonely entries (state:1 @6, state:3 @9, state:8 @20, state:10 @23, state:12 @25, narrator:3 @13, exposition:1 @0) evaluated:
  - state:1/3/8/12: all prop-state open/close entries on oc-ward-coverage-notes or oc-accounting-ledger. These are irreversible record-events the rubric explicitly expects state-update coverage for (§calibration anchor). The loneliness reflects absence of other facets at functional-transition bones (@6 open, @9 close, @20 close, @25 close), which is correct — these are operational beats with no peak-class decoration. **PASS** — lonely is not superfluous; each records an irreversible state transition at a non-peak bone.
  - state:10 @23: oc-jarvis-channel-form.holder transfer. Same reasoning — irreversible prop-transfer at a peak-shadow bone. **PASS**.
  - narrator:3 @13: lone NI entry at the pre-calc beat "the elders are already in the long-pattern record as nodes… the step the record has been waiting four months for her to take." R2 shard verdict: KEEP. Rubric scrutiny: rising-zone pre-calc surfacing is a licensed NI channel; the four-months specificity is the clinical-register tell; lonely because no co-facet fires at @13 (a functional beat). **PASS** — earns on attention/pre-calc licensing; no redundancy.
  - exposition:1 @0: prior-episode-bridge at the synthetic anchor. @0 is outside any co-citation network by construction. **PASS** — preamble entries are structurally lonely; this is expected.

  Summary of SUPERFLUOUS class: **0 findings** (all lonelies pass rubric scrutiny or carry grounding exemption).

---

## CONSTRAINT findings (3)

- [state:--] oc-* prop field-extension, margit-referrals SEAM-006/007/008 — state-updates entries state:1–3, 5–6, 9–12 (env source) target `prop:oc-ward-coverage-notes`, `prop:oc-jarvis-channel-form`, and `prop:oc-accounting-ledger`. No prop cards exist for any of these three slugs. The state-updates file documents this with a `# rubric-carve-out — field-extension for oc-* prop targets pending margit cards` preamble per schema § Rubric carve-out preamble protocol, with inline `# field-extension` tags on each affected entry and SEAM-006/007/008 margit-referral notes. Per rubric-fidelity severity calibration: documented author defense present → **SIGNAL** (not HARD). The margit referrals are outstanding and must be resolved before b01c07 facets. Routing: margit (SEAM-006: oc-ward-coverage-notes.card.md; SEAM-007: oc-jarvis-channel-form.card.md; SEAM-008: oc-accounting-ledger.card.md; priority: before b01c07 facets per state-updates carve-out annotation).

- [exposition:1] @0 — source-traceability audit: every claim in the gloss-text must trace to a `sources:` entry. Checking the prior-episode-bridge text: "Yesterday the coverage held" → chapters[b01c06].handoff_in (Flea Bottom intelligence routing: continuing) ✓; "intelligence kept flowing up the Jarvis line to Otto" → handoff_in open_threads ("Flea Bottom intelligence routing: continuing") + b01c03:3 jarvis-coin-kl-courier + otto-hightower/card.md ✓; "the arrangement that pays for the quiet on Sera's question" → b01c05 exposition:2 sera-protection-architecture ✓; "Movement patterns, not persons" → chapters[b01c06].chunk ("Movement patterns are what she has been delivering since d04") ✓; "This morning the count runs the Hook at its standard density" → chapters[b01c06].handoff_in.world_state + scene b01c06s01.chunk ✓; "The harm I can prevent is still the only column the accounting closes" → scene b01c06s01.chunk (harm-prevention framing) ✓; "The form is the same. What Otto asks for next will not be." → chapters[b01c06].chunk + actors/otto-hightower/card.md ✓. All claims trace. **PASS** — no source-traceability finding.

- [state:14] @8 and [state:2] @8 — same anchor, different sources. state:2 (env source) = `prop:oc-ward-coverage-notes.contact-source-field: unresolved -> blank-authored`. state:14 (taylor source pre-renumber) = `actor:taylor-hebert-kl-122ac.knowledge.body-map.wren-contact-source-field: unauthored -> authored-blank-ward-resident-hook-routine-name-withheld`. These two entries describe the same physical event (Taylor blanks the contact-source field) from two different targets (prop state vs. actor knowledge state). This is not a contradiction (they record different state targets) but a potential DEDUP between prop-state and actor-knowledge. Per the schema: `<target>` = `prop:<slug>` vs. `actor:<slug>` — these are distinct canonical-write-back surfaces. The prop records the instrument state; the actor-knowledge records the information composition. Both are required; the rubric-state-updates § Coverage justification supports dual-target on an irreversible record-composition event. **PASS** — cross-target dual record on an omission act is the correct pattern; no constraint violation.

  Summary: CONSTRAINT class net findings: 1 SIGNAL (oc-* prop carve-out, margit outstanding); no HARD findings.

---

## AP-SCAN findings (2)

- [narrator:2] @8 + [narrator:4] @22 — **AP-010 inverted-predicate template** ("the blank she writes is authored, not missing" / "the seal is the breach"). Two uses of the X-is-Y inverted-predicate chassis across the NI file. Per the NI rubric, the cap is ≤1 licensed single-use as a register-defining device. Both R2 shard and the dispatch flag this as a pre-existing R1 exposure (not introduced in R2; R2 adds narrator:6 @12 and narrator:7 @19 are authored clear of the chassis). AP-010 saturation check: 2 hits / 7 total entries = 29%. URI-AP-SCAN-SATURATION escalation threshold: ≥40% in a ≤25% band facet. 29% < 40% → **SIGNAL** (not HARD). Routing: interest-narrator author — if the chapter proceeds to Phase 5b without fixer action, narrator:4 @22 is the repair candidate (narrator:2 @8 is the licensed single use; the rubric cap is ≤1).

- [exposition:1] @0 — voice-register scan: the bridge text is first-person Taylor throughout ("the line I had been delivering on" / "since I agreed to it" / "The harm I can prevent"). No author-meta phrases detected ("in this episode" / "the reader" / "we'll see"). No third-person Taylor drift. No Earth-Bet proper nouns. No hollow-prose constructions. **PASS** — no AP-SCAN finding on exposition.

---

## TASTE-FLAG findings (1)

- [narrator:3] @13 — **voice-fidelity candidate**: "the elders are already in the long-pattern record as nodes — meeting-frequency, errand-direction, who they receive instruction from — and the ask is only that she convert nodes to names, which is the step the record has been waiting four months for her to take." The phrase "the step the record has been waiting four months for her to take" attributes agentive patience to the record (the record has been waiting). This is a mild figurative register that edges toward personification of the instrument. It is within Taylor's data-register POV (she would phrase operational readiness this way) but the auditor notes it as a **TASTE-FLAG: voice-fidelity** candidate — does the record's waiting read as Taylor's POV or as the instrument's? Signal-only; feeds Phase 5b seam-finding for the NI adversarial reviewer.

---

## PILE-UP REVIEW (4 pile-ups)

- **@24** (9 facets: feel:2, meta:1, narrator:5, state:5, state:11, vibes:12, vibes:13, vibes:14, vibes:15): `taylor-hebert-kl-122ac opens the ward-coverage notes` — verdict: **warranted**. @24 is the moral_legibility_to_self +1.0 peak-bone, the chapter's closing recognition beat (the two-substrate contrast: four names sent / Wren's blank still intact). The co-decoration is load-bearing: feel:2 (somatic latency before the open), meta:1 (the false-completion figure), narrator:5 (the structural contrast in two substrates), state:5/11 (the axis move + prop re-open), vibes:12–15 (two-substrate contrast vibe-cloud for 4 entity targets). Each entry fires on its own rubric grounds for a peak-bone of this magnitude. The pile-up is proportional to the bone's substance weight (moral_legibility_to_self +1.0 is the chapter's third axis move, at the terminal peak). No entry is redundant with another across facets (feeling=somatic / metaphor=figure / NI=cognition / state=canonical-record / vibes=operator-bias). Over-decoration would require two entries in the same register — none observed.

- **@4** (7 facets: narrator:1, sensory:1, state:1, vibes:1, vibes:2, vibes:3, wren-stitch-maker-flea-bottom-ward:1): `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac` — verdict: **warranted**. @4 is the relational_anchor_status +1.0 peak-bone, the first spoken Wren exchange, a dialogue-anchor bone. The pile-up is structurally expected: narrator:1 (Taylor's registration of the exchange), sensory:1 (sound spike of direct address), state:1 (relational axis move), vibes:1/2/3 (3-entity vibe fan-out: Wren ++ mutual-silence / Taylor + wren-as-named-speaker / episode + first-spoken-exchange), wren:1 (the dialogue utterance itself). Each fires in a distinct register. No duplication. Warranted for a relational peak-bone with a dialogue anchor.

- **@22** (7 facets: narrator:4, state:3, state:4, state:9, vibes:9, vibes:10, vibes:11): `taylor-hebert-kl-122ac seals the jarvis-channel form` — verdict: **warranted**. @22 is the moral_framework -1.0 peak-bone (the send; the breach). The pile-up structure: narrator:4 (pre-calc surfacing on the breach), state:3 (moral_framework axis move), state:4 (named-elder-delivery-record field flip), state:9 (oc-jarvis-channel-form prop sealed), vibes:9/10/11 (3-entity vibe fan-out on the send). Two state entries (state:3 actor-stats / state:9 prop-state) are different canonical targets (not duplication). Warranted at the chapter's moral breach peak.

- **@8** (6 facets: feel:1, narrator:2, state:2, vibes:4, vibes:5, vibes:6): `taylor-hebert-kl-122ac blanks the contact-source field` — verdict: **warranted**. @8 is the omission peak-bone (the un-priced protective move). The pile-up: feel:1 (the hand suspended before the blank), narrator:2 (the pricing of the authored blank), state:2 (the actor-knowledge field flip for the omission), vibes:4/5/6 (3-entity omission vibe fan-out). Four distinct registers. Warranted for the chapter's first ethical act peak.

---

## RUBRIC-FIDELITY findings (1)

- [memory:--] file — **monument-family diversity (SOFT seam, SIGNAL)**: the memory rubric targets ≥3 monument families for a >50-beat corpus; for a 25-bone chapter the rubric explicitly admits single operating residue with doubled-cue as within range. Both mem:1 @12 (Earth-Bet displacement / override-architecture-residue body-record face) and mem:2 @19 (Westerosi-monument-clamp / override-architecture-residue protective-arrangement-at-distance face) share a single underlying card: `cond-override-architecture-residue-122ac`. The R2 memory shard notes this as a SOFT seam (margit-split referral: monument-body-record-cognition + monument-protective-arrangement-at-distance as separate cards) — identical to the c05 seam. Per the rubric calibration, this is within range for a 25-bone chapter; single-monument-family-with-doubled-cue is rubric-admitted. **SIGNAL** (not HARD; rubric admits it; the doubled-register test passes — both Earth-Bet displacement AND Westerosi-monument-clamp fire). Routing: margit (SOFT split referral; deferred; carry from c05).

---

## Known-seam adjudications

**Seam 1 — memory @12/@19 NI co-citation (dispatch item 1):** CLEAN. cite-index shows `mem:1 @12 back=Y co=[narrator:6]` and `mem:2 @19 back=Y co=[narrator:7]`. Both spines are present in the post-R2 cite-index. The HARD dependency (missing-spine gate) is resolved. No finding.

**Seam 2 — narrator FREQUENCY-BAND (dispatch item 2):** Ruled SIGNAL (breach-high at 28%) per FREQUENCY-BAND class above. Justified by HARD cross-facet co-cite obligation; not density-on-flat.

**Seam 3 — AP-010 inverted-predicate recurrence (dispatch item 3):** Ruled SIGNAL at 29% saturation (< 40% threshold for HARD per URI-AP-SCAN-SATURATION) per AP-SCAN class above.

**Seam 4 — state-updates oc-* prop field-extensions (dispatch item 4):** Ruled SIGNAL per CONSTRAINT class above. Documented author defense present in the carve-out preamble. Margit referrals SEAM-006/007/008 outstanding.

**Seam 5 — sensory grounding adds (dispatch item 5):** grd-001/002/003 all resolve in the grounding-ledger (all `status: satisfied`); sensory:3/4/5 carry valid `licensed-grounding-exception` tags. **EXEMPT** from FREQUENCY-BAND cap and SUPERFLUOUS/lonely scrutiny. No FAULT-GROUNDING-LICENSE-DANGLING. CLEAN.

**Seam 6 — state proto-line token collision (dispatch item 6):** Ruled **SIGNAL** (accepted tooling artifact; consistent with c05 precedent; cite-index is the authoritative disambiguation surface; not a bidirectional-citation HARD). See STRUCTURAL class above.

---

## Audit summary

- Total entries reviewed: 53 facet entries + 1 dialogue entry + 25 proto-lines
- **HARD classes:** STRUCTURAL 0, FREQUENCY-BAND 0, CONTRADICTION 0, DEDUP 0, SUPERFLUOUS 0, CONSTRAINT 0, RUBRIC-FIDELITY 0
- **SIGNAL classes:** STRUCTURAL 2 (double-frontmatter form; token collision tooling artifact), FREQUENCY-BAND 2 (NI 28% justified; sensory 8% unlicensed), METADATA-INCONSISTENCY 1 (metaphor multi-justification note inconsistency), AP-SCAN 1 (AP-010 inverted-predicate 29% saturation in NI), DEDUP 1 (NI/memory @12 overlap — intended doubled-register), TASTE-FLAG 1 (NI:3 record-agentive phrase), RUBRIC-FIDELITY 1 (memory single-monument-family doubled-cue admitted)
- **Advisory items:** 1 margit referral set (SEAM-006/007/008, oc-* prop cards; priority before b01c07); 1 margit referral candidate (monument-class card split for cond-override-architecture-residue-122ac)
- **CURVE-SHAPE:** SHAPE-OK (climax chapter; scene-A rising-to-peak / scene-B flat-mid / scene-C rising-to-peak; all scene-level rhythms coherent with declared dramatic_shape)
- **F-R2 discipline-fail summary:** f-r2-1 0; f-r2-2 0; f-r2-3 0; f-r2-4 0 (per consolidated .r2-decisions.md frontmatter; 0 discipline fails; 0 arbiter interventions). Orchestrator-critic F-R2-1 threshold (>0 = HARD) is clear; B7 threshold (f-r2-2 + f-r2-3 + f-r2-4 > 2 = SIGNAL) is clear.

## Routing

| Finding | Facet | Author | Action |
|---|---|---|---|
| STRUCTURAL: double-frontmatter form | state-updates | studio + taylor fork | SIGNAL; no block |
| STRUCTURAL: token collision | state-updates / cite-index tooling | showrunner / build_cite_index | SIGNAL; no block |
| FREQUENCY-BAND: NI 28% | interest-narrator | taylor-hebert-kl-122ac impersonator | SIGNAL; justified; no block |
| FREQUENCY-BAND: sensory 8% unlicensed | sensory | studio | SIGNAL; no block |
| METADATA-INCONSISTENCY: metaphor multi-justification note | metaphor | editor | SIGNAL; no block |
| AP-SCAN: AP-010 narrator:2/@8 + narrator:4/@22 | interest-narrator | taylor-hebert-kl-122ac impersonator | SIGNAL; narrator:4 is repair candidate if Phase 5b flags |
| DEDUP: narrator:6 + mem:1 @12 | interest-narrator / memory | both | SIGNAL; intended doubled-register; Phase 5b seam-finding |
| TASTE-FLAG: narrator:3 record-agentive | interest-narrator | taylor-hebert-kl-122ac impersonator | SIGNAL; Phase 5b |
| CONSTRAINT: oc-* prop carve-out | state-updates | studio + margit | SIGNAL; margit SEAM-006/007/008 before b01c07 |
| RUBRIC-FIDELITY: memory single-monument-family | memory | taylor-hebert-kl-122ac impersonator + margit | SIGNAL; margit split referral deferred |
| Pile-ups @24/@4/@22/@8 | all | — | warranted; no block |
