```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  gate: /and-write Phase 6 substance bone-gate (revise --from-signals; 4 new bones)
  findings:

    # ─── PER-BONE CHECKS ────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: "A1 (b01c05s02n01a) — cost_ledger_anchor: cl-d05"
      why: "cl-d05 is a confirmed entry in series.substance.cost_ledger[] (memory.md line 1362-1365; gain: political_register-prot +3; cost: opportunity-missed; anchor: book b01). A1 is chatter substrate paying cl-d05's first tranche (+1.5 on political_register-prot at @25 in s03). CHATTER-UNPAID does not fire."

    - id: pass-002
      type: pass
      what: "C1 (b01c05s03n06a) — cost_ledger_anchor: cl-d05"
      why: "Same ledger entry as A1. C1 is chatter substrate paying the same cl-d05 mechanism: the rushwick-feed holding the color is the apparatus-level event that makes @25 (Taylor stops the rushwick-pass) read as response. cl-d05 valid. CHATTER-UNPAID does not fire."

    - id: pass-003
      type: pass
      what: "B1 (b01c05s02n03a) — HELD-AXIS-UNCONTRACTED check"
      why: "Bone cites axis: moral_framework as held. s02 contract axes_held (memory.md lines 3611-3621) includes moral_framework with rationale 'routing enforcement as pattern-data is inside the licensed exception.' Axis is in s02's contracted axes_held. HELD-AXIS-UNCONTRACTED does not fire."

    - id: pass-004
      type: pass
      what: "B1 (b01c05s02n03a) — HELD-AXIS-NOT-ENACTED check"
      why: "SVO: 'the courier raises the spine.' The courier's physical recovery is part of the observable enforcement incident Taylor is routing as movement-pattern. The licensed exception (routing enforcement as pattern-data) is unaffected by the courier's body-recovery. The bone enacts the moral_framework hold by being a directly observable physical event that falls squarely within the feed's categorization scope. Discipline-enactment present. HELD-AXIS-NOT-ENACTED does not fire."

    - id: pass-005
      type: pass
      what: "B2 (b01c05s02n06a) — HELD-AXIS-UNCONTRACTED check"
      why: "Bone cites axis: moral_framework as held. s02 contract axes_held includes moral_framework (same entry as pass-003). Axis contracted. HELD-AXIS-UNCONTRACTED does not fire."

    - id: pass-006
      type: pass
      what: "B2 (b01c05s02n06a) — HELD-AXIS-NOT-ENACTED check"
      why: "SVO: 'taylor-hebert-kl-122ac drafts the jarvis-report.' The s02 chunk explicitly names this action: 'Taylor begins the Jarvis report in the same register she uses for passage-avoidance patterns and junction-agitation clustering.' Drafting in the licensed register enacts the moral_framework hold — the routing-name is honored without interrogation; the factual-movement-pattern discipline is intact at the action layer. Discipline-enactment present. HELD-AXIS-NOT-ENACTED does not fire."

    # ─── PER-SCENE CHECKS ───────────────────────────────────────────────────

    - id: pass-007
      type: pass
      what: "s02 — EVENT-MAP coverage post-integration (15 bones: 12 existing + A1 + B1 + B2)"
      why: "A1 strengthens 'cf-d10-courier-face thread initiated' (existing @8 courier entry now has a feed-apparatus recurrence event). B1 strengthens 'enforcement incident, courier retained on feet' (spine-raise disambiguates @14 'finds the feet'). B2 strengthens 'Taylor routes the enforcement incident to Jarvis as a factual movement-pattern report' (drafting is now bone-realized). All three new bones cover already-existing event_map entries; no new uncovered events introduced. EVENT-UNCOVERED does not fire."

    - id: pass-008
      type: pass
      what: "s02 — per-axis Δ aggregate post-integration"
      why: "s02 contract: axes_in_motion: [] (zero movement). All 3 new bones are either chatter (A1: axis_moves: []) or held (B1, B2: axes_held only; no axis_moves). Aggregate Δ across s02 remains 0. SUBSTANCE-FLAT / AXIS-UNDERDELIVERED do not fire (the target is zero movement; zero is delivered)."

    - id: pass-009
      type: pass
      what: "s02 — held-axes witness coverage post-integration"
      why: "s02 axes_held: political_register-prot, moral_framework, capability, relational_anchor_status. B1 and B2 both add moral_framework witness. Existing bones handle political_register-prot, capability, and relational_anchor_status witness. No regression in held-axis witnessing from the addition."

    - id: pass-010
      type: pass
      what: "s02 — stakes-axis (moral_framework) in union"
      why: "s02 scene_conflict stakes_axis is moral_framework. moral_framework remains in s02's axes_held union post-integration. STAKES-AXIS-MISSING does not fire."

    - id: pass-011
      type: pass
      what: "s02 — opposing-force visible post-integration"
      why: "s02 opposing_force: 'the enforcement incident's specificity / categorization absorbing content it was not built to process.' Existing bones @10-@13 (three figures pinning courier) and @15-@16 (Taylor filing) make this visible. B1 (courier spine-raise as part of the observable incident) and B2 (drafting the Jarvis-report) strengthen the opposing-force depiction rather than occlude it."

    - id: pass-012
      type: pass
      what: "s03 — EVENT-MAP coverage post-integration (13 bones: 12 existing + C1)"
      why: "C1 strengthens 'political_register-prot opens its account; neutral-instrumentally-observant foreclosed; cl-d05 anchor lands.' No new uncovered events introduced. EVENT-UNCOVERED does not fire."

    - id: pass-013
      type: pass
      what: "s03 — per-axis Δ delivered post-integration"
      why: "s03 contract: axes_in_motion target is political_register-prot +1.5 anchored to cl-d05. Existing @25 carries +1.5 (aggregate exact). C1 (axis_moves: [], cost_ledger_anchor: cl-d05) is chatter substrate; it does not move the axis. Aggregate at exactly +1.5. No underdelivery. AXIS-UNDERDELIVERED does not fire."

    - id: pass-014
      type: pass
      what: "s03 — stakes-axis (political_register-prot) dominance"
      why: "s03 axes_in_motion contains only political_register-prot. No new axis movement added by C1. STAKES-AXIS-NOT-DOMINANT does not fire (single axis in motion is trivially dominant)."

    - id: pass-015
      type: pass
      what: "s03 — cost-ledger paid (cl-d05)"
      why: "cl-d05 (political_register-prot +3; cost: neutral-instrumentally-observant foreclosed) is confirmed in series.substance.cost_ledger[]. C1 ('the rushwick-feed holds the color') is explicitly the apparatus-level mechanism that opens political_register-prot's account; the held color IS the cl-d05 substrate. The existing @25 carries the +1.5 axis move with cost_ledger_anchor: cl-d05. The cost is paid at the named anchor. COST-NOT-PAID does not fire."

    # ─── REGISTER-AS-MANNERISM CHECK ────────────────────────────────────────

    - id: pass-016
      type: pass
      what: "URI-WRITE-REGISTER-MANNERISM — verb-object pair check across integrated 35-bone set"
      why: |
        New verbs checked against the integrated bone set:
        - "holds the color" (C1): first occurrence of this V-O pair. "holds the rushwick-pass" appears twice (@29, @31) but that is a distinct object; the V-O pair "holds the rushwick-pass" reaches 2, which is under the ≥3 threshold.
        - "holds the wall-line" (@9): 1 occurrence.
        - "returns the courier" (A1): first occurrence; "returns the sound" (@13) is a distinct V-O pair; "returns" verb-only count is 2, but the threshold is V-O pair, not verb alone.
        - "raises the spine" (B1): first occurrence of this V-O pair.
        - "drafts the jarvis-report" (B2): first occurrence of this V-O pair.
        No verb-object pair in the integrated 35-bone set reaches ≥3 occurrences. REGISTER-AS-MANNERISM does not fire.

    # ─── DATA-LIMIT FLAG ────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: "CHATTER-OVER-CAP verification incomplete — per-bone substance_delta for existing 31 bones not accessible from flat bones file or memory.md b01c05 section"
      why: |
        The flat bones file (active-project/theater/bones/b01-c05.md) contains SVO only; it does not carry per-bone substance_delta. The memory.md b01c05 chapter entry provides scene-level contracts but does not enumerate per-bone records (unlike b01c01 which had full per-bone records in memory). Without per-bone substance_delta for the existing 31 bones, an exact chatter count per scene cannot be derived from available data.

        Partial analysis from available data:
        - s02: 15 bones post-addition; density_target.min = 0.55; cap = (1-0.55)×15 = 6.75 → max 6 chatter bones.
        - s03: 13 bones post-addition; density_target.min = 0.60; cap = (1-0.60)×13 = 5.2 → max 5 chatter bones.
        - A1 is 1 chatter bone added to s02; C1 is 1 chatter bone added to s03.
        - The existing 31 bones held a prior bone-gate PASS, meaning their pre-addition chatter counts were within cap at their respective bone-counts (s02: 12 bones, cap was (1-0.55)×12 = 5.4 → max 5; s03: 12 bones, cap was (1-0.60)×12 = 4.8 → max 4).
        - Adding 1 chatter bone each raises the cap ceiling by approximately 0.45 (s02) and 0.8 (s03) due to the larger bone_count in the denominator. If s02 had exactly 5 chatter bones pre-addition (at cap), it now has 6 chatter against a cap of 6.75 — still within cap. If s03 had exactly 4 chatter bones pre-addition (at cap), it now has 5 chatter against a cap of 5.2 — still within cap.
        - Worst-case analysis shows both scenes remain within cap even if prior chatter counts were exactly at prior caps.

        Assessment: CHATTER-OVER-CAP is unlikely to fire based on worst-case analysis, but cannot be verified exactly from available data. This flag does not block the gate; it is advisory for the next /and-write full-bone-record emit.

    # ─── SUMMARY ────────────────────────────────────────────────────────────

  verdict: PASS
  verdict_notes: |
    All 4 new bones (A1, B1, B2, C1) pass per-bone verification:
    - A1, C1 (chatter): cl-d05 confirmed valid in cost_ledger[]; payment logic intact; no CHATTER-UNPAID.
    - B1 (held): moral_framework in s02 axes_held contract; courier spine-raise enacts the licensed-exception hold; no HELD-AXIS-UNCONTRACTED or HELD-AXIS-NOT-ENACTED.
    - B2 (held): moral_framework in s02 axes_held contract; drafting Jarvis-report enacts the licensed-exception hold; no HELD-AXIS-UNCONTRACTED or HELD-AXIS-NOT-ENACTED.

    Per-scene verification (s02: 15 bones; s03: 13 bones) passes on all axes:
    - No event_map gaps introduced.
    - No axis-movement added where contract specifies zero movement (s02) or disrupts exact target (s03 +1.5 unchanged).
    - Held-axis witness coverage intact.
    - Stakes-axis in union for both scenes.
    - Opposing-force visible in both scenes.
    - cl-d05 cost paid at named anchor.

    Register-as-mannerism: no V-O pair reaches ≥3.

    One data-limit flag (flag-001): CHATTER-OVER-CAP cannot be verified exactly from flat bones file alone. Worst-case analysis clears; flag is advisory only.

    Zero HARD findings. Zero SIGNAL findings requiring disposition. Gate: PASS.
```
