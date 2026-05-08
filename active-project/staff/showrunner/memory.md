# showrunner memory — schema: schemas/showrunner-memory.schema.md

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: active-project/staff/showrunner/season-s01-plan.md

series:
  theme: The cost of building when everything resists you — and what you become in the process of building it anyway.
  laws:
    - Taylor Hebert is the protagonist. Full Gold Morning memories intact at reincarnation.
    - Taylor reincarnates as a baseborn human girl. No title, no house, no recognized identity.
    - The Riverlands are already in conflict at the story opening — no peaceful establishment arc.
    - Story begins 120 AC. Dance of Dragons ignites ~129 AC — approximately 9 years of story.
    - Taylor retains parallel multithreaded fauna control (insects, rats, ravens, non-complex fauna). Without shard buffering, use is physically punishing — cost curve in cond-fauna-control-rules.
    - On Earth-Bet, ASOIAF/Fire & Blood is published fiction. Taylor has event-level historical knowledge of the Dance. Historical knowledge is not personal knowledge — hard fence.
    - Reincarnation is a fresh start. No route back to Earth Bet. Gold Morning is closed.
    - No parahuman infrastructure in Westeros. No Shards, no PRT, no containment protocols.
  lore:
    - The Dance of Dragons is historical fact Taylor can anticipate; Westerosi characters cannot.
    - Westeros runs on blood legitimacy; Taylor has none and cannot fake an origin.
    - Riverlands lords are intensifying faction pressure at 120 AC — foraging, impressment, extortion.
    - Harrenhal has just changed hands to a Hightower-affiliated castellan (Lord Corwyn Hatch).
  behaviors:
    - Fast, pulpy, dramatic. Action and escalation are the primary registers. Not introspection-dominant, not chess-match scheming.
    - Taylor's escalation-reflex is structural: every escalation in Westeros has political or physical consequences she must navigate.
    - Violence-as-fluency — she speaks organized violence more fluently than almost anyone in this world.
    - Being correct and three moves ahead buys survival, not status. The environment punishes her constantly.
    - The feudal order does not adapt to Taylor; she must adapt to it or die.
    - Complications must escalate through each season, not concentrate at season finales (S1 pulp-enthusiast condition).
  plot:
    start: 120 AC, age 11, orphan ward at Harrenhal-shadow sept, three simultaneous opening pressures
    end: Dance of Dragons theater, ground-level network consumed by the war it was built to survive
    protagonist_arc: Anonymity → Invisibility → Neutrality → Sovereignty, each lost in sequence; the thing she built from nothing becomes the mechanism of her consumption
    series_question: Can someone who already paid the full price once build enough from nothing to matter when the second catastrophe arrives — and should they?
  cast_roster:
    - taylor-hebert-westeros
    - septon-dying-protector
    - oc-castellan-harrenhal
    - westerosi-traveling-maester
    - rymer-hedge
    - edric-cray
    - septon-rowan
    - mira-stonefield
    - ser-aemon-bracken
    - ser-harwick-plumm
    - ser-edwyn-celtigar
    - rhaenyra-targaryen
  stage_elements:
    - loc-harrenhal-sept-environs
    - loc-harrenhal-exterior
    - westerosi-smallfolk-dwelling-interior
    - westerosi-smallfolk-village-common
    - oc-riverlands-ruined-tower
    - oc-riverlands-river-ford
    - forest-clearing-dusk
    - cond-fauna-control-rules
    - cond-impressment-census-120ac
    - cond-riverlands-120ac-state
    - cond-westerosi-customary-authority
    - cond-no-parahuman-infrastructure
    - cond-reincarnation-mechanics
    - cond-series-tone-constraints

