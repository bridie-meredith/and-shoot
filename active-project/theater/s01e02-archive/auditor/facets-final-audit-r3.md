---
audit: facets-final-r3
episode: s01e02
date: 2026-05-11
mode: flag-only
status: CLEAN
remediation-context: Phase 5b cycle-1 fixer pass (5 minimum-change items)
totals: 0 HARD + 5 SIGNAL
---

# Audit r3 — post-cycle-2-fixer

## Fix landing verification

**Item 1 — tens:70 @83 retune r=1 → r=2**
CONFIRMED. `tensometer.md` entry 70: `70 @83 2`. `tensometer-s01e02.md` entry 70: `70 @83 2`. Applied in both files. Cite-index entry `tens:70 @83 r=2 back=N co=[loc-state:5, narrator:15]` consistent with r=2.

**Item 2 — narrator:27 @149 label swap ("Khepri-threshold" → "foreknowledge-band threshold")**
CONFIRMED. `interest-narrator.md` entry 27 reads: `27 @149 the phrase the beetles carried is closer to a foreknowledge-band threshold than anything the network has relayed`. No occurrence of "Khepri" anywhere in the file. Label-swap clean.

**Item 3 — mem:10 @125 DELETE**
CONFIRMED. `memory.md` contains IDs 3, 4, 7, 9, 11, 12. mem:10 is absent. Cite-index `### mem (6 entries)` lists no mem:10. Proto-line @125 carries no `[mem:10]` citation: line reads `125 taylor-hebert-flea-bottom drops the stylus [narrator:23] [sensory:3] [state:7] [vibes:9] [vibes:10]`.

**Item 4 — mem:2 @30 DELETE**
CONFIRMED. `memory.md` contains IDs 3, 4, 7, 9, 11, 12. mem:2 is absent. Cite-index `### mem (6 entries)` lists no mem:2. Proto-line @30 carries no `[mem:2]` citation: line reads `30 taylor-hebert-flea-bottom opens the log [narrator:8]`.

**Item 5 — state:1 @149 record_anomaly_logged old-state `true` → `anomaly-noted`**
CONFIRMED. `state-updates.md` broken-maester slice entry 5 reads: `5 @149 actor:oc-broken-maester.record_anomaly_logged: anomaly-noted -> phrase-isolated`. Old-state is the string `anomaly-noted`. Boolean `true` is absent. Type-mismatch repaired.

---

## Cite-index count consistency

r2 total: 284 entries. Cycle-2 DELETEs: mem:2 + mem:10 = 2 removed. Expected r3 total: 282.
Cite-index header: `totals: 282 facet entries`. CONSISTENT.

mem section: r2 carried IDs 2, 3, 4, 7, 9, 10, 11, 12 (8 entries). Post-deletion: IDs 3, 4, 7, 9, 11, 12 (6 entries). Cite-index `### mem (6 entries)`. CONSISTENT.

ID gaps in mem section (2, 5, 6, 8, 10) reflect cumulative deletions across r1 fixer and cycle-2 fixer. Per dispatch instruction: gap-as-permitted-per-schema, not a fault.

---

## Recalibrated CONSTRAINT scan (Earth-Bet proper-noun fence)

Scan scope: all facet entry content fields — NI entry text, memory entry text and target-reference glosses, vibes token arrays and licensed-by fields, feeling somatic-tell text, state-update field names and old-state and new-state values, sensory old-state and new-state, location-state descriptive text, tensometer axis annotation comments, proto-line text. Substring match against the full 27-item list: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Behemoth, Leviathan, Simurgh, Khonsu, Tohu, Bohu, Gold Morning, Gimel, Scion, Eidolon, Glaistig Uaine, Echidna, Coil, Cauldron, Dragon, Bonesaw, Mannequin, Crawler, Siberian, Slaughterhouse Nine.

**Clean — no proper-noun violations found in facet entry content.**

Per-file trace:
- `memory.md` (6 entries): All Earth-Bet displacement-cloaks use mechanism-descriptive or generic register. mem:3 "pre-deployment ritual" — no proper noun. mem:4 "institutional record-cruelty / administrative-violence pattern" — no proper noun. mem:7 "swarm-feed as cognition extension — the prior life's parallel-track register" — no proper noun. mem:9 back-reference slug `s01e01:134` — no proper noun. mem:11 "the prior life had a different name for" — no proper noun. mem:12 "failed-recognition-by-dying-parent pattern — the rising-from-the-vigil variant, cross-rhyme to the song-stopping" — no proper noun. CLEAN.
- `interest-narrator.md` (37 entries): narrator:27 @149 confirmed uses "foreknowledge-band threshold." All other entries use Westerosi/invented procedural language. No proper nouns anywhere in the file. CLEAN.
- `vibes.md` (23 entries): All thematic tokens use invented language ("the-Tya-shaped-debt", "withdrawal-as-management", "grief-without-object", "clinical-self-erasure"). No proper nouns. CLEAN.
- `feeling.md` (9 entries): Purely somatic register (weight, gaze, breath, hand-position, thumb-on-bench). No proper nouns. CLEAN.
- `state-updates.md`: All field names and values are procedural or invented (e.g., `anomaly-noted`, `phrase-isolated`, `first-payment-accepted`, `ambient-signal`, `named-log-entry`, `bodily-committed-withdrawal`). No proper nouns. CLEAN.
- `sensory.md` (5 entries): Physical and environmental register (alley-daylight, latch-crack, stylus-drop-clatter, insect-density-note, chair-and-floor-creak). No proper nouns. CLEAN.
- `location-state.md` (12 entries): Location-descriptive register (junction conditions, room states, atmospheric qualifiers). No proper nouns. CLEAN.
- `tensometer.md`: Axis annotation comments use Westerosi narrative language. No proper nouns in any axis comment. CLEAN.
- `proto-lines/s01e02.md`: All subject tokens are Westerosi or invented (taylor-hebert-flea-bottom, oc-tanner-father, lords-man, beetles, wasps, flies, oc-broken-maester, etc.). No proper nouns in any proto-line text. CLEAN.

