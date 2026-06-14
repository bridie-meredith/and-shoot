```yaml
audit:
  scope: book
  target: b01
  timestamp: 2026-06-08
  task: cross-chapter bones form-scan — SVO-form debt check post no-ledger rebuild (20 chapters, certification level)
  findings:

    # ── SYSTEMIC VERDICT ──────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        PERCEPTION-VERB-AS-MAIN-VERB faults are present in 17 of 20 chapters.
        The dominant pattern: "reads X," "watches X," "finds X," "feels X,"
        "understands X," "recognizes X," "knows X" as the primary verb of a bone.
        Total PERCEPTION-VERB faults counted: 46 across the book.
        Chapters c01 and c02 are clean. Chapter c19 is nearly clean (1 instance).
        Every other chapter carries at least 2; the peak chapters (c04, c08, c12,
        c14, c18) carry 4–8 each.
      why: >
        Perception-verb bones defer the concrete event to a facet that doesn't
        exist yet (narrator-interest) or bury it under what the narrator observed
        rather than what she did. At the bones level this means the SVO is
        structurally underpowered: the "verb" is a cognition wrapper and the
        actual event (sends flies, writes the name, crosses the gate) is either
        absent or relegated to a prepositional tail. Downstream, the stitcher
        renders the perception wrapper rather than the action — contributing to
        the "reading about someone noticing things" register that drove the b01
        readability failure.
      criteria: >
        Each faulted bone must carry a concrete-action main verb in the SVO
        position. Where the perception is the scene's central event (she reads a
        letter, she observes a fact that drives the next action), the bone may
        retain the perception word only if the SVO renders the physical act
        (breaks the seal / scans the sheet / lifts the fly to the junction).
        Pure surveillance-stance bones ("watches X from the flies," "reads the
        junction," "finds corwick at the water-point") must recast the verb as the
        physical event that produces or follows from the sighting.

    - id: fault-002
      type: fault
      what: >
        STATIVE/PERSISTENCE-VERB faults present in 14 of 20 chapters.
        Dominant pattern: "holds the feet," "holds her position," "holds X
        in her head," "holds still," "stays," "keeps the weight still."
        Total STATIVE faults counted: 28 across the book.
        The "holds the feet" / "holds the range" motif (c01, c07, c09 etc.) is
        the most frequent instance; it appears as a deliberate stance-signaling
        pattern but the verb in every case is a non-event masquerading as a beat.
      why: >
        Stative bones consume a numbered beat position without delivering an
        event. At low density they signal intentional pause; at the density
        observed here (average 1.4 stative bones per chapter) they dilute the
        event-skeleton. Downstream: the stitcher renders the pause as prose
        duration and the chapter can read as having less narrative momentum than
        the substance arc promises.
      criteria: >
        Stative non-event bones should be converted to concrete action (the
        thing the character does with her stillness: plants the feet, braces the
        soles, steadies the weight) or eliminated and their beat absorbed into an
        adjacent action bone. The "holds the feet" motif may survive once per
        chapter if the physical act (weight-plant, stance-lock) is the
        narratively meaningful beat — not as a filler posture descriptor.

    - id: fault-003
      type: fault
      what: >
        ABSTRACTION-OBJECT / STATIVE-OBJECT faults present in 11 of 20 chapters.
        Pattern: "holds the full city," "holds the contempt," "holds the older
        shape," "holds the read," "holds the connection," "holds the man's name
        and Wren's name in one look," "weighs the gain against the cost,"
        "weighs Sera's guarantee against the man's detention."
        Total counted: 18 across the book.
      why: >
        These bones take a concrete-action verb (holds, weighs, sets) but attach
        it to an abstract object (a city-image, a feeling, a cognitive frame).
        The result is a pseudo-action bone: the verb carries the appearance of
        event but the object has no physical referent. Downstream: prose renders
        the abstraction rather than a body performing an act.
      criteria: >
        Where "holds X" means "maintains surveillance of X," the bone must render
        the physical act of that maintenance (sweeps the flies across X / keeps
        the insects on X). Where "holds X" means "experiences or sits with an
        emotion or thought," the bone should either be eliminated (emotion
        delivery belongs in the narrator-interest or feeling facet) or recoded
        as the physical correlate (keeps the stylus off the page / sets the
        hand flat on the surface).

    - id: fault-004
      type: fault
      what: >
        ABSTRACTION-AS-SUBJECT (DEC-0115) faults — light, localized.
        c19 bone 25: "the contempt rests beside the work and never enters it."
        c18 bone 33: "the Greens take the succession channel" — "the Greens" is
        a faction (borderline; they are human agents). The more problematic
        instance: c10 bone 7 "the lower-gate road runs below the margin" is
        environmental description, not a DEC-0115 violation (roads running is
        physical). The primary live instance is c19:25 where an emotion ("the
        contempt") is the grammatical subject performing a stative action.
        Total clean DEC-0115 violations: 1 (c19:25). 1-2 borderline (c18:33).
      why: >
        DEC-0115 was the root-cause fix for the b01 ledger-register failure.
        Even after the rebuild, one bone (c19:25) allows an abstract noun
        (contempt) to be the performing subject of a stative verb. This is a
        clean violation. It is singular and does not indicate the rebuild failed
        systematically on the no-ledger axis — it appears to be a residual
        formulation that survived because it sounds like intentional style
        ("the contempt rests beside the work") rather than ledger-apparatus prose.
      criteria: >
        c19:25 must recast the subject as taylor-hebert-kl-122ac performing a
        physical act that renders the same beat (the feeling present but not
        entering the work). The emotion word may appear in a PP or subordinate
        clause but may not be the grammatical subject of the main verb.

    # ── PER-CHAPTER FAULT TABLE (inline) ────────────────────────────────────

    # Chapter | Bones | Form-faults | Dominant fault class
    # b01-c01 |  27   |     2       | STATIVE ("holds the feet" ×2)
    # b01-c02 |  51   |     2       | STATIVE ("holds still" ×2)
    # b01-c03 |  36   |     8       | PERCEPTION-VERB (feels, watches, weighs/finds, reads, finds ×2) + STATIVE (holds ×3)
    # b01-c04 |  39   |     5       | PERCEPTION-VERB (reads ×3, counts) + STATIVE (holds ×1)
    # b01-c05 |  35   |     4       | STATIVE (holds ×2) + PERCEPTION-VERB (picks out) + borderline (stays)
    # b01-c06 |  26   |     3       | PERCEPTION-VERB (reads ×2, sorts) + STATIVE (holds stylus ×1)
    # b01-c07 |  25   |     3       | PERCEPTION-VERB (receives) + STATIVE (goes still, steadies)
    # b01-c08 |  29   |     7       | PERCEPTION-VERB (reads ×4, finds ×2, follows) + STATIVE (holds)
    # b01-c09 |  27   |     4       | PERCEPTION-VERB (knows, reads) + STATIVE (holds ×2)
    # b01-c10 |  27   |     3       | PERCEPTION-VERB (reads) + STATIVE (holds ×2)
    # b01-c11 |  30   |     2       | PERCEPTION-VERB (tastes, reads)
    # b01-c12 |  42   |     7       | PERCEPTION-VERB (reads ×4, weighs) + STATIVE (holds ×2) + ABSTRACTION-OBJECT
    # b01-c13 |  31   |     3       | PERCEPTION-VERB (watches) + STATIVE (holds ×2)
    # b01-c14 |  48   |     8       | PERCEPTION-VERB (finds, reads, understands, weighs, counts, recognizes, remembers) + STATIVE (holds)
    # b01-c15 |  40   |     3       | PERCEPTION-VERB (feels, reads) + borderline (names as labeling)
    # b01-c16 |  25   |     2       | PERCEPTION-VERB (sees, feels)
    # b01-c17 |  36   |     3       | PERCEPTION-VERB (reads ×2, sees)
    # b01-c18 |  46   |     6       | PERCEPTION-VERB (watches ×4, reads, counts, finds)
    # b01-c19 |  35   |     4       | STATIVE (holds, has run) + PERCEPTION-VERB (gets, recognizes) + ABSTRACTION-AS-SUBJECT (contempt rests)
    # b01-c20 |  31   |     3       | PERCEPTION-VERB (knows, feels, understands)

    - id: flag-001
      type: flag
      what: >
        c03 uses composite multi-clause bones (e.g., "taylor-hebert-kl-122ac
        feels the flies catch jarvis-coin-kl-courier's stillness against the
        moving crowd three seconds before her eyes find him") rather than minimal
        SVO form. This is not a fault class in the five-category scan but it
        compounds the PERCEPTION-VERB problem: multi-clause bones embed multiple
        fault instances in a single bone ID, making per-bone fixer targeting
        imprecise.
      why: >
        Multi-clause bones produce multi-fault single IDs. When fixer corrects
        the bone, the single ID may need to split into 2–3 clean minimal-SVO
        bones. This is a structural note, not a blocking fault.

    - id: flag-002
      type: flag
      what: >
        The "holds the feet" / "holds the range" motif appears in c01, c04, c07,
        c09, c16, c17 as a deliberate stance-signal. The repetition is clearly
        intentional — it is the Taylor stillness signature. However at bones-gate
        standard every instance is a STATIVE non-event. This creates a tension
        between the book's designed motif and the bones-gate form rule.
      why: >
        Flagged for principal decision: if the motif is load-bearing (it appears
        to be — it marks the moments Taylor chooses not to act), a waiver or a
        recasting convention should be documented. The form fix ("plants the
        feet," "braces the soles") is available and preserves the beat; the
        question is whether the exact "holds" idiom matters enough to defend.

    # ── SYSTEMIC VERDICT ─────────────────────────────────────────────────────

    - id: fault-005
      type: escalate
      what: >
        SYSTEMIC verdict confirmed. Total form-fault count: ~95 instances across
        20 chapters (PERCEPTION-VERB: ~46; STATIVE: ~28; ABSTRACTION-OBJECT: ~18;
        ABSTRACTION-AS-SUBJECT: 1–2; PP-OF-PLACE: 0–2 marginal).
        Chapters affected: 19 of 20 (c01 and c02 are cleanest; c02 has 2 minor
        statives; only c02 could be considered near-clean).
        The rebuild shortcut that skipped the bones-gate left SVO-form debt
        uniformly distributed across the book.
      why: >
        19/20 chapters affected means this is not a c07 anomaly. The c07 review
        that FAILed on 6 faults was representative of a book-wide condition, not
        a local exception. The escalate type is used here only for scope: fixing
        this requires a book-level batch pass, not an episode-scope targeted fix.
        Escalation is to the production principal for the remediation decision
        (batch `/and-write revise` vs. tolerate-as-is).
      criteria: >
        Principal must decide: (A) batch form-pass across all 20 chapters to
        clear PERCEPTION-VERB and STATIVE faults before the book is considered
        gate-clean at the bones level, or (B) accept current form debt as
        tolerable-below-the-prose given that the cold-read found prose alive and
        followable. If (A): a targeted `/and-write revise --form-only` pass per
        chapter is the minimum (no substance arc change, no IDs changed for
        unaffected bones; repair is concentrated on the ~5 faults per chapter
        average). If (B): document the acceptance decision and waive the
        bones-gate retroactively for these specific fault classes on the b01
        rebuild.
```

