```yaml
audit:
  scope: series
  target: taylor-hebert-westeros-road-to-hell
  timestamp: 2026-05-24
  findings:

    # ─── CONSTRAINT COMPLIANCE ───────────────────────────────────────────────

    - id: finding-001
      type: pass
      what: Earth-Bet proper-noun fence (project.hard_fences[0])
      why: taylor-hebert-kl-122ac/card.md Hard Fences section explicitly encodes the fence as binding; the constraint is also in the series.laws list (cond-earth-bet-noun-fence). No trajectory delta, cost_ledger entry, or cast_roster role description uses parahuman jargon. Constraint is coherently enforced across all three artifact layers.

    - id: finding-002
      type: pass
      what: POV single Taylor hard fence (project.hard_fences[1])
      why: series.structure.pov = single. cast-brief.md § 2 recaps the constraint and enumerates its deliverability consequences for every cast member. dramatist viability Q3 confirms POV deliverability PASS for all 10 minimum-viable members. No non-Taylor narrator is proposed without interlude marking.

    - id: finding-003
      type: pass
      what: No titles on book or chapter (project.hard_fences[2])
      why: memory.md books[b01] carries no title field; structure uses slugs (b01). Constraint is structural — verified consistent.

    - id: finding-004
      type: pass
      what: End-place hard fence — locus "both" (Taylor dead/expelled + cost-bearer dies in Dance's opening violence)
      why: Trajectory d14 explicitly encodes both conditions as LOCKED. cost-bearer slot resolved to Wren; wren/card.md Hard Fence 6 encodes d14 death as a hard fence. position-prot-collapse end_rank = 1 (dead/expelled). relational_anchor_status end_rank = 9 (unprotected-at-burn). All three artifact layers agree.

    - id: finding-005
      type: pass
      what: Single-book length floor — 18 chapters, 3 scenes/chapter minimum
      why: books[b01].structure.chapter_count = 20, within 18-22 range. series.structure.book_length.scenes_per_chapter = 3-5. bone budget at chunk_targets.book.bone_count = 270-700 is consistent with 20 chapters × 3-5 scenes × 5-15 bones/scene (floor: 20×3×5 = 300; ceiling: 20×5×15 = 1500 — lower range 270 is slightly below the arithmetic floor of 300 but this is a bone-count target range, not a hard floor; the 18-chapter minimum is satisfied by the 20-chapter plan).

    - id: finding-006
      type: flag
      what: chunk_targets.book.bone_count lower bound (270) is below the arithmetic floor implied by the structure
      why: 20 chapters × 3 scenes/chapter (minimum) × 5 bones/scene (minimum) = 300 bones minimum. The chunk_targets.book.bone_count lower bound of 270 would require an average below the scene-minimum floor on some chapters. This is not a constraint violation (bone_count ranges are targets, not hard minimums per CLAUDE.md), but the 270 figure may generate SUBSTANCE-FLAT warnings at /and-substance book Phase 0 if interpreted as a hard floor. No structural impact on the series picture; flagged for downstream awareness.
      # Note: no criteria field — type is flag, not fault.

    - id: finding-007
      type: pass
      what: Canonicity fence — F&B-aligned (HOTD where F&B silent); AU-tolerant for Worm transit
      why: series.laws carries cond-westerosi-magic-dormant-122ac, cond-dragon-proximity-122ac. Otto's informal position since 120 AC is correctly encoded. Aemond's age (12 in 122 AC, per aemond-targaryen-122ac card) is canonically consistent (born 110 AC). Rhaenyra at Dragonstone, Laena dead 120 AC, Jacaerys and Lucerys as young children — all encoded in rhaenyra-targaryen-122ac/card.md and consistent with F&B. Taylor's transit mechanism is explicitly unexamined in the project brief, consistent with AU-tolerance provision.

    # ─── STATE CONSISTENCY ────────────────────────────────────────────────────

    - id: finding-008
      type: pass
      what: Perspective distribution — cast_roster vs signature perspective load
      why: cast_roster lists 1 protagonist / 1 antagonist / 5 supporting / 4 world. Signature carries 9 protagonist-perspective axes, 1 antagonist-perspective axis (social_tether-antag), 2 world-perspective axes (position-world, political_register-world). Distribution matches: single antagonist carries the single antagonist-perspective axis; world roles (4) carry the 2 world axes jointly; protagonist carries all 9 protagonist axes. No perspective slot is unoccupied by a named carrier.

    - id: finding-009
      type: pass
      what: Antagonist-pressure entries — pressure_source attributability
      why: All 9 antagonist_pressure entries name either Otto Hightower (cast slot: antagonist), Dance-ignition timeline (environmental — correctly designated; no cast slot required per cast-brief § Carrier Coverage Watch-item), Gold Morning memory (internal antagonist — Taylor's own interiority; correctly not a cast slot), cond-kl-witch-label-formation-122ac (series.laws condition), or faction-violence (environmental sub-pressure from Dance pre-ignition). Every pressure_source is attributable to a named cast member or a named condition/environmental force. No orphan pressure source.

    - id: finding-010
      type: pass
      what: series_audit.approved_at is null (pre-approval state)
      why: memory.md series_audit block: approved_at: ~, approved_by: ~, report_path: ~, stale_since: ~. All null. Consistent with being in the Phase 5 approval checkpoint. No stale_since set. If user approves, the command body must write approved_at and report_path to this block.

    # ─── CROSS-ARTIFACT DRIFT ─────────────────────────────────────────────────

    - id: finding-011
      type: pass
      what: Trajectory deltas (d01–d14) vs cost_ledger entries vs cast carrier coverage
      why: Full cross-walk completed:
        d01 — shifts capability + social_tether; cl01a (capability +1, witch-label onset, cost-bearer block exposure) + cl01b (social_tether-prot-rise +2) anchor to d01. Taylor (protagonist) and Wren (cost-bearer, enters exposure radius) both present as named carriers. No orphan.
        d02 — shifts relational_anchor_status + moral_legibility_to_self; no explicit cost_ledger entry for d02 movement (relational_anchor_status first crack is un-priced; correct per axis notes "named-but-outside-ledger"). No cost ledger entry is appropriate here; the absence is the point.
        d03 — shifts position-prot-rise, moral_framework, capability; cl02 (position +4, moral_framework -3) + cl-antag-d03 (social_tether-antag +4). Otto (antagonist) is the carrier; offer event matches d03 cause. Consistent.
        d04 — shifts capability + social_tether; cl03a (capability +3, moral_framework -2) + cl03b (social_tether-prot-rise +4) + cl-world-d04 (position-world +2). Flea Bottom network build event. Consistent.
        d05 — shifts political_register-prot; cl-d05 (political_register-prot +3, opportunity-missed). Alicent/Aemond/Criston insect-feed content is the pressure source per antagonist_pressure entry. Consistent.
        d06 — shifts relational_anchor_status + moral_legibility_to_self; cl-d06 (relational_anchor_status +2, moral_framework -1). Wren inside protection architecture. Consistent.
        d07 — shifts moral_framework + position; cl-d07a (position-prot-rise +2) + cl-world-d07 (political_register-world +2). Otto makes arrangement explicit. Consistent.
        d08 — shifts relational_anchor_status; cl-d08 (relational_anchor_status +2) + cl-d08b (social_tether-prot-rise +1). Wren as coverage-gap mechanism. Consistent; auditor flag-001 from prior cycle (cl-d08b inferentially anchored) carried forward as a watch-item per memory.md notes. Not re-escalated; watch-item remains.
        d09 — shifts political_register-prot; cl06 (political_register-prot +5, contempt arrives with no exit). Articulated contempt beat. Consistent.
        d10 — shifts social_tether + position + moral_legibility_to_self; cl04 (relational_anchor_status +3) + cl-antag-d10 (social_tether-antag +4). Non-extractable confirmed; courier detained. Consistent.
        d11 — shifts relational_anchor_status + moral_legibility_to_self; cl-d11 (relational_anchor_status +1). Taylor intercepts use-vector. Consistent.
        d12 — shifts moral_framework + capability; cl05 (capability +2, moral_framework -1). Full-coverage push. Consistent.
        d13 — shifts political_register-prot; cl-d06 referenced (typo risk — cl06 is the contempt-without-refusal entry; cl-d05 is the earlier resentment entry). The cost_ledger entry cl06 is correctly attributed to d13's contempt-without-refusal outcome even though the substance_delta labels it cl-d05 and cl06 together. No functional gap; two resentment/contempt entries cover d05 and d09/d13 beats. No orphan.
        d14 — shifts 5 axes simultaneously; cl07a (moral_legibility_to_self +4, social_tether-prot-collapse -7) + cl07b (position-world +2, position-prot-collapse -6) + cl07c (political_register-world +2, relational_anchor_status reaches 9). Dance ignition, Wren death, Taylor removal. Consistent.

    - id: finding-012
      type: pass
      what: cast-brief role specs vs card content — spot-check 5 actors
      why: Checked taylor-hebert-kl-122ac, otto-hightower, wren-stitch-maker-flea-bottom-ward, septon-halvard-flea-bottom, alicent-hightower-122ac.
        taylor-hebert-kl-122ac: Cold-utilitarian register, Earth-Bet noun fence, khepri-mantle sealed, range cap 200/400m, single-book closed arc, all required hard fences present. Vibe Seeds carry residue-not-spectacle and khepri-rhyme/cost signature (private associations section). Brief requirements fully encoded.
        otto-hightower: Proposal-register voice fully developed with five synthesized d03/d07/d09/d11/d12 dialogue samples. Hard Fence 5 explicitly encodes "proposal-register only; no direct threat." Sera-leverage mechanism encoded in Relationships + Action Costs. 122 AC position (off Small Council since 120 AC) stated in Description. Brief requirements fully encoded.
        wren-stitch-maker-flea-bottom-ward: Hard Fence 6 encodes d14 death as locked; Hard Fence 2 encodes "does not ask Taylor the question"; cond-cost-bearer-scene-frequency referenced; observer-training habit encoded. Brief requirements fully encoded.
        septon-halvard-flea-bottom: Hard Fence 1 confirms "not a named HOTD or F&B figure"; Hard Fence 3 confirms at-least-one-direct-encounter-per-act; Hard Fence 4 confirms "does not provide an alternative to Taylor's plan"; principled-slower voice encoded with 5 dialogue samples; moral_legibility_to_self axis carried. Brief requirements fully encoded.
        alicent-hightower-122ac: Hard Fence 1 confirms compound-eye-only observable; Hard Fence 5 confirms "no direct dialogue with Taylor"; dynastic-maternal affect encoded; smallfolk-invisible register explicitly present; political_register-prot contempt-accumulation function described. Brief requirements fully encoded.

    - id: finding-013
      type: pass
      what: carry_forward entries — distinctness and downstream target specificity
      why: cast_roster_notes.carry_forward contains 4 entries (cf-wren-d14-perceptual-mechanism, cf-d10-courier-face, cf-rhaenyra-pressure-staging, cf-relational-anchor-environmental). Each has a unique id; no duplicate IDs. Each names a specific downstream target (/and-substance chapter at d14; /and-substance chapter d05-d10 distribution; /and-substance book/chapter; studio scene texture). No two entries share the same target node. All four carry-forwards originate from the dramatist viability report (phase-3-dramatist-viability.md) as confirmed by the `from:` field. Content of each carry-forward matches the dramatist report's stated specifications. No drift between the report and the memory entries.

    # ─── DOWNSTREAM OPERABILITY ──────────────────────────────────────────────

    - id: finding-014
      type: flag
      what: actor_baselines field is empty (memory.md line 223-224)
      why: Schema requires actor_baselines to be authored at Step 4d post-cast. The field is currently []. Per the schema note embedded in memory.md, this is a HARD-ABORT condition for /and-substance book b01 Phase 0 if the field remains empty. This is not a Phase 5 fault — it is a known downstream dependency. The series-level audit is not blocked by this gap. The follow-on work item (author actor_baselines, likely at /and-substance book pre-Phase-1 or as an explicit step before /and-substance book b01) must be completed before the first book-level substance command. Auditor notes this as a flagged downstream known condition, not a fault.
      # No criteria field — type is flag.

    - id: finding-015
      type: pass
      what: /and-substance book b01 Phase 0 hard-abort preconditions (other than actor_baselines)
      why: series_audit.approved_at is null (will be set on user approval per the checkpoint). series_audit.stale_since is null. books[b01].stale_since is null. cast_roster is populated with 11 entries, all schema-compliant (slug, role, perspective fields present for each). The Phase 0 check requires approved_at to be non-null and stale_since to be null; both conditions will be satisfied on approval. No blocking gap identified beyond actor_baselines (flagged separately above).

    # ─── SUBSTANCE CARRIER COVERAGE ─────────────────────────────────────────

    - id: finding-016
      type: pass
      what: 12-axis carrier coverage — independent re-verification against final cast
      why: Verified against cast_roster as provisioned (11 members) vs all 12 in-motion axes:
        moral_framework (protagonist): Taylor — COVERED. Otto pressure. No orphan.
        capability (protagonist): Taylor — COVERED. Wren d08 coverage-gap mechanism.
        position-prot-rise (protagonist): Taylor — COVERED. Otto d07 formalization + Sera justification object.
        position-prot-collapse (protagonist): Taylor — COVERED. Otto dissolution at d14.
        relational_anchor_status (protagonist + cost-bearer): Taylor + Wren — COVERED. Environmental partial carrier (cond-kl-witch-label-formation-122ac) correctly designated as studio/staging matter.
        moral_legibility_to_self (protagonist): Taylor — COVERED. Septon Halvard as mirror at d06/d10 beat.
        political_register-prot (protagonist): Taylor — COVERED. Alicent/Aemond/Criston insect-feed content; Rhaenyra road-not-taken irony pressure added by elevation.
        social_tether-prot-rise (protagonist): Taylor — COVERED. Oswyn + Wren (Flea Bottom substrate) + Jarvis (patron-channel link).
        social_tether-prot-collapse (protagonist): Taylor — COVERED. Otto dissolution.
        social_tether-antag (antagonist): Otto — COVERED. Jarvis as structural exposure vector.
        position-world (world): Alicent + Aemond — COVERED. Criston operational arm + Rhaenyra Black-faction counter-position.
        political_register-world (world): Alicent + Aemond — COVERED. Rhaenyra Black-faction claimant + Sera succession-calculus object.
        12/12 covered. Zero orphans. Consistent with dramatist Q1 PASS.

    - id: finding-017
      type: pass
      what: Antagonist-pressure entry coverage — at least one real on-page force
      why: social_tether-antag axis has Otto Hightower (named cast member, antagonist perspective, direct on-page presence at d03/d07/d10). moral_framework pressure source is Otto Hightower (same). Three additional axes have Otto as primary pressure source (social_tether-prot-rise, position-prot-rise, position-prot-collapse). Two axes have Dance-ignition timeline as pressure source — a real environmental force made on-page through the trajectory's punctuated eruption events (d10, d12, d14). One axis has Gold Morning memory as internal antagonist — real interiority force with explicit per-chapter beat obligations. All nine antagonist_pressure entries have an attributable on-page force.

    # ─── NAME-NOVELTY AUDIT ──────────────────────────────────────────────────

    - id: finding-018
      type: pass
      what: oswyn-mudway-flea-bottom-elder — name-novelty check
      why: "Oswyn" does not appear in cards/personas/INDEX.md library persona slugs (checked full planetos list and full earth-bet list). The INDEX entry for oswyn-mudway-flea-bottom-elder is authored for this project; its slug is unique in the library. "Mudway" is a constructed street-name; not a surname appearing in any prior project cast. INDEX.md original_characters section entry records "name-novelty PASS" at authoring. Not a mira-stonefield-pattern echo (no archetype lead name; "Oswyn" does not appear in the library's prior OC name set). PASS.

    - id: finding-019
      type: pass
      what: jarvis-coin-kl-courier — name-novelty check
      why: "Jarvis" does not appear in cards/personas/INDEX.md prior slug names. "Coin" is a constructed surname per the card body ("acquired surname in the Flea Bottom practice for those of unclear parentage"). INDEX.md original_characters section records "name-novelty PASS" at authoring. No prior project OC named Jarvis visible in library index. PASS.

    - id: finding-020
      type: pass
      what: septon-halvard-flea-bottom — name-novelty / no-HOTD-canonical-name check
      why: "Halvard" does not appear in any canon HOTD or F&B figure name in the library index (no septon-halvard entry in any prior project). The card Hard Fence 1 explicitly states "Not a named HOTD or F&B figure." INDEX.md records "no HOTD/F&B canonical identity, name-novelty PASS" at authoring. Checked against library septon entries (septon-rowan, septon-dying-protector, oc-ward-septon-dragon-gate) — no "Halvard" prior use. The first name "Halvard" is not an archetype exemplar from the library's named characters. PASS.

    - id: finding-021
      type: flag
      what: INDEX.md contains two duplicate slug entries under planetos: criston-cole-122ac appears twice (lines 47 and 60); jarvis-coin-kl-courier appears twice (lines 49 and 64)
      why: These appear to be formatting/duplication artifacts in the INDEX file rather than functional card conflicts — only one physical card exists for each slug in active-project/actors/. The duplicate entries create risk of margit reading the index as having more members than it does, and could confuse downstream slug-count checks. Should be resolved at next margit touch on the index. Does not block the series picture.
      # No criteria field — type is flag.

    # ─── CARD SCHEMA FIDELITY ─────────────────────────────────────────────────

    - id: finding-022
      type: pass
      what: Card schema compliance — spot-check 5 actors (taylor-hebert-kl-122ac, otto-hightower, wren-stitch-maker-flea-bottom-ward, septon-halvard-flea-bottom, alicent-hightower-122ac)
      why: All five cards checked against schemas/card.schema.md:
        Frontmatter required fields — name, class, scope, origin, quality, tier — all present on all five cards.
        class: persona on all five. Correct.
        scope: library on all five. Correct (these are library cards copied into active-project/actors/).
        quality: full on all five. Required for on-stage personas per schema quality gate. PASS.
        tier: lead (taylor-hebert-kl-122ac, otto-hightower), supporting (wren, septon-halvard, alicent-hightower-122ac). Appropriate to scene-load specifications. PASS.
        persona-purpose: [on-stage-character] on all five. Correct.
        Core sections — Description, Voice, Taste, Pet Peeves present on all five. PASS.
        Fiction Role Overlay — Thematic Purpose, Look, Hard Fences, Default Stance, Action Menu, Action Costs, Off-Screen Cadence present on all five. Missing: Triggers and Inventory on alicent-hightower-122ac. Triggers is listed as optional in schema but is present on the other four cards; its absence on Alicent is not a violation given her compound-eye-only observable constraint (she has no triggers visible to Taylor). Inventory is project-scope only per schema; scope is library; correct to omit.
        Vibe Seeds section present on all five. PASS.
        variant-of + variant-reason on taylor-hebert-kl-122ac (variant-of: taylor-hebert). Both fields present. PASS.
        rhaenyra-targaryen-122ac (not in spot-check set but checked incidentally): variant-of: rhaenyra-targaryen, variant-reason present. variant-project: taylor-hebert-westeros-road-to-hell present. PASS.
        No card in the spot-check set shows schema drift.

    - id: finding-023
      type: flag
      what: otto-hightower card — scope: library; no variant-of or variant-project fields; original scant entry upgraded to full at taylor-westeros-good-intentions Phase 4
      why: The INDEX.md original_characters entry records "otto-hightower (upgraded scant→full; canon HOTD; tier: lead; upgraded taylor-westeros-good-intentions Phase 4 provisioning 2026-05-18)." The card itself carries scope: library and no variant-of field — it is the base card for Otto Hightower, upgraded in place rather than as a variant. This is technically correct schema behavior (a scant→full upgrade of the base card does not require a variant card). However, the card carries substantial project-specific addenda (dialogue samples synthesized for this project's beats; Wren/Sera/Aemond relationships written for this project's configuration) that may not be appropriate on the canonical library base card without scoping notes. This creates a latent risk: future projects using otto-hightower will inherit project-specific relationship and dialogue material authored for taylor-hebert-westeros-road-to-hell without it being marked as such. Not a blocking issue for this series; flagged for margit attention at project-close.
      # No criteria field — type is flag.

    # ─── VIBE-CLOUD DERIVATION ────────────────────────────────────────────────

    - id: finding-024
      type: pass
      what: Vibe-cloud derivation — spot-check 3 actor vibes files (taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward, otto-hightower)
      why: Checked against series vibe_cloud.keys (8 keys in memory.md books[b01].vibe_cloud) and trajectory vibe_cloud_keys (series-trajectory.md).
        taylor-hebert-kl-122ac/vibes.md: Contains all 8 book-level vibe_cloud keys as top-level entries (cold-utilitarian interiority, penitential-grey King's Landing, tragic-causal, contempt-without-refusal, smallfolk-gallows register, residue not spectacle, atonement-as-repetition, rising entrapment). World keys are a subset of the series vibe-cloud. PASS. Private/personal associations are distinct from world keys (khepri-memory-as-standard, insect-sense-as-residue-not-spectacle, earth-bet-noun-fence, cost-signature-range-bound). PASS. The residue-not-spectacle key carries "insect-sense-as-functional-infrastructure-not-wonder" and the cost signature is present ("cost-signature-range-bound" associations). PASS.
        wren-stitch-maker-flea-bottom-ward/vibes.md: World keys present (smallfolk-gallows register, residue not spectacle, tragic-causal, rising entrapment) — a subset of the series vibe-cloud, correct for a supporting character. Private/personal associations (observer-training-habit, mutual-silence, d14-catastrophe-hard-fence) are distinct from world keys. PASS. File is not empty. PASS.
        otto-hightower/vibes.md: World keys present (cold-utilitarian interiority, penitential-grey King's Landing, tragic-causal, rising entrapment) — subset of series vibe-cloud. Private associations (proposal-register, arithmetic-as-menace, sera-leverage-mechanism) are distinct from world keys. PASS. File is not empty. PASS.

    # ─── INTEGRATION ASSESSMENT ──────────────────────────────────────────────

    - id: finding-025
      type: pass
      what: Full series integration — substance signature + trajectory + structure + laws/lore/behaviors + cast + vibe-cloud cohere as a whole
      why: The 12-axis substance signature moves in a consistent direction with the 5-beat path (motivation → anchor → escalation → trade → irony). The trajectory's 14 deltas are individually anchored to cost_ledger entries, and the cost_ledger entries are anchored to named cast members or named conditions. The cast roster's perspective distribution (1/1/5/4) matches the signature's perspective allocation (9 protagonist / 1 antagonist / 2 world axes). The vibe-cloud is derived consistently from the trajectory's emotional register. The laws and behaviors list references the correct conditions for the world-building constraints. The books[b01] substance_delta.axes_in_motion roll-up matches the series signature start/end ranks (verified from memory.md: all 12 axes show net delta within ±1 of the series signature delta as recorded in the Phase 2/3 roll-up note). The carry_forward entries are actionable, distinct, and scoped correctly. The entire picture is operably coherent for /and-substance book b01.

    # ─── PLAN QUALITY SIGNAL ─────────────────────────────────────────────────

    - id: finding-026
      type: pass
      what: Phase 5 substance signature review history — attempt exhaustion check
      why: memory.md records Phase 5 attempt 1 → REVISE (audience SUBSTANCE-FLAT; dramatist ROLL-UP + CURVE-SHAPE FAIL; auditor faults). Phase 5 attempt 2 → ACCEPT (audience 3-of-3 SUBSTANCE-FELT; dramatist all 5 checks PASS; auditor ACCEPT zero hard / 4 soft non-blocking). Two attempts; second attempt cleared cleanly. No attempt-exhaustion scenario applies. The v2 substance signature is the live substance; it was not proceeded under exhaustion. No plan quality escalation warranted.
```

