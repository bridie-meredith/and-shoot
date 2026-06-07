# Showrunner Memory Schema

Showrunner memory is series-scoped and cross-session. It is the index and fast-lookup layer that lets showrunner reconstruct a full working context at the start of any session, without reading every card or plan file from scratch.

File location: `active-project/staff/showrunner/memory.md`

Updated by: every authoring command (`/and-project`, `/and-series`, `/and-substance`, `/and-cast`, `/and-write`) at the end of its persistence phase. Showrunner itself is read-mostly; the command bodies own write authority over their respective blocks. See per-block "Authored by" tags below.

Optimized for Claude, not for human reading. Keep entries compact — one line per item unless a pointer is needed.

**Schema revision history.** The pre-substance schema (`seasons[].episodes[].*`) is preserved in archive copies of pre-substance command bodies for back-reference. Under the substance overhaul (URI-SUBSTANCE-OVERHAUL, 2026-05-17) the `seasons` block is replaced by `books[]` and the `episodes[]` block is replaced by `chapters[].scenes[].bones[]`; "season"/"episode" vocabulary is dropped from the live schema.

---

## Top-level layout

```yaml
project:    # /and-project
series:     # /and-series + /and-substance series
books:      # /and-substance book/chapter + /and-write
active:     # advances across the chain
```

---

## `project:` block — scope + staff (authored by `/and-project`)

```yaml
project:
  brief: <one-line distill of the user's elevator pitch>
  constraints:
    settings: [...]                      # decided world-frame items (e.g. "currency: gold dragons + silver stags")
    themes_as_bounds: [...]              # binding tonal/thematic commitments
    hard_fences: [...]                   # cross-world non-negotiables (e.g. Earth-Bet proper-noun fence)
  staff:
    audience: [<slug>, <slug>, <slug>]   # exactly three audience-persona slugs from staff/audience/INDEX.md
    screen_writer: <persona-or-default>
    dramatist: <persona-or-default>
    auditor: <persona-or-default>
    editor: <persona-or-default>         # library-only under the polish-deferred chain; bound for future revival
    orchestrator_critic: <card-version>  # e.g. v3; tracks staff/orchestrator-critic/card.md version
  series_audit:                          # /and-cast Phase 5 approval checkpoint
    approved_at: <iso-timestamp> | null
    approved_by: user | null
    report_path: staff/reviews/series-audit-<timestamp>.md | null
    stale_since: <iso-timestamp> | null  # set when /and-series, /and-substance series, or /and-cast re-runs after approval
```

Required at scaffold; `series_audit.*` filled by `/and-cast` Phase 5 on `y` approval. `/and-substance book b01` Phase 0 HARD-aborts if `series_audit.approved_at` is missing or `stale_since` is set.

---

## `series:` block — series chunk + structure + substance + cast (authored by `/and-series`, `/and-substance series`, `/and-cast`)

