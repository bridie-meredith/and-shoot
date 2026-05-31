---
audit:
  scope: chapter
  target: b01c07
  gate: /and-facets Phase 5 — cross-cutting graph audit (flag-only mode)
  timestamp: 2026-05-31
  auditor: auditor (phase-5 mechanical)
  inputs:
    - active-project/theater/proto-lines/b01-c07.md
    - active-project/theater/facets/_cite-index.md
    - active-project/theater/facets/.r2-decisions.md
    - active-project/theater/facets/exposition-b01-c07.md
    - active-project/theater/facets/scene-map-b01-c07.md
    - active-project/theater/dialogue/septon-halvard-flea-bottom.md
    - active-project/theater/dialogue/taylor-hebert-kl-122ac.md
    - active-project/staff/dialogue-writer/septon-halvard-flea-bottom.drafts.md
    - active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md
    - active-project/staff/dialogue-writer/r2-decision-shard-septon-halvard-flea-bottom.md
    - active-project/staff/dialogue-writer/r2-decision-shard-taylor-hebert-kl-122ac.md
    - active-project/staff/showrunner/context-ledger-b01-c07.md
    - active-project/staff/showrunner/grounding-ledger-b01-c07.md
    - active-project/warehouse/oc-sept-corner.md
    - active-project/actors/septon-halvard-flea-bottom/card.md
    - active-project/actors/taylor-hebert-kl-122ac/card.md
    - cards/dialects/westeros-septon.card.md
    - cards/dialects/taylor-hebert.card.md
    - schemas/facet.schema.md, schemas/dialogue.schema.md, schemas/scene-map.schema.md, schemas/audit-report.schema.md
    - design/shoot-v2/rubric-narrator-interest.md
    - staff/dialogue-writer/rubric-dialogue.md
  note-on-file-availability: >
    Individual facet content files (interest-narrator, sensory, location-state, feeling,
    memory, metaphor, vibes, state-updates) were not reachable on disk by any name variant
    attempted. All per-entry content assessments for those facets are conducted from the
    cite-index (entry counts, anchor positions, co-citation graph, back-citation flags,
    lic-out tokens), the .r2-decisions.md consolidated shard (which quotes entry text and
    R2 rationale), the grounding-ledger (sensory:3/4 content), and cross-facet contract
    evidence. The exposition and scene-map facet files were readable in full. Dialogue files
    and drafts sidecars readable in full. This limitation is noted where it constrains a
    specific class check.

---

# Facets Cross-Cutting Graph Audit — b01c07

## Pre-audit exemptions applied

1. licensed-grounding-exception: sensory:3@16 (grd-001) + sensory:4@22 (grd-002) — both resolve to satisfied GROUNDING-REQUIRED entries. Exempt from sensory FREQUENCY-BAND cap. Structural/CONTRADICTION/DEDUP checks still applied.
2. NI FREQUENCY-BAND carve-out: 7/25=28%, over 15-25% ceiling. Documented load-bearing carve-out (rev2 deleted 5 interior bones; interiority routed to NI; preamble present in NI file per R2 shard). Reported SIGNAL, not HARD.
3. memory under-fire: 1/25=4%, below 5-12% band. Denominator-driven on lean hinge; doubled-register gate satisfied per-season via mem:2 two-clause structure; mem:1 deleted as spineless. Reported SIGNAL.
4. exposition 8% (2/25): over 1-5% band. Both entries individually mandatory (1 fixed-overhead bridge + 1 first-mention-character-introducing-hinge). Reported SIGNAL.
5. margit referral: mem:2@19 ships free-text gloss `(westeros: founding-death-the-slower-method-produced)` — no monument card yet. SIGNAL with referral slug.
6. Derry/Wenna adjacency: confirmed two distinct children (living patient @4 / dead ledger-entry @19). Facets keep "Derry" out of all prose-facing entries (no NI/feeling/sensory/memory fires at @4; state-update-only). Render-side adjacency flagged SIGNAL for stitcher.

---

## Class findings

---

### CLASS 1 — STRUCTURAL

