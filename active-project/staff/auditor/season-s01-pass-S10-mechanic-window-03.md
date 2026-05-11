```yaml
audit:
  scope: season
  target: s01 — Window 3, IDs 330–494 + inserts 497/498/499/503/507 + boundary beats 513/514/515
  timestamp: 2026-05-11
  pass: S10 Sweep B — Mechanic verdict cycle 2 (narrow scope: AP-SCAN / CURVE-SHAPE / FREQUENCY-BAND)
  source: active-project/theater/proto-lines/s01.bones.md
  tensometer: active-project/theater/facets/tensometer-s01-window-03.md
  combined_verdict: MECHANIC-FAIL-AP-SCAN-CURVE-SHAPE-FREQUENCY-BAND

  cycle_1_resolutions:
    - fault-001: RESOLVED — IDs 355 and 449 now read "taylor-hebert-flea-bottom wakes". No interiority subject.
    - fault-002: RESOLVED — IDs 387/388 now relay physical actors (taylor-hebert-flea-bottom, oc-tanner-elder);
        ID 416 relays "the pen-scratch" (physical sound); ID 417 is now "oc-broken-maester sets the pen";
        ID 471 relays "the middleman" (physical actor). ID 339 now relays "the clerk" (physical actor).
        Note: resolution of ID 339 introduced a new fault (see fault-001-c2 below).
    - fault-003: RESOLVED — ID 469 now reads "the middleman takes the account". Adjective removed.
    - fault-004: RESOLVED — IDs 353, 447, 462, 493 deleted. Gaps visible in bones file as required by schema.
    - fault-005: PARTIALLY ADDRESSED — tensometer now authored; 3s now present in file. However, two
        tensometer 3s (@335, @368) fail rubric validation, reproducing CURVE-SHAPE fault for scenes
        330–342 and 361–375. See fault-002-c2 and fault-003-c2.
    - fault-006: PARTIALLY ADDRESSED — tensometer exists with distribution 66.9%/29.2%/3.9%.
        1s and 2s are within band. 3-frequency at 3.9% is below the 5% floor but author asserts
        honest rating. However: two 3s are misrated (fault-002-c2), which if corrected reduces
        3-frequency to ~2.6%, worsening the below-floor condition. See fault-004-c2.

  findings:

    - id: fault-001-c2
      type: fault
      what: >
        Bones file IDs 338 and 339 — both read "the flies relay the clerk" (identical SVO).
        File lines: "338 the flies relay the clerk" followed immediately by "339 the flies relay
        the clerk". These are adjacent, consecutive, exact duplicates.
      why: >
        AP-SCAN / structural duplication. The cycle-1 fix for fault-002 replaced ID 339's
        abstract-object content ("the flies relay the junction departure") with a physical actor
        ("the clerk"). That fix is correct in isolation, but the result produces an exact
        duplicate of ID 338, which already read "the flies relay the clerk". Two consecutive
        identical SVO proto-lines cannot both record discrete observable physical events —
        one is structurally redundant. This is the same AP-SCAN class as cycle-1 fault-004.
        Downstream consequence: the tensometer has @338 unrated (it falls before the window
        boundary at entry 9, rated 1) and @339 rated 1 — both scalars are valid, but the
        stitcher will render the same beat twice in prose. The tensometer entry for @339 (entry
        10, rated 1) survives the duplicate, but the facet pipeline treats them as two distinct
        beats. One stitcher compression is lost.
      criteria: >
        The 338/339 pair must resolve to a single proto-line, or ID 339 must be recast as a
        genuinely distinct physical beat from ID 338. If both relay beats represent the same
        single physical event, one must be deleted (leaving the gap visible). If they represent
        distinct relay moments separated by some interval, a distinguishing element (different
        verb, different observed detail, or an intervening beat) must make the distinction legible.

    - id: fault-002-c2
      type: fault
      what: >
        Tensometer entries:
        Entry 6 — "@335 3" (proto-line: "the clerk writes the entry", scene group 330–342);
        Entry 36 — "@368 3" (proto-line: "the second clerk writes the entry", scene group 361–375).
        Axis citation for both: "stakes-visibility + reversal-proximity peaks — clerk writes entry;
        registration IS the turn."
      why: >
        AP-SCAN / CURVE-SHAPE. Both entries assign rung 3 to routine administrative write beats
        with no on-face charge. The rubric requires a 3 to satisfy: peak reversal-proximity (the
        beat IS the turn), or peak stakes-visibility (the beat IS the exposure or commit), or
        peak body-charge (held at maximum compression). Against all three axes for @335 and @368:

        Stakes-visibility: "the clerk writes the entry" — no named character is at risk on the
        face of this SVO. The clerk is performing a routine administrative act. The rubric
        anti-pattern "Plot-importance inflation" applies: the writer knows this entry matters
        narratively (Taylor's network is being registered), but tensometer reads on-face charge,
        not narrative function. On-face: neutral.

        Reversal-proximity: the write beat extends the open-book action from the prior beat.
        The axis citation claims "registration IS the turn" — but registration of what, visible
        to whom, on the face of this beat? The SVO is "clerk writes entry." There is no
        named stake, no identified subject of the registration, no on-face reversal. Compare
        the rubric calibration example: "the stylus marks two parallel lines beside Taylor's
        entry" earns 2 because Taylor's name appears in the action and the officer is the actor —
        the stake is named on-face. Here, the stake is inferred from context, not present in
        the SVO.

        Body-charge: no body-charge on the face of this beat. The write act is neutral motion.

        The rubric's "Speech-beat default" anti-pattern has a direct parallel here: just as
        "X speaks to Y" defaults to 1 because speech content carries the charge, not the
        proto-line beat, "X writes the entry" defaults to 1 because the significance of the
        entry content is not on the face of the beat. Both @335 and @368 should be rated 1
        (or at most 2 if a specific named stake — e.g., an officer observing, Taylor's name
        in the entry — can be cited on-face, which the current SVO does not support).

        Downstream CURVE-SHAPE consequence: scenes 330–342 and 361–375 have no legitimate
        3-beat. With @335 and @368 corrected to honest ratings, both scenes have zero 3s and
        no dramatist exception flags. The rubric states: "Each scene must satisfy at least one
        3 OR an explicit dramatist-flagged exception." Scenes 330–342 and 361–375 fail this
        test. This reproduces the cycle-1 fault-005 CURVE-SHAPE finding for those two scene
        groups.
      criteria: >
        @335 and @368 must be rerated to their honest rung against at least one rubric axis.
        If no axis lights at 3, the entry must be rated 1 (default for routine write beats)
        or 2 only if a specific named on-face stake can be cited. Following rerating, scenes
        330–342 and 361–375 must either receive a proto-line that legitimately earns a 3
        (screen-writer kickback scope) or carry explicit dramatist exception flags
        (scene-as-transit / scene-as-respite). The axis-citation summary must be updated
        to reflect actual axis performance for whichever rung is assigned.

    - id: fault-003-c2
      type: fault
      what: >
        Tensometer entry 124 — "@462 2". ID 462 is a deleted proto-line (removed as part of
        cycle-1 fault-004 resolution). The bones file shows the ID 462 gap between 461 and 463.
        Tensometer entry 153 — "@493 1". ID 493 is a deleted proto-line (removed as part of
        cycle-1 fault-004 resolution). The bones file shows the ID 493 gap between 492 and 494.
      why: >
        AP-SCAN / cross-facet consistency. The tensometer cites two proto-line IDs that no
        longer exist in the bones file. Per the cross-facet contract: once a proto-line is
        deleted, any facet entry citing it is orphaned. The stitcher has no proto-line record
        to attach these tensometer scalars to. The downstream consequence at stitcher time:
        @462 and @493 are treated as beats to render, but the bones layer has no SVO for them
        — either the stitcher errors or produces a null-content beat. The tensometer's beat
        count is overstated by 2 (154 entries counting deleted bones → effective count 152).
        This also falsely inflates the frequency-band calculation: the 154-denominator used
        in the tensometer's own band calculation is wrong.
      criteria: >
        Tensometer entries @462 and @493 must be removed. The frequency-band calculation must
        be recomputed on the correct denominator (152 proto-lines, or the correct count after
        all orphan entries are removed). The bones-file deletion gaps at 462 and 493 are
        correct and must not be reinstated.

    - id: fault-004-c2
      type: fault
      what: >
        Tensometer frequency-band section states: "3s: 6/154 = 3.9% (target 5–10%) — slightly
        below floor." After removing orphaned entries @462 and @493 (fault-003-c2) and
        correcting misrated @335 and @368 from 3 to honest rungs (fault-002-c2): corrected
        3-count = 4 (remaining legitimate 3s: @394, @395, @417, @468); corrected denominator
        = 152. Corrected 3-frequency = 4/152 = 2.6%. The tensometer also omits entries for
        in-scope beats @513, @514, @515 (fault-005-c2 below), which if rated 1 push the
        denominator to 155 — corrected 3-frequency 4/155 = 2.6%. 2s: 45/152 = 29.6%
        (within band). 1s: 103/152 = 67.8% (within band).
      why: >
        FREQUENCY-BAND. The rubric frequency test states: a distribution outside the 5–10%
        3-rung band "suggests systemic miscalibration — investigate before shipping." The
        tensometer author noted 3.9% as "slightly below floor" and stated "scalar inflation
        refused." That position was honest given the bones, but two of the six 3s are
        misratings (fault-002-c2), not inflation refusals — they are ratings that fail the
        rubric's axis tests. With honest ratings applied, the true 3-frequency is 2.6%,
        which is 2.4 percentage points below the 5% floor — not a minor deviation. The
        rubric response to below-band 3-frequency is: if scalars are honest, the proto-line
        file does not contain enough charged beats. This is a screen-writer kickback signal:
        Window 3 bones require additional rupture / commit / registration proto-lines
        before tensometer can achieve an honest distribution within band. The cycle-1
        fault-006 finding assessed ~1–2 legitimate 3-level candidates at the bone layer
        before tensometer authoring. The tensometer confirms this: 4 legitimate 3s across
        154 beats reflects the same structural underload the cycle-1 audit identified.
        The bones additions (513/514/515) did not add charged beats; all three are ambient
        relay/write beats.
      criteria: >
        After resolving fault-002-c2 (rerating @335 and @368), fault-003-c2 (removing orphan
        entries), and fault-005-c2 (adding missing entries), the frequency-band section must
        be recomputed on the corrected population. If honest 3-frequency remains below 5%,
        the tensometer must emit a screen-writer kickback flag naming the specific scene groups
        that lack legitimate 3-candidates (minimum: scenes 330–342, 361–375, and 477–494).
        The kickback flag is the rubric-mandated response; scalar inflation is prohibited.

    - id: fault-005-c2
      type: fault
      what: >
        Tensometer file is missing entries for in-scope bones @513, @514, and @515.
        These three proto-lines appear physically in the bones file within the Window 3
        body (between the 329 gap and ID 330), were designated as Window 3 boundary beats
        by the cycle-1 fault-005 resolution, and are listed as in-scope in this audit's
        dispatch. No tensometer entries cite @513, @514, or @515.
      why: >
        AP-SCAN. The tensometer rubric states: "tensometer has no per-entry cull — every
        proto-line gets a scalar." Three in-scope proto-lines are unrated. Downstream
        consequence: the stitcher has no tension signal for these three beats. If the
        stitcher defaults to treating unrated beats as 1 (ambient), the compression contract
        is met, but the cross-facet contract is broken — facets that gate on tensometer
        rung (loudness flags, memory flags, audience-interest flags) will skip these beats
        without the auditor having validated whether a non-1 rating was warranted.
        Beat @515 ("taylor-hebert-flea-bottom writes the entry") is almost certainly 1,
        but @513 ("the beetles relay the base room") and @514 ("the beetles relay
        oc-broken-maester") sit at a boundary that contextually precedes a scene transition —
        context in which a 2 might be defensible if the relay constitutes charged surveillance.
        The determination belongs to the dramatist, not the stitcher's default.
      criteria: >
        Tensometer entries for @513, @514, and @515 must be authored and inserted at the
        correct physical position in the tensometer file (before the @330 entry). Each
        entry must name an axis citation if rated 2 or 3. If rated 1, no citation required.

    - id: fault-006-c2
      type: fault
      what: >
        Tensometer axis-citations summary entry for @417:
        "@417: reversal-proximity peaks — beetles relay cessation; stop reverses prior motion."
        Current proto-line content: "oc-broken-maester sets the pen" (rewritten in cycle-1
        fault-002 resolution from "the beetles relay the cessation").
      why: >
        AP-SCAN / citation consistency. The axis citation documents the old proto-line content
        ("beetles relay cessation") that was replaced during cycle-1 fixes. The current
        proto-line is "oc-broken-maester sets the pen." The citation is factually wrong: it
        names a subject (beetles) and object (cessation) that do not appear in the current
        bone. Any downstream consumer reading the axis-citations summary to verify the 3-rating
        for @417 receives incorrect information. The scalar itself (3) may be defensible
        on the current proto-line's merits — "sets the pen" is analogous to the rubric
        calibration example "the stylus stops on the board" (rated 3 when the stop reverses
        prior motion) — but the citation must document the current content, not the discarded
        draft. The rating of @417 at 3 requires fresh axis justification against the actual SVO.
      criteria: >
        The axis-citations summary entry for @417 must be rewritten to cite the current
        proto-line ("oc-broken-maester sets the pen") and name the axis or axes that
        support the assigned rung. If the 3 is defensible on the current content, document
        it. If it is not defensible on the current content, rerate to the correct rung.

    - id: flag-001-c2
      type: flag
      what: >
        Tensometer entries for @394 and @395 — both rated 3, interpreted as a double-tap
        (coin placed → fist closed). The lead-in at @393 ("taylor-hebert-flea-bottom extends
        the palm") is rated 2, satisfying the ramp requirement. However, the prior beats
        @391 ("taylor-hebert-flea-bottom exits the dock-side alley") and @392
        ("oc-tanner-elder speaks to taylor-hebert-flea-bottom") are both rated 1,
        producing a 1→1→2→3→3 shape in the coin-exchange sequence.
      why: >
        The cycle-1 audit flagged a 1→3 adjacency problem in this scene group. The tensometer
        resolves this by inserting @393 rated 2 as the ramp beat, which satisfies the rubric's
        "beats leading into a 3 should ramp through 2s" requirement. The single 2 before the
        double-tap is minimal but not a violation — the rubric does not specify how many 2s
        must precede a 3, only that the jump is not direct 1→3. The @392 rated 1 ("elder
        speaks to taylor") is defensible per rubric anti-pattern 2 (speech-beat default: 1).
        No fault. Flagging for editor awareness: the charge ramp is thin (one 2 before a
        double 3). The stitcher will weight this sequence heavily; editor should confirm
        the scene can carry the density load.
      criteria: ~

    - id: flag-002-c2
      type: flag
      what: >
        Scene group 477–494 (full circuit walk + log close). Tensometer rates the entire
        group: 477–491 all at 1 except @482 (enters Fish Gate margin, rated 2) and @488
        (spiders relay the window, rated 2). No 3 in the sequence. No dramatist
        exception flag.
      why: >
        The rubric requires each scene to contain at least one 3 OR an explicit exception flag.
        This scene group has no 3 and no flag. The two 2s (@482, @488) are plausible
        (entering a charged location edge, insect surveillance beat in a transit context) but
        neither earns a 3. The scene is structurally a transit/cool-down scene (full circuit
        walk, return to base, log close), which would qualify for a "scene-as-transit" exception
        flag. The dramatist has not issued that flag. This is a CURVE-SHAPE violation by the
        letter of the rubric. However, this is the window's final scene group and its transit
        function is apparent from the bones — this may be an oversight in flag notation rather
        than a structural failure. Classifying as flag rather than fault because the scene's
        transit character is defensible on inspection; the missing notation is the issue.
        Fixer or dramatist should either add the exception flag or confirm whether the scene
        requires a rupture beat.
      criteria: ~

    - id: flag-003-c2
      type: flag
      what: >
        ID gaps within Window 3 (cycle-1 flag-002 carried forward): gaps at 348/349,
        418/419, 442/443 from prior deletions; new gaps at 353, 447, 462, 493 from
        cycle-1 fault-004 resolution.
      why: >
        No fault — deletions are legal and gaps must remain visible per schema. Carrying
        forward for editor awareness. The Phase 7 split must not attempt to fill or
        recover these gaps. New gap at 462 is doubly confirmed: ID deleted from bones
        and orphan tensometer entry must also be removed (fault-003-c2).
      criteria: ~
```
