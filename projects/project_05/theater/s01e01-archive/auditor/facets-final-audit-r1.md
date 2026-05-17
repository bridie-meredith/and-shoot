---
audit: facets-final-r1
episode: s01e01
date: 2026-05-11
mode: flag-only
status: FINDINGS-PRESENT
totals: 14 findings across 7 facets
---

# Facets Final Audit — s01e01

Auditor: cross-cutting graph auditor fork (Phase 5 of /and-facets)
Mode: FLAG-ONLY. No mutations performed. HARD findings are delete-candidates held as flags; SIGNAL findings routed to facet authors for review.

---

## Class 1: STRUCTURAL

### Finding 1-A
- id: flag-001
- type: flag
- class: STRUCTURAL
- severity: HARD
- what: tensometer.md entries `tens:79 @495`, `tens:80 @504`, `tens:123 @506`, `tens:129 @138 (blank)`, `tens:143 @516`, `tens:147 @517`, `tens:148 @525` — these anchor IDs (495, 504, 506, 516, 517, 525, and blank @138) have no corresponding proto-lines in `s01e01.md`. The proto-lines file covers aggregate_range 1–155 with no bone IDs in the 400s or 500s. `@138` is a listed blank (time-skip) per the proto-lines file itself.
- why: Seven tensometer entries anchor to proto-line IDs that do not exist in the episode's proto-lines file. The cite-index acknowledges these (`back=N` on tens:80, tens:123, tens:143, tens:147) but lists them without explanation in the episode context. The tensometer header notes "includes interpolated IDs 495, 504, 506, 517, 518, 525" — these are season-window bones, not episode-specific bones (s01e01 aggregate range is 1–155). A per-episode facet file should anchor only to bones within its episode's aggregate range. The out-of-range entries cannot be stitched into s01e01 prose and produce cite-index confusion (back=N entries flagged as "lonely" without explanation of why they exist in this file).
- routing: tensometer author (dramatist)

### Finding 1-B
- id: flag-002
- type: flag
- class: STRUCTURAL
- severity: HARD
- what: tensometer.md line `123a @518 3` — an alphabetically-suffixed ID used for a bone that does not appear in the proto-lines ID space (no @518 in s01e01.md). The schema requires monotonic positive integer IDs scoped per facet file; `123a` is not a monotonic integer.
- why: Non-monotonic ID breaks the schema's ID-monotonicity rule. The `@518` anchor does not resolve to any s01e01 proto-line. The curve-verdict comment block immediately following (`# axis: reversal-proximity peaks — beetle-relay rhythm breaks...`) is a free-comment, which is legal, but the entry itself is structural schema non-compliance. If this bone was added via the late-insert path and represents the KICKBACK-3 resolution, it should carry the next available integer ID (e.g., ID 123 or 148-series) and should be documented in the file's late-insert section; `123a` is not resolvable by the stitcher's monotonic ID parser.
- routing: tensometer author (dramatist)

### Finding 1-C
- id: flag-003
- type: flag
- class: STRUCTURAL
- severity: SIGNAL
- what: state-updates.md is a multi-source concatenated file (six `# source:` headers: env, oc-broken-maester, oc-dock-runner, oc-tanner-elder, oc-tanner-father, oc-tanner-mother, taylor-hebert-flea-bottom). The schema specifies `facet: <type>` frontmatter per file; this file carries six separate frontmatter blocks, each introduced by `# source:` rather than conforming to a single unified frontmatter. Entry IDs continue sequentially across the concatenated sections (env entries 1–15; oc-dock-runner 16–19; tanner-elder 20–22; tanner-father 23–24; tanner-mother 25–27; taylor 28–34), which technically satisfies the monotonic requirement at the file level. However, the six distinct `facet:` declarations within one file create ambiguity about which frontmatter governs the file. The schema (`facet.schema.md` §Uniform line shape) specifies a single optional frontmatter block per file.
- why: Stitcher and downstream tooling that reads the file's frontmatter will read only the first `# source: env` block. The subsequent five `facet:` declarations inside the body are invisible to any standard frontmatter parser. This is a format deviation, not a content error, but creates integration risk if the stitcher's frontmatter parser stops at the first block.
- routing: studio (env section author); state-updates authors as a group for consolidation awareness

