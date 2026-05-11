---
audit: season-tuning-r1
date: 2026-05-10
scope: /and-season s01 corpus + E-defense routing proposals
locked-rubric: design/shoot-v2/and-season-tuning-r1/rubric-and-season.md
auditor-model: claude-sonnet-4-6
---

# Season Tuning R1 — Auditor 11-Class Scan

## File-level verdict

HARD-FINDINGS: 5
SIGNAL-FINDINGS: 10
overall: FAIL-HARD-FINDINGS

---

## Findings by class

### Class 1 — STRUCTURAL

**fault-001** [HARD] Aggregate file contains out-of-monotonic-order IDs in the e01 region. IDs 922, 924, 930, 931, 916, 935, 926, 925, 927, 928, 932, 919, 920, 921, 923, 904, 905, 906, 907, 910, 911 appear interspersed within the main sequence (e.g., IDs run: 32, 34, 35, 922, 37, 38, 39, 40, 42, 924, 43, 930, 44... and later 935 for the apprentice mark, 926 for an entry at the 120s range, 916 for a fly-touch in the 40s region). The schema states "monotonic positive integer, file-scoped." The aggregate is season-scoped (flat, single-file), so monotonic applies to the file. These 900-range IDs appearing mid-sequence within the 1-250 content region are non-monotonic. A fixer computing `aggregate_id = aggregate_range_start + episode_id - 1` will produce incorrect mappings for any episode that covers these out-of-order IDs. (active-project/theater/proto-lines/s01.aggregate.md, lines approximately 47, 54, 56, 60, 64, 126, 138, 248, 252, 272, 734, 819, 941, 1021, 1035) — citation: schemas/proto-line.schema.md §Field rules / `<id>`: "Monotonic positive integer, file-scoped."

**fault-002** [HARD] s01e01 per-episode file header shows `aggregate_range: 1-149`. E-defense Phase E (U12, REVISE) routes this to showrunner-self: update to `1-148`. The file has NOT been updated — E-defense explicitly states no corpus files were modified in Phase E. The current aggregate_range in the per-episode file is inconsistent with the E-defense decision. Post-E execution has not run. This is a pending-execution fault, not yet a corpus fault — but it is a discrepancy between the decision record (E-defense.md, U12) and the current file state. (active-project/theater/proto-lines/s01e01.md line 9) — citation: Phase 4 Step 3 "aggregate_range: contiguous and non-overlapping with sibling ranges; union of all ranges equals 1..N."

Note: fault-002 is a pre-execution state gap. The E-defense decision is correct; the fault is that it has not been applied. If Phase G runs after Phase F execution, this would be resolved. It is classified HARD because the current file state fails the aggregate_range validation rule.

**fault-003** [HARD] s01e06 per-episode file contains a second internal `# pov: taylor-hebert-jaehaerys` marker at file line 101 (between episode body lines 88 and 90). The aggregate contains the corresponding marker between aggregate IDs 787/920 and 789. The per-episode file correctly copies this marker through. However: the schema says "body comment-clean per proto-line schema (POV markers excepted; copied through from the aggregate)" — this is compliant. RECLASSIFY from HARD to SIGNAL. See signal-001 below.

(Reclassification note: fault-003 is not a hard fault. The schema explicitly licenses POV markers in the body. No HARD finding here.)

**signal-001** [SIGNAL] s01e05 body begins with `# pov: mira-stonefield-jaehaerys` at episode file line 13 (between episode line 2 and episode line 3). Episode line 1 is blank; episode line 2 is `mira-stonefield-jaehaerys enters the alley`. The pov marker is not at the very first line of the body — two episode lines precede the marker before Mira's POV is formally declared. Per schema, the marker should be at or before the first line attributed to that POV character. The line immediately before the marker (episode line 2: `mira enters the alley`) is already a Mira-POV action — so the marker is one position late (the first body action already assumes Mira POV). This is interpretive rather than a clear schema violation, since the schema only says markers are "required" at transitions and "copied through from the aggregate." In the aggregate, the marker sits between aggregate IDs 563 and 565 — before the first Mira body action — which is schema-compliant. The per-episode file's episode line 2 (the first body action) precedes the marker. This is a copy-through ordering drift. (active-project/theater/proto-lines/s01e05.md lines 12-13) — citation: rubric Phase 4 Step 3 "Body comment-clean per proto-line schema (POV markers excepted; copied through from the aggregate)."