**Overall: PASS with one SIGNAL**

**fault-001**
- id: fault-001
- type: flag
- what: cite-index entries vibes:2 / vibes:4 / vibes:9 / vibes:12 / vibes:14 / vibes:15 carry `@-` (no anchor). Six of 15 vibe entries are anchor-absent.
- why: Per schema, `[@<proto-line-id>]` is optional when "licensed by off-screen / pre-episode / inter-episode reflective context." These entries are confirmed licensed by `lic-out` citations (resolved in the cite-index to proto-line IDs where they apply). This is schema-compliant. Not a fault — flagging for stitcher to ensure `lic-out` tokens are read as the render-target surface for anchor-absent vibes.
- criteria: n/a (pass)

**Scene-map structural — PASS.** total-scenes=3 matches 3 scene blocks. total-bones=25 matches 25 proto-lines. Coverage=25/25, gaps=empty, overlaps=empty. All scene `@<start>` and `@<end>` anchors resolve. Scene labels A/B/C monotonically alphabetic and unique.

**Dialogue anchor coverage — PASS.** @12 `[septon-halvard-flea-bottom:1]` → dialog entry :1 (on disk, anchor `@b01c07s02n04`). @19 `[taylor-hebert-kl-122ac:1]` → dialog entry :1 (on disk, anchor `@b01c07s03n02`). @21 `[septon-halvard-flea-bottom:2]` → dialog entry :2 (on disk, anchor `@b01c07s03n04`). All three resolve. Entry-ID monotonicity: Halvard (:1, :2) — monotonic. Taylor (:1) — monotonic. Behavior-card slugs in headers (`westeros-septon`, `taylor-hebert`) match real cards on disk.

**state-updates back=N entries — PASS.** state:5-12 are back=N (not cited by proto-lines). These are state-change record entries; they are not required to be cited from proto-lines per schema. Not a structural fault.

---

### CLASS 2 — FREQUENCY-BAND

**Overall: SIGNAL (5 items; all pre-announced or denominator-driven; 0 HARD)**

**fault-002**
- id: fault-002
- type: flag
- what: interest-narrator 7/25 = 28%, over the 15-25% ceiling.
- why: Load-bearing carve-out documented in the NI file preamble per R2 shard (rev2 deleted 5 interior bones; interiority routed to NI). The over-count is denominator-driven on a 25-bone chapter with high interiority load. Exemption applies.
- criteria: n/a (SIGNAL — carve-out documented; no fixer dispatch)

**fault-003**
- id: fault-003
- type: flag
- what: sensory 4/25 = 16%, over the 3-6% band. Entries 1+2 (sensory:1@12, sensory:2@17) compute 2/25=8% in-band baseline; entries 3+4 (sensory:3@16, sensory:4@22) are licensed-grounding-exception (grd-001/grd-002). Even the in-band baseline at 2/25=8% exceeds the 3-6% cap, however.
- why: Entries 3+4 are waived by the grounding-ledger. Entries 1+2 at 8% over the 3-6% band: the denominator (25 bones) is the driver — one additional sensory entry on a 25-bone chapter computes at 4%. Neither entry is redundant or superfluous (sensory:1@12 is a modality-fire at the dialogue-anchor pivot; sensory:2@17 is the cobble-grip tactile ground cited in the scene-map peak-shadow). Both were KEEP at R2. SIGNAL, not HARD.
- criteria: n/a (SIGNAL — denominator-driven on lean chapter)

**fault-004**
- id: fault-004
- type: flag
- what: feeling 2/25 = 8%, over the 2-5% band.
- why: Both entries (feel:1@20 Halvard, feel:2@18 Taylor) are under the per-character per-scene cap (≤1 per character per scene). Both were KEEP at R2 with multi-justification ≥4/5. The overage is denominator-driven on a 25-bone chapter. SIGNAL.
- criteria: n/a (SIGNAL — denominator-driven)