---

## New-HARD scan

**None introduced.**

Orphan back-reference check for mem:2 and mem:10 deletions:
- No surviving cite-index entry carries a `lic-out=`, `co=`, or `lic-in=` reference to mem:2 or mem:10.
- No surviving proto-line carries a `[mem:2]` or `[mem:10]` inline citation.
- No surviving NI, vibes, feeling, or state entry carries a `licensed-by:` field referencing mem:2 or mem:10.
- Deletion of mem:10 from the @125 pile-up reduces that pile-up from 6 to 5 co-located facets: narrator:23, sensory:3, state:7, vibes:9, vibes:10. A 5-way pile-up at a r=3 rupture beat remains warranted; no structural failure from the reduction.

narrator:27 hard-fence post-swap: "foreknowledge-band threshold" contains no Earth-Bet proper nouns per the full recalibrated scan above. CLEAN.

ID monotonicity: mem gaps at 2, 5, 6, 8, 10 are cumulative deletion residue across r1 and cycle-2 fixer passes. Per-schema: permitted.

No new HARD from any source.

---

## SIGNAL inheritance from r1/r2

**A-001 (tens approach @83-@84 1→3 adjacency gap) — RESOLVED.**
tens:70 @83 is confirmed r=2. The approach sequence to @85 latch-break is now: r=2 @83 → r=1 @84 → r=3 @85. The rubric's direct 1→3 prohibition is no longer triggered; the r=2 at @83 provides the approach signal. The 2→1→3 pattern (r=2 approach, r=1 intervening, r=3 rupture) is within rubric tolerance. Finding closed.

**T-001 (eviction approach @83-@84 momentum-stall candidate) — RESOLVED.**
Collapses with A-001 resolution. The r=2 at @83 dissolves the atmosphere-thin reading at the climax approach. Finding closed.

**F-002 (feeling aggregate sparsity 5.8% marginally above 5% ceiling) — unchanged. SIGNAL.**
9 entries across 155 proto-lines = 5.8%. No cycle-2 fix touched feeling.md. Rubric scope ambiguity (per-character-episode vs. aggregate-episode interpretation of the 2-5% band) unresolved. Per-character rates all below 5%. Advisory; track against s01e03.

**M-001 (NI shard f-r2-counts taxonomy misuse) — unchanged. SIGNAL.**
Source shard preserved uncorrected for traceability per documented intent. Consolidator's correction to canonical frontmatter stands. Consolidated total well below gate threshold. Discipline note for future shards only.

**M-002 (oc-tanner-elder feeling shard F-R2-3 misclassification) — unchanged. SIGNAL.**
Consolidated total `f-r2-3: 1` remains below the `f-r2-2 + f-r2-3 + f-r2-4 > 2` gate threshold. Taxonomy misclassification in source shard only; no gate impact. Advisory.

**A-002 (metaphor:1 @89 AP7 tens=1 discipline) — unchanged. SIGNAL.**
Single surviving meta:1 @89 at tens=1. R2 judge defense documented (entry names the instrument's condition, does not ornament). Audience gate cycle-1 unanimously sustained the R2 defense and clarified AP7 scope (AP7 is peak-zone prohibition; inapplicable at tens=1). Advisory only.

**S-002 (state-updates consolidated file duplicate source-header lines) — unchanged. SIGNAL.**
Cosmetic merge artifact confirmed still present: `# source: oc-broken-maester` appears at consecutive lines 25-26; same duplication pattern for oc-dock-runner, oc-tanner-elder, oc-tanner-father, oc-tanner-mother, and taylor-hebert-flea-bottom slices. Content and canonical entry data unaffected. Merge artifact only.

---

## Verdict

CLEAN HARD=0 — all 5 cycle-2 fixer items confirmed landed; no new HARD introduced; recalibrated Earth-Bet proper-noun CONSTRAINT scan returns clean across all facet content fields in all nine facet files and the proto-lines file; 5 SIGNAL findings carry forward from r1/r2 unchanged; A-001 and T-001 resolved by Item 1 (tens:70 @83 r=2 confirmed).
