```yaml
audit:
  scope: season
  target: s01
  pass: S10-boundary-carry-01-02
  cycle: 2
  timestamp: 2026-05-11
  prior_cycle: season-s01-pass-S10-boundary-01-02-cycle-1.md
  verdict: BOUNDARY-CARRIES
  findings:

    - id: fault-001
      type: pass
      what: >
        ID 511 (inserted between IDs 158 and 159):
        `taylor-hebert-flea-bottom faces the junction`
      why: >
        Cycle 1 fault-001 required: at minimum one bone prior to ID 163 must
        place Taylor at the junction in an established-station posture
        (stationary, insect-relay active, or equivalent physical indicator of
        prior presence), distinct from the crossing motion of IDs 159–160.

        ID 511 registers Taylor in a stationary, junction-oriented posture —
        facing the junction — prior to the family's crossing at IDs 159–160.
        The verb "faces" is a physical-register position bone (orientation,
        not motion). Its placement before the crossing arrivals establishes
        Taylor as already present and directed toward the junction before the
        family enters the scene. This is distinct from the family's crossing
        motion and distinct from Taylor's own approach at ID 163; ID 511 is a
        stasis-register that satisfies the established-station physical-
        register requirement. Fault cleared.
      criteria: ~

    - id: fault-002
      type: pass
      what: >
        ID 512 (inserted between IDs 158 and 159, immediately following 511):
        `oc-tanner-elder faces the road`
      why: >
        Cycle 1 fault-002 required: a bone establishing the elder's stationary
        position at the junction prior to IDs 159–160, physical-register not
        a speech act.

        ID 512 registers oc-tanner-elder in a stationary, road-facing posture
        before the family crosses. "Faces the road" is a physical-register
        orientation bone that places the elder at the junction's road-facing
        margin — the precise position of the routing-membrane role established
        at IDs 145–148. The elder is watching incoming traffic (road-facing)
        from the junction, the same functional position demonstrated in window
        1 close. The bone is not a speech act. Its placement before IDs
        159–160 registers the elder as already stationed at the junction
        before the arrivals appear. Fault cleared.
      criteria: ~

    - id: fault-003
      type: flag
      what: >
        Window 2 open (IDs 511, 512, 159–169): log-carry pattern break
        unchanged by additions. IDs 511/512 add station-register bones (faces
        the junction; faces the road) but do not introduce the log. The log
        remains absent from the full window 2 open through ID 181 (family
        exit), reappearing at ID 183.
      why: >
        The flag from cycle 1 stands. The REGEN-ADD addressed the two faults
        without closing this gap; the log reappears post-family-exit (ID 183)
        so the object is not dropped from the season. The absence across
        IDs 511–181 is consistent with action-beat prioritization and may be
        intentional. Editor advisory: note for continuity review at wrap.
        Non-blocking; no fixer dispatch.
      criteria: ~
```