```yaml
series:
  # from /and-series — structured chunk: path + trajectory IS the chunk; prose is a rendering
  chunk:
    path:
      motivation: <one-line; what gets the protagonist up at start-state>
      anchor: <one-line; the person/thing the motivation attaches to — may be null>
      escalation: <one-line; what converts small protagonist actions into larger ones>
      trade: <one-line; the act that turns "good intention" into "hell" — the road-to-hell hinge>
      irony: <one-line; how the trade returns as the catastrophe>
    trajectory:
      start_state:                            # axis-keyed map; axes are project-specific
        <axis>: <state-at-book-open>
      end_state:                              # may inherit from project.constraints.hard_fences
        <axis>: <state-at-book-close>
      deltas:                                 # ordered; each names what changes and (where useful) what causes it
        - <delta-1>
        - <delta-2>
    lens_used: relational | political | interior | penitential | escape | vocational | structural | accidental | composed
    prose: |                                  # rendered by Phase 2; human-facing only
      <prose paragraph rendering of path + trajectory>
  structure:
    book_count: <N>
    book_length:
      chapters_per_book: <range>           # e.g. 4-8
      scenes_per_chapter: <range>          # e.g. 1-3 (scenes are substantial)
      bones_per_scene: <range>             # e.g. 5-15 (scene-action-sized bones)
    cyclical: true | false
    pov: single | multi | rotating-per-book
    cross_book_continuity:
      recurring_antagonists: [...]
      ongoing_subplots: [...]
    world_evolution: static | evolving
    series_end_shape: definitive | open-ended | ambiguous | tragic | triumphant
  laws: [...]                              # non-standard physics / magic / world rules
  lore: [...]                              # background facts
  behaviors: [...]                         # series-wide character behavior constraints

  # from /and-substance series Phase 4 (signature) — series.substance.*
  substance:
    state_axes:
      - slug: <axis-slug>                  # e.g. wealth, health, community, emotional, capability, knowledge, reputation, agency, trust
        dimension: <one line>
        one_means: <one line>              # anchor: what rank 1 looks like in this story
        five_means: <one line>             # anchor: what rank 5 looks like
        nine_means: <one line>             # anchor: what rank 9 looks like
        perspective: protagonist | antagonist | world
        start_rank: <1-9>
        end_rank: <1-9>
        class: plot | emotional            # optional; used by future emotional-substance orthogonality check (OOS)
        notes: <one line>                  # optional; phase-shape, two-phase axes, consequence-vs-trade anchoring
    actor_baselines:                       # per-actor, per-axis positions — DENSE matrix: every actor × every axis
      # The state_axes block above pins per-perspective aggregate positions (the dramatic shape).
      # actor_baselines pins per-actor positions because the perspective aggregate hides divergent
      # actors (Otto vs Aemond both antagonist; Wren / Sera / Gylda all supporting with different arcs).
      #
      # Authoring discipline: dense matrix. Every cast_roster actor × every state_axes axis gets an
      # entry. The `applicability` field disambiguates absent-because-omitted from absent-because-out-of-scope:
      #
      #   moves           — start_rank ≠ end_rank; this actor's position moves on this axis across the book
      #   static          — start_rank = end_rank; this actor's position is fixed; the cell is examined and pinned
      #   not-applicable  — this actor does not participate in this axis's machinery; rationale REQUIRED in notes
      #
      # This shape prevents judgment-by-omission: an actor with no entry on an axis is a SCHEMA VIOLATION,
      # not a meaningful absence. Use applicability:not-applicable to record the deliberate exclusion.
      - actor: <actor-slug>                # must match a slug in series.cast_roster
        axis: <axis-slug>                  # must match a slug in series.substance.state_axes[]
        applicability: moves | static | not-applicable
        start_rank: <1-9> | null           # REQUIRED for applicability:moves and applicability:static; null only for not-applicable
        end_rank: <1-9> | null             # REQUIRED for applicability:moves and applicability:static; null only for not-applicable
        source: lifted-from-state-axes | inferred-from-role-card | scene-pinned-<chapter-slug>
        notes: <one line>                  # rationale REQUIRED for applicability:not-applicable; recommended for moves/static
    cost_ledger:
      - id: <ledger-entry-id>              # stable handle for `bones[].substance_delta.cost_ledger_anchor`
        gain: <axis-slug> +<delta>
        cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
        anchor:                            # populate from the level where the cost is paid; finer wins
          book: <book-slug>
          chapter: <chapter-slug> | null   # null when cost spans the whole book
          scene: <scene-slug> | null       # null when cost spans the whole chapter
    antagonist_pressure:
      - axis: <axis-slug>
        pressure_source: <one line>
        cost_curve: <one line>             # how the pressure escalates across the series
    chunk_targets:
      series:  { delta_per_signature_axis: <range>, density_target: <range> }
      book:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      chapter: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      scene:   { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      bone:    { delta_per_axis: <range>, axes_per_bone: <range> }   # typical 1-axis ±1 rank; occasionally 2-axis; conditional: 1-3 when scene_target_delta_magnitude >= 1.0; magnitude = scene_target_delta_magnitude when scene_target_delta_magnitude < 1.0 (fractional sub-scene moves permitted at sub-1.0 scene targets; Phase 6 gate accepts magnitude == scene_target_delta_magnitude in these cases). Precedent: DEC-0002 (c07 + c08 sub-1.0 bone deltas accepted).
  vibe_cloud:                              # series-level vibe-cloud, authored by /and-series
    keys: [...]

  # from /and-cast
  cast_roster:
    - slug: <actor-slug>
      role: <one-line role description>
      perspective: protagonist | antagonist | supporting | world
  stage_elements:
    - <location | prop | condition slug>: <one-line purpose in series>
```