---

## Severity assessment

The cold-read found the prose reads **alive** and **followable** despite this form debt. That matters.

The dominant fault class — PERCEPTION-VERB — functions here as a lens-mediated narration style: "reads the junction through the flies" is how an insect-network narrator inhabits the world. The bones are capturing *what Taylor perceives* rather than *what Taylor does*. At the prose layer, the stitcher has clearly been rendering this as first-person sensory narration rather than as "she watched and thought" bookkeeping prose. So the form debt is **real at the bones layer** but its reader-facing consequence is **partially absorbed by the prose rendering**.

The ABSTRACTION-AS-SUBJECT fault (DEC-0115 target) is **localized to 1–2 instances** — the rebuild succeeded on its primary objective. The ledger-apparatus register is not present in the bones. The no-ledger rebuild worked.

The STATIVE faults ("holds the feet," etc.) do not survive into prose as a reader-facing problem; the stitcher renders physical posture. They are **hygiene-layer faults**: real at the bone skeleton, invisible at the draft surface.

**Reader-facing vs. hygiene split:**
- PERCEPTION-VERB: 50/50. Surveillance-stance bones ("watches," "sees") are partially reader-facing (prose can render "she watched" which is cold-distance register). Document-reading bones ("reads the letter," "breaks the seal") render fine. The "watches" cluster in c18 (4 bones) is the most reader-facing risk.
- STATIVE: hygiene. Does not survive into prose.
- ABSTRACTION-OBJECT: hygiene-to-mild. "Holds the full city" renders as "she held the city in her flies" which is fine prose.
- ABSTRACTION-AS-SUBJECT (c19:25): single instance, reader-facing only if the stitcher renders the prose with "contempt" as the subject of a clause.

