# render-log — b01-c05

profile: schema-defaults (no active-project/theater/stitch-profile.md; matches c01/c02/c03/c04)
persona: neutral (library: staff/stitcher/personas/neutral.md; no project-scoped persona)
narrator: taylor-hebert-kl-122ac
voice: first-person past, contractions: profile-default-off (Taylor cold-utilitarian register; c01-c04 precedent)
phase-7-mode: strict (schema default)
generated-date: 2026-05-28
slug: b01-c05
bones-file: active-project/theater/bones/b01-c05.md
cite-index: active-project/theater/facets/_cite-index.md
scene-map: active-project/theater/facets/scene-map-b01-c05.md
phase-1-mode: scene-window (schema default; URI-SCENE-WINDOW; URI-SUBSTANCE-OVERHAUL)
voice-exemplar-candidates: [active-project/voice-exemplar.md]  # series-level; N=1 single-arm; POV 1st-person, matches header
cherry-pick: n/a (N=1, no-op)
allow-bare-speech: false (no-speech episode — chapter has zero speak-bones, /and-write Phase 1.5 SKIPPED)
keep-drafts: false (Phase 8 default prune)
re-stitch-context: post /and-write revise --from-signals (2026-05-28); prior c05 stitch FAILED Phase 9 cold-read; archived to draft/_archive/2026-05-28-c05-pre-revise/; prior render-log preserved at render-log-b01-c05-pre-revise.md

## Phase 0 — validate + load

inputs present:
  - bones: 35 (3 scenes per scene-map; 7+15+13 across s01/s02/s03)
  - cite-index: present (SHA: 3758943716d1526a post-Phase 5 cycle-3 CLEAN)
  - scene-map: present (scene-A @1-@7 rising | scene-B @8-@22 rising-to-peak | scene-C @23-@35 rising-to-peak-to-foreclosure-confirmed)
  - exposition: present (4 entries: 1 italic-preamble @0 + 1 preamble-paragraph @0 + 2 em-dash-fold first-mention at @2/@8)
  - dialogue: ABSENT (no-speech episode; not legacy-fallback)
  - voice-exemplar: single arm (active-project/voice-exemplar.md ~280 words; Marilynne-Robinson-style contemplative first-person; POV 1st matches bones-header narrator: taylor-hebert-kl-122ac)
  - feedback-file: absent

parking-lot scan:
  - no items target /and-stitch b01-c05 (HARD or SOFT)
  - (resolution carry: pl-2026-05-28-002 Sera-architecture HARD resolved at /and-facets Phase 5b 2026-05-28)

## Phase 0.6 — exposition consumption

exposition-source: facet (active-project/theater/facets/exposition-b01-c05.md)
preamble-source: exposition-facet (not legacy-fallback)
preamble-file: active-project/draft/b01-c05.preamble.md

episode-open pool (rendered as preamble; 2 entries):
  - exposition:1 @0 prior-episode-bridge italic-preamble (110/120 words; first-person Taylor; sources cite chapters[b01c05].handoff_in + chapters[b01c04].handoff_out + cond-taylor-pov-behavior + cond-kl-geography-122ac)
  - exposition:2 @0 episode-open-context preamble-paragraph (78/80 words; Sera-architecture WHO+WHAT+WHY trio resolving pl-2026-05-28-002 HARD; sources cite actors/sera-hightower-kl-122ac + actors/otto-hightower + chapters[b01c05]s01/s03 force-blocks)

per-anchor first-mention pool (staged for Phase 1; 2 entries):
  - exposition:3 @2 first-mention-place the-rushwick em-dash-fold (26/30 words)
  - exposition:4 @8 first-mention-character the-courier-rushwick em-dash-fold (28/30 words)

per-anchor scene-orient pool: empty (no scene-open-orient entries; R1 + R2 refused all 3 candidate scene-boundaries — chapter-open triple-stack at @1, scene-A→B continuity at @8, scene-B→C clause-b loc-state:9 carries at @23)

## Phase 0.7 — dialogue intake

dialogue-source: ABSENT (no-speech-episode; legitimate)
speech-bones: 0
speakers: ∅
character-files-loaded: 0
utterances-staged: 0
bare-speech-bones: 0
unmoored-utterances: 0
speaker-mismatches: 0

