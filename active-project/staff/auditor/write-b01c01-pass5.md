```yaml
audit:
  scope: chapter
  target: b01c01
  gate: /and-write Phase 5 continuity
  timestamp: 2026-05-18
  findings:

    - id: fault-001
      type: fault
      what: >
        coll-net-mender-flea-bottom state file (active-project/actors/coll-net-mender-flea-bottom/state.md)
        records location as "fish-gate-district-outdoor-work-spot". Bones b01c01s01n03, b01c01s01n04,
        b01c01s01n08 place Coll on-stage at the corner-room off the Hook (Flea Bottom), which the
        chapter chunk and scene chunk both anchor to Hook district. Fish Gate is one of KL's seven
        named gates and is a distinct district from Flea Bottom / Hook. The two locations do not
        overlap under the KL geography constraint (cond-kl-geography-122ac).
      why: >
        A downstream studio fork reading Coll's state file to author location-state or sensory facets
        will load fish-gate-district-outdoor-work-spot as his scene location and produce a facet in
        contradiction with the bones. The /and-stitch lens-anchor pass will have no consistent location
        anchor for Coll. If the state file is not corrected before /and-facets, the location-state
        facet will contain a geography fault that propagates to the draft.
      criteria: >
        Coll's state file location must resolve to a location consistent with the Hook / Flea Bottom
        anchor established by the chapter chunk and scene chunk. Either the state file is updated to
        a Hook-district location, or the chapter/scene chunk is revised to place the work-corner at
        Fish Gate — whichever is the intended canonical location. The two records must name the same
        district.

    - id: flag-001
      type: flag
      what: >
        s01 bone slugs in dispatch order: n01, n02, n03, n04, n09, n05, n07, n06, n08.
        Slug n09 appears fifth in sequence between n04 and n05; slugs n06 and n07 are reversed
        relative to their numeric handles. These are authoring-handle slugs, not flat_ids, so
        non-sequential ordering is not a schema violation. However, the non-monotonic slug order
        suggests n09 was inserted after initial numbering and n06/n07 were sequenced by authoring
        logic rather than slug-order.
      why: >
        At Phase 7 serialization, /and-write assigns flat_ids by walking scenes in the declared order.
        If the ordered bone list above is the canonical scene order, Phase 7 will assign flat_ids
        correctly regardless of slug numbering. No downstream fault if Phase 7 serializes in this
        declared order. Noted for Phase 7 emit confirmation: the serializer must use the declared
        physical order (n01→n02→n03→n04→n09→n05→n07→n06→n08), not slug-numeric order.

    - id: flag-002
      type: flag
      what: >
        No time-skip blank-numbered bone exists between b01c01s02n08 (taylor drops the nets,
        end of the working day) and b01c01s03n01 (wren enters the street). The s03 chunk
        states Wren appears "on the third or fourth day." Without a blank-numbered line at the
        scene boundary, Phase 7 serialization will render the s02→s03 transition as continuous
        same-day action.
      why: >
        The stitcher reads blank-numbered lines as non-trivial elapsed-interval markers and renders
        a paragraph break. Without this marker, the draft will compress a multi-day gap into an
        immediate transition, contradicting the chapter chunk's explicit "third or fourth day"
        placement of Wren's appearance. This is not a bone-content fault but a Phase 7 emit
        requirement.
      criteria: ~

    - id: flag-003
      type: flag
      what: >
        handoff_out specifies "insect-sense reads at passive: density, temperature, movement patterns
        below deployment threshold." Density is delivered by b01c01s01n06 (insects cover the
        flagstones) and b01c01s02n02 (insects fill the block). Temperature is delivered by
        b01c01s02n03 (the walls cool). Movement patterns: b01c01s02n05 (the city-watch passes the
        hook) is street-level environmental observation; no bone explicitly marks movement-pattern
        reading via passive insect-sense. The third handoff_out element is implicit rather than
        bone-delivered.
      why: >
        The handoff_out's "movement patterns" claim is partially unsubstantiated at bone level.
        This does not block /and-facets — the chapter chunk explicitly narrates movement-pattern
        reading as part of the working day — but the sensory facet author will have no bone to cite
        for insect-sense movement-reading. The sensory facet may either invent an uncited assertion
        or leave the movement-pattern element undelivered.
      criteria: ~

  verdict: FAULTS-1
  verdict_note: >
    One fault (fault-001: Coll location state mismatch). Two informational flags requiring Phase 7
    emit action (flag-001: slug order confirmation; flag-002: time-skip marker between s02 and s03)
    and one advisory flag for facet authoring (flag-003: movement-pattern delivery gap).
    All five fault-class axes checked: FAULT-POV clean, FAULT-REFERENCE clean,
    FAULT-REACHABILITY clean, FAULT-HANDOFF-IN-MISMATCH clean (source_chapter null; seed state
    honored), FAULT-STATE one finding (fault-001).
```
