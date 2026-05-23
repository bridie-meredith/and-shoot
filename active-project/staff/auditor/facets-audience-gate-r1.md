---
report: facets-audience-gate
chapter: b01c01
cycle: 1
of_cycles_cap: 3
date: 2026-05-23
mode: facet-adversarial (strict 3-of-3 ACCEPT per facet)
reviewers_fired: 36 dispatches (3 sensory specialists + 9 facets × 3 active-audience + 3 dialogue-characters × 3 active-audience)
aggregate: FAIL (1 facet ACCEPT, 11 facet FAIL)
stage: cycle-1-complete
---

# Audience-gate Report — b01c01 cycle 1

The first cycle of Phase 5b adversarial review fired 36 reviewer dispatches across nine facets + three per-character dialogue files. Strict 3-of-3 ACCEPT aggregation rule applied per URI-AUDIENCE-AGGREGATION-RULE.

**Verdict tally:** ACCEPT 13 / REVISE 22 / FAIL 1 (worm-canon-pedant / interest-narrator).

---

## Per-facet aggregate (cycle 1)

| Facet | cape-fic | dark-fantasy | worm-canon / specialist | Aggregate |
|---|---|---|---|---|
| location-state | revise | revise | revise | **FAIL** |
| interest-narrator | revise | revise | fail | **FAIL** |
| sensory | revise (disambig) | revise (modality) | revise (old-state) | **FAIL** |
| state-updates | revise | revise | revise | **FAIL** |
| memory | accept | revise | revise | **FAIL** |
| feeling | accept | revise | accept | **FAIL** |
| metaphor | accept | revise | accept | **FAIL** |
| vibes | revise | revise | revise | **FAIL** |
| exposition | accept | revise | accept | **FAIL** |
| dialogue-coll | accept | revise | accept | **FAIL** |
| dialogue-taylor | revise | revise | revise | **FAIL** |
| dialogue-wren | accept | accept | accept | **ACCEPT** ✓ |

11 of 12 fail. Only `dialogue-wren-stitch-maker-flea-bottom-ward` passes 3-of-3.

---

## Headline findings (worth surfacing before fixer dispatch)

These four findings either escalate auditor SIGNALs to HARD-class consequence, or surface seams the Phase 5 mechanical scan did not reach. They are likely to drive cycle-2 reviewer attention even if the long-tail callouts below get fully remediated.

### H1. POTENTIAL EARTH-BET FENCE HIT — narrator:2 @9
- **Reviewer**: worm-canon-pedant (verdict: fail — the only FAIL of cycle 1)
- **Claim**: `narrator:2 @9` text contains *"a power that requires containing"*. "power" as a category noun is canon-Earth-Bet parahuman vocabulary (the noun Taylor uses to classify parahumans including herself).
- **Auditor convergence**: NONE. Auditor's Earth-Bet scan returned 0 hits because it was proper-noun only; the worm-canon-pedant escalates to vocabulary-category scope.
- **Disposition**: This is the only verdict in cycle 1 that exceeds REVISE. If confirmed as a hard-fence hit it is a HARD finding that the auditor's mechanical scan missed; if rejected as common-English-word it stays advisory. **Needs adjudication before fixer dispatch.**

### H2. Rubric Form-rule violation on NI semicolon-spine
- **Reviewer**: worm-canon-pedant
- **Claim**: rubric `design/shoot-v2/rubric-narrator-interest.md` §Form states "Single clause. No semicolon-spine." This makes 3 of 6 NI entries (narrator:3, narrator:6, narrator:7) direct rejections, not advisory saturation hits.
- **Auditor convergence**: partial. Auditor fault-014 flagged the same three entries under URI-AP-SCAN-SATURATION (50% > 40% threshold) and classified SIGNAL with escalation-candidate note. Cape-fic + dark-fantasy both flagged template-anticipation by narrator:7. If the rubric Form text is unambiguous, fault-014 should escalate to HARD per rubric direct-rejection rule.
- **Disposition**: needs rubric-text check. If confirmed, three entries require rewrite (single-clause form) — not just one.

