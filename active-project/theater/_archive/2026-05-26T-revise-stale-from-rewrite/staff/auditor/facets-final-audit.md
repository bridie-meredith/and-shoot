audit: facets-final-r1
episode: b01c02
date: 2026-05-25
mode: flag-only
status: FINDINGS-PRESENT
totals: 9 findings — 2 HARD, 5 SIGNAL, 2 advisory (pile-up review)

---

## STRUCTURAL findings (0)

None. All facet files carry valid frontmatter. ID monotonicity holds in all files. Anchor IDs in all `@<id>` fields resolve to proto-line IDs present in `active-project/theater/proto-lines/b01-c02.md` (aggregate_range 1-29). Bidirectional citation: all `[<facet>:<id>]` tokens on canonical proto-lines resolve to existing facet entries. Slice consolidation (feeling, state-updates) is present with `# source:` markers and monotonic renumbering. Scene-map coverage field reads `29/29 bones in exactly one scene` — no gaps, no overlaps reported. Proto-body integrity: auditor cannot verify byte-identity of `_inflight/` copies (they are not present in the target scope of this audit dispatch), but the canonical proto-lines file matches the bones file SVO bodies on spot-check of all 29 bones.

Structural finding count: **0**.

---

## FREQUENCY-BAND findings (2 SIGNAL)

**Sensory:** 2 entries / 29 proto-lines = 6.9%. Rubric band 3-6%. Above ceiling by 0.9 percentage points. Modality coverage: 2 modalities (sound, smell) — meets the ≥2 floor.

- flag-001
  - id: flag-001
  - type: flag
  - what: sensory-b01-c02.md — 2 entries / 29 proto-lines = 6.9%; rubric ceiling 6%
  - why: technically above-band; on a 29-bone chapter the ceiling is structurally tight (1 entry = 3.4%, 2 entries = 6.9%); fixer action would require deleting one of the two entries, which would drop modality coverage to 1 and breach the ≥2-modality floor. The floor and ceiling are arithmetically incompatible at this proto-line count — the rubric's sparsity assumptions were calibrated for 100+ proto-line episodes. Signal-only: the per-episode caps and the modality floor together give the correct bound; the percentage band is advisory here per the b01c01 R2 precedent on bones-only chapters.
  - why (downstream): no downstream consequence if stitcher receives both entries; only risk is auditor-cycle inconsistency if the rule is applied mechanically on future chapters of similar length.

**NI (narrator-interest):** 9 entries / 29 proto-lines = 31%. Rubric band 15-25%. Above ceiling by 6 percentage points.

- flag-002
  - id: flag-002
  - type: flag
  - what: interest-narrator-b01-c02.md — 9 entries / 29 proto-lines = 31%; rubric ceiling 25%
  - why: R2 decision shard defends this as structurally necessary — 7 of 9 entries are mandatory POV co-citations required by the state-updates rubric's cross-facet contract (POV actor-state entries require NI co-citation at the same beat), and the remaining 2 serve file-shape open/close functions. The R2 shard's pattern-scan notes the inflated-percentage-at-bones-only-chapters precedent (b01c01 NI similarly ran hot). Signal-only: absolute count (9 NI across 3 scenes) reads as spotlight not saturation; the percentage-band ceiling was calibrated for 100+ proto-line episodes.
  - why (downstream): no downstream blocking consequence; advisory for rubric calibration tracking.

**Memory:** 2 entries / 29 proto-lines = 6.9%. Rubric band 5-12%. Within band. PASS.

**Feeling:** 1 entry / 29 proto-lines = 3.4%. Rubric band 2-5%. Within band. PASS.

**Metaphor:** 0 entries / 29 proto-lines = 0%. Rubric band 0-3%. Within band. PASS.

**Exposition:** 5 entries / 29 proto-lines = 17.2%. Rubric band 1-5%. Above band. However, per the b01c01 R2 precedent and the R2 exposition shard's explicit seam-1 reconciliation, the per-episode caps are the binding constraint on bones-only chapters (1-5% was calibrated for 100+ proto-lines). All per-episode caps satisfied: 1 prior-episode-bridge (cap = 1), 1 episode-open-context (cap ≤ 3), 1 first-mention (cap ≤ 12), 2 scene-orient (cap = 1 per scene, 2 scenes fired). Signal per the established precedent.

- flag-003
  - id: flag-003
  - type: flag
  - what: exposition-b01-c02.md — 5 entries / 29 proto-lines = 17.2%; rubric band 1-5%
  - why: above-band is a structural artifact of bones-only chapter length, not an authoring error; all per-episode caps satisfied; b01c01 precedent established this pattern. Signal only. Rubric calibration note: the 1-5% band should carry a bones-only-chapter footnote.
  - why (downstream): no blocking consequence; advisory for rubric calibration.

**Vibes:** 17 entries / 29 proto-lines = 58.6%. Rubric says sparsity is liberal — no upper ceiling for vibes since they are not rendered as prose. PASS (rubric explicitly permits dense vibes files).

