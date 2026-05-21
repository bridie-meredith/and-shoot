---
audit: facets-final-r1
scope: chapter
target: b01c02
timestamp: 2026-05-21
mode: flag-only
status: FINDINGS-PRESENT
totals:
  STRUCTURAL: 1 finding (1 flag)
  FREQUENCY-BAND: 0 findings
  METADATA-INCONSISTENCY: 1 finding (1 flag)
  CURVE-SHAPE: 0 findings
  CONTRADICTION: 1 finding (1 flag)
  DEDUP: 0 findings
  SUPERFLUOUS: 0 findings
  CONSTRAINT: 2 findings (1 flag, 1 fault)
  AP-SCAN: 1 finding (1 flag)
  TASTE-FLAG: 1 finding (1 flag)
  PILE-UP-REVIEW: 1 finding (1 flag)
  RUBRIC-FIDELITY: 2 findings (1 flag, 1 fault)
  hard_total: 2
  signal_total: 8
---

# Facets Final Audit — b01c02

Phase 5 cross-cutting twelve-class graph audit. Mode: FLAG-ONLY (all findings route back to authors; no deletes executed here). Date: 2026-05-21.

---

## Pre-audit context verification

The dispatch brief identified four known items for verification:

1. **feel:1 (coll @12) DELETED** — confirmed. `feeling.md` contains the deletion comment at the coll-net-mender slice; `vibes:10 + state:10` carry the not-naming beat; R2 shard records `f-r2-1: 1` for this DELETE under R2.3. The deletion is rubric-correct per the R2 shard's three independent grounds.

2. **meta:1 @28 DELETED** — confirmed. `metaphor.md` carries the deletion comment; R2.4 shard records three compounding failure grounds (unresolvable `memory:@9` anchor, AP7 peak-bone default-refuse, G5 premature-closure). Deletion is rubric-correct.

3. **exposition:2 @2 + exposition:3 @8 DELETED** — confirmed. Shard R2.5 records both as DELETED: :2 (water-carrier, single-mention non-load-bearing fixture); :3 (near-witness, NI-establishing coverage). IDs retired; the surviving register write-back covers only pressed-labor-sweep @4 and ledger @23.

4. **exposition:4 re-anchored @5→@4** — confirmed. Shard R2.5 records REVISE with G5 position rationale. `exposition-b01-c02.md` shows entry 4 anchored at @4 with `renders-as: post-bone-clause`.

5. **mem:2 @25 peak-bone exception** — verified against rubric. The R2.2 shard explicitly adjudicates both exception criteria: (a) displacement-clamp construction holds ("a tongue that outlived the hand that set it" — charter-language clamp); (b) resonance-not-action argument holds (narrator:5 @25 carries the peak as action; memory fires on what the strike discharges). Per-scene cap satisfied (only memory fire in scene-C). The exception is formally valid under rubric-memory-flags §Licensing-discipline / quiet-beat anchor / peak-bone exception.

---

## Class 1: STRUCTURAL

### Finding S-001

- **id:** flag-001
- **type:** flag
- **what:** `state-updates.md` lines 2-4 carry consolidated frontmatter with `sources:` list, but the individual source-slice headers (lines 8-9, 63-68, 72-76, 83-86) each also contain their own `facet: state-updates` + `episode: b01c02` + `author:` + `source:` frontmatter. This creates a double-frontmatter structure: one consolidated block at the file top plus per-slice mini-frontmatter bodies. The `schemas/facet.schema.md` specifies a single top-of-file frontmatter; the per-slice headers are an extension not covered by the schema.
- **why:** The stitcher and cite-index builder consume `facets/state-updates.md` as a unified file. Double frontmatter (one file-level + N slice-level) risks parser ambiguity at stitch-time if the downstream consumer expects a single `---` block. The r3-signal-001 note references consolidation by `build_cite_index`; if the cite-index builder already handles this structure, the flag is advisory only. The schema should reflect the extension or the per-slice headers should be converted to comments.
- **routing:** studio (state-updates author); stitcher/build_cite_index maintainer to confirm parser handles multi-block front-matter gracefully.

---

## Class 2: FREQUENCY-BAND

No findings. Density measurements:

- **loc-state:** 11 entries / 27 bones = 40.7%. Within the studio-authored location-state rubric's necessity gate (fires at movement/positioning verbs + new-location anchors). All 11 entries attach to movement/positioning/entry/exit verbs or first-in-new-location anchors. No density cap specified for loc-state; the rubric's frugality axis is per-entry (not file-level band), and all entries survive strip-test inspection.
- **narrator (interest):** 6 entries / 27 bones = 22.2%. Well inside the 25% ceiling per the rubric. The R2 shard pattern-scan confirms 22% fire density and all six entries earn their peaks.
- **state-updates:** 15 entries / 27 bones = 55.6%. This is above the rubric's 8–18% band cited for a 77-bone chapter, but the b01c02 chapter contains only 27 bones. Scaling: 15 entries on 27 bones = 55.6%, which is elevated. However, 6 of the 15 entries are oc-prop field-extensions (entries 4, 5, 6, 7, 8, 9) covering the lamp/ledger/pen sequence in scene-C, which constitute genuine persistent state-changes on project-original props. The rubric's density band (8–18%) was calibrated on a 77-bone chapter; on a 27-bone chapter, proportional adjustment brings the high-end to roughly 5 entries. 15 entries is still above the adjusted band. This is addressed under RUBRIC-FIDELITY (finding RF-001) below.
- **memory:** 2 entries / 27 bones = 7.4%. Within the 5–12% sparsity band per rubric. Pass.
- **feeling:** 2 active entries (feel:1 deleted; feel:2 @28 taylor; feel:2 @15 wren — note: the numbering in the file shows `1 @28` and `2 @15` within the consolidated file). 2 / 27 = 7.4%. Within rubric's sparse-by-design frugality. Pass.
- **sensory:** 2 entries / 27 bones = 7.4%. The short-chapter floor-vs-ceiling exemption (V3) applies: bone_count 27 < 30, modality count = 2 (sound + light), floor met. Sparsity exceeds 6% ceiling by 1.4pp but the exemption explicitly marks above-band density as ADVISORY when floor = 2 on short chapter. Advisory, not blocking.
- **vibes:** 14 entries. No upper density ceiling in rubric; per rubric §Vibes "loosest facet by sparsity (no upper ceiling)." File-level gate is operator-bias-actionability and licensed-by-resolvable. See RUBRIC-FIDELITY for any per-entry concerns.
- **exposition:** 3 surviving entries (@0, @4, @23). Three entries for a 27-bone chapter is sparse; the rubric specifies audience-gap-driven necessity. All three surviving entries have been R2-validated. Pass.
- **metaphor:** 0 surviving entries (meta:1 deleted). Zero fires = within rubric (0–3% = zero acceptable). Pass.
- **dialogue:** 3 entries total (wren:1 @19; taylor:1 @20; taylor:2 @20). Speech bones are @19 (wren) and @20 (taylor). Per-anchor cap ≤3 met; both anchors covered. Dialogue-coverage gate: speech_bones [19, 20], both covered. Pass.