Per Phase 0.7 § "If the directory is empty AND the proto-lines file contains any `<X> speaks to <Y>` bones" — DOES NOT FIRE (no speech bones). Dialogue staging skipped without abort; no `--allow-bare-speech` needed.

## Phase 1 — lens-anchored render (scene-window mode)

fork-001 scene-A bones=@1-@7  scene-window-render
   bones-consumed: @1, @2, @3, @4, @5, @6, @7
   back-look: empty (scene-A is chapter-open; preamble at active-project/draft/b01-c05.preamble.md prepended at Phase 8 — not in scope here)
   forward-look: scene-B opens @8 (courier enters lane-mouth) — preserved geographic vocabulary headroom: "lane-mouth" used twice in scene-A (L1 entry-geometry, L7 release-threshold) but both load-bearing; "junction" / "side-alley" / "wall-line" reserved for scene-B
   exposition-folded: exposition:3 @2 em-dash-fold rendered verbatim (26 words; "a lane-cluster between the hill's stone skirt and the city's upward lean, alleys for passing not selling, ground abutting the lower Red Keep servant-passages") at L2
   facets-folded:
     - loc-state:1 @1 → L1 co-anchor fold (cool damp under paving, harbor-side light, north face in shade)
     - loc-state:2 @5 → L5 co-anchor fold (stone narrowing along hill-skirt, lane falling into morning light past the wall)
     - loc-state:3 @7 → L7 co-anchor fold (lane-mouth widens at threshold; coverage release at boundary)
     - sensory:1 @4 → L4 co-anchor fold (cart-wheels grinding over paving in heavy uneven rhythm of stone — tactile cart-wheel-on-stone)
     - narrator-interest:1 @2 → L4 near-anchor fuse (discipline-as-load-bearing transferred from Roper's Court — moved one beat to first body-read where the read actually fires; flagged minor anchor-slip in bone-walk)
     - narrator-interest:2 @5 → L5 same-anchor fuse (different-substrate-than-Hook + categorization-layer-engaging-without-naming-layer-above; rendered as "not Hook foot-traffic" + "a different substrate under the same categorization; the layer above it stayed unnamed" — surface-fence kept, NI's compound "categorization-discipline-as-load-bearing" NOT rendered literally per Q9)
     - vibes:1-4 → bias-only (register/cadence operator; no token-bundle phrases imported; "novel-coverage-substrate" / "cold-utilitarian" / "residue-not-spectacle" read as register choice — flat clinical-accounting cadence, no spectacle-naming on first court-tier exposure)
   variance-moves:
     - @4 provisioner-train "came through from the south side" / @6 message-runner "came across after them" — varied direction-and-aspect verbs for the two transit-pair openings (avoids verb-stem repetition on the two parallel bones)
     - @5 "took the east-lane" / @7 "took the lane-mouth" — verb repetition retained (concrete + bone-faithful; abstracting either to "moved into" would trigger FAULT-VARIANCE-ABSTRACTION per scene-A guidance); the route-noun differs and carries the variance
     - cart-wheel sensory at @4 prevents the provisioner-train transit from reading identically to the message-runner transit (no sensory on the runner — runner is "alone, no load, tighter compressed gait" — body-shape variance carries the differentiation)
     - exposition:3 em-dash-fold at @2 places the gloss inside the entering-action clause (not as standalone sentence) so the world-before-protagonist register set by L1 is not broken by an information dump
   refusals:
     - did NOT render NI's stitched compound "categorization-discipline-as-load-bearing" literally (Q9 anti-jargon fence); rendered the underlying register move at L4 ("read them the way I had read every body since coverage came up… no affect required to file them") and L5 ("different substrate under the same categorization; the layer above it stayed unnamed")
     - did NOT use "discipline" lexeme in scene-A despite NI:1 firing — register move rendered without the word to preserve word-budget headroom for narrator:3 @10 region and downstream uses (NI saturation watch 4/10)
     - did NOT decorate L3 (feed-fills-junction) with vibes:1's "novel-coverage-substrate" naming; rendered as "the count settled the way it had always settled" — discipline-transfer reading, not novelty-marking; the substrate-difference call is held for L5 NI:2 fold
     - did NOT split @5 into two paragraphs (peak-shadow standalone-sentence rule satisfied by leading L5 sentence; NI:2 follows in same paragraph)
   bone-walk:
     - @1 (hill's stone skirt meets lane-mouth) → L1 | world-before-protagonist open; loc-state:1 co-anchor fold (cool damp paving, harbor light, north shade)
     - @2 (Taylor enters Rushwick) → L2 | first-person entry verb ("I stepped into the Rushwick"); exposition:3 em-dash-fold inline verbatim; NI:1 register-move displaced to L4 near-anchor fuse (anchor-slip minor — first body-read is the natural fire-moment)
     - @3 (insect-feed fills junction) → L3 | "The feed filled the junction" + texture detail (lintels, wall-seams, cart-shadow) + register continuation ("settled the way it had always settled")
     - @4 (provisioner-train crosses junction) → L4 | "A provisioner-train came through from the south side"; sensory:1 co-anchor fold (cart-wheels grinding, heavy uneven rhythm); NI:1 fuse ("I read them the way I had read every body since coverage came up")
     - @5 (provisioner-train takes east-lane) → L5 | peak-shadow STANDALONE leading sentence ("The train took the east-lane…"); loc-state:2 co-anchor fold; NI:2 fold (substrate + unnamed layer above) follows as separate sentences in same paragraph
     - @6 (message-runner crosses junction) → L6 | "A message-runner came across after them"; body-shape contrast to provisioner-train (alone, no load, tighter compressed gait); no facet folds at this anchor
     - @7 (message-runner takes lane-mouth) → L7 | peak STANDALONE single-sentence paragraph; loc-state:3 co-anchor fold (lane-mouth widens at threshold, coverage releases at boundary); coverage-release-as-discipline's-physical-limit rendered as "the coverage I held released him… the count holding to its side of the boundary"
   drift-risk: minor — NI:1 anchor-slip @2 → L4 (one bone later than the facet anchor); rationale: the discipline-transfer read fires more cleanly at first body-read than at entry-and-hold; fence not crossed (still in scene-A, still inside the @2-@5 NI-firing window per scene-map). No bone CUT, no bone RENDERED-ILLEGIBLE, no RESHOW required. No FAULT-VARIANCE-ABSTRACTION (concrete verbs available for both transit pairs). No Q9 jargon coinages. No protected-pattern violations: world-before-protagonist open intact at L1; two-body categorization rise @4-@5 + @6-@7 rendered as parallel transit pairs with differentiated body-shape and rhythm-shape rising into peak @7.

fork-002 scene-B bones=@8-@22  scene-window-render
   bones-consumed: @8, @9, @10, @11, @12, @13, @14, @15, @16, @17, @18, @19, @20, @21, @22
   back-look: scene-A close at L7 ("the runner gone past the wall before the next body entered") — the next body IS the courier; scene-B opens on continuation, not re-introduction. Lane-mouth geography not re-established; courier-arrival is the new content. Avoided re-opening verbs from scene-A ("stepped into" / "came through from the south side" / "came across after them" / "took the lane-mouth"); "came into the lane-mouth" is verb-stem-shared with scene-A "came through" but the route-noun + agent + the deferred-then placement carries differentiation.
   forward-look: scene-C opens @23 (Taylor takes the room-floor) — discontinuous time-skip from morning-Rushwick to evening-lodging; scene-B close at @22 is post-incident scene-exit (count releases courier at junction-corner forty feet off held line). No forward bridging needed; the scene-shift handles itself.
   exposition-folded: exposition:4 @8 em-dash-fold rendered verbatim (28 words; "a man the feed had now flagged three mornings running on the same heel-first gait through the same lane, filed as recurring body, no name attached"). Voice-transform applied: facet's "Taylor's feed" rendered as "the feed" per first-person POV (the possessive collapses naturally in first-person register; the feed IS Taylor's instrument by frame).
   facets-folded:
     - loc-state:4 @10 → L2 co-anchor fold (wall-line; cool stone of hill-skirt; sightline to junction broken only by gap in building seam; tallow-smoke drifting east from stitch-house ward + thinning before the corner)
     - loc-state:5 @11 → L3 co-anchor fold (single-file because alley took one body at a time; rough original stone for walls; uneven flooring underfoot). Acoustic-baseline (alley-interior-contained-silence) NOT folded at @11/@12 — held for @14 emission event where it carries the perceptual logic ("the walls of the alley turned the noise…inward and then outward at the mouth")
     - loc-state:6 @12 → L3 co-anchor fold (two of them turned and held the width of it; alley-mouth sealed by their bodies; admits no third) + categorization-tag from vibes:8/scene-B-chunk-content folded as bone-body register ("not robbery, the approach was wrong for robbery, the coordination was wrong") — enforcement-vs-robbery distinction carried on-bone per exposition cull-pass DROP rationale (bone-body carries; no first-mention-character gloss for anonymous transients)
     - loc-state:7 @20 → L9 co-anchor fold (alley-mouth clear; east-lane visible through gap behind them)
     - loc-state:8 @22 → L11 co-anchor fold (junction-corner at east turn; forty feet off held line)
     - sensory:2 @14 + loc-state:5 acoustic-baseline → L5 co-anchor fold; the bone SVO "the side-alley returned the sound" rendered as the leading standalone sentence; the perceptual mechanism (walls turning noise inward then outward at the mouth; effortful body-sound below human-register threshold until alley-emission carries it) folded as the second sentence + gap-instrument fold at sentence close ("the feed had no field for what the alley delivered")
     - narrator-interest:3 @10 → L2 same-anchor fuse ("Third sighting in three mornings; the feed had him filed already; the hold was the hold I had used at every junction since coverage came up") — discipline-at-the-body-not-at-the-cognition register; uses the "discipline" lexeme deferred from scene-A NI-saturation watch (now justified at NI:3's recurring-body anchor)
     - narrator-interest:4 @14 → L5 same-anchor fuse ("the feed had no field for what the alley delivered") — gap-registered-as-gap; the not-naming IS the read; rendered as the closing clause of the gap-instrument paragraph
     - narrator-interest:5 @19 → L8 same-anchor fuse ("the report had a destination, and the destination was the architecture that held someone else's exposure at a length of someone else's arm") — folding via memory:1 quotation; the form's destination IS the architecture register carried at the @19 anchor; SUBSTANCE-DELIVERY satisfies pl-2026-05-28-002 implicit-Sera-routing per /and-facets Phase 5b resolution
     - narrator-interest:6 @21 → L10 same-anchor fuse ("the entry going in as recurring body with enforcement-incident attached, no name written into a ledger where his face would have one") — cf-d10 thread anchor + body-map-without-naming-into-ledger discipline
     - memory:1 @19 → L8 verbatim quotation fold (Westerosi-monument-clamp protective-arrangement-at-distance register; surface preserves "the architecture that held someone else's exposure at a length of someone else's arm"); displacement-discipline clean — no Sera/Otto/Jarvis named; the routing-destination IS the architecture
     - state-updates: state:3 @17 (jarvis-form filing) carried implicit in L8 filing-triad — "I filed the incident into the form the feed kept for enforcement-incidents"; state:1 + state:9 @21 (body-map initiated; courier added) carried in L10 ("I added the courier to the body-map…the entry going in as recurring body")
     - vibes — bias-only: vibes:5 @9 (apparatus-filing-before-operator) → register the courier-return-from-feed sentence in apparatus-priority cadence ("the feed returned him from where it had been holding him, sorted him into the cut his prior sightings had opened"); vibes:6/7/8 @14 (gap-instrument feed-logging-silence + world-above-apparatus-ceiling) → cadence of the gap-instrument paragraph rendered without token-bundle phrases ("dark-fantasy-world-above-apparatus-ceiling" NOT rendered literally); vibes:9 @17 (atonement-as-repetition) → NOT rendered as architecture-naming; @17-@19 rendered as procedure per the brief's force-block discipline
   variance-moves:
     - @8 opens with "The courier came into the lane-mouth then" — the trailing "then" defers the verb-shape from scene-A's "stepped into" / "came through" / "came across" / "took"; the deferred-then construction carries the temporal continuity to scene-A's "before the next body entered" without re-establishing geography
     - @9 "returned him from where it had been holding him, sorted him into the cut his prior sightings had opened, and let the count carry on" — three apparatus-verbs (returned / sorted / carry on) in a triple cadence; "cut" preferred over scene-A's "settled" / "filled" for the slot-opening register; the apparatus-priority cadence reads as filing-before-operator-names-recurrence (vibes:5 register choice)
     - @10 broken across two sentences in L2 paragraph: physical hold (wall-line + sightline + tallow-smoke) then cognitive hold (third-sighting + feed-already-filed + same-hold-since-coverage) — separates loc-state co-anchor from NI:3 register fold so the body-discipline and cognition-discipline don't run together
     - @11-@12 fused into L3 paragraph (scene-map fusion-eligible-run): @11 enters-side-alley + alley-geometry; @12 closes-alley-mouth + containment-fact + enforcement-vs-robbery categorization; fusion legitimate because both are approach-geometry beats with shared loc-state surface; the em-dash extension into the enforcement-vs-robbery clause holds the categorization without splitting into a fourth paragraph
     - @13 standalone single-sentence paragraph ("The third pinned him to the stone") — peak-shadow-bones discipline per scene-map; physical pin to stone is the act
     - @14 standalone leading sentence ("The side-alley returned the sound") then continued in same paragraph with sensory:2 + loc-state:5 acoustic-baseline mechanism + NI:4 gap fold — the peak-bone SVO stands alone as required, the mechanism explanation expands without collapsing into a summary
     - @15 standalone single-sentence paragraph ("The courier raised his spine") — gap-instrument-triple middle beat; spine-raise disambiguates @16's finds-feet per cold-read failure (ii) prevention
     - @16 standalone single-sentence paragraph ("He found his feet under him and stood") — finds-feet beat; the addition of "and stood" is the recovery-completion, not a fusion (sequential recovery per scene-map protected-pattern)
     - @17-@19 rendered as three structurally distinct cognitive operations within L8 paragraph: "I filed…" (categorize-into-form) / "I delivered…" (transmit-to-outbound) / "I drafted…" (route-up-to-architecture) — cause-chain cold-read failure (i) prevention; the routing destination naming at @19 is the third sentence and folds memory:1 verbatim
     - @20 transition out: "the three figures came out of the alley-mouth" — verb "came out" varies from @11 "came into the side-alley"; the loc-state:7 fold (alley-mouth clearing + east-lane visible) is the spatial release; "unhurried purpose of the gait" carries vibes:9 cadence without naming atonement-as-repetition
     - @21 + @22 split into two short paragraphs (L10 + L11): @21 body-map-entry + ledger-discipline; @22 junction-corner + count-releases-him — preserves cf-d10 thread anchor at @21 as its own beat
   refusals:
     - did NOT render vibes:9 "atonement-as-repetition" label or its surface cognates ("atonement" / "repetition-as-architecture" / "the architecture catching its own reflection") at @17-@19 — rendered as procedure per force-block discipline; @17 + @18 are clinical-procedural sentences ("I filed…" / "I delivered…") with no architecture-naming until @19 where the routing destination IS the architecture register per memory:1 verbatim
     - did NOT collapse @14-@15-@16 gap-instrument triple into a summary or fused paragraph — three distinct paragraphs per scene-map protected-pattern + URI-STITCH-SIGNAL-CLUSTER soft-gate
     - did NOT collapse @17-@18-@19 filing-triad into single beat — three structurally distinct cognitive operations within one paragraph per cold-read failure (i) prevention
     - did NOT name Sera / Otto / Jarvis at @19 — memory:1 verbatim language holds the Westerosi-monument-clamp displacement; the protective-architecture surfaces as routing-destination shape, not as named protected party (s01/s03 force-block discipline preserved)
     - did NOT decorate @17-@19 with cognitive-naming of what the form is or where it goes beyond the bone-body's "the form the feed kept for enforcement-incidents" + "the report had a destination" — the architecture-naming is the @19 clause-end, not a paragraph of meta-cognition
     - did NOT introduce the side-alley as new geography with a first-mention gloss — scene-A's east-lane + the @11 bone "three figures enter the side-alley" carry the geography; "side-alley off the east exit" is register-resident from scene-map row co-anchor
     - did NOT use vibes:7 token "dark-fantasy-world-above-apparatus-ceiling" literally; rendered as "the feed had no field for what the alley delivered" — gap-naming without ceiling-metaphor
   bone-walk:
     - @8 (courier enters lane-mouth) → L1 | "The courier came into the lane-mouth then"; exposition:4 em-dash-fold inline verbatim (28 words); apparatus-return-sentence at L1 close folds @9 (next bone) as the feed's response to entry — fusion-shape between @8-@9 not in scene-map but legitimate because @9's "insect-feed returns the courier" IS the feed's response to @8's entry (the two beats are entry+response, not separable in the apparatus-priority cadence; vibes:5 register)
     - @9 (insect-feed returns courier) → L1 fused with @8 | "the feed returned him from where it had been holding him, sorted him into the cut his prior sightings had opened, and let the count carry on" — apparatus-priority cadence; cf-d10 courier-recurrence registered; gait-signature recognition implicit in "the cut his prior sightings had opened" (the cut is the gait-signature slot); worm-canon SOFT-WATCH structurally-distinct operations preserved because @10 NI:3 adds the cognitive register (third-sighting + same-hold) as the second distinct operation
     - @10 (Taylor holds wall-line) → L2 | loc-state:4 co-anchor fold (wall-line + cool stone + hill-skirt + sightline gap + tallow-smoke); NI:3 fold (third sighting + feed-filed + same-hold-since-coverage) — physical-hold + cognitive-hold split across two sentences
     - @11 (three figures enter side-alley) → L3 | "Three figures came into the side-alley after him" + loc-state:5 fold (single-file because alley took one body at a time; rough original stone; uneven flooring); fused with @12
     - @12 (three figures close alley-mouth) → L3 fused with @11 | "At the mouth two of them turned and held the width of it, the alley-mouth sealed by their bodies in the way two bodies will seal an opening that admits no third — not robbery, the approach was wrong for robbery, the coordination was wrong" — loc-state:6 containment-fact fold + enforcement-vs-robbery categorization carried on-bone per exposition cull DROP
     - @13 (three figures pin courier) → L4 STANDALONE | "The third pinned him to the stone" — peak-shadow-bones discipline; physical pin
     - @14 (side-alley returns sound) → L5 STANDALONE leading sentence + paragraph continuation | "The side-alley returned the sound" peak-bone SVO standalone; sensory:2 + loc-state:5 acoustic-baseline mechanism expansion ("walls of the alley turned the noise of a body working against stone inward and then outward at the mouth, carrying past the threshold below the register I would have called human until the alley delivered it"); NI:4 gap fold ("the feed had no field for what the alley delivered")
     - @15 (courier raises spine) → L6 STANDALONE | "The courier raised his spine" — gap-instrument-triple middle beat; disambiguates @16
     - @16 (courier finds feet) → L7 STANDALONE | "He found his feet under him and stood" — recovery completion; sequential recovery preserved
     - @17 (Taylor files enforcement-record) → L8 sentence-1 | "I filed the incident into the form the feed kept for enforcement-incidents: movement-pattern, body-count, approach-geometry, duration, resolution" — state:3 jarvis-form fold implicit (the form is the jarvis-form); rendered as procedure not architecture
     - @18 (Taylor delivers enforcement report-entry) → L8 sentence-2 | "I delivered the entry to the outbound at the line where my own filings closed, the categorization clean, the form's fields full" — second cognitive operation (transmit); the "outbound" + "where my own filings closed" preserves the routing-to-architecture register without naming
     - @19 (Taylor drafts jarvis-report) → L8 sentence-3 | "I drafted the report on top of it for the courier above the form — the report had a destination, and the destination was the architecture that held someone else's exposure at a length of someone else's arm" — third cognitive operation (route-up); memory:1 verbatim fold; NI:5 routing-destination register; pl-2026-05-28-002 implicit-Sera-routing delivered without on-page naming (force-block discipline preserved)
     - @20 (three figures exit alley-mouth) → L9 | loc-state:7 fold (alley-mouth clearing; east-lane visible through gap behind them); "unhurried purpose of the gait carrying them east and out past the stone" — departure-walk cadence (vibes:9 bias-only)
     - @21 (Taylor adds courier to body-map) → L10 | "I added the courier to the body-map, the entry going in as recurring body with enforcement-incident attached, no name written into a ledger where his face would have one" — state:1 + state:9 body-map fold; NI:6 ledger-discipline; cf-d10 thread anchor preserved as standalone short paragraph
     - @22 (courier takes junction-corner) → L11 | "He took the junction-corner at the east turn, forty feet off from my held line, and the count let him go past it" — loc-state:8 fold (junction-corner + forty feet + held-line sightline); count-releases-him close parallels scene-A L7 "count holding to its side of the boundary" — scene-exit cadence echoes scene-A scene-close cadence for chapter-rhythm continuity
   drift-risk: low.
     - Fusion @8-@9 into L1 (not in scene-map fusion-eligible-runs) — defensible: @8 is the entry-SVO and @9 is the apparatus-response-SVO; the entry-and-response pair is structurally inseparable in the apparatus-priority cadence (vibes:5); worm-canon SOFT-WATCH structurally-distinct courier-operations preserved because the cognitive register fires at @10 NI:3 (third-sighting + same-hold) — three operations across three distinct surfaces (apparatus @8-@9 / cognition @10 / approach-geometry @11-@12) maintained. Flag forward to Phase 2 redundancy-cull / Phase 9 cold-read for ratification.
     - "the cut his prior sightings had opened" at L1 — concrete-spatial metaphor for the gait-signature slot; not stitcher-coined as compound, but borderline metaphor; chose over "the slot" / "the place his prior sightings had cut" (existing draft variant) for the verb-shape variance and the apparatus-priority register. If Phase 9 cold-read flags as too-pretty, fallback is "the slot his prior sightings had opened" or "the place" (existing draft form).
     - "the report had a destination, and the destination was the architecture that held someone else's exposure at a length of someone else's arm" — long sentence; memory:1 verbatim fold; chose to keep verbatim rather than break the displacement-cue. The cadence rises into the architecture-naming as the chapter's substance-irony surfaces; intentional length. If Phase 9 flags as ornate, the displacement-cue must be preserved per HARD parking-lot resolution.
     - No FAULT-VARIANCE-ABSTRACTION: concrete verbs throughout (came / held / turned / pinned / returned / raised / found / filed / delivered / drafted / added / took); no abstraction to "moved" / "did" / "acted".
     - No Q9 jargon coinages: no stitcher-coined hyphens; "enforcement-incidents" / "body-count" / "approach-geometry" / "body-map" / "junction-corner" all bone-faithful or scene-map register-resident.
     - No protected-pattern violations: gap-instrument triple @14-@15-@16 stands as three distinct beats; filing-triad @17-@19 stands as three distinct cognitive operations; courier 4-bone discipline preserved across @9 + @10 + @12 + @17-@19 (with the structural distinctness defense at @8-@9 fusion above); cf-d10 thread anchor at @21 stands as its own beat.
     - No on-page Sera-naming; force-block discipline at @17-@19 preserved (procedure not architecture-self-reflection); memory:1 displacement-cue at @19 satisfies pl-2026-05-28-002.
   flagged-seams (for Phase 2 / 5b / 9):
     - SEAM-1 @8-@9 L1 fusion not scene-map-licensed; structural defense above; flag for Phase 2 redundancy-cull ratification + Phase 9 cold-read worm-canon SOFT-WATCH courier-3-distinct-operations check
     - SEAM-2 "the cut his prior sightings had opened" L1 metaphor; flag for Phase 9 ornate-prose check; fallback variants noted
     - SEAM-3 L5 gap-instrument paragraph long-sentence ("The walls of the alley turned the noise of a body working against stone inward and then outward at the mouth, carrying past the threshold below the register I would have called human until the alley delivered it, and the feed had no field for what the alley delivered.") — combines sensory:2 mechanism + loc-state:5 acoustic-baseline + NI:4 gap-register in one sentence; preserves the sound-event causal chain (walls→inward→outward→threshold→delivery→feed-no-field); if Phase 9 flags as overlong, split point is after "the alley delivered it" → "The feed had no field for what the alley delivered" as standalone sentence
     - SEAM-4 L8 filing-triad three sentences in single paragraph; structurally distinct cognitive operations per cold-read failure (i) prevention; if Phase 9 flags as too-dense, split point is after sentence-2 → @19 as standalone short paragraph parallel to @21 cf-d10 anchor
     - SEAM-5 L11 close echoes scene-A L7 close ("count let him go" / "count holding to its side of the boundary") — intentional chapter-rhythm parallel; if Phase 2 redundancy-cull flags as repetition, the L11 form ("the count let him go past it") is more compressed than the scene-A close so the echo reads as variation not duplication
