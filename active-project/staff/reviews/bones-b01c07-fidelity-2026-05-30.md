```yaml
audit:
  scope: chapter
  target: b01c07
  timestamp: 2026-05-30
  review_type: bones-fidelity
  overall_verdict: PASS-WITH-NOTES
  finding_counts:
    hard: 3
    signal: 2
    taste: 0
  fidelity_verdict: PASS-WITH-NOTES
  sources_read:
    - active-project/staff/showrunner/_drafts/b01c07-bones-draft-2026-05-30-rev2.md
    - active-project/staff/showrunner/memory.md (lines 4680-4871)
    - active-project/theater/bones/b01-c07.md
    - active-project/theater/dialogue/septon-halvard-flea-bottom.md
    - active-project/theater/dialogue/taylor-hebert-kl-122ac.md
    - active-project/actors/taylor-hebert-kl-122ac/card.md
    - active-project/actors/septon-halvard-flea-bottom/card.md
    - active-project/actors/taylor-hebert-kl-122ac/state.md
    - active-project/actors/septon-halvard-flea-bottom/state.md
    - schemas/bones.schema.md
    - schemas/dialogue.schema.md
    - schemas/audit-report.schema.md

  findings:

    # ── HARD FINDINGS ──────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      class: HARD
      location: "flat 15 (b01c07s02n07) — MOVING soc-tether +0.5"
      criterion: FAULT-FORM-MODIFIER
      what: >
        Emitted bone: "taylor-hebert-kl-122ac stays in the argument."
        "in the argument" is a prepositional phrase of containment/location.
        The bones schema (§ SVO discipline) explicitly bans "Prepositional phrases
        of place / destination / source / direction / instrument / accompaniment"
        under FAULT-FORM-MODIFIER. This is the s02 MOVING bone carrying
        soc-tether-prot-rise +0.5. The rev2 draft's operation-record for D3/D4
        routes all the rebuttal-restraint NI content to this bone and marks it
        "unchanged PASS bone" (renumbered from old n08), but the SVO form was not
        audited for the modifier ban at prior attempts. The +0.5 axis-move claim
        depends on this bone as its DEC-0052 physical-observable witness; a formally
        invalid bone cannot serve as a clean Δ-witness.
      why: >
        A MOVING bone with a banned PP modifier means the substance_delta Δ-witness
        for soc-tether-prot-rise +0.5 at s02 is staked on a malformed SVO.
        If left unresolved, /and-facets inherits an axis-move with a faulty anchor;
        the stitcher renders a PP-laden line that fails the bones-comment-clean rule.
        The s02 soc-tether Δ is half of the chapter's +1.0 delivery; its witness bone
        must be clean.
      criteria: >
        The bone at flat 15 must be re-expressed as a concrete SVO with no
        prepositional modifier, while retaining "stays" or an equivalent whitelist
        verb with a concrete or at minimum non-PP-modified object that still witnesses
        the physical observable (Taylor remaining present at the sept-corner during/after
        the thesis-landing without yet departing). The revised form must pass the
        FAULT-FORM-MODIFIER check and retain the soc-tether +0.5 Δ-witness claim.

    - id: fault-002
      type: fault
      class: HARD
      location: "flat 22 (b01c07s03n05) — MOVING soc-tether +0.5"
      criterion: FAULT-FORM-MODIFIER
      what: >
        Emitted bone: "taylor-hebert-kl-122ac stays at the sept-corner."
        "at the sept-corner" is a prepositional phrase of place, banned under
        FAULT-FORM-MODIFIER. This is the s03 MOVING bone carrying
        soc-tether-prot-rise +0.5 (D7 recast). The rev2 draft explicitly cites
        "stays at the sept-corner" as the "exact form that passed at attempt 1 for
        a soc-tether moving bone," invoking prior-pass status as license. Prior-pass
        status from a different attempt cycle does not override the schema. The PP
        "at the sept-corner" is identical in structure to the banned PP "in the
        argument" at fault-001.
      why: >
        Same downstream consequence as fault-001: the s03 soc-tether +0.5 Δ-witness
        is a malformed SVO. Chapter's total soc-tether delivery is +1.0; both moving
        bones are faulty. The argument spine's social-embedding completion event —
        the "stays then leaves" enacted as unresolved-close — loses its clean
        physical-observable anchor. /and-facets inherits two PP-bearing moving bones
        instead of the one it was supposed to receive after three attempts.
      criteria: >
        The bone at flat 22 must be re-expressed without the PP "at the sept-corner,"
        retaining the physical observable of Taylor remaining at the location after
        Halvard's cost-acknowledgment speech and immediately before "leaves the
        sept-corner" (flat 23). The revised form must pass FAULT-FORM-MODIFIER and
        retain the soc-tether +0.5 Δ-witness claim. The existing flat 23 "leaves the
        sept-corner" is itself a PP-bearing bone but carries no Δ (held bone only);
        that fault is separately flagged below.

    - id: fault-003
      type: fault
      class: HARD
      location: "flat 16 (b01c07s02n08) — HELD soc-tether post-move"
      criterion: FAULT-FORM-NON-ACTION-VERB (abstraction-as-object via holds)
      what: >
        Emitted bone: "septon-halvard-flea-bottom holds the silence."
        The bones schema narrow holds license reads: "'holds' is licensed only when
        (1) the object is a body part of the subject and the action is
        stillness-against-pressure, or (2) the object is a physical object resisting
        pressure." The example of a failing form given in the schema is "the yard
        holds the silence." The emitted bone is structurally identical. "The silence"
        is an abstract noun; it is neither a body part of Halvard nor a physical object
        resisting pressure. The rev2 draft cites the narrow holds license as justifying
        this form but misreads the license — the license requires the body-part or
        physical-object-resisting-pressure condition; "silence" satisfies neither.
      why: >
        Flat 16 is a HELD post-move bone; the soc-tether Δ at s02 was already
        delivered at flat 15 and is not re-staked on flat 16. However, a FAULT-FORM
        finding on any bone in the emitted file is a HARD gate at /and-review bones,
        regardless of Δ-status. The sensory and engagement function this bone serves
        (the working-silence beat between thesis landing and argument continuing) must
        be retained, but the holds-abstraction form is illegal. If uncorrected, /and-facets
        receives a non-schema-compliant bone and the stitcher renders a line the
        bones schema prohibits.
      criteria: >
        The bone at flat 16 must be re-expressed without "holds the silence" or any
        equivalent holds-abstraction form. The physical observable (Halvard not pressing,
        not speaking, remaining still in the space after Taylor stays in the argument)
        must be captured through a concrete intransitive or transitive SVO that does
        not use holds-abstraction or a banned modifier. The sensory-register function
        of this bone (working-silence beat) should be preserved in the physical act.

    # ── SIGNAL FINDINGS ────────────────────────────────────────────────────────

    - id: fault-004
      type: flag
      class: SIGNAL
      location: "flat 23 (b01c07s03n06) and flat 7 (b01c07s01n07) — HELD bones"
      criterion: FAULT-FORM-MODIFIER (PP of place on held bones)
      what: >
        Flat 23: "taylor-hebert-kl-122ac leaves the sept-corner." — "the sept-corner"
        is the destination object of "leaves." This may read as transitive-with-object
        rather than PP ("leaves" taking a direct object); compare "enters the sept-corner"
        (flat 7) which is clearly transitive. However, the schema licenses "taylor enters
        the yard" explicitly (§ SVO discipline: "Use a transitive verb that takes the
        location as direct object"). "Leaves" taking a location as direct object follows
        the same pattern. This is borderline rather than clear-fault.
        Similarly flat 7 "enters the sept-corner" follows the licensed transitive form.
        Both are held bones with no Δ claim. The SIGNAL is raised because: flat 23 is the
        NI-anchor bone for WATCH-3 (foreclosure-planted-not-enacted) and the NI facet
        must cite it cleanly; and because the fixer addressing fault-001 and fault-002
        should at the same time confirm whether "leaves" in flat 23 is read as
        transitive-with-object (clean) or as PP-of-place (fault). Auditor reads it as
        likely clean but flags for confirmation.
      why: >
        If flat 23 is actually clean (transitive direct-object), no action. If it is
        read as PP-of-place at /and-facets review, it would flag WATCH-3's NI-anchor
        bone as malformed. Flagged here to prevent a downstream second fault cycle
        over a borderline form on a load-bearing NI-anchor bone.
      criteria: null

    - id: fault-005
      type: flag
      class: SIGNAL
      location: "chapter-level — NI facet load (7 NI routes, 0 NI facet yet authored)"
      criterion: FOLLOW-CHECK pre-advisory (PROP-0020 completeness track)
      what: >
        The 5 deleted bones (D3, D4, D5, D6, D8) and 2 recast bones (D2, D7) transfer
        all interior intelligence — rebuttal-restraint, register-sharpening causality,
        named-death ledger-weight, two-accountings image, completion-not-closure,
        foreclosure-interior-voice — to the narrator-interest (NI) facet. The rev2
        draft contains 7 distinct NI route notes (lines 97-127 and 777-784). None of
        these routes are load-bearing on the bones alone; all require the NI facet to
        deliver them.
        The chunk-cold-read verdict was PASS-CHUNK-VOICE-RISK ("seminar-risk"; "low
        present jeopardy"; "the named-death beat MUST land concrete or the chapter reads
        as a seminar"). The bones spine is mechanically intact (argument-thesis covered,
        counter-deployed, unresolved-close enacted). However, the chapter's interior
        argument-weight — WHY the argument grips Taylor (WATCH-2 causality), the
        precision of what the thesis maps onto, the felt cost of the unresolved
        parallel-accounting — is entirely deferred to the NI facet.
        This is design-compliant (bones = physical; interior = facets) but creates a
        compound risk: if the NI facet underdelivers on any of the 7 routes, the seminar-
        risk flips to seminar-fact. The /and-review bones FOLLOW-CHECK will assess this
        at /and-facets Phase 0 (PROP-0020 pre-check). Surfaced here so the NI facet
        author at /and-facets is explicitly loaded with the full 7-route requirement,
        not just the bones-facing handoff notes.
      why: >
        If the NI facet is authored without explicitly honoring all 7 routes at the
        correct anchor bones, the /and-stitch Phase 9 cold-read will likely find:
        Taylor's engagement reads as asserted not caused (WATCH-2 gap), the named-death
        lands as gesture not weight (WATCH-1 thin), and the unresolved-close reads as
        structural notation rather than felt cost (WATCH-4 gap). These are the exact
        failure modes the chunk-cold-read identified as risks. Flagged so the /and-facets
        NI author treats the 7 routes as explicit deliverables, not optional texture.
      criteria: null

    # ── PASS FINDINGS (explicit) ───────────────────────────────────────────────

    - id: pass-001
      type: pass
      location: "Aggregation — chapter-level Δ sums"
      what: >
        political_register-prot: s02 +0.3 (flat 14) + s03 +0.2 (flat 18) = +0.5 EXACT.
        social_tether-prot-rise: s02 +0.5 (flat 15) + s03 +0.5 (flat 22) = +1.0 EXACT.
        Both chapter targets met. (The HARD faults at fault-001 and fault-002 affect
        the form of the Δ-witness bones, not the arithmetic; the arithmetic is correct.)
      why: null

    - id: pass-002
      type: pass
      location: "Moving bone DEC-0052 physical-observable verification — flat 14"
      what: >
        Flat 14 (s02n06): "taylor-hebert-kl-122ac faces septon-halvard-flea-bottom."
        pol-reg +0.3. "faces" is whitelist-licensed physical-observable verb. Single
        subject. Concrete named-entity object (actor slug). No modifier. An observer
        would see the physical orientation. DEC-0052 discriminator: PASSES. The D2 recast
        (replacing "holds halvard's gaze") is confirmed clean.
      why: null

    - id: pass-003
      type: pass
      location: "Moving bone DEC-0052 physical-observable verification — flat 18"
      what: >
        Flat 18 (s03n01): "taylor-hebert-kl-122ac names the body count." pol-reg +0.2.
        "names" is a concrete communicative-act verb. "the body count" as object:
        parallel to "names the sick child" (flat 4, held bone, passed at all attempts);
        both are label-referents for concrete content rather than pure abstractions.
        Accepted by parity with flat 4. Physical observable: the speech-act of naming.
        DEC-0052: PASSES.
      why: null

    - id: pass-004
      type: pass
      location: "Dialogue-anchor bone coverage — flats 12, 19, 21"
      what: >
        All three dialogue-anchor bones carry the required citation tokens:
        flat 12 [septon-halvard-flea-bottom:1] ✓, flat 19 [taylor-hebert-kl-122ac:1] ✓,
        flat 21 [septon-halvard-flea-bottom:2] ✓. No bare dialogue-anchor bones.
        FAULT-DIALOGUE-MISSING-AT-ANCHOR: clear.
      why: null

    - id: pass-005
      type: pass
      location: "Dialogue files — presence, form, anchor alignment"
      what: >
        Both dialogue files present and non-empty. Frontmatter correct (character,
        episode, behavior-card fields populated). Anchor alignment: Halvard:1 @s02n04
        = flat 12 ✓; Taylor:1 @s03n02 = flat 19 ✓; Halvard:2 @s03n04 = flat 21 ✓.
        Schema form (id @anchor | objective | utterance) correct for all 3 entries.
      why: null

    - id: pass-006
      type: pass
      location: "Dialogue card-compliance — Earth-Bet proper-noun fence"
      what: >
        All three utterances checked against the Earth-Bet proper-noun fence (no Worm,
        Khepri, cape, parahuman, shard, trigger vocabulary). Halvard:1, Halvard:2,
        Taylor:1: clean. Taylor:1 names "Wenna Cobb, Pig-Tallow Lane" — Westerosi
        proper nouns, not Earth-Bet leakage. FAULT-DIALOGUE-EARTH-BET-FENCE: clear.
      why: null

    - id: pass-007
      type: pass
      location: "Dialogue card-compliance — behavior-card hard fences"
      what: >
        Halvard:1 (errand-man thesis): principled Flea Bottom register, no theological
        jargon, names wrong without providing strategy, does not know Taylor is
        the referent. Halvard hard fences 1-5: all clear.
        Halvard:2 (cost-acknowledgment): honest, pausal, names uncertainty, does not
        retract or claim Taylor is wrong. Hard fence 4 (does not provide an alternative):
        satisfied — "I've only the one I can live beside" is an acknowledgment of cost,
        not a strategic alternative.
        Taylor:1 (counter): cold-utilitarian register, specific body not category,
        names Wenna Cobb + street + failure-mechanism (eleven-day interval, burial not
        call). No self-justification-to-the-room read — chunk licenses the disclosure
        as non-performative counter-argument required by the argument. Taylor hard
        fences: clear.
      why: null

    - id: pass-008
      type: pass
      location: "Dialogue objective-anchoring — all 3 objectives"
      what: >
        Halvard:1 objective ("name what is wrong with the Lane man's arrangement,
        working it through honestly, not aimed at Taylor") — utterance delivers the
        compound-corruption thesis via the errand-man case without aiming it at Taylor.
        Taylor:1 objective ("deploy the counter by naming the specific cost the slower
        method already exacted") — utterance names Wenna Cobb + Pig-Tallow Lane +
        the eleven-day fever interval + burial-not-call. WATCH-1 concrete delivery ✓.
        Halvard:2 objective ("acknowledge the cost of his own position honestly without
        retracting it or claiming she is wrong") — delivered. All 3 objectives: ✓.
      why: null

    - id: pass-009
      type: pass
      location: "Chunk→bones fidelity — load-bearing event coverage"
      what: >
        S01: All chunk events (circuit, halt-and-contact, Halvard-as-precinct-node,
        sick-child-named, plain-acknowledgment, insect-feed-placing) have direct bone
        coverage. No deletions in s01. Full fidelity.
        S02: Halvard fever-description (flat 9), maester-cost (flat 10), pivot (flat 11),
        thesis-delivery (flat 12 + Halvard:1 dialogue), Taylor-goes-still (flat 13),
        Taylor-stays (flat 15, faulted form but event present), silence-beat (flat 16,
        faulted form but event present), sensory-ground (flat 17). The two deletions
        (D3, D4) transferred interior events (rebuttal-restraint, deferred-counter)
        to NI facet via flat 15's NI route — these are legitimately interior content.
        No load-bearing physical event dropped.
        S03: Body-count-named (flat 18), Taylor-counter-speech (flat 19 + Taylor:1
        dialogue + WATCH-1 delivered), Halvard-absorbs (flat 20), Halvard-acknowledges-
        cost (flat 21 + Halvard:2 dialogue), unresolved-close enacted as stay+leave
        (flats 22+23), sensory-ground (flat 24), chapter-close (flat 25). Three
        deletions (D5, D6, D8) transferred interior images and metaphorical-placing
        to NI facet — all were either SVO-illegal (multi-subject D6, abstraction-as-
        object D8, metaphorical-placing D5) or redundant to dialogue coverage.
        No load-bearing physical event dropped.
        ARGUMENT SPINE: thesis (Halvard:1) ✓, counter (flat 18 + Taylor:1) ✓,
        unresolved-close (flats 22+23) ✓, foreclosure-planted-not-enacted (flat 25 +
        NI route at flat 23) ✓.
      why: null

    - id: pass-010
      type: pass
      location: "State consistency — actor locations and inventory"
      what: >
        Taylor state: location flea-bottom-hook-district; chapter set in sept-corner
        within the Hook — consistent. Halvard state: location flea-bottom-hook-precinct;
        appears at sept-corner (Halvard's established fixed point in the Hook per card) —
        consistent. Neither actor uses inventory items. No prop-inventory violations.
      why: null

    - id: pass-011
      type: pass
      location: "SVO form — all non-flagged bones (1-13, 17, 18, 19, 20, 24, 25)"
      what: >
        All bones not named in fault-001, fault-002, fault-003, or fault-004 pass SVO
        discipline: single subject, concrete verb, no copulas, no negations, no
        perception verbs, no conjunctions, no compound objects, no interiority as action.
        Flat 6 ("the insect-feed places septon-halvard-flea-bottom") — "places" is a
        concrete action, subject is a named-entity prop-equivalent, object is a named
        actor: clean. Flat 13 ("taylor-hebert-kl-122ac goes still") — intransitive
        posture-act, modifier stripped at D1: clean. Flat 20 ("septon-halvard-flea-bottom
        absorbs the counter") — "absorbs" is a concrete action; "the counter" as object
        is borderline (abstract referent) but established by the chunk's own vocabulary
        ("[force: halvard-without-sufficient-answer]") and parity with "names the body
        count" (flat 18). Clean.
      why: null

    - id: pass-012
      type: pass
      location: "Bones header — seven required fields"
      what: >
        All seven header fields present and populated: episode (b01c07), narrator
        (taylor-hebert-kl-122ac), goal (one sentence, sourced from substance contract),
        cast (taylor-hebert-kl-122ac, septon-halvard-flea-bottom), locations
        (oc-sept-corner), prior_episode (b01c06), aggregate_range (1-25). FAULT-HEADER:
        clear on all fields.
      why: null

    - id: pass-013
      type: pass
      location: "Halvard state — direct_encounters lag (advisory only)"
      what: >
        Halvard's state file shows direct_encounters_this_arc: 0, but c07 is the first
        genuine engagement (chapter 7). This lag is in the state file, not in the bones
        file; the bones file itself is consistent with the handoff_out from c06 ("Halvard:
        counter-argument latent but not yet engaged"). The bones audit scope does not
        extend to state-file freshness; noted for showrunner's state-reconciliation pass
        at /and-write chapter-close. No finding on the bones file itself.
      why: null
```