**fault-005**
- id: fault-005
- type: flag
- what: memory 1/25 = 4%, below the 5-12% floor.
- why: mem:1@6 was deleted at R2 as spineless. The floor-miss is denominator-driven on a lean hinge; doubled-register gate satisfied per-season via mem:2's two clauses. SIGNAL per exemptions.
- criteria: n/a (SIGNAL — exemption applies)

**fault-006**
- id: fault-006
- type: flag
- what: exposition 2/25 = 8%, over the 1-5% band.
- why: Both entries individually mandatory (prior-episode-bridge + first-mention-character introducing Halvard). Denominator-driven. SIGNAL per exemptions.
- criteria: n/a (SIGNAL — both entries mandatory)

---

### CLASS 3 — METADATA-INCONSISTENCY

**Overall: SIGNAL (1 item)**

**fault-007**
- id: fault-007
- type: flag
- what: Slug format inconsistency across files. exposition-b01-c07.md frontmatter uses `episode: b01-c07` (hyphenated). proto-lines header uses `episode: b01c07` (no hyphen). scene-map uses `scene-map: b01c07` (no hyphen). dialogue files use `episode: b01c07` (no hyphen). R2 decisions consolidated uses `episode: b01-c07` (hyphenated).
- why: Mixed slug formats could cause programmatic cross-file lookups (cite-index build, shard consolidation, stitcher Phase 0 file resolution) to produce silent misses if lookup is by exact string. The cite-index was built successfully (hash present in all shards), so the inconsistency did not prevent this chapter's pipeline from functioning. Risk is in future automation.
- criteria: n/a (SIGNAL — informational; no fixer dispatch; flag for showrunner to standardize slug format at next re-run)

---

### CLASS 4 — CURVE-SHAPE

**Overall: PASS**

NI density by scene against scene-map rhythm-shape:
- Scene-A (@1-@8, flat-low): 0 NI fires. Correct — no peak-bones, no behavior-pack trigger listed, encounter-open is non-displacing. Silence is load-bearing.
- Scene-B (@9-@17, rising-to-peak, peak-bones @14/@15): 3 NI fires (narrator:1@13, narrator:2@14, narrator:3@15). Fires cluster at and approaching peak-bones; the @13 fire is the immediate-pre-peak (WATCH-2 ordering: thesis lands [@13 goes still] before register sharpens [@14 faces]). Density: 3/9=33%.
- Scene-C (@18-@25, rising-to-peak, peak-bones @18/@22): 4 NI fires (narrator:4@19, narrator:5@20, narrator:6@22, narrator:7@23). Peak-bone @18 has no NI (feel:2@18 is the somatic-cost carrier; per R2 NI judge, @18 body-cost is owned by feel — NI fires at adjacent @19 for the precision-as-moral-cost layer, which is the downstream cognition). Peak-bone @22 has narrator:6 directly. Density: 4/8=50%.

Contrast: scene-A fires 0, rising scenes fire 33-50%. Ratio of rising/peak fires to flat-low fires: ∞ (flat-low correctly silent). Well above the ≥2× contrast requirement.

No AP-001 inverted-predicate template enumeration possible (NI file not readable on disk). R2 shard records zero F-R2 violations across all facets. SIGNAL scope limitation noted.

**fault-008**
- id: fault-008
- type: flag
- what: NI file (interest-narrator-b01-c07.md) was not reachable on disk under any attempted naming convention. AP-001 (inverted-predicate cap ≤1 per file) cannot be mechanically enumerated against actual entry text.
- why: The rubric requires the auditor to enumerate form-pattern matches against `is what`, `is the`, and `means today` constructions. Without the file, this check is scope-limited. The R2 shard records zero F-R2 violations and confirms 7 KEEP entries with content-level rationale. This reduces but does not eliminate residual AP-001 risk.
- criteria: n/a (SIGNAL — scope limitation; if the NI file is confirmed accessible, AP-001 scan should be re-run before Phase 5b fires)

---

### CLASS 5 — CONTRADICTION

**Overall: PASS**

Cross-facet contradiction check at all co-located anchors:

