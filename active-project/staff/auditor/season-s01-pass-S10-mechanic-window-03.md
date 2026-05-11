```yaml
audit:
  scope: season
  target: s01 — Window 3, IDs 330–494 + inserts 497/498/499/503/507 + boundary beats 513/514/515
  timestamp: 2026-05-11
  pass: S10 Sweep B — Mechanic verdict cycle 3 (re-fire of cycle 2; URI-026 cap = 2, iteration 2)
  source: active-project/theater/proto-lines/s01.bones.md
  tensometer: active-project/theater/facets/tensometer-s01-window-03.md
  combined_verdict: MECHANIC-FAIL

  cycle_2_resolutions:
    - fault-001-c2: RESOLVED — ID 338 now reads "the flies relay the junction"; ID 339 now reads
        "the flies relay the clerk". SVOs are distinct. Duplication cleared.
    - fault-002-c2: RESOLVED — @335 rerated from 3 to 2; @368 rerated from 3 to 2.
        Tensometer entries confirm: line 6 "@335 2", line 36 "@368 2".
    - fault-003-c2: RESOLVED — @462 and @493 orphan entries are marked removed via comment lines
        ("# @462 orphan removed (proto-line deleted in cycle 1 dedup)" and
        "# @493 orphan removed (proto-line deleted in cycle 1 dedup)"). Cross-facet orphans cleared.
    - fault-005-c2: RESOLVED — Tensometer entries for @513 (2), @514 (2), and @515 (1) now present
        at positions 0a, 0b, 0c. All three boundary beats rated. Axis citations not required for
        the two 2s under dispatch direction (boundary-carry; dispatch acknowledged 2 as defensible
        surveillance context).
    - fault-006-c2: RESOLVED — Axis citation for @417 now reads "oc-broken-maester sets the pen;
        the discrete act of stopping his writing reverses prior motion (the pen-scratch session
        terminates)." Citation documents current SVO correctly. Rating of 3 is defensible: the
        rubric calibration anchor "the stylus stops on the board" (rated 3) is directly parallel —
        pen set down reverses prior continuous motion; reversal-proximity peaks.
    - fault-004-c2: PARTIALLY ADDRESSED — see fault-001-c3 below.
    - flag-001-c2: No change required. Carried for editor awareness (coin-exchange ramp thin
        but not a violation). No new finding.
    - flag-002-c2: No change. 477–494 transit exception flag still absent. Carried as
        STRUCTURAL-RESIDUAL per dispatch.
    - flag-003-c2: No change. ID gaps carried per schema.

  structural_residuals_acknowledged:
    - CURVE-SHAPE: Scenes 330–342 and 361–375 have no 3-rated beat and no dramatist exception flag
        after honest rerating of @335 and @368. Scene group 477–494 (full circuit walk) has no 3
        and no exception flag. These are bones-deficit conditions: the proto-line file does not
        contain rupture/commit/registration beats that would legitimately earn 3 in those scene
        groups. Tensometer ratings are honest. Kickback to screen-writer is the correct response;
        scalar inflation is prohibited.
    - FREQUENCY-BAND: Corrected 3-count = 4 (@394, @395, @417, @468). Corrected denominator =
        152 body entries (154 total entries minus 2 orphans commented out) + 3 boundary entries
        = 155 rated entries. 4/155 = 2.6% (or 4/152 = 2.6% body-only). Both measures below
        the 5% floor. This is a bones-deficit condition: Window 3 does not contain enough
        charged beats to support an honest 3-frequency within band. Acknowledged as
        STRUCTURAL-RESIDUAL (bones deficit, not miscalibration).

  findings:

    - id: fault-001-c3
      type: fault
      what: >
        Tensometer frequency-band section (tensometer file lines 170–175) still reads:
        "3s: 6/154 = 3.9% (target 5–10%) — slightly below floor." and
        "Scalar inflation refused."
        Current actual 3-count in the tensometer: 4 (@394, @395, @417, @468).
        Current actual denominator: 155 rated entries (152 body entries with orphans
        commented out, plus 3 boundary entries at positions 0a/0b/0c).
        The frequency-band section was not updated when cycle-2 changes were applied
        (rereating @335 and @368 from 3 to 2 removed two 3s; adding @513/@514/@515
        added three rated entries). The summary arithmetic is factually wrong.
        Additionally: the rubric states the response to honest below-band 3-frequency
        is a screen-writer kickback flag naming the specific scene groups that lack
        legitimate 3-candidates. The tensometer file contains only a "Screen-writer flag
        (advisory)" for the maester-market trip (IDs 400–422). It does not contain the
        rubric-mandated kickback flag naming scenes 330–342, 361–375, and 477–494 as
        lacking legitimate 3-candidates. The fault-004-c2 criteria explicitly required
        this flag be emitted.
      why: >
        AP-SCAN. Any downstream consumer reading the frequency-band section to assess
        tensometer distribution receives incorrect data (3-frequency stated as 3.9% from
        a count of 6, actual is 2.6% from a count of 4). The cross-facet contract assumes
        the tensometer header accurately summarizes the scalar distribution. The missing
        screen-writer kickback flag is a rubric compliance gap: the rubric mandates the
        flag as the response to honest below-band 3-frequency; without it, the pipeline
        has no upstream signal to screen-writer that Window 3 bones require additional
        rupture/commit/registration beats before facet work can achieve an honest
        distribution within band.
      criteria: >
        The frequency-band section must be recomputed to reflect the current rated
        population: 3-count = 4, denominator = 155 (152 body + 3 boundary), 3-frequency
        = 4/155 = 2.6%. The 1-count and 2-count must also be verified against actual
        entries and updated if incorrect. Following recomputation, the tensometer must
        emit a screen-writer kickback flag (distinct from the existing advisory flag)
        naming scenes 330–342, 361–375, and 477–494 as lacking legitimate 3-candidates
        per rubric axis test. The kickback flag text must name the deficiency as a
        bones-deficit condition and prohibit scalar inflation as the remedy. The existing
        "Screen-writer flag (advisory)" for the maester-market trip may be retained
        separately; it does not satisfy the rubric-mandated kickback requirement.

    - id: flag-001-c3
      type: flag
      what: >
        Boundary-beat ratings @513 (2) and @514 (2) at tensometer positions 0a and 0b.
        No axis citations provided for either 2-rated entry.
      why: >
        The rubric states: "a facet entry rated 2 must answer: what specifically is charged
        on the face of this beat?" (rung-2 test). The tensometer header ("Boundary-carry
        bones (W3 open, post-cycle-1 regen)") gives context but no per-entry axis citation.
        @513 ("the beetles relay the cold candle") and @514 ("the beetles relay
        oc-broken-maester") may defensibly earn 2 as charged surveillance beats at a
        scene-transition boundary — beetles relaying a named actor (oc-broken-maester)
        is a stakes-visibility 2 candidate; beetles relaying an environmental detail
        (cold candle) is weaker. Both are defensible in context but uncited.
        Classifying as flag rather than fault: the dispatch acknowledged the 2 ratings
        as defensible for surveillance context, and per-entry citations for boundary-carry
        positions are not explicitly required by the schema. No fixer dispatch needed.
        Editor should confirm axis justification for @513 and @514 is stable before
        stitcher-lock.
      criteria: ~

    - id: flag-002-c3
      type: flag
      what: >
        Scene group 477–494 (full circuit walk). No 3. No dramatist exception flag.
        Carried from flag-002-c2 with STRUCTURAL-RESIDUAL designation confirmed by dispatch.
      why: >
        Transit function of the scene is apparent from bones (full circuit walk, return
        to base, log close). Exception flag notation ("scene-as-transit") would resolve
        this against the rubric's scene-level shape requirement. Notation is still absent.
        The structural residual is acknowledged by dispatch; no fixer dispatch is blocked
        on this, but the exception flag should be added at and-wrap or next mechanic pass.
      criteria: ~

    - id: flag-003-c3
      type: flag
      what: >
        ID gaps within Window 3 carried from prior cycles: 348/349, 418/419, 442/443
        (prior deletions); 353, 447, 462, 493 (cycle-1 fault-004 resolution); 515 is
        present in bones but absent from tensometer body window (it appears only as
        boundary-carry entry 0c and does not recur in the 330–494 range, which is correct).
      why: >
        No fault. Deletions are legal; gaps must remain visible per schema. Carrying for
        editor awareness. Phase 7 split must not attempt to fill or recover gaps.
      criteria: ~
```