**State-updates:** 5 entries / 29 proto-lines = 17.2%. Rubric nominal band 8-18% (per the carve-out preamble's density floor argument). 1 env entry + 4 actor entries. The env slice carries a defended carve-out (1 entry / 29 = 3.4%, below the floor, with documented justification for sparse-fire). Signal per carve-out preamble.

- flag-004
  - id: flag-004
  - type: flag
  - what: state-updates.md env slice — 1 entry / 29 proto-lines = 3.4%; below the rubric 8-18% density band
  - why: carve-out preamble is present and detailed (all three axes tested per entry; fire-defenses for all silent bones documented). The chapter has no prop cards and no location transition, leaving only the time_of_day flip at @20 as a defensible field-flip. Preamble defense meets the rubric's own SEAM notation standard. Signal, not fault. Flagged for the SEAM-001 cross-chapter state-chain risk noted in the preamble (b01c01 authored zero env state-updates, leaving the @20 `<old>` value "dawn" derivable only from handoff_out baseline, not from a prior state-update entry).

---

## METADATA-INCONSISTENCY findings (1 SIGNAL)

- flag-005
  - id: flag-005
  - type: flag
  - what: `active-project/theater/facets/.r2-decisions.md` — NI R2 decision shard frontmatter field `cite_index_hash: uncomputed-no-shell-access-in-impersonator-harness`
  - why: the R2 stale-shard pre-check at Phase 3 requires every shard's `cite_index_hash` to carry a real SHA for cross-session staleness detection (URI-FACETS-R2-STALE-SHARD, A6). The NI shard explicitly documents it could not compute the hash. The memory exposition shard carries `cite_index_hash: cite-index-2026-05-25-b01c02-45entries` (a descriptive string, not a SHA). The feeling R2 shard carries `cite_index_hash: cite-index@2026-05-25/45entries/14-of-29-decorated` (also descriptive, not SHA). Only the exposition R2 shard carries a proper SHA-form hash (`0a24cee164dd87eec18731b08a1e8e3fbee3642a414430b4ad9e569cd28610ab`). The schema requires SHA-form; descriptive strings cannot be compared for staleness detection.
  - why (downstream): the staleness check is process-hygiene, not stitcher-blocking. If a future session re-runs R2 for b01c02, the Phase 3 pre-check cannot determine whether the NI/memory/feeling shards are stale. Signal only; no current downstream consequence because the chapter is single-session authored.

---

## CURVE-SHAPE verdict

- Episode-level: **SHAPE-OK**.
  - Chapter `dramatic_shape: rising` (per b01c02 substance contract; confirmed from series trajectory and chapter substance allocation).
  - Scene-map rhythm-shapes: scene-A `flat-low`, scene-B `peak-and-release`, scene-C `peak-and-release`.
  - The sequence flat-low → peak-and-release → peak-and-release is coherent with `rising`: the chapter opens in mechanism-establishment register (flat-low), gains its first peak at @17 (Wren-as-coverage-map node), and closes with its second peak at @24 (recognition-and-suppression). Each subsequent scene's peak is narratively higher-stakes than the prior scene's pressure level. No resolving-only or release-only scenes present.
  - The "rising" dramatic_shape enum does not require a single climactic peak; it permits ascending peak-and-release patterns where each peak raises the floor for the next. This chapter fits that pattern. SHAPE-OK.
- Per-scene:
  - Scene-A (flat-low, @1-@9): no peak-bones present — consistent with flat-low.
  - Scene-B (peak-and-release, @10-@19): peak @17, shadows @16/@18 — consistent with peak-and-release.
  - Scene-C (peak-and-release, @20-@29): peak @24, shadows @23/@25 — consistent with peak-and-release.
- Adjacency: no tensometer to scan. Pressure-signal substitute (scene-map peak-bones): peaks at @17 and @24 are 7 bones apart; no 1→3 jump anomaly detectable in the available signal.
- Flatlining: scene-A is 9 bones at flat-low; well within 30-bone contiguous threshold. No flatlining concern.

---

## CONTRADICTION findings (0)

Scanned all state-update entries for field-level contradictions. State-updates entries:
- state:1 @20: `studio.time_of_day: dawn -> end-of-day`
- state:2 @6: `actor:taylor-hebert-kl-122ac.deployment-state: ambient-subsistence-reading -> systematic-precinct-coverage-deliberate`
- state:3 @17: `actor:taylor-hebert-kl-122ac.internal-accounting.wren-status: unknown -> filed-as-ward-junction-contact-unnamed`
- state:4 @24: `actor:taylor-hebert-kl-122ac.internal-accounting.coverage-map-recognition-event: not-yet-occurred -> occurred`
- state:5 @25: `actor:taylor-hebert-kl-122ac.internal-accounting.coverage-map-recognition-status: unsuppressed -> suppressed-under-harm-reduction`

All five fields are distinct. No two entries set incompatible state on the same field at the same or different anchors. Chain order: @6 → @17 → @24 → @25 → (env @20) is chronologically consistent with the scene-map's time sequence. No contradiction found.

Contradiction finding count: **0**.

---

## DEDUP findings (1 HARD)

**HARD:** Cross-facet content duplication between feeling:1 and the proto-line body at @17.

- fault-001
  - id: fault-001
  - type: fault
  - what: `feeling.md` entry 1 @17 — "her shoulders hold where they were | expressed: no"; proto-line @17 body is "the insects file the ward-junction contact"
  - why: the R2 feeling judge evaluated feel:2 @24 and correctly deleted it on the grounds that `proto-line @24 "taylor-hebert-kl-122ac stalls the count"` carries the body-action directly (C1/C2 anchor logic). The same test applies to feel:1 @17: proto-line @17's subject is "the insects" (not Taylor), and the action is "file the ward-junction contact." The somatic tell is Taylor's postural hold DURING a beat where the bone's subject is the swarm, not Taylor. This is not a C1/C2 failure (the proto-line does not carry the somatic tell; the subject is the insects, not Taylor's body). R2 judge correctly concluded Q1 passes: the audience cannot read the postural hold from the proto-line. **However:** narrator:4 @17 reads "the ward-junction contact filed itself in the fold she kept for the entries that did not enter the ledger, and the filing took less hesitation than it had the first time she did it." The phrase "less hesitation than it had the first time" is a first-person registration of the postural/interiority response to the filing act. This NI entry covers the cognitive-postural register ("less hesitation") that the feeling entry covers somatically ("shoulders hold where they were"). The two entries are not exact-same content — NI covers the cognitive-hesitation-comparison; feeling covers the postural stillness during the filing. These are adjacent registers (hesitation-as-cognitive vs stillness-as-somatic), not identical registers. **Ruling: SIGNAL, not HARD.** Reclassified. The entries are sufficiently distinct that deletion of one yields information loss; both are defensible under the DEDUP rubric's "lens facet yields to dialogue when speaker uses the same phrasing" principle (reversed here: both are lens facets covering overlapping but not identical registers).

Reclassification note: upon examining the DEDUP criteria more closely, this is more properly a TASTE-FLAG than a DEDUP HARD (the entries cover adjacent registers, not the same content). Reclassifying to TASTE-FLAG.

Cross-facet: narrator-interest vs feeling at same anchors. @17: narrator:4 covers hesitation-as-cognitive; feel:1 covers stillness-as-somatic. Different register channels; no DEDUP. @24: feel:2 was deleted by R2 judge; no remaining feeling entry at @24. No DEDUP found.