### H3. Cite-graph state confusion between audit report and current cite-index
- **Reviewers**: worm-canon-pedant (location-state), sensory-disambiguation-pedant, sensory-old-state-reader
- **Symptom**: Multiple reviewers treat fault-001/002/003 as still-active because the audit report's WHAT fields describe pre-repair state (e.g. "loc-state:5 back=N"). The fixer landed the repairs and current `_cite-index.md` shows loc-state:5/6/7 back=Y, but the audit report text was not updated post-repair.
- **Disposition**: not a substantive fault in the artifacts — the cite-graph IS repaired — but it pollutes audience reasoning. Option: re-issue audit report with post-repair WHAT fields, OR add a post-repair status banner to `facets-final-audit.md`. The downstream effect is several REVISE callouts that hang off a fault that no longer exists.

### H4. state:10 value mismatch between audit report and on-disk
- **Reviewer**: worm-canon-pedant (state-updates)
- **Symptom**: Auditor fault-012 quotes `<new>` value as `flea-bottom-block-level-with-patrol-rotation`. On-disk reads `flea-bottom-block-level-day-count-complete`. The narrowing repair landed but the inline comment at state:10 still enumerates "watch-rotation geometry" as accumulated knowledge (per cape-fic).
- **Disposition**: fault-012 repair was field-only; inline comment still contradicts narrator:7's licensing scope. Either strip the watch-rotation reference from the comment, or expand narrator:7 to name patrol-rotation explicitly.

---

## Deduplicated callout register (by facet:id)

