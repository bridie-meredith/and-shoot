audit:
  scope: season
  target: s01 aggregate (active-project/theater/proto-lines/s01.aggregate.md)
  timestamp: 2026-05-09
  pass: FACET-GAPS
  findings:

    # --- LOCATION-STATE ---

    - id: fault-001
      type: fault
      what: Scene E (beats 127–149) — no actor-enters-location or `the <loc>` frame-anchor beat opens the scene; scene opens directly at beat 127 oc-craftsman-mother speaks with no location established since Scene D's workshop close
      why: Studio fork has no proto-line to cite as frame-anchor for the location-state entry that licenses all subsequent beats in this scene; inherited environment from Scene D is ambiguous (Scene D closes in the workshop/yard; Scene E could be the same workshop or a different room). Every downstream beat in this scene renders in an undefined location.
      criteria: An actor-enters or `the <loc>` beat must exist at or before beat 127 that unambiguously establishes the location for Scene E; the beat must be a discrete physical SVO anchoring the scene's space.

    - id: fault-002
      type: fault
      what: Scene G (beats 220–232) — no location-establishing beat; scene opens with oc-craftsman-mother speaking to Taylor (beat 220) with no prior entry beat; beat 232 oc-craftsman-mother enters the workshop implies they were outside the workshop, but no location is established for the scene's open
      why: Studio fork cannot anchor a location-state entry for Scene G. The scene's physical context (roadside, lane, yard, or undefined exterior) is invisible to downstream facet authors; sensory-flag selection and loc-state frugality both fail without a frame-anchor.
      criteria: A location-entry beat must exist at or before beat 220 that establishes where Taylor and oc-craftsman-mother are standing; the beat must name a slug-resolved location.

    - id: fault-003
      type: fault
      what: Scene H (beats 234–250) — no actor-enters-sept beat; scene opens with septon-rowan drawing a volume (beat 234) with no re-entry established after Scene G's exterior
      why: The sept is implied by context (prior sept scenes), but Taylor's re-entry is not marked with a discrete proto-line. Studio fork will cite the last explicit location-state entry from Scene F (Taylor exits the sept at beat 217), which makes Scene H's location temporally inconsistent with the Scene G exterior. Frame-anchor is absent.
      criteria: A taylor-hebert-jaehaerys enters the sept beat (or equivalent re-entry) must exist at or before beat 234 to re-establish the sept as the active location for Scene H.

    - id: fault-004
      type: fault
      what: Scene O (beats 565–643, mira POV) — no actor-enters-alley beat for Mira at scene open under the new POV; beat 563 (prior POV segment) closes with Taylor following Mira; beat 565 opens under mira POV with mira facing Taylor but no entry-beat for the alley under this POV; beat 628 mira enters the alley is a later re-entry, not an open
      why: The location-state fork for the mira POV segment has no frame-anchor to cite at scene open. Mira's position in the alley at beat 565 is confirmed only by inference from the prior Taylor-POV segment, which the mira POV fork may not reliably inherit.
      criteria: A mira-stonefield-jaehaerys enters the alley beat (or a `the alley` frame-anchor beat) must exist at or immediately before beat 565, establishing the location under the mira POV segment.

    # --- DIALOGUE ---

    - id: fault-005
      type: fault
      what: Beat 354 `oc-lords-steward speaks to the dock crowd` and beat 398 `oc-lords-steward speaks to the dock crowd` — listener slug is `the dock crowd`, which is not an actor slug and has no card in the warehouse
      why: Dialogue schema requires `<speaker-slug> speaks to <listener-slug>`. `the dock crowd` is an environment noun, not a slug. The dialogue-writer fork for oc-lords-steward cannot load a card, cannot author an objective, and has no anchor to write an utterance against. Both beats will produce malformed dialogue entries or be skipped entirely, leaving the two most public pronouncements of the census/levy machinery unvoiced.
      criteria: Both beats must resolve the listener to a slug-form entity (e.g., a named OC crowd representative, a named townsman, or the beats must be recast as `oc-lords-steward addresses [slug]` with a citable listener). If crowd-address is structurally intended, a crowd-entity OC slug must be introduced in the warehouse so the dialogue fork can anchor against it.

    # --- SENSORY ---

    - id: flag-001
      type: flag
      what: Scene G (beats 220–232) — no environmental sensory-inflection beat exists in the scene; all beats are character-action (touches shoulder, holds hand, speaks); no sound, light, thermal, or tactile environmental change is present
      why: Studio sensory fork has no bare-word environmental noun to cite for Scene G; the scene will produce zero sensory fires under rubric frugality (correct outcome given content), but if the scene is structurally intended to carry a sensory register (exterior light, weather, ambient sound), no anchor bone exists to support it. Scene may render flat in stitched output.
      criteria: Advisory only — no fixer required unless the scene-plan requires a sensory register for Scene G; if so, an environmental beat must be added.

    - id: flag-002
      type: flag
      what: Scene M (beats 521–540) — no non-sound, non-tactile sensory anchor; the scene is interior workshop, closed door; only cup-handling beats (536–538) provide tactile/liquid anchors; no light, thermal, or smell anchor present
      why: Sensory fork will produce sound-and-tactile-only coverage for Scene M, potentially contributing to modality-monoculture if the episode's overall sensory file lacks other modalities. Not a gap per se — Scene M is correctly sparse — but worth flagging for the file-level modality-coverage health-check.
      criteria: Advisory only.

    # --- TENSOMETER ---

    - id: flag-003
      type: flag
      what: Scene C (beats 62–80) — approximately 8 content beats; the scene contains no clear rupture/commit/peak beat; beat 73 `oc-craftsman-father lowers his voice` and beat 75 `taylor holds the breath` are the highest-charge beats but both are sustained-tension rather than rupture; the scene does not deliver a 3-rated beat by rubric criteria
      why: Tensometer rubric requires at least one 3 per scene or an explicit dramatist-flagged exception (scene-as-respite or scene-as-transit). Scene C functions as a transition from the evening workshop to sleep; it may be defensible as scene-as-respite, but the dramatist must mark it explicitly to avoid a kickback to screen-writer.
      criteria: Advisory — dramatist must either identify the 3-beat in Scene C or flag it as scene-as-respite in the tensometer file to close the curve-shape gap.

    - id: flag-004
      type: flag
      what: Scene G (beats 220–232) — same scene-level tensometer gap; 8 content beats, no rupture; the scene functions as transitional/post-sept relational; no physical commit or rupture present
      why: Same curve-shape expectation as fault-003 (tensometer rubric). Scene G is more clearly transit-class than Scene C but still requires explicit dramatist marking.
      criteria: Advisory — dramatist must flag Scene G as scene-as-transit.

    # --- NARRATOR-INTEREST ---

    - id: flag-005
      type: flag
      what: Mira-POV segment (beats 565–643) and oc-craftsman-mother POV segment (beats 701–787) — no narrator-interest rubric instance exists for mira-stonefield-jaehaerys or oc-craftsman-mother; the locked rubric at design/shoot-v2/rubric-narrator-interest.md is taylor-hebert-westeros-specific and explicitly notes that reuse requires re-authoring against the other character's behavior pack
      why: The NI fork dispatched for the mira and oc-craftsman-mother POV segments will lack rubric authority for channel identification, voice-fidelity calibration, and earning-axis judgment. The resulting NI files for those segments cannot be reviewed under the locked rubric. Downstream facets (memory-flags, audience-interest, state-updates) that depend on NI co-citation will have no validated spine entries for those POV segments.
      criteria: Advisory — POV-specific NI rubric instances must be authored for mira-stonefield-jaehaerys and oc-craftsman-mother before NI facet authoring proceeds for their segments. This is a process gap, not a content gap in the aggregate.

    # --- MEMORY ---

    - id: flag-006
      type: flag
      what: Swarm-rupture sequence (beats 455–479) — structurally the most charged cluster in the aggregate (tens=3 zone); memory-flags rubric forbids firing on tens=3 beats by default; the aftermath zone (beats 480–519) provides the correct quiet-beat anchor territory, but the aftermath is sparse (beats 502–508 are the main aftermath content) and only 7 content beats exist between the rupture and the next scene transition
      why: The swarm event is the strongest monument-trigger candidate in the aggregate (Earth-Bet fauna-control displacement + Westerosi institutional violence pattern). The memory-flags rubric inverted-tens rule pushes authoring into the aftermath zone, but the aftermath is thin. If the dramatist rates beats 502–508 as still-elevated (tens=2), the memory fork may find no quiet-beat anchor available and be forced to skip the monument entirely, which would be a file-level register gap.
      criteria: Advisory — screen-writer may want to add 1–2 aftermath beats in the 502–519 range at tens=1 to give the memory fork a validated quiet-beat anchor for the swarm displacement fire.

    # --- DENSITY FLAGS ---

    - id: fault-006
      type: fault
      what: Beats 32–60 (Scene B) — 26 consecutive content beats (from beat 32 to beat 59) with no internal time-skip marker; the stretch is a sustained parent-exchange scene including at minimum 12 dialogue-speaks-to beats among oc-craftsman-father, oc-craftsman-mother, and Taylor; the density exceeds the 10-beat threshold without inflection
      why: Facet authors (dialogue, feeling, sensory, tensometer) working across this 26-beat unbroken stretch will produce stale, repetitive output. The dialogue fork has no structural inflection to break on; the tensometer fork has no natural scene-boundary to mark a rise-peak-release; the feeling fork cannot satisfy its per-scene cap when the scene has no sub-scene markers. The rubric's over-dense flag criterion (10+ beats per scene without inflection) is met.
      criteria: At least 2 internal time-skip markers must be inserted within the beat 32–59 range to break the scene into sub-scenes or inflection zones; insertion points should align with the narrative structure (e.g., after beat 43 where the ruffles-hair moment closes a beat cluster, and after beat 51 where the tallow-lamp/candle sequence begins).

    - id: fault-007
      type: fault
      what: Beats 599–626 (within Scene O, mira POV) — 28 consecutive content beats (oc-lords-steward arrival at beat 599 through mira returning the bolt at beat 626) with no internal time-skip marker; contains 16 speaks-to beats among oc-lords-steward, the town reeve, and mira
      why: Same over-dense failure mode as fault-006. The oc-lords-steward interrogation of mira is structurally a single confrontation but 28 unbroken beats will produce repetitive dialogue and tensometer output. Feeling fork per-scene cap cannot be satisfied without structural sub-division.
      criteria: At least 1 internal time-skip marker must be inserted within the beat 599–626 range to create a scene-internal inflection point; insertion should align with the folio-marking at beat 618–619 (the procedural commit beat) as a natural sub-scene boundary.

    - id: flag-007
      type: flag
      what: Beats 127–149 (Scene E) — 23 consecutive content beats without internal time-skip; borderline at the 10-beat threshold; the tallow-lamp-gutters beat (140) and winter-candle-catches (148) provide natural inflection points but are not marked as sub-scene breaks
      why: At 23 beats the scene is over the threshold; facet authors will manage but may produce lower-contrast output. Not as severe as faults 006 and 007 given the natural candle-inflection structure. Flagged for advisory review.
      criteria: Advisory — a time-skip marker between beats 143 and 145 (candle-draw and candle-catch) would create a clean sub-scene break at the lamp-to-candle transition. Optional; scene is functional without it.

    # --- UNDER-DENSE STRETCHES ---

    - id: fault-008
      type: fault
      what: Beats 299–301 (triple consecutive blank time-skip between beat 298 oc-child-peer climbs the grain-stall fence rail and beat 302 oc-child-peer calls) — three blank beats with zero content bones in the interval; a chunk-implied beat (Taylor watching child on fence, transition from prior arrival to the called exchange) has no supporting SVO
      why: The chunk implies elapsed time during which Taylor observes the child on the fence — a structurally significant moment (Taylor's passive-fauna attention pattern should be active here, and the approaching peer-interaction is a monitored approach). No bone exists for any facet author to cite. Narrator-interest, sensory, and feeling forks have nothing to anchor against in this interval; the stitcher will render the transition as a pure time-skip with no weighted beats.
      criteria: At least 1 content beat must exist between beat 298 and beat 302 giving a discrete physical SVO anchoring Taylor's or the environment's state during the fence-climb interval; a fauna beat or a taylor-hebert-jaehaerys holds-the-feet/holds-the-face beat would satisfy.

    # --- NUMBERING / STRUCTURAL ---

    - id: flag-008
      type: flag
      what: Beat 389 — absent from the aggregate (sequence jumps from 388 to 390 in the Scene K dock confrontation); beat 219 also absent (sequence jumps from 217 to 220); beat 901, 902, 903 absent in the loft-close sequence (900, then 904)
      why: Deleted beats per schema (ID gaps are intentional deletions, not authoring errors). Flagging for completeness so facet authors know these are intentional gaps and not to backfill. No fixer action required.
      criteria: Advisory only — confirm deletions are intentional and no content was lost from the intended chapter-plan.

    - id: flag-009
      type: flag
      what: Beat 219 missing (sequence jumps from 217 taylor exits the sept to 220 oc-craftsman-mother speaks) — the gap is a single deleted beat immediately after the sept-exit; it may coincide with the Scene G location-establishing beat that fault-001-class gaps are already flagging
      why: The missing beat 219 may have been the location-transition beat (taylor crosses the lane, taylor reaches the lane, or similar) that established Scene G's exterior location. If so, its deletion is the proximate cause of the fault-002 location gap.
      criteria: This is informational context for fault-002. If fixer adds a location-establishing beat for Scene G, inserting it at position 219 (restoring the ID) or as a new insert-at would both satisfy. Fixer determines minimum change.