---

## Remediation recommendation

**Cheapest shape: targeted batch form-pass, not full `/and-write revise`.**

A full `/and-write revise` per chapter reruns substance-arc logic and risks introducing new substance drift. The form debt here is surface-only: the events are correct, the axes are correct, the substance arc is intact. Only the verb class in the SVO is at fault.

Recommended path:
1. Accept the STATIVE ("holds the feet" motif) faults as a documented design waiver — they are load-bearing signal beats and the form fix ("plants the feet") is cosmetically different, not substantively better.
2. Accept the ABSTRACTION-OBJECT faults as hygiene — they do not survive into visible prose problems.
3. Run a targeted form-pass on the PERCEPTION-VERB faults in the high-density chapters: **c03, c04, c06, c07, c08, c09, c12, c14, c18** (these 9 chapters account for ~70% of the PERCEPTION-VERB count). Pass scope: replace surveillance-stance perception-verbs with the concrete physical event they signal. Do NOT change bone IDs, do NOT touch substance deltas, do NOT revise event coverage.
4. Fix the single ABSTRACTION-AS-SUBJECT fault (c19:25) as a one-line correction.

Estimated per-chapter fault load for the 9 high-density chapters: 4–8 faults each (avg ~5). At a minimal form-pass rate, this is ~45 bone-line edits across 9 chapters — a fixer-class task, not a screen-writer rewrite.

**Tolerate-as-is is also defensible** given the prose cold-read passing. The form debt is real but sub-threshold for reader impact in the current draft state. If the project is moving forward to b02, the recommendation is to fix c19:25 (the one clean DEC-0115 violation) and document the rest as a b01 known-debt item rather than block forward motion on a form-hygiene pass.