### Finding 1-D
- id: flag-004
- type: flag
- class: STRUCTURAL
- severity: SIGNAL
- what: interest-narrator.md post-R2 density header states "Post-R2 density: 39/155 ≈ 25.2%." The file's author section counts 39 entries after the R2 add of narrator:41. However the cite-index header (generated prior to or concurrent with R2) lists "39 entries" in the narrator facet count and the cite-index body enumerates narrator:1 through narrator:41 with 39 lines. Consistency between the file's own count and the cite-index count is satisfied. However, the R2 decisions consolidated file header lists `interest-narrator: {K: 38, D: 0, A: 1, cap-refusals: 4}` which confirms 38 kept + 1 add = 39 total. The file's "Entries retained: 38" comment in the post-cull section (which pre-dates R2) and the "post-R2 density: 39" are consistent. No actual discrepancy — but the file has two density statements (pre-R2 "38/155 ≈ 24.5%" and post-R2 "39/155 ≈ 25.2%") that are both present in the file body, creating a stale-data seam that could mislead a reader checking current state.
- why: A file with two density numbers and no explicit "SUPERSEDED" marker on the first figure is metadata-ambiguous. Low severity — both figures are present and labeled — but the pre-R2 figure should carry a superseded flag or be removed.
- routing: interest-narrator author (dialogue-writer-fork:taylor-hebert-flea-bottom)

---

## Class 2: FREQUENCY-BAND

### Finding 2-A
- id: flag-005
- type: flag
- class: FREQUENCY-BAND
- severity: HARD
- what: tensometer.md frequency-band section (post cycle-3): 2s = 26/149 ≈ 17.4% against rubric target 20–30%. The file explicitly acknowledges this ("below floor — structural; opening-window low-charge") and carries a prior cycle-2 acknowledgment. The file treats this as an accepted structural deviation.
- why: 17.4% is 2.6 percentage points below the 20% floor. The file's self-defense ("opening-window low-charge") is noted but not independently verified against the rubric's exemption criteria. The rubric's FREQUENCY-BAND gate does not contain an exemption for "opening-window low-charge" as a named exception class. The file attributes the pattern to the episode's establishment character, which is a qualitative claim, not a rubric-enumerated exemption. Carry-forward note from the orchestrator-verdict confirms this is a known structural pattern for W1/W2/W3, but the per-episode audit should independently flag the below-floor condition so the fixer or editor pass can confirm the exemption applies to the facet-level file (not just the season-window bone-gate).
- routing: tensometer author (dramatist); orchestrator-critic verdict cross-reference for exemption confirmation

### Finding 2-B
- id: flag-006
- type: flag
- class: FREQUENCY-BAND
- severity: SIGNAL
- what: interest-narrator.md post-R2 density is 39/155 ≈ 25.2%, which sits 0.2 percentage points above the 25% rubric ceiling (15–25% band). The file's R2 mutation note acknowledges this ("sits at upper edge of rubric band") and defends it as "structural for episode that establishes two locales + full doubled-register channel inventory."
- why: 25.2% is a minor overage but crosses the rubric ceiling. The self-defense is plausible — two locale-establishments in one episode with a full channel inventory justifies density — but the FREQUENCY-BAND gate is a hard number. The 0.2% overage corresponds to roughly 0.3 of an entry above the ceiling at 155 proto-lines. Whether the defense holds is a rubric calibration question; the auditor flags the ceiling breach for the editor/fixer to confirm or remediate.
- routing: interest-narrator author (dialogue-writer-fork:taylor-hebert-flea-bottom)

### Finding 2-C
- id: flag-007
- type: flag
- class: FREQUENCY-BAND
- severity: SIGNAL
- what: feeling.md aggregate sparsity. Per-character contribution rates: taylor 4/155 = 2.58%; tanner-father 3/155 = 1.94% (file notes 3/149 = 2.01% using its own denom); tanner-mother 2/155 = 1.29%; tanner-elder 2/155 = 1.29%; broken-maester 1/155 = 0.65%; dock-runner 1/155 = 0.65%. The rubric specifies 2–5% per character per episode. Four of six character slices (tanner-mother, tanner-elder, broken-maester, dock-runner) fall below the 2% floor on their own slice reading. The total episode-aggregate across all characters: 13/155 = 8.4%, which the schema does not explicitly gate as an aggregate; the gate is "2-5% per character."
- why: The schema says "2-5% per character." Six characters produce six per-character readings. Four of them are below 2%. The individual file rationales are defensible for non-POV characters with limited on-screen beats (tanner-elder appears at 2 scene peaks; dock-runner appears at 1 scene; maester at 1 scene; mother at 2 scenes). The per-character-per-scene cap (≤1 hard) structurally limits how many entries can fire for characters with few scenes. The rubric's intent for lightly-appearing characters may be a per-eligible-scene rate rather than an episode-spanning rate. This is a rubric ambiguity, not a clear violation, but the below-floor readings should be documented for rubric calibration and confirmed by the editor.
- routing: feeling-facet authors (per-character forks); editor for rubric calibration decision