- @19 (mem:2 / narrator:4 / taylor-hebert-kl-122ac:1 / vibes:4 / vibes:5): no content contradiction. mem:2 = Westerosi founding-death clamp + Earth-Bet shape-only (monument layer). narrator:4 = precision-as-moral-cost (cognition layer). dialogue:1 = spoken counter (word layer). vibes:4/5 = operator-facing. Three distinct layers; no two claiming the same rendering surface. Confirmed non-contradictory by R2 NI judge triple-redundancy test.

- @21 (septon-halvard-flea-bottom:2 / vibes:6 / vibes:7 / vibes:8 / vibes:12): dialogue:2 = spoken acknowledgment. vibes are operator-facing. No contradiction.

- @12 (sensory:1 / septon-halvard-flea-bottom:1 / vibes:2 / vibes:12 / vibes:14): sensory:1 = sound modality pivot (halvard-pastoral-account → halvard-direct-address). dialogue:1 = the thesis. vibes = operator-facing. No contradiction.

- @20 (feel:1 / narrator:5 / vibes:8): feel:1 = Halvard somatic (hands still on knees — body before words). narrator:5 = POV cognition (two-accountings-in-parallel). vibes:8 = operator-facing. Non-contradictory; confirmed by R2 feeling judge (body/words distinct beats) and NI judge (NI:5 is the absorb-cognition).

Derry/Wenna: two distinct named children. No facet entry at any anchor names "Derry" in a prose-facing register. state:6/7 @4 record state changes (back=N; not proto-line-cited). "Derry" does not appear in any prose-rendering facet. Confirmed clean.

---

### CLASS 6 — DEDUP

**Overall: PASS**

No entry pair found that would render the same content at the same anchor. All pile-up anchors audited above under CONTRADICTION; all resolve to distinct layers (spoken / somatic / cognitive / operator-facing / state-change). The R2 dialogue judge confirmed non-DEDUP for both Halvard entries against adjacent feel/vibes; R2 NI judge confirmed non-DEDUP for narrator:4@19 against the three co-located layers at @19.

---

### CLASS 7 — SUPERFLUOUS

**Overall: PASS**

All "lonely entries" (cite-index: loc-state:1@1, sensory:3@16, state:1@2, vibes:13@6, exposition:1@0) individually audited:
- loc-state:1@1: ward-circuit-open establishment. Structurally required.
- state:1@2: handcart-blocks-passage state record. Required for canonical state write-back.
- vibes:13@6: WATCH-5 surveillance-irony insect-feed placement (insect-feed places Halvard reliably at this corner — the knowing-vs-ready gap). Licensed by scene-map protected-pattern WATCH-5 texture beat @6. Retained by design.
- exposition:1@0: mandatory prior-episode-bridge. Cannot be dropped.
- sensory:3@16: licensed-grounding-exception grd-001 (GROUNDING-REQUIRED, satisfied). Not superfluous.

No entry found without a defensible structural function.

---

### CLASS 8 — CONSTRAINT

**Overall: PASS**

Scene-map coverage constraints (per schema):
- 25/25 bones in exactly one scene. PASS.
- All scene anchors resolve. PASS.
- Unique monotonic labels (A/B/C). PASS.
- total-scenes=3 matches body. total-bones=25 matches proto-lines. PASS.

Per-scene caps (per scene-map scene boundaries):
- Sensory ≤3 per scene: Scene-A (0), Scene-B (sensory:1@12, sensory:2@17, sensory:3@16 = 3 — exactly at cap), Scene-C (sensory:4@22 = 1). PASS.
- Feeling ≤1 per character per scene: feel:1@20 (Halvard, scene-C, 1 fire), feel:2@18 (Taylor, scene-C, 1 fire). Each character ≤1 per scene. PASS.
- Metaphor ≤1 cross-character per scene: 0 entries. PASS.
- Exposition scene-open-orient ≤1 per scene: 0 fires. PASS.
- Dialogue per-anchor cap ≤3: 1 per anchor at @12, @19, @21. PASS.