### location-state (3/3 REVISE → FAIL)
- `[loc-state:3] @6` — continuity-carry weak. Worm-canon: violates `rubric-location-state.md § Transition-run continuity license` (introduces NEW focus-element tallow-stall, not what persists from loc-state:1's baseline of building-entrance / building-keeper). Cape-fic + dark-fantasy: delivers smell with zero tactical/cost yield; "smell-note is not a tactical entry."
- `[loc-state:4] @11` — anchor verb "threads" in rubric REJECT dexterity-verb list; auditor defends on scene-open exception but rubric priority ordering between URI-FACETS-CYCLE-1 prohibition and scene-open exception is ambiguous.
- `[loc-state:5/6/7]` — reviewer (worm-canon) treats as still-corrupt per fault-003 (see H3 above; cite-index actually shows back=Y post-repair).
- `[loc-state:7] @22` — alley-mouth geometry correct, but scene-C approach zone shows Flea Bottom as set-dressing-for-Wren-entrance rather than place-with-own-operations-before-Wren (dark-fantasy).

### interest-narrator (2 REVISE + 1 FAIL → FAIL)
- `[narrator:2] @9` — **POTENTIAL EARTH-BET HIT** (H1 above). "power" as category noun.
- `[narrator:3] @13` — semicolon-pivot first instance; establishes chassis (worm-canon claims direct Form rule violation per H2; cape-fic + dark-fantasy escalate saturation concern).
- `[narrator:5] @24` — author-annotation language ("confirmed before she named it a radius") instead of interior-register-in-motion; doubled before-she-knew-it construction (dark-fantasy).
- `[narrator:6] @26` — semicolon-pivot; ALSO consumes inverted-predicate-cap twice in a single entry (dark-fantasy adversarial reading not flagged by auditor); structure arrives before the bleak content (the child saw what cape's read missed).
- `[narrator:7] @20` — semicolon-pivot; "nothing had been moved that needed not to be moved" reads as ledger-satisfaction not ledger-cost; comfortable competence (dark-fantasy); content-leak claiming patrol-rotation registration without specific acquisition beat (cape-fic).
- `[narrator:NI-gap] @23` — missing fire on Wren's first speech. Worm-canon: peer-children mask-thinning trigger per rubric §Earning ACCEPT signatures; dark-fantasy: approach-zone weight-accumulation failure.
- `[narrator:NI-gap] @25` — missing fire on Taylor's own spoken response; what is she suppressing while producing Westerosi-child voice (dark-fantasy)?

### sensory (3 specialist REVISE → FAIL)
- `[sensory:2] @12` — unanchored old-state "open-air-working-surface": loc-state:4 @11 names spatial position only, no tactile baseline. Baseline-invention.
- `[sensory:3] @14` — weakly-charged verb "cool" (announces thermal-event class) + unanchored thermal old-state ("stone-walls-midday-ambient" not in any prior loc-state).
- `[sensory:4] @17` — borderline-charged verb "strike" + unanchored auditory old-state + post-repair anchor confusion (no loc-state co-fire at @17).
- `[sensory:--] file` — modality distribution scene-inverted: scene-B 3/4 fires, scene-C (payload zone) 0/4. The chapter's heaviest dramatic beat carries zero perceptual inflection.
- `[sensory:--] file` — sparsity 14.8% (4/27) above 6% ceiling; V3 short-chapter exemption requires modality count == 2 (file has 4), so exemption does not engage. File header's "ADVISORY range" claim is unsupported by rubric.
- `[sensory:--] gap@2` — drain-channel: bare verb "crosses" + loc-state:2 establishes "wet stone gap, footing costs a stride's width"; tactile inflection earned, skipped.
- `[sensory:--] gap@13` — insects-fill-the-block: bare verb "fill" + narrator:3 co-fire; sound modality inflection (ambient onset vs midday baseline) earned, skipped.
- `[sensory:--] gap@22-29` — scene C: zero sensory fires across 8 bones; spatial constriction at @22 has tactile analog; payload @26 unbraced perceptually.

### state-updates (3/3 REVISE → FAIL)
- `[state:4] @18` — environmental-only entry on watch-pass beat; no actor-state on Taylor; world moved, protagonist absorbed nothing (dark-fantasy).
- `[state:9] @9` — `knowledge.ward-geometry` field name: "ward" double-register (Westerosi city-district + PRT Ward program). No documented disambiguation. Worm-canon: unmarked vocabulary collision → revise; either disambiguate or rename to `knowledge.block-geometry` / `knowledge.quarter-layout`.
- `[state:10] @20` — **H4 above**: inline comment enumerates "watch-rotation geometry" as accumulated knowledge feeding the @20 close; field value `day-count-complete` is clean but comment still claims patrol-rotation as filed (cape-fic + worm-canon converge on partial repair).
- `[state:3 env-entry-3] @7` — prop:oc-taylor-pack slug card-resolution unverified (fault-019 advisory; both cape-fic and dark-fantasy note the unresolved card).

### memory (1 ACCEPT + 2 REVISE → FAIL)
- `[memory:1] @9` — dark-fantasy: "is no longer doing" too mild to deliver scar; backfill not somatic load. Worm-canon: bare free-text gloss without margit-resolved card slug (URI-FACETS-CYCLE-1 licensing-discipline axis).
- `[memory:2] @16` — Worm-canon: "hands-as-labor-marker-vs-authority-instrument" Westerosi-primary does NOT map to any of the rubric's enumerated Westerosi-monument trigger-class patterns (Conquest-dating / Harrenhal / Dance succession-language / Faith-Militant / Doom / Northern-loyalty). Either reclassify as Earth-Bet primary (with Westerosi as atmospheric secondary, not clamp fire), or anchor to a named Planetos monument the @16 cue supports. Dark-fantasy: generic-craft meditation, no Planetos cultural signal surfaces; doubled-register requires Westerosi register to be reader-legible.

### feeling (2 ACCEPT + 1 REVISE → FAIL)
- `[feel:1] @9` — dark-fantasy: posture-not-cost ("sets both feet even" = default assessment stance); rides on feel:2's spine; borderline, not blocking on its own.
- `[feel:3] @26 (Wren)` — dark-fantasy: card §Look definition played back verbatim; type-confirmation, not chapter-payload-weight. The chapter's central blow needs a body to land on; Taylor @27's receipt (deleted feel:3 R2.3) is the missing half of the architecture the wren slice's PATTERN-SCAN line ~198 still describes as live (= fault-008 cosmetic consequence). The pair no longer exists; what remains is delivery without landing.

### metaphor (2 ACCEPT + 1 REVISE → FAIL)
- `[metaphor:--] file` — dark-fantasy: empty file is rubric-correct under AP7; but every figurative move in the chapter (mem:1 / mem:2 / narrator:6) runs through Taylor's Earth-Bet displacement frame. Planetos has zero figurative claim of its own. A single low-anchor figure at @6 or @15 (within 0-3% target) would have given Flea Bottom its own voice. The dark-fantasy attack is a taste-level world-grounding failure compatible with the rubric defense.

### vibes (3/3 REVISE → FAIL)
- `[vibes:2] @6` — **AP8 / AP13 formal sentence-parsability fail** (worm-canon + dark-fantasy converge). Token `beauty-requires-not-paying-attention-she-pays-attention` parses as two-clause compound: `she pays attention` carries standalone subject + finite verb. V1.1 Patch 2 explicit. Repair: noun-phrase compression (e.g. `attention-she-does-not-withhold`). Auditor missed it.
- `[vibes:2] @6` — cape-fic: shared-license padding. `state-update:2` (time-of-day null→morning) has zero informational bearing on king's-landing tallow-smoke vibe. Operative license is `proto:6` alone.
- `[vibes:5] @13` — dark-fantasy: `confirmed-on-screen-b01c01` is authoring provenance in the bias register; not operator-actionable. Replace with a durable behavioral disposition token.
- `[vibes:7] @26` — dark-fantasy: tokens `first-on-screen-naming-of-what-she-saw` + `the-flies-report-as-demonstration` are provenance-as-vibe; only `reported-before-interpreted` functions as bias-token; replace the provenance tokens.
- `[vibes:8] @26` — dark-fantasy: `the-follow-up-withheld-on-screen` is provenance-as-vibe; `first-confirmed-shape-of-the-mutual-silence` is the one viable token.
- `[vibes:9] @27` — dark-fantasy: `the-anomaly-confirmed-on-screen` is provenance-as-vibe; `holds-the-eyes-does-not-file` is the viable bias token. (cape-fic: fault-011 licensed-by confirmed repaired in current file; the worm-canon-pedant dialogue-taylor verdict assumed fault-011 still active — minor stale-read.)

### exposition (2 ACCEPT + 1 REVISE → FAIL)
- `[exposition:1] @1` — dark-fantasy: "no titles and no guild rolls, subsistence-class permanent" reads as sociological framing, not Planetos slum-physics. Revise to include one Planetos-specific institutional fact (Gold Cloak circuit / septon's absence / copper-star informal economy unique to this ward).
- `[exposition:2] @4` — dark-fantasy: simile earns its place as compression; gloss says fixture-not-confidant correctly but doesn't carry Westerosi-fixture register (relationship to Watch / building-keeper / lane-runner).
- `[exposition:5] @22` — dark-fantasy: "ward arrangement" needs the absence-cost clause (no house, no name, no next step) to be Planetos-specific rather than generic domestic-service.
- **ADD proposals (dark-fantasy)**: @2 drain-channel gloss; @6 tallow-stall gloss; @18 Gold Cloak institutional-weight gloss.
- **ADD proposal (cape-fic)**: @20 `the count` first-implicit-use gloss for Taylor's running insect-count instrument.

### dialogue-coll (2 ACCEPT + 1 REVISE → FAIL)
- `[coll:1] @8` — dark-fantasy: facet-license citation cross-anchor near-miss. Sidecar cites `exposition:2 @4` as facet-license; speech-act fires at @8; cross-bone citation ≠ co-fire-at-anchor per rubric CONSTRAINT § citation-completeness. The @8 bone has no co-located lens facets.
- `[coll:1] @8` — dark-fantasy: behavior card file absence at `cards/dialects/coll-net-mender-flea-bottom.card.md` per reviewer (NEEDS VERIFICATION — file may exist at differing path).
- `[coll:1] @8` — dark-fantasy: line carries no Planetos-specific weight; generic medieval-labor-offer NPC; fixture-not-confidant survival logic (silence-as-liability-management) absent from utterance surface.

### dialogue-taylor (3/3 REVISE → FAIL)
- `[taylor:2] @25` — **central seam (3-reviewer convergence)**: line clean on every mechanical axis; bare proto-line anchor with no co-located lens facets; sidecar offloads weight to NI:5 (@24 lonely entry, no co-load) + vibes:9 (@27); reader experiences dismissal of cost-bearer with zero adjacent texture.
  - cape-fic: structural claim "decision not reflex" not graph-supported (NI:5 lonely; vibes:9 fault-011 thought to still be HARD by this reviewer — actually repaired but the dependency on a previously-HARD entry remains a thin foundation).
  - dark-fantasy: flat refusal dressed as restraint; line costs Taylor nothing reader can feel.
  - worm-canon: Q1 §Voice citation rests on absence of idiom, but card defines voice-feature as positive ("accent wrong in a way no one can place"). Chosen draft A eliminates the tell; rejected draft B was closer to card's voice spec.
- `[taylor:2] @25` — worm-canon: sidecar R2 audit-notes claim "all three citations resolve" but vibes:9 carries fault-011 HARD (now repaired but stale at time of sidecar authoring); sidecar citation-integrity claim is false-clean.

### dialogue-wren (3/3 ACCEPT → ACCEPT ✓)
- No callouts. Only facet cleanly passing cycle 1.

---

## Audience-side ADD proposals (consolidated)

Dark-fantasy:
- exposition @2 — drain-channel as Flea-Bottom-specific infrastructure (hook-channels carry water + patrol routes).
- exposition @6 — tallow-stall as ward-without-guild-jurisdiction commerce; the smell as ward's main identifier.
- exposition @18 — Gold Cloak institutional weight (not name; operational reality — informal taxation / patrol-product / interest enforcement).

Cape-fic:
- exposition @20 — `the count` first-implicit-use gloss for Taylor's running insect-count instrument.

Worm-canon:
- exposition @9 — no ADD warranted; cluster (mem:1 + narrator:2 + feel:1 + vibes:3/4) already carries Earth-Bet-displacement register; ADD here would double lens-carried content (anti-pattern).

Per A3 cycle-N ADD pre-validation: any cycle-2 ADD must pre-validate against the relevant facet rubric before commit. Cycle 3 ADDs are structurally banned.

---

## Convergence trace (Phase 5 auditor ↔ Phase 5b audience)

- Auditor HARD findings (post-repair): 0 (fault-001/002/003/011/012 repaired).
- Auditor SIGNAL findings: 14 (fault-005/006/007/008/009/010/013/014/015/016/017/018/019; fault-004 episode-scope vibes:10 advisory).
- Audience callouts (deduped by [<facet>:<id>] or file-level): 36+ distinct.
- Shared findings (auditor + audience both flagged the same entry/seam):
  - fault-008 (wren PATTERN-SCAN stale ref to deleted feel:3 @27) — confirmed by cape-fic + dark-fantasy + worm-canon on feeling.
  - fault-014 (NI semicolon saturation) — confirmed by all three NI reviewers; worm-canon escalates to direct Form-rule failure (H2).
  - fault-016 (scene-C approach thin @22-25) — confirmed by cape-fic + dark-fantasy on NI / metaphor / state-updates / dialogue-taylor / sensory; structural impact wider than auditor's TASTE-FLAG framing.
  - fault-013 (exposition:1 cape-fic attestation form gap) — confirmed advisory.
  - fault-012 (state:10 NI content-alignment) — partial: field-only repair landed; inline comment still mis-enumerates (H4).
- Audience-only findings:
  - H1 narrator:2 "power" potential category-noun fence hit.
  - H2 rubric Form-rule (vs. saturation-only) interpretation of semicolon-spine.
  - vibes:2 AP8 / AP13 formal sentence-parsability failure (`she pays attention` standalone clause inside hyphen-token).
  - sensory:2/3/4 unanchored old-states.
  - sensory file-level scene-inverted modality distribution + V3 exemption non-engagement (4 modalities).
  - state:9 `ward-geometry` double-register collision.
  - memory:2 Westerosi-monument forced-fit (not in rubric trigger list).
  - metaphor file-level world-grounding gap (Planetos has no figurative claim of its own).
  - vibes:5/7/8/9 provenance-as-vibe token-quality failures.
  - dialogue-coll:1 facet-license cross-anchor near-miss.
  - dialogue-taylor:2 bare-anchor with weight-offloaded-to-adjacent-bones.
  - dialogue-taylor:2 §Voice citation rests on absence not presence (kl-122ac wrong-accent tell missing).
- Auditor-only findings the audience did not surface independently:
  - fault-005 (memory 7.4% sparsity) — accepted by cape-fic + worm-canon-pedant; flagged by dark-fantasy as weight-failure not density-failure.
  - fault-006 (feeling 7.4% sparsity) — accepted by cape-fic + worm-canon; flagged by dark-fantasy on architecture-incomplete grounds.
  - fault-007 (loc-state 25.9% density) — none of the three reviewers attacked density directly; the loc-state failure is qualitative (loc-state:3 carry-license + loc-state:7 set-dressing), not quantitative.
  - fault-009 (vibes:7/8 wren split DEDUP advisory) — cape-fic confirms split holds; dark-fantasy attacks token-quality not split-redundancy.

**Bidirectional loop verdict: VALIDATED.** Multiple shared findings across both paths; audience surfaces 11+ additional findings the mechanical scan structurally cannot reach (rubric-text-level Form rule reading, taste-level world-grounding, license-citation cross-anchor analysis, voice-feature affirmative vs absence interpretation).

---

## Stall / underdmanned-facet incidents

None. All 36 dispatches returned verdicts within the agent watchdog window. No URI-AUDIENCE-CYCLE-2-MEMORY-STALL events fired (this is cycle 1; payload sizes were full).

---

## Remediation routing (for cycle 2 fixer dispatch)

The volume + breadth of cycle-1 revises is broad. Per `.claude/commands/and-facets.md` § Remediation cycle, the next action is dispatch fixer with consolidated callouts + facet rubrics. Cycle-N ADD pre-validation rules (URI-FACETS-CYCLE-N-ADD A3) apply. Cap-burn discipline: prior c01 run cap-burned at cycle 3 on the now-redone bone set; budget cycle 2 deliberately.

**Recommended ordering for fixer dispatch** (heaviest-impact / clearest path first):

1. **H1 first (potential Earth-Bet hit narrator:2 "power")** — adjudicate before committing fixer to broader rewrite. If confirmed, NI rewrites must remove "power" as well.
2. **H2 (rubric Form rule on NI semicolon)** — rubric-text check determines whether narrator:3/6/7 require rewrite (Form failure) or count-reduction (saturation). Drives scope of NI repair.
3. **H3 (audit report cite-graph state drift)** — update audit report WHAT fields post-repair OR add status banner. This unblocks several reviewers' downstream readings on next cycle.
4. **H4 (state:10 inline comment)** — strip watch-rotation from comment OR expand narrator:7 text.
5. **vibes:2 AP8 token rewrite** — clear formal-gate failure; noun-phrase compression.
6. **sensory:2/3/4 old-state lineage** — derive from actual prior loc-state OR loc-state entries authored at @11/@14/@17 to provide the baseline.
7. **memory:2 Westerosi-monument anchor** — reclassify as Earth-Bet primary OR add Planetos monument anchor.
8. **state:9 ward-geometry disambiguation** OR field-rename.
9. **dialogue-taylor:2 approach-zone cost-tell** — fractional interior register insertion (NI:5 strengthening at @24, or new NI fire at @25).
10. **dialogue-coll:1 facet-license** — either add a co-located lens fire at @8, or correct citation.
11. **loc-state:3 carry-note** — rewrite to name what persists from loc-state:1 baseline, OR reclassify as standard state-change entry.
12. **exposition Planetos-specific institutional facts** — three rewrites + audience-side ADDs.
13. **vibes provenance-token rewrites** (vibes:5/7/8/9) — replace authoring-provenance tokens with operator-bias tokens.
14. **fault-008 wren PATTERN-SCAN** — update commentary to note @27 deletion (auditor criteria, not closed yet).

Cycle-2 reviewer set: re-fire all 11 failing facets. dialogue-wren passes; does not re-fire.

---

## Output to disk (cycle 1)

- Per-reviewer verdict files: `active-project/staff/audience/<persona-slug>/<facet>-r1-verdict.md` × 36.
- Consolidated report: this file (`active-project/staff/auditor/facets-audience-gate-r1.md`).
- Showrunner-memory status: `audited-r1-mechanical` retained; `audience_gate_cycle: 1`; `audience_gate_complete: false`.

Phase 6 persistence gate is NOT met (cycle 1 did not pass). Cycle 2 required.