---

## Class 3: METADATA-INCONSISTENCY

### Finding 3-A
- id: flag-008
- type: flag
- class: METADATA-INCONSISTENCY
- severity: SIGNAL
- what: tensometer.md header states `bones: 1–155 (includes interpolated IDs 495, 504, 506, 517, 518, 525)`. The file body contains entry `123a @518` but does not contain an entry for `@517` in the interpolated-ID section of the body — entry `147 @517 2` appears in the "Late-inserted bones" section at the file's bottom, while the body's sequential list goes from 123/@506 to 124/@132, skipping 518 (which is the `123a` non-monotonic entry). The header claims 518 is an included interpolated ID but the body entry `123a @518` is non-sequential and non-monotonic. The total entry count is ambiguous: the frequency-band section says "Total entries: 149" but the body has entries 1–148 plus `123a`, which could count as either 148 or 149 depending on how `123a` is counted.
- why: The header's "includes interpolated IDs" claim, the late-insert section at bottom, and the `123a` non-monotonic mid-body insertion are three different accounting methods for the same bones. The total-entry count of 149 is self-reported and may be correct, but auditor cannot verify monotonic integrity without resolving the `123a` non-integer status. Inconsistency between stated total (149), body enumeration method, and the late-insert section creates a metadata reliability issue.
- routing: tensometer author (dramatist)

---

## Class 4: CURVE-SHAPE

### Finding 4-A
- id: flag-009
- type: flag
- class: CURVE-SHAPE
- severity: SIGNAL
- what: tensometer.md KICKBACK-1 (Scene E, bones 62–69) and KICKBACK-2 (Scene J, bones 105–116) remain unresolved in the final tensometer file. The curve-verdict section acknowledges both: "Rise-without-peak. Bone 66 (reeve slows the step) raises watch-cost on Taylor but the scene makes no registration — reeve speaks to father and exits" (KICKBACK-1); "Sustained-2 without rupture. Bones 111–113 form live-surveillance plateau (maester speaks / beetles relay / Taylor records) but no commit" (KICKBACK-2). Only KICKBACK-3 is marked RESOLVED.
- why: Two unresolved structural kickbacks in the final episode facet file mean the episode ships with known CURVE-SHAPE gaps: a rise-without-peak at Scene E and a sustained-2 plateau without rupture at Scene J. These are carry-forward items to the screen-writer if a window-revise routes, but in the current faceted state they are structural flags on the episode's tens-curve that the editor and stitcher should be aware of when handling those scenes. The tensometer's self-documentation of these kickbacks is procedurally correct, but the auditor confirms them as active structural flags.
- routing: tensometer author (dramatist); screen-writer (if window-revise is triggered)

---

## Class 5: CONTRADICTION

No contradictions found. State-updates entries chain cleanly (verified: tanner-elder location 1→2→3; dock-runner position FGM→loc-flea-bottom→junction→loc-flea-bottom; taylor location tanner-village→loc-flea-bottom→loc-flea-bottom-base; tanner-mother position entries 25→26→27 consistent with offstage-exit assumption documented in the file). No two facet entries set incompatible state on the same anchor.

---

## Class 6: DEDUP

No deduplication faults found. Cross-facet check on the three pile-up anchors:

- @43 (7 facets): feel:8 (mother somatic), mem:6 (failed-recognition monument), narrator:12 (silence-as-shape), sensory:3 (song→silence), tens:41 (r=3), vibes:8 (grief-without-object), vibes:9 (asking-around-the-edge) — all seven entries do distinct work. No two entries carry the same content on the same channel.
- @98 (8 facets): loc-state:1, mem:7, narrator:25, sensory:4, state:6, state:31, tens:92, vibes:13 — state:6 and state:31 are the two state-update entries at this anchor; they are distinct targets (studio.active_location and actor:taylor.location respectively) on two different schemas. No dedup fault.
- @90 (6 facets): feel:3, narrator:23, state:29, tens:85, vibes:3, vibes:10 — all distinct channels/targets.