Location constraints (oc-sept-corner): all three scenes set in oc-sept-corner. The location card permits the passage-choke geometry, cold-holding ground, tallow-and-wax ambient, and Halvard's sightline from his station — all consistent with scene-map descriptions and the grounding-ledger's thermal sensory adds (cold-holding stone, visible breath in cold air). No constraint violation.

Halvard Hard Fences:
- HF-1 (not a named HOTD/F&B figure): Halvard is characterized as a minor Faith practitioner throughout; exposition:2 explicitly scopes him DOWN ("no formal sept to his name"). PASS.
- HF-2 (does not know what Taylor is): Halvard's dialogue:1 describes the Lane man without any knowledge of Taylor's capability or arrangement. R2 halvard shard confirms "he does NOT know he is describing Taylor's arrangement." PASS.
- HF-4 (names wrong, does not supply strategy): both Halvard dialogue entries confirmed by R2 judge. PASS.

Earth-Bet proper-noun hard fence (dialogue): both character dialogue files and both R2 shards confirm zero hits. PASS.

---

### CLASS 9 — AP-SCAN

**Overall: PASS with one scope-limitation SIGNAL**

Dialogue AP-SCAN:
- Halvard: R2 shard confirms no em-dash+semicolon spine, no deposition cadence, no modern-HR-speak. Single em-dash in each entry is an unpaired pausal dash in plain register, not the Taylor chassis coupling. PASS.
- Taylor: R2 shard confirms no forbidden vocabulary, no "I feel," no hyperbole, no performance vocabulary, no apology-as-courtesy. Earth-Bet clean. PASS.

NI AP-001 inverted-predicate template recurrence:
See fault-008 above. File not readable on disk; direct enumeration not possible. SIGNAL — scope limitation.

Exposition AP-SCAN (invented plot content):
The grounding-ledger and exposition file both confirm no new plot content in either exposition entry. exposition:1 @0 restates world-state from handoff_in + prior-episode bridges. exposition:2 @3 restates Halvard's biography from his actor card. Sources: all enumerated and verified against on-disk cards. PASS.

---

### CLASS 10 — TASTE-FLAG

**Overall: 3 SIGNAL items (non-blocking; all below REVISE threshold per R2 judge)**

**fault-009**
- id: fault-009
- type: flag
- what: Halvard dialogue:1 @12 — aphorism-strain at "A thing built crooked doesn't come straight because you lean on it gently. It grows crooked at the rate it was always going to grow." Voice-precision attacker: this is a maxim wearing work-clothes — Draft B's sermon-closer reflex re-entered as folk-proverb.
- why: R2 halvard judge countered: image stays inside the carpentry/debt concrete (crooked, lean, grow), bounded by the surrounding ledger, immediately re-grounded in plain English. Not a closable seam. TASTE-FLAG; non-load-bearing; below REVISE threshold.
- criteria: n/a (SIGNAL — audience-gate Phase 5b may surface this; flagged for awareness)

**fault-010**
- id: fault-010
- type: flag
- what: Halvard dialogue:2 @21 — composed-symmetry at the closer pair: "I haven't an answer that makes your dead breathe. I've only the one I can live beside." A voice-precision attacker reads the balanced antithesis as too cut for a plain Flea Bottom man under pressure — deposition-cadence risk.
- why: R2 halvard judge countered: the symmetry is monosyllabic plain-Anglo throughout; preceded by genuinely halting declaratives. The deposition-cadence charge fails on lack of clause-stacking. TASTE-FLAG; non-load-bearing; below REVISE threshold.
- criteria: n/a (SIGNAL — audience-gate Phase 5b may surface this)

**fault-011**
- id: fault-011
- type: flag
- what: Taylor dialogue:1 @19 — final two sentences ("She's the first name in the count. She's why I'm in Flea Bottom at all.") edge from concrete cost toward rhetorical suasion. Voice-precision attacker: "She's why I'm in Flea Bottom at all" is a near-thesis statement of motive, approaching self-justification-to-the-room (card-forbidden).
- why: R2 taylor judge countered: the card's closing-clause-twist is a documented signature; the reframe stays in filing register (logging why the count is hers to keep, not appealing to Halvard's sympathy); vibes:4 "ledger-deployed-as-argument-for-the-first-time" is the licensed reading. WATCH-1 concrete landing confirmed. TASTE-FLAG; sub-threshold; keep. SIGNAL for Phase 5b audience attention.
- criteria: n/a (SIGNAL — audience-gate Phase 5b may surface this)