---

## `books[]` block — recursive chunk hierarchy (authored by `/and-substance`, finalized by `/and-write`)

Each book is one entry. Each book contains chapters; each chapter contains scenes; each scene contains bones. Bones are scene-children with their own per-bone state-delta — the source of truth lives here, not in the bones file.

```yaml
books:
  - slug: b01                              # auto-generated by /and-substance series Phase 6
    chunk: |
      <book-level chunk authored by /and-substance series>
    structure:                             # /and-substance series Phase 2
      chapter_count: <N>                   # picked inside series.structure.book_length.chapters_per_book
    substance_delta:                       # /and-substance series Phase 3
      axes_in_motion:                      # axes that ACTUALLY move across this book; held axes go in axes_held
        - axis: <axis-slug>                # must match series.substance.state_axes[].slug
          direction: up | down             # REQUIRED; null/~ is malformed (use axes_held for held-flat axes)
          target_delta_magnitude: <positive number>   # REQUIRED; > 0 (zero is malformed — use axes_held)
          cost_ledger_anchor: <id> | [<id>, ...] | null
          notes: <one line>
      axes_held:                           # axes deliberately held flat at this level — load-bearing dormancy
        - axis: <axis-slug>
          rationale: <one line>            # why held; usually names the discipline / scene_conflict that holds it
      density_target: <range>
    stale_since: <iso-timestamp> | null    # set when /and-substance series re-runs with `redo` after persistence
    vibe_cloud:                            # book-level vibe-cloud, authored by /and-substance series
      keys: [...]
    drama: |                               # /and-substance book Phase 4 — "what cannot survive this book"
      <one-paragraph drama statement>
    chapters:
      - slug: b01c01                       # auto-generated by /and-substance book Phase 6
        chunk: |
          <chapter chunk authored by /and-substance book>
        structure:                         # /and-substance book Phase 2
          scene_count: <N>                 # picked inside series.structure.book_length.scenes_per_chapter
        substance_delta:                   # /and-substance book Phase 3
          axes_in_motion:                  # axes that actually move across this chapter
            - axis: <axis-slug>
              direction: up | down         # REQUIRED; no null
              target_delta_magnitude: <positive number>   # REQUIRED; > 0
              cost_ledger_anchor: <id> | [<id>, ...] | null
              notes: <one line>
          axes_held:                       # axes deliberately held flat at this chapter
            - axis: <axis-slug>
              rationale: <one line>
          density_target: <range>
          chapter_class: standard | frame-coda    # OPTIONAL; defaults to `standard`. `frame-coda` marks an interlude / retrospective chapter outside the protagonist-axis scope (e.g. b01c18 archmaester-retrospective coda). Frame-coda chapters are exempt from /and-write Phase 6 substance bone-gate per its frame-coda exemption clause. Authored by /and-substance chapter Phase 4 alongside dramatic_shape + goal + pov_narrator.
        stale_since: <iso-timestamp> | null
        status: planned                    # state-machine enum; see below
        pov_narrator: <actor-slug>         # /and-substance chapter Phase 3; resolved from series.structure.pov
        dramatic_shape: rising | climax | falling | hinge
        goal: <one-line "what this chapter shows the audience">
        handoff_in:                        # /and-substance book Phase 3; cross-chapter continuity
          open_threads: [...]
          world_state: [...]
          character_state: [...]
          source_chapter: <prior-chapter-slug> | null
        handoff_out:                       # /and-substance book Phase 3
          open_threads: [...]
          world_state: [...]
          character_state: [...]
          target_chapter: <next-chapter-slug> | null
        scenes:
          - slug: b01c01s01                # auto-generated by /and-substance chapter Phase 6
            chunk: |
              <scene chunk authored by /and-substance chapter; substantial.
               URI-CHUNK-TAG-PROTOCOL (2026-05-25): load-bearing spans are tagged inline
               with bracketed markers extractable by /and-write Phase 1:
                 [event: <name>]      — a concrete thing that happens in the scene
                 [image: <name>]      — a load-bearing sensory anchor the prose must carry
                 [force: <name>]      — protagonist_force / opposing_force as it appears in narrative form
                 [mechanism: <name>]  — a causal mechanism the prose must show legibly
               Tags do not alter the chunk's readability; they make "what's load-bearing"
               the chunk-author's call rather than the bone-author's interpretation, and
               make /and-write Phase 6 EVENT-MAP-INCOMPLETE check mechanical.>
            substance_delta:               # /and-substance chapter Phase 3
              axes_in_motion:              # axes that actually move across this scene
                - axis: <axis-slug>
                  direction: up | down     # REQUIRED; no null
                  target_delta_magnitude: <positive number>   # REQUIRED; > 0
                  cost_ledger_anchor: <id> | [<id>, ...] | null
                  notes: <one line>
              axes_held:                   # axes deliberately held flat at this scene; stakes_axis often appears here
                - axis: <axis-slug>
                  rationale: <one line>
              density_target: <range>
            scene_conflict:                # /and-substance chapter Phase 3
              protagonist_force: <one line>
              opposing_force: <one line>
              stakes_axis: <axis-slug>
            stale_since: <iso-timestamp> | null
            event_map:                     # /and-write Phase 1 (event-coverage contract); checked at Phase 6 event-presence gate
              - event: <named event / load-bearing image / the scene_conflict.protagonist_force, one line>
                bones: [<bone-slug>, ...]  # >=1 bone covering this event, OR empty with omission_rationale set
                omission_rationale: <one line> | null   # REQUIRED non-null when bones is empty — a deliberate, justified omission
            bones:                         # /and-write Phase 1 (scene-decomposition); per-bone substance_delta lives here
              - slug: b01c01s01n01         # n-prefix for bones (b would collide with book)
                flat_id: <int>             # assigned at /and-write Phase 7 serialization
                svo: |
                  <one-line SVO bone — scene-action-sized>
                substance_delta:
                  axis_moves:              # axes the bone ACTUALLY moves; empty list = chatter bone (must pay a cost-ledger entry)
                    - axis: <axis-slug>
                      direction: up | down # REQUIRED; null/~ malformed (use axes_held for held-flat axes)
                      magnitude: <positive number>   # REQUIRED; > 0 (zero is malformed — use axes_held or empty axis_moves)
                  axes_held:               # axes deliberately held flat at this bone — stillness-against-pressure, dormancy-enacted
                    - axis: <axis-slug>
                      rationale: <one line>  # why held; usually names the discipline being enacted by the SVO action
                  cost:
                    axis: <axis-slug> | null
                    direction: down        # cost is always negative on its axis (or the axis moves toward its damaging end — see cost_note pattern in cost_ledger entries)
                    magnitude: <positive number>
                  cost_ledger_anchor: <cost-ledger-entry-id> | null
                gate_verdict:              # filled by /and-write Phase 6 ONLY on PASS; cleared at Phase 0 on revise/redo
                  bonefide: true
                  flat: false
                  signals: [<finding-class>, ...]   # SIGNAL findings preserved across runs for SIGNAL-targeted revise
        # chapter-level fields filled by /and-write
        bones_file: theater/bones/b01-c01.md
        bones_count: <N>
        substance_bone_gate_verdict: PASS | FAIL-<reason>
        substance_delta_measured:
          axes_moved: [...]
          density_measured: <ratio>
          felt_verdict: SUBSTANCE-FELT | SUBSTANCE-FLAT-<axis> | SUBSTANCE-SUSPECT-cheap-gain-<axis>
        chunk_cold_read:                   # written by /and-substance chapter Phase 5.5 (PROP-0019 / PROP-0019-A); chunk-level cold-read gate
          reviewed_at: <iso-timestamp>
          verdict: PASS-CHUNK | PASS-CHUNK-VOICE-RISK | CHUNK-CLASS-A | CHUNK-CLASS-B | SHIPPED-WITH-RISK-RECORDED
          classification: A | B | n/a
          recovered_summary: <cold-reader criterion-6 summary>
          intended_goal: <chapters[].goal at review time>
          continue: yes | no               # first-pass Q5
          continue_strict: yes | no         # Q7 re-answer (post no-charity confusion list); AUTHORITATIVE for classification
          report_path: staff/reviews/chunk-coldread-<chapter>-<timestamp>.md
          disposition: R | P | S | n/a      # n/a for PASS-CHUNK and PASS-CHUNK-VOICE-RISK
          dispositioned_at: <iso-timestamp>
          dispositioned_by: admin | principal
          voice_risk:                        # PROP-0019-A; present whenever verdict == PASS-CHUNK-VOICE-RISK
            triggered: <true|false>
            signals: [<A and/or B>]
            central_event: <central event in plain actor-verb-object terms>
            voice_risk_carry: <central event + abstraction-vocabulary; arms /and-stitch Phase 8.5 central-event-muffle>
          cold_read_risk_carry: <if (P): comma-list of principal-authorized known-risk findings>
        bones_review:                      # written by /and-review bones <chapter>; /and-facets Phase 0 HARD-checks presence + freshness
          reviewed_at: <iso-timestamp>
          report_path: staff/reviews/bones-<chapter>-<timestamp>.md
          verdict: PASS | PASS-WITH-NOTES | FAIL
          follow_check: PASS | PASS-WITH-NOTES | FOLLOW-FAIL   # PROP-0020 followability pre-check; FOLLOW-FAIL HARD-aborts /and-facets Phase 0 (distinct from advisory verdict:FAIL)
          bones_file_mtime_at_review: <iso-timestamp>   # bones-file mtime when the review ran; staleness check against current mtime
          stale_since: <iso-timestamp> | null
        context_followability:             # written by /and-facets Phase 2.5/4.5 (PROP-0020 context-weave + PROP-0022 readability twin)
          completeness_verdict: FOLLOWABLE | GLARING-HOLE
          readability_verdict: ALIVE | AIRLESS-HOLE          # PROP-0022 second axis
          report_path: staff/reviews/context-follow-r2-<chapter>-<timestamp>.md
          reviewed_at: <iso-timestamp>
          context_ledger_open: <N>          # open CONTEXT-REQUIRED lines in context-ledger-<chapter>.md
          grounding_ledger_open: <N>        # open GROUNDING-REQUIRED lines in grounding-ledger-<chapter>.md (PROP-0022)
          unresolved: [<gap-id>, ...]       # Phase 4.6 WARN carry (context-debt that survived conditional R3)
        cold_read:                         # written by /and-stitch Phase 9 cold-read terminal gate
          read_at: <iso-timestamp>
          verdict: PASS | PASS-WITH-DEPTH-PASS-REQUIRED | FAIL
          recovered_summary: <one-line cold reader's chapter summary>
          readability_axis:                # PROP-0022 separated scoring; PASS requires READABLE (completeness alone is not enough)
            verdict: READABLE | AIRLESS
            basis: <one line — person-to-follow / breathes, or apparatus-reporting; from cold-read answers + Phase 4 VOICE-APPARATUS-DEFAULT/EMBODIMENT-BLOCKED counts>
          report_path: staff/reviews/coldread-<chapter>-<timestamp>.md
          staging_signals: <N>             # count of EXPAND/GROUND/STAGE/NEEDS-BEAT findings from the additive editorial pass
          staging_report_path: staff/reviews/staging-<chapter>-<timestamp>.md
          signal_clusters:                 # /and-stitch Phase 9 Step 4 URI-STITCH-SIGNAL-CLUSTER (2026-05-24; threshold tightened 2026-05-25)
            - pattern: <pattern-label>     # e.g. body-staging-gap, opposing-force-prose-mute, held-bone-rationale-only, peak-under-staged
              count: <N>
              bone_ids: [<flat-id>, ...]
              trigger: same-pattern>=5 | adjacent-in-peak-zone>=3 | on-axis-move-bones>=3
          prose_rationale_audit:           # /and-stitch Phase 9 Step 3.5 URI-STITCH-PROSE-RATIONALE-MUTE (2026-05-25); PC-02 gate
            ran_at: <iso-timestamp>
            verdict: CLEAN | SIGNALS-RECORDED | SOFT-BLOCK
            mute_findings:                 # bones whose prose-span lacks concrete-physical-tokens for their rationale-named OF/body/register elements
              - bone_id: <flat-id>
                rationale_element: <opposing-force | body-staging | register-enactment>
                rationale_text: <one-line excerpt>
                prose_span: <sentence-ID range>
                finding: PROSE-RATIONALE-MUTE-<bone-id>
            stale_since: <iso-timestamp> | null
          stale_since: <iso-timestamp> | null
        depth_pass_pending:                # /and-write Phase 7 sets true when a revise --from-signals runs on a chapter with cold_read.verdict == PASS-WITH-DEPTH-PASS-REQUIRED
          true | false                     # /and-stitch Phase 9 Step 4 reads this; on PASS verdict, stamps depth_pass_resolved_at and clears this flag
        depth_pass_resolved_at:            # /and-stitch Phase 9 PASS stamps this when depth_pass_pending was true; confirms delivery
          <iso-timestamp> | null           # PC-01 (URI-STITCH-SIGNAL-CLUSTER MANDATORY promotion, 2026-05-25);
                                           # consumed by /and-substance book <next-book> Phase 0 HARD-abort + /and-review verdict <book> precondition
    # book-level field filled by /and-review verdict <book-slug>
    orchestrator_critic_verdict:
      ruling: PASS | PASS-WITH-NOTES | FAIL
      report_path: staff/reviews/verdict-<book-slug>-<timestamp>.md
      verdict_at: <iso-timestamp>
      stale_since: <iso-timestamp> | null
```

