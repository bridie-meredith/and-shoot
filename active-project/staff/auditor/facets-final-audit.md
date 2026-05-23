---
report: facets-final-audit
chapter: b01c01
timestamp: 2026-05-23
audit-classes-run: 12
HARD: 3
SIGNAL: 7
earth-bet-hits: 0
cite-graph-coherence: FAIL
scene-map-coverage: PASS
sidecar-absent-flag: known (dialogue-taylor R1 fork; R2 authored forward) — not re-raised as HARD
---

# Facets Final Audit — b01c01

Phase 5 mechanical audit against 12 audit classes. HARD = 3 (cite-graph structural faults). SIGNAL = 7. Phase 6 is gated: HARD must reach 0 before Phase 5b fires.

---

audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-23
  findings:

## STRUCTURAL findings (3 HARD, 1 SIGNAL)

    - id: fault-001
      type: fault
      what: proto-lines/b01-c01.md flat_id @15 carries citation token [loc-state:4]; cite-index records loc-state:4 as anchored at @11 (back=N at @11; back=N at @15 is absent from the cite-index entry — the token is present in proto-lines at @15 but the cite-index does not record loc-state:5 as back=Y)
      why: The loc-state:4 entry anchors at @11 (the working-corner midday locus) per location-state-b01-c01.md line 4. Proto-lines @15 ("taylor-hebert-kl-122ac passes the well-step") carries [loc-state:4] instead of the expected [loc-state:5]. The stitcher resolves citations by following token→entry; a token pointing to the wrong entry places the wrong facet content (the net-frame anchor at @11) against the well-step proto-line at @15. The downstream stitch render will pull loc-state:4's sensory note ("the working corner off the Hook: Coll's net-frame at the far edge") for the well-step proto-line, corrupting the render-as at that anchor.
      criteria: The citation token on proto-line @15 must resolve to loc-state entry 5 (anchored at @15: the well-step). Either the proto-line's [loc-state:4] token is corrected to [loc-state:5], or the loc-state file's entry numbering is reconciled such that the @15 entry has the ID that proto-lines @15 carries. The cite-index must be rebuilt post-correction to reflect coherent bidirectionality.

    - id: fault-002
      type: fault
      what: proto-lines/b01-c01.md flat_id @9 carries citation token [state:4]; cite-index records state:4 as anchored at @18 (back=Y at @18); flat_id @9 is not listed as a back=Y co-location for state:4 in the cite-index
      why: State entry state:4 anchors at @18 (studio.active_conditions.watch-rotation: absent -> passing-the-hook) per state-updates.md. Proto-lines @9 ("taylor-hebert-kl-122ac holds the feet") carries [state:4] — a citation that does not correspond to any state-updates entry anchored at @9. The stitcher will attempt to resolve [state:4] at @9 and pull the watch-rotation state-change (an @18-anchored event) into the render of the @9 held-feet beat, producing an anachronistic sensory render-as. The state:9 entry (actor:taylor.knowledge.ward-geometry: null -> flea-bottom-block-level-passive) IS the correct @9 actor-state fire, but the proto-line carries [state:4] (the @18 env-entry) rather than [state:9] (the @9 actor-entry).
      criteria: The stale [state:4] citation token on proto-line @9 must be removed. If the @9 beat warrants a state citation, the correct token is [state:9] (the actor:taylor.knowledge.ward-geometry @9 entry). The proto-lines file and cite-index must be rebuilt post-correction to reflect the accurate citation at @9.

    - id: fault-003
      type: fault
      what: cite-index section for loc-state shows loc-state:5 @15 back=N, loc-state:6 @18 back=N, loc-state:7 @22 back=N; proto-lines examination confirms @17 carries [loc-state:5] (not @18, where loc-state:6 anchors) and @22 carries [loc-state:6] (not [loc-state:7] as the facet entry requires)
      why: Three loc-state entries have back=N, meaning the proto-lines either carry the wrong citation token for that anchor or carry no token at all. Specifically: (a) @17 "the boots strike the cobbles" carries [loc-state:5] in proto-lines, but loc-state:5 anchors at @15; the @17 proto-line should carry [loc-state:6] (the watch-rotation Hook entry). (b) @22 "wren-stitch-maker-flea-bottom-ward enters the alley-mouth" carries [loc-state:6] in proto-lines but loc-state:6 anchors at @18; the @22 proto-line should carry [loc-state:7] (the alley-mouth scene-C entry). This is a systematic one-off citation-offset across the second half of the loc-state file: each proto-line carries the citation token for the PRIOR loc-state entry rather than the current one. The stitcher will apply wrong loc-state sensory-notes at three anchor beats in scenes B and C.
      criteria: Proto-lines @17, @18, and @22 must carry citation tokens matching the loc-state entry anchored at that flat_id: @17 → no loc-state token (or confirm loc-state:6 if a misplaced token is the source; loc-state:6 anchors at @18 not @17); @18 → [loc-state:6]; @22 → [loc-state:7]. The cite-index must be rebuilt post-correction. Root cause is likely a one-off numbering error introduced during the R2 loc-state citation-write-back to the inflight proto-lines copy.

    - id: fault-004
      type: flag
      what: cite-index entry vibes:10 @- (episode-scope vibe entry); back=- (no proto-line anchor)
      why: The episode-scope vibes:10 entry (target: episode; op: +) does not anchor to any proto-line flat_id. The cite-index records this as @- / back=-, which is structurally valid for an episode-scope operation per the vibes rubric (episode-scope ops target the episode vibe-cloud, not a specific bone). However, the entry's licensed-by field cites proto:9 and proto:27 — two specific proto-lines. If the stitcher's citation resolver encounters [vibes:10] on a proto-line, it has no anchor to validate against. Currently no proto-line carries [vibes:10] per the cite-index, so no stitcher fault is imminent. Flagged for confirmation that episode-scope vibes entries are intentionally anchor-free and that the licensed-by citation to specific proto-lines is being used as authoring provenance (not as a machine-resolvable citation hook requiring back=Y on those lines).
      criteria: N/A (flag only). Fixer should confirm that episode-scope vibes entries are handled correctly by the stitcher's citation path (no [vibes:10] token appears in proto-lines; the episode-scope entry renders via a different path than anchor-bound entries).