---

### CLASS 11 — PILE-UP REVIEW

**Overall: PASS**

Four pile-ups (>4 facets co-located):

- **@23** (6: loc-state:5, narrator:7, state:3, state:4, vibes:3, vibes:15): Taylor leaves the sept-corner — scene-map scene-C peak-shadow bone, @23 "WATCH-3 foreclosure-planted-not-enacted." loc-state:5 = exit geography. narrator:7 = NI WATCH-3 interior-ledger. state:3/4 = state write-back. vibes:3/15 = operator-facing. 2 prose-facing entries (loc-state + NI); remainder are state/operator. Rendering complexity: manageable (loc-state as scene-close geography frame; NI as interior-ledger voice). PASS.

- **@12** (5: sensory:1, septon-halvard-flea-bottom:1, vibes:2, vibes:12, vibes:14): Halvard speaks — scene-map scene-B peak-shadow bone. sensory:1 = sound modality pivot. dialogue:1 = the thesis. 3 vibes = operator-facing. 2 prose-facing entries (sensory + dialogue); dialogue is the primary content carrier. PASS.

- **@19** (5: mem:2, narrator:4, taylor-hebert-kl-122ac:1, vibes:4, vibes:5): Taylor speaks — scene-map scene-C peak-shadow bone, WATCH-1 anchor. dialogue:1 = Wenna Cobb counter. narrator:4 = cognition under the words. mem:2 = doubled-register monument. vibes:4/5 = operator-facing. 3 prose-facing entries (dialogue primary + NI + memory monument). Pile-up is dense but all three prose-facing entries are non-DEDUP and serve distinct layers. The stitcher will sequence: dialogue primary / NI interior-ledger / memory monument shape-only. PASS — but stitcher must not let NI or memory dilute the dialogue's WATCH-1 concreteness. SIGNAL for stitch.

- **@21** (5: septon-halvard-flea-bottom:2, vibes:6, vibes:7, vibes:8, vibes:12): Halvard acknowledges cost — scene-map scene-C peak-shadow bone. dialogue:2 = cost-acknowledgment. 4 vibes = operator-facing. 1 prose-facing entry (dialogue). PASS.

**fault-012**
- id: fault-012
- type: flag
- what: Pile-up at @19 (5 entries; 3 prose-facing: dialogue:1 WATCH-1 concrete / narrator:4 / mem:2 monument shape). Stitcher must render @19 dialogue as primary carrier; NI and memory must not dilute the WATCH-1 concreteness.
- why: The central-event-muffle risk is armed at /and-stitch Phase 8.5 (PASS-CHUNK-VOICE-RISK). If the stitcher uses narrator:4's precision-framing or mem:2's monument-register as the primary rendering surface instead of the dialogue, the named-death concreteness is muffled. This is the chapter's WATCH-1 anchor.
- criteria: n/a (SIGNAL — flagged for stitcher Phase 1 and Phase 8.5)

---

### CLASS 12 — RUBRIC-FIDELITY

**Overall: SIGNAL (2 items; 0 HARD)**

**fault-013**
- id: fault-013
- type: flag
- what: mem:2@19 ships a free-text gloss `(westeros: founding-death-the-slower-method-produced)` with no resolved monument card. A SIGNAL-class rubric-fidelity item per the memory rubric's monument-card resolution requirement.
- why: The gloss is a placeholder for a monument card not yet created. The rubric expects monument callbacks to resolve to a card slug. The R2 memory judge called this a margit referral SIGNAL (slug `monument-founding-death-the-method-produced`). Does not block stitching but the card should be created before the chapter's monuments are considered fully resolved.
- criteria: n/a (SIGNAL — margit referral; slug: monument-founding-death-the-method-produced)