---

## `chapters[].status` enum

Monotonic state machine; status only ever moves forward within a fresh authoring pass. Re-running an upstream command in `revise`/`redo` mode resets status to the earliest value that command owns and stale-marks downstream artifacts per the staleness-cascade rules.

| status | set by | meaning |
|---|---|---|
| `planned` | `/and-substance book` Phase 6 | Chapter chunk + per-chapter Δ written; scenes not yet authored. |
| `scened` | `/and-substance chapter` Phase 6 | Scenes + per-scene `substance_delta` + `scene_conflict` + `pov_narrator` + `dramatic_shape` + `goal` + `handoff_in/out` populated; bones not yet authored. |
| `bones-written` | `/and-write` Phase 7 (post-bone-gate PASS) | Bones authored across all scenes; bones file + scene-map facet emitted. |
| `faceted-r1` | `/and-facets` R1 fanin | R1 facet rubrics applied. |
| `audited-r1-mechanical` | `/and-facets` mechanical-audit pass | Citation accrual + body-integrity + slice consolidation passed. |
| `audited-r1` | `/and-facets` audience-gate verdict PASS | URI-DIALOGUE-COVERAGE-GATE + URI-SCENE-WINDOW + audience-gate re-verified. |
| `faceted-r2` | `/and-facets` R2 fanin | R2 facets applied. |
| `stitched` | `/and-stitch` Phase 8 finalize | `draft/<book>-<chapter>.md` (clean) + `draft/<book>-<chapter>.annotated.md` emitted. |