---

## Class 3: METADATA-INCONSISTENCY

### Finding M-001

- **id:** flag-002
- **type:** flag
- **what:** The R2 consolidated decisions file (`facets/.r2-decisions.md`) frontmatter records `f-r2-counts: {f-r2-1: 1, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}` and `discipline-fails: 0`. The `f-r2-1: 1` traces to R2.3 (feeling-coll; DELETE feel:1 @12 on rubric-form grounds — second-clause subject-shift to "the shuttle" exiting somatic register). The shard for R2.3 (coll slice) correctly records `f-r2-counts: {f-r2-1: 1}`. However, the Taylor-feeling shard R2.3 references `feel:2 @28` in its body (the keep verdict), but the top-of-file frontmatter in `feeling.md` numbers the Taylor entry as `1 @28` and the Wren entry as `2 @15`. The file-level IDs do not match the shard numbering: R2.3 Taylor shard refers to "feel:2 @28" throughout but the feeling.md consolidated file assigns `1 @28` to Taylor and `2 @15` to Wren. This is a numbering discrepancy between the shard's internal references and the final facet file.
- **why:** The cite-index resolves `feel:1 @28` and `feel:2 @15`. If the Taylor shard was authored when Taylor's entry was provisionally `feel:2`, the shard's internal citations (`feel:2 @28`) will not resolve against the cite-index's actual IDs (`feel:1 @28`). The cross-facet contract in `narrator.md` cites `feel:2` in the R2 shard analysis for the @28 anchor. The cite-index confirms the correct live ID as `feel:1 @28`. The shard's internal citation is stale.
- **routing:** feeling-author (impersonator-taylor-hebert-kl-122ac slice); R2 decision-log maintainer. Update shard internal citations to match the final feeling.md IDs. No content change required — only shard-internal reference strings.

---

## Class 4: CURVE-SHAPE

No findings. Per-facet curve checks:

- **memory:** Two fires. Scene-A: mem:1 @8 (peak-shadow bone, settle-tail of rise-peak-settle; quiet-beat licit). Scene-C: mem:2 @25 (peak-bone, exception explicitly granted under R2.2 with displacement-clamp + resonance-not-action). Per-scene cap (1 per scene): scene-A 1, scene-B 0, scene-C 1 — compliant. Doubled-register: mem:1 = Earth-Bet displacement (cost-borne-by-the-unconsenting); mem:2 = Westerosi-monument clamp (conquest-charter-language). Both registers represented. Inverted pressure-signal alignment: 1 of 2 fires is at a peak-bone (with granted exception); the non-peak fire is in settle-tail — distribution acceptable under the peak-bone exception path.
- **narrator:** Six fires. Scene-A: @4, @5, @8. Scene-B: @15. Scene-C: @25, @28. Peak-bones (@5, @15, @25) all carry fires — correct for narrator-interest (fires on rising zones and peak-bones). Scene-C has two fires; scene-C contains two peak-bones (@25, @28); both are documented. No anti-pattern.
- **sensory:** Two fires, two distinct modalities (sound:1 @7; light:2 @22). Cross-modal coverage met. Short-chapter floor exemption applies (see FREQUENCY-BAND). Inflection-pair: no drop/up pair on same modality — no coherence check needed. Both entries anchor to distinct inflection points.
- **feeling:** Two fires (taylor @28 scene-C; wren @15 scene-B). Per-character per-scene caps: Taylor scene-C cap used once (only fire in chapter); Wren scene-B cap used once. No character over-fires a scene.

---

## Class 5: CONTRADICTION

### Finding C-001