---

## Class 7: SUPERFLUOUS

### Finding 7-A
- id: flag-010
- type: flag
- class: SUPERFLUOUS
- severity: SIGNAL
- what: tensometer entries `tens:79 @495`, `tens:80 @504`, `tens:123 @506`, `tens:143 @516`, `tens:147 @517`, `tens:148 @525` are anchored to proto-line IDs outside s01e01's aggregate range (1–155). Per the spec, tens=1 entries are never superfluous. However, entries anchored to non-existent proto-lines in this episode's file are superfluous by definition — they cannot be consumed by the s01e01 stitcher because they have no proto-line body to decorate. If these are season-window bones that do not fall in s01e01's episode range, they belong in the season-level tensometer file (tensometer-s01-window-02.md or -03.md) and not in the per-episode facet file.
- why: Six entries (plus the @518/123a entry flagged under STRUCTURAL) that cannot be stitched into the episode's output are superfluous decoration weight on the facet file. They do not pass the "decorates a proto-line" existence test required by the schema. The stitcher cannot resolve their anchors.
- routing: tensometer author (dramatist)

---

## Class 8: CONSTRAINT

### Finding 8-A
- id: flag-011
- type: flag
- class: CONSTRAINT
- severity: SIGNAL
- what: memory.md entry `mem:7 @98` description: "the city arrives the way a date arrives at a hand that already holds the book." This figure also appears verbatim in interest-narrator.md entry `narrator:25 @98`: "King's Landing arrives at the senses the way a date in a book arrives at a hand that holds the book." The memory entry's target reference reads "(westeros: foreknowledge-clamp on succession-window / Dance-timeline; margit-referral candidate for monument-dance-of-dragons)." The memory description is near-identical to the NI entry's figure — both use the date-arrives-at-the-hand-that-holds-the-book construction. The memory rubric constraint requires that memory entries have the NI spine (same-@) but must be non-redundant with the NI entry's content. The NI entry registers the perceptual event; the memory entry should register the monument-callback beneath it, not re-deliver the figure.
- why: The memory and NI entries at @98 share the same simile construction. The memory entry's description is the monument-signal, but the way it is written, the description IS the NI figure paraphrased. A reader of the cite-index sees two entries both carrying "date-arrives-at-hand-holding-book" at the same anchor. The CONSTRAINT rule for memory facet specifies "memory without NI-spine" as a violation (spine is present — satisfied); the concern here is near-redundancy of the figure itself between the two entries. The stitcher receiving both would have difficulty rendering one without echoing the other. This is a content-constraint seam rather than a hard violation, but it requires resolution at stitch time.
- routing: memory author (dialogue-writer-fork: taylor-hebert-flea-bottom); interest-narrator author for coordination