**Partial-revise rule (G1):** any bone change drops `status` back to `bones-written` on Phase 7 emit, regardless of how many scenes were touched. Downstream facet outputs + draft are stale-marked.

---

## `active:` block

```yaml
active:
  book: b01 | null
  chapter: b01c01 | null
  cascade_in_progress: true | false    # written by /and-substance --cascade; cleared on completion
```

---

## Routing — paths to working files

```yaml
routing:
  series_plan: active-project/staff/showrunner/series-plan.md
  staleness_log: active-project/staff/showrunner/staleness-log.md
  cascade_checkpoint: active-project/staff/showrunner/cascade-checkpoint.md
  reviews: active-project/staff/reviews/
  bones_dir: active-project/theater/bones/
  facets_dir: active-project/theater/facets/
  dialogue_dir: active-project/theater/dialogue/
  draft_dir: active-project/draft/
```

---

## Field notes

**project.staff.editor** — bound at `/and-project` for future revival; the polish-deferred chain does not dispatch the editor agent. Recorded so the persona is reserved.

**series.substance.cost_ledger[].anchor** — the cost-ledger anchor refines as the chunker chain descends. `/and-substance series` writes `anchor.book` only; `/and-substance book` may refine `anchor.chapter`; `/and-substance chapter` may refine `anchor.scene`. Refinement is non-destructive — coarser anchors stay populated; finer anchors add on top so `/and-write` Phase 6 bone-gate resolves against the finest-grained populated field.