Cross-facet: vibes vs memory at @17 / @18. Vibes:6 carries "wren-as-the-gap-the-map-has-a-shape-around / the-account-open-with-no-entry"; mem:2 @18 carries the shape-of-the-absence as override-architecture-residue. These cover distinct semantic layers (vibe-cloud operator-bias token bundle vs monument-callback with specific Earth-Bet displacement mechanism). Not DEDUP.

Within-facet: no within-facet same-anchor duplicates found. Vibes has multiple entries @6 and @17 and @24, but each carries a distinct keyword/target combination as the schema permits.

**Revised DEDUP finding count: 0 HARD findings. See TASTE-FLAG below.**

---

## SUPERFLUOUS findings (0)

Lonely entries per cite-index (no co-location, no inbound license):
- `loc-state:5 @26` — bone @26: "the accounting closes the fever-cluster entry." Time: end-of-day. Rhythm zone: scene-C fusion-eligible-run (@26-@29). Loc-state:5 carries `continuity-from loc-state:4:` sensory note. Rubric: continuity-carry entries on flat-low/resolving/release-only zones are never superfluous (per audit class SUPERFLUOUS convention). Scene-C rhythm-shape is peak-and-release, not resolving. However: the bone sits in the `fusion-eligible-runs: @26-@29` range, which the scene-map marks as the scene's post-peak dissolve zone. The continuity-carry entry at @26 is the post-peak carry establishing that the drain-angle sensory state persists through the ledger-close sequence. Three-axis test: (necessity) without loc-state:5 the stitcher has no loc-state signal from @20 through @29, leaving the ledger-close sequence without environmental grounding; (interestingness) the drain-water trickle adds the only non-cognitive sensory texture to the chapter's close; (frugality) single entry for nine bones — extremely frugal. Passes necessity/interestingness/frugality. Not superfluous.

- `narrator:3 @15`, `narrator:8 @16`, `narrator:9 @29` — all three are NI R2 ADDs with full justification in the decision shard. Lonely in the cite-index (no co-citations required by rubric for these bones). Under the SUPERFLUOUS convention, entries in flat-low zones are never superfluous; @15 is in scene-B rising zone, @16 is a peak-shadow, @29 is the chapter-close exhale. R2 shard's per-entry justifications are specific (narrator:8's at-rest read on the cover/cataloguing doubled-action; narrator:9's cost-tracking on the suppression-overhead body-residue). Three-axis test for each: all pass. Not superfluous.

- `exposition:1 @0`, `exposition:2 @0` — preamble entries at the synthetic `@0` anchor. The cite-index marks them as lonely (no co-citations from lens facets, which is expected — the preamble renders before the body). SUPERFLUOUS evaluation: @0 entries are episode-open-* scope; they are structurally isolated from lens facet co-citation by design. Necessity: all three personas need the 3-week bridge and the coverage-map vocabulary (R2 exposition shard validates per-entry). Not superfluous.

- `exposition:3 @9` — first-mention-place at the ward-junction first-mention bone. Lonely in the cite-index (bone @9 has no lens facet co-citations; only the exposition entry). The bone reads "the foot-traffic knots the ward-junction" — ward-junction is first introduced here. Necessity: the term is used repeatedly through @15-@29 in both the bones file and the NI facet; without this gloss the term enters reader consciousness undefined. Not superfluous.

- `exposition:4 @10` — scene-open-orient-B. Lonely (no lens facet co-cites at @10). Scene-bridge entries render before the first bone of the new scene; no lens facet fires at the scene-open anchor is exactly the firing condition per the fire-rule (condition b/c validate that lens is not covering the temporal disjuncture). Not superfluous.

Superfluous finding count: **0**.

---

## CONSTRAINT findings (2 — 1 HARD, 1 SIGNAL)

**Earth-Bet hard-fence scan:**

Scanned all text fields across all nine facet files for Earth-Bet proper nouns (Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea, and slug components of same).

- Memory facet: `mem:1` description text uses "older country's charters," "province," "stroke" — no Earth-Bet proper nouns. Target-ref is `monument-conquest-charter-language` — no Earth-Bet slug components. Clean.
- Memory facet: `mem:2` description text uses "architecture," "override," "method" — no Earth-Bet proper nouns. Target-ref is `cond-override-architecture-residue-122ac` — no Earth-Bet slug components. Clean.
- Memory authoring notes (lines 39-44 in memory-b01-c02.md): the fence-sweep documentation lists "locker, Bakuda, Leviathan, Khepri, Annette, Skitter, Weaver, Gold Morning, PRT, Endbringer, S9, Coil, Dinah, Brockton" and Dance-specifics — these are the scan targets referenced in the documentation, not violations. The author's hard-fence sweep is documented and clean.
- NI, sensory, feeling, vibes, state-updates, loc-state, exposition, metaphor: scanned all free-text fields. No Earth-Bet proper nouns found.
- Vibes: entity-target slugs include `actor:wren-stitch-maker-flea-bottom-ward`, `actor:oswyn-mudway-flea-bottom-elder`, `actor:taylor-hebert-kl-122ac`, `loc:oc-stitch-house-lane` — no Earth-Bet slug components.

Earth-Bet hard-fence: **CLEAN** across all facets.

**Memory without NI-spine (CONSTRAINT cross-facet contract):**

- `mem:1 @7`: cite-index shows `mem:1 @7 back=Y co=[narrator:2]`. NI spine present. Passes.
- `mem:2 @18`: cite-index shows `mem:2 @18 back=Y co=[narrator:5]`. NI spine present. Passes.

**Metaphor `licensed-by:` anchor resolution:**

Metaphor facet: zero entries. All `licensed-by:` checks N/A. Passes.

**Feeling duplicating POV NI (CONSTRAINT cross-facet):**

`feel:1 @17` somatic tell "her shoulders hold where they were | expressed: no" — NI @17 reads "the ward-junction contact filed itself in the fold she kept for the entries that did not enter the ledger, and the filing took less hesitation than it had the first time she did it." NI covers cognitive-hesitation-comparison; feeling covers postural-stillness. Adjacent registers but not identical content. Not a CONSTRAINT duplication (the rubric requires NI to yield when the speaker uses the same phrasing — these use different phrasing and different register channels). Passes.

