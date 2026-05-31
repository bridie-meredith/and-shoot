# studio STM

## 2026-05-31 — /and-facets b01-c06 Phase 1 R1 location-state authoring (revise pass)

Authored location-state.md for b01c06 (2 entries after authoring-phase cull, 26 bones).
Single location throughout: oc-stitch-house-lane (the lane, blocked lane-mouth → south-court working position). Single time-of-day: morning.
Three scenes: scene-A rising-to-peak (handcart/crowd/Wren/omission), scene-B flat-tense (loaded pause), scene-C rising-to-peak (accounting/send/contrast).

Fires:
  loc-state:1 @1 — morning chapter-open place-anchor; lane-mouth blocked by the handcart crossways; crowd backing the junction; establishes the active obstruction as the first environmental condition
  loc-state:2 @5 — threshold crossing: taylor enters the south court via angle-gap workaround; distinct sub-space off the tallow-boiler's wall; establishes south-court working position as the inherited base for all scene-B/C action

Cull (authoring phase): 1 entry removed
  @3 (wren crosses the crowd — movement verb, but frugality REJECT: the crowd is already established at @1; crossing through a crowd that exists in inherited state adds no new location fact; strip test: @3 resolves cleanly in inherited @1 env)

Confirmed REJECT decisions:
  @2 (crowd presses junction — stillness/hold of crowd mass; persistence of @1 condition; anti-pattern 3)
  @3 (wren crosses crowd — see cull above; frugality REJECT)
  @4 (wren speaks to taylor — pure dialogue beat, no positioning in question; REJECT per necessity §)
  @6–@9 (administrative/dexterity verbs in-place; scene-A south-court holds in inherited @5)
  @10–@15 (scene-B: @10 = informational arrival, no new location-moment; @11–@15 = dexterity/administrative in-place; inherited @5 south-court throughout)
  @16–@26 (scene-C: all dexterity/administrative/stillness in-place; @24 courier-takes strip-test passes in inherited @5; @25–@26 dexterity in-place)

No continuity-carry entries:
  scene-A @1-@2 fusion-run: covered by @1 place-anchor; no separate carry needed
  scene-B @11-@12 fusion-run: rhythm-shape is flat-tense — NOT a qualifying shape (license requires flat-low/resolving/release-only); REJECT
  scene-C @16-@17, @21-@22 fusion-runs: rhythm-shape is rising-to-peak — license excluded

No flagged seams.

## 2026-05-31 — /and-facets b01-c07 Phase 1 R1 location-state authoring