**signal-002** [SIGNAL] s01e03 aggregate_range 251-418 = 168 lines. s01e06 aggregate_range 700-912 = 213 lines. Both exceed the 160-line default band ceiling named in Phase 4 Step 1(a). The rubric states "default target band: each episode 80-160 proto-lines" and "all proposed episodes within the band." e03 at 168 is 8 lines over; e06 at 213 is 53 lines over. E-defense addresses e06 over-band through U16 (revise close to ~692, then boundary-rebalance to dramatist). E03 over-band is not directly addressed by a Phase E REVISE — the U4 REVISE closes e03 at aggregate 370 (120 lines, bringing e03 within band) but then inflates e04 to 193 lines. The e03 over-band in the current corpus is a pre-execution finding. (active-project/theater/proto-lines/s01e03.md line 9; s01e06.md line 9) — citation: Phase 4 Step 1(a) "default target band: each episode 80-160 proto-lines."

Previously identified: A-corpus Phase 4 split snapshot. Signal only (rubric says "default" not hard maximum; E-defense Phase E routes e03 and e06 over-band through boundary-rebalance subtasks).

**signal-003** [SIGNAL] Episode count = 6. 6 is a multiple of 3. Compliant. NO FINDINGS beyond confirmation.

---

### Class 2 — FREQUENCY-BAND

**fault-004** [HARD] s01e05 aggregate_range 564-699 (136 aggregate IDs). Within the 80-160 band as stated. However: E-defense U16 proposes moving the e05 close to ~aggregate 692, which would reduce e05 to ~129 lines (within band). The consequent e06 would span ~693-912 = ~220 lines (over ceiling). The U16 boundary-rebalance is escalated to dramatist: "e06 over-band; must confirm whether cutting before aggregate 700 does not bisect the Elara POV stretch." Specifically: the `# pov: oc-craftsman-mother` marker in the aggregate sits between aggregate IDs 700 and 701 (file line ~834). If e05 closes at 692, the pov marker (at aggregate ~700-701) falls inside e06, which is correct — e06 would open at aggregate 693 (Taylor-POV, from the post-U16 Elara-POV zone). But the pov marker for `oc-craftsman-mother` would then be at aggregate 700-701, which is inside e06 but 7 IDs after the e06 open. The rubric says "no cut bisects a POV-coherent stretch." If the cut at 692 falls inside the Taylor-POV stretch (Taylor POV runs from aggregate 645-699 before the Elara pov marker at 700), then cutting at 692 bisects the Taylor-POV stretch — the Taylor pov runs 645-699, and a cut at 692 breaks the Taylor stretch. This is a POV-honor violation candidate if the U16 cut is executed at 692 without moving the `# pov: taylor-hebert-jaehaerys` aggregate marker or adjusting the cut to the pov boundary. This is a predictable post-E hard fault. (active-project/theater/proto-lines/s01e05.md; E-defense U16) — citation: Phase 4 Step 1 "POV honor: No cut bisects a POV-coherent stretch."

Note: This finding does not exist in the current corpus (e05 close is currently at 699, within the Taylor-POV stretch). It is a predictable post-execution fault if U16 is executed at the provisional 692 target without verifying that 692 falls within Taylor-POV and that no POV boundary exists at that exact point.

