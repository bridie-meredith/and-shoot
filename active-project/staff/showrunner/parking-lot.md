# Parking Lot — cross-chunk watch items

Schema: `schemas/parking-lot.schema.md`. Append-only; resolution stamps fields rather than deleting. Scanned by Phase 0 of every re-runnable command (CLAUDE.md Rule 14).

```yaml
parking_lot:
  version: 1
  items:
    - id: pl-2026-06-14-001
      created_at: 2026-06-14T22:26:00Z
      created_by: "session 2026-06-14 cont.4 (Book-II II.4 refinement pass — principal margit flag)"
      target:
        command: "/and-cast"
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        The II.4 "maimed lady" (the court figure Gael's apparatus damages / the maiming beat
        in II.4) needs a NAME + a cast card (margit). Currently a role-mark only. Resolve before
        II.4 goes to chapter production so the figure is consistent if she recurs.
      context_refs:
        - active-project/staff/showrunner/memory.md
        - active-project/intake/spine.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-14-002
      created_at: 2026-06-14T22:26:00Z
      created_by: "session 2026-06-14 cont.5 (Book-III III.2 pass — principal call: named on-page spared rival)"
      target:
        command: "/and-cast"
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        The III.2 spared rival — the underworld figure Gael spares on-page (judged not worth the
        effort) who becomes the loose-end that sells her movements to Otto and converges at the
        III.6 dock — needs a NAME + a cast card (margit). This is a NEW RECURRING underworld
        figure (appears III.2, pays off III.6 FIRE[GANG-LOOSE-END]). Apply name-novelty care
        (no library/prior-project slug reuse). Resolve before III.2/III.6 chapter production.
      context_refs:
        - active-project/design/run-04/series-outline.md
        - active-project/intake/spine.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-14-003
      created_at: 2026-06-14T22:26:00Z
      created_by: "session 2026-06-14 cont.5 (Book-III horror-undertow steer)"
      target:
        command: "/and-write"
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        The "black-cells" (the Red Keep's dungeons, where servants are swept and disappear under
        the Book-III horror undertow) need a LOCATION card (margit/studio + warehouse provision)
        before Book-III chapter authoring (III.2/III.3/III.4/III.6 reference them). Render
        person-first/concrete per Rule 22.
      context_refs:
        - active-project/design/run-04/series-outline.md
        - active-project/intake/spine.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-14-004
      created_at: 2026-06-14T22:26:00Z
      created_by: "session 2026-06-14 cont.5 (Book-III horror-undertow steer — token candidate)"
      target:
        command: "/and-substance"
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        PRINCIPAL-TRIAGE: decide whether to formally wire a motif token
        BLACK-CELLS / MISSING-SERVANTS (the realm's-terror collateral — people go missing, thefts,
        servants swept to the cells) as a PLANT/FIRE thread across Book III, vs leave it a
        register-undertow note (current state — NOT wired, to avoid unreviewed check-threads churn).
        If wired, add PLANT at III.2 and FIRE at III.3/III.4/III.6 and re-run check-threads.
      context_refs:
        - active-project/design/run-04/series-outline.md
        - active-project/intake/spine.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null
```
