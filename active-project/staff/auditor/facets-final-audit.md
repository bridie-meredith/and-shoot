```yaml
audit:
  scope: chapter
  target: b01c15
  timestamp: 2026-06-04
  gate: /and-facets Phase 5 — mechanical cross-cutting facet audit
  findings:

    # ── CLASS 1: STRUCTURAL ────────────────────────────────────────────────────

    - id: fault-001
      type: pass
      what: "@0-@40 proto-line ID range — all 40 bones present in b01-c15.md, numbered 1-40 monotonically. @0 appears only in exposition:1 (chapter-preamble bridge) consistent with cite-index note."
      why: ID monotonicity verified. No gaps, no duplicates.

    - id: fault-002
      type: pass
      what: "Bidirectional citation — every [facet:id] token on every proto-line resolves to a facet entry."
      why: "Full walk: [loc-state:1]→loc-state@1 ✓, [loc-state:2]→loc-state@3 ✓, [loc-state:3]→loc-state@14 ✓, [loc-state:4]→loc-state@32 ✓; [state:1]→state@1 ✓, [state:2]→state@1 ✓, [state:3]→state@12 ✓, [state:4]→state@22 ✓, [state:5]→state@23 ✓, [state:6]→state@31 ✓, [state:7]→state@33 ✓, [state:8]→state@36 ✓, [state:9]→state@37 ✓, [state:10]→state@38 ✓, [state:11]→state@40 ✓, [state:12]→state@17(consolidated-12) ✓, [state:13]→state@13(consolidated-13) ✓, [state:14]→state@22(consolidated-14) ✓, [state:15]→state@27(consolidated-15) ✓; [narrator:1-10]→NI@5/@8/@11/@13/@17/@22/@26/@27/@30/@39 ✓; [sensory:1-4]→sensory@5/@20/@30/@32 ✓; [feel:1]→feeling@30 ✓, [feel:2]→feeling@39 ✓; [mem:1]→memory@22 ✓, [mem:2]→memory@39 ✓; [meta:1]→metaphor@28 ✓; [vibes:1-7]→vibes@11/@5/@18/@27/@28/@34/@39 ✓; [exposition:2-4]→exposition@3/@16/@26 ✓."

    - id: fault-003
      type: flag
      what: "Reverse citation walk — exposition:1 (@0 bridge) carries no proto-line @0 citation; cite-index note states this is per-design (episode-open bridge, not a proto-line)."
      why: "The exposition:1 entry is structurally unanchored from the proto-line side. This is documented as intentional per cite-index §Notes. Noted for the record; not a fault."

    - id: fault-004
      type: pass
      what: "Header well-formed check — all 9 facet files carry facet/episode/author header fields. Consolidated files (state-updates, feeling) carry source-slices field."
      why: "No malformed headers."

    - id: fault-005
      type: flag
      what: "vibes:5 @28 licensed-by field reads: 'proto:28, peak-bone:27, state-update:tba'. The 'tba' token on state-update:tba remains unresolved in the vibes file."
      why: "The cite-index does not list a dangling tba in its notes; the state-update field is an auxiliary licensed-by, not a primary structural anchor. The primary anchors (proto:28 + peak-bone:27) are valid. The tba is advisory/decorative rather than structurally required for the vibes entry to function. No downstream breakage; however, the token is unresolved. Noted as a flag for the stitch team. Not a HARD finding because state-updates:14 (@27) is the plausible resolution and the entry is otherwise sound."

    # ── CLASS 2: FREQUENCY-BAND ───────────────────────────────────────────────

    - id: fault-006
      type: pass
      what: "Sensory density: 4/40 = 10% gross. Standard entries (non-licensed): sensory:1 @5 + sensory:4 @32 = 2/40 = 5%. Within 3-6% band. Licensed exceptions: sensory:2 @20 (grd-001) + sensory:3 @30 (grd-002). Both carry grounding-ledger entries with status: satisfied. Ledger IDs resolve. Per-scene: S01=1, S02=1, S03=1, S04=1. All ≤3."
      why: "Sensory band PASS. Grounding-ledger licenses valid."

    - id: fault-007
      type: pass
      what: "Exposition density: 4/40 = 10% gross. Standard entries (non-licensed): exposition:1 @0 is a chapter-bridge (no band contribution per cite-index). Licensed entries: exposition:2 @3 (ctx-001), exposition:3 @16 (ctx-002), exposition:4 @26 (ctx-003). All three context-ledger IDs carry status: satisfied. Non-licensed net count = 0 formal band-entry bones (the @0 bridge is reader-state, not a glossed-term per cite-index; standard density is effectively 0/40 in the formal band, with 3 licensed additions). Context-ledger licenses valid."
      why: "Exposition band PASS. All three context-ledger licenses resolve."

    - id: fault-008
      type: pass
      what: "Narrator-interest density: 10/40 = 25%. Top-of-band per cite-index (15-25% band). At the ceiling but not over."
      why: "NI band PASS."

    - id: fault-009
      type: pass
      what: "Memory density: 2/40 = 5%. Within 5-12% band."
      why: "Memory band PASS."

    - id: fault-010
      type: pass
      what: "Feeling density: 2/40 = 5%. Top-of-band per cite-index (2-5% band)."
      why: "Feeling band PASS."

    - id: fault-011
      type: pass
      what: "Metaphor density: 1/40 = 2.5%. Within 0-3% band."
      why: "Metaphor band PASS."

    # ── CLASS 3: CONTRADICTION / DEDUP ────────────────────────────────────────

    - id: fault-012
      type: pass
      what: "3-layer bone @22: [mem:1 + narrator:6 + state:4 + state:14]. mem:1 = channel-found-from-both-ends confirmation (arrangement non-extractable); narrator:6 = marks the thermal-rise and does NOT mark what it confirms (the architecture found from the other side); state:4 = prop:oc-coverage-record.thermal-rise marked; state:14 = actor arrangement_extractability advances to non-extractable. Each layer operates in a distinct register — the memory surfaces the prior-chapter fact, the NI surfaces the self-observation-gap, the env-state surfaces the prop change, the actor-state surfaces the axis advance. No redundancy."
      why: "Distinct registers confirmed."

    - id: fault-013
      type: pass
      what: "@27 3-layer bone: [narrator:8 + state:15 + vibes:4]. narrator:8 = gap opens a hole, the absence takes a shape, person-sized; state:15 = relational_anchor_status_axis +1.5 LOCK; vibes:4 = person-shaped-clearing / negative-space-as-deliberate-architecture. NI operates on the perception event; state-update registers the axis advance; vibes surfaces the atmospheric accumulation. Distinct."
      why: "No cross-layer redundancy at @27."

    - id: fault-014
      type: pass
      what: "@30 3-layer bone: [feel:1 + narrator:9 + sensory:3]. feel:1 = hand stops on the stylus (suppressed somatic); narrator:9 = the gap holds its shape one more beat, she holds it, lets it settle nowhere; sensory:3 = sound — one exhalation. Three modalities: somatic suppression (feeling), perceptual-cognitive hold (NI), auditory grounding (sensory). Distinct."
      why: "No cross-layer redundancy at @30."

    - id: fault-015
      type: pass
      what: "@39 4-layer bone: [feel:2 + mem:2 + narrator:10 + vibes:7]. feel:2 = hand crosses field without catch (enacted absence); mem:2 = eleven-month blank field, the small-version-of-a-thing, the routing-of-a-life SHAPE-ONLY; narrator:10 = the category is eleven months old, what changed is shape; vibes:7 = enacted-absence / ledger-closes-with-gap-inside. NI operates on the cognitive accounting; memory brings the eleven-month backstory; feeling enacts the physical gesture; vibes names the atmospheric register. Distinct."
      why: "No cross-layer redundancy at @39."

    # ── CLASS 4: CONSTRAINT ───────────────────────────────────────────────────

    - id: fault-016
      type: pass
      what: "Memory-with-NI-spine check. mem:1 @22 → narrator:6 @22 ✓ (same anchor). mem:2 @39 → narrator:10 @39 ✓ (same anchor)."
      why: "Both memory entries have co-cited NI on the same anchor bone."

    - id: fault-017
      type: pass
      what: "metaphor meta:1 @28 provisional tba resolution. The carve-out notes cite 'ni:tba + sensory:tba' as provisional tokens at Phase 1. Per the rubric carve-out in metaphor-b01-c15.md, these resolve at Phase 4. Checking actual facet graph: narrator:8 fires @27 (peak-bone:27 is its paired anchor), vibes:5 fires @28. The cite-index resolves licensed-by as 'peak-bone:27 + ni:tba + sensory:tba'. Narrator:8 is at @27 not @28; the NI spine for the adjacent peak-bone is @27. For ni:tba: the metaphor carve-out explains the licensed-by includes ni:tba meaning the NI layer on the peak-beat complex (@27-@28) — narrator:8 is @27 which is the peak-bone complex. The metaphor file body cites 'ni:tba' and 'sensory:tba' with explicit note '[feeling:tba — resolves at Phase 4 to feeling-flag @30]'. The feeling:1 @30 is in the facet graph. sensory:3 @30 is also in the facet graph. These tba tokens were authored at Phase 1 before Phase 4 citation resolution. The question is whether the resolution was completed. The metaphor file does NOT update the tba tokens to specific IDs — they remain as 'ni:tba' and 'sensory:tba' in the licensed-by string. The constraint says 'the licensed-by cannot bind to ≥2 real supporting layers' — verify. The real layers that support meta:1 @28: (a) peak-bone:27 ✓ (scene-map confirms @27 is the scene-C peak-bone), (b) narrator:8 @27 is the NI spine on the peak beat — resolves ni:tba, (c) sensory:3 @30 or sensory:2 @20 cover the S03 sensory register — resolves sensory:tba, (d) feeling:1 @30 is the feeling-flag for the somatic-tell. The licensed-by requirement of ≥2 real supporting layers is met by the real graph. However, the licensed-by field in the metaphor file still reads 'peak-bone:27 + ni:tba + sensory:tba [feeling:tba — resolves at Phase 4]' — the tba tokens were NOT replaced with actual facet IDs at Phase 4."
      why: "The binding is structurally valid (real graph supports ≥2 layers), but the tba tokens remain unresolved as text in the licensed-by field. This is a record-hygiene issue: a downstream reader of the facet file cannot verify the citation without consulting the full graph. Flag for resolution. Not a HARD finding because the underlying graph supports the binding."
      criteria: null

    - id: fault-018
      type: flag
      what: "metaphor meta:1 @28 licensed-by field: 'peak-bone:27 + ni:tba + sensory:tba [feeling:tba — resolves at Phase 4 to feeling-flag @30]' — tba tokens not replaced with resolved IDs (ni:tba should read narrator:8, sensory:tba should read sensory:3, feeling:tba should read feel:1)."
      why: "Traceability: a future reader of the metaphor file cannot verify the three supporting layers without cross-referencing the full facet graph. The carve-out explicitly intended Phase 4 resolution. The Phase 4 pass appears to have populated the feeling/NI/sensory entries but did not write back to the metaphor licensed-by field."

    - id: fault-019
      type: pass
      what: "State-updates actor:POV NI co-citation check. state:12 @17 cites spine: narrator-interest @17 (narrator:5 fires @17 ✓); state:13 @13 cites spine: narrator-interest @13 (narrator:4 fires @13 ✓); state:14 @22 cites spine: narrator-interest @22 (narrator:6 fires @22 ✓); state:15 @27 cites spine: narrator-interest @27 (narrator:8 fires @27 ✓)."
      why: "All four actor-state shifts carry verified NI spine co-citation."

    - id: fault-020
      type: pass
      what: "Exposition source-traceability. exposition:1 @0 cites sources: glossed-terms.md b01c12:2/b01c05:2/b01c03:6/b01c03:3 + scene-map + substance_delta. exposition:2 @3 cites glossed-terms.md b01c08:2. exposition:3 @16 cites glossed-terms.md b01c08:2. exposition:4 @26 cites glossed-terms.md b01c12:2 + b01c01:9 + b01c14 bridge. All four carry sources fields."
      why: "Source-traceability PASS."

    - id: fault-021
      type: pass
      what: "Licensed-context-exception / licensed-grounding-exception dangling check. context-ledger IDs: ctx-001 satisfied_by exposition:2 ✓, ctx-002 satisfied_by exposition:3 ✓, ctx-003 satisfied_by exposition:4 ✓. grounding-ledger IDs: grd-001 satisfied_by sensory:2 ✓, grd-002 satisfied_by sensory:3 ✓. No dangling ledger IDs."
      why: "All ledger IDs resolve to authored entries. PASS."

    # ── CLASS 5: EARTH-BET HARD-FENCE PROPER-NOUN SCAN ────────────────────────

    - id: fault-022
      type: pass
      what: "Full text scan across all 9 facet files for Earth-Bet proper nouns: Khepri, Gold Morning, Brockton Bay, Skitter, Scion, parahuman, cape, PRT, Endbringer, Worm-canon power-classification terms (trigger, shard, entity, tinker, thinker, master, shaker, mover, striker, breaker, changer, blaster, stranger, brute, trump, Wards, Undersiders, Cauldron, Birdcage, Queen Administrator, Earth-Bet, Gimel, Aleph)."
      why: "Results: memory:2 @39 cites 'earth-bet: routing-lives-at-a-remove SHAPE-ONLY' — this is a metadata tag on the memory entry, not a text field in the rendered facet content. The tag is an authoring note (the shape reference is shape-only per the atonement/Gold-Morning-as-shape rule) visible inside the facet file only. The tagged phrase 'routing-lives-at-a-remove' contains no Earth-Bet proper noun; 'earth-bet' appears only as the tag label naming the constraint being respected. This is authoring-process notation in the facet layer, not authored text that would flow into prose. No Earth-Bet proper nouns appear in any text field intended for rendered output. exposition:3 @16 includes 'Worm-canon-pedant' as an audience persona slug in the licensed-by field — this is an internal citation, not authored content. No proper-noun fence violations in any prose-destined text field."

    - id: fault-023
      type: pass
      what: "scene-map Earth-Bet fence self-declaration: 'Earth-Bet fence: CLEAN (insect-feed rendered as fly/flight-muscle/thermal physics; no parahuman jargon; no Gold-Morning echo this chapter).' Cross-checked against all facet entries: confirmed clean."
      why: "Earth-Bet HARD fence: 0 violations. HARD count = 0."

    # ── CLASS 6: CURVE-SHAPE ──────────────────────────────────────────────────

    - id: fault-024
      type: pass
      what: "Scene-map rhythm-shape declarations: scene-A = 'falling-arc establishment'; scene-B = 'falling — the weight deepens through substrate'; scene-C = 'falling-arc peak (the chapter's deepest beat — recognition WITHOUT consequence, not a climax)'; scene-D = 'the fall into settled state — the stillness is load-bearing, not deflation'. Dramatic_shape from substance: falling. The curve runs: external-anchor → substrate-weight → recognition-peak (relational_anchor +1.5 + antag-LOCK) → settled-full-load."
      why: "CURVE-SHAPE coherent with falling dramatic_shape. SHAPE-OK confirmed. The rising-to-settled-full-load disposition is the correct shape for a 'falling' chapter with no catharsis — the peak IS the quiet recognition, not an external climax. No curve mismatch."

    # ── CLASS 7: SCENE-MAP COVERAGE ───────────────────────────────────────────

    - id: fault-025
      type: pass
      what: "Scene-map coverage line: 'coverage: 40/40 bones in exactly one scene'. Scene-ranges: S01 @1-@13 (13 bones), S02 @14-@23 (10 bones), S03 @24-@31 (8 bones), S04 @32-@40 (9 bones). Total = 40. No gaps listed, no overlaps listed."
      why: "Every bone @1-@40 in exactly one scene range. URI-SCENE-WINDOW PASS."

    - id: fault-026
      type: pass
      what: "Per-scene sensory caps (≤3/scene): S01=sensory:1 @5 → 1; S02=sensory:2 @20 → 1; S03=sensory:3 @30 → 1; S04=sensory:4 @32 → 1. All scenes = 1 sensory entry. All within ≤3 cap."
      why: "Sensory per-scene cap PASS."

    - id: fault-027
      type: pass
      what: "Per-scene feeling cap (≤1/char/scene): feeling:1 @30 is S03 (Taylor only); feeling:2 @39 is S04 (Taylor only). One character (Taylor), one entry per scene. No scene with >1 feeling entry for the same character."
      why: "Feeling per-scene cap PASS."

    - id: fault-028
      type: pass
      what: "Per-scene metaphor cap (≤1/scene): meta:1 @28 is S03. Only one metaphor entry in the chapter. S01, S02, S04 = 0. S03 = 1. Within ≤1 cap."
      why: "Metaphor per-scene cap PASS."

    # ── CLASS 8: RUBRIC-FIDELITY ──────────────────────────────────────────────

    - id: fault-029
      type: pass
      what: "loc-state verb-class check. All four loc-state entries describe place-state (anchor position, condition, traffic) rather than action verbs. loc-state:1 @1 'stone-lip-open, corner-gutter-occupied, outer-court-approach-clear' — state description ✓. loc-state:2 @3 'court-center-open, master-at-arms-led' — state description ✓. loc-state:3 @14 'passage-slope-open, corner-gutter-occupied' ✓. loc-state:4 @32 'passage-arch-gutter-settled, eastern-fringe-normalizing' ✓. All use nominal/adjectival state descriptors; no action-verb-class violations."
      why: "loc-state verb-class rubric PASS."

    - id: fault-030
      type: pass
      what: "state-updates no-registration-vocabulary check. Review of all 15 state entries: entries describe field transitions with arrow notation (old_state -> new_state). None use registration vocabulary (no 'is registered as', 'is noted as', 'has been established', or similar). The entry 'prop:oc-coverage-record.site-condition-entries.thermal-rise: absent -> marked' uses 'marked' as a field-value state, not as a verb-of-registration. CLEAN."
      why: "state-updates registration-vocabulary rubric PASS."

    - id: fault-031
      type: pass
      what: "NI no-inverted-predicate-saturation check. Ten NI entries reviewed for inverted-predicate pattern (the 'X does not Y' inversion family as AP-SCAN saturation risk). Entries: NI:1 'stone does not accommodate at all' — one inversion; NI:2 'arc is sized for a body that is not on the court' — one inversion; NI:3 'yield happens in the older man's frame, not the boy's' — contrast, not AP-saturation; NI:4 'routes nothing of him anywhere' — suppressed-action, not AP-inversion; NI:5 'change is not weather' — one inversion; NI:6 'does not mark what it confirms' — suppressed-record; NI:7 'not noise, not interference, not a dropout' — triple-negative deliberate (the silence triple is a figure, not saturation); NI:8 'absence takes a shape' — no inversion; NI:9 'lets it settle nowhere' — suppressed-landing; NI:10 'the field where a name would go stays a field' — suppressed-act. Inverted-predicate count: NI:1, NI:2, NI:5 use a clear 'X does not Y' pattern = 3/10 = 30%. Below 40% AP-SCAN saturation threshold."
      why: "NI inverted-predicate saturation PASS (3/10 = 30% < 40% threshold)."

    - id: fault-032
      type: pass
      what: "sensory old-state anchors check. sensory:1 @5 'outer-court-stone-morning-ambient -> sapphire-flat-catch' — carries old_state ✓. sensory:2 @20 'outer-court-stone-morning-cold -> passage-arch-stone-hill-warm' ✓. sensory:3 @30 'feed-interior-silence -> one-exhalation' ✓. sensory:4 @32 'passage-arch-stone-hill-warm -> stone-morning-baseline' ✓. All four entries include old-state anchors."
      why: "sensory old-state rubric PASS."

    - id: fault-033
      type: flag
      what: "Card-resolution on new prop and field slugs: state-updates-env-b01-c15.md §Field-extensions lists margit referrals needed: prop:oc-coverage-record.card.md (new prop, 4 fields); studio.ambient_conditions.thermal-rise-status (new field); studio.fauna_sense_status.eastern-fringe-interference (new field); studio.fauna_sense_status.feed-density (new field; reconcile with b01c12+ fauna_sense_status schema). These are unresolved margit referrals noted in the facet file itself."
      why: "New prop:oc-coverage-record and three new studio sub-fields are used by state-updates without corresponding cards in the active warehouse. The state-updates rubric (frugality §field-extension protocol) requires field extensions to be flagged for margit referral — the file does this correctly. Not a HARD finding because the facet file self-flags and the referrals are captured inline. Noted as SIGNAL per audit dispatch instructions: 'the new prop:oc-coverage-record + studio sub-fields are flagged for margit referral — note as SIGNAL, not HARD.'"

    - id: fault-034
      type: pass
      what: "AP-SCAN saturation check on sparse facets (metaphor, memory, feeling — all ≤5% density). metaphor: 1 entry, refuse-log present and substantive (documents refused patterns and rubric references). No AP-pattern concentration in the single entry. memory: 2 entries, both carry clean source-attribution (spine citations, prior-chapter call-back). No AP-pattern. feeling: 2 entries, both somatic physical-register with expressed:no (suppressed affect, within cond-taylor-pov-behavior register). No AP-pattern."
      why: "Sparse-facet AP-SCAN saturation PASS."

    # ── SUMMARY ───────────────────────────────────────────────────────────────

    - id: summary-001
      type: pass
      what: "HARD count: 0. SIGNAL count: 3 (fault-005 vibes:5 tba token unresolved; fault-018 metaphor licensed-by tba tokens not written back; fault-033 margit referrals for new prop + 3 new studio sub-fields). Headline: CLEAN."
      why: "Phase 5 gate clears. HARD=0 satisfied."
```