seasons:
  - slug: s01
    status: active
    timeline: 120–122 AC
    episodes:
      - slug: s01e01
        status: shot
      - slug: s01e02
        status: shot
      - slug: s01e03
        status: shot
      - slug: s01e04
        status: shot
      - slug: s01e05
        status: shot
      - slug: s01e06
        status: planned
    end_of_season_state:
      # Actor positions at proto-line sequence close (ch10 final line)
      # Updated 2026-05-07 from S4 continuity audit (fault-011)
      taylor-hebert-westeros:
        location: loc-harrenhal-interior (Harrenhal hall — ch10 final position; residual transit gap fault-002: approach road ch08-close → hall ch10-open; ch07 outer ward → ch08 side chamber → approach road is now recorded per restructure 2026-05-07)
        inventory: [] (castellan-wardship-document superseded by ward-of-administration entry)
        status: formally named ward-of-administration by oc-castellan-harrenhal; named and placed in Harrenhal's administrative structure
      septon-rowan:
        location: loc-harrenhal-interior (departed hall ch10 line 47; transit from village-common unrecorded, fault-006)
        inventory: [folio-with-motherhouse-and-recorder-papers]
        status: witnessed formalization; departed hall; returning to village-common area presumed
      ser-harwick-plumm:
        location: loc-harrenhal-interior (departed hall ch10 line 44 with ward-record scroll)
        inventory: [prop-intercession-record-book, prop-ward-record-scroll (sealed, carried out)]
        status: wrote and sealed ward-of-administration entry; Hatch-deputization persona card patch pending (margit parallel work)
      ser-aemon-bracken:
        location: oc-riverlands-river-ford (departed Harrenhal outer ward ch09 line 60; not present ch10)
        inventory: [] (prop-bracken-counter-claim-page left on castellan's table ch09)
        status: counter-claim filed ch09; contest resolved without him present; wardship did not go to Bracken
      westerosi-traveling-maester:
        location: unknown — departed Harrenhal interior side chamber ch08 line 26; en route east
        inventory: [prop-assessment-roll (sealed), satchel, chain, notebook]
        status: assessment complete (conducted in Harrenhal side chamber, not sept cottage — restructure 2026-05-07); sealed report delivered to great hall (ch08-interlude); maester not present ch09 or ch10
      oc-castellan-harrenhal:
        location: loc-harrenhal-interior (departed hall ch10 line 35)
        inventory: [prop-rolled-inspection-page/claim-document, prop-bracken-counter-claim-page]
        status: issued ward-of-administration determination under Celtigar pressure; departed hall before Rowan/Taylor exchange
      prop_custody_summary:
        - prop-ward-record-scroll: sealed, carried out of hall by ser-harwick-plumm (ch10 line 44)
        - prop-rolled-inspection-page/claim-document: held by oc-castellan-harrenhal (set on table ch09, not retrieved by Plumm after exit)
        - prop-bracken-counter-claim-page: held by oc-castellan-harrenhal (stacked with document ch09 lines 46-47)
        - prop-intercession-record-book: in Plumm's possession (pocketed ch05 line 66; not produced again)
        - prop-assessment-roll: carried by westerosi-traveling-maester (sealed ch08 line 23)
        - castellan-wardship-document: on sept chancel shelf or retrieved during unrecorded gap; superseded
      open_continuity_faults:
        - fault-001: ch09 raven fidelity at half-league range — fauna channel ceiling for speech-level feed from gatehouse sill
        - fault-002: Taylor transit from approach road (ch08-close) to Harrenhal hall (ch10-open) unrecorded; ch07 outer ward → ch08 side chamber path now resolved by restructure 2026-05-07; remaining gap covers ch09 roadside-rise to ch10 hall entry
        - fault-003: Plumm inventory not updated across chapter sequence (NOW RESOLVED in state files)
        - fault-004: ch06 sealed parchment prop-custody chain broken; ch07 line 93 sequencing ambiguous
        - fault-006: Rowan transit from village-common to hall unrecorded
        - fault-010: ch08 blank gap (lines 27-88) — Bracken filing and Celtigar letter scene may be missing or unextracted

active:
  season: s01
  episode: s01e06

# session-log: 2026-05-03
# Partial shoot of s01e01 run, halted after 3 bullets for diagnostic review.
# All shoot assets cleared. s01e01 reset to planned for clean restart.
# Fixes applied before reset:
#   - pulp-enthusiast card: clock-starting / setup-tolerance clause added to taste
#   - census-officer card: backfilled to cards/personas/ library with tier: minor
#   - impersonator: voice-priming step added; model upgraded to opus
#   - tier system: lead/supporting/minor field added to card schema; and-shoot A3/B4 routed
#   - coach: board-change, interior-inventory, action-consequence, content-anchor checks all in agent
#   - passive-sense vibe key in taylor-hebert-westeros/vibes.md — retained
#   - cond-reincarnation-mechanics tombstone — complete
#   - taylor-hebert/ stale dir — already removed

# session-log: 2026-05-07
# Actor state files refreshed from S4 continuity audit (fault-011):
#   ser-harwick-plumm/state.md — location updated to loc-harrenhal-interior; inventory populated with
#     prop-intercession-record-book (ch05) and prop-ward-record-scroll (ch10); prop chain-of-custody
#     for rolled inspection page and claim document documented in notes; Plumm card patch (Hatch-deputization)
#     pending from margit parallel work.
#   ser-aemon-bracken/state.md — location updated to oc-riverlands-river-ford (returned after ch09 exit);
#     movement log added; counter-claim filing documented; absent at ch10 resolution.
#   westerosi-traveling-maester/state.md — location updated from stale village-common to departed sept cottage
#     (ch08 line 26); prop-assessment-roll added to inventory; transit gap from ch05 to ch08 noted.
#   taylor-hebert-westeros/state.md — location updated to loc-harrenhal-interior (ch10 end position);
#     inventory cleared (wardship document superseded); transit gap (fault-002) noted in sublocation.
#   septon-rowan/state.md — location updated to loc-harrenhal-interior (ch10 line 47 exit);
#     prop-sealed-parchment-ch06 gap documented in notes; fault-004 custody ambiguity noted.
#   showrunner/memory.md — end_of_season_state block added with all actor positions, prop custody
#     summary, and open continuity fault list.

# session-log: 2026-05-07 (ch08 restructure)
# ch08 relocated to Harrenhal interior (side chamber) to honor fauna-control 600m ceiling (RESIDUAL-1 resolved by moving Taylor within range, not amending constraint).
# State files updated:
#   westerosi-traveling-maester/state.md — location updated from sept cottage to Harrenhal interior side chamber; movement log and timeline note revised.
#   taylor-hebert-westeros/state.md — fault-002 transit note updated: sept-environs framing superseded; residual gap now approach-road → hall only; ch07-outer-ward → ch08-side-chamber path recorded.
#   showrunner/memory.md — maester end_of_season_state entry updated; taylor location note updated; fault-002 description narrowed.
# Plumm/Bracken/Rowan state files verified consistent: no cottage references, Bracken and Rowan beats unaffected, Plumm beats unaffected.

# cut-log
cut: 2026-05-06 — mid-shoot — s01e06 (B2 of 71 complete; Phase A fully done; skip-wrap of s01e05 archived this session)
cut: 2026-05-06 — mid-shoot — s01e06 (B5 of 71 complete; SCENE 1 fully shot; two-clocks unresolved at the door for SCENE 2 open)
cut: 2026-05-05 — mid-shoot — s01e06 (B6 of 71 complete; SCENE 2 open; B7 pending — first POV-shift to Rowan; pipeline procedures hardened this session)