Authored location-state.md for b01c07 (5 entries after authoring-phase cull, 25 bones).
Single location throughout: oc-sept-corner (the chandler's storehouse / sept corner, the Hook, Flea Bottom). No location change across the chapter.
Three scenes: scene-A morning (handcart blocking), scene-B late-morning (time advance; handcart cleared; argument begins), scene-C late-morning (counter + departure).

Fires:
  loc-state:1 @1 — morning place-anchor; circuit halted at handcart-blocked choke-point
  loc-state:2 @7 — enters sept-corner; passage-clearing; sept-bay shadow on crossing-stone threshold
  loc-state:3 @9 — scene-B time-advance anchor (morning → late-morning); cold-holding ground unwarmed past light-shift
  loc-state:4 @15 — plants the feet (peak bone @15; substance_delta social_tether +0.5); ground cold underfoot at standing weight
  loc-state:5 @23 — leaves the sept-corner; cross-lane mouth exit; clears Halvard's sight line

Cull (authoring phase): 0 entries removed.
All 5 entries pass strip / pointing / frugality / previous-entry tests.
Confirmed REJECT decisions:
  @2 (handcart blocks passage — environmental-persistence/stillness beat; REJECT per anti-pattern 3; @1 already establishes blocking condition)
  @13 (taylor goes still — stillness/hold beat; explicit REJECT per rubric necessity section)
  @14 (taylor faces halvard — social positioning, not through-space movement; location-card already covers sight-lines; REJECT)
  @17 (sept-corner ground grips — environmental-persistence/atmosphere beat; inherits from @15; REJECT)
  @22 (taylor steadies the feet — same location/time/ground as @15; frugality REJECT — inherits from loc-state:4)
  @24 (lane cold grips sept-corner stone — persistence beat; anti-pattern 3; REJECT)
  @25 (clears the Hook — departure complete; already covered by exit at @23; frugality REJECT)
No continuity-carry entries: scenes B + C are rising-to-peak (license excluded); scene-A fusion-run @1-@2 covered by place-anchor at @1.
Flagged seam: @15 vs @9 frugality margin — @9 establishes cold-holding ground; @15 fires on the same ground. Defensible because @15 is a peak bone (substance_delta; the planted weight is what the ground's cold physically grips) and the pointing test returns a distinct focus-element ("soles at planted weight" vs. "stone holds night cold past light-shift"). Flagged for R2 reviewer.

## 2026-05-28 — /and-facets b01-c05 Phase 1 R1 state-updates-env authoring

Revised existing state-updates-env.md for b01c05 (7 entries, 31 bones; env + prop slice only).
Key corrections applied: entry 1 anchor moved from @1 to @2 (anti-pattern #7 guard; @1 is world-before-protagonist); field name corrected from active_location to location (matches studio state.md schema line 8).
Fires: @2 studio.location (oc-stitch-house-lane → the-rushwick); @3 studio.coverage_active_range (four-ward-complete → rushwick-included); @16 prop:oc-enforcement-report-entry.state (absent → filed-with-jarvis; field-extension); @18 prop:oc-courier-body-map.state (absent → initiated; field-extension; cf-d10 anchor); @20 studio.location (the-rushwick → taylor's-lodging); @20 studio.time_of_day (morning → evening); @27 prop:oc-courier-body-map.state (initiated → filed).
Density: 7/31 = 22.6%; above band but defended — 2 record-creation events + 2 prop-state promotions; each entry survives strip-test and persistence-test.
Skip-notable: @1 (pre-empt guard), @7 (peak-bone env-silent; coverage-release is registration), @10 (side-alley sub-zone held; anti-pattern #10 avoided), @13 (peak-bone env-silent; sensory carries effortful), @15 (pre-empt guard; delivery at @16 is canonical irreversible beat), @25 (peak-bone env-silent; actor-fork's authority).
Flagged seams: SEAM-001 (taylor's-lodging noun-form lacks oc-card; margit referral); SEAM-002 (oc-enforcement-report-entry.card.md needed); SEAM-003 (oc-courier-body-map.card.md needed before b01c06); SEAM-004 (chapter-close time_of_day = evening; b01c06 Phase 0 must account for time-of-day reset).
Chapter-close env state: location = taylor's-lodging; time_of_day = evening; coverage_active_range = rushwick-included; prop:oc-courier-body-map.state = filed; prop:oc-enforcement-report-entry.state = filed-with-jarvis.

## 2026-05-28 — /and-facets b01-c05 Phase 1 R1 sensory authoring (FILED)

Filed sensory-b01-c05.md (2 entries, 35 bones). Density 2/35 = 5.7% — within 3-6% band (state.md carried stale 31-bone count yielding 6.45% ADVISORY; corrected here — no ADVISORY applies; standard band).
Two fires across two modalities:
  sensory:1 @4 tactile (lane-stone-surface-baseline → provisioner-cart-load-on-stone, spike) — scene-A, provisioner-train crossing junction with loaded carts. Old-state sourced from loc-state:1 @1 + oc-rushwick Texture vocabulary.
  sensory:2 @13 sound (alley-stone-contained-silence → courier-effortful-body-sound, spike) — scene-B, mandatory bones-review note-003 carry; effortful-qualifier stripped at Phase 6 fault-002; dark-fantasy gap-instrument. Old-state sourced from loc-state:7 @11 (alley-interior contained) + oc-rushwick Sensory Vocabulary (side-alley sound-gap defined). Anchor @13 per locked state; SEAM-005: more precise anchor may be @14 (alley-returns-sound bone is the explicit perceptual event) — flagged for R2 reviewer attention.
Modalities: tactile + sound (2; floor met).
note-003 effortful-qualifier: CONFIRMED CARRIED at sensory:2 @13.
note-001 courier-walk visual/spatial: NOT CARRIED — rubric-ineligible (interior replay / fauna-feed-extension); routed to narrator-interest.
Tallow-smoke: NOT fired — sustained ambient per oc-rushwick ("consistent ambient note"); belongs in loc-state baseline, not sensory inflection; correct omission.
Scene-C: 0 fires — all bones cognitive/replay; indoor env established at loc-state:9 @20; no discrete perceptual inflection above threshold.
Per-scene cap: scene-A 1 fire (≤3 ✓), scene-B 1 fire (≤3 ✓), scene-C 0 fires (≤3 ✓).
Inflight: theater/facets/_inflight/proto-lines-sensory.md filed (byte-identical SVOs + [sensory:N] tokens).

## 2026-05-28 — /and-facets b01-c05 Phase 1 R1 location-state authoring

Authored location-state.md for b01c05 (9 entries after authoring-phase cull, 31 bones).
Single location: the-rushwick (no oc-card; pl-2026-05-28-001 flagged for margit).
Three scenes: scene-A outdoor morning (junction + lane-mouth + east-exit), scene-B outdoor morning (side-alley sub-location), scene-C indoor evening (lodging room-floor).
Fires: @1 world-before-protagonist anchor (lane-mouth/stone-skirt); @4 junction provisioner-train; @6 junction message-runner; @7 lane-mouth coverage-edge; @8 lane-mouth courier-entry; @10 side-alley entry; @11 alley-mouth blocked; @17 alley-mouth reopened; @20 indoor room-floor scene-C anchor.
Cull (authoring phase): 4 candidates removed (@2 enters-rushwick; @5 takes-east-lane; @14 finds-feet; @19 takes-junction-corner).
No continuity-carry entries: all scenes excluded by rising / rising-to-peak rhythm-shape.
Seam flagged: @3 (insect-feed fills junction — feed-perception beat, inherits @1), @9 (holds wall-line — stillness, inherits @8), @12 (pin courier — contact-in-place, inherits @11), @13 (alley returns sound — environmental-agency/sensory beat, inherits @11; sensory facet carries "effortful" qualifier), @15–@16 (filing/delivery dexterity — inherit @11/@8 per scene position).
Scene-C inherited: @21–@31 all inherit from @20 (room-floor); all are cognitive/replay beats with no loc-state change.

## 2026-05-27 — /and-facets b01-c04 Phase 1 R1 state-updates-env authoring

Authored state-updates-env.md (14 entries, 39 bones; env + prop slice only; actor state separate).
New field: studio.coverage_active_range (field-extension; tracks four-ward insect-feed footprint as env-observable; 3 fires at @15/@22/@27).
New prop: prop:oc-report-sheet (field-extension; holder chain @31→@32; pocketed by Jarvis; exits scene @36).
Chapter-close state: four-ward coverage active; oc-report-sheet in Jarvis's coat; yard empty; Taylor exiting stitch-house lane.
Density 14/39 = 36%; above rubric band but justified by multi-ward / multi-day structure; rubric-carve-out preamble filed.
Culled at authoring: 1 entry (middens-cart @17 — strip-test fail; no downstream canonical relevance).

## 2026-05-27 — /and-facets b01-c04 Phase 1 R1 location-state authoring

Authored location-state-b01-c04.md (6 entries after cull, 39 bones).
Four locations across three scenes: oc-cooper-yard-eel-alley (scenes A + C), oc-pig-tallow-lane (scene B), oc-ropers-court (scene C), oc-stitch-house-lane (scene C walk-back).
Fires: @1 chapter-open place-anchor (tallow-damp); @4 shed-wall cover geometry; @13 pig-tallow-lane place-anchor (junction-mouth convergence); @25 roper's-court place-anchor (early-morning grey; sight-clear tributaries); @29 location-switch back to cooper's yard (handoff geometry; half-yard open air); @39 stitch-house-lane chapter-close (north-end lane-mouth).
Cull: 2 deleted. @17 (carter parks cart — no actor movement immediately turns on cart position). @36 (Jarvis exits cooper's yard — exit legible in inherited @29 env; @39 provides stitch-house-lane anchor independently).
No continuity-carry entries: all three scenes excluded (scene A: rising; scene B: rising-to-peak; scene C: rising-to-peak-to-trail — none qualify; @33-@34 run is 2 bones, below minimum).
Scene C location-sequence seam flagged: @29 (loc-state:5) marks the location switch from roper's-court to cooper's-yard within scene C; no explicit Taylor-enters-yard bone between @28 and @29 — stitcher infers transition from loc-state citation on @29.

## 2026-05-27 — /and-facets b01-c04 Phase 1 R1 sensory authoring

Authored sensory-b01-c04.md (3 entries, 39 bones).
Four locations across three scenes: oc-cooper-yard-eel-alley (scene-A @1-@12), oc-pig-tallow-lane + oc-stitch-house-lane (scene-B @13-@24), oc-ropers-court + oc-cooper-yard return + oc-stitch-house-lane walk-back (scene-C @25-@39).
Three fires: @1 smell (eel-alley-dawn-air → tallow-damp-lane-caulking); @13 smell (tallow-damp → middens-discard-compound); @25 sound (carter-work-ambient → roper's-court-near-silence).
2 modalities: smell + sound. Density 7.7% — marginally over 6% ceiling; all three entries survive strip-audit (no sustained-as-inflection, no charged-word, no fauna-feed). Flagged as seam.
Cull: 0 entries removed.

## 2026-05-26 — /and-facets b01-c03 Phase 1 R1 location-state authoring

Authored location-state-b01-c03.md (5 entries, 36 bones).
Two micro-locations: morning market in the Hook (scene A @1-@12) + cooper's yard off Eel Alley (scenes B+C @13-@36).
Five fires: @1 scene-A market anchor; @13 scene-B location switch; @15 Jarvis enters yard (composite); @26 scene-C anchor; @32 Jarvis departs (composite shift).
No continuity-carry entries (scene-A fusion-run @1-@3 excluded by rising rhythm-shape; scene-C @33-@34 run too short at 2 bones for license).

## 2026-05-26 — /and-facets b01-c02 Phase 1 R1 location-state authoring

Authored location-state-b01-c02.md (11 entries, 47 bones).
Three-scene chapter; single precinct location (oc-stitch-house-lane) throughout.
Environmental arc: dawn → morning (coverage extension) → dusk (shadow-fills drain angle).
Parking-lot item pl-2026-05-25-019 addressed at loc-state:7 @22 (alley-mouth shared spatial frame).
Continuity-carry at loc-state:11 @44 (dusk-shadow through fusion-eligible-run @44–@46).