**Vibes `licensed-by:` resolution:**

All vibes entries carry `licensed-by:` fields. Cross-checked resolvability:
- `state-update:1` through `state-update:5` — all resolve to the state-updates.md entries (note: vibes uses state-update:1/2/3/4 referencing the state-updates facet; the state-updates file has entries labeled 1-5 in the consolidated file, so state-update:4 = state:4 @24 and state-update:5 would be @25). The vibes file references `state-update:4` in vibes:13 and 15 — but checks the state-updates file: there are only 5 entries (1=env@20, 2=taylor@6, 3=taylor@17, 4=taylor@24, 5=taylor@25). Vibes references `state-update:1, state-update:2, state-update:3, state-update:4`. These resolve: state-update:1=@20 env entry, 2=@6 actor entry, 3=@17 actor entry, 4=@24 actor entry. The `licensed-by: state-update:1` on vibes:1-5 (@6) refers to state-update ID 1 in the state-updates file — which is state:1 @20 (the time_of_day flip). However, vibes:1-5 anchor at @6, and the referenced state-update:1 is at @20 (later in the chapter). This is a forward-citation of `licensed-by:` — a vibes entry anchoring at @6 citing a state-update that fires at @20.

- fault-002
  - id: fault-002
  - type: fault
  - what: vibes-b01-c02.md entries 1, 2, 3, 4, 5 (@6) — all carry `licensed-by: state-update:1` among their sources; state-update:1 in the consolidated state-updates.md is `@20 studio.time_of_day: dawn -> end-of-day`; this fires 14 bones AFTER the vibes entries' anchor (@6)
  - why: the vibes schema forbids forward-citing `licensed-by:` sources (`active-project/theater/facets/` — per `schemas/facet.schema.md` § vibes-updates: "vibes are permanent stickers — a vibe added in s01e01 persists to s01e02+ unless explicitly retired"). The concern is not the vibe's persistence but the `licensed-by:` field: the field must point to sources that existed at or before the licensing anchor, not to a later-in-chapter state-update. A `licensed-by:` reference citing a state-update that fires later than the vibes entry's anchor is a forward-citation — the vibes update is claimed to be licensed by a field-flip that had not yet occurred at the anchor point. The CONSTRAINT class enumerates "vibes with unresolvable or forward-citing `licensed-by:`" as a violation.
  - why (downstream): if the stitcher uses `licensed-by:` provenance for sequencing or validation, forward-cited sources produce incoherent ordering. The more material risk is that the `state-update:1` reference is almost certainly intended to refer to `state-update:2` (the `actor:taylor-hebert-kl-122ac.deployment-state` flip at @6, which IS the licensing anchor for the systematic-coverage-architecture vibes). The state-update ID confusion may propagate to fixer's correction scope.
  - criteria: vibes:1-5 at @6 must cite only sources that resolve to state-update entries at anchors ≤ @6, or to `proto:<id>` / `canon:<gloss>` / `world-build:<gloss>` sources. If the intent is to license these vibes from the deployment-state flip at @6, the correct citation is `state-update:2` (actor:taylor-hebert-kl-122ac.deployment-state @6), not `state-update:1` (@20 time_of_day).

**Exposition scene-orient fire-rule (CONSTRAINT):**

Exposition @10 (scene-open-orient-B) and @20 (scene-open-orient-C): R2 judge ran full fire-rule validation against the locked graph. Both entries satisfy:
- (a) time-skip blank confirmed via scene-map time-band transitions.
- (b) loc-state at scene-open anchor: loc-state:3 fires at @11 (not @10), and its prose-surface content is sensory/place, not temporal. For @20: loc-state:4 fires AT @20 but carries place/sensory content, not a temporal-disjuncture marker. The R2 shard's Seam-5 analysis correctly identifies that loc-state's `time-band` is metadata that informs renderer placement but does not surface as a temporal bridge to the reader. The fire-rule clause (b) requires `loc-state SILENT AT anchor` — for @10, loc-state is indeed silent at @10 itself (loc-state:3 is at @11). For @20, loc-state:4 IS at @20. The question is whether loc-state:4 at @20 covers the temporal disjuncture.

  Per the exposition CONSTRAINT rule: "loc-state at scene-open anchor (loc-state at-establishment carries the time/place; if it fires, the scene-orient is wallpaper)." Loc-state:4 at @20 carries "angle-wall cobblestone underfoot at the pinch-point: the narrowing marks the lane's south terminus; the feed has no cover here" — this is a place marker, not a time marker. The clause (b) prohibition targets loc-state that "carries the time/place" orientation that makes the scene-bridge redundant. When loc-state carries PLACE but not TIME, and the scene-bridge's load is the temporal disjuncture, the scene-bridge is not wallpaper. The R2 exposition judge's Seam-5 analysis surfaces this as a valid structural nuance.

  However: the strict reading of condition (b) is "loc-state does NOT fire at the scene-open anchor" — loc-state:4 does fire AT @20. The R2 judge's interpretation (fires but on place not time; therefore not covering the disjuncture the bridge carries) is defensible but pushes the condition (b) boundary. This is a borderline call.

- flag-006
  - id: flag-006
  - type: flag
  - what: exposition-b01-c02.md entry 5 (@20 scene-open-orient-C) — loc-state:4 fires AT @20 per the cite-index; condition (b) of the scene-orient fire-rule requires loc-state to be silent at the scene-open anchor; loc-state:4 fires at exactly @20
  - why: the strict reading of condition (b) could classify this as a fire-rule violation (scene-bridge fires when loc-state is present at the anchor). The R2 judge's defense (loc-state carries place, scene-bridge carries time; distinct loads; not wallpaper) is substantively sound but technically reads past the "does NOT fire at the scene-open anchor" language. If this is classified as a HARD CONSTRAINT violation, exposition:5 would be deleted, removing the end-of-day temporal bridge at the scene-C opening. The downstream stitcher consequence: without exposition:5, the @20 bone "taylor-hebert-kl-122ac takes the drain angle" reads as continuous with scene-B, losing the end-of-day recognition-hinge framing.
  - why (downstream): deletion of exposition:5 would weaken the chapter's scene-C opening and lose the temporal bridge at the recognition-and-suppression hinge. Signal, not fault — the R2 judge's defense is substantively correct even if technically pushing the fire-rule's strict language. Recommend rubric clarification: "loc-state silent at the scene-open anchor ON THE TEMPORAL DISJUNCTURE DIMENSION" rather than "loc-state does not fire at the scene-open anchor."