**signal-004** [SIGNAL] Cast distribution across the season. e01: 3 named actors. e03: 12 named actors in cast header (taylor-hebert-jaehaerys, oc-child-peer, oc-craftsman-mother, the cloth-factor's wife, oc-craftsman-father, rymer-hedge, oc-lords-steward, the ferryman, the town reeve, the fishwife, the clerk, septon-rowan). e04: 11 named actors. Cast density is highest in the climax-adjacent episodes (e03, e04) and lowest in the baseline episode (e01). This is structurally appropriate per the season plan — "the crowd thickens around the IGNITION event." Not a rubric fault; flagging for Class 11 reference.

**signal-005** [SIGNAL] POV distribution at season scope: Taylor-dominant (e01-e04 + portions of e05 and e06) + 2 interlude POVs (Mira in e05, Elara in e06). This matches the season-plan's named interlude structure. The rubric's Phase 4 Step 1 "POV honor" is satisfied at the split level: no cut bisects a POV-coherent stretch in the current corpus (e05 cut at 699 falls at the end of the Taylor-return-home stretch, AFTER the Taylor pov resumes at aggregate ~645; e06 cut starts at 700 which is the Elara pov zone). Compliant. NO HARD FINDING for current corpus.

---

### Class 3 — METADATA-INCONSISTENCY

**fault-005** [HARD] s01e06 `narrator: oc-craftsman-mother` does not match dominant-POV-by-line-count per the /and-season Phase 4 Step 3 spec. From the s01e06.md body:
- `# pov: oc-craftsman-mother` marker is at episode file line 12 (between episode body lines 1 and 2). Elara-POV bones run from episode line 3 through episode line 88 = approximately 86 substantive lines (with blanks).
- `# pov: taylor-hebert-jaehaerys` marker at episode file line 101 (between lines 88 and 90). Taylor-POV bones run from episode line 90 through episode line 211 = approximately 122 substantive lines.
- Taylor dominates e06 by line count (~122 vs ~86). The spec says `narrator:` is "the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch." Dominant = Taylor. The header names Elara.
- This is a metadata fault. The `narrator:` field on s01e06.md is wrong under the literal Phase 4 Step 3 spec. (active-project/theater/proto-lines/s01e06.md line 4) — citation: /and-season Phase 4 Step 3 spec "narrator: the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch."
- Previously identified: B-baseline Gap 8, A-corpus anomaly note, E-defense carry-back queue.
- Note: E-defense routes this to Phase H carry-back (rubric clarification, not corpus fix). The rubric ambiguity is real — but under the current V1 spec text, the field is wrong. Classified HARD because it fails a stated validation rule.

**signal-006** [SIGNAL] s01e05 `narrator: mira-stonefield-jaehaerys`. From s01e05.md body:
- `# pov: mira-stonefield-jaehaerys` at episode file line 13 (between episode lines 2 and 3). Mira-POV bones run from episode line 2 through episode line 83 = approximately 82 substantive lines.
- `# pov: taylor-hebert-jaehaerys` at episode file line 95 (between episode lines 83 and 84). Taylor-POV bones run from episode line 84 through episode line 137 = approximately 54 substantive lines.
- Mira dominates e05 (82 lines vs 54 lines). The `narrator: mira-stonefield-jaehaerys` header is CONSISTENT with dominant-POV spec for e05.
- B-baseline Gap 8 and A-corpus incorrectly stated that Taylor dominates e05 (using "aggregate line 671" to mean the file-line position of the pov marker, then computing 564-670 = 107 Taylor lines vs 671-699 = 29 Mira lines — but those are aggregate IDs, not line counts). The actual per-episode file shows Mira dominates. The B-baseline Gap 8 finding for e05 is a false positive. Recording as SIGNAL because the e05 narrator field is in fact compliant; the prior analysis was in error.
- This corrects a named prior finding. No fixer action needed on e05 narrator field.

**signal-007** [SIGNAL] memory.md episode entries for s01e05 and s01e06 carry `interlude: true`. The showrunner-memory schema shows `interlude: true | false  # optional, only if applicable`. These entries are present and correctly mark the interlude episodes. No schema violation. However: if the narrator field on e06 is corrected per fault-005, the corresponding `narrator:` field in memory.md s01e06 entry (line 106: `narrator: oc-craftsman-mother`) would also need updating. The memory.md entry mirrors the per-episode file header — if the file is corrected, memory.md must also be corrected. (active-project/staff/showrunner/memory.md lines 104-113) — citation: showrunner-memory schema "The cast/locations/prior_episode/aggregate_range fields mirror the per-episode proto-line file's extended header."

**signal-008** [SIGNAL] memory.md s01e01 entry shows `aggregate_range: 1-149`. E-defense U12 routes this to showrunner-self for update to `1-148`. The memory.md has not been updated. This is the same pre-execution state gap as fault-002 but in the memory file. (active-project/staff/showrunner/memory.md line 67) — citation: showrunner-memory schema; E-defense U12 pending.

**signal-009** [SIGNAL] The showrunner-memory schema specifies that per-episode entries should have `proto_lines_path`. All six episode entries in memory.md carry `proto_lines_path`. However, the schema's episode entry format in the schema file shows `proto_lines_path: active-project/theater/proto-lines/s01e01.md` — the paths in memory.md use this exact pattern. Compliant. NO FAULT.

---

### Class 4 — CURVE-SHAPE

**signal-010** [SIGNAL] S2 CLEAN verdict from the existing pass-S2 identifies: buildup 1-418, climax 419-519 (peak 455-474), denouement 520-912. Peak placement at aggregate 455-474 = 50-52% of the 912-line aggregate. A-corpus notes this is "46-62% of the aggregate" (citing range 419-563 = e04, the swarm episode). The peak itself (455-474) maps to approximately 50% — borderline "back half" (rubric says "back half of the aggregate" = >50%). The peak at 50% is exactly at the midpoint, which is the edge of compliance. If the aggregate is understood as 1-912, then "back half" = lines 457+. The peak range 455-474 straddles the exact midpoint. This is a borderline finding that the S2 CLEAN verdict accepted. Under the rubric's "when in doubt, flag" instruction, the midpoint landing of the climax peak is a signal. Previously identified: A-corpus axis 1 note ("front-half of the back-half, borderline-acceptable per the 'back half' rule but worth pressing"). Not reclassified by Phase E (U1 DEFEND). Signal only.

**signal-011** [SIGNAL] Denouement share. The S2 CLEAN verdict names denouement as 520-912 = 393 lines of 912 total = 43% of aggregate. U1 DEFEND carry-back note acknowledges the rubric has no maximum denouement share; the 44% finding is real and the rubric has no answer. E-defense routes this to Phase H carry-back. Under the current V1 rubric, no fault exists — but the denouement share is large enough to warrant the carry-back. Signal only; previously identified in E-defense U1.

---

### Class 5 — CONTRADICTION

**signal-012** [SIGNAL] Cross-episode state contradiction candidate: The post-rider's letter (s01e04 episode lines 127-133, aggregate 542-548) arrives and is received by the town reeve. e05 opens on Mira-POV with no signal that the letter event is in any actor's working state. E-defense routes this to U10 (REVISE: revise 1-2 bones in aggregate 550-562 to signal Taylor's registration of the letter event). This is a named continuity gap, not a logical contradiction — the letter is not contradicted, only unacknowledged. Not a hard contradiction; it's a state-propagation gap routed to screen-writer. No contradiction finding — the letter event is not denied or reversed.

No hard cross-episode state contradictions found between episode pairs where content is verifiable from the split files. The existing S4 SEASON-CONTINUITY-OK (r2) provides baseline coverage. No new contradictions surfaced from direct reading of the per-episode split files.

---

### Class 6 — DEDUP

No episode boundary repeats prior-episode content. The aggregate is a single continuous flat object; episode boundaries are cuts, not restarts. e05 opens on `mira enters the alley` which continues directly from e04's close `taylor follows mira-stonefield-jaehaerys` — this is continuation, not duplication. NO FINDINGS.

---

### Class 7 — SUPERFLUOUS

**signal-013** [SIGNAL] s01e02 lines 86-103 (aggregate 233-250): after Taylor exits the sept with the volume (episode line 69/aggregate ~216-218), a second sept scene opens (episode line 86/aggregate ~234) where Rowan draws a volume, Taylor marks a column, and the episode closes on `taylor traces the column`. This second sept sequence (episode lines 86-103) is aftermath of the volume-handoff board-change that already closed the episode's payoff at episode line 58-59 (taylor takes/grips the volume). E-defense U3/U13 identifies this as the core placement fault — the payoff at 207-208 is buried in the interior, and 43 lines of column-tracing aftermath follow. Under Class 7 (superfluous): the second sept visit and column-tracing aftermath (episode lines 70-103, aggregate ~218-250) do not advance the season forward beyond what the volume-handoff already established. Their deletion would not change downstream comprehension of the pastoral-claim state-change. Previously identified: E-defense U3 (REVISE). Signal — routable via Phase E's already-named dramatist boundary-rebalance.

---

### Class 8 — CONSTRAINT

**signal-014** [SIGNAL] Cast-presence consistency check on s01e03. The cast header lists 12 actors: taylor-hebert-jaehaerys, oc-child-peer, oc-craftsman-mother, the cloth-factor's wife, oc-craftsman-father, rymer-hedge, oc-lords-steward, the ferryman, the town reeve, the fishwife, the clerk, septon-rowan. The episode covers loc-market-square, loc-river-ferry-dock, and loc-local-sept. septon-rowan appears in the body at episode lines 152-162 (aggregate ~400-410) at the ferry dock census sequence — Rowan approaches oc-lords-steward and speaks. The series stage matrix places Rowan at loc-local-sept. Having Rowan at loc-river-ferry-dock is plausible (he could travel there) but the episode header lists loc-local-sept as a location, not the dock as a separate entry — the dock IS listed as a location in the header (loc-river-ferry-dock). So Rowan at the dock is covered by the episode's location set. No hard presence-violation. Signal only — the presence is plausible but the transition from sept to dock is not signaled in the bones (no bone shows Rowan traveling to the dock). The cast-presence mechanics are satisfied structurally; the missing travel-signal is a bone-level gap, not an impossible presence.

No series-law violations found from direct reading of the six per-episode files. cond-fauna-control-rules is honored in e04 (involuntary swarm, retrospective cost per U5 DEFEND reasoning). cond-series-tone-constraints-84ac prohibition on catharsis before the Dance is honored — no cathartic second peak in denouement. cond-smallfolk-political-physics honored throughout (no direct confrontation without institutional mediation).

---

### Class 9 — AP-SCAN (anti-pattern scan)

**fault-AP-1** [HARD] Idiom depletion — physical-stasis verb cluster. Tabulation from direct reading of all six per-episode files:

`holds the feet` instances by episode:
- s01e01: lines 34, 43 (and body line 34 is aggregate 35 per the mapping) — 2 instances (as `holds the feet`)
- s01e02: line 67 — 1 instance
- s01e03: lines 27, 43, 83, 101, 139, 142, 169 — 7 instances
- s01e04: lines 9, 22, 57 (as `presses the feet` at 57), 85 (as `presses the feet`), 145 — 3 `holds the feet` + 2 `presses the feet`
- s01e05: lines 11, 22 (from s01e03 mapping), 68, 81, 137 — approximately 4 instances in e05
- s01e06: lines 90, 100, 207 — 3 instances

Rough aggregate count: `holds the feet` = approximately 18-20 instances across 6 episodes; `presses the feet` = additional 2 instances. Total physical-stasis cluster including `holds the eyes`, `holds the chin`, `holds the face`, `holds the head`, `holds the shoulder`, `holds the mouth` brings the cluster to 60+ instances across the season.

This exceeds the S3.5 drift-pattern threshold of "a verb appearing 5+ times across the season as a borderline state-verb" — `holds the feet` alone appears 18+ times. The schema's `holds` narrow license states: "licensed only when (1) the object is a body part of the subject and the action is stillness-against-pressure." `holds the feet` passes this narrow license syntactically. However, the depletion frequency creates the anti-pattern named in E-defense U17 and the B-baseline carry-forward.

Previously identified: E-defense U17 (DEFEND-with-carry-back), B-baseline (S6 carry-forward, worm-canon-pedant shard-load-suppressed). Classification: HARD at Class 9 scan level because it represents a systematic pattern that the auditor can mechanically confirm (20+ instances of a single idiom) even though E-defense DEFENDS it under V1 rubric gaps. The rubric's explicit gap ("no quantified definition of 'buildup' and 'denouement' share") applies to U17 defense, but the S3.5 drift-pattern report obligation exists in V1: "a verb appearing 5+ times across the season as a borderline state-verb is flagged for systematic recast." `holds the feet` is on the narrow-license list — the S3.5 exemption for schema-licensed `holds` is arguable — but the scale of depletion (18+ instances) is a V1 drift-pattern finding. Classified HARD because the S3.5 pass is a mandatory auditor pass and this is above the stated 5-instance threshold.

**signal-015** [SIGNAL] Procedural recurrence (S6 carry-forward — dark-fantasy-reader). The folio/inquiry/census sequence recurs structurally: e03 (census folio, dock), e04 (incident folio, market square), e05 (inquiry folio, market square). Three consecutive episodes use `oc-lords-steward draws the [X] folio` as a structural beat. This is the ledger-sequence fatigue named in B-baseline S6 vibe drift. Previously identified: B-baseline Table row "S6 vibe — dark-fantasy-reader: VIBE-DRIFT-procedural-recurrence." Signal — the recurrence is named and the E-defense does not resolve it directly (it is carried forward and not revisited by a REVISE in the Phase E decisions). Signal only; not a schema or structural violation.

**signal-016** [SIGNAL] Shard-load suppression. Across the 20+ `holds the feet` / `holds the eyes` / `holds the chin` cluster, the distinction between cost-register (Taylor paying biological cost for swarm proximity or involuntary activation) and patience-register (Taylor managing social exposure by controlled stillness) is not mechanically differentiated in the bones. The `presses the temple` at e04 line 73 (aggregate ~491) is the one explicitly cost-register physical marker. All other `holds the feet/eyes/chin` instances are in social-management or observation registers. Per the worm-canon-pedant carry-forward: shard-load is suppressed by the idiom flattening cost and patience into the same physical form. Previously identified: B-baseline, E-defense U17. Signal only; same as fault-AP-1 but from the audience-lens angle rather than the mechanical-count angle.

**signal-017** [SIGNAL] Over-aftermath post-IGNITION (U1 finding). e04 post-IGNITION bones: episode lines 56-148 = 93 bones after the swarm contracts (line 56). The U1 DEFEND argues this is intentional "long cost" structure. The rubric's S2 denouement characterization covers this. Signal — the 93-bone post-IGNITION aftermath is real and the rubric provides no ceiling for aftermath length at episode scope. Signal only per U1 DEFEND.

---

### Class 10 — TASTE-FLAG

**signal-018** [SIGNAL] The maester arrival sequence (s01e06 episode lines 103-211, aggregate ~802-912) is 109 bones long and covers: maester enters Fairstead, visits the workshop, visits the sept, crosses to the ferry, boards, crosses the water, then Taylor climbs the loft. This is the season's "the apparatus knows the name" close. The sequence is largely told from observation (Taylor-POV after episode line 90), watching the maester move through locations. A future reader may press: the maester's visit is a series of `the maester speaks to / draws / marks / closes` procedural actions — 109 bones of procedural visit — that mirrors the very ledger-sequence fatigue flagged in signal-015. The distinction is that this sequence is the season's closing image and the apparatus is finally visible in person, not through paper. However, the anti-pattern (institutional actor + folio + marks + exits) is structurally identical to the census sequences. This is a taste-flag anticipation: the maester arrival risks reading as a third procedural-folio sequence rather than as the season's qualitatively different close. Not a current rubric fault. Flagging for future audience attention.

**signal-019** [SIGNAL] e06 closing bones (episode lines 203-211, aggregate ~900-912): `taylor climbs the loft ladder`, `the sept fly orbits the baptismal basin rim`, `the dock mosquito circles`, `the ferry folio crosses the water`, `taylor holds the feet`, blank, blank, `oc-craftsman-mother calls`, `taylor presses the loft floor`. The final image is `taylor presses the loft floor` — a physical-stasis/response image. Under the Phase 4 Step 2 CLOSE-EARNS-NEXT test for the season-close episode, this is also the series-act-1 close (no further episodes in s01). Whether `presses the loft floor` is adequate as a season-close image is a taste judgment the rubric's CLOSE-EARNS-NEXT criterion will need to answer when s02 is planned. Flagging for carry-back to the s02 season-open planning phase.

---

### Class 11 — PILE-UP REVIEW

**signal-020** [SIGNAL] s01e03 cast pile-up: 12 named actors. The episode covers the Clem-Ferris child-witness sequence AND the Pryor census dock sequence AND the Rowan literacy-folio sequence — three distinct scene clusters, each with its own cast subset. The 12-actor count is earned by the episode's function as the "census day / multiple vectors converge on Taylor" episode. Each of the 12 actors has a function:
- child-witness cluster: taylor, oc-child-peer, oc-craftsman-mother, cloth-factor's wife
- dock/census cluster: taylor, oc-craftsman-father, rymer-hedge, oc-lords-steward, ferryman, town reeve, fishwife, clerk
- folio cluster: oc-lords-steward, septon-rowan
The casting is warranted by the scene structure. However: the cloth-factor's wife appears only in one interaction (episode line 4: `oc-craftsman-mother speaks to the cloth-factor's wife`) and has no further body presence. Her inclusion in the cast header is correct per the spec ("comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener") — she is a listener. But her single-line presence in a 170-line episode makes her a borderline cast member. Not a fault; flagging as a pile-up contributing factor.

**signal-021** [SIGNAL] s01e04 cast pile-up: 11 named actors. The IGNITION episode. The cast is earned: the market-square swarm event plausibly gathers a crowd. `the collector's man` and `the townsman` appear as direct participants in the altercation that triggers the swarm. `mira-stonefield-jaehaerys` is introduced as a named observer. `the post rider` appears in the closing letter-arrival sequence. Cast pile-up is narratively earned for the season's climax episode. NO fault.

**signal-022** [SIGNAL] e01 cast thinness: 3 actors. e01 is the baseline-establishing episode — household only, no outside contacts. Three actors (taylor, oc-craftsman-mother, oc-craftsman-father) for 149 aggregate-IDs is appropriate for the season plan's "early-baseline" register. Not a pile-up issue; confirming the cast distribution is structurally intentional. NO fault.

---

## Cross-class summary

### Findings overlapping with B-baseline gaps (no double-count)

- **Gap 8 (narrator field anomaly, e05/e06):** fault-005 covers e06. signal-006 corrects the prior analysis and shows e05 narrator is actually compliant. The e06 HARD finding stands; the e05 finding is a false positive in B-baseline.
- **Gap 2 (cross-episode continuity):** U7, U8, U9, U10, U11 in E-defense route the identified continuity gaps. No new continuity contradictions found beyond named gaps. signal-012 confirms U10's letter-arrival gap without finding a new one.
- **Gap 3 (placement quality):** E-defense addresses through U3/U12/U13/U14/U16 REVISE decisions. No new placement findings beyond U3/U13 's e02 at 58 lines (below 80-line floor, already named in E-defense).
- **Gap 4 (S6 vibe-drift escalation):** signal-015 and signal-016 are the prior S6 carry-forwards. No new vibe-drift instances found; the prior two are confirmed present.
- **Gap 6 (conflicting entertainment thresholds):** Not scannable mechanically from corpus; rubric-level issue. Confirmed present in rubric text. No corpus finding.
- **Gap 7 (season-scope adversarial criteria):** signal-018 and signal-019 are taste-flag anticipations that partially address the season-scope adversarial gap. Not a corpus fault.

### Findings overlapping with E-defense routing

- **fault-001 (aggregate non-monotonic IDs):** Not addressed by any E-defense REVISE. New finding. The E-defense routing subtasks (bone additions, header updates) will not repair the out-of-order IDs in the aggregate.
- **fault-002 (s01e01 aggregate_range pre-execution):** Covered by U12 showrunner-self pending task. Will be resolved by execution.
- **fault-004 (predictable post-E POV-honor violation at U16 cut):** New finding. E-defense U16 notes the dramatist must "confirm that cutting before aggregate 700 does not bisect the Elara POV stretch" — but does not flag the equal risk of bisecting the Taylor-POV stretch when cutting at 692 inside the 645-699 Taylor stretch. This is a gap in the U16 routing.
- **fault-005 (s01e06 narrator field):** Named in Gap 8 / B-baseline / E-defense carry-back queue. The carry-back classifies this as a rubric-clarification problem (Phase H). Auditor classifies it HARD because the current V1 spec makes the field wrong.
- **fault-AP-1 (holds-the-feet idiom depletion):** Named in U17 DEFEND-with-carry-back. Auditor classifies HARD because S3.5 drift-pattern mandate is a V1 obligation and the 18+ instance count exceeds the stated 5-instance threshold.
- **signal-002 (e03/e06 over-band):** Covered by U4/U16 boundary-rebalance routing. Pre-execution.
- **signal-013 (e02 aftermath superfluous):** Covered by U3/U13 REVISE. Pre-execution.

### Net new findings (not previously named)

- **fault-001:** Aggregate file non-monotonic IDs (900-range IDs interspersed in e01 content region). Not named in any prior phase.
- **fault-004:** Predictable POV-honor violation if U16 cut executes at aggregate 692, bisecting the Taylor-POV stretch (645-699). E-defense U16 routing identifies e06 over-band and the Elara-POV marker placement check, but does not flag the Taylor-POV bisection risk at the proposed 692 cut point.
- **signal-006:** Correction of B-baseline Gap 8's e05 analysis. e05 narrator field is compliant under dominant-POV spec. The prior analysis used file-line-as-aggregate-ID confusion.
- **signal-018 / signal-019:** Season-close sequence taste-flags at season scope. New; not previously named.

---

## Recommendation

### Fixer-routable HARD findings

- **fault-005** — s01e06 header `narrator: oc-craftsman-mother` must be corrected to `taylor-hebert-jaehaerys` under the V1 dominant-POV spec, OR the rubric must be amended via Phase H carry-back to license interlude-POV as narrator when an interlude is the episode's primary dramatic arc. Until Phase H resolves the rubric ambiguity, the field is wrong under V1 text. If Phase H resolves it as "interlude-POV wins," the field is correct and fault-005 closes. Fixer cannot route this until Phase H verdict; block on Phase H.
- **fault-002 / signal-008** — s01e01 aggregate_range header (per-episode file + memory.md) pending U12 showrunner-self execution. No fixer needed; showrunner-self owns this.
- **fault-AP-1** — S3.5 drift-pattern obligation. The 18+ `holds the feet` count exceeds the 5-instance threshold for systematic recast. The E-defense DEFENDS this under rubric gaps; auditor flags it as HARD because the S3.5 obligation is in V1 text. Resolution path: either execute screen-writer regeneration of the flagged instances (60+ bone regeneration per U17 scope) or add Phase H rubric amendment explicitly extending the narrow-license exemption to idiom-depletion at scale. Cannot be fixer-routed without a rubric decision.

### Carry-back queue candidates

- **fault-004** — Add a step to the U16 boundary-rebalance subtask: verify that the proposed e05 close point does not bisect the Taylor-POV stretch that runs aggregate 645-699 (the `# pov: taylor-hebert-jaehaerys` marker in the aggregate appears between aggregate IDs ~644 and 645). A cut at 692 is inside this stretch. The dramatist boundary-rebalance should confirm whether 692 falls before or after any POV marker within the stretch, and document the finding. If the cut must respect POV boundaries, the valid cut range is either before 645 (inside the Mira stretch, inadvisable) or at the end of the Taylor stretch at 699 (the current cut point, which Phase E is trying to move). The U16 dramatist subtask routing should be amended to include this check.
- **signal-006** — Correct the B-baseline Gap 8 analysis for e05. The e05 narrator field is compliant. Phase H rubric clarification for Gap 8 should focus only on e06.
- **signal-018 / signal-019** — Season-close sequence (maester arrival + loft-floor close) for future audience attack in s02 planning phase.

### Findings that require human escalation

- **fault-001 (aggregate non-monotonic IDs):** The 900-range IDs interspersed in the e01-range aggregate content are not addressed by any E-defense routing. These IDs appear to be survivor IDs from prior edits that wound up out-of-sequence in the aggregate's flat numbering. If the aggregate is the canonical source of truth and the per-episode files are derived, the non-monotonic IDs in the aggregate mean: (a) fixer formula `aggregate_id = aggregate_range_start + episode_id - 1` will not produce correct mappings for any episode bones derived from the out-of-order region, and (b) any Phase 4 Step 3 validation that assumes monotonic IDs within the aggregate_range will miscount. The aggregate is stated as having "900 numbered lines + 5 inline `# pov:` markers" (A-corpus), and the per-episode files' body IDs are re-numbered 1..M starting at 1 — so the per-episode files are self-consistent. But the aggregate's ID ordering is a schema violation that requires either (a) human review to confirm the out-of-order IDs are intentional legal-deletion-gap survivors that are schema-compliant under the "stable — once assigned, never reused, never reassigned" rule, or (b) correction of the aggregate's non-monotonic sequences. The schema says IDs are "stable" and "re-ordering preserves IDs" — it does NOT say the aggregate must be read in monotonic order, only that IDs are not reused or reassigned. If the 900-range IDs are survivor IDs from resequenced content (moved from later positions to earlier positions in the narrative), they violate the "re-ordering preserves IDs" rule: the IDs reflect their old narrative position, not their current one. Human decision needed on whether these IDs are legal survivors (schema-compliant) or reordering artifacts (schema violation).

- **fault-AP-1 / U17:** The idiom-depletion question — whether S3.5's 5-instance drift-pattern threshold applies to schema-licensed `holds` uses — requires human decision. E-defense DEFENDS under rubric gap; auditor classifies HARD under V1 S3.5 text. The two readings cannot be reconciled without human adjudication or a Phase H rubric amendment.

---

## Phase G complete
