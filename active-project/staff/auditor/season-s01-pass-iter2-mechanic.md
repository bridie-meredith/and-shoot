```yaml
audit:
  scope: season
  target: s01-all-chapters (chapter-01 through chapter-10)
  timestamp: 2026-05-07
  findings:

    # ── CHAPTER 03 ─────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        chapter-03 body — IDs appear in non-monotonic file order throughout.
        After ID 60 the file body reads: 6, 7, 8, 9, 16, 3, 61 … 5, 68, 69, 39 … 21 …
        70, 45, 46, 47 … 27 … 34, 44, 33 … 37, 38, 40, 41, 42, 43.
        Multiple backward steps exist (e.g., 60 → 6 → 7; 67 → 5; 69 → 39; 47 → 71 → 72 → 27; 44 → 33).
      why: >
        The stitcher walks IDs in citation order. Non-monotonic file order means
        the proto-line file cannot serve as the authoritative sequence anchor;
        any downstream facet author reading the file top-to-bottom will misread
        the narrative order. Chapter-03 has no inline comment exempting its
        non-monotonic IDs (unlike ch06, which has an explicit inserted-IDs note).
        FAULT-FORM-ID-SEQUENCE.
      criteria: >
        Chapter-03 body must be reordered so IDs increase monotonically from top
        to bottom (gaps from deletions are permitted; backward steps are not).
        Alternatively, if the non-monotonic ordering reflects a deliberate
        citation-sequence design, an inline comment identical in form to the ch06
        inserted-IDs note must document every out-of-order block before this
        passes a constraint audit.

    # ── CHAPTER 07 ─────────────────────────────────────────────────────────────

    - id: fault-002
      type: fault
      what: >
        chapter-07, ID 95 (new beat): `septon-rowan produces the sealed parchment`
        The word `sealed` is an adjective modifying `parchment`.
      why: >
        Schema rule: "No modifiers. No adjectives, no adverbs."
        Adjective `sealed` is a result-state descriptor applied to the object.
        FAULT-FORM-MODIFIER.
      criteria: >
        The line must name the parchment without any adjective. The distinction
        between sealed and unsealed parchments, if load-bearing, belongs in the
        state-update or dialogue facet that cites this proto-line, not in the
        proto-line itself.

    - id: fault-003
      type: fault
      what: >
        chapter-07, ID 96 (new beat): `septon-rowan sets the parchment on the counter`
        The phrase `on the counter` is a prepositional phrase of place/destination.
      why: >
        Schema rule: "Prepositional phrases of place / destination / source /
        direction / instrument / accompaniment are explicitly banned.
        (FAULT-FORM-MODIFIER). Use a transitive verb that takes the location as
        direct object."
        `on the counter` is a prepositional destination phrase, not a direct
        object. The licensed form would be a transitive verb that names the
        counter as its object.
      criteria: >
        The line must eliminate the `on the counter` prepositional phrase.
        Destination information may be captured by using a transitive verb that
        takes the counter as direct object (e.g., `septon-rowan places the
        parchment`; location detail routes to the location-state facet).

    - id: fault-004
      type: fault
      what: >
        chapter-07, ID 64 (old material): `taylor-hebert-westeros sets the document down`
        The word `down` is a directional adverb.
      why: >
        Schema rule: "No modifiers. No adjectives, no adverbs."
        Directional adverbs (`down`, `up`, `away`, `aside`) modify the verb and
        are banned. FAULT-FORM-MODIFIER. This line survived prior passes; strict
        iteration-2 bias surfaces it.
      criteria: >
        The line must not contain a directional adverb. If the act of placing
        requires no directional qualifier to be physically observable, delete the
        adverb. If the direction is load-bearing, it routes to a location-state
        or state-update facet that cites this proto-line.

    # ── CHAPTER 08 ─────────────────────────────────────────────────────────────

    - id: fault-005
      type: fault
      what: >
        chapter-08, IDs 33, 34, 36, 40, 41 (all new beats, IDs 29–48 range):
          33 the recorder's hand crosses the counter
          34 ser-aemon-bracken's hand drops the document
          36 ser-aemon-bracken's hand presses the document
          40 the recorder's hand lifts the document
          41 the recorder's hand places the document
        Subject in each line is a possessive body-part construction
        (`the recorder's hand`, `ser-aemon-bracken's hand`).
      why: >
        Schema rule: "Subject is a named entity — actor slug, prop slug, or
        `the <noun>` for unnamed environment elements." Possessive constructions
        (`X's hand`) do not match any of the three licensed subject forms.
        An actor slug would be `the-recorder` or `ser-aemon-bracken`; `the hand`
        (bare) would be an unnamed environment element. The possessive hybrid is
        not licensed. These five lines share a single fault class;
        FAULT-FORM-MALFORMED-BEAT (subject not a legal entity slug).
      criteria: >
        Each line's subject must resolve to a licensed form: actor slug, prop
        slug, or `the <noun>`. The POV-filtered "only the hand is visible"
        narrative effect, if load-bearing, belongs in the narrator-interest or
        sensory facet that cites these proto-lines; it does not alter the
        required SVO subject form.

    - id: fault-006
      type: fault
      what: >
        chapter-08, ID 45 (new beat): `taylor-hebert-westeros wipes the upper lip`
        The word `upper` is an adjective modifying `lip`.
      why: >
        Schema rule: "No modifiers. No adjectives, no adverbs."
        `upper` is a descriptive/locating adjective. While `upper lip` is an
        anatomical set phrase, the mechanic rule admits no exceptions for
        anatomical familiarity. FAULT-FORM-MODIFIER.
      criteria: >
        The line must name the body part without the adjective. `the lip` is
        sufficient; specificity about which lip routes to a sensory or
        narrator-interest facet if load-bearing.

    # ── CHAPTER 09 ─────────────────────────────────────────────────────────────

    - id: fault-007
      type: fault
      what: >
        chapter-09, ID 31 (old material): `ser-harwick-plumm reaches for the page`
        The phrase `for the page` is a prepositional phrase.
      why: >
        Schema rule: "Prepositional phrases of place / destination / source /
        direction / instrument / accompaniment are explicitly banned.
        (FAULT-FORM-MODIFIER). Use a transitive verb that takes the location as
        direct object."
        `reaches for the page` uses a prepositional object rather than a direct
        object. The licensed form is a transitive verb taking `the page` as its
        direct object. This line survived prior passes; strict iteration-2 bias
        surfaces it.
      criteria: >
        The prepositional phrase `for the page` must be eliminated. If the
        physical act is an attempted reach (hand moves toward but does not
        succeed), that nuance routes to the feeling-flag or state-update facet;
        the proto-line records the observable act with a transitive verb.

    # ── CHAPTER 04 ─────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        chapter-04, ID 53: `a raven perches taylor-hebert-westeros`
        `perches` is used transitively with a person as the direct object
        (meaning: alights upon Taylor).
      why: >
        This transitive use of `perches` is internally consistent with the
        file's pattern of eliding `on/at` prepositions by treating the
        destination as a direct object (cf. `a fly lands the garden wall` in
        ch02, `the ravens lift the bell tower` in ch03). No adjective or
        prepositional phrase is present; the fault class is not triggered.
        Flagged as unusual usage that may be ambiguous to prose stitcher or
        facet author: `perches [on] taylor-hebert-westeros` vs. `perches
        [something onto] taylor-hebert-westeros`.
      why: Editor receives this as advisory; no fixer dispatch.

    # ── VERDICT ────────────────────────────────────────────────────────────────

    - id: verdict
      type: fault
      what: >
        FILE-LEVEL VERDICT: FAIL.
        7 fault-class findings (fault-001 through fault-007).
        1 flag (flag-001, non-blocking).
        Faults span: ch03 ID-sequence structural fault; ch07 IDs 95, 96, 64
        (modifier/prep-phrase); ch08 IDs 33/34/36/40/41 (possessive subject)
        and ID 45 (modifier); ch09 ID 31 (prep-phrase).
      why: >
        Mechanic faults in proto-lines propagate into facet authoring: facet
        authors cite proto-lines by ID and treat them as clean SVO anchors.
        A malformed proto-line (adjective in object, prep phrase, illegal subject)
        forces prose-level recovery at stitcher time rather than at the correct
        bone-structure stage.
      criteria: >
        All fault-class findings must be resolved by fixer before facet authoring
        begins on affected chapters (ch03, ch07, ch08, ch09).
```
