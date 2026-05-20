# Run postmortem — output vs. intent (b01c01 end-to-end)

Date: 2026-05-20
Auditor: postmortem-fork
Scope: the FIRST end-to-end run through chapter b01c01 of `taylor-westeros-good-intentions`.
Chain executed: `/and-project` → `/and-series` → `/and-substance series` → `/and-cast` → `/and-substance book b01` → `/and-substance chapter b01c01` → `/and-write b01c01` → `/and-facets b01c01` → `/and-stitch b01c01`.

For each command: (i) intended output (per `.claude/commands/<name>.md` description), (ii) actual artifact paths, (iii) schema conformance, (iv) content-vs-purpose, (v) gaps / deviations.

---

## 1. `/and-project taylor-westeros-good-intentions ...`

**Intended (per `.claude/commands/and-project.md` line 2):** "Activate a new and-shoot project. Scaffolds `active-project/`, binds staff personas + audience trio + orchestrator-critic version, runs boundary-scope + taste-judge forks, runs world-building (1a-1d)."

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/` directory tree present with `actors/`, `audience/`, `staff/{showrunner,studio,auditor,fixer,margit,screen-writer,editor,stitcher,...}/`, `warehouse/`, `theater/`, `draft/`.
- `/home/user/and-shoot/active-project/staff/showrunner/boundary-scope.md` (95 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/world-notes.md` (59 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/prompt-binding.md` (59 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/taste-selection.md` (18 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/brief-expansion.md`, `open-questions.md`, `1b-{audience,dramatist}-review.md`, `1b-log.md`.
- `/home/user/and-shoot/active-project/audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/`.
- Staff bindings in `active-project/staff/showrunner/memory.md` lines 25-31 (`audience`, `screen_writer`, `dramatist`, `auditor`, `editor`, `orchestrator_critic: v1.3`).

**Schema conformance:** No schema directly governs the project scaffold; `boundary-scope.md` follows the in-command template (BOUNDARIES / OPEN PARAMETERS / STORY TYPE / CHARACTER ARCHETYPES sections all populated). `memory.md:1-37` populates `project.brief`, `project.constraints.{settings,themes_as_bounds,hard_fences}`, and `project.staff.*` per `schemas/showrunner-memory.schema.md`.

**Content-vs-purpose:** Strong. Boundary-scope explicitly enumerates HIGH/MEDIUM-confidence boundaries vs. OPEN parameters; world-notes carries 1b resolutions (Taylor power-state, arrival, year 122 AC, social entry point, end-locus="both"). Audience trio + staff bound; orchestrator-critic v1.3 pinned. Taste-judge selected story-type (slow-prevention-tragedy) + 9 archetype picks (`prompt-binding.md:21-34`).

**Gaps / deviations:**
- `world-notes.md:48-50` still names "Lucerys" + "Nessa" as load-bearing in 1b resolutions even though `/and-series` later stripped them to class-slots (`series-log.md:14-15` documents this as an unresolved upstream cleanup). Minor staleness — flagged but unfixed.
- **Name-leak vector confirmed (CLAUDE.md OOS item):** `boundary-scope.md:58` lists "mira-stonefield archetype" as the foil reference; this is also flagged in CLAUDE.md as the documented name-leak path. No actual `mira-*` slug shows up in `actors/`, but the contamination vector is live in the scaffold.

---

## 2. `/and-series`

**Intended (`.claude/commands/and-series.md` line 2):** "Author the series chunk + structural commitments. Phase 1 collects seven structural prompts. Phase 1.5 designs the premise — gap-detect, brainstorm 6 candidate paths via 6 lenses, user picks/mutates, expand to trajectory."

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/staff/showrunner/series-plan.md` (111 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/series-log.md` (18 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/series-trajectory.md` (312 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/series-gap-report.md` (123 lines).
- Persisted to `memory.md` at `series.chunk` (lines 39-53) + `series.structure` (54-66) + `series.{laws,lore,behaviors}` (67-82).

**Schema conformance:** `series.chunk` carries the structured object (`path.{motivation,anchor,escalation,trade,irony}` + `trajectory.source` + `lens_used`) per schema; legacy `prose` field correctly retired per note at `memory.md:52`. `series.structure.*` fields populated (book_count, chapter/scene/bone ranges, cyclical, pov, world_evolution, series_end_shape).

**Content-vs-purpose:** Strong. `series-plan.md` shows 6-path brainstorm (round 1, six lenses); user picked path-4 and mutated to composed path-4+path-2+contempt layer (`series-log.md:6`). Trajectory expanded across 7 axes × 14 deltas (`series-trajectory.md` enumerates d01-d14 with start/end states per axis). All three audience reviewers ACCEPT/ACCEPT; dramatist ACCEPT; naive-reader 4/5.

**Gaps / deviations:**
- `path-6` body landed mid-stream and had to be restored under `Round-1 path-6 body (restored — was displaced by append above)` (`series-plan.md:102-111`). Authorial ordering glitch; recovered.
- `series-log.md:14-18` flags three downstream follow-ons that were never executed (upstream `/and-project revise` for stale Nessa/Lucerys names; `cond-nessa-scene-frequency` rename — done in part, see `warehouse/cond-cost-bearer-scene-frequency.md`; d08 chapter-substance trigger flag; naive-reader Q5 hook-gap carry).

---

## 3. `/and-substance series`

**Intended (`.claude/commands/and-substance.md` line 2):** Recursive chunker; at series level "authors the signature" (state axes + cost ledger + antagonist pressure + chunk_targets) + per-book Δ + book chunks.

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/staff/showrunner/signature-draft.md` (384 lines) — explicitly marked `# SUPERSEDED — 2026-05-18` at file head (lines 1-8) with redirect to `memory.md → series.substance.cost_ledger` as canonical.
- Persisted: `memory.md` `series.substance.state_axes[]` (line 84 onward; 27 entries = 9 axes × 3 perspectives), plus `series.substance.cost_ledger`, `antagonist_pressure`, `chunk_targets`, and per-book Δ.
- `memory.md` `books[b01]` chunk + per-chapter Δ populated.

**Schema conformance:** State axes carry `slug / dimension / one_means / five_means / nine_means / perspective / start_rank / end_rank / class` per the substance plan (`design/substance/plan.md`). Cost-ledger anchors resolvable; ledger id `cl-intelligence-arrangement` is canonical (signature-draft.md uses the abandoned `cl-knowledge-contempt`; the superseded notice at signature-draft.md:7-8 is correctly authored).

**Content-vs-purpose:** Strong. 9-axis signature × 3 perspectives all present in memory; reviewers fired per `staff/reviews/series-signature-*` (cape-fic, dark-fantasy, worm-canon-pedant + dramatist + audit) across two passes.

**Gaps / deviations:**
- `signature-draft.md` is a 384-line intermediate file that should arguably have been pruned at persist time rather than left in active-project; in practice the SUPERSEDED notice + memory-as-canonical pointer mitigates this, but a downstream agent reading the file naively could anchor bones at the wrong cost-ledger id.

---

## 4. `/and-cast`

**Intended (`.claude/commands/and-cast.md` line 2):** "Compose the substance-driven cast roster + fire the series-level audit checkpoint (the only blocking human checkpoint in the chain)." Phase 1 brief; Phase 2 candidate menu; Phase 3 selection + dramatist viability; Phase 4 margit provisioning; Phase 5 audit checkpoint.

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/staff/showrunner/cast-brief.md` (178 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/cast-candidate-menu.md` (446 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/cast-selection.md` (259 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/cast-dramatist-review.md` (180 lines).
- `/home/user/and-shoot/active-project/staff/showrunner/cast-provisioning-log.md` (155 lines).
- `/home/user/and-shoot/active-project/staff/reviews/series-audit-2026-05-18T120000Z.md` — series-audit report; user-approved at 2026-05-18T123000Z (`memory.md:32-36`).
- 8 actor directories provisioned in `active-project/actors/` (taylor, otto, aemond-122ac, wren, sera-122ac, gylda, coll, corvan).

**Schema conformance:** Actor directories carry `card.md + ltm.md + stm.md + state.md + vibes.md` per `schemas/memory.schema.md` (per `cast-provisioning-log.md:10-18` description). Series-audit fields populated in `memory.md:32-36` (`approved_at`, `approved_by: user`, `report_path`, `stale_since: ~`).

**Content-vs-purpose:** Strong. Cast resolves both `[cost-bearer]` (wren) and `[protect-target]` (sera-hightower-kl-122ac) deferred-slots from `/and-series`. Dramatic-range review at `cast-selection.md:113-152` confirms every state-axis has at least one on-stage carrier; no axis-orphans; cost-bearer + protect-target pair structurally complementary (independent non-resolving vulnerabilities). 9 axes mapped to carriers explicitly.

**Gaps / deviations:**
- `cast-selection.md:117` references a "9th axis" (`agency`) and `knowledge` axis as carriers in the table though `memory.md`'s state_axes enumerates 9 axes — the trajectory has 7 axes per `series-trajectory.md:1` ("lens: penitential + political") but `memory.md` substance has 9 axes (moral-framework, capability, position, social-tether, relational-anchor-status, moral-legibility-to-self, political-register-toward-elite, knowledge, agency). The 7-vs-9 disjoint between `series.chunk.trajectory` (7 axes) and `series.substance.state_axes` (9) is internally surfaced but not flagged.
- Cast-provisioning-log states all 8 actors provisioned; only 3 appear in the on-stage chapter 1 cast (`taylor`, `coll`, `wren`). This is intended per per-chapter on-stage selection, but `otto`, `aemond`, `sera`, `gylda`, `corvan` actor dirs have no usage in this run — accumulated state remains untouched (expected, not a fault).

---

## 5. `/and-substance book b01`

**Intended (`.claude/commands/and-substance.md` lines 65, 38, 116):** At book level — "Author one chunk per chapter (`chapters[1..chapter_count]`). Each chunk is one paragraph naming the chapter's local collision and what shifts. Honors book drama and POV pattern." Also populates `handoff_in/out` between adjacent chapters.

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/staff/showrunner/b01-draft.md` (1057 lines) — book-substance draft.
- Persisted: `memory.md` `books[b01].{chunk, substance_delta, drama, chapters[]}` populated. Chapter b01c01 and downstream chapters (b01c02, …) chunks present in `memory.md` (`memory.md:794`+ shows b01c02 chunk).
- Reviews: `staff/reviews/substance-b01-{audience,audit,dramatist}-2026-05-18*.md` (3 audience + 1 audit + 1 dramatist + pass-2 retries).

**Schema conformance:** `chapters[<slug>].chunk` populated per schema; `substance_delta.axes_in_motion[]` for each chapter; `handoff_in/out` (mirror-check pairs per dramatist Phase 5) present.

**Content-vs-purpose:** Strong. Each chapter chunk names local collision (e.g. b01c02 = "Danger moves through Flea Bottom in the form of a pressed-labor sweep — Taylor uses insect-sense to locate and pull Wren clear..."), with substance_delta per the cost-ledger. Audit + 3-of-3 audience passes recorded.

**Gaps / deviations:**
- `b01-draft.md` is a 1057-line working file that should have been distilled/pruned post-persist; same pattern as `signature-draft.md`. Not faulty per schema but leaves intermediate drafts in active-project.

---

## 6. `/and-substance chapter b01c01`

**Intended (`.claude/commands/and-substance.md` line 66):** "Author one chunk per scene (`scenes[1..scene_count]`). Each chunk is substantial — scenes typically fill most of a chapter. Each names the scene's collision shape (without explicitly stating per-bone Δ)." Plus per-scene `substance_delta`, `scene_conflict`; chapter-level `pov_narrator`, `dramatic_shape`, `goal`.

**Actual artifact paths:**
- Persisted in `memory.md` lines 469-789:
  - `chapters[b01c01].pov_narrator` (line 553) = `taylor-hebert-kl-122ac`.
  - `chapters[b01c01].dramatic_shape` (554) = `hinge`.
  - `chapters[b01c01].goal` (555) = "the operating rule in its intact form, the ward it will fail to protect, and the child who will pay the price of its failure."
  - 3 scenes (`b01c01s01`, `s02`, `s03`) each with `chunk`, `substance_delta.axes_in_motion`, `density_target`, `scene_conflict.{protagonist_force, opposing_force, stakes_axis}`.
- Per-scene `chunk` is a substantive paragraph (lines 558-559, 634-635, 719-720).
- Reviews: `staff/reviews/substance-b01c01-{audience,audit,dramatist}-2026-05-18.md`.

**Schema conformance:** Per `schemas/showrunner-memory.schema.md`: `scenes[]` carry `slug`, `chunk`, `substance_delta`, `scene_conflict`; chapter-level fields `pov_narrator`, `dramatic_shape`, `goal` all present. Required per `/and-write` Phase 0 validation (and-write.md:46-47).

**Content-vs-purpose:** Strong. Each scene chunk articulates its local collision; scene_conflict cleanly names protagonist_force vs. opposing_force. The `goal` is concrete enough to anchor Phase 4 trim (and-write.md:163). The dramatic_shape `hinge` is defended in-line ("chapter 1 of 18 in tragedy; load-bearing baseline...") — dramatist-reviewed per the inline comment.

**Gaps / deviations:**
- Scene-2 substance contract carries a SIGNAL-002 advisory (line 721) about explicit "Khepri" naming in interior monologue colliding with the chapter chunk's "Khepri-haunted without naming Khepri" register; classified SIGNAL because the discipline lives in chunk prose rather than `project.constraints.hard_fences`. Routed to `/and-write` for bone-level smoothing. The bone author resolved it (no Khepri in bones), but the constraint-source discipline mismatch points to a gap between chunk-prose-as-rule vs. hard-fence-as-rule.

---

## 7. `/and-write b01c01`

**Intended (`.claude/commands/and-write.md` line 5):** "Reads scene chunks + substance contracts produced by `/and-substance chapter`. Decomposes each scene into bones-with-deltas, then SVOs them. Produces the per-chapter flattened bones file at `theater/bones/<book>-<chapter>.md` + the scene-map facet at `theater/facets/scene-map-<book>-<chapter>.md`."

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/theater/bones/b01-c01.md` (41 lines).
- `/home/user/and-shoot/active-project/theater/facets/scene-map-b01-c01.md` (37 lines).
- Per-scene authoring intermediates: `staff/screen-writer/write-b01c01-s01-bones.md`, `s02-bones.md`, `s03-bones.md`, `b01c01-scene-draft.md`, `write-b01c01-bridges.md`.
- Auditor reports: `staff/auditor/write-b01c01-pass2.md` (constraint), `write-b01c01-pass5.md` (continuity), `write-b01c01-bone-gate.md` (Phase 6 substance gate).
- Per-bone `substance_delta` persisted in `memory.md` `chapters[b01c01].scenes[].bones[]` (lines 569-788) — every bone carries `axis_moves[]` + `cost_ledger_anchor`.

**Schema conformance (bones file vs. `schemas/bones.schema.md`):**
- Header: all 7 fields present (`episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`). PASS.
- `aggregate_range: 1-29` correctly reflects max flat_id (bones.schema.md line 41 `aggregate_range: 1-<N>`). PASS.
- Body is plain SVO, no markdown bullets, no scene markers, no facet pre-tags, no per-bone substance annotations. PASS.
- Time-skip blank-numbered lines at `10` and `21` per schema lines 82-84. PASS.
- Speech bones use `<speaker> speaks to <listener>` form (lines 18, 23, 25, 26, 35, 37, 38). PASS.
- `holds` license: used at @9 ("holds the feet"), @19 / @27 ("holds the eyes") — narrow license per schema line 103 (body part of subject = stillness-against-pressure). PASS.
- No copulas, negations, conjunctions, perception verbs visible in body. PASS.
- Citation brackets: absent — correct per schema line 117 ("citations accrue at facet-authoring time, not at bone-extraction time"). PASS.

**Schema conformance (scene-map vs. `schemas/scene-map.schema.md`):**
- Frontmatter: `scene-map`, `generated`, `source`, `emitted-by`, `total-scenes`, `total-bones` all present. PASS.
- Per-scene block: `<scene-label> @<start>-@<end> | <location-slug> | <time-of-day> | <one-line>` shape per scene; `rhythm-shape`, `peak-bones`, `peak-shadow-bones`, `fusion-eligible-runs`, `protected-patterns` indented. PASS.
- Coverage footer: `coverage: 27/27 bones in exactly one scene`; gaps empty; overlaps empty. PASS.
- **Anomaly:** scene-map frontmatter declares `total-bones: 27` (lines 6, 36), but the bones file's `aggregate_range: 1-29` and 27 live bones + 2 time-skip blank-numbered lines (10, 21) = 29 flat_ids; the scene-map correctly counts only the 27 SVO bones. Internally consistent with schema lines 87, 141 (frontmatter total-bones = live bones, not max flat_id).
- An extra `time-skip markers:` block (lines 30-32) was added between the scene blocks and the coverage footer. Not in the canonical schema body but documentary-only; arguably a useful annotation. Schema does not forbid it.

**Content-vs-purpose:**
- Scene-decomposition matches scene chunks: s01 = arrival + Coll-registration; s02 = working-day rhythm + watch passes; s03 = Wren entry + assessment-and-catch. Maps cleanly to the chapter `goal` (operating rule intact / ward / child).
- Per-bone `substance_delta` (in memory) every bone has at least one `axis_moves` entry; "stillness-against-pressure" bones (e.g. b01c01s01n10 "holds the feet" line 626-631) carry capability=null magnitude=0 with "discipline enacted, not just stated" rationale — the substance bone-gate intent.
- `dramatic_shape: hinge` + chapter `goal` are visible in the bones header.
- Phase 4 audience trim deleted 3 bones (b01c01s01n03, s01n11, s03n09; comments at lines 585-589, 742-744) per 2-of-3 vote; slugs preserved in skip, no renumbering. Schema-compliant.

**Gaps / deviations:**
- Bones file uses lowercase actor slugs (`taylor-hebert-kl-122ac`, etc.) per convention — correct.
- The `time-skip markers:` annotation block between scenes (line 30-32 of scene-map) is not in the schema's documented structure (the schema places only `rhythm-shape` / `peak-bones` / etc. under each scene block, then the coverage footer); harmless but technically extra-schema.
- All three scenes share `rhythm-shape: flat-low` with `peak-bones: none` — flagged downstream in facets `state-updates.md:33-37` as the "0 peak-bones" cap-collision (structurally limits NI fires to 22.2% near band ceiling). Substance-correct (the chapter IS rule-intact, baseline-establishing), but a downstream stress in the facet-band arithmetic.

---

## 8. `/and-facets b01c01`

**Intended (`.claude/commands/and-facets.md` line 2):** "Unified facet pipeline for one chapter. Single command, six phases — R1 fanout → R1 fanin → R2 fanout → R2 fanin → audit (mechanical) → audience-gate (adversarial, blocking). Tensometer dropped; scene-map upstream-emitted; Phase 4d validates (not derives). Output: `active-project/theater/facets/` + `active-project/theater/dialogue/` + audit report + audience-gate verdict."

**Actual artifact paths:**
- Canonical facet files at `/home/user/and-shoot/active-project/theater/facets/`:
  - `interest-narrator.md` (19), `memory.md` (16), `feeling.md` (67), `metaphor.md` (57), `sensory.md` (23), `vibes.md` (54), `state-updates.md` (151), `exposition-b01-c01.md` (67), `location-state.md` (14), `scene-map-b01-c01.md` (37; upstream from `/and-write` — kept here for `/and-facets` consumption).
  - Per-character feeling/state-update slices (`feeling-{coll,taylor,wren}.md`, `state-updates-{env,taylor,wren,coll}.md`).
  - `_cite-index.md` (129 lines).
  - `_inflight/` + `_inflight-r2/` working dirs preserved (8-9 files each).
- Per-character dialogue files at `/home/user/and-shoot/active-project/theater/dialogue/`:
  - `taylor-hebert-kl-122ac.md` (1 entry @25), `coll-net-mender-flea-bottom.md` (1 entry @8), `wren-stitch-maker-flea-bottom-ward.md` (2 entries @23, @26). Coverage of all 4 speech bones (@8, @23, @25, @26). PASS URI-DIALOGUE-COVERAGE-GATE.
- Audit reports under `staff/auditor/`: `facets-final-audit.md`, `-r2.md`, `-r3.md`, `-r2-verify.md`, `cycle2.md`, `cycle2-re-audit.md`, `cycle3-closure.md`; `facets-audience-gate-r1.md`, `facets-audience-gate-r3.md`.
- Orchestrator-critic verdict: `staff/showrunner/and-facets-b01c01-summary.md` (82 lines).

**Schema conformance:**
- Facet files mostly conform to `schemas/facet.schema.md`: each line `<id> @<flat_id> <content>` per facet type; frontmatter present.
- **Sensory.md (23 lines, 1 live entry only):** `sensory:1 @3` light entry present; `sensory:2` and `sensory:3` are commented-out delete records (lines 10-23). Schema-clean (deletes leave ID gaps).
- **Memory.md (16 lines, 1 live entry):** `mem:1` deleted under user directive (lines 6-15); `mem:2 @18` is the sole live entry. Modality-coverage shortfall flagged by audience-gate; status `audited-r1-mechanical`.
- **Feeling.md (67 lines, 3 live entries across 2 characters):** consolidated frontmatter with per-source slices per schema; coll explicitly zero-fire (refused) with rationale.
- **Metaphor.md (57 lines, 0 live entries):** zero-fire refusal documented; AP1 (no upstream anchor since prior_episode=none) is the rationale.
- **Exposition-b01-c01.md (67 lines, 5 live entries; IDs 1,2,3,6,8 — gaps 4,5,7 from R2 deletions):** per-anchor-cap discipline followed; `@0` synthetic anchor for episode-open-preamble; `licensed-by:` populated per schema line 203. PASS.
- **Vibes.md (54 lines, 22 entries):** `+` / `++` ops per schema; `licensed-by:` mandatory + present on every entry; entity-target-primary form. PASS.
- **State-updates.md (151 lines, 22 entries) + slices:** large embedded `# rubric-carve-out` comments (lines 7-37, 71-101, 114-139) document POV-co-citation defense; schema-permissible (comments).
- **Location-state.md (14 lines, 4 live entries; loc-state:3 deleted F-007):** `<loc> | <time> | <weather> | <conditions> | <sensory note>` shape per schema. PASS.
- **Dialogue files:** `character:`, `episode:`, `behavior-card:` header; `<id> @<flat_id> | <objective> | <utterance>` body. PASS `schemas/dialogue.schema.md`.

**Content-vs-purpose:**
- Facet citations to bone flat_ids resolve (anchors @1-@29 with gaps @10, @21 for time-skips).
- Cite-index reports 67 facet entries; 25/27 bones decorated (92.6%). 2 bare bones (likely @5 + @14 or @28/@29 per density distribution).
- R1 → R2 deltas: KEEP-all-R1; 0 ADD / 0 DELETE (per summary line 18). R2 essentially confirmed R1.
- Audit (Phase 5) cycle 1 = 6 HARD + 15 SIGNAL; cycle 3 closure = 0 HARD; remediation cycles = 2.

**Gaps / deviations (significant):**
- **`audience_gate_cap_burned: true`** — `/and-facets` ran 3 / 3 cycles and never converged to 3-of-3 ACCEPT on `sensory` (modality floor reopened after sensory:3 deletion) and `memory` (mem:1 feel-as-spine defense rejected by all 3 reviewers uniformly across cycles 1+2). Per the critic card hot-button: "Cap-burn is a NOT-SUCCESSFUL verdict, not a 'ship anyway' license."
- Status remains `audited-r1-mechanical` (NOT advanced to `audited-r1`). Per `/and-facets` Phase 0 state-machine (`and-facets.md:85-87`), this should block `/and-stitch`. The stitcher still ran (see §9) — escalation accepted by user per orchestrator-critic recommendation.
- **Five process gaps captured** in the orchestrator-critic verdict for upstream tuning (R2 stale-shard cross-session protocol; cite-index pragma carve-out; modality-floor vs sparsity-band arithmetic collision; memory rubric feel-as-spine carve-out; cycle-N fixer adds introducing new findings).
- Co-existing canonical-vs-slice files (`feeling.md` + `feeling-{coll,taylor,wren}.md`; `state-updates.md` + `state-updates-{env,taylor,wren,coll}.md`) — schema is silent on per-source slice files but the cite-index notes "consolidated by build_cite_index from per-source slices." Functional, but the slice-file pattern is not documented in `schemas/facet.schema.md`.
- `_inflight/` + `_inflight-r2/` working directories left behind in `theater/facets/`. The orchestrator could have pruned them post-Phase-4; the rerun-protocol does not require it but they're noise.
- Stale-citation cleanup: render-log (`render-log-b01-c01.md:18-19`) notes the cite-index still references stale `sensory:2`, `sensory:3`, `mem:1` — "expected; excluded from scope per prior audit dispatch + rejected-items fixer." So the cite-index is non-fresh on disk.

---

## 9. `/and-stitch b01c01`

**Intended (`.claude/commands/and-stitch.md` line 2):** "Stitcher pipeline for one chapter. Eight phases — lens-anchored render → redundancy cull → compression → voice transform → local flow (speaker-paragraph breaks) → buildup preservation → editorial reflection → finalize (strips scene-callout markers). Output - `draft/<book>-<chapter>.md` + `draft/<book>-<chapter>.annotated.md` + `staff/stitcher/render-log-<book>-<chapter>.md`."

**Actual artifact paths:**
- `/home/user/and-shoot/active-project/draft/b01-c01.md` (29 lines — clean draft).
- `/home/user/and-shoot/active-project/draft/b01-c01.annotated.md` (92 lines — traced).
- `/home/user/and-shoot/active-project/staff/stitcher/render-log-b01-c01.md` (per ls; 100+ lines read).
- Annotated draft uses `[L1]..[L22]` stable line-IDs with `<trace>` blocks per line documenting source bones, facets, lens, phase-7 edits.

**Schema conformance:**
- Clean draft `b01-c01.md` carries no scene markers, no `## Scene N` headers, no `[SCENE BREAK]` lines. PASS Phase 8 strip discipline (and-stitch.md:11). Italic preamble (2 paragraphs) + horizontal rule + body. PASS.
- Annotated `b01-c01.annotated.md` carries header comments + `[L<n>]` IDs + `<trace>` blocks (no schema authority for the annotated format; the command body specifies its shape and the file matches).
- Speaker-paragraph rule (and-stitch.md:10): every `speaks to` bone's rendered dialogue paragraph starts a new paragraph (L8, L17, L18, L19 — Coll, Wren, Taylor, Wren utterances each isolated). PASS.

**Content-vs-purpose:**
- Bones realized: the 27 SVO bones all surface in the 22-line clean draft via fusion/compression (e.g. L10 = "I lifted the basket and Coll pulled the net; I threaded the needle, and the needle crossed the mesh" = bones @11+@12+@13+@14 fused under `fusion-eligible-runs @11-@20` license from scene-map).
- Facets realized: exposition preamble (L1, L2 = exposition:1, :2), inline-appositives for Coll (L5 = exposition:3 @4), the-Hook (L14 = exposition:6 @18), Wren (L16 = exposition:8 @22); sensory:1 light delta at L4; loc-state at L3+L4+L14+L16; NI fires at L5, L7, L11, L14, L16, L20; feel fires at L9 (taylor), L20 (taylor + wren); dialogue verbatim at L8, L17, L18, L19. Voice-transform (third-to-first, present-to-past) executed.
- Lens discipline: annotated file documents lens chosen per line (NI-leads / sensory + loc-state co-anchor fold / bone-only / dialogue-verbatim / feel-leads).
- Phase-7 edits documented with cause-codes (CUT-CLAUSE, KEEP, REWORD).

**Gaps / deviations:**
- **FAULT-AUDIT-MISS surfaces in the annotated draft (rendered as-is):**
  - L5 `<trace>` notes `FAULT-EXPOSITION-AUDIT-MISS (S3 Q6 borderline)` + `FAULT-AUDIT-MISS` on sensory:1 + narrator:1 ("wall-bottom" / "eye-lift" Q9-hit on facet content).
  - L11 `<trace>` notes `FAULT-AUDIT-MISS-S2-passive-held` ("passive held" verbatim from NI facet @15 — Q9 state-verb-fragment register hit; "upstream auditor should have caught at NI authoring").
  These are flagged not blocked — the stitcher rendered as-is and surfaced them for upstream auditor follow-up. Indicates upstream `/and-facets` audit missed Q9-class register hits on facet content.
- **Persona is `neutral`** (render-log line 7) — `/and-stitch` Phase 0 step 4 (`and-stitch.md:99`) warns that silent `neutral` against a tuned project is "the canonical failure mode for this pipeline." No project-scoped persona card exists in `active-project/staff/stitcher/personas/` (the dir does not appear to exist; only `render-log-b01-c01.md` was found in `staff/stitcher/`). The schema-default `neutral` was used because the project does not have a tuned persona card; this is consistent with the polish-deferred boundary but means voice-bias work is not happening.
- **Pre-flight succeeded despite `/and-facets` cap-burn.** The render-log Phase 0 (lines 17-26) and Phase 0.7 confirm URI-DIALOGUE-COVERAGE-GATE PASS; the cite-index staleness (sensory:2, sensory:3, mem:1) was acknowledged at line 19 and excluded from scope. The stitcher proceeded because the bone-facet citations the stitcher reads in body do not include the deleted IDs.
- **Profile resolution defaulted to schema.** Render-log line 6 = "profile: schema defaults (no episode/project profile authored)" — no `active-project/theater/stitch-profile.md` exists. The chain runs entirely on the schema-default profile. Acceptable per polish-deferred but a signal that the stitch-profile authoring step is not exercised.
- **Stable line-IDs L1-L22 with no gaps.** Phase 8 of `/and-stitch` says gaps are allowed; this run produced none, indicating no Phase-7 hard CUTs (only CUT-CLAUSE). Schema-clean.

---

## Cross-artifact consistency checks

| Check | Verdict |
|---|---|
| Bones cast header (`taylor, coll, wren`) matches `actors/` provisioning | PASS (3 of 8 provisioned actors appear; rest are downstream-scoped) |
| Scene-map total-bones (27) matches live bones in bones file (29 flat_ids − 2 time-skips = 27) | PASS |
| Scene-map ranges cover bones file exactly | PASS (coverage 27/27, gaps empty, overlaps empty) |
| Facet anchors resolve to bone flat_ids | PASS modulo stale cite-index entries for deleted sensory:2/3 + mem:1 (excluded by stitcher Phase 0.7) |
| Dialogue file coverage (every `speaks to` bone has ≥1 utterance) | PASS (4/4 @8, @23, @25, @26) |
| Chapter goal in bones file matches `memory.md` `chapters[b01c01].goal` | PASS (verbatim match) |
| Narrator in bones file matches `memory.md` `chapters[b01c01].pov_narrator` | PASS (`taylor-hebert-kl-122ac`) |
| Series-audit approved before `/and-substance book b01` ran | PASS (`memory.md:32-36` — approved 2026-05-18T123000Z; `stale_since: ~`) |
| Cost-bearer (wren) + protect-target (sera) class-slots resolved at `/and-cast` | PASS (sera not on-stage in c01; wren is the on-stage cost-bearer per chapter goal) |
| `signature-draft.md` SUPERSEDED notice prevents downstream wrong-id anchoring | PASS-with-risk (notice at file head; downstream agents must read it) |

---

## Most-diverged artifacts (executive ranking, worst first)

1. **`/and-facets` audience-gate cap-burn** — `memory` + `sensory` facets failed the blocking adversarial gate uniformly across 3 cycles. Status capped at `audited-r1-mechanical` (NOT `audited-r1`). Critic card explicitly classes this as NOT-SUCCESSFUL. `/and-stitch` proceeded anyway, downstream.
2. **`/and-stitch` annotated-draft FAULT-AUDIT-MISS surfaces** — three Q9 register hits on facet content (sensory:1 "wall-bottom", narrator:1 "eye-lift", narrator @15 "passive held") rendered as-is because upstream `/and-facets` audit missed them. Indicates rubric gaps in facet authoring.
3. **`signature-draft.md` + `b01-draft.md` orphaned intermediates** in `staff/showrunner/` — large files (384 + 1057 lines) that should arguably have been pruned at persist time. The SUPERSEDED notice on `signature-draft.md` mitigates risk but they are noise; signature-draft's `cl-knowledge-contempt` id is wrong (canonical is `cl-intelligence-arrangement`).
4. **`world-notes.md` stale Lucerys/Nessa naming** — flagged by `/and-series` as needing upstream cleanup; never executed. Low impact (downstream commands stripped to class-slots correctly) but the source-of-truth lineage is inconsistent.
5. **No tuned `stitch-profile.md` and `neutral` persona** — `/and-stitch` fell back to schema defaults; the command's own Phase-0-step-4 warning says silent-neutral-against-tuned-project is canonical failure. The polish-deferred boundary permits this; tuning is simply unused work.
6. **Cite-index staleness on disk** — references sensory:2, sensory:3, mem:1 even after deletions. Excluded from scope by stitcher's Phase 0.7 acknowledgment but the on-disk file is non-fresh; a naive consumer would resolve to non-existent entries.