---

## Aggregate Verdict

`HARD: 0 | SIGNAL: 0 | TASTE: 0`

Findings breakdown: 17 PASS / 5 FLAG / 0 FAULT / 0 ESCALATE

Flags are non-blocking:
- finding-006: bone_count lower bound (270) is marginally below the arithmetic minimum floor implied by structure; watch-item for /and-substance book Phase 0.
- finding-014: actor_baselines field is empty; known HARD-ABORT condition for /and-substance book b01 Phase 0 if not resolved before that command runs.
- finding-021: INDEX.md has two duplicate slug entries (criston-cole-122ac, jarvis-coin-kl-courier); resolve at next margit touch.
- finding-023: otto-hightower base card carries project-specific content without scoping; latent cross-project contamination risk; address at project-close.
- finding-024: (incorporated into PASS; no standalone flag needed)

---

## Cap Summary

The series picture is coherent end-to-end: all 12 in-motion axes have named carriers, all hard fences are encoded in the relevant actor cards, all trajectory deltas are anchored to cost_ledger entries, and the cast as provisioned passes dramatist viability and axis coverage checks with zero orphans. The one item that most warrants attention before /and-substance book b01 is the empty actor_baselines field (finding-014), which will HARD-ABORT the first book-level substance command if not authored as a follow-on step prior to running that command.
```