- **id:** flag-003
- **type:** flag
- **what:** `state-updates.md` entry 11 (@5): `actor:taylor-hebert-kl-122ac.capability-deployment-history: dormant-never-deployed-in-kl -> deployed-defensive-flea-bottom`. `state-updates.md` entry 2 (@5): `studio.fauna_sense_status: lane-filling-active -> lane-mouths-closed-routing-active`. These two entries both fire at @5 and both represent the deployment hinge. Cross-referencing with `showrunner/memory.md` (b01c02 handoff_out): `capability 4 (first deployment executed)`. No contradiction within the facets.

  However, state:12 @15 records `actor:taylor-hebert-kl-122ac.social-tether-wren: peripheral-permitted-attachment -> crystallized-observer-bond`. The `showrunner/memory.md` b01c02 scene B (`b01c02s02`) records social-tether moving from rank 2.1→2.4 in scene-B, and Wren-layer crystallizes here. The state-update field `social-tether-wren` is a Taylor-authored actor-state entry. Cross-checking the rubric: `actor:<POV-character>.*` entries require narrator-interest co-citation. `narrator:4 @15` fires: "Wren is looking at her the way you look at a thing you have decided about, and that look does not have a column in the ledger." This is Taylor registering Wren's crystallization from outside — the NI entry is Taylor's perception of Wren's state, not Taylor's own actor-state shifting. The state:12 field `social-tether-wren` is a POV actor-state shift (it changes Taylor's social-tether subfield). The narrator-interest co-citation requirement fires on `actor:taylor.*` entries; `narrator:4 @15` IS present. Co-citation satisfied.

  The actual contradiction is subtler: state:15 @15 records `actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness: observed-and-decided-not-to-ask -> attachment-crystallized-deliberate-observer`. This entry is a non-POV actor-state entry written by `impersonator-wren-stitch-maker-flea-bottom-ward` (source: wren-stitch-maker-flea-bottom-ward). The rubric allows non-POV actor-state entries without narrator-interest co-citation — confirmed. The wren-fork authoring wren's state is authority-compliant. No contradiction.

  The flag is: the R2 decision shard for Taylor's feeling entry (R2.3 Taylor) refers internally to `feel:3 @15` for the Wren entry, but the cite-index and the feeling.md file show `feel:2 @15`. This is a cross-reference inconsistency in the shard prose (not in the deployed facet graph). Already flagged as M-001. No additional finding.

  No new CONTRADICTION finding — class produces zero faults. Withdrawing the flag premise above.

  **Corrected status: 0 findings in class CONTRADICTION.**

---

## Class 5: CONTRADICTION (corrected)

No findings after cross-graph verification. Per-field consistency checks passed across loc-state / state-updates / narrator / scene-map.

---

## Class 6: DEDUP

No findings. The DEDUP check examines whether any facet entry explicitly states what another facet already shows at the same anchor, such that the stitcher would render duplicate content. Spot-checks:

- @5 (8-facet pile-up): loc-state:3 names the sealed lane-mouths; narrator:2 adds the moral-framework justification ("routing is what the prohibition still permits her to call clean"); state:2 + state:11 write the deployment history. The four vibes entries (:1–:4) are word-algebra tokens (not prose). No surface-text duplication.
- @15 (7-facet pile-up): feel:2 shows Wren's body; narrator:4 registers Taylor's cognition of Wren's look; state:12 + state:15 write actor-state fields; vibes:6 + vibes:7 are tokens; loc-state:9 places the physical gap. No surface-text duplication.
- @28: feel:1 shows Taylor's hand closing short; narrator:6 registers the not-closing as the only sure line. These are distinct jobs (somatic show vs. cognition registration). meta:1 was deleted; no allegory conflicts. No DEDUP.

---

## Class 7: SUPERFLUOUS

No findings. The cite-index "lonely entries" list (loc-state:1 @2, loc-state:8 @14, state:1 @1, state:8 @27, exposition:1 @0) are examined:

- `loc-state:1 @2`: @2 is "the water-carrier enters the doorway." The lone co-location status is expected — exposition:2 was deleted at R2 (water-carrier not load-bearing); no other lens fires at @2. The loc-state entry itself anchors the doorway threshold geometry ("alley-width just wide enough for one body at a time") which is the spatial fact making the sweep's approach legible to the reader. The rubric's necessity gate: @2 is an entry/movement bone and the sensory note names the specific spatial constraint the sweep approach requires. Strip-test passes — without the entry the doorway geometry is unanchored. Not superfluous.
- `loc-state:8 @14`: @14 is "taylor-hebert-kl-122ac faces the alley-mouth." This is the scene-B opening orientation. The loc-state entry ("the alley-mouth Taylor faces: open again, the Watch column well past, ordinary foot-traffic re-establishing") re-establishes the post-sweep environment at the scene-B open. Rubric: "first beat in a new location-and-moment" license applies — the sweep has passed and the environmental state has changed since loc-state:7. Not superfluous.
- `state:1 @1`: First touch on `studio.fauna_sense_status`. Maps "ambient-passive → lane-filling-active." This is the canonical first-deployment state-write. Not superfluous.
- `state:8 @27`: `prop:oc-pen.state: in-hand -> set-down`. This is a persistent physical-state change (pen goes down; bones @28 "holds the hand" and @29 "closes the ledger" operate without the pen). Strip-test: without this entry, the pen state is untracked through the holding-the-hand and closing-the-ledger bones. Not superfluous.
- `exposition:1 @0`: Prior-episode-bridge. No back-link (back=N in cite-index) because @0 is the only item at position 0 and nothing else decorates the pre-bone preamble slot. Correct; not superfluous.

---

## Class 8: CONSTRAINT

Earth-Bet hard-fence proper-noun scan across all facet text fields and dialogue utterances:

**Dialogue scan:** Scanned all utterance text.
- wren:1 @19: "The flies were round you again. They were round you on Tickler's Lane two days gone, and the lane went quiet after. It goes quiet where you've been. I weren't looking for it. I just saw." — CLEAN. No Earth-Bet proper nouns.
- taylor:1 @20: "The watch came through. They did not stop. That is all it was." — CLEAN.
- taylor:2 @20: "Go home, Wren. The street is quiet now." — CLEAN.

**Facet text field scan (description/sensory note/gloss/vibe-token fields):**
- `narrator:2 @5`: "routing is what the prohibition still permits her to call clean" — references "prohibition" (project-term, not Earth-Bet proper noun). CLEAN.
- `mem:1 @8`: "the count of who saw was set by faces she did not pick, the way a cost has settled on people who never agreed to carry it before -> monument-cost-borne-by-the-unconsenting" — target-reference uses mechanism-descriptive slug per rubric (URI-032). Description is displacement-cue form, no proper noun. CLEAN.
- `mem:2 @25`: "the struck line is a decision written down and then unwritten, and she has felt the weight of that kind of word before, in a tongue that outlived the hand that set it -> monument-conquest-charter-language" — description is displacement-cue form, no proper noun. Target reference: `monument-conquest-charter-language` is a mechanism-descriptive Westerosi-monument slug, permissible. CLEAN.
- All vibes tokens: word-algebra only; no Earth-Bet proper nouns found. CLEAN.
- All exposition gloss-text fields: CLEAN.

### Finding CN-001 (HARD fault)

- **id:** fault-001
- **type:** fault
- **what:** `exposition-b01-c02.md`, entry 5 @23 (ledger gloss): "the book I keep by lamplight — a running account of every cost my actions make that I cannot pay back." The gloss itself is clean. However, the `sources:` citation for exposition:5 includes `facets/exposition-b01-c01.md (the-prohibition gloss-id 1)`. The cross-episode register write-back comment states that `pressed-labor-sweep` was already glossed at b01c02, first-mention-anchor @4. The register write-back section also reads: "R2 NOTE: near-witness (gloss-id 3) and water-carrier (gloss-id 2) DELETED at R2 — both removed from register write-back. The R1 glossed-terms.md already carries near-witness and water-carrier lines (added at R1 cite-index merge); the Phase 4 cite-index rebuild must strike BOTH."

  The fault: the instruction "Phase 4 cite-index rebuild must strike BOTH [near-witness and water-carrier]" is written inside the exposition file and flagged for an action, but there is no evidence in the delivered files that this strike was executed. The `_cite-index.md` does not reference `water-carrier` or `near-witness` as terms (the cite-index does not track the glossed-terms.md register directly), but the glossed-terms.md register itself is not in-scope for this audit as a delivered file. The R2.5 shard explicitly flags: "Phase 4 cite-index rebuild must strike BOTH." This action was a pre-audit requirement; if it was not executed, the glossed-terms.md register carries two stale entries that will instruct future chapters to skip re-glossing these terms, which would cause a first-mention-character coverage failure downstream if they appear again.

- **why:** If `water-carrier` and `near-witness` remain in the glossed-terms register as "already glossed," a future chapter where either figure appears will be exempted from re-glossing under the cross-episode register's "already covered" rule, but the glosses were deleted — so the future-chapter reader will have no orientation. This is a downstream continuity-coverage failure that cannot be detected at stitch time.

- **criteria:** The `staff/exposition-author/glossed-terms.md` register must have the `water-carrier` (gloss-id 2) and `near-witness` (gloss-id 3) entries struck, consistent with their R2.5 deletion. The `pressed-labor-sweep` anchor must be corrected from @5 to @4 in the register. These are register write-back mutations, not facet content changes.

- **routing:** exposition-author; cross-episode glossed-terms.md register maintainer.

### Finding CN-002

- **id:** flag-004
- **type:** flag
- **what:** Exposition license-completeness check — first-mention-character coverage. The chapter proto-lines include @2 "the water-carrier enters the doorway" and @8 "the near witness faces the alley-mouth." Both were glossed at R1 and both glosses were deleted at R2 on load-bearing / NI-coverage grounds. The rubric's Always-gloss: "Named individuals appearing in prose without prior introduction" — check whether "water-carrier" and "near witness" are named individuals vs. set dressing. Rubric exclusion: "the carter, the dock-runner, the lord's-man" as definite descriptions needing first-mention glosses, but excludes "a bowl on the table" as obvious English nouns. The water-carrier is a compound noun that "self-glosses" (R2.5 verdict), and the near-witness is established as a type (not a named individual) whose function is wholly carried by narrator:3 and mem:1. The deletions are rubric-correct. However, the embedded-noun completeness rule (URI-FACETS-CYCLE-1) requires checking whether any surviving exposition gloss-text contains un-glossed proper-noun frames. Exposition:4 @4 gloss text: "when the city's hired watchmen need hands for a public work, they sweep a poor district and conscript whoever cannot prove they are wanted elsewhere. In Flea Bottom there is rarely anyone who can." — "Flea Bottom" appears in this gloss. Is "Flea Bottom" on the cross-episode glossed-terms register or in the project's always-known register? The showrunner memory records "place: King's Landing — Flea Bottom anchor" in constraints.settings — Flea Bottom is a project-canonical location present from series open. For the active audience (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant), Flea Bottom is introduced in b01c01 and is part of the series constraint register. The embedded-noun fault would require "Flea Bottom" to be un-glossed AND audience-unknown. Given b01c01 established it and the cast is familiar, this reads as advisory rather than HARD. Flagging for editorial confirmation that "Flea Bottom" is on the always-known register for b01c02 readers (having been established in b01c01 via exposition or prose).

- **why:** If b01c02 is the first episode a reader encounters (prior-episode-bridge exists for exactly this case), the prior-episode-bridge at @0 mentions "this body and this city" and "a ledger by lamplight" but does not name Flea Bottom. The watch-sweep gloss at @4 references Flea Bottom as a location identifier without defining it. A reader joining cold at b01c02 may not have "Flea Bottom" in their orientation frame.

- **routing:** exposition-author. Verify whether "Flea Bottom" should appear in the b01c02 prior-episode-bridge or whether the @4 gloss should replace "In Flea Bottom" with a brief appositive ("in Flea Bottom, the city's poorest ward, there is rarely anyone who can").

---

## Class 9: AP-SCAN

### Finding AP-001

- **id:** flag-005
- **type:** flag
- **what:** URI-AP-SCAN-SATURATION severity calibration check on `interest-narrator.md`. The R2.1 shard pattern-scan explicitly notes: "the one thing my ear flagged is the inverted-predicate shape: narrator:2 ('routing is what the prohibition still permits her to call clean') is a clean single use of the AP-10 definitional template. narrator:6 brushes near it ('the not-closing is the only line tonight she is sure of') but resolves a perception into an *uncertainty registration*, not a rule, so it does not count as a second template instance." The R2 shard adjudicates this as cleared. The audit confirms: the AP-10 (inverted-predicate definitional template) fires once (narrator:2) and is handled. However, the saturation-calibration scan also requires examining whether the cost-tracking vocabulary (`count`, `cost`, `column`, `ledger`, `accounting`, `price`) saturates across the six NI entries at a frequency that normalizes the register to the point where no individual fire carries weight. Checking: narrator:1 (no cost vocab); narrator:2 (`permits` — rubric-term, not saturation); narrator:3 (`watch-cost`, `priced`, `count`); narrator:4 (`column in the ledger`); narrator:5 (`counted`, `count is short`); narrator:6 (`line`). Three of six entries use counting/ledger vocabulary. The rubric notes this is "Taylor's resting unit of measure per the card, not an authorial chassis." Given the Taylor card explicitly cites cost-tracking as a named channel and the chapter's substance is a ledger-accounting sequence (scene-C), the density is register-coherent, not saturation. Advisory only.

- **why:** If the cost/count vocabulary pattern persists at this density into subsequent chapters without relief, it will read as authorial chassis rather than character voice by approximately b01c04. This is a carry-forward advisory rather than a b01c02 fault.

- **routing:** interest-narrator author (impersonator-taylor-hebert-kl-122ac); note for b01c03 authoring brief to vary the registration vocabulary away from cost-ledger-count cluster at least once per three entries.

---

## Class 10: TASTE-FLAG

### Finding TF-001

- **id:** flag-006
- **type:** flag
- **what:** `vibes.md` entry 14 @20: `actor:taylor-hebert-kl-122ac ++ earning-collapse: [speech-exchange-as-the-first-actualized-wren-layer, the-moment-the-un-priced-speaks-back]`. The token `earning-collapse` does not appear in the pre-seeded vibe-cloud (showrunner memory `series.vibe_cloud.keys`) or in the book-level vibe-cloud. Per rubric, `+` requires keyword absent from target's current vibe-set — this is a new keyword, which is compliant for `+`. However, the token `earning-collapse` invokes a specific book-level dramatic mechanism ("three mistakes" per the b01c02 chapter context, per the sidecar `world-build:earning-collapse-three-mistakes`). The `licensed-by` cites `world-build:earning-collapse-three-mistakes` — this is a world-build gloss, not a named card or state-update. Per rubric Gate 4 (licensed-by resolvable), the source must point to an existing facet entry, proto-line, or named canon/world-build context. A `world-build:` gloss is permitted as a source form per the schema. However, there is no `world-build` card slug `earning-collapse-three-mistakes` visible in the warehouse. This is a world-build gloss pointing to a narrative concept, not to an on-disk resource. The rubric permits free-gloss world-build sources but the operator-bias-actionability test (Gate 6) applies: does `earning-collapse` as a keyword bias downstream operators in a recoverable way? The token `earning-collapse` is unusual and could be mistaken for a collapse-type event (narrative collapse) rather than a crystallization; the token bundle `[speech-exchange-as-the-first-actualized-wren-layer, the-moment-the-un-priced-speaks-back]` is more legible. The keyword itself is the gate concern.

- **why:** Downstream operators (stitcher, screen-writer) reading the vibe-cloud key `earning-collapse` without access to the `world-build:earning-collapse-three-mistakes` gloss may interpret it as a macro-level narrative collapse event rather than as the crystallization of Wren's un-priced layer. The token bundle clarifies but the keyword misleads. This could bias the stitch toward a deflationary register at @20 when the intended register is crystallization.

- **routing:** showrunner (vibes author). Consider renaming keyword to `wren-layer-actualization` or `un-priced-crystallization` for operator-clarity. Alternatively, add a world-build context note in the vibes file comment.

---

## Class 11: PILE-UP REVIEW

The cite-index identifies two pile-ups:

**@5 (8 facets):** `loc-state:3, narrator:2, state:2, state:11, vibes:1, vibes:2, vibes:3, vibes:4`
- Scene-map: peak-bone ("chapter hinge — insect-deployment commitment must not collapse into ellipsis"); protected pattern.
- loc-state:3 (lane-mouths sealed — environmental state-change; correct at peak).
- narrator:2 (moral-framework justification — correct peak NI fire).
- state:2 (studio.fauna_sense_status deployment write-back — canonical state change; correct at peak).
- state:11 (actor:taylor.capability-deployment-history — first deployment; correct at peak).
- vibes:1–4 (four vibe-cloud tokens firing at the chapter hinge).

### Finding PU-001

- **id:** flag-007
- **type:** flag
- **what:** The four vibes entries at @5 (vibes:1–4) all fire at the chapter peak-bone. Per rubric §Op coherence: `+` requires keyword absent from target's current vibe-set for each. The four entries target distinct keyword/target pairs: `actor:taylor ++ insects` (vibes:1), `actor:taylor ++ override-architecture-residue` (vibes:2), `loc:flea-bottom + operational-substrate` (vibes:3), `episode + first-deployment` (vibes:4). All four are new keywords per the `+` op. However, the rubric's AP1 (transient-as-vibe) — test: would this still be true at b01c03 open? — applies to each. `vibes:1` (taylor ++ insects routing-without-contact): this vibe is about the *manner* of the first deployment; it would be superseded at b01c03 by the ongoing deployment pattern — potentially transient. `vibes:2` (taylor ++ override-architecture-residue: constraint-tested-not-broken): this token is the permanent residue characterization and survives past b01c02. `vibes:3` (loc:flea-bottom + operational-substrate): permanent location vibe. `vibes:4` (episode + first-deployment): targets `episode` scope — episode-scoped vibes are by definition chapter-local; permanence AP1 test does not apply to episode-scope targets. The concern is specifically vibes:1 token `routing-without-contact` — this characterizes the b01c02 deployment *mode* and may become obsolete once the deployment architecture evolves. It is applied to `actor:taylor`, which is a persistent target. Token may be better placed on `episode` scope.

- **why:** If `routing-without-contact` persists as a permanent `actor:taylor` vibe token after b01c03+ where the architecture expands, the token will create stale bias in downstream operators who read it as Taylor's current deployment mode rather than the b01c02 first-deployment constraint.

- **routing:** showrunner. Verify whether `vibes:1 @5` token `routing-without-contact` should target `episode` scope (for b01c02 scoped permanence) rather than `actor:taylor` (book-wide permanence).

**@15 (7 facets):** `feel:2, loc-state:9, narrator:4, state:12, state:15, vibes:6, vibes:7`
- Scene-map: peak-bone (wren-attachment crystallization — protected pattern).
- All seven facets carry distinct jobs. No DEDUP concern (confirmed above). No additional finding.

---

## Class 12: RUBRIC-FIDELITY

### Dimension 1: Per-entry signature checks

**State-updates rubric, Reality axis:**
- state:11 @5: `actor:taylor-hebert-kl-122ac.capability-deployment-history: dormant-never-deployed-in-kl -> deployed-defensive-flea-bottom` — field is a justified extension (capability-deployment-history; documented in the rubric-carve-out section as a tracked-state aspect). Reality: the deployment is the scene's peak event; persistence past the beat is the b01c02 handoff-out state. POV actor-state requires narrator-interest co-citation: narrator:2 @5 fires ("routing is what the prohibition still permits her to call clean"). Co-citation satisfied. Pass.
- state:12 @15: `actor:taylor-hebert-kl-122ac.social-tether-wren: peripheral-permitted-attachment -> crystallized-observer-bond` — POV actor-state. Co-citation required: narrator:4 @15 fires ("Wren is looking at her the way you look at a thing you have decided about"). Satisfied. Pass.
- state:13 @26: `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-social-physics: observational-sweep-pattern -> categorical-structural` — POV actor-state. Scene-C peak-bone @25 is the nearest peak; @26 is the underline beat (peak-shadow). POV actor-state requires NI co-citation. The cite-index shows `narrator:5 @25` fires. The state:13 entry fires at @26, not @25. Narrator fires at @25; state fires at @26. The rubric's POV-actor-state NI co-citation requires the same `@<proto-line-id>`. State:13 fires at @26; narrator:5 fires at @25. No narrator entry fires at @26.

### Finding RF-001 (HARD fault)

- **id:** fault-002
- **type:** fault
- **what:** `state-updates.md` entry 13, `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-social-physics: observational-sweep-pattern -> categorical-structural`, anchored at @26 ("taylor-hebert-kl-122ac underlines the entry"). This is a POV actor-state entry (actor:taylor.*). Per rubric §Cross-facet contract (state-updates rubric §POV-character actor-state must have narrator-interest co-citation): "every `actor:<POV>.*` entry pairs with a narrator-interest entry on the same beat." The cite-index confirms: @26 carries only `state:7 @26` and `state:13 @26` with no narrator entry. `narrator:5` fires at @25, not @26. There is no narrator-interest entry at @26 in the locked graph.
- **why:** The knowledge-type reclassification (observational-sweep-pattern → categorical-structural) is the knowledge axis movement the worm-canon-pedant TASTE-FLAG from Phase 4/Phase 6 identified as load-bearing ("the jump-type must be preserved in interior-scene bones"). Without an NI co-citation at @26, the stitcher has no interior-registration basis for rendering the reclassification as load-bearing. The state-update fires but the NI that would make it render in the prose is missing. This is a cross-facet contract violation per the state-updates rubric.
- **criteria:** Either (a) the interest-narrator file must be extended with a new entry at @26 that registers the categorical-structural reclassification in Taylor's interior, OR (b) state:13 must be re-anchored to @25 (the pen-set / pressure-arrives peak where the recognition actually surfaces, per scene-map: "@25 — ledger gap surfaces before the held hand disciplines against it") with narrator:5 @25 as its co-citation spine. Option (b) is minimum change: the underline at @26 is the physical act; the categorical recognition fires at the ledger-gap moment @25. Moving state:13 to @25 allows narrator:5 to serve as the spine.
- **routing:** state-updates author (impersonator-taylor-hebert-kl-122ac slice); interest-narrator author if option (a) is chosen.

### Dimension 2: Per-facet file-level shape gate

**State-updates file-level shape:**

### Finding RF-002

- **id:** flag-008
- **type:** flag
- **what:** State-updates rubric episode-level shape: "Sparsity. Estimated band for s01e01: 8–18% of proto-lines (~6–14 entries on 77 beats)." The rubric's band is derived from a 77-bone chapter. For b01c02 (27 bones), proportionally: 8% = 2.2 entries; 18% = 4.9 entries. The file carries 15 entries = 55.6%. Even accepting that 6 of those are oc-prop field-extensions (4, 5, 6, 7, 8, 9 in the env/studio slice), the non-oc-prop entries still sum to 9 = 33.3%, above the adjusted ceiling. The rubric's "target diversity" requirement (three target classes: studio.*, prop:*.*, at least one actor:*) is met. The density is elevated relative to the proportional-adjusted band. The rubric's anti-pattern #9 (density-on-flat) warns against firing on every motion-verb; however, the scene-C oc-prop entries are genuine persistent state-changes, not motion-verb contamination. The elevated density is attributable to the scene-C accounting sequence (8 bones @22–@29) generating 6 oc-prop state-changes (lamp, ledger, pen operations) plus 3 actor-state entries (state:11, state:12, state:13). The question is whether all 6 oc-prop entries survive the Reality axis strip-test.

  State:4 @22 (oc-lamp.state: unlit → lit) — persistent; strip-test passes.
  State:5 @23 (oc-ledger.state: closed → open) — persistent.
  State:6 @25 (oc-ledger.current-entry: blank → struck) — persistent.
  State:7 @26 (oc-ledger.current-entry: struck → struck-categorical-underlined) — the underline is a discrete delta from the strike; the rubric-carve-out note justifies it as "a discrete delta from the strike." Whether this is genuinely persistent is the question: the ledger stays underlined through @29. Strip-test: without this entry, state:6 carries `struck` through @29. The difference between `struck` and `struck-categorical-underlined` is meaningful per the substance contract (categorical distinction marked). Marginally passes.
  State:8 @27 (oc-pen.state: in-hand → set-down) — persistent through @28-@29.
  State:9 @29 (oc-ledger.state: open → closed) — persistent.

  The elevated density is justified by the oc-prop-rich scene-C accounting sequence; none of the 6 oc-prop entries fail Reality. The absolute density figure (55.6%) is advisory, not blocking, given the short chapter's pro-rated band. Flagged as ADVISORY.

- **why:** If future chapters also contain dense object-interaction sequences, the oc-prop field-extension path could balloon state-updates density consistently. The rubric's density band needs a formal short-chapter exemption analogous to the sensory rubric's URI-FACETS-V3-SHORT-CHAPTER if oc-prop-rich chapters are expected.
- **routing:** state-updates rubric maintainer; showrunner to note for b01c03 authoring that oc-prop extensions should be rationed to genuine persistent-state changes and reviewed against the pro-rated density band.

### Dimension 3: Cross-facet co-citation symmetric checks

**Cite-index bi-directional check (back=Y presence for all cited entries):**

The cite-index records `exposition:1 @0 back=N`. The schema confirms: `back=N` indicates the exposition entry is not cited by any proto-line (it fires at @0, the preamble position, which precedes all numbered proto-lines). This is correct behavior for a prior-episode-bridge; it is not a co-citation failure. No finding.

**Memory co-citation with narrator:**
- mem:1 @8: cite-index shows `co=[loc-state:6, narrator:3, vibes:8]`. narrator:3 is the co-citation spine. Consistent with rubric (NI spine required; narrative:3 fires at @8). Pass.
- mem:2 @25: cite-index shows `co=[narrator:5, state:6, vibes:11]`. narrator:5 is the co-citation spine. The peak-bone exception has been granted under R2.2. Consistent. Pass.

**Feeling co-citation with narrator (POV-non-redundancy):**
- feel:1 @28 (taylor): cite-index shows `co=[narrator:6]`. narrator:6 @28 fires ("the not-closing is the only line tonight she is sure of"). The R2.3 Taylor shard documents Q1 (POV-non-redundancy): NI registers cognition ("the only line she is sure of"); feeling shows the hand doing it. Distinct jobs. Pass.
- feel:2 @15 (wren): Wren is non-POV; POV-non-redundancy Q1 clause is modified ("Q1 passes because feeling is the sole facet carrying wren's interior at all"). cite-index shows `co=[loc-state:9, narrator:4, state:12, state:15, vibes:6, vibes:7]`. narrator:4 fires at @15 from Taylor's POV (Taylor reading Wren); feel:2 carries Wren's interior from inside. Distinct POV layers. Pass.

**Dialogue citation-completeness (both card-signatures AND facet-licenses populated post-R2):**

Per the rubric's citation-completeness requirement (URI-FACETS-CYCLE-1): every chosen-mark entry must have BOTH `card-signatures:` AND `facet-licenses:` populated with concrete citations post-R2.

- wren:1 @19 sidecar: `card-signatures:` — extensively cited (§smallfolk Cadence, §smallfolk Syntax, §grrm-mannerisms, §persona Voice tells, §cond-westerosi-witness-vocabulary, §persona Dialogue samples). `facet-licenses:` — R2.6 shard resolved DEFERRED-TO-R2 to `vibes:13 @19` (cite-index confirms co-location). The sidecar's R1 `facet-licenses: [DEFERRED-TO-R2 — feeling/NI at @19...]` was resolved at R2 to `vibes:13 @19` per R2.6 shard. **However**, the sidecar file (`wren-stitch-maker-flea-bottom-ward.drafts.md`) still shows the R1 placeholder `facet-licenses: [DEFERRED-TO-R2 — feeling/NI at @19 expected...]` in the Draft B block. The R2.6 shard documents the resolution but the sidecar itself was not updated with the concrete resolved citation. Per the rubric: "A sidecar that documents the facet-license axis in R1-blind placeholder form and is not resolved at R2 with a concrete `<facet>:<id>` citation is a SIGNAL finding per entry." The shard resolved it; the sidecar did not reflect the resolution. SIGNAL.

- taylor:1 @20 and taylor:2 @20 sidecars: similarly carry `facet-licenses: [DEFERRED-TO-R2 — feeling-taylor / sensory-taylor at @20; ...]` in the Draft A blocks. The R2.6 Taylor shard resolves these to `vibes:14 @20`. The sidecar Draft A blocks still carry the DEFERRED placeholder.

### Finding RF-003 (HARD fault)

Reclassifying: the rubric states "A sidecar that documents the facet-license axis in R1-blind placeholder form and is not resolved at R2 with a concrete `<facet>:<id>` citation is a SIGNAL finding per entry." SIGNAL (not HARD) per the rubric's own classification — the shard has resolved it; the sidecar is the non-updated artifact, not the deployed graph. The cite-index correctly shows co-location. The rubric escalates to HARD only on cycle-2 when a block-assertion is made without per-entry resolution. This is cycle-1 (first audit). Reclassified as SIGNAL.

- **id:** flag-009
- **type:** flag
- **what:** Three dialogue drafts sidecar entries carry R1-blind placeholder `facet-licenses: [DEFERRED-TO-R2...]` form that was not updated in the sidecar at R2 write-back. Affected entries: wren:1 @19 (Draft B chosen block in wren sidecar); taylor:1 @20 (Draft A chosen block in taylor sidecar); taylor:2 @20 (Draft A chosen block in taylor sidecar). The R2.6 decision shards document resolution: wren:1 → `vibes:13 @19`; taylor:1 + taylor:2 → `vibes:14 @20`. The cite-index confirms co-location (vibes:13 co=[wren-stitch-maker-flea-bottom-ward:1]; vibes:14 co=[taylor-hebert-kl-122ac:1, taylor-hebert-kl-122ac:2]).
- **why:** The sidecar is the per-entry record of authoring decisions. If the sidecar carries stale placeholder form, future audits reading the sidecar alone (without the R2 shard) will re-flag the entries as unresolved, creating false positives. The sidecar is also the citation-completeness record the rubric enumerates at audit.
- **routing:** dialogue-writer forks (taylor-hebert-kl-122ac and wren-stitch-maker-flea-bottom-ward); update chosen-mark `facet-licenses:` fields to the concrete R2-resolved citations.

### Dimension 4: Card-resolution checks

**monument-cost-borne-by-the-unconsenting** (mem:1 target-reference): The R2.2 shard flags this as a SIGNAL under "monument-card resolution test" — "could not enumerate the warehouse to confirm a `monument-*` card exists for either slug." The auditor confirms: a warehouse scan does not surface `monument-cost-borne-by-the-unconsenting.md` or equivalent. Per rubric: SIGNAL if the gloss is structurally clear and a margit referral is the conservative path. The slug is mechanism-descriptive and fence-clean. Carrying forward from R2.2 shard.

**monument-conquest-charter-language** (mem:2 target-reference): Same status per R2.2 shard — no warehouse card confirmed. SIGNAL.

Both flags are carries from the R2.2 shard decision and are not new findings. Noting for completeness; not re-filing as independent audit findings since the shard already documents them.

---

## Audit Summary

### HARD findings (2)

| id | class | what |
|----|-------|------|
| fault-001 | CONSTRAINT | Glossed-terms register likely carries stale water-carrier + near-witness entries and wrong pressed-labor-sweep anchor; R2.5 deletion instructions not confirmed executed |
| fault-002 | RUBRIC-FIDELITY | state:13 @26 is a POV actor-state entry without NI co-citation at the same proto-line anchor; rubric requires NI co-citation on the same @N for all actor:taylor.* entries |

### SIGNAL findings (8)

| id | class | what |
|----|-------|------|
| flag-001 | STRUCTURAL | state-updates.md multi-block frontmatter (consolidated + per-slice) not covered by schema; potential parser ambiguity at stitch |
| flag-002 | METADATA-INCONSISTENCY | R2.3 Taylor shard refers to feel:2 @28 internally; the deployed feeling.md assigns id 1 to Taylor's @28 entry; shard internal citations are stale |
| flag-004 | CONSTRAINT | "Flea Bottom" embedded in exposition:4 @4 gloss-text may be unoriented for a cold-join reader at b01c02; cross-episode glossed-terms register should confirm coverage |
| flag-005 | AP-SCAN | Cost/count vocabulary cluster (narrator:3, :4, :5) appearing in 3 of 6 NI entries; advisory carry-forward to b01c03 authoring brief to vary registration vocabulary |
| flag-006 | TASTE-FLAG | vibes:14 @20 keyword `earning-collapse` is ambiguous for downstream operators; token bundle clarifies but keyword may bias stitch toward deflationary register instead of crystallization |
| flag-007 | PILE-UP-REVIEW | vibes:1 @5 token `routing-without-contact` applied to `actor:taylor` (permanent target); may become stale as deployment architecture evolves past b01c02 routing mode |
| flag-008 | RUBRIC-FIDELITY | state-updates density 55.6% elevated vs. proportional-adjusted band for 27-bone chapter; oc-prop extensions justified but rubric lacks formal short-chapter density exemption |
| flag-009 | RUBRIC-FIDELITY | Three dialogue sidecar chosen-mark `facet-licenses:` fields carry R1 DEFERRED placeholder form not updated to resolved R2 citations |

---

## Routing

| finding | type | route-to |
|---------|------|----------|
| fault-001 (CN-001) | HARD | exposition-author; glossed-terms.md register maintainer |
| fault-002 (RF-001) | HARD | state-updates author (impersonator-taylor-hebert-kl-122ac slice); interest-narrator author if NI-add path chosen |
| flag-001 (S-001) | SIGNAL | studio (state-updates author); stitcher/build_cite_index maintainer |
| flag-002 (M-001) | SIGNAL | feeling-author (impersonator-taylor-hebert-kl-122ac slice); R2 decision-log maintainer |
| flag-004 (CN-002) | SIGNAL | exposition-author |
| flag-005 (AP-001) | SIGNAL | interest-narrator author (carry to b01c03 brief) |
| flag-006 (TF-001) | SIGNAL | showrunner (vibes author) |
| flag-007 (PU-001) | SIGNAL | showrunner (vibes author) |
| flag-008 (RF-002) | SIGNAL | state-updates rubric maintainer; showrunner |
| flag-009 (RF-003) | SIGNAL | dialogue-writer forks (taylor-hebert-kl-122ac; wren-stitch-maker-flea-bottom-ward) |