### Finding 8-B
- id: flag-012
- type: flag
- class: CONSTRAINT
- severity: HARD
- what: Earth-Bet hard-fence scan on interest-narrator.md. Entry `narrator:4 @11`: "the gaze rests on her at the angle Tya used to hold the chin; she had not adjusted for that." The name "Tya" is an in-world Westerosi name (the tanner's daughter whose body Taylor inhabits); this is NOT an Earth-Bet proper noun. PASS — this is correct usage. Full scan of all 39 NI entries, all 9 memory entries, all 13 feeling entries, all metaphor entries: no Earth-Bet proper nouns found (Brockton Bay, Skitter, Lung, Bakuda, PRT, Khepri, Cauldron, Undersiders, Coil, Dinah, Lisa, Brian, Rachel, Emma, Taylor used as address, Gold Morning named directly). The memory entries reference Earth-Bet monument families by structural description only ("refusal-to-look / locker-tutor / helpless-protector," "fauna-silence-at-scale / arrival-pattern," "peer-trust-test / undersiders-trust-pattern") without naming proper nouns. Hard fence: CLEAN.

  However, one proximity flag exists: memory entry `mem:4 @134` description contains "(earth-bet: fauna-silence-at-scale / arrival-pattern; margit-referral candidate for monument-endbringer-arrival)." The term "endbringer-arrival" appears in the target-reference field (parenthetical gloss), not in the prose-facing description field. The target-reference field is an internal routing label, not a stitched output. The "endbringer" lexeme appears only in the margit-referral gloss, not in any prose-rendering field. Per the schema, the target reference field is for routing, not for prose. This is at the edge of the hard-fence — "Endbringer" is an Earth-Bet proper noun class — but its containment in the margit-referral gloss rather than the prose description field means it does not violate the prose-facing fence. Flagged as a proximity concern; the margit-referral gloss should use monument-slug form rather than Earth-Bet class names.

- why: The target-reference field's use of "monument-endbringer-arrival" and "monument-annette-death" as slugs in mem:3, mem:4, mem:6, mem:8, mem:9 creates margit-referral slugs that contain Earth-Bet proper nouns (Endbringer, Annette). These are routing labels internal to the pipeline, but if margit receives them as card slugs, the margit-warehouse would contain cards with Earth-Bet proper-noun slugs, which is a downstream fence question. Current episode audit confirms no prose-facing violation. The margit-referral slug naming convention should be reviewed.
- routing: memory author (dialogue-writer-fork: taylor-hebert-flea-bottom); margit (for slug-naming convention audit before card authoring)

### Finding 8-C
- id: flag-013
- type: flag
- class: CONSTRAINT
- severity: SIGNAL
- what: vibes.md entry `vibes:11 @130` — `licensed-by: proto:130, proto:114, feeling-oc-broken-maester:1, tens:2`. The cite-index shows `tens:2 @2 r=1` (tens ID 2 anchors to proto-line @2, not @130). Licensing a tens entry by its ID number (tens:2) when that tens entry anchors to a different proto-line than the vibe entry is potentially a citation-by-ID rather than citation-by-reading. The schema says `<source>` may be `tens:<reading>` (reading being the rung value: 1, 2, or 3), not necessarily `tens:<ID>`. If `tens:2` in the licensed-by field means "tens rung 2 (a 2-rated tension scalar)" this is valid shorthand for the tens reading at the vibe's anchor proto-line. If it means "the tens entry with ID=2" that is a forward-anchor reference to a completely different proto-line (@2), which is an incoherent source citation. The same pattern appears in `vibes:5 @114 licensed-by: ... tens:2`, `vibes:8 @43 ... tens:3`, `vibes:3 @90 ... tens:3`, `vibes:10 @90 ... tens:3`, `vibes:17 @77 ... tens:3`, `vibes:1 @1 ... lic-out=[... tens:3]`.
- why: The `licensed-by: tens:<N>` notation is ambiguous — it could mean "tens reading N at this anchor" (a reading reference) or "tens entry with ID N" (an ID reference). The schema specifies `tens:<reading>` which implies rung-value. But the lic-out field in the cite-index uses the same notation (e.g., `vibes:2 lic-out=[... tens:3]`). If lic-out references the rung-value, the interpretation is "this vibe licenses downward something at rung-3" which is semantically valid. Auditor cannot resolve this ambiguity without rubric clarification, but the cross-citation coherence cannot be verified without knowing which interpretation the cite-index uses. If any lic-out entries in the cite-index refer to tens entry IDs rather than readings, the DAG may be incoherent.
- routing: showrunner (vibes author); cite-index generator for notation clarification

---

## Class 9: AP-SCAN

### Finding 9-A
- id: flag-014
- type: flag
- class: AP-SCAN
- severity: SIGNAL
- what: interest-narrator.md entry `narrator:25 @98`: "King's Landing arrives at the senses the way a date in a book arrives at a hand that holds the book." This entry uses a simile ("the way a date in a book arrives at..."). The narrator-interest rubric (per the NI voice §Reject) flags ornamental simile as a reject-signature. The R1 author flagged this as SEAM-3 and the R2 judge retained it as "functional (Dance-foreknowledge clamp expressed as the date-in-the-book figure, named-monument-free)." The R2 verdict defense is that the figure is the content of the foreknowledge-clamp, not an ornament. The rubric's simile-reject is on ornamental comparisons; a figure that IS the channel-content may be defensible under the doubled-register rubric. However, the NI facet schema specifies "one-clause description of what the narrator registers" — the date-in-a-book comparison is a two-clause simile, not a one-clause description. AP-SCAN flags this as an NI form-discipline question: the schema's one-clause shape is violated by the simile's two-part structure ("King's Landing arrives at the senses [clause 1] the way a date in a book arrives at a hand that holds the book [clause 2]").
- why: Simile within NI content field is an AP-scan flag. The R2 judge defended the figure's register but did not address the one-clause form-discipline requirement. Even if the figure's functional register survives the simile-reject scan, the form question (one-clause vs two-clause) remains open. Fixer or editor should confirm whether the form deviation is within-spec.
- routing: interest-narrator author (dialogue-writer-fork:taylor-hebert-flea-bottom); editor for form-discipline call

---

## Class 10: TASTE-FLAG

No TASTE-FLAG findings. Signal-class assessment:

- Atmosphere-thin risk: Scene E (reeve, bones 63–70) is the locus of KICKBACK-1 (no peak registration). The NI fires on the scene (narrator:15 @63, narrator:16 @66) hold the atmosphere via watch-cost pricing. The KICKBACK-1 is a CURVE-SHAPE structural issue already flagged (4-A) rather than an atmosphere-thin in the rendering sense — the atmosphere is present; the tens peak is absent.
- Momentum-stall risk: Scene J (perimeter walk, bones 109–118) is the KICKBACK-2 locus (sustained-2 plateau without rupture). The NI fires at @110 and @114 carry momentum through the beetle-expansion and maester-recognition. Stall risk is structural (tens), not NI-rendering.
- Voice-fidelity: The interest-narrator simile at @98 (flagged at 9-A) is the only voice-fidelity proximity flag. R2 retained it; the dialect audience should confirm.

TASTE-FLAG: No additional finds beyond cross-references to 9-A.

---

## Class 11: PILE-UP REVIEW

Pile-ups per cite-index (>4 co-located facets):

### @98 (8 facets): loc-state:1, mem:7, narrator:25, sensory:4, state:6, state:31, tens:92, vibes:13
Proto-line: `taylor-hebert-flea-bottom enters loc-flea-bottom`
Verdict: **WARRANTED**
Rationale: This is the episode's locale-establishment threshold-cross for King's Landing — the single most load-bearing environmental transition in the episode. All 8 facets carry distinct jobs: loc-state establishes the first carded location; mem:7 opens the Dance-foreknowledge monument; narrator:25 is the POV's arrival registration; sensory:4 fires the smell modality at the locale shift; state:6 flips studio.active_location; state:31 flips actor:taylor.location (two distinct target schemas); tens:92 places the approach-zone rung; vibes:13 opens the operational-territory vibe. No entry is decorative. The density is structurally warranted for the episode's most event-dense anchor.

### @43 (7 facets): feel:8, mem:6, narrator:12, sensory:3, tens:41, vibes:8, vibes:9
Proto-line: `oc-tanner-mother drops the song`
Verdict: **WARRANTED**
Rationale: The episode's Scene C tens=3 reversal-proximity peak. feel:8 is the mother's somatic-arrest; mem:6 opens the failed-recognition monument; narrator:12 registers the silence-as-shape; sensory:3 fires the sound-drop; tens:41 is the rung; vibes:8 opens grief-without-object; vibes:9 opens asking-around-the-edge on the mother. The two vibes entries are distinct vibe-keywords on the same target — both warranted as separate persistent operator-bias additions. All seven entries do distinct work at the episode's structurally richest beat.

### @103 (7 facets): loc-state:2, narrator:27, state:10, state:32, tens:97, vibes:15, vibes:16
Proto-line: `taylor-hebert-flea-bottom enters loc-flea-bottom-base`
Verdict: **WARRANTED**
Rationale: Second locale-establishment threshold-cross (base lodging). Same structural logic as @98 — locale arrival requires loc-state, location-flip on two schemas, vibes establishing the operational platform, NI registering the threat-sweep, tens placing the transition. Both vibes entries are distinct keywords (first-lodging-anchored vs maester-connectivity-established) on the same target. Warranted density.

### @90 (6 facets): feel:3, narrator:23, state:29, tens:85, vibes:3, vibes:10
Proto-line: `oc-tanner-elder routes taylor-hebert-flea-bottom`
Verdict: **WARRANTED**
Rationale: Scene H tens=3 reversal-proximity peak — the elder's routing is the irreversible institutional act. feel:3 is the elder's assessment-already-complete somatic; narrator:23 is Taylor's gate-pricing interior; state:29 flips Taylor's placement-status; tens:85 is the rung; vibes:3 extends the Tya-shaped-debt vibe; vibes:10 opens the conditional-ledger vibe on the elder. Six entries at the episode's largest structural pivot; all warranted.

### @154 (5 facets): feel:13, mem:9, narrator:40, state:34, tens:145
Proto-line: `taylor-hebert-flea-bottom speaks to oc-dock-runner`
Verdict: **WARRANTED**
Rationale: Scene N tens=3 (per rubric @151 is the tens=3 anchor; @154 is tens=1 per tensometer:145 r=1, but the NI and memory authors defend firing on the commitment-act rather than the verbal-prelude). Five entries: feel:13 (hand-stillness somatic), mem:9 (peer-trust monument), narrator:40 (first-irreversible-thing interior), state:34 (network-anchor state flip), tens:145 (r=1 rung). All distinct. One minor note: the tens scalar at @154 is 1, but four non-tens facets fire here — the pile-up is low-tens-density rather than tens-peak-density, which is the expected pattern for a commit-beat where the interior registrations outpace the kinetic tension. Warranted.

---

## Summary Table

| Class | Finding ID | Severity | Routing |
|-------|------------|----------|---------|
| STRUCTURAL | flag-001 | HARD | tensometer (dramatist) |
| STRUCTURAL | flag-002 | HARD | tensometer (dramatist) |
| STRUCTURAL | flag-003 | SIGNAL | studio + state-updates authors |
| STRUCTURAL | flag-004 | SIGNAL | interest-narrator author |
| FREQUENCY-BAND | flag-005 | HARD | tensometer (dramatist) |
| FREQUENCY-BAND | flag-006 | SIGNAL | interest-narrator author |
| FREQUENCY-BAND | flag-007 | SIGNAL | feeling-facet authors; editor |
| METADATA-INCONSISTENCY | flag-008 | SIGNAL | tensometer (dramatist) |
| CURVE-SHAPE | flag-009 | SIGNAL | tensometer (dramatist); screen-writer |
| CONSTRAINT | flag-011 | SIGNAL | memory author; NI author |
| CONSTRAINT | flag-012 | HARD (proximity) | memory author; margit |
| CONSTRAINT | flag-013 | SIGNAL | showrunner (vibes); cite-index |
| AP-SCAN | flag-014 | SIGNAL | interest-narrator author; editor |
| SUPERFLUOUS | flag-010 | HARD | tensometer (dramatist) |

**HARD findings: 4** (flag-001, flag-002, flag-005, flag-010; flag-012 is proximity-HARD)
**SIGNAL findings: 9** (flag-003, flag-004, flag-006, flag-007, flag-008, flag-009, flag-011, flag-013, flag-014)

**CONTRADICTION: 0**
**DEDUP: 0**
**TASTE-FLAG: 0 (independent; 9-A cross-reference noted)**
**PILE-UP: 5 reviewed; 5 WARRANTED**

---

## Routing Section

| Agent | Findings | Action |
|-------|----------|--------|
| tensometer author (dramatist) | flag-001, flag-002, flag-005, flag-008, flag-009, flag-010 | Resolve out-of-range bone anchors; fix non-monotonic ID 123a; address 2s frequency-band below-floor or confirm rubric exemption; clean metadata inconsistency; document kickback carry-forward status |
| studio (state-updates env) | flag-003 | Multi-source file format deviation; consider consolidation or schema note |
| interest-narrator author | flag-004, flag-006, flag-014 | Remove stale pre-R2 density figure; confirm 25.2% ceiling overage with editor; address one-clause form question on @98 simile |
| feeling-facet authors (all character forks) | flag-007 | Confirm per-character sparsity rubric interpretation for lightly-appearing characters |
| editor | flag-006, flag-007, flag-014 | Rubric calibration calls on NI ceiling, feeling per-character floor, and NI form discipline |
| memory author | flag-011, flag-012 | Coordinate with NI author on @98 figure near-redundancy; review margit-referral slug naming for Earth-Bet proper-noun containment |
| showrunner (vibes author) | flag-013 | Clarify tens:<N> notation in licensed-by fields (reading vs ID) |
| cite-index generator | flag-013 | Clarify lic-out tens:<N> notation across all entries |
| margit | flag-012 | Slug naming convention review before monument card authoring |
| screen-writer | flag-009 | KICKBACK-1 and KICKBACK-2 carry-forward to window-revise if triggered |