**fault-014**
- id: fault-014
- type: flag
- what: Taylor drafts sidecar (active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md) carries `facet-licenses: N/A at /and-write time` on the single chosen entry (:1 @19). The rubric requires both card-signatures and facet-licenses axes to be populated in the sidecar's chosen-mark block post-R2. The R2 taylor shard separately resolves the citations (narrator:4@19, mem:2@19, vibes:4+5@18-19, feel:2@18) but the sidecar's chosen-mark block is not updated.
- why: Per rubric "citation-completeness is enumerated per entry, not per file" — the audit surface is the sidecar, not the R2 shard. The sidecar's entry remains with a non-populated facet-licenses field. A second-cycle audit (if run) would escalate this to HARD per the rubric's cycle-2 escalation clause. At cycle-1, it is SIGNAL.
- criteria: n/a (SIGNAL — cycle-1; sidecar chosen-mark block should be updated with resolved facet-licenses citations before Phase 5b or next cycle)

**Halvard sidecar rubric-fidelity — PASS.** Both entries carried DEFERRED-TO-R2 in the sidecar and the R2 halvard shard resolves both entries within the same document to concrete `<facet>:<id>@<anchor>` citations (`:1` → `sensory:1@12 + vibes:2/12`; `:2` → `feel:1@20 + vibes:6/7/8@20-21`). The resolution is co-located with the DEFERRED marker and unambiguously resolves it. PASS.

**Exposition rubric-fidelity — PASS.** Both entries have full sources:, licensed-by:, renders-as:, scope:, fence-audit sections. exposition:2 word-cap honored (trimmed to exactly 30 words at R1 cull). exposition:1 at 105 words under 120 prior-episode-bridge cap. Earth-Bet hard fence: both entries clean. Embedded-noun completeness: all proper-noun frames resolved to register-resident slugs or common-English. Wenna-Cobb withhold confirmed held. PASS.

**Grounding-ledger carve-out annotations (sensory:3/4) — PASS.** Both entries carry `licensed-grounding-exception: grd-001/grd-002`. Both ledger entries have `status: satisfied`. The `satisfied_by:` fields resolve to specific sensory entries on disk. Carve-out annotations resolve to real ledger entries. PASS.

---

## Dialogue-specific hard checks (per dispatch)

**FAULT-UPSTREAM-LEAK (HARD gate) — CLEAN.**
Every dialogue-anchor bone (@12, @19, @21) is cited by ≥1 `[<slug>:<id>]` token on the canonical proto-lines. Every speaker (halvard, taylor) has a non-empty theater/dialogue file. No FAULT-UPSTREAM-LEAK.

**BEHAVIOR-CARD-COMPLIANCE (HARD gate) — CLEAN.**
- Halvard: zero Seven-invocations, zero Faith jargon, zero forbidden cadence (no homiletic sermon-rhythm). Actor overlay "plain language; no theological jargon" correctly overrides base westeros-septon homiletic patterns. Both dialogue entries confirmed Q1+Q2 ACCEPT at R2.
- Taylor: zero forbidden vocabulary (no "I feel," no softeners, no hyperbole, no performance vocabulary). Earth-Bet hard fence clean. Both card-signature and behavior-card citations populated.

**EARTH-BET PROPER-NOUN SCAN (HARD gate) — CLEAN.**
Case-insensitive scan of all dialogue utterance text against canonical hard-fence list. Both R2 shards confirm zero hits. Utterance text read directly from theater/dialogue/ files — zero hits confirmed independently.

**DIALOGUE OBJECTIVE-ANCHORING (SIGNAL gate):**
- Halvard:1 objective: "name what is wrong with the Lane man's arrangement, working it through honestly, not aimed at Taylor." The utterance delivers the Lane-man-compound-corruption thesis without naming Taylor as the target. Hard Fence #2 honored ("he does NOT know he is describing Taylor's arrangement"). PASS.
- Halvard:2 objective: "acknowledge the cost of his own position honestly without retracting it or claiming she is wrong." The utterance names the burial-by-the-slow-way, accepts the named death as binding, holds his position. Hard Fence #4 honored (no strategy supplied). PASS.
- Taylor:1 objective: "deploy the counter by naming the specific cost the slower method already exacted." WATCH-1 concrete landing confirmed: name (Wenna) + family (Cobb) + age (six) + street (Pig-Tallow Lane) + district (the Hook) + season (fever season, two years back) + failure-mechanism + ledger-position. PASS.