**chapters[].pov_narrator** — always populated on every chapter so `/and-write` Phase 7 can write the bones-file `narrator:` header without further lookup. Resolution: `series.structure.pov = single` → inherited from series; `rotating-per-book` → inherited from book; `multi` → picked per chapter from cast roster.

**bones[].substance_delta** — the per-bone state-delta lives here, in memory, NEVER in the flattened bones file. The bones file is comment-clean.

**axes_in_motion vs axes_held (at every chunk level + bone level)** — split as of 2026-05-21. Pre-split, `axes_in_motion` carried entries with `direction: null, magnitude: 0` to record dormancy-enacted / stillness-against-pressure axes; the convention is dropped because it makes "this axis moved" indistinguishable from "this axis was deliberately held" at the bookkeeping layer. Under the split:
- **`axes_in_motion[]`** lists axes that actually move. `direction ∈ {up, down}`, `magnitude > 0` (book/chapter/scene: `target_delta_magnitude`; bone: `magnitude`). Null/zero entries are malformed.
- **`axes_held[]`** lists axes deliberately held flat by discipline. Each entry: `{axis, rationale}`. The held axis is load-bearing for the scene's stakes — that is *what makes a held-flat axis different from a chatter bone*. A chatter bone has neither `axis_moves` nor `axes_held` and must pay a cost-ledger entry to justify its existence.
- **`scene_conflict.stakes_axis`** may resolve to either `axes_in_motion[]` (the axis the conflict moves) or `axes_held[]` (the axis the conflict holds) — both are valid stakes. `/and-write` Phase 6 substance bone-gate checks against the union when validating that the stakes axis appears.