**Exposition source-traceability:**

Spot-checked claims in each exposition entry against listed sources:
- exposition:1 (prior-episode-bridge): sources include `chapters[b01c02].handoff_in.open_threads`, `chapters[b01c01].handoff_out.character_state`, `cond-override-architecture-residue-122ac`, `cond-taylor-pov-behavior`, `cond-kl-witch-label-formation-122ac`, scene chunks b01c01s03 and b01c02s01. Claims: "three weeks," "the count," "the rule," "reading was not directing," "the line." All trace to listed sources (handoff_in/handoff_out carry the 3-week skip; the prohibition restated from b01c01 substance; scene chunks ground the listening-extension decision). Passes source-traceability.
- exposition:2 (episode-open-context): sources include chapter b01c02 chunk, scene chunks, cond-taylor-pov-behavior, cond-override-architecture-residue-122ac. Claims: "flies and beetles," "heat clusters," "foot-traffic," "count of bodies," "coverage map" / "accounting" / "ledger," "harm-reduction." All trace to listed sources (chapter b01c02 chunk names these vocabulary terms; condition cards carry the clinical-register and harm-reduction framing). Passes.
- exposition:3 (ward-junction first-mention): sources include cond-kl-geography-122ac, cond-kl-social-physics-122ac, loc oc-stitch-house-lane. Claim: "a corner in the Hook where three or four alleys gave onto one another under a single precinct-ward's reach." This traces to cond-kl-geography-122ac § the-hook and the loc card's geographic description. Passes.
- exposition:4, exposition:5 (scene-bridges): sources include scene-map and scene chunk references. Claims are brief temporal markers ("Days of it, and the pattern came." / "End of day. I ran the map."). These trace directly to scene-map time-bands and scene chunk framings. Passes.

**Exposition first-mention-character coverage:**

Walk of all 29 proto-lines for named individuals or characters introduced in narrator-prose (not dialogue — chapter has zero dialogue-anchor bones):
- The only recurring individual in the bones file is Wren, referred to throughout as "the ward-junction body" / "ward-junction contact" — this is deliberate not-knowing per the chapter contract (Wren-unnamed, function-labeled). The chapter discipline is that Taylor does not know who the woman is; expositing her as a named character would defeat the contract. The R2 exposition judge explicitly defends against a first-mention-character gloss for Wren (DROP candidate-c in the cull pass). No other named individuals appear in bones or narrator prose (Taylor is the narrator/POV; Oswyn appears only in vibes:14 as an off-anchor entry, not in the bones themselves). Passes.

**Dialogue-coverage sanity check (URI-DIALOGUE-COVERAGE-GATE — upstream-leak verification):**

