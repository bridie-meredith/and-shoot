---
audit:
  scope: chapter
  target: "chapters[b01c01].scenes[*] (Phase 5 substance-chunker pass)"
  timestamp: 2026-05-25
  findings:

    # ── CLASS C / CLASS D — HARD ──────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: C+D
      severity: HARD
      what: >
        s03 substance_delta.axes_in_motion[social_tether-prot-rise].target_delta_magnitude = 1.0
        and notes field reads "gain side of cl01b (journey-required cost cl01a already paid in scene 2)."
        Series cost ledger cl01b (memory.md line 1344) declares gain: "social_tether-prot-rise +2".
        The chapter contract for b01c01 also sets target_delta_magnitude: 1.0 for social_tether-prot-rise
        (memory.md line 1644-1646). The scene notes claim full settlement of cl01b with no partial-delivery
        qualification; the delivered magnitude (+1.0) is half the ledger-declared gain (+2).
      why: >
        If cl01b's gain is +2 and b01c01 settles it in full (as the notes imply), then one rank of
        social_tether-prot-rise is unaccounted for in the chapter and scene contracts: it is neither
        delivered here nor deferred to a downstream chapter. The book-level target for
        social_tether-prot-rise is +7 total across 20 chapters (memory.md line 1558-1561). If cl01b
        is a +2 event but b01c01 only books +1, the remaining +1 from cl01b has no anchor chapter —
        creating a gap in the ledger's coverage accounting that will surface as an orphan gain at
        /and-write Phase 6 bone-gate or /and-substance book Phase 3 roll-up validation.
      criteria: >
        One of the following must be true and stated unambiguously in the scene and chapter contracts:
        (A) The scene and chapter target_delta_magnitude for social_tether-prot-rise is corrected to 2.0
            and cl01b is fully settled here — which requires the chapter contract and roll-up table to
            reflect the revised magnitude; OR
        (B) The scene notes for s03 are revised to specify that cl01b is partially settled here (+1 of
            +2), name the downstream chapter that will book the remaining +1, and the chapter contract
            notes field for cl01b records the split explicitly; OR
        (C) The series cost ledger cl01b gain annotation is corrected from "+2" to "+1" to match the
            chapter/scene contracts — which requires verifying that the book-level roll-up and actor
            baselines for social_tether-prot-rise remain consistent at ±1 tolerance after the correction.
        The mismatch between ledger gain and scene delivery must be resolved in one direction; the
        current state leaves the accounting ambiguous.
      locator: "b01c01s03 / substance_delta.axes_in_motion[social_tether-prot-rise].target_delta_magnitude + notes; series cost_ledger cl01b.gain"

    # ── CLASS A — PASS ────────────────────────────────────────────────────────

    - id: pass-A-s01
      type: pass
      class: A
      severity: null
      what: >
        b01c01s01 schema conformance: axes_in_motion is empty [], axes_held has 6 entries all with
        rationale, density_target is a valid range (0.6-0.7), scene_conflict has all three required
        fields, stakes_axis (moral_framework) is present in axes_held.
      why: null
      criteria: null
      locator: b01c01s01

    - id: pass-A-s02
      type: pass
      class: A
      severity: null
      what: >
        b01c01s02 schema conformance: axes_in_motion has one entry (capability, direction: up,
        target_delta_magnitude: 1.0 > 0), axes_held has 4 entries all with rationale,
        density_target is a valid range (0.75-0.9), scene_conflict has all three required fields,
        stakes_axis (moral_framework) present in axes_held.
      why: null
      criteria: null
      locator: b01c01s02

    - id: pass-A-s03
      type: pass
      class: A
      severity: null
      what: >
        b01c01s03 schema conformance: axes_in_motion has one entry (social_tether-prot-rise,
        direction: up, target_delta_magnitude: 1.0 > 0), axes_held has 4 entries all with
        rationale, density_target is a valid range (0.65-0.8), scene_conflict has all three
        required fields, stakes_axis (social_tether-prot-rise) present in axes_in_motion.
      why: null
      criteria: null
      locator: b01c01s03

    # ── CLASS B — PASS ────────────────────────────────────────────────────────

    - id: pass-B-rollup
      type: pass
      class: B
      severity: null
      what: >
        Roll-up check: capability sum across scenes = 0.0 + 1.0 + 0.0 = 1.0 (chapter target: 1.0,
        exact). social_tether-prot-rise sum = 0.0 + 0.0 + 1.0 = 1.0 (chapter target: 1.0, exact).
        All four chapter-held axes (moral_framework, relational_anchor_status, political_register-prot,
        moral_legibility_to_self) are present in axes_held at every scene. No missing coverage.
      why: null
      criteria: null
      locator: "b01c01s01 + b01c01s02 + b01c01s03 / axes_in_motion + axes_held"

    # ── CLASS C — partial PASS (see fault-001 for the failing item) ───────────

    - id: pass-C-s01
      type: pass
      class: C
      severity: null
      what: >
        s01 contract-vs-text: chunk text matches all six axes_held claims. Prohibition framed as
        labor and daily choice (moral_framework); insect range noted but suppressed (capability);
        stitch-house two lanes over planted without naming (relational_anchor_status); self-
        accounting described as maintenance not reckoning (moral_legibility_to_self); no court
        content (political_register-prot); anonymity intact (social_tether-prot-rise). No cost_ledger
        anchor claimed. Consistent.
      why: null
      criteria: null
      locator: b01c01s01

    - id: pass-C-s02
      type: pass
      class: C
      severity: null
      what: >
        s02 contract-vs-text: chunk shows first insect deployment (capability +1.0, cl01a gain side).
        Crowd-clearing via insect-sense described; fever-read without contact described. Witnesses
        present (crowd has not re-compressed, crowd watches the foreign woman). The "does not make
        a decision / does not file it as one" phrasing directly enacts the moral_framework held
        rationale. Cost side of cl01a (witch-label formation) defers to s03 as authoring notes
        indicate; gain side (capability +1 deployed) is fully enacted in the chunk. Consistent.
      why: null
      criteria: null
      locator: b01c01s02

    # s03 Class C finding is consolidated into fault-001 above.

    # ── CLASS D — partial PASS (see fault-001 for the failing item) ───────────

    - id: pass-D-cl01a
      type: pass
      class: D
      severity: null
      what: >
        cl01a anchor proposed as b01c01s02 (gain side) + b01c01s03 (cost propagation). s02 chunk
        shows the deployment and crowd presence (gain side consistent). s03 chunk shows Oswyn
        watching and witch-label assembling (cost surface consistent). Split-anchor notation is
        supported by schema field-notes (non-destructive refinement per G4). Anchors are internally
        consistent with chunk content.
      why: null
      criteria: null
      locator: "b01c01s02 + b01c01s03 / cost_ledger cl01a"

    # ── CLASS E — PASS ────────────────────────────────────────────────────────

    - id: pass-E-thematic
      type: pass
      class: E
      severity: null
      what: >
        All four thesis axes covered across scenes without undeclared dramatization:
        moral_framework — dramatized in s01 chunk (prohibition as labor) and s02 chunk (prohibition
        not filed as cracked); declared held in all three scenes.
        capability — dramatized in s02 chunk (insect deployment); declared in_motion s02, held s01+s03.
        relational_anchor_status — Wren planted in s01 chunk (stitch-house two lanes over), crowd
        presence in s02 rationale, stitch-house smell in s03 chunk; declared held all three scenes.
        social_tether-prot-rise — confirmed nil s01, held s02 (witnesses present, embedding not yet
        formed), moved s03 (Oswyn awareness layer, ward-category shift); declared consistently.
        No scene dramatizes an axis without declaring it. No THEMATIC-AXIS-UNDECLARED findings.
      why: null
      criteria: null
      locator: "b01c01s01 + b01c01s02 + b01c01s03 / axes coverage vs chunk text"

    # ── CLASS F — PASS ────────────────────────────────────────────────────────

    - id: pass-F-density
      type: pass
      class: F
      severity: null
      what: >
        Scene-level chunk_targets: density_target 0.6-0.9; delta_per_signature_axis 0-1.5.
        s01: 0.6-0.7 (within bounds). s02: 0.75-0.9 (within bounds). s03: 0.65-0.8 (within bounds).
        Per-scene axis magnitudes: capability s02=1.0, social_tether-prot-rise s03=1.0, both within
        0-1.5 scene-level target. All within tolerance.
      why: null
      criteria: null
      locator: "b01c01s01 + b01c01s02 + b01c01s03 / density_target; chunk_targets scene"

    # ── CLASS G — PASS ────────────────────────────────────────────────────────

    - id: pass-G-naming
      type: pass
      class: G
      severity: null
      what: >
        Slug naming b01c01s01/s02/s03 — monotonic, conforms to Phase 6 convention. All axis slugs
        used in scenes (moral_framework, capability, relational_anchor_status, political_register-prot,
        moral_legibility_to_self, social_tether-prot-rise) match slugs used in series.substance
        cost_ledger and antagonist_pressure blocks. No stray or mismatched slugs.
      why: null
      criteria: null
      locator: "b01c01s01 + b01c01s02 + b01c01s03 / axes slugs + scene slugs"

  summary:
    hard_count: 1
    soft_count: 0
    verdict: REVISE
    note: >
      One hard finding (fault-001): mismatch between cost_ledger cl01b declared gain (+2) and
      the delivered magnitude in b01c01's chapter and s03 scene contracts (+1). The scene notes
      claim full settlement of cl01b without partial-delivery qualification, leaving one rank of
      social_tether-prot-rise unanchored in the ledger. All other classes pass: schema is
      well-formed, roll-up is exact, held axes are fully covered, chunk text enacts all
      substance_delta claims, density targets are within bounds, and axis slugs are consistent.
      Fix is scoped to either the cost ledger annotation, the scene/chapter contract magnitudes,
      or explicit partial-settlement notation — no structural change to the scene decomposition
      is required.
