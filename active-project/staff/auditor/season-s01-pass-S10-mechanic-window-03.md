```yaml
audit:
  scope: season
  target: s01 — Window 3, IDs 330–494 (beats 18–26)
  timestamp: 2026-05-11
  pass: S10 Sweep B — Mechanic verdict (narrow scope: AP-SCAN / CURVE-SHAPE / FREQUENCY-BAND)
  source: active-project/theater/proto-lines/s01.bones.md
  combined_verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND

  findings:

    - id: fault-001
      type: fault
      what: >
        ID 355 — "the headache wakes taylor-hebert-flea-bottom";
        ID 449 — "the headache wakes taylor-hebert-flea-bottom" (repeat beat in a later scene group).
      why: >
        AP-SCAN. An internal somatic state ("the headache") is the grammatical subject performing
        a physical action ("wakes"). A headache is not an actor or physical entity that can execute
        a discrete observable action. The proto-line schema bans interiority at the proto-line level
        (FAULT-FORM-INTERIORITY): internal states are facets that cite proto-lines, not subjects of
        proto-lines. Both instances use identical wording and carry the same fault. Downstream
        consequence: when facets are authored against these beats, the tensometer and sensory-flag
        authors have no clean physical event to cite — only an interior state doing the acting.
        Stitcher cannot render a beat whose subject is non-physical.
      criteria: >
        Each beat must record the observable physical event that corresponds to the somatic onset —
        the subject must be a physical actor or named physical entity. Internal state onset belongs
        in a feeling-flag or sensory-flag facet citing a physical proto-line.

    - id: fault-002
      type: fault
      what: >
        ID 339 — "the flies relay the junction return";
        ID 387 — "the wasps relay the dock-side return";
        ID 388 — "the wasps relay the labor-web path";
        ID 416 — "the beetles relay the onset";
        ID 417 — "the beetles relay the cessation";
        ID 471 — "the flies relay the junction departure".
      why: >
        AP-SCAN. Each of these proto-lines takes an abstract event noun as the direct object of
        "relay": "junction return," "dock-side return," "labor-web path," "onset," "cessation,"
        "junction departure." These are not physical objects or named entities — they are
        descriptions of states, intervals, or events. The proto-line schema prohibits
        abstraction-as-object (FAULT-FORM-INTERIORITY). Physical relay beats must name what the
        insects physically carry or observe — a person, a sound, a physical object, a spatial
        location — not an abstract summary of what happened. The six instances form a pattern
        concentrated in this window. Downstream consequence: facet authors have no physical anchor
        to cite; the sensory and narrator facets that are supposed to build on these relay beats
        will have to invent content not present in the bone.
      criteria: >
        Each relay beat must name a physical thing being relayed — an actor, a sound (e.g.,
        "the footfall"), a physical object, or a named location — not a summary noun for an event
        or interval.

    - id: fault-003
      type: fault
      what: >
        ID 469 — "the middleman takes the sealed account".
      why: >
        AP-SCAN. "Sealed" is an adjective modifying "account." The proto-line schema explicitly
        prohibits modifiers, including adjectives (FAULT-FORM-MODIFIER). No adjectives in
        proto-lines; the physical state of the document (sealed vs. unsealed) is either a separate
        prior beat (which ID 468 partially covers as "oc-tanner-elder seals the account") or a
        state-update facet. The object in the proto-line must be the bare noun slug: "the account."
        Downstream consequence: modifier-carrying proto-lines contaminate facet-authoring training
        data and introduce prose-description at the bone layer, which is reserved for SVO only.
      criteria: >
        The proto-line must use "the account" as the direct object, with no adjective. The
        document's sealed state is already registered in ID 468 and belongs to a state-update
        facet citing that beat.

    - id: fault-004
      type: fault
      what: >
        ID 353 — "taylor-hebert-flea-bottom writes the entry" (exact duplicate of ID 352);
        ID 447 — "taylor-hebert-flea-bottom writes the entry" (exact duplicate of ID 446);
        ID 462 — "the flies relay the messenger" (exact duplicate of ID 461);
        ID 493 — "taylor-hebert-flea-bottom writes the entry" (exact duplicate of ID 492).
      why: >
        AP-SCAN / structural duplication. Each pair is an exact repetition of subject, verb, and
        object with no intervening beat and no distinguishing content. The proto-line schema
        requires that each proto-line records a discrete observable physical event. Two identical
        consecutive proto-lines cannot both be discrete events — one is redundant. The duplicate
        "writes the entry" pattern appears three times in Window 3 (352/353, 446/447, 492/493);
        the duplicate "relay the messenger" appears once (461/462). Downstream consequence: the
        tensometer must assign scalars to both; the stitcher will render the beat twice in prose,
        producing repeated sentences or requiring editor intervention. This is a bone-layer defect
        that cannot be corrected downstream without touching the proto-line file.
      criteria: >
        Each pair must resolve to a single proto-line, or the second instance must be recast as a
        genuinely distinct physical beat with a different verb or object that distinguishes it from
        the first. If only one write-entry event occurred, only one proto-line should record it.

    - id: fault-005
      type: fault
      what: >
        Window 3 scene-level curve shape across all scene groups (IDs 330–494).
      why: >
        CURVE-SHAPE. The rubric requires that every scene contain at least one 3-level beat
        (rupture / commit / registration) or carry an explicit dramatist "scene-as-respite" /
        "scene-as-transit" exception flag. Examining each scene group in Window 3:

        Scene group 330–342 (clerk at junction + log): procedural registration scene. No beat
        reads as a commit, rupture, or public-exposure peak. The clerk writes, exits. No 3-level
        candidate. No exception flag.

        Scene group 344–359 (network spread + perimeter + headache): flat run of deployment and
        ambient beats. The only elevated candidate is the headache beat (355), which is also
        AP-SCAN faulted (fault-001). No clean 3-level beat. No exception flag.

        Scene group 361–375 (second clerk + apothecary + log): parallel structure to 330–342.
        Same assessment — procedural, no rupture or commit beat. No exception flag.

        Scene group 383–398 (dock-side inquiry + coin exchange + log): the coin exchange
        (393–395: extends the palm / places the coin / closes the fist) is the window's strongest
        3-level physical candidate. However, the lead-in beats (384–391: insect deployment,
        cluster thins, flies retract) are all 1-level ambient, with no 2-level charge ramp before
        the exchange. The rubric requires beats leading into a 3 to ramp through 2s; a direct
        1→3 jump is flagged as either misrating or true sudden-turn requiring explicit marking.

        Scene group 400–422 (broken-maester circuit + log): beats 416–417 ("relay the onset" /
        "relay the cessation") are also AP-SCAN faulted (fault-002). Even if corrected, the
        surrounding beats are 1-level ambient. No clean 3-level beat before the log close.

        Scene group 438–453 (overnight spread + perimeter + headache): structural repeat of
        344–359. Same assessment. The "faces the Red Keep" (507) appears at the end of this group
        and is a 2-level orientation beat at best — strong, but not a rupture or commit.

        Scene group 455–475 (messenger + elder seals + middleman): the sealed-account handoff
        (467–469) has 3-level commit potential (elder seals, middleman takes — irreversible
        transfer). But ID 469 carries the adjective fault (fault-003). Even if corrected,
        the scene has no 2-level ramp into the handoff — the beats from 465 to 467 are clean
        transit (exits, enters, writes).

        Scene group 477–494 (full circuit walk + log): pure transit and double-write close. No
        charge beats. Structurally a 1-level flatline across the entire group. No exception flag.

        Downstream consequence: when tensometer is authored against these bones, the dramatist
        will face either (a) scalar inflation — rating ambient beats at 2/3 to manufacture shape,
        which breaks the cross-facet contract — or (b) multiple scene-level kickback flags that
        send authoring back to screen-writer. The rubric says the dramatist's response to a
        failing curve is a screen-writer kickback, not scalar inflation. This audit identifies
        the kickback targets pre-authoring so they can be addressed at the bone layer before
        tensometer authoring begins.
      criteria: >
        Each scene group without an exception flag must contain at least one proto-line that
        functions as a rupture, commit, or registration beat readable from the SVO sentence alone.
        Scene groups that are structurally transit or respite must carry an explicit exception
        marker (scene-as-respite / scene-as-transit). The 1→3 adjacency problem in scene group
        383–398 must be resolved either by inserting a 2-level charge beat between the ambient
        run and the coin exchange, or by the dramatist explicitly flagging it as a true
        sudden-turn at tensometer-authoring time.

    - id: fault-006
      type: fault
      what: >
        Window 3 overall beat composition: estimated ~120 proto-line beats across IDs 330–494
        (including out-of-sequence inserts 497, 498, 499, 503, 507).
      why: >
        FREQUENCY-BAND. The expected rung distribution across a corpus of proto-lines is
        60–75% 1s, 20–30% 2s, 5–10% 3s (from the tensometer rubric). Assessing Window 3's
        bones against the axes that drive rung assignment:

        Confirmed 1-level beats (ambient, transitional, log open/write/close, insect deployment,
        perimeter walks, enter/exit navigation): approximately 108–112 beats.

        Plausible 2-level beats (charged stillness, public exposure, turn-proximity): the coin
        exchange approach (393), the elder confrontation (377–381), the messenger scene (455–463),
        the elder seals the account (468), faces the Red Keep (507) — approximately 8–10 beats.

        Plausible 3-level beats (rupture, commit, registration peak): coin closes the fist (395),
        middleman takes the account (469, after adjective fault is fixed) — approximately 1–2 beats.

        Approximate distribution: ~92% 1s, ~7% 2s, ~1% 3s.

        This is significantly outside the expected band: 1s are ~17–32 percentage points too
        high; 2s are ~13–23 points too low; 3s are ~4–9 points too low. The rubric states that
        a distribution outside band indicates systemic miscalibration and requires investigation
        before shipping. At the bone layer, before tensometer authoring, this means the proto-line
        file does not contain enough materially-charged beats to support an honest tensometer
        within the expected frequency band. Downstream consequence: either the tensometer
        systematically inflates scalars (breaking the cross-facet contract) or it produces an
        honest but severely flattened distribution that signals a structurally underloaded episode
        segment to the stitcher — compressing large portions of the window into single "and"
        connectives.
      criteria: >
        The bone set for Window 3 must contain enough beats that, when rated honestly by axis,
        fall in the 20–30% 2-rung and 5–10% 3-rung bands. Achieving this at current beat count
        (~120) requires approximately 24–36 additional 2-level beats and 6–12 additional 3-level
        beats, or reduction of 1-level beats to bring the denominator down while adding charged
        beats. This is a screen-writer kickback scope: the window needs more charged beats at
        the bone layer before tensometer authoring proceeds.

    - id: flag-001
      type: flag
      what: >
        Out-of-sequence IDs 495 (line 105 in file), 496, 497, 498, 499, 500, 501, 502, 503,
        504, 505, 506, 507, 508 — all appear within or near the Window 3 range in the file's
        physical ordering but carry IDs higher than 494. Some appear interleaved between
        lower-numbered lines (e.g., 497 between IDs 356 and 357; 503 between 417 and 420).
      why: >
        The proto-line schema requires monotonic positive integer IDs, stable once assigned.
        Out-of-sequence IDs are legal (they represent insertions after initial numbering, per
        the schema's "deletions leave ID gap visible" rule). However, several of these
        out-of-sequence IDs appear physically within the Window 3 body and are therefore
        in scope for this audit even though their numeric IDs exceed 494. This audit has
        reviewed those that appear in the file between IDs 330 and 494 (specifically 497, 498,
        499, 503, 507). IDs 495, 496, 500, 501, 502, 504, 505, 506, 508 appear earlier in
        the file (before line 390) and are outside Window 3 scope.

        The interleaving pattern is consistent with the schema's insertion-without-renumber
        rule. No fault on the numbering itself. Flagging for editor awareness: the Phase 7
        split will need to correctly assign these out-of-sequence beats to their episode slots
        based on physical position, not numeric sort order.
      criteria: ~

    - id: flag-002
      type: flag
      what: >
        ID gaps 348, 349 (between 347 and 350); IDs 418, 419 (between 417 and 420);
        IDs 442, 443 (between 441 and 444) — all within Window 3.
      why: >
        Per schema, skipped IDs indicate deleted proto-lines. Three deletion clusters appear
        in Window 3. No fault — deletions are legal and leave gaps intentionally visible.
        Flagging for editor awareness: the stitcher and Phase 7 split must not attempt to
        recover or fill these gaps. If the deleted beats were load-bearing for scene continuity,
        the corresponding scenes (344–359 insect network, 400–422 broken-maester, 438–453
        overnight spread) may have continuity gaps that the editor pass should inspect.
      criteria: ~
```