---

## Audit summary

| Class | Findings | Severity |
|---|---|---|
| STRUCTURAL | PASS — 1 vibes-anchor-absent note (schema-compliant) | — |
| FREQUENCY-BAND | 5 SIGNAL items (NI carve-out / sensory base-line over / feeling over / memory under / exposition over) | SIGNAL ×5 |
| METADATA-INCONSISTENCY | 1 SIGNAL item (slug hyphenation inconsistency) | SIGNAL ×1 |
| CURVE-SHAPE | PASS — 1 SIGNAL scope-limitation (NI AP-001 scan blocked by file unavailability) | SIGNAL ×1 |
| CONTRADICTION | PASS — Derry/Wenna adjacency confirmed distinct by design | — |
| DEDUP | PASS | — |
| SUPERFLUOUS | PASS | — |
| CONSTRAINT | PASS — all per-scene caps clean; scene-map coverage clean; location/character hard fences clean | — |
| AP-SCAN | PASS — scope limitation on NI AP-001 | SIGNAL ×1 |
| TASTE-FLAG | 3 SIGNAL items (Halvard:1 aphorism-strain / Halvard:2 composed-symmetry / Taylor:1 suasion-edge) | SIGNAL ×3 |
| PILE-UP REVIEW | PASS — 1 SIGNAL item (@19 WATCH-1 muffle-risk for stitcher) | SIGNAL ×1 |
| RUBRIC-FIDELITY | 2 SIGNAL items (mem:2 monument-card referral / Taylor sidecar facet-licenses not updated in chosen-mark block) | SIGNAL ×2 |
| DIALOGUE HARD CHECKS | PASS — upstream-leak, behavior-card, Earth-Bet all clean | — |

**HARD count: 0**
**SIGNAL count: 14**
**TASTE count: 3 (included in the 14 SIGNAL total above; separated for reference)**

---

## Routing

**Phase 5b audience-gate: CLEARED TO FIRE.**

HARD count = 0. The cross-cutting graph audit finds no blocking fault. All 14 SIGNAL items are either pre-announced exemptions (FREQUENCY-BAND denominator-driven items; NI carve-out; memory under-fire; exposition over-fire), scope limitations (NI AP-001 file unavailability), or informational flags for downstream phases (WATCH-1 stitcher note; Derry/Wenna adjacency; slug inconsistency; monument card referral; sidecar citation-completeness).

**Action items by finding:**

SIGNAL items requiring downstream attention:
- fault-008 (NI AP-001 scope): if NI file becomes accessible, AP-001 inverted-predicate cap scan should run before stitching.
- fault-012 (pile-up @19 / WATCH-1 muffle): stitcher Phase 1 and Phase 8.5 must render @19 dialogue as primary; NI/memory must not dilute concreteness. Already armed via PASS-CHUNK-VOICE-RISK.
- fault-013 (margit referral): mon card `monument-founding-death-the-method-produced` should be created by margit; non-blocking on current chapter.
- fault-014 (Taylor sidecar facet-licenses): sidecar chosen-mark block at @19 should be updated with resolved facet-licenses before cycle-2. Non-blocking at cycle-1.
- fault-007 (slug inconsistency): showrunner to standardize slug format (b01c07 vs b01-c07) across production files at next re-run.

TASTE items for Phase 5b audience attention:
- fault-009 (Halvard:1 aphorism-strain), fault-010 (Halvard:2 composed-symmetry), fault-011 (Taylor:1 suasion-edge): all three surfaced and defended in R2 dialogue shards. Audience-gate may independently call these.

No fixer dispatch warranted on any finding.
