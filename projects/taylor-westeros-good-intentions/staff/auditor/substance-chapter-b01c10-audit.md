audit:
  scope: chapter
  target: b01c10
  timestamp: 2026-06-01
  findings:

    - id: fault-001
      type: fault
      what: >
        Chapter contract (memory.md line 5683, cl-world-d07 notes field) and scene s03
        substance_delta notes (b01c10-draft.md lines 175–181) both declare
        "cl-world-d07 completed." The cost-ledger entry at memory.md lines 1374–1377 defines
        cl-world-d07 gain as political_register-world +2. The chapter's
        target_delta_magnitude for political_register-world is 1.0 (chapter contract line 5679;
        scene s03 notes confirm "+1.0 of +1.0 chapter target drawn here"). Only +1.0 of a
        +2.0 total ledger gain is drawn this chapter. The "completed" declaration is false: the
        ledger entry retains +1.0 undistributed gain.
      why: >
        A "completed" label on a half-drawn ledger entry creates an accounting inconsistency in
        two downstream directions. If a subsequent chapter draws the remaining +1.0 from
        cl-world-d07, it will contradict the "completed" close declared here and the contract
        for that chapter will fail cost-ledger consistency. If no subsequent chapter draws the
        remaining +1.0, the gain is stranded — the world-axis allocation is under-delivered
        against the ledger's stated potential, and the series-level substance signature will
        show an unclosed entry. Either outcome corrupts the cost-ledger as an accounting
        surface for downstream audits.
      criteria: >
        The chapter contract and scene s03 notes must accurately reflect the draw state of
        cl-world-d07. Either: (a) the target_delta_magnitude for political_register-world is
        raised to 2.0 so that the full ledger gain is drawn and "completed" is accurate; or
        (b) the "completed" language is removed and replaced with language that states the
        partial draw and the remaining balance (e.g. "+1.0 of +2.0 drawn here; balance
        available for future allocation"), with the chapter contract notes updated to match.
        The cost and direction are not in dispute; only the completion status requires
        correction.

    - id: fault-002
      type: flag
      what: >
        Scene s04 substance_delta notes for moral_framework (b01c10-draft.md lines 269–274)
        state: "Systematic-override-rationalized threshold crossed ... The entry closes. The
        threshold does not re-open." The cost-ledger entry cl03a (memory.md lines 1350–1353)
        defines the total cost as moral_framework −2. The chapter draws −1.0 across s02 and
        s04 (−0.5 each tranche). The remaining cost −1.0 is undistributed.
      why: >
        The phrase "the threshold does not re-open" is narratively accurate (the moral
        milestone of systematic-override-rationalized is a one-way event) but the note is
        co-located with a ledger-draw annotation. A reader of the s04 notes could reasonably
        interpret this as the ledger entry cl03a being complete, when in fact −1.0 of −2.0
        cost remains available for future chapters. This does not produce an immediate
        accounting error (the note uses "threshold" language, not "completed" language), but
        it creates ambiguity that could mislead a downstream chapter contract author or auditor
        into treating cl03a as a closed entry.
      why: >
        This is a flag rather than a fault because the note's threshold-crossing claim is
        narratively correct and the ledger itself does not declare completion; the risk is
        misreading during downstream contract authoring, not a current accounting break. No
        fixer dispatch required, but the notes should be disambiguated before b01c11 contract
        is drafted.

    - id: fault-003
      type: pass
      what: >
        Check 1 — Contract-text match (bare-assertion Δ). All seven axes_in_motion entries
        across four scenes have described causes in the chunk text for their rank claims.
        No bare-assertion Δ found.
      why: ""

    - id: fault-004
      type: pass
      what: >
        Check 3 — THEMATIC-AXIS-UNDECLARED (URI-CONTRACT-THEMATIC-AXIS). Chapter goal thesis
        axes (moral_framework, position-prot-rise, moral_legibility_to_self) are all present
        in the chapter-level axes_in_motion declarations (memory.md lines 5684–5693). No
        undeclared thesis axis.
      why: ""

    - id: fault-005
      type: pass
      what: >
        Check 4 — Schema validity. All axes_in_motion entries have direction ∈ {up, down},
        target_delta_magnitude > 0, and valid axis slugs matching the state_axes definitions
        (memory.md lines 90–220). All axes_held entries carry rationale fields. All per-scene
        stakes_axis values are valid slugs present in axes_in_motion for their respective
        scenes. moral_legibility_to_self in s04 carries cost_ledger_anchor: null, which is
        permissible for a suppressed-recognition event without a ledger anchor.
      why: ""

    - id: fault-006
      type: pass
      what: >
        Check 5 — Chunk-tag protocol (URI-CHUNK-TAG-PROTOCOL). All four scenes carry
        [event:], [mechanism:], [force:], and [image:] tags on load-bearing spans. No
        concrete event, load-bearing image, or causal mechanism found untagged across s01–s04.
      why: ""

    - id: fault-007
      type: pass
      what: >
        Check 6 — Continuity. (a) Corwick introduced via Oswyn in c08: confirmed by s02
        chunk ("She has Corwick's name from Oswyn"). (b) Corwick withheld through c09:
        confirmed by handoff_in open_threads and s02 chunk ("holding it in the internal
        record that does not route to Jarvis"). (c) Taylor-Otto never meet directly: confirmed
        by s01 chunk explicit statement and [force: jarvis-as-only-channel-taylor-otto-never-direct]
        tag; consistent with chapter contract (memory.md line 5638–5639). No continuity
        breaks found.
      why: ""

    - id: fault-008
      type: pass
      what: >
        Check 2 — Cost-ledger consistency (direction and draw): cl-d07a, cl03b, cl-antag-d10,
        cl-world-d04, cl03a. All five entries have scene-level directions matching ledger gain
        or cost sides. No over-draw on any entry. cl-d07a: +1.0 of +2.0 drawn (no over-draw;
        balance noted for c14). cl03b: +1.0 of +4.0 drawn. cl-antag-d10: +1.5 of +4.0 drawn.
        cl-world-d04: +1.0 of +2.0 remaining drawn (partial noted). cl03a: −1.0 of −2.0
        drawn. fault-001 addresses the cl-world-d07 completion-label error separately.
      why: ""