Chapter b01c02 has zero speech-bone SVOs (confirmed by exposition-b01-c02.md's dialogue-adjacent fence audit: "SPEECH-BONE SET = ∅"). Zero dialogue-anchor bones; zero expected speaker files. The upstream-leak check is structurally inoperative. Passes trivially.

**Scene-map coverage (URI-SCENE-WINDOW):**

Scene-map reports `coverage: 29/29 bones in exactly one scene`. Ranges: scene-A @1-@9 (9 bones), scene-B @10-@19 (10 bones), scene-C @20-@29 (10 bones). 9+10+10=29. Total-bones declared: 29. Total-scenes declared: 3. No gaps, no overlaps, no dangling anchors, no duplicate scene-labels. Passes.

**Scene-map per-scene caps:**

- Sensory ≤3 per scene: sensory:1 @4 (scene-A), sensory:2 @11 (scene-B). 1 per scene for the scenes that have fires. Scene-C: 0. Passes.
- Feeling ≤1 per character per scene: feel:1 @17 (scene-B only). 1 feeling entry total across 3 scenes. Passes.
- Metaphor ≤1 cross-character per scene: 0 metaphor entries. Passes.
- Exposition scene-open-orient ≤1 per scene: exposition:4 @10 (scene-B), exposition:5 @20 (scene-C). Scene-A has the chapter-open refused (correctly). 1 per scene that fires. Passes.

**Loc-state transition-run continuity-license (URI-SCENE-RHYTHM):**

`loc-state:5 @26` carries `continuity-from loc-state:4:`. Validation:
- (a) Anchor @26 is inside scene-C `fusion-eligible-runs: @26-@29` — PASSES.
- (b) Scene-C rhythm-shape is `peak-and-release`. The continuity-carry license requires `flat-low / resolving / release-only`. `peak-and-release` is NOT on the permitted list.

- fault-003
  - id: fault-003
  - type: fault
  - what: location-state-b01-c02.md entry 5 (@26) — carries `continuity-from loc-state:4:` notation; loc-state:5's anchor @26 is inside scene-C `fusion-eligible-runs: @26-@29` but scene-C's `rhythm-shape` is `peak-and-release`, not a continuity-license-permitted shape (flat-low / resolving / release-only)
  - why: FAULT-LOC-STATE-CONTINUITY-MISPLACED. The continuity-carry entry was authored on a momentum scene (scene-C is peak-and-release, meaning it contains a peak-bone and peak-shadow bones; the post-peak @26-@29 zone is a fusion-eligible dissolve but the scene's rhythm-shape is still classified as peak-and-release). The continuity-license's rhythm-shape gate (condition b) requires the scene's rhythm-shape to be flat-low, resolving, or release-only — none of which match peak-and-release. The entry was authored into a fusion-eligible run inside a momentum scene, which is the misplacement the FAULT-LOC-STATE-CONTINUITY-MISPLACED finding targets.
  - why (downstream): the continuity-carry entry at @26 adds the drain-water trickle sensory note to the ledger-close sequence. If deleted or reauthored as a standard loc-state entry (not a continuity-carry), the stitcher still receives the environmental grounding; the issue is the carryover notation form, not the content. If retained as-is, the audit class CONSTRAINT is violated. Fixer should either (a) reauthor loc-state:5 without the continuity-carry notation (making it a standard loc-state entry at @26 with the same sensory content) or (b) confirm that a post-peak fusion-eligible run within a peak-and-release scene satisfies the spirit of the license (the post-peak bones are effectively a resolving zone within the peak-and-release shape) — if fixer takes option (b), a rubric carve-out annotation is required per the carve-out preamble schema.
  - criteria: loc-state:5 @26 must not carry a continuity-carry notation that violates condition (b) of the URI-SCENE-RHYTHM continuity-license. Either reauthor as a standard loc-state entry retaining the same sensory content, or author a rubric carve-out preamble entry justifying why a post-peak fusion-eligible run within a peak-and-release scene satisfies the continuity-license's rhythm-shape gate.

---

## AP-SCAN findings (1 SIGNAL)

**NI AP scan — X-was-Y predicate chassis saturation:**

The NI R2 decision shard's PATTERN-SCAN section self-identifies this: three instances of the cold-utilitarian-inventory past-perfect declarative chassis at sentence-final position (narrator:1 "the 200 was the working ceiling," narrator:5 "the gap … was the wrong shape," narrator:6 "the count stalled at the edge … what was on the other side of the stall was the recognition"). Saturation check: 3 instances / 9 total entries = 33%. Below the 40% URI-AP-SCAN-SATURATION threshold for HARD escalation. The R2 judge noted this pattern and diversified the ADD chassis (narrator:8 paired-clause, narrator:9 temporal-comparison). Threshold: 33% < 40% — SIGNAL only, does not escalate to HARD.

- flag-007
  - id: flag-007
  - type: flag
  - what: interest-narrator-b01-c02.md — X-was-Y past-perfect declarative chassis at sentence-final position; narrator:1 @6, narrator:5 @18, narrator:6 @24; 3 of 9 entries = 33%
  - why: AP-SCAN candidate for template saturation (AP10 per the rubric's chassis-repetition concern). Below the 40% HARD-escalation threshold; SIGNAL. The R2 judge's diversification of the ADD chassis is the correct mitigation. If a future revise pass adds a fourth X-was-Y entry, the saturation would hit 4/10 = 40% and escalate to HARD. Forward watch item.
  - why (downstream): no blocking consequence at 33%; audience may notice the template at pass-5b but it is within the diversity range the R2 judge calculated acceptable.

**Metaphor AP7 scan:** zero fires; AP7 default-refuse discipline upheld. No AP-SCAN findings for metaphor.

**Vibes AP8 sentence-parsability scan:** Spot-checked token bundles for sentence-parsable tokens (tokens that parse as subject + finite verb + object). Vibes:1 tokens: "first-deliberate-architecture-as-the-cage-she-built" — compressed noun-phrase with relative clause modifier; "harm-reduction-framing-is-the-first-rung" — parses as subject (harm-reduction-framing) + copula (is) + predicate (the-first-rung). This is a sentence-parsable token.

- flag-008
  - id: flag-008
  - type: flag
  - what: vibes-b01-c02.md entry 1 (@6) — token `harm-reduction-framing-is-the-first-rung` parses as subject + finite verb + predicate (is = finite copula); violates the schema's sentence-parsability test ("a token is forbidden if it parses as a complete sentence with subject + finite verb + object")
  - why: AP-SCAN AP8 (vibes AP-multi-source / sentence-parsability). The schema states the sentence-parsability test is the line for forbidden tokens. "harm-reduction-framing-is-the-first-rung" contains the finite copula "is" with a subject before it and a nominal predicate after; this parses as a declarative sentence compressed into hyphenated form. The other tokens in vibes:1 are clear noun-phrases ("first-deliberate-architecture-as-the-cage-she-built" is a relational noun-phrase; "systematic-over-ambient-as-the-direction-that-does-not-reverse" contains "does not reverse" which similarly parses as a clause — see below).
  - why (downstream): the stitcher reads vibes as bias signals, not prose; a sentence-parsable token would be interpreted as a bias-phrase rather than produced as prose, so the downstream rendering consequence is low. The AP8 violation is a schema discipline issue rather than a rendering quality issue. Signal only.

  Secondary check: `systematic-over-ambient-as-the-direction-that-does-not-reverse` in vibes:1 — "does not reverse" parses as finite clause within the token. Also AP8 candidate. Flagged under the same finding.

AP-SCAN saturation: 2 AP8 token hits / 17 vibes entries = 11.8%. Well below 40% threshold. SIGNAL.

---

## TASTE-FLAG findings (1)

- flag-009
  - id: flag-009
  - type: flag
  - what: feeling.md entry 1 (@17) — "her shoulders hold where they were | expressed: no" and narrator:4 @17 "the filing took less hesitation than it had the first time she did it" — adjacent registers at the same bone (somatic stillness / cognitive hesitation-comparison)
  - why: TASTE-FLAG / voice-fidelity. Both entries are technically defensible (different register channels), but a cold-reader at the same proto-line encounters the peak-bone carrying: 10 co-located facet entries (feel:1, narrator:4, state:2, vibes:6-12). The feeling and NI entries cover adjacent but not identical registers. An audience adversarial reader may attack: "the shoulders-hold somatic tell is the same information as the less-hesitation NI clause, just in different words." The NI is cognition-as-comparative-accounting; the feeling is body-as-postural-discipline; they are distinct channels under the rubric but the reader experiences both at the same bone. The TASTE-FLAG captures the audience-attack-surface without asserting a fault.
  - why (downstream): if a 5b audience reviewer flags this as a DEDUP attack, fixer would need to delete one. Under the rubric's tiebreaker (lens facet yields to the facet that is harder to replace), the feeling entry is harder to replace (somatic tells are the channel that body-only feeling carries; the NI's less-hesitation cognition is easier to express without the feel entry). This tiebreaker reasoning favors keeping feel:1 and deleting or revising the NI's less-hesitation clause — but this is a 5b adversarial-gate concern, not a Phase 5 mechanical fault.

---

## PILE-UP REVIEW (2 warranted, 1 warranted)

- @17 (10 co-located facets: feel:1, narrator:4, state:2, vibes:6-12): `the insects file the ward-junction contact`
  - Verdict: **warranted**. This is the scene-B peak-bone. The pile-up composition: 1 feeling (somatic stillness), 1 NI (cognitive hesitation-comparison), 1 state-update (wren-status: unknown → filed-as-ward-junction-contact-unnamed), 7 vibes (entity-target cross-fan-out: Taylor × 2, Wren × 3, lane × 1, episode × 1). The state-updates rubric requires NI co-citation at the same beat (explaining the state:2 + narrator:4 pair). The memory-flags rubric forbids peak-bone fires by default (memory absent at @17 — correct). The feeling and NI are distinct register channels. The vibes cross-fan-out (Taylor's wren-status, Wren's the-named-absence / rising-entrapment / mutual-silence, lane as mechanism-site, episode coverage-architecture-established) is the structural manifestation of a scene peak where multiple entities are affected simultaneously. Over-decoration standard: entries would need to fail their own three-axis tests. Each entry passes (per R2 judge's KEEP verdicts). The pile-up is dense but all entries are load-bearing for the chapter's central relational-accounting beat. Warranted.

- @6 (7 co-located facets: narrator:1, state:2, vibes:1-5): `taylor-hebert-kl-122ac extends the range`
  - Note: cite-index shows state:2 at @6 (the deployment-state flip), but the state-updates.md file has state:2 as @6 entry (actor:taylor-hebert-kl-122ac.deployment-state). The cite-index row for state:2 reads `state:2 @6 back=N co=[narrator:1, state:1, vibes:1, vibes:2, vibes:3, vibes:4, vibes:5]` — the `back=N` means the proto-line body does not carry a `[state:2]` citation token. The state-updates slice carries `state:2 @6` without the back-citation in the proto-lines file.
  - Pile-up verdict: **warranted**. The scene-A deployment-state flip (@6) is the chapter's mechanism-establishment anchor; the vibes cross-fan-out (Taylor: rising-entrapment × 1, atonement-as-repetition × 1, residue-not-spectacle × 1; loc: mechanism-site × 1; episode: coverage-architecture-established × 1) establishes the vibe-cloud for the chapter's organizing frame. NI:1 spines the state-update (required by rubric). Five vibes entries at a single mechanism-flip anchor is dense but the cross-entity fan-out covers Taylor (3 entities: Taylor's actor vibes, the lane, the episode scope) — distinct targets, distinct keywords, no duplicate territory. The episode-scope vibes at @6 and @17 and @24 are structurally appropriate (the three scene-peaks/flip-moments are the natural anchors for episode-scope vibe updates). Warranted.

- @24 (6 co-located facets: narrator:6, state:3, vibes:13, 15, 16, 17): `taylor-hebert-kl-122ac stalls the count`
  - Verdict: **warranted**. Scene-C peak-bone. Pile-up composition: 1 NI (recognition-as-architecture-built-to-stall), 1 state-update (coverage-map-recognition-event: not-yet-occurred → occurred), 4 vibes (Taylor: the-first-crack × 1, ledger-discipline-as-suppression × 1; episode: recognition-suppressed × 1; lane: mechanism-site × 1). Each entry serves the recognition-arrives beat. The vibes cross-entity fan-out is 3 targets at the chapter's axis-crack arrival point. Memory is deliberately absent (scene-C silence rubric-defended). Feeling:2 was deleted by R2 judge (correct per the DEDUP logic — the proto-line carries the body-action directly). State:3 + narrator:6 are the required POV co-citation pair. Warranted.

---

## RUBRIC-FIDELITY findings (0)

**Per-entry signature scan:**

- Loc-state: 5 entries. Anchor verbs scanned: @1 (leaves — transitional; ACCEPT), @4 (takes — positioning; ACCEPT), @11 (marks — attribution; ACCEPT), @20 (takes — positioning; ACCEPT), @26 (closes — accounting verb on the scene; but this entry is a continuity-carry with a different anchor verb in the bone "the accounting closes the fever-cluster entry" — the loc-state entry's anchor verb is "closes" which is an accounting verb, not a transitional/positioning verb. However, loc-state:5 is a continuity-carry entry, and the fault at the continuity-carry level is already captured in CONSTRAINT (fault-003). The signature check for loc-state:5 is secondary to the misplacement fault. Flag carries under fault-003; no separate RUBRIC-FIDELITY finding.

- State-updates registration vocabulary scan: state-updates entries use field-extension vocabulary ("deployment-state," "wren-status," "coverage-map-recognition-event," "coverage-map-recognition-status"). The rubric's anti-pattern #1 targets "registration vocabulary" (`noticed`, `registered`, `awareness`, `baseline-new-faces`) in `<new>` values. Checked: "systematic-precinct-coverage-deliberate," "filed-as-ward-junction-contact-unnamed," "occurred," "suppressed-under-harm-reduction." None of these are registration vocabulary in the anti-pattern sense — they describe operating modes and filing-status, not perception-of-observation. Passes.

**Per-facet file-level shape gate:**

- Memory doubled-register gate: at least one Earth-Bet displacement AND at least one Westerosi-monument clamp. mem:2 = Earth-Bet displacement (override-architecture-residue); mem:1 = Westerosi-monument clamp (conquest-charter-language). Both present. Passes.

- State-updates POV co-citation completeness: all four `actor:taylor-hebert-kl-122ac.*` entries (state:2 @6, state:3 @17, state:4 @24, state:5 @25) must pair with NI co-citations on the same beat. Per cite-index: state:2 @6 co-cites narrator:1 ✓, state:3 @17 co-cites narrator:4 ✓, state:4 @24 co-cites narrator:6 ✓, state:5 @25 co-cites narrator:7 ✓. All four pass.

- Sensory modality distribution: 2 modalities (sound @4, smell @11). ≥2 floor met. Dominance ceiling: 50%/50% — no single modality ≥67%. Passes.

- Memory quiet-beat / peak-beat distribution: mem:1 @7 (scene-A flat-low — licit), mem:2 @18 (scene-B peak-shadow resolving-tail — licit per rubric §Cross-axis tests: peak-shadow ≠ peak-bones). Scene-C silence rubric-defended. Passes.

**Per-entry cross-facet co-citation checks:**

- Memory without NI-spine: both memory entries have NI co-citations. Passes (repeated from CONSTRAINT; no new finding).
- State-updates actor POV without NI: all four actor entries have NI co-citations. Passes.

**Card-resolution checks:**

- mem:2 target-ref `cond-override-architecture-residue-122ac` — must resolve to an existing card in `cards/` or `active-project/warehouse/`. The series memory lists `cond-override-architecture-residue-122ac` under `series.laws`. This confirms the condition card is a named law; the card itself is presumed to exist in `active-project/warehouse/` or `cards/conditions/` (it is the canonical cross-chapter condition card for the series). Resolution assumed present (the auditor does not have direct file-system access to confirm the card path but the series.laws citation confirms its canonical existence). No RUBRIC-FIDELITY finding.
- mem:1 target-ref `monument-conquest-charter-language` — this is a descriptive monument slug without a trailing card path. The R2 memory judge notes it is "mechanism-descriptive (not an Earth-Bet proper-noun slug)" and that "a mechanism-form `monument-*` slug could be authored later via margit referral." The RUBRIC-FIDELITY card-resolution check requires the slug to resolve to an existing card. `monument-conquest-charter-language` does not appear to have a warehouse or cards/ entry — it is described as a notation slug for a monument type, not a card reference.
  - This would normally be a RUBRIC-FIDELITY HARD finding (unresolved card slug → `rubric-fidelity-card-resolution — target missing monument card`). However, the R2 memory shard explicitly anticipates this and categorizes it as SIGNAL-not-HARD on the same "mechanism-form slug; card could be authored later via margit referral" reasoning. The R2 judge's classification stands as an author-stated defense. Per the RUBRIC-FIDELITY class description: "SIGNAL for borderline cases the rubric leaves explicitly unspecified or marks 'exceptional with documented author defense' (when defense is present in the entry's notes, accept as SIGNAL)." Defense is present. Downgraded to SIGNAL.

- flag-010 (subsumed into existing SIGNAL classification; no separate finding ID assigned)
  - The `monument-conquest-charter-language` target-ref in mem:1 @7 lacks a resolvable card path in `cards/` or `active-project/warehouse/`. R2 memory judge anticipates this and documents it as a SIGNAL with a margit-referral recommendation. Accepted as SIGNAL per the author-defense provision. Margit referral candidate: `cards/conditions/monument-conquest-charter-language.card.md` (mechanism-descriptive form per URI-032).

RUBRIC-FIDELITY finding count: **0 HARD**. 1 SIGNAL absorbed (monument card unresolved; author-defended).

---

## Audit summary

- Total entries reviewed: 46 facet entries across 9 facets + 1 proto-lines file + 1 scene-map + 1 cite-index
- Finding totals by type:
  - **fault (HARD):** 2
    - fault-001: was reclassified to TASTE-FLAG (feel/NI adjacent registers — not identical content)
    - **fault-002 (HARD):** vibes:1-5 @6 carry `licensed-by: state-update:1` forward-citing a state-update at @20 — 14 bones after the vibes anchor
    - **fault-003 (HARD):** loc-state:5 @26 continuity-carry on a peak-and-release scene (condition b violation — URI-SCENE-RHYTHM)
  - **flag (SIGNAL):** 7
    - flag-001: sensory 6.9% above 6% band ceiling (modality floor makes deletion harmful; structural artifact)
    - flag-002: NI 31% above 25% band ceiling (mandatory co-citations inflate; bones-only structural artifact)
    - flag-003: exposition 17.2% above 1-5% band (per-episode caps satisfied; bones-only structural artifact)
    - flag-004: state-updates env slice 3.4% below 8% density floor (carve-out preamble present and defended)
    - flag-005: R2 shard cite_index_hash fields — NI/memory/feeling shards carry descriptive strings not SHA-form; staleness check cannot run mechanically on future sessions
    - flag-006: exposition:5 @20 — loc-state:4 fires AT @20 (condition b boundary; scene-bridge survives on substantive defense but technically at the fire-rule edge)
    - flag-007: NI AP10 X-was-Y chassis 33% (below 40% saturation HARD threshold; SIGNAL)
    - flag-008: vibes:1 AP8 sentence-parsable tokens (2 tokens: `harm-reduction-framing-is-the-first-rung`, `systematic-over-ambient-as-the-direction-that-does-not-reverse`)
    - flag-009: TASTE-FLAG — feel:1 + narrator:4 at @17 cover adjacent registers; 5b adversarial-attack surface
  - HARD classes: STRUCTURAL 0, CONTRADICTION 0, DEDUP 0, SUPERFLUOUS 0, CONSTRAINT 2, RUBRIC-FIDELITY 0
  - SIGNAL classes: FREQUENCY-BAND 4, METADATA-INCONSISTENCY 1, AP-SCAN 2, TASTE-FLAG 1
  - CURVE-SHAPE: SHAPE-OK

## Routing

- **fault-002** → fixer (author: showrunner / vibes). Criteria: vibes:1-5 at @6 must cite only sources that resolve to state-update entries at anchors ≤ @6. If intent is to license from the deployment-state flip at @6, correct citation is `state-update:2` (not `state-update:1`).
- **fault-003** → fixer (author: studio / location-state). Criteria: loc-state:5 @26 must not carry a continuity-carry notation that violates condition (b) of the URI-SCENE-RHYTHM continuity-license. Reauthor as a standard loc-state entry retaining the same sensory content, or author a rubric carve-out preamble entry with substantive rhythm-shape defense.
- **flag-001 through flag-009** → advisory; no fixer dispatch required. Forward-watching items for audience-gate (5b) review: flag-009 (TASTE-FLAG feel/NI adjacency at @17) is the most likely 5b attack surface.
- **Monument card referral** → margit. mem:1 target-ref `monument-conquest-charter-language` should be promoted to a card in `cards/conditions/` per URI-032 mechanism-descriptive slug convention. Not blocking; deferred to margit triage.