## FREQUENCY-BAND findings (3 SIGNAL)

    - id: fault-005
      type: flag
      what: memory-b01-c01.md; 2 entries on 27 bones = 7.4%; declared sparsity target in rubric is 1-5% of bones (0-1 entries maximum)
      why: The file header explicitly acknowledges the over-band count and defends it on doubled-register grounds (Earth-Bet displacement + Westerosi-monument clamp both required by rubric file-level shape gate). R2.2 judge carried the defense forward. The defense is rubric-grounded; this is advisory only. However, the sparsity breach at 7.4% is above the 5% ceiling and will draw audience scrutiny at Phase 5b. The rubric's §Calibration anchors allow the breach when doubled-register requires both registers to fire in a short chapter (27 bones is below the 30-bone floor where standard sparsity applies cleanly). The defense is present and legible; flagged as FREQUENCY-BAND advisory, not a blocking fault.
      criteria: N/A (flag only). If audience-gate challenges the count, the defense (doubled-register requirement + short-chapter constraint) is the on-file argument.

    - id: fault-006
      type: flag
      what: feeling.md (taylor-hebert-kl-122ac slice); 2 entries on 27 bones = 7.4%; declared sparsity target is 2-5%
      why: The file header acknowledges the over-band count and defends it on the V3 feel-as-spine carve-out (both entries serve as memory spines at the chapter's two doubled-register anchors). R2.3 judge confirmed. The scene-C slot is empty after the deletion of feel:3 @27. The defense is rubric-grounded; flagged as advisory. If the audience-gate raises it, the on-file defense (V3 carve-out, memory-spine function, short-chapter) is the argument.
      criteria: N/A (flag only).

    - id: fault-007
      type: flag
      what: location-state-b01-c01.md; 7 entries on 27 bones = 25.9%; standard rubric guidance is 4-9% per schema § location-state band; file header declares sparsity above guidance but cites flat-low fusion-eligible-run structure as justification
      why: All three scenes are flat-low with large fusion-eligible runs (@1-6, @12-19, @22-27). The loc-state file header argues that the continuity-carry structure and the necessity of each entry per the three-axis test (necessity / interestingness / frugality) justify the above-band count. However, the count is significantly above the 9% upper guidance. The RUBRIC-FIDELITY class cannot resolve the dispute without a rubric that explicitly names a continuity-carry exemption band; absent that explicit exemption, the above-band count is an advisory FREQUENCY-BAND flag. The audience-gate will determine if the density reads as overstuffed in the stitch render.
      criteria: N/A (flag only). Fixer should not trim loc-state before the audience-gate verdict.

## METADATA-INCONSISTENCY findings (1 SIGNAL)

    - id: fault-008
      type: flag
      what: feeling.md wren-stitch-maker-flea-bottom-ward slice, line 198: "Two bodies, adjacent beats, distinct work." This comment references "Taylor drops gaze to the mesh one beat before lifting it" (feel:3 @27) as doing complementary work. But feel:3 @27 was deleted at R2.3 per the taylor slice header and per the deletion-note in the taylor slice. The wren-slice commentary at line 198 has not been updated to reflect the deletion; it still references the deleted feel:3 entry as a live cross-facet pair.
      why: The PATTERN-SCAN paragraph in the wren slice (lines ~190-200) states "Two bodies, adjacent beats, distinct work" referring to the @26 (Wren) and @27 (Taylor) feel entries as structural complements. Taylor's @27 entry is deleted. The wren-slice commentary creates a false picture of the file's state that the audience-gate reviewers will read as part of the consolidated graph. An audience-gate reviewer reading the wren slice commentary will expect to find feel:3 @27 in the taylor slice and find only a deletion-note. This creates reviewer confusion at Phase 5b.
      criteria: N/A (flag only). The wren slice's PATTERN-SCAN paragraph should note that the @27 Taylor feel entry was deleted at R2.3 (feel:3 @27 deletion-note) and update the cross-facet commentary accordingly.

## CURVE-SHAPE verdict

All three scenes carry rhythm-shape: flat-low per scene-map-b01-c01.md. No peak-bones in any scene. dramatic_shape declared as `hinge` in showrunner memory. The hinge designation (chapter 1 of 18 in a tragedy) is load-bearing: b01c01 establishes the prohibition-intact baseline, not a pressure peak.

SHAPE-OK: The flat-low rhythm across all three scenes is consistent with a `hinge` chapter declared as a baseline placement. The `hinge` enum per schemas/showrunner-memory.schema.md permits a flat-baseline shape when the hinge function is the operating-rule establishment (the rule is intact here, not under pressure). The absence of peak-bones is structurally correct: the chapter's narrative function is to establish the discipline before it is tested. The metaphor file's empty state (correct under AP7 which requires peak-bones as the licensing band) is the direct consequence of the flat-low shape and is correctly handled.

Per-scene: scene-A flat-low (no peak) / scene-B flat-low (no peak) / scene-C flat-low (no peak). Adjacency: 0 1→3 jumps (all scenes flat-low, no density spike). Flatlining: the entire chapter (27 bones) is flat-low; this is architecturally correct for a hinge-baseline chapter and does not read as unintended flatlining. SHAPE-OK.

## CONTRADICTION findings (0)

No contradictions found. State-updates entries check: studio.time_of_day moves null→morning→afternoon sequentially; no reversal. Actor position changes are unidirectional within the chapter (@22 Wren enters, @28 Wren exits; no reentry contradiction). State-updates at @1 initialize two fields simultaneously (position + occupation for Taylor) — these are initialization pairs, not contradictions.

## DEDUP findings (2 SIGNAL)

    - id: fault-009
      type: flag
      what: vibes:7 @26 and vibes:8 @26 — two separate vibe entries both targeting actor:wren-stitch-maker-flea-bottom-ward at the same proto-line @26; vibes:7 targets wren's `observation` token cluster, vibes:8 targets wren's `silence` token cluster
      why: Two co-anchored entries on the same target-actor at the same beat is above the standard single-event per-target expectation but the rubric's V1.1 Patch explicitly permits multi-token ++ operations when distinct keyword clusters are licensing distinct behavioral implications. The showrunner (vibes author) split them explicitly (E5 in the fan-out section: "(a) ++ on wren's observation — first on-screen fire; (b) ++ on wren's silence"). This is within the rubric's fan-out design. Flag is advisory: if Phase 5b audience finds the split redundant (two vibe fires on the same actor at the same beat), the on-file defense is the distinct-cluster argument. Not a HARD.
      criteria: N/A (flag only).

    - id: fault-010
      type: flag
      what: vibes:9 @27 (actor:taylor-hebert-kl-122ac ++ wren: licensed-by: feeling:3, proto:27) — vibes:9's licensed-by field cites feeling:3 as a spine. But feeling:3 @27 (taylor drops gaze one beat before lifting it) was deleted at R2.3. The license citation is broken: feeling:3 no longer exists in the canonical feeling.md.
      why: The vibes:9 entry's `licensed-by:` field contains `feeling:3` as one of two citations (the other is `proto:27`). Post-R2.3 deletion of feel:3 @27, the `feeling:3` citation no longer resolves to a live entry. The rubric requires that vibes `licensed-by:` anchors resolve to existing entries; an unresolvable anchor is a CONSTRAINT violation (§CONSTRAINT — vibes with unresolvable or forward-citing licensed-by). However, the second citation `proto:27` is a proto-line anchor that does resolve. The rubric's CONSTRAINT class requires "at least one resolving citation in licensed-by"; proto:27 resolves. Classifying as SIGNAL (flag) rather than HARD because the proto-line citation provides a live anchor; the feeling citation is the broken half of a two-citation licensed-by. If the rubric mandates all citations must resolve (not just one), this escalates to HARD.
      criteria: N/A (flag only; reclassify to fault if rubric is found to require all licensed-by citations to resolve). Fixer should remove `feeling:3` from vibes:9's licensed-by and confirm proto:27 alone is sufficient for the anchor license.

## SUPERFLUOUS findings (0)

Lonely entries were reviewed (loc-state:4 @11, narrator:5 @24, sensory:2 @12, sensory:3 @14, state:3 @7, exposition:2 @4). Each passes the rubric three-axis test (necessity / interestingness / frugality) independently:

- loc-state:4 @11: scene-B open; new time-of-day + new working locus; fires at the mandatory scene-open anchor under the movement-verb gate (absence of movement verb at @11 is a rubric exception for scene-open anchors). Lone but necessary.
- narrator:5 @24: the bones-review NOTE confirmed this beat cannot self-carry the assessment-fires registration; narrator is the required carrier for the structural distinction; lone because the pre-calc registration is interior-only; not superfluous.
- sensory:2 @12, sensory:3 @14: both are distinct modalities (tactile, thermal) in a flat-low scene where modality diversity is the justification for the short-chapter V3 exemption; lone entries from different modality families do not need co-location to earn.
- state:3 @7: pack position change is a genuine persistent inventory state-change; no co-citation required by rubric for a physical-inventory move.
- exposition:2 @4: first-mention-character for Coll; no co-citation exists at @4 because NI is silent; the exposition's specific payload (fixture-not-confidant orientation) is not carried by any lens facet; not superfluous.

## CONSTRAINT findings (2 HARD, 1 SIGNAL)

The Earth-Bet hard-fence scan is reported separately below (0 hits). The following CONSTRAINT findings are non-Earth-Bet violations.

    - id: fault-011
      type: fault
      what: vibes:9 @27 licensed-by field cites feeling:3 — a deleted entry (feel:3 @27 removed at R2.3 on §Form temporal-latency seam); the CONSTRAINT class requires "vibes with unresolvable licensed-by → HARD" (per Phase 5 audit class 8 CONSTRAINT enumeration)
      why: The rubric's CONSTRAINT class enumerates "vibes with unresolvable or forward-citing licensed-by" as HARD. feeling:3 is deleted; the citation is unresolvable. Even though proto:27 is the second citation and resolves cleanly, the CONSTRAINT class's language "unresolvable licensed-by" applies to the citation set — one broken citation in the set means the set is not fully clean. The R2 vibes judge did not update the licensed-by field when feel:3 was deleted (R2 vibes is not re-judged per Phase 3 note: "Vibes is not re-judged in R2; the showrunner-authored R1 vibes facet stands as-is unless the audit flags it").
      criteria: vibes:9's licensed-by must not contain an unresolvable entry-reference. Remove feeling:3 from the licensed-by citation; confirm proto:27 provides sufficient anchor for the entry's license claim. The vibes facet author (showrunner) executes the repair; the cite-index must be rebuilt to confirm back-resolution is clean after the correction.

    - id: fault-012
      type: fault
      what: state-updates.md (taylor-hebert-kl-122ac slice), entry state:10 @20 (actor:taylor-hebert-kl-122ac.knowledge.ward-geometry: flea-bottom-block-level-passive -> flea-bottom-block-level-with-patrol-rotation) has no narrator-interest co-citation; rubric §Cross-facet contract for state-updates-actor:<POV>: requires NI co-citation on every actor:POV state-update entry
      why: Per the RUBRIC-FIDELITY class (§Cross-facet contract in rubric-state-updates.md), every actor:<POV>.* entry must pair with a narrator-interest entry on the same beat. narrator:7 @20 fires on the same beat (the ledger-close entry: "the day closed under the count she had been running; nothing had been moved that needed not to be moved"). This IS a POV-interiority fire on the same bone. The cite-index confirms co-location: state:10 @20 co-cites [narrator:7, state:5] — so narrator:7 IS co-cited. However, the critical question is whether the NI entry's content licenses the knowledge-field mutation. narrator:7 is a ledger-close / cost-tracking register fire, not a ward-geometry knowledge-acquisition fire. The state-update says she now knows flea-bottom-block-level-with-patrol-rotation, but the NI at @20 does not register the patrol-rotation as a specific knowledge event — it registers the day as closed-under-count. The knowledge axis mutation at @20 is broader than what the co-cited NI entry registers. This is a partial cross-facet co-citation failure: the co-citation exists but the NI content does not fully license the specific field mutation named in the state-update. Elevated to HARD because the rubric-state-updates §Cross-facet contract is a named REQUIRED rule per RUBRIC-FIDELITY class.
      criteria: Either (a) the state:10 entry's field mutation is narrowed to match what narrator:7's ledger-close register licenses (the day's read is complete, consistent with general ward-geometry-built-up but not specifically the patrol-rotation which was registered at @18-@19 by narrator:4 — now deleted), or (b) narrator:7 is updated to name the patrol-rotation as one of the day's counted items in its text (which would bring the NI text into alignment with the state field mutation). The co-citation structure is intact; the content alignment is the gap.

    - id: fault-013
      type: flag
      what: exposition-b01-c01.md entry exposition:1 @1, licensed-by field names "dark-fantasy-reader (Planetos-local-color-needs-naming-as-institution-not-just-environment)" and "worm-canon-pedant (geographic-anchor-for-series-locus)"; per CONSTRAINT § exposition license-completeness, each entry's licensed-by must name ≥1 persona-card slug plus a specific gap-claim; both named slugs are active-project audience personas per showrunner memory (staff.audience: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]); however exposition:1's licensed-by omits cape-fic-reader from the justification (the R2.5 shard explicitly notes "Cape-fic-reader does not gap here" — which is valid, but the CONSTRAINT class requires the persona-set attestation to be complete, and an explicitly-refused persona with documented rationale is the correct form); the omission itself may signal that the 2-of-3 gap confirmation is present (it is), but the form requires documentation that the third persona was tested and found clean
      why: Minor license-completeness form gap. The R2.5 shard contains the cape-fic-reader attestation ("does not gap here"). The exposition file's licensed-by field does not include the clean-attestation for the refused persona. The CONSTRAINT rule reads "every entry's licensed-by field must name ≥1 persona-card slug + a specific gap-claim"; the current form satisfies this (2 slugs, both with gap-claims). The advisory is that the refused-persona attestation should appear in the licensed-by or notes to make the 2-of-3 coverage explicit and protect against Phase 5b adversarial review. Classified as SIGNAL (the ≥1 requirement is met; this is a form tightness issue, not a gap in the gap-test itself).
      criteria: N/A (flag only). If audience-gate challenges exposition:1, the R2.5 shard provides the cape-fic attestation on demand.

## AP-SCAN findings (2 SIGNAL)

    - id: fault-014
      type: flag
      what: narrator-interest-b01-c01.md entries narrator:2 and narrator:3 each use a single semicolon in a clause-sequence structure; narrator:6 uses the inverted-predicate form with a semicolon. The three semicolon-spine entries are: "the sense runs along the walls and stops because the walls are the limit, not because something forced it back" (narrator:2 — no semicolon, re-check: this is a clause with comma + because-inversion, not a semicolon spine); "every warm body in the block is legible; the density is running at the level that used to mean work, and she is not doing work" (narrator:3 — one semicolon); "the flies are what the read should have caught and didn't; what she sees is what the insects already knew, and she arrived at it without the insects" (narrator:6 — one semicolon); "the day closed under the count she had been running; nothing had been moved that needed not to be moved" (narrator:7 — one semicolon). AP-1 (chassis contamination — em-dash + semicolon spine on non-Taylor speakers) does not apply here (these are Taylor-POV NI entries, not non-Taylor speaker dialogue). However, AP-7 (vocabulary saturation — low-frequency construction pattern) applies: 3 of 6 NI entries use a semicolon-pivot structure (narrator:3, narrator:6, narrator:7). 3/6 = 50%, above the 40% saturation threshold for sparse-by-design facets (NI band 15-25%). Per URI-AP-SCAN-SATURATION, this escalates from advisory to blocking when hits/total-entries ≥ 0.40 in a facet with FREQUENCY-BAND ceiling ≤ 25%. NI ceiling is 25%; 3/6 = 50% > 40%. This SHOULD trigger AP-SCAN escalation to HARD under URI-AP-SCAN-SATURATION.
      why: The semicolon-pivot construct appears in 3 of 6 NI entries (50%), exceeding the 40% saturation threshold for sparse-by-design facets. Under URI-AP-SCAN-SATURATION, this is template-saturation (not isolated misfire) that produces the "reading the construction before the content" failure mode. The R2.1 judge PATTERN-SCAN specifically reviewed semicolon usage and concluded "the semicolon usage across surviving entries is one-per-line in single-pivot structure... reads as base-card structural-function use, not ornament." The R2 judge's defense addresses quality, not the mechanical saturation count. The URI-AP-SCAN-SATURATION rule escalates on count regardless of quality. However, narrator:2 does NOT use a semicolon (it uses comma-clause inversion), which reduces the semicolon count to 3 out of 5 entries that use any structured pivot at all. Formally: semicolon-bearing entries are narrator:3, narrator:6, narrator:7 = 3 of 6 total = 50%. Threshold 40% is exceeded; escalation to HARD is mechanically triggered. Classified as SIGNAL here with escalation-candidate note, because the R2 judge's defense introduces uncertainty about whether the "construction before content" failure mode is present (the R2 defense argues each construction does distinct work). Fixer-dispatch recommended before audience-gate to resolve whether the saturation count constitutes a mechanical HARD or whether the R2 judge's quality-defense suffices as a documented author defense (rubric text: "SIGNAL for borderline cases the rubric leaves explicitly unspecified or marks 'exceptional with documented author defense' — when defense is present in the entry's notes, accept as SIGNAL").
      criteria: N/A (flag only). Escalate to fault if fixer cannot confirm the R2 judge defense constitutes the documented-author-defense exception in URI-AP-SCAN-SATURATION.

    - id: fault-015
      type: flag
      what: exposition-b01-c01.md, entry exposition:2 @4 (Coll first-mention): "the kind of presence a ward accumulates the way buildings accumulate moss, noticed without registering as notable" — the simile ("the way buildings accumulate moss") may trigger AP-3 (asinine-pattern / figurative language in exposition). The exposition rubric forbids "ornamental figurative language substituting for plain-English gloss"; the simile here carries the semantic content (gradual-passive accumulation) rather than decorating it.
      why: Exposition's AP-SCAN class includes anti-jargon-hit / hollow-prose-hit / asinine-pattern-hit. The simile "the way buildings accumulate moss" is figurative language in an exposition entry. Whether it triggers AP-3 depends on whether the rubric classifies figurative-as-gloss as asinine-pattern (it does not — the simile carries meaning efficiently). However, the audience-gate's adversarial mode may attack it. Flagged as advisory; the simile earns by being shorter and more precise than the plain-English equivalent ("gradually becomes part of the environment through accumulated duration without marking the transition"). Not a blocking AP finding.
      criteria: N/A (flag only).

## TASTE-FLAG findings (2 SIGNAL)

    - id: fault-016
      type: flag
      what: Scene C (@22-29) carries 0 memory-flags, 0 NI in the first two bones (@22-@23), and the feeling layer has feel:4 (Wren) at @26 only; the payload beat at @26 is covered by 5 co-located facets (feel:3/narrator:6/vibes:7/vibes:8/wren:2), but the approach zone (@22-@25) has sparse facet coverage (loc-state:7 @22, exposition:5 @22, state:11-12 @22, narrator:5 @24, taylor-dialogue @25). The scene C atmosphere carries the chapter's structural weight; thin approach coverage may read as momentum stall before the payload lands.
      why: atmosphere-thin risk at scene-C approach zone. The plot payload of the chapter (NOTE-003) lives at @26; the approach (@22-@25) has only loc-state and exposition at @22, then a bare @23 (wren's first speech, dialogue only, no co-located lens facets), then narrator:5 @24 alone, then dialogue @25 alone. If the stitcher renders @23 and @25 without cross-facet texture, the payload at @26 may feel abrupt. TASTE-FLAG: momentum-stall risk at scene-C approach. Feeds Phase 5b adversarial reading.
      criteria: N/A (flag only). Audience-gate should specifically probe the @22-@25 approach zone.

    - id: fault-017
      type: flag
      what: vibes entries 1 and 2 both target actor:taylor-hebert-kl-122ac on `insects` and `king's-landing` respectively; their licensed-by citations are `state-update:1, state-update:2, proto:5` (vibes:1) and `state-update:1, state-update:2, proto:6` (vibes:2). However, state-update:1 and state-update:2 are the @1 initialization entries (studio.active_location: null→flea-bottom; studio.time_of_day: null→morning). Using chapter-open initialization state-updates as a vibe license for two separate vibe entries (@1 and @6) means both vibes are licensed by the same two state entries, which is a multi-source-via-single-state-pair pattern.
      why: vibes AP-multi-source: using a single pair of state-updates (the chapter-open initializations) to license two different vibe operations at different anchors is AP-multi-source-via-shared-license. The V1.1 patch does not explicitly forbid this pattern, but the at-rest reading asks whether the @6 vibe (king's-landing tallow-smoke) is distinctively licensed by the @1 initialization entries or merely by the @6 proto-line (tallow-stall pass). The `proto:6` citation anchors vibes:2 correctly to the @6 event; the `state-update:1/2` shared license weakens the semantic distinctiveness. Advisory flag; not a blocking fault.
      criteria: N/A (flag only). Audience-gate may surface this under voice-fidelity lens (the tallow-smell vibe's license reads as initialization-carry rather than event-specific licensing).

## PILE-UP REVIEW (3 pile-ups)

- @1 (6 facets: exposition:1, loc-state:1, state:1, state:2, vibes:1, vibes:2) — verdict: WARRANTED. The chapter-open beat is the canonical high-density anchor: place establishes, time establishes, currency establishes, two vibes initialize. Each entry performs a distinct function at the chapter threshold: loc-state:1 opens the environmental register; state:1-2 initialize location and time; vibes:1-2 initialize two distinct keyword clusters (insects and king's-landing); exposition:1 fills the institutional-social gap none of the lens entries covers. All six entries pass the SUPERFLUOUS three-axis test independently. The density is warranted for an establishment beat.

- @9 (6 facets: feel:1, mem:1, narrator:2, state:4 [see fault-002 re: citation correctness], vibes:3, vibes:4) — verdict: WARRANTED with citation-fault note. The @9 held-feet bone is the chapter's inverted-establishing-fact anchor; it is structurally load-bearing and the highest-density beat in a flat-low chapter. Each entry performs a distinct register: feel:1 (somatic posture), mem:1 (Earth-Bet displacement monument), narrator:2 (cognitive register of refusal), vibes:3-4 (two distinct vibe tokens on override-architecture-residue and atonement). The pile-up is warranted; however state:4 (@18 watch-rotation) should not be in this pile-up — see fault-002. Post-correction the pile-up drops to 5 entries with the correct state:9 (@9 actor knowledge) citation optionally present.

- @26 (5 facets: feel:3, narrator:6, vibes:7, vibes:8, wren:2) — verdict: WARRANTED. The chapter's payload beat. Note: feel:3 here is the consolidated-id for the wren slice's entry 3 (@26 Wren's gaze-to-hands somatic tell). This is feel:4 in the consolidated feeling.md (wren-slice local id 1, consolidated id 4 per wren's cite-index note "feel:4 / feel:5-candidate numbering reflects consolidated-id convention"). The pile-up annotation in the cite-index shows "feel:3" — if this refers to the deleted taylor feel:3 @27, that is a stale pile-up entry. If it refers to the wren feeling entry (consolidated feel:4), the cite-index pile-up label is incorrect (should read feel:4, not feel:3). Flagged as a metadata inconsistency in the pile-up annotation; needs reconciliation at cite-index rebuild.

## RUBRIC-FIDELITY findings (1 SIGNAL)

    - id: fault-018
      type: flag
      what: memory-b01-c01.md, file-level doubled-register test: the rubric requires "at least one Earth-Bet displacement fire AND at least one Westerosi-monument clamp fire." mem:1 @9 = Earth-Bet displacement; mem:2 @16 = Westerosi-monument clamp PRIMARY + Earth-Bet shadow. The doubled-register requirement is satisfied. However, per rubric §Calibration anchors, the standard 1-5% sparsity ceiling applies unless doubled-register mandates a second fire. With 2 entries (7.4%), the above-band is defended on doubled-register grounds. RUBRIC-FIDELITY check: the defense is present and the criteria is met. No fault. Flagged as a cross-check confirmation: the R2.2 judge's file-level shape gate (doubled-register PASS) is confirmed by the audit.
      criteria: N/A (pass confirmation; no finding to resolve).

    - id: fault-019
      type: flag
      what: state-updates.md (env slice), entry 3 at @7 (prop:oc-taylor-pack.position: carried -> set-at-working-corner): the prop slug "oc-taylor-pack" is not verified as resolving to an existing card in active-project/warehouse/ or cards/props/. The RUBRIC-FIDELITY class requires "every facet entry that names a card slug must resolve to an existing card." The "oc-" prefix suggests an original-character prop (not a library card), but without warehouse verification the slug is unconfirmed.
      why: Per RUBRIC-FIDELITY §(d) Card-resolution checks: prop slugs in state-updates target fields must resolve. The prop:oc-taylor-pack slug was not verified against active-project/warehouse/ during this audit pass (warehouse contents not fully enumerated in the audit inputs). Flagged as advisory pending warehouse verification.
      criteria: N/A (flag only). Verify prop:oc-taylor-pack resolves to an active-project/warehouse/ card. If absent, the auditor's margit-referral candidate slug is prop:oc-taylor-pack (mechanism-descriptive form of the pack Taylor carries).

---

## Audit summary

- Total entries reviewed: 49 facet entries + 4 dialogue utterances (3 characters) + 10 vibes entries + scene-map
- HARD classes: STRUCTURAL 3 (fault-001, fault-002, fault-003: loc-state citation offset, stale state:4 token at @9, loc-state one-off offset in scenes B/C), CONSTRAINT 2 (fault-011: vibes:9 unresolvable licensed-by; fault-012: state:10 NI co-citation content-alignment gap)
- SIGNAL classes: FREQUENCY-BAND 3 (fault-005/006/007), METADATA-INCONSISTENCY 1 (fault-008), DEDUP 2 (fault-009/010 advisory), AP-SCAN 2 (fault-014 saturation-candidate; fault-015 exposition simile), TASTE-FLAG 2 (fault-016 scene-C approach thin; fault-017 shared-license), RUBRIC-FIDELITY 2 (fault-018 confirmation; fault-019 prop slug)
- CURVE-SHAPE: SHAPE-OK (hinge chapter, flat-low baseline, no peak-bones; structurally correct)
- Earth-Bet hard-fence scan: 0 hits across all text fields (facet entries, dialogue utterances, objectives, sidecar bodies)
- Cite-graph coherence: FAIL (3 HARD: fault-001 loc-state:4 mis-cited at @15; fault-002 stale state:4 token at @9; fault-003 systematic loc-state one-off token offset in scenes B and C)
- Scene-map coverage: PASS (27/27 bones covered, no gaps, no overlaps, no dangling anchors, frontmatter totals match body)

## Routing

- fault-001, fault-002, fault-003: cite-graph structural corrections → fixer (studio / cite-index rebuild). Proto-lines file and loc-state file citations must be reconciled; cite-index must be rebuilt post-correction.
- fault-011: vibes:9 licensed-by correction → fixer (showrunner as vibes author). Remove the dead feeling:3 citation from vibes:9's licensed-by field.
- fault-012: state:10 NI content-alignment → fixer (state-updates-actor taylor fork OR narrator-interest author). Either narrow the state:10 field mutation or expand narrator:7's text to name the patrol-rotation.
- SIGNAL findings (fault-004 through fault-019 excluding HARDs): advisory; no fixer dispatch until after audience-gate verdict unless escalation criteria trigger.
