```yaml
audit:
  scope: series
  target: taylor-hebert-jaehaerys — series-level activation audit
  timestamp: 2026-05-09
  findings:

    # ── FAULTS ────────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        series-plan.md Section 6, project-decision sentence (adolescent-body
        ceiling transition) reads: "the 10/20/30-minute actor-card ceilings
        shift upward on a schedule season planning must specify."

        The numbers 10/20/30 are the adult base-curve breakpoints, not the
        child-body breakpoints. The authoritative child-body cost curve
        (warehouse cond-fauna-control-rules, Physical Cost Curve — Child-Body
        Edition) defines the S1 breakpoints as: headache onset at 3–10 minutes,
        nosebleed onset at 10–20 minutes, blackout risk beyond 20 minutes.

        The 1d-audit (fault-001) identified this divergence in the actor card
        and the fixer resolved it at the card level. However, the series-plan
        text was not in scope for the 1d fix, and the series-plan's own
        project-decision sentence still carries the adult-adjacent numbers.
        The fixer-log does not record any edit to series-plan.md.
      why: >
        Season-plan authoring for S2 reads the series-plan adolescent-body
        ceiling note as the authoritative transition statement. A screen-writer
        reading "the 10/20/30-minute ceilings shift upward at ~91 AC" will
        carry wrong S1 baseline numbers into the S2 cost-curve specification,
        producing a ceiling that starts from the wrong floor. The
        cond-fauna-control-rules Growth section maps S1 (age 9–11) at
        3/10/20 min and age 11–14 (S1–S2 bridge) as extending toward 15
        minutes. If the S2 season plan treats the S1 ceiling as 10/20/30 and
        then adds proportional lengthening, the resulting S2 ceiling is
        materially higher than the constraint allows.
      criteria: >
        The series-plan.md adolescent-body ceiling project-decision sentence
        must state the correct child-body S1 breakpoints (3/10/20 minutes,
        per the warehouse cond-fauna-control-rules) as the floor from which
        the transition at ~age 13–14 / ~91 AC lifts. The numbers 10/20/30
        must be removed from or corrected in that sentence.

    - id: fault-002
      type: fault
      what: >
        series-plan.md Section 6 Laws lists the slug
        `cond-westerosi-customary-authority` as a named project-constraint
        condition with the description: "authority derives from house, faith,
        or crown grant; organizing without institutional sponsorship is legible
        as sedition at sufficiently high threat-read."

        The card that exists at that slug
        (cards/conditions/cond-westerosi-customary-authority.card.md) carries:
          scope: project
          project: taylor-hebert-westeros
        Its body text is titled for 120 AC and contains multiple references
        to 120 AC–specific apparatus: the impressment census, Harrenhal,
        "Lannister-Hightower Accommodation," and cross-house deputization.
        None of these exist in the 84–101 AC project.

        The correct card for this project is
        cond-westerosi-customary-authority-jaehaerys, which is also listed in
        Section 6 and exists as a full project-scoped card in the warehouse.
        Listing both slugs implies both are active; only the Jaehaerys variant
        is correct for this project.
      why: >
        Any agent loading series-plan.md as context and following the
        `cond-westerosi-customary-authority` slug will reach the 120 AC card,
        which contains scene-planning content (impressment census, Harrenhal
        detention path, cross-house deputization) that is wrong-era for 84 AC
        and could produce constraint violations in episode planning if
        internalized as applicable law. The series plan appearing to endorse
        this card as a constraint for the 84 AC project is a plan-card
        consistency fault.
      criteria: >
        The slug `cond-westerosi-customary-authority` must be removed from
        series-plan.md Section 6 Laws. The Jaehaerys-era variant
        (cond-westerosi-customary-authority-jaehaerys) is already listed in
        Section 6 and correctly describes the applicable behavioral physics;
        it is the sole correct entry for this slot. No new card is needed.

    - id: fault-003
      type: fault
      what: >
        memory.md seasons entry for s01 is missing three fields required by
        schemas/showrunner-memory.schema.md:

        (1) `chunk` — the schema requires a one-to-two sentence chunk
        statement at the season level ("what this season delivers to the
        series"). The memory.md seasons entry for s01 contains: slug, title,
        window, status, plan, episodes — no chunk.

        (2) Episode-level `chunk` — the schema requires a one-sentence chunk
        on each episode entry ("what this episode delivers to the season").
        All eight episode entries (s01e01–s01e08) contain: slug, title, status
        (and interlude/narrator where applicable) — no chunk on any episode.

        (3) `next_season_sketch` — the schema requires exactly one sentence at
        the season level for the horizon. No next_season_sketch field is
        present.

        The schema example shows:
          seasons:
            - slug: s01
              status: active
              chunk: <one-to-two sentence chunk statement>
              episodes:
                - slug: s01e01
                  status: planned
                  chunk: <one sentence>
              next_season_sketch: <one sentence only>
      why: >
        Showrunner memory is the fast-path context reconstruction tool for
        every session open. The chunk fields are the indexed summaries that
        allow showrunner to reconstruct season and episode commitments without
        reading the full plan files. Absent chunk fields, showrunner must
        read the full plan files to answer "what does S1 deliver?" and "what
        does s01e01 deliver?" at every session open — which defeats the purpose
        of the memory file. The next_season_sketch absence means the S1→S2
        horizon is not indexed in the fast-path lookup; showrunner has no
        one-line signal for where S2 planning is pointed.
      criteria: >
        memory.md must be updated to add: (a) a chunk field at the s01 season
        level, one to two sentences summarizing what S1 delivers to the series
        arc; (b) a chunk field on each of the eight episode entries, one
        sentence each summarizing what the episode delivers to the season; (c)
        a next_season_sketch field at the s01 level, exactly one sentence for
        the S2 horizon. Content must be drawn from series-plan.md S1 chunk and
        season-s01-plan.md episode chunks — no new planning decisions are
        required.

    - id: fault-004
      type: fault
      what: >
        memory.md cast_roster format deviates from the schema.

        Schema (schemas/showrunner-memory.schema.md) specifies:
          cast_roster:
            - <actor-slug>: <one-line role description>

        memory.md cast_roster uses:
          cast_roster:
            - taylor-hebert-jaehaerys     # lead — Taylor reborn ...
            - oc-craftsman-mother          # Elara Ashford — ...

        The format used is a bare list item (slug + inline comment) rather
        than a mapping entry (slug: description). In YAML, an inline comment
        is not a field value — it is stripped by any YAML parser. An agent
        reading memory.md programmatically as YAML would receive a list of
        bare slugs with no role descriptions, which is not the indexed fast-
        path lookup the schema intends.
      why: >
        The cast_roster's one-line role descriptions are the fast-path
        lookup that lets showrunner identify which actor carries which
        function without loading all eight actor cards. If the descriptions
        are comment-syntax (stripped by parsers), the roster is a slug list
        with no annotation — slower to use and not compliant with the schema's
        stated format. The same deviation applies to the stage_elements list,
        which uses the same comment syntax.
      criteria: >
        memory.md cast_roster and stage_elements entries must be reformatted
        to use YAML mapping syntax: `- slug: one-line description` for each
        entry. The role description content already present in the comments
        is the correct content and only needs to be moved to the mapping value
        position.

    # ── FLAGS ─────────────────────────────────────────────────────────────────

    - id: flag-005
      type: flag
      what: >
        memory.md categorizes conditions differently from series-plan.md
        Section 6.

        series-plan.md Section 6 organizes conditions into: Laws, Lore,
        Power mechanics, Suppression arc, Series tone.

        memory.md organizes the same conditions into: laws, lore, behaviors.

        Specific divergences:
        - cond-smallfolk-political-physics is listed under "Lore" in
          series-plan.md but under "behaviors" in memory.md.
        - cond-fauna-control-rules, cond-shard-behavioral-weight, and
          condition-swarm-in-foreign-ecology appear under "Power mechanics"
          and are not explicitly a "behaviors" category in series-plan.md,
          but memory.md groups all three under "behaviors."
        - cond-suppression-policy-progression appears under "Suppression arc"
          in series-plan.md but under "laws" in memory.md.
        - cond-series-tone-constraints-84ac appears under "Series tone" in
          series-plan.md but under "laws" in memory.md.
      why: >
        The schema allows laws/lore/behaviors as the three memory fields, and
        the memory file's categories are not required to mirror the series
        plan's organizational sections. However, the specific placement of
        cond-smallfolk-political-physics (a behavior-of-a-social-class card)
        under "behaviors" in memory and "Lore" in the plan is the most
        semantically inconsistent. This is advisory for editor and future
        planning agents; the functional constraint content is intact and the
        deviation does not create a fictional violation.

    - id: flag-006
      type: flag
      what: >
        memory.md seasons entry for s01 uses a `title` field and a `window`
        field. The schema does not define either of these fields in the seasons
        block. The schema's seasons entry fields are: slug, status, chunk,
        episodes (list), next_season_sketch. The extra fields (title, window,
        plan) carry useful information but are schema-extraneous.
      why: >
        Non-blocking. The extra fields do not break the memory file's function.
        The schema note is advisory: future memory writes should not rely on
        these extraneous fields being present or indexed; agents should use the
        chunk field (once added per fault-003) for season summary retrieval.
        The plan pointer field is arguably useful for routing and could be
        proposed as a schema addition, but that is outside auditor scope.

    - id: flag-007
      type: flag
      what: >
        The s01e01 episode chunk in season-s01-plan.md does not name a
        concrete development that is different at episode-close from episode-
        open, beyond the condition "performing childhood costs something real
        and that cost is already running." The "what cannot remain unchanged"
        statement is a condition-change (cost is running) rather than a social
        or physical fact. The pulp-enthusiast STM named this at both season-
        plan review sessions and it was explicitly carried forward to episode-
        plan authoring without being resolved at season-plan level.

        The season-s01-plan.md Section I explicitly notes: "e01 named change
        (carry-forward): Episode-plan authoring must identify one named thing
        that is concretely different at episode-close from episode-open. Not
        a mood shift — a social or physical fact."
      why: >
        This is a committed carry-forward, not an undetected gap; the season
        plan owns it and routes it to episode-plan authoring. Flagged here for
        audit-trail completeness — the episode-plan for s01e01 must resolve
        this before shoot begins. If episode-plan authoring does not name the
        concrete development, the shoot phase will have no commitment to enforce.

    - id: flag-008
      type: flag
      what: >
        The oc-maester-traveler slug appears in season-s01-plan.md Section F
        (cast matrix for s01e08) and Section H. Section H explicitly notes
        that he "does not join the series cast roster" and that "Margit
        provisions as a walk-on prop-actor if needed." No actor directory
        exists at active-project/actors/oc-maester-traveler/ and none is
        expected per the season plan.

        However, the septon-rowan card contains an ERA ADJUSTMENT NOTE (Margit
        log 2026-05-09) that adjusts the "Dance nine years out" horizon to
        "Great Council 101 AC approximately 15–17 years out." This adjustment
        is in the provisioned copy only (active-project/actors/septon-rowan/)
        and not reflected in any formal update to the library card. This means
        the library card for septon-rowan carries an incorrect horizon that
        would produce a wrong-era read if loaded without the provisioned copy.
      why: >
        The oc-maester-traveler absence is fully acceptable per the season
        plan's explicit ruling. The septon-rowan era-adjustment note is in
        the provisioned copy, which is what will be loaded during shoot, so
        there is no shoot-phase risk. The flag is advisory: if the library
        card is loaded independently (e.g., during a future project that
        re-uses septon-rowan), it will carry the Dance-horizon error until
        migrated. Margit should formally update the library card on next touch.

    # ── PASS ITEMS ────────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Series-plan S1 chunk vs. season-s01-plan deliverables — five committed
        cross-checks.
      why: >
        (1) Ignition at ~86 AC: confirmed at s01e05 "The Steward's Note
        [IGNITION, ~86 AC]." The involuntary swarm rise, horse bolt, note made
        by Pryor — all committed. Pass.
        (2) Mira recruitment seed: s01e06 initiates the earn — debt real and
        unnamed, not closed in S1. Consistent with series-plan "recruitment
        seed." Pass.
        (3) Sept established as literacy node: s01e02 "The Septon's Offer"
        delivers this — literacy instruction accepted, sept now Taylor's node,
        Rowan holds first pastoral claim. Pass.
        (4) Elara intimate-cost begins paying: s01e07 "Elara's Question" names
        Elara's irreversible action (Elara → Edwyn; family unit re-coheres)
        and Taylor's present-tense decision (lie explicitly or accept closing
        of operational cover). The intimate cost lands in S1, not deferred.
        Series-plan commitment met. Pass.
        (5) Maester arrival closes the season: s01e08 "Ledger Work" delivers
        the traveling maester, Pryor-originated directive, board-change
        confirmed as tier-crossing. Pass.

    - id: pass-002
      type: pass
      what: >
        Cost migration sequence — S1 = intimate cost, S2 = coalition cost.
      why: >
        Series-plan Section 4 states: "intimate-cost begins paying before S1
        ends" and "cost migrates outward." Season-s01-plan delivers intimate
        cost in S1 via e07 (Elara's irreversible action, Taylor's present-
        tense decision at close). The series-plan S2 chunk names coalition
        cost beginning (Mira's market-day gatherings dissolution under
        monitoring record). The season-s01-plan Section I explicitly states
        "Suppression-policy stage at S1 close: incident-response" and
        "Patterned-response begins in S2." The cost migration sequence is
        internally consistent across series-plan and season-s01-plan.

    - id: pass-003
      type: pass
      what: >
        Suppression-policy progression at S1 close — incident-response only,
        no premature escalation.
      why: >
        season-s01-plan.md Section I: "Suppression-policy stage at S1 close:
        incident-response. Pryor's note exists; it has reached one maester;
        the apparatus knows the name. Patterned-response begins in S2. The S1
        close must not overstate the institutional threat-level — it is a
        tier-crossing, not a policy shift." s01e08 chunk confirms: the board
        has changed (note crossed a tier, apparatus now networked-surveillance),
        but no Stage 2 patterned-response language appears in S1. The episode
        chunks for s01e01 through s01e08 do not cross into Stage 2 at any
        point. Pass.

    - id: pass-004
      type: pass
      what: >
        Cast referenced in season-s01-plan matrix = cast in cast_roster — all
        8 actors plus the walk-on ruling.
      why: >
        Season-s01-plan.md cast matrix references: taylor-hebert-jaehaerys,
        oc-craftsman-father, oc-craftsman-mother, septon-rowan, oc-lords-
        steward, rymer-hedge, oc-child-peer, mira-stonefield-jaehaerys,
        oc-maester-traveler (s01e08 only). All eight series-roster actors
        are confirmed at active-project/actors/<slug>/card.md. The
        oc-maester-traveler is explicitly ruled out of the cast roster by
        Section H ("walk-on functional role; does not join the series cast
        roster"). This is not an omission fault; it is a deliberate season-
        plan decision with a named rationale. Pass.

    - id: pass-005
      type: pass
      what: >
        All locations referenced in season-s01-plan episode and stage matrices
        exist in warehouse.
      why: >
        season-s01-plan.md Section G references seven locations:
        loc-craftsman-workshop-home, westerosi-smallfolk-dwelling-interior,
        westerosi-smallfolk-village-common, loc-local-sept, loc-market-square,
        loc-river-ferry-dock, loc-river-market-town. All seven confirmed at
        active-project/warehouse/<slug>.card.md. Section H explicitly confirms
        no new location cards are required for S1 and that the wool-factor
        stall and alley (s01e06) are sub-locations of loc-market-square, not
        new cards. Pass.

    - id: pass-006
      type: pass
      what: >
        All condition slugs listed in series-plan.md Section 6 (excluding the
        wrong-era slug identified in fault-002) exist as cards in warehouse
        or library.
      why: >
        Slugs confirmed present: cond-feudal-hierarchy-law,
        cond-westerosi-customary-authority-jaehaerys, cond-riverlands-84ac-state,
        cond-faith-of-seven-jaehaerys, cond-maester-network-behavior,
        cond-smallfolk-political-physics, cond-westerosi-superstition-frame,
        cond-no-parahuman-infrastructure, cond-reincarnation-mechanics-84ac,
        cond-fauna-control-rules, cond-shard-behavioral-weight,
        condition-swarm-in-foreign-ecology, cond-suppression-policy-progression,
        cond-series-tone-constraints-84ac. All 14 cards are present. The
        wrong-era slug (cond-westerosi-customary-authority) exists as a card
        but carries 120 AC content — addressed in fault-002 as a plan-card
        consistency fault. Pass on all correct slugs.

    - id: pass-007
      type: pass
      what: >
        Audience STM completeness — all three persona STMs cover required
        planning sessions.
      why: >
        Required sessions per dispatch: 1b attempt 1+2, series-plan attempt
        1+2, season-s01-plan attempt 1+2.

        worm-canon-pedant/stm.md: 6 sessions present — 1b attempt 1 (revise),
        1b attempt 2 (accept), series plan attempt 1 (revise), series plan
        attempt 2 (accept), season-s01-plan attempt 1 (accept), season-s01-
        plan attempt 2 (accept). Complete.

        dark-fantasy-reader/stm.md: 6 sessions present — 1b attempt 1
        (revise), 1b attempt 2 (accept), series plan attempt 1 (accept),
        series plan attempt 2 (accept), season-s01-plan attempt 1 (accept),
        season-s01-plan attempt 2 (accept). Complete.

        pulp-enthusiast/stm.md: 6 sessions present — 1b attempt 1 (accept),
        1b attempt 2 (accept), series plan attempt 1 (revise), series plan
        attempt 2 (accept), season-s01-plan attempt 1 (accept), season-s01-
        plan attempt 2 (accept). Complete.

        No STM is a stub. All three are fully populated through the end of
        season-s01-plan planning. Pass.

    - id: pass-008
      type: pass
      what: >
        memory.active state — season and episode fields.
      why: >
        memory.md active block:
          season: s01
          episode: s01e01
        These match the expected state at series activation: S1 is active,
        s01e01 is the first episode. The season status field in the seasons
        block correctly reads "active" for s01. Pass.

    - id: pass-009
      type: pass
      what: >
        Audit-trail completeness — all required log and audit files present.
      why: >
        Files confirmed present:
        - active-project/staff/showrunner/1b-log.md: present, records two
          attempts, decisions, carry-forwards.
        - active-project/staff/showrunner/1c-log.md: present, records cast
          selection, stage elements, vibes population, memory updates.
        - active-project/staff/auditor/1d-audit.md: present, full classified
          report (5 faults, 3 flags, 8 passes) in schema format.
        - active-project/staff/showrunner/series-plan-log.md: present, two
          attempts, final verdict accept, carry-forwards.
        - active-project/staff/showrunner/season-s01-plan-log.md: present,
          two attempts, final verdict accept, carry-forwards.
        - active-project/staff/fixer/fixer-log.md: present, records 1d-audit
          fault resolution (5 entries, all criteria-met).
        All required log files are present and non-stub. Pass.

    - id: pass-010
      type: pass
      what: >
        Plan quality — internal consistency of series-plan.md and
        season-s01-plan.md; no contradictory commitments.
      why: >
        Series-plan season chunks reviewed for internal contradiction:
        S1 intimate-cost / S2 coalition-cost / S3 policy / S4 costs-final
        is a consistent one-directional escalation. The S1 chunk names Elara
        as the intimate-cost target; S2 names Mira's network as the coalition-
        cost target; S3 names Faith-fracture and Septon Rowan's network as the
        mid-arc failure; S4 names the enforcement record and Mira's prior
        network. No season chunk commits to the same resource (person, network,
        institution) as the cost target in more than one season — costs migrate
        correctly outward without recycling. The series-plan's cost-migration
        rule (cond-series-tone-constraints-84ac) is satisfied at the planning
        level. season-s01-plan.md eight episode chunks reviewed: no episode
        chunk contradicts another; the arc from e01 (arrival/concealment) to
        e05 (ignition/visibility) to e08 (tier-crossing) is a coherent
        trajectory. No contradictory commitments found.

    - id: pass-011
      type: pass
      what: >
        All eight actor cards confirmed quality: full and schema-compliant.
      why: >
        All eight actors at active-project/actors/<slug>/card.md confirmed
        with: class: persona, scope: project, origin: authored, quality: full.
        All persona-purpose fields set to [on-stage-character]. Tier fields
        present where applicable (taylor-hebert-jaehaerys: lead; supporting
        tier confirmed on oc-craftsman-mother, oc-craftsman-father,
        oc-lords-steward, septon-rowan, mira-stonefield-jaehaerys, rymer-hedge,
        oc-child-peer). No card uses a class outside the five defined. Pass.

    - id: pass-012
      type: pass
      what: >
        Constraint cross-check: Faith Militant prohibition, Shard/parahuman
        separation, ignition mechanics, foreknowledge limits — across plans,
        cards, and memory.
      why: >
        Faith Militant prohibition: present and consistent in
        cond-faith-of-seven-jaehaerys, cond-westerosi-customary-authority-
        jaehaerys, cond-riverlands-84ac-state, cond-feudal-hierarchy-law,
        and series-plan Section 6. No scene or plan beat implies armed Faith
        enforcement. Pass.

        Shard/parahuman separation: cond-no-parahuman-infrastructure and
        cond-shard-behavioral-weight are internally consistent (warehouse copies
        both correctly scoped, Shard carve-out present, no-return-channel
        stated). No plan or card introduces a second parahuman or Shard-
        mediated event beyond the behavioral weight. Pass.

        Ignition mechanics: world-notes, 1b-options.md, series-plan, season-
        s01-plan all agree on I-A — tax-collector retinue, involuntary swarm,
        ~86 AC, age ~9, lord's steward makes note. No drift. Pass.

        Foreknowledge limits: series-plan and season-s01-plan carry-forwards
        consistently note the hard limit at individual Council-actor level and
        the "broad strokes accurate, specifics fuzzy" framing. No plan beat
        in S1 invokes specific named Council actors or claims precise date
        prediction. Pass.
```