**series.substance.actor_baselines[]** — per-actor positional grid, authored as a **dense matrix** (every cast_roster actor × every state_axes axis). `state_axes[].perspective ∈ {protagonist, antagonist, world}` pins per-perspective aggregate positions, but a perspective hides divergent actors (Otto vs Aemond both antagonist; cost-bearer / protect-target / witness-mirror all supporting). The dense-matrix discipline prevents judgment-by-omission: an absent entry is a schema violation, not a meaningful absence.

Each cell carries an `applicability` field:
- **`moves`** — `start_rank ≠ end_rank`; this actor's position arcs on this axis across the book. Both ranks required.
- **`static`** — `start_rank = end_rank`; this actor's position is fixed (examined and deliberately pinned). Both ranks required.
- **`not-applicable`** — this actor does not participate in this axis's machinery (walk-on with no per-axis arc; archetype-flat character; frame-coda voice outside scope). Ranks may be null; `notes:` REQUIRED to record the deliberate exclusion.

`source:` records lineage: `lifted-from-state-axes` (verbatim from perspective-aggregate), `inferred-from-role-card` (built from cast-roster role description), or `scene-pinned-<chapter-slug>` (set when a specific chapter resolved the actor's position on that axis).

**bones[].flat_id** — assigned at `/and-write` Phase 7 serialization. Stable within a run; `revise` mode preserves flat_ids for unchanged bones (gap-filling for new bones).

**bones[].gate_verdict.signals[]** — preserved across runs so `/and-write revise --from-signals` can target SIGNAL-flagged bones for partial-revise. `/and-review bones <chapter>` re-fire auto-clears signals that no longer apply.

**orchestrator_critic_verdict** — written by `/and-review verdict <book>`. `stale_since` is set by any `/and-substance` or `/and-write` re-run at-or-under the book after the verdict was recorded.

**series.chunk** — structured object as of `/and-series` v2. The path + trajectory IS the canonical chunk; `prose` is a human-facing rendering produced by Phase 2 and may lag behind structural revisions. Downstream consumers that need a string read `series.chunk.prose`; consumers that need decision-grade premise data read `series.chunk.path` and `series.chunk.trajectory`. Migration TODO: /and-substance series should be rewritten to read the structured form directly (v1 reads .prose for backward compatibility).

---

## Companion file: `series-plan.md`

The memory file above is the index. The detail lives in `active-project/staff/showrunner/series-plan.md` — a prose document containing:
- Full law descriptions (where the one-line summary is insufficient)
- Full lore entries
- Full behavior constraint explanations
- Book drama descriptions
- Cast biographies (pointers to actor cards)
- Full signature rationale (where the one-line anchor is insufficient)

When showrunner needs detail beyond the one-line summary, it reads the series plan. The memory file is the fast path; the series plan is the authority.
