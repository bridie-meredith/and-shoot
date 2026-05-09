```yaml
audit:
  scope: season
  target: s01
  pass: S7
  label: facet-readiness
  timestamp: 2026-05-07
  file_level: FAIL
  chapters_present: 10 (chapter-01 through chapter-10)
  chapters_expected: 14 (per task dispatch)
  chapters_missing: chapter-11, chapter-12, chapter-13, chapter-14

  findings:

    # --- SCOPE FINDING ---

    - id: fault-001
      type: fault
      what: >
        Proto-line directory contains 10 chapter files (chapter-01 through
        chapter-10). Task dispatch specifies 14 proto-line files. chapter-11,
        chapter-12, chapter-13, chapter-14 do not exist.
      why: >
        Facet authoring for the full season cannot begin until all chapter
        proto-line files are present. Missing chapters produce a partial
        facet corpus with no cross-chapter continuity pass possible for
        the absent beats.
      criteria: >
        chapter-11, chapter-12, chapter-13, and chapter-14 must be authored
        and pass the per-chapter pipeline before season-scope facet authoring
        begins. If the season plan calls for fewer than 14 chapters, the task
        dispatch count must be corrected and this finding retired.

    # --- CHECK 1: CITATION-ANCHOR CLEANLINESS ---

    - id: pass-002
      type: pass
      what: All 10 present chapters (chapter-01 through chapter-10).
      why: >
        No pre-seeded citation anchors of any form ([loc-state:?],
        [<speaker>:<n>], or other facet-author placeholders) appear anywhere
        in any of the 10 files. Bone-only discipline is intact.

    # --- CHECK 2: ID STABILITY ---

    - id: fault-003
      type: fault
      what: >
        chapter-06, lines 46 and 50 and 66: IDs 106, 107, 108 appear in
        physical file position between IDs 38 and 55. File sequence reads:
        ...38, 106, 39, 40, 41, 107, 42...53, 54(skip), 108, 55...
      why: >
        Facet authors walk the proto-line file from top to bottom and author
        facet entries in top-to-bottom order. Encountering IDs 106, 107, 108
        embedded in the 38–55 range means the facet file will carry entries
        @106 and @107 before entries @39–@55, making the facet file
        non-monotonic in anchor order. Cross-facet consistency checks that
        compare facet entry positions against proto-line positions will produce
        incorrect ordering. Location-state facet authors will have no clean
        way to assign a contiguous environment window around these beats.
      criteria: >
        IDs 106, 107, 108 must be renumbered to IDs that fit monotonically
        between 38 and 39 (e.g. 38a, 38b, 38c if fractional IDs are adopted,
        or the file must be restructured so these IDs appear in the canonical
        ascending order relative to their narrative position). Alternatively,
        the three lines may be given new IDs above 108 and the narrative
        position note attached as a comment, but only if the proto-line schema
        explicitly licenses out-of-sequence IDs — which it does not at this
        time. The minimum fix is file reordering so IDs ascend monotonically
        when read top-to-bottom, with ID gaps for the deleted lines left in
        place. If renumbering is chosen, all three affected IDs must be
        treated as new ID assignments (schema: once assigned, never reused).

    - id: pass-004
      type: pass
      what: >
        ID stability in all other present chapters: chapter-01, chapter-02,
        chapter-03, chapter-04, chapter-05, chapter-07, chapter-08,
        chapter-09, chapter-10.
      why: >
        All ID gaps in these files are deletion gaps (schema-legal) or
        blank-numbered time-skip markers. No IDs are reused. No IDs appear
        out of ascending file order within any of these nine files.

    # --- CHECK 3: POV LEGIBILITY ---

    - id: flag-005
      type: flag
      what: >
        chapter-06 (line 1: "chapter: 06"), chapter-07 (line 1: "chapter: 07"),
        chapter-08 (line 1: "chapter: 08"), chapter-10 (line 1: "chapter: 10").
        Each of these files opens with one or two non-schema header lines
        (chapter: NN and title: <name>) before the required narrator: and goal:
        lines.
      why: >
        The proto-line schema specifies exactly two required header lines:
        narrator: and goal:, in that order, with a blank line following before
        the body. The extra chapter:/title: lines do not break facet authoring
        (narrator and goal are still present and legible) but are not in the
        schema. A facet-authoring tool or reviewer that validates header
        structure strictly will reject these files at the first line.
      criteria: null

    - id: pass-006
      type: pass
      what: >
        chapter-01, chapter-02, chapter-03, chapter-04, chapter-09: narrator
        and goal headers present, correctly formatted, blank line before body.
      why: null

    - id: pass-007
      type: pass
      what: >
        chapter-05 interlude marker: narrator: septon-rowan, goal present,
        and "# interlude: true — septon-rowan is not the series protagonist"
        comment present. Per memory rule (POV default + self-resolve),
        non-Taylor chapters must be marked interludes. This chapter complies.
      why: null

    - id: fault-008
      type: fault
      what: >
        chapter-06, chapter-07, chapter-08, chapter-10 all have
        narrator: taylor-hebert-westeros (standard POV) but none carry
        an interlude marker (correct — Taylor chapters are not interludes).
        However chapter-06 through chapter-10 all carry the non-schema
        chapter:/title: prefix lines. These four chapters are Taylor-POV
        and do not need interlude markers. This finding is about format only,
        separated from flag-005 because the fix is authoring scope (these
        files need the extra lines removed to pass a strict schema check),
        not editorial scope.
      why: >
        If a future tool auto-parses the first line as narrator:, it will
        read "chapter: 06" as the narrator slug, breaking all downstream
        POV-consistency checks for these four chapters.
      criteria: >
        The chapter:/title: prefix lines must be removed from chapter-06,
        chapter-07, chapter-08, and chapter-10 so each file opens with
        narrator: as its first line, matching the schema.

    # --- CHECK 4: EXTERNAL-OBSERVABLE SURFACE ---

    - id: fault-009
      type: fault
      what: >
        chapter-06, line 30 (ID 23): "septon-rowan crosses"
        Bare intransitive motion verb with no destination or object.
      why: >
        Schema: "Bare intransitive motion verbs without destination fault
        FAULT-FORM-NO-VERB. `taylor moves` is not observable; `taylor enters
        the yard` is." A state-updates facet author has no location to write
        into the <old> -> <new> field. A location-state facet author cannot
        anchor this beat to any environment. The line is not facet-citable
        for any positional or movement facet.
      criteria: >
        The line must supply a destination as a direct object
        (e.g. "septon-rowan crosses the room" or "septon-rowan crosses to
        the table"), making the physical movement observable and facet-citable.

    - id: fault-010
      type: fault
      what: >
        chapter-08, line 10 (ID 4): "an armed man plants the feet at the
        cottage door"
        "at the cottage door" is a prepositional phrase of place.
      why: >
        Schema: "Prepositional phrases of place / destination / source /
        direction / instrument / accompaniment are explicitly banned
        (FAULT-FORM-MODIFIER)." A facet author reading this line cannot
        rely on it as a clean SVO anchor; the modifier makes the line
        non-conforming and fixer must clean it before facet authoring begins.
      criteria: >
        The prepositional phrase must be removed. The destination information
        may be expressed as a transitive verb that takes the location as a
        direct object (e.g. "an armed man blocks the cottage door") or the
        beat split into two proto-lines if both the planting and the location
        are narratively load-bearing.

    - id: pass-011
      type: pass
      what: >
        All remaining proto-lines across chapter-01 through chapter-10 present
        physically observable actions. Somatic tells (holds the feet, holds
        the chin, presses the temples, pinches the nose, tilts the head,
        lifts the chin, lowers the eyes) are physical and externally
        observable. Narrow holds-license instances (holds the feet, holds
        the chin, holds the hands, holds the eyes, holds the spine) are
        properly licensed as body-part stillness-against-pressure uses.
      why: null

    # --- CHECK 5: SLUG RESOLVABILITY ---

    - id: pass-012
      type: pass
      what: >
        Named actor slugs across all 10 chapters: taylor-hebert-westeros,
        septon-dying-protector, oc-census-officer, septon-rowan,
        oc-plumms-man, oc-castellan-harrenhal, ser-harwick-plumm,
        ser-aemon-bracken, ser-edwyn-celtigar, westerosi-traveling-maester,
        oc-girl-from-hamlet (implied via "the girl" in chapter-02).
        All resolve to entries in cards/personas/INDEX.md.
      why: null

    - id: flag-013
      type: flag
      what: >
        chapter-07: "the recorder" appears as subject or speaker/listener
        in 9 lines (IDs 1, 2, 3, 6, 8, 9, 10, 11, 20, 21, 22, 24, 25, 26).
        No card slug is registered in cards/personas/INDEX.md for this entity.
        The schema licenses "the <noun>" for unnamed environment elements
        but the recorder has a sustained functional role across ch07 —
        speaking, stamping, entering records, closing ledgers — that goes
        beyond background fill.
      why: >
        Without a card slug, a state-updates facet author cannot write
        actor:<slug>.field entries for this entity. A feeling-flags author
        has no character fork to author against. This does not block
        location-state, tensometer, or memory facets, but it does limit
        state-updates and feeling-flags coverage for ch07.
      criteria: null

    - id: flag-014
      type: flag
      what: >
        chapter-08, line 10 (ID 4): "an armed man" used as subject.
        chapter-01, line 149 (ID 137): "the woman" used as subject.
        These are one-line or two-line walk-ons with no card slug.
      why: >
        Same limitation as flag-013 but lower severity — single-beat
        appearances with no sustained role. State-updates and feeling-flags
        facets cannot target these entities. Location-state, tensometer,
        and sensory facets are unaffected.
      criteria: null

    - id: flag-015
      type: flag
      what: >
        chapter-08, lines 22 (ID 16) and 31 (ID 25):
        "taylor-hebert-westeros speaks to westerosi-traveling-maester"
        (no article "the" before "westerosi-traveling-maester").
        All other lines that reference this entity as subject use
        "the westerosi-traveling-maester".
      why: >
        Inconsistent article use in the listener position of dialogue beats.
        This does not break slug resolution (the slug is still recognizable)
        but is a formatting inconsistency that a strict parser treating
        "westerosi-traveling-maester" and "the westerosi-traveling-maester"
        as different subjects would misread.
      criteria: null

    # --- CHECK 6: DENSITY APPROPRIATENESS ---

    - id: pass-016
      type: pass
      what: >
        chapter-01 (~90 content lines), chapter-02 (~80), chapter-03 (~37),
        chapter-04 (~95), chapter-05 (~65), chapter-06 (~100),
        chapter-07 (~70), chapter-09 (~85), chapter-10 (50).
        All within range where facet density caps (tensometer: every line;
        sensory ≤3/scene, 3-6%; feeling 2-5%; metaphor 0-3%; memory sparse)
        can be honored without creating either a starved anchor set or
        an over-dense authoring problem.
      why: null

    - id: flag-017
      type: flag
      what: >
        chapter-08: approximately 32 facet-citable content lines remain after
        the two large deletion blocks (IDs 29-60 and IDs 65-88, totaling 55
        deleted or absent lines). The chapter's goal names three narrative
        deliverables (maester's report, Bracken filing, Celtigar letter read
        aloud) but only the maester's report and the chapter-close beats
        have surviving proto-lines. No proto-lines for Bracken's filing or
        Celtigar's letter read aloud are present in the file — the beats in
        those ID ranges (29-60 and 65-88) are entirely absent.
      why: >
        The chapter goal cannot be delivered on the declared facets if the
        beats that constitute two of its three deliverables have no proto-line
        anchors. A tensometer author cannot score Bracken/Celtigar beats.
        A narrator-interest author cannot flag Taylor's reaction to them.
        A state-updates author cannot record the consequential state changes
        those beats would carry. If the deletions are permanent, the chapter
        goal must be revised to match the surviving beats; if the deletions
        are placeholder gaps awaiting authoring, the missing proto-lines must
        be authored before facet authoring begins.
      criteria: null

    # --- CHECK 7: CROSS-CHAPTER REFERENT STABILITY ---

    - id: pass-018
      type: pass
      what: >
        All named slugs that appear in multiple chapters use consistent slug
        forms across all appearances:
        taylor-hebert-westeros (ch01-ch10), septon-rowan (ch04, ch05, ch06,
        ch07, ch09, ch10), ser-harwick-plumm (ch04, ch05, ch07, ch09, ch10),
        oc-castellan-harrenhal (ch04, ch07, ch09, ch10), ser-aemon-bracken
        (ch09), ser-edwyn-celtigar (ch09, ch10), westerosi-traveling-maester
        (ch08), septon-dying-protector (ch01, ch06).
      why: null

  # --- FILE-LEVEL VERDICT ---

  file_level_verdict: >
    FAIL. Two faults block immediate facet authoring: fault-001 (4 chapter
    files absent), fault-003 (chapter-06 ID out-of-sequence), fault-008
    (schema header format in chapters 06, 07, 08, 10), fault-009
    (chapter-06 bare motion verb), fault-010 (chapter-08 FAULT-FORM-MODIFIER).
    The four present-chapter faults (003, 008, 009, 010) are file-scope and
    fixable without plan-level changes. fault-001 is a missing-artifact fault
    requiring screen-writer to author and pipeline-pass four additional
    chapters. Flag-017 (chapter-08 goal-vs-beats mismatch) should be resolved
    by the orchestrator before chapter-08 facet authoring is scheduled:
    either the deletion gaps are filled with proto-lines or the chapter goal
    is revised to match the surviving beats.

    Unblocked chapters (facet authoring may begin once chapter-level faults
    are resolved): chapter-01, chapter-02, chapter-03, chapter-04, chapter-05,
    chapter-07, chapter-09, chapter-10.

    Blocked chapters pending specific fixes:
      - chapter-06: fault-003 (ID reordering) + fault-008 (header) +
                    fault-009 (bare motion verb).
      - chapter-08: fault-008 (header) + fault-010 (FAULT-FORM-MODIFIER) +
                    flag-017 advisory (goal/beat gap).
      - chapter-11 through chapter-14: not yet authored (fault-001).
```
