```yaml
audit:
  scope: season
  target: s02-pass-2-constraint
  timestamp: 2026-05-10
  findings:

    # ── SVO MECHANIC COMPLIANCE ───────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: "bones 303, 436 — `the road bends the tributary direction` / `the road bends the east mill approach`"
      why: >
        Both use `bends` as a transitive verb with a direction or named approach as object. A road
        bending a direction is not an observable physical act; it is a spatial-description assertion
        (the shape of the road). This is FAULT-FORM-INTERIORITY — the object is an abstract directional
        concept, not a physical entity acted upon. The `bends` verb here is closer to a copula in
        function ("the road curves toward X") than a genuine action verb. Neither direction-noun
        (`the tributary direction`) nor named approach (`the east mill approach`) is a physical object
        the road can act upon.
      criteria: >
        Each bone must describe a physical event observable by a witness. If the intent is to mark
        Taylor crossing a bend, the bone must show a physical actor taking an action at that point
        (e.g., `the road curves` as location-state, or Taylor crossing the bend as her movement bone).
        The abstract directional-object must be replaced with a physical entity or the bone deleted.

    - id: fault-002
      type: fault
      what: "bone 306 — `the wool factor's cot rises the tributary bank`"
      why: >
        `rises` is used as a transitive verb with `the tributary bank` as its object. A cot/building
        does not perform an action on a bank; it occupies a position. This is FAULT-FORM-NON-ACTION-VERB
        — `rises` here is stative position-naming ("sits elevated on the bank") disguised as action.
        A building rising a bank is not an observable physical event; it is a location description.
      criteria: >
        The bone must be replaced with an observable physical event, or this positional information
        must be removed from the proto-lines entirely and delegated to a location-state facet. If
        the intent is to show Taylor first sighting the cot, recast as Taylor's movement to or
        approach of the cot, which is already partially covered by bone 307.

    - id: fault-003
      type: fault
      what: "bones 181, 192, 239, 244 — `the oc-garrison-captain` (with article)"
      why: >
        The slug `oc-garrison-captain` is used throughout the aggregate (correctly) but bones 181,
        192, 239, and 244 prefix it with the article `the`: `the oc-garrison-captain descends the
        dock approach`, `the oc-garrison-captain exits the dock`, `the oc-garrison-captain descends
        the dock approach`, `the oc-garrison-captain reaches the dock edge`. The schema requires
        SUBJECT to be a named entity — either an actor slug (used bare) or `the <noun>` for unnamed
        environment elements. Prefixing a slug with `the` is malformed: `the oc-garrison-captain`
        is neither a bare slug nor a `the <noun>` unnamed entity. Later bones use the slug correctly
        bare (bones 767, 768, 770, 773, 774, 777, 778). The inconsistency creates an ambiguous
        subject identity in the early bones.
      criteria: >
        Bones 181, 192, 239, and 244 must use the bare slug `oc-garrison-captain` as subject,
        consistent with every other appearance of this actor in the aggregate (bones 767 onward).
        The article `the` must be removed.

    - id: fault-004
      type: fault
      what: "bones 613–615 — `the flies return the common` / `the flies return the dock` / `the flies return the blue-fork road`"
      why: >
        The author flagged these for review. Verdict: FAULT. `return` used transitively as "withdraw
        back to [location]" is idiomatic but does not satisfy SVO discipline here. The object (`the
        common`, `the dock`, `the blue-fork road`) is a location — and per the SVO brief, prepositional
        phrases of destination are banned, including when they are smuggled in as direct objects.
        `return the common` reads as "return to the common" collapsed into a pseudo-transitive — the
        location is a destination, not a thing the flies act upon. A fly cannot return a common in
        the way it can enter, cover, or leave one. The verb-object combination is a prepositional-
        destination construction in disguise (FAULT-FORM-MODIFIER).
        The same verdict applies to the parallel constructions at bones 756–757
        (`the flies return the road` / `the flies return the dock`) and bones 924–925
        (`the flies return the extended grid` / `the flies return the dock`).
        All six instances share the same defect.
      criteria: >
        All six bones (613, 614, 615, 756, 757, 924, 925 — note 925 is `the flies return the dock`,
        same pattern) must be recast with a verb that takes the location as a true direct object
        (e.g., `the flies retreat the dock`, `the flies leave the common`) or with an intransitive
        verb that does not require a location object (`the flies contract`). The destination meaning
        must not be encoded as a pseudo-direct-object.

    - id: flag-001
      type: flag
      what: "bones 669–671 — `the garrison outpost's near fence empties the flies` / `the flies retreat the garrison outpost's near fence` / `the garrison outpost returns the flies at the perimeter`"
      why: >
        Three related constructions at the garrison-perimeter sequence.
        Bone 669: `empties the flies` — the garrison fence as subject performing `empties` on a swarm
        is borderline. The intent (insects driven off by insect-hostile environment) is physical and
        legible; `empties` as an action verb in the object-as-subject form is defensible under the
        schema's allowance for environmental action. Passable but weak.
        Bone 671: `the garrison outpost returns the flies at the perimeter` — `at the perimeter` is
        a prepositional phrase appended to a complete SVO, which is FAULT-FORM-MODIFIER. However,
        this is the same `return` construction flagged in fault-004. If fault-004 is remediated,
        bone 671 should be addressed in the same pass. Flagged here for coordination rather than
        duplicated as a separate fault.
        Bone 746: parallel construction `the garrison outpost perimeter empties the flies` appears
        again in the B4 repeat sequence — same borderline status.
      criteria: null

    - id: fault-005
      type: fault
      what: "bone 671 — `the garrison outpost returns the flies at the perimeter`"
      why: >
        `at the perimeter` is a prepositional phrase appended after the complete SVO, a textbook
        FAULT-FORM-MODIFIER. Even if `returns` were an acceptable verb here, the appended
        prepositional phrase violates the no-modifier rule. A clean SVO terminates at the object.
      criteria: >
        The prepositional tail `at the perimeter` must be removed. If the spatial information is
        load-bearing, it belongs in a location-state facet citing this bone, not in the proto-line.
        The bone should read cleanly as `the garrison outpost returns the flies` (if that verb is
        acceptable post-fault-004 remediation) or be recast to avoid both the return-construction
        and the prepositional tail.

    - id: flag-002
      type: flag
      what: "bones 533–534, 598–606, 637–642, 737–754, 876–887, 914–916 — extended swarm-grid sequences (`the flies trace / fan / extend / cover / push` multi-line runs)"
      why: >
        These are structurally sound SVO constructions individually. The flag is for editor: these
        sequences of 4–8 adjacent swarm-mapping bones may represent proto-line over-generation in
        the same physical moment (the flies covering the same road-grid at different points in the
        same sustained hold). Pass 4 trim is the correct pass to evaluate whether adjacent parallel
        bones covering the same grid in the same moment collapse to fewer lines. Not a SVO-mechanic
        fault, not a constraint violation — advisory for trim pass.
      criteria: null

    - id: fault-006
      type: fault
      what: "bone 895 — `the town reeve raises the summons folio`"
      why: >
        `raises` here describes a sustained-position gesture (holding something aloft, displaying it)
        rather than a discrete physical act with onset and terminus. In context the reeve is
        approaching and brandishing the document. `raises` as stative-position-naming is
        FAULT-FORM-NON-ACTION-VERB if it means "holds it raised" rather than "lifts it from a
        lowered position." The surrounding bones (893 reeve approaches, 896 reeve speaks to fishwife)
        suggest this is a display gesture, not the discrete act of lifting. If it IS the discrete
        act of lifting from rest, it passes. The ambiguity is the issue: the bone is contextually
        readable as stative.
      criteria: >
        The bone must unambiguously describe a discrete physical act. If the intent is the moment
        of raising (lifting from side or belt to outstretched position), `lifts the summons folio`
        is cleaner. If the intent is the display gesture as a continuous state, the bone is
        FAULT-FORM-NON-ACTION-VERB and must be recast as the action that initiates the display
        (`draws the summons folio` is already used at bone 855; a variant that does not repeat
        is needed, or the bone is deleted as redundant with 851).

    # ── CONDITION CARD COMPLIANCE ─────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: "cond-suppression-policy-progression — S2 stage ceiling"
      why: >
        The aggregate correctly holds suppression at patterned-response through the full season.
        Pryor operates via quarterly reports, a dock sentry (B1), named gatherings on the record
        (B2), a garrison-acknowledgment protocol (B4), and a summons to the reeve (B5). None of
        these cross into Stage 3 (formal policy: lord briefed, official directive with lord's seal,
        movement restriction on Taylor). The B5 summons goes to the reeve, not to Mira or Taylor
        directly, and does not carry the lord's seal — consistent with patterned-response ceiling.
        The aggregate's H-section note ("S2 close must not overstate") is honored in the bones.

    - id: pass-002
      type: pass
      what: "cond-feudal-hierarchy-law + cond-westerosi-customary-authority-jaehaerys — smallfolk agency ceiling"
      why: >
        No bone grants Taylor or any smallfolk character formal legal recourse against institutional
        action. Taylor's intervention at B5 (bones 899–912) is physical interposition and speech,
        not legal appeal. The town reeve retains institutional authority throughout; he is
        discouraged but not legally constrained by Taylor. No scene implies smallfolk can invoke
        rights against the lord's apparatus. The institutional response remains documentary and
        procedural, consistent with the Jaehaerys long-peace framing.

    - id: pass-003
      type: pass
      what: "cond-no-parahuman-infrastructure — vocabulary and concept prohibition"
      why: >
        No parahuman vocabulary, no Earth-Bet proper nouns, no Brockton Bay / cape / shard proper
        nouns appear in the aggregate. Taylor's ability is rendered entirely through the physical
        behavior of insects, mosquitoes, beetles, and flies without any parahuman naming. No second
        parahuman entity appears.

    - id: pass-004
      type: pass
      what: "cond-westerosi-superstition-frame — uncanny phenomena frame"
      why: >
        Taylor's swarm use is rendered purely as physical insect behavior (the flies cluster, the
        dock mosquito circles, the beetles trace). No Westerosi character in the proto-lines
        attributes these events to a mechanistic or non-supernatural explanation at the bone level.
        No proto-line introduces a character directly naming Taylor's ability in modern terms.
        The frame is preserved.

    - id: pass-005
      type: pass
      what: "cond-series-tone-constraints-84ac — catharsis prohibition"
      why: >
        The B6 dissolution (bones 942–1040) does not resolve in Taylor's favor or provide catharsis.
        Mira's dissolution is rendered as her arithmetic decision (bones 963–968, 1012–1020). The
        season closes on Taylor passively logging the newcomer's arrival (bones 1050–1091) from the
        road-edge, unable to source the figure's purpose. No bone implies Taylor's work resolved
        something durably. The structural cost-without-resolution requirement is met.

    - id: pass-006
      type: pass
      what: "cond-shard-behavioral-weight — shard as structural pressure, not narrated cognition"
      why: >
        The Shard's behavioral weight surfaces correctly as action choices (Taylor faces the dock
        when she should leave; Taylor approaches the town reeve at B5 peak; Taylor extends the
        grid past the comfort point). No bone narrates the Shard as an external voice, as a
        named force Taylor perceives, or as a cognition Taylor identifies. The weight operates
        through physical commitment bones (approaches, holds, presses) without interior labeling.

    - id: pass-007
      type: pass
      what: "cond-fauna-control-rules — child-body ceiling through B2; adolescent ceiling from B3 forward"
      why: >
        The aggregate's cost-ceiling differentiation is structurally present. B1–B2 bones use
        passive-sense constructions exclusively (the dock mosquito circles, a fly lands, the flies
        cluster) — no active-control sustained hold beyond the passive-sense zero-cost register.
        B3 (bones ~507–591) introduces the extended-grid active hold with `presses the temple`
        and `releases the feet` cost markers at the new ceiling level. B4 (bones ~634–728) shows
        the garrison-road extended hold (flies push the outpost perimeter, flies hold the perimeter's
        near arc) at the new ceiling — differentiated from B1–B2's shorter holds by the reach
        achieved (garrison road, tributary bend, east mill approach simultaneously). B5 (bones
        ~874–937) shows the confrontation-level hold during the reeve intervention — longest
        sustained active window in the aggregate, consistent with the new ceiling.
        No bone in B1–B2 shows active control that would require the adolescent ceiling; no bone
        post-B3 implies Taylor is still operating under the child-body short fuse.

    # ── SLUG + REFERENCE RESOLUTION ─────────────────────────────────────────

    - id: flag-003
      type: flag
      what: "oc-garrison-captain — no card confirmed in active-project/warehouse"
      why: >
        The season plan (G section) designates `oc-garrison-captain` as a walk-on requiring
        margit provisioning. The slug is used extensively (bones 181, 184, 192, 193, 239, 244,
        246, 248, 252, 253, 767, 768, 770, 773, 774, 777, 778). No card at
        `active-project/warehouse/oc-garrison-captain.card.md` was confirmed present. The plan
        notes this explicitly. This is a pre-existing known gap, not an aggregate authoring error.
      criteria: null

    - id: flag-004
      type: flag
      what: "oc-tributary-village-newcomer — no card confirmed; rendered as `the figure` (bones 1055–1082)"
      why: >
        The season plan (G section) designates `oc-tributary-village-newcomer` as a walk-on,
        purpose deliberately unnamed. The aggregate renders this character as `the figure` rather
        than using the slug. This is a legitimate `the <noun>` unnamed-entity form per the schema.
        The flag is advisory: if margit provisions a walk-on card for this character, the slug
        should be inserted at the per-episode split. No fault at aggregate level — the `the figure`
        form is schema-compliant for an unnamed entity.
      criteria: null

    - id: flag-005
      type: flag
      what: "loc-blue-fork-river-road — used as location slug anchor in bones (284, 288, 337, 338, 436, 453, 603, 636, 902, etc.) but rendered as description string `the blue-fork road` not slug"
      why: >
        The location slug `loc-blue-fork-river-road` is a new S2 addition per the series plan.
        The aggregate references the road consistently as `the blue-fork road` (a `the <noun>`
        form) rather than the slug. This is consistent with how S1 bones handled named locations
        (e.g., `the market square` not `loc-market-square`). The schema allows `the <noun>` for
        environment elements. However, the split-time header computation for the `locations:` field
        per per-episode files relies on slug-grep; `the blue-fork road` will not match
        `loc-blue-fork-river-road` in an automated grep. Advisory for Phase 4 split operator.
      criteria: null

    - id: pass-008
      type: pass
      what: "core cast slug resolution — taylor-hebert-jaehaerys, oc-craftsman-mother, oc-craftsman-father, mira-stonefield-jaehaerys, oc-lords-steward, septon-rowan, oc-child-peer, rymer-hedge"
      why: >
        All eight series-roster slugs appear correctly and consistently throughout the aggregate.
        No variant spellings or malformed slug forms detected. All cast-matrix beats (B1–B6) are
        covered by each slug's appearances: Taylor present in all beats; Mira present in B2, B5,
        B6; Rymer present in B2 and B4; Elara (oc-craftsman-mother) present in B1, B2, B3;
        Edwyn (oc-craftsman-father) present in B1, B2, B3; Pryor (oc-lords-steward) present in
        B1, B4; Septon Rowan present in B5, B6; Clem (oc-child-peer) present in B2 and B3.
        All slug forms are consistent.

    # ── CROSS-STRETCH CONSTRAINT COHERENCE ───────────────────────────────────

    - id: pass-009
      type: pass
      what: "B3 adolescent-ceiling transition as perimeter for B4–B6 active-control application"
      why: >
        B3 (approx. bones 507–591) establishes the new cost ceiling through the extended-grid
        hold sequence (flies trace, fan, cover the wider arc with `releases the feet` at bone 530
        and `presses the temple` cost markers). B4 (approx. bones 634–728) correctly shows the
        garrison-road hold at the new ceiling level — reaching the garrison outpost perimeter from
        Fairstead, a distance not achievable under the child-body ceiling. B5 (approx. bones
        874–937) shows the confrontation-level hold during the reeve intervention at the new
        ceiling, with the extended road-grid cover sustained during Taylor's physical approach to
        the reeve. No bone in B4–B6 shows Taylor operating at the shorter pre-transition fuse.
        The ceiling established at B3 is consistently honored through the remainder of the season.

    - id: pass-010
      type: pass
      what: "B1 dock sentry as persistent institutional fact in B2–B5"
      why: >
        The dock sentry (oc-garrison-captain) is established as a new physical presence at the
        ferry dock in B1 (bones 181–194, 239–253). B2 continues to show the garrison captain
        at the dock (bones 239–253 precede the B2 tributary expansion). B4 shows Rymer carrying
        the acknowledgment packet to the garrison waypost, consistent with the garrison's
        institutional role established in B1. B5 shows the flies extending the garrison road
        approach during Taylor's confrontation hold (bones 914–916), confirming the garrison
        remains an active institutional presence. The B1 establishment is honored.

    - id: pass-011
      type: pass
      what: "Mira's gathering as named institutional target — B2 establishment respected in B5–B6"
      why: >
        B2 establishes Mira's gatherings as a named record on Pryor's quarterly report
        (bones 358–416: gathering scenes with Pryor's rider delivering the folio packet to the
        reeve). B5 shows the town reeve acting against the gatherings via the sealed summons
        (bones 851–861), consistent with the monitoring record having reached sufficiency threshold.
        B6 shows Mira dissolving the gatherings in response to institutional pressure from the
        folio record (bones 957–968), not as a unilateral decision — the town reeve arrives with
        the folio (bone 957). The chain from B2 naming to B5 directive to B6 dissolution is coherent.

    - id: pass-012
      type: pass
      what: "Rymer anomaly logged-but-unsourced — B4 establishment not resolved in B5–B6"
      why: >
        B4 (bones 644–728) logs Rymer's behavioral delta (altered road stop, different interlocutors
        at the road edge, bones 700–708) through Taylor's passive-sense without sourcing it. B5
        bones reference Rymer only in the cast matrix (not present in B5 bones directly). B6
        bones do not include Rymer at all. The anomaly is correctly left logged-but-unresolved per
        the H-section mandate. No bone in B5–B6 attempts to explain or dismiss Rymer's shift.

    - id: flag-006
      type: flag
      what: "B6 dissolution — Mira arithmetic / withholding-shape requirement (H-section execution constraint)"
      why: >
        The season plan H-section (dramatist execution constraint, iteration 2) requires that B6
        render Mira's arithmetic as her recognition of the specific shape of Taylor's withholding,
        not only as institutional pressure response. At proto-line level, the bones show: Mira
        dissolving publicly (bones 963–968), Mira interacting with the town reeve twice (bones
        953–975, 1002–1015), Mira consulting the folio record (bones 994–1000, 1019–1020), Mira
        interacting with Septon Rowan and receiving the chapter-house letter (bones 982–990,
        1027–1034). The bones correctly show Mira's agency in the dissolution. However, the
        withholding-recognition dimension — whether Mira's arithmetic explicitly surfaces what
        Taylor held back and when — is dialogue-layer content, not proto-line content (proto-lines
        carry only `speaks to` bones). The constraint cannot be audited at bone level; it must be
        audited at the dialogue-facet level in the downstream pass. This flag is advisory for the
        facet authoring gate: the B6 Mira dialogue bones (947, 950, 955, 960, 963, 967, 972, 974,
        984, 987, 1004, 1008, 1012, 1027, 1028, 1033) must collectively carry the withholding-
        recognition content. If the dialogue facet does not land this, the H-section constraint
        fails at facet-authoring — not at proto-line level.
      criteria: null

    - id: pass-013
      type: pass
      what: "cond-faith-of-seven-jaehaerys — no organized Faith violence; Faith authority is moral only"
      why: >
        Septon Rowan appears in B5 (bones 813–831) receiving the chapter-house letter and in B6
        (bones 982–990, 1025–1035) receiving the newcomer. No bone implies Rowan deploys organized
        Faith enforcement, armed Faith investigation, or institutional coercion. His role is
        pastoral and documentary. The chapter-house letter and literacy-extension register
        (bones 815, 820) are consistent with Faith-as-social-pressure, not Faith-as-enforcement.

    - id: pass-014
      type: pass
      what: "B6 POV switch — Taylor exterior register for newcomer-logging (season-plan POV ruling)"
      why: >
        The B6 interlude section (bones 941–1040) correctly operates under the
        `# pov: mira-stonefield-jaehaerys` marker. The Taylor-exterior register at season close
        (bones 1043–1091, marked `# pov: taylor-hebert-jaehaerys`) correctly handles the
        newcomer's arrival from Taylor's passive-sense position at the road-edge — what the insects
        return from the local-sept approach, not what Mira sees from the market square. The POV
        switch is compliant with the season-plan ruling.

    # ── HEADER COMPLIANCE ────────────────────────────────────────────────────

    - id: fault-007
      type: fault
      what: "aggregate-level header — missing `narrator:` and `goal:` fields"
      why: >
        Per `schemas/proto-line.schema.md`, every proto-line file begins with `narrator:` and
        `goal:` as mandatory fields. The s02.aggregate.md file begins with comment lines and a
        `# pov:` inline marker but does not carry a file-level `narrator:` or `goal:` header.
        The schema states both fields are mandatory under shoot-v2. The aggregate is a Phase 2/3
        working artifact, and the schema's file-path-conventions section describes the aggregate
        as beginning with `narrator:` and `goal:` headers per the standard. The omission faults
        as FAULT-HEADER-NARRATOR and FAULT-HEADER-GOAL.
      criteria: >
        The file must be given a `narrator:` field identifying the primary POV actor (the season-
        plan designates `taylor-hebert-jaehaerys` as the primary narrator with `mira-stonefield-jaehaerys`
        as the B6 interlude — the file-level narrator field should name the primary; the inline
        `# pov:` markers handle POV transitions). The file must also carry a `goal:` field stating
        the season-level goal. These must appear at the top of the file before the body, followed
        by a blank line per schema convention.

verdict: FAIL
fault_count: 7
flag_count: 6
pass_count: 14
escalate_count: 0

notes: >
  Seven faults identified. Six are line-level recasts routable to fixer. Fault-007 (missing
  header fields) is a file-level metadata fix. No findings require escalation to season-plan
  revision. The aggregate's constraint compliance is otherwise strong: suppression-stage ceiling,
  feudal-hierarchy law, no-parahuman prohibition, superstition frame, tone constraint, shard
  behavioral weight, and fauna-control cost-ceiling differentiation all pass. The `return`
  construction (fault-004) affects six bones across three stretch-clusters (613–615, 756–757,
  924–925) and should be remediated in a single fixer pass covering all six simultaneously.
```
