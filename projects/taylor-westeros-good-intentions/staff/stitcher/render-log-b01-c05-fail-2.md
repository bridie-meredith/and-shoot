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

fork-003 scene-C bones=@23-@35  scene-window-render
   bones-consumed: @23, @24, @25, @26, @27, @28, @29, @30, @31, @32, @33, @34, @35
   back-look: scene-B close at L11 ("the count let him go past it") — chapter's first scene-exit close on a release-verb at the junction-corner; scene-C opens on a discontinuous time-skip to the lodging room-floor in the evening. No re-entry into Rushwick geography; the scene-shift is signaled by the loc-state:9 indoor/evening register (lamp absence, boards-underfoot-dry, still-air, no-through-transit) and the deferred temporal marker ("By evening I had the room-floor to myself"). Anti-repetition discipline: scene-B's closing apparatus-sentence ("the count let him go past it") is not echoed at scene-C open; "the count" / "the feed" sentence-openers held back from L1 — L1 leads with a temporal marker, L2 leads with first-person action ("I ran"), L4 leads with subject-noun ("The rushwick-feed did not settle"), L5 leads with body-act ("My head tilted").
   forward-look: NO scene-D. @35 is the chapter's terminal bone; chapter closes on the courier-walk foreclosure-confirmation. NOTHING APPENDED after L12 — no wrap-up sentence, no editorial reflection, no thematic close. Per scene-map protected-pattern terminal-bone @35 and the dark-fantasy SOFT-WATCH carry, the chapter's terminal cadence is the foreclosure-as-second-attempt holding the same way; the door does not open when turned, twice; the chapter stops with the second hold.
   exposition-folded: NONE (no scene-C anchors carry exposition entries per Phase 0.6; scene-orient at @23 REFUSED at R2 per fire-rule clause-b — loc-state:9 carries the shift; NI verified-silent through @24; scene-shift conveyed by paragraph break only)
   facets-folded:
     - loc-state:9 @23 → L1 co-anchor fold (taylor-lodging-room indoor evening; still-air; lamp unlit because the window's last light was the working light; boards underfoot dry where the lane had been damp at the wall — explicit contrast to scene-B's wall-line damp paving establishes the indoor shift without requiring a scene-orient gloss)
     - narrator-interest:7 @28 → L4 same-anchor fuse — apparatus-residue-contrast Hook-vs-Rushwick register; rendered as "the feed routing the provisioner-train through the same architecture and bringing the architecture back with the train" + the second-length-pass verification ("to see if it was the read and not the feed; the color persisted") — Hook-vs-Rushwick contrast carried as DIFFERENCE per scene-map protected-pattern, not as declaration
     - narrator-interest:8 @29 → L6 same-anchor fuse (recognition-cessation peak) — INSTRUMENT-COMPLICITY carrier per pl-2026-05-28-002; rendered as "the feed was an apparatus I had been keeping neutral, an instrument with a use, and the instrument was recognizing the route it carried as the route — not the lane, not the courier, but the architecture the routing went through, and the architecture was the architecture I had not asked the feed to mark. The discipline I had been keeping was the discipline of a neutral read; the discipline was what the apparatus was no longer willing to support." — INSTRUMENT-COMPLICITY language preserved (the feed recognizing the content it routes through the same architecture); NO Sera/Otto/Jarvis surface naming; the architecture-naming is the routing-shape, not the protected party
     - narrator-interest:9 @31 → L8 same-anchor fuse — body-record filing register (cf-d10 face-content); rendered via memory:2 verbatim fold below; NI register on body-record-cognition not separately surfaced beyond the memory-verbatim's filing-act
     - narrator-interest:10 @35 → L12 same-anchor fuse (foreclosure-tail close) — "the courier-walk held the rushwick-pass" as the read that does not return; terminal bone carries NI without paragraph-internal cognitive register expansion (the SVO IS the read-that-does-not-return)
     - memory:2 @31 → L8 verbatim quotation fold (Earth-Bet displacement / override-architecture-residue body-record cognition); surface preserves "the entry going in the way bodies go into the record when the record is the route they will be moved along later" — displacement-discipline clean, no Khepri / Gold Morning / Endbringer / Skitter naming; the recursion of "the way bodies go into the record when the record is" is the licit cue; carve-out clause applied — resonance lands at @31 not at @29 peak (peak is the action-in-itself per rubric)
     - feeling:1 @29 → L5 co-anchor fold ("My head tilts toward the held color" — facet present-tense rendered as past-tense first-person "My head tilted toward the held color"); body-of-recognition; distinct from NI's cognitive register at @29 (head-tilt is the §Look signature card-match 5/5; the recognition-as-body precedes the recognition-as-cognition by one sentence; the body acts before the cognition has a word for it — rendered explicitly as "The stopping was the body's, before I had a word for what the body was doing")
     - state-updates env:5 @23 (location the-rushwick → taylor-lodging) → L1 implicit in lodging-room naming + indoor-evening register
     - state-updates env:6 @23 (time_of_day morning → evening) → L1 explicit ("By evening I had the room-floor to myself")
     - state-updates env:7 @31 (oc-courier-body-map.state initiated → filed) → L8 implicit in "I held the entry's face there a length and then I closed the file"
     - state-updates taylor:2 @28 (discipline_state.neutral-instrumental-read: available → apparatus-failing-color-persists-across-retry) → L4 implicit in the second-length-pass verification ("I ran the pass a second length to see if it was the read and not the feed; the color persisted")
     - state-updates taylor:3 @29 (political_register_prot_axis 1.0 → 2.5) → L5+L6 implicit in the recognition-cessation peak; the +1.5 axis-move carried by the body-act of stopping in response to apparatus-output (not by interior naming)
     - state-updates taylor:4 @29 (discipline_state: apparatus-failing → foreclosed-for-rushwick-content) → L6 implicit in "the discipline was what the apparatus was no longer willing to support" — foreclosure-as-discipline-meeting-apparatus-refusal register
     - state-updates taylor:5 @31 (knowledge.courier-body-record absent → filed-as-cf-d10-thread-anchor) → L8 explicit in "I filed the courier body-record" + the held-face-then-closed-file beat
     - vibes — bias-only: vibes:13 @28 (apparatus-level recognition correlate) → cadence at L4 ("the feed routing the provisioner-train through the same architecture and bringing the architecture back with the train"); vibes:14 @28 (residue-not-spectacle on rushwick-content-color-held) → register at L4 ("The rushwick-feed did not settle. The color that had been on the junction at the morning hour was on the junction at the evening hour"); vibes:15+16 @29 (political-register-color-present + contempt-without-refusal) → bias for L6 register without surface-tokens — "contempt-without-refusal" NOT rendered as surface phrase per HARD constraint (Taylor does NOT name contempt at d05); the read-failure surfaces as "the apparatus was no longer willing to support" not as articulated contempt; vibes:17 @29 (political-register-threshold-crossed) → bias-cadence for the recognition's permanent-color implication (carried structurally by foreclosure-quartet not by surface-naming); vibes:18+19+20 @35 (foreclosure-confirmed-twice-no-reopen + second-attempt-as-the-foreclosure-proof + ward-as-recognition-correlate-not-neutral-feed-node) → cadence for the terminal foreclosure-quartet; "ward-as-recognition-correlate" NOT rendered as compound (Q9); the structural compound is delivered as the quartet itself — two attempts, two distinct holds (provisioner-train @33, courier-walk @35)
   variance-moves:
     - L1 leads with temporal marker ("By evening") not with subject-noun or apparatus-verb; this defers from scene-B's closing apparatus-cadence ("the count let him go past it") and from scene-A's chapter-open subject-noun cadence ("Stone met") — the temporal lead earns the scene-shift discontinuity
     - L1 establishes the indoor-evening contrast via concrete sensory facts (lamp unlit; window's last light; air held still; boards dry where lane was damp) rather than scene-orient meta-naming — the loc-state:9 fold is the orientation, no scene-callout marker needed
     - L1 closes on "set the day on the floor in front of me the way a person lays out coin to count it" — coin-laying metaphor for the evening-replay shape; ties the contemplative cadence to a concrete domestic action; voice-exemplar cadence-prime register (the "a person lays out coin" abstraction has the contemplative-first-person reach the exemplar models)
     - @24 + @25 fused into L2 (scene-map fusion-eligible-run Hook baseline pair): "I ran the Hook-feed first…the feed delivered the count and the body-flags and the gait-records and closed itself out clean, every entry resolved against its return" — the Hook-resolves verb-shape "closed itself out clean, every entry resolved against its return" is the transitive completion clause that addresses flag-002 @25 intransitive borderline (the bone's "the Hook-feed resolves" reads with explicit object-of-resolution language); single paragraph for the Hook baseline establishes the baseline-against-which-Rushwick-will-fail per scene-map peak-shadow @25
     - @26 + @27 fused into L3 (scene-map fusion-eligible-run Rushwick first-pass pair): "Then I ran the rushwick-feed. The morning's coverage of the junction came back the way the Hook had come back, the provisioner-train re-crossing the junction at the hour it had crossed, the count carrying the train east the way the count had carried it east" — first-pass parallels the Hook structurally (the parallel IS the setup for the @28 break); @27 provisioner-train re-crossing carried as the replay-content with the same crossing-cadence the morning had; the paragraph extends through the courier-window and report-entry to establish that the Rushwick replay attempts to carry forward like the Hook does
     - L4 (@28) STANDS ALONE as the apparatus-correlate paragraph per scene-map peak-shadow @28: "The rushwick-feed did not settle" leading sentence + "The color that had been on the junction at the morning hour was on the junction at the evening hour" (color-persistence-across-time) + "the feed routing the provisioner-train through the same architecture and bringing the architecture back with the train" (NI:7 apparatus-residue-contrast Hook-vs-Rushwick) + "I ran the pass a second length to see if it was the read and not the feed; the color persisted" (state:2 verification beat) — apparatus-holds-color-persists is the apparatus-level event that @29 will respond to
     - L5 (@29 first half) STANDS ALONE: "My head tilted toward the held color. I stopped the rushwick-pass." — feeling:1 body-of-recognition + the act of stopping; two short sentences in one paragraph (the body acts; the body stops); recognition-cessation peak carried by the body-act
     - L6 (@29 second half / cognitive register) STANDS ALONE: "The stopping was the body's, before I had a word for what the body was doing. The hand I had laid flat on the boards came up off the boards. The feed was an apparatus I had been keeping neutral, an instrument with a use, and the instrument was recognizing the route it carried as the route — not the lane, not the courier, but the architecture the routing went through, and the architecture was the architecture I had not asked the feed to mark. The discipline I had been keeping was the discipline of a neutral read; the discipline was what the apparatus was no longer willing to support." — NI:8 INSTRUMENT-COMPLICITY register carried as the apparatus-meeting-its-own-routing-architecture recognition; the architecture-naming is the routing-shape ("the architecture the routing went through" / "the architecture I had not asked the feed to mark"); the routing-destination from scene-B @19 ("the architecture that held someone else's exposure at a length of someone else's arm") is the architecture meeting itself here without on-page naming of Sera/Otto/Jarvis (force-block discipline preserved); the discipline-as-apparatus-refusal close is the cognitive register of the recognition that the body-act at L5 already delivered
     - L7 (@30) short paragraph: "I closed the evening review. The window's light had thinned to the line above the sill, and I closed the day's coverage out into the form it kept when the day was done, the entries delivered, the count resolved." — closes-evening-review beat; the window's-light detail carries the temporal close (loc-state:9 light fading) without re-establishing the evening-time
     - L8 (@31) standalone paragraph: "I filed the courier body-record. The face the alley had returned went into the body-map under the recurring-body anchor I had opened that morning, the enforcement-incident attached, the entry going in the way bodies go into the record when the record is the route they will be moved along later, and I held the entry's face there a length and then I closed the file." — memory:2 verbatim fold (Earth-Bet displacement); cf-d10 face-content callback ("The face the alley had returned"); state:5 body-record filing event; state:7 oc-courier-body-map.state initiated → filed implicit in held-face-then-closed-file; carve-out clause applied (resonance after peak, not on peak)
     - @32 STANDALONE single-sentence paragraph: "I ran the rushwick flat-read." — bare-form; the foreclosure-quartet first attempt; no aspect, no cadence-decoration — the bare-form IS the deliberate-attempt register that @33's hold will defeat
     - L10 (@33) standalone paragraph: "The provisioner-train held the rushwick-pass. The train re-crossed the junction at the morning hour and the feed brought the crossing back and the architecture came back with it; the pass would not run as the Hook had run, would not close out clean against its return, would not deliver the junction as a count and only a count. The door I had turned did not open at the turn." — foreclosure-quartet first hold; provisioner-train as physical anchor (scene-map protected-pattern); the three would-not negations chain the foreclosure-shape; the door-does-not-open-at-the-turn metaphor seals the first attempt; physical-anchor hold per scene-map foreclosure-quartet
     - @34 standalone single-sentence paragraph: "I ran the rushwick flat-read again, slower this time, the feed taken at a length deliberate enough to let the neutral read seat if it would seat." — dup-001 distinguishing prose: same SVO as @32 ("runs the rushwick flat-read") but distinct cadence (longer; conditional "if it would seat"; deliberate-aspect "slower this time"; the second-attempt-as-foreclosure-proof per vibes:19 register bias); the second attempt's distinctness is in the aspect of patience, not in a different verb — preserves the bone-faithful SVO repetition while delivering distinct prose
     - @35 TERMINAL single-sentence paragraph: "The courier-walk held the rushwick-pass." — terminal bone; physical-anchor hold (courier-walk per scene-map); NOTHING APPENDED after; chapter closes on the foreclosure-confirmation; the parallel construction with @33 ("The provisioner-train held the rushwick-pass" / "The courier-walk held the rushwick-pass") carries the foreclosure-quartet structural compound (two attempts, two distinct holds) without naming "foreclosure" on-page; the terminal-bone SVO IS the chapter-close per dark-fantasy SOFT-WATCH carry
   refusals:
     - did NOT render any scene-orient at @23 (R2 fire-rule clause-b refused; loc-state:9 carries; no scene-callout marker per HARD URI-SUBSTANCE-OVERHAUL)
     - did NOT name Sera / Otto / Jarvis at @29 — the INSTRUMENT-COMPLICITY register surfaces as "the architecture the routing went through" / "the architecture I had not asked the feed to mark"; the routing-destination from scene-B @19 is the architecture that is meeting itself here, without on-page naming (HARD force-block per pl-2026-05-28-002 resolution; the Sera-link was anchored in scene-B's @19 verbatim memory:1 fold, and the @29 recognition meets it without articulating it)
     - did NOT render "contempt-without-refusal" surface token at @29 — vibes:16 is bias-only; Taylor does NOT name contempt at d05; the read-failure surfaces as "the apparatus was no longer willing to support" (apparatus-refusal register), not as articulated contempt (HARD per brief)
     - did NOT render "foreclosure-confirmed-twice-no-reopen" / "ward-as-recognition-correlate" / "second-attempt-as-the-foreclosure-proof" surface compounds at @35 — vibes:18/19/20 are bias-only; the structural compound is delivered as the quartet itself (two attempts @32+@34, two holds @33+@35), not as on-page naming (Q9 anti-jargon fence)
     - did NOT append any wrap-up sentence or thematic close after @35 — terminal bone discipline (HARD per scene-map protected-pattern terminal-bone @35); the chapter stops on the courier-walk hold
     - did NOT collapse the foreclosure-quartet @32-@35 into a single attempt-pair or merged paragraph — four standalone paragraphs (two attempts @32+@34, two holds @33+@35); the door-does-not-open-when-turned-TWICE structure is the scene-map protected-pattern (HARD)
     - did NOT reorder or merge @28 with @29 — @28 standalone L4 paragraph (apparatus-holds-color-persists) precedes @29 standalone L5+L6 paragraphs (body-stops + cognitive-register); world-physics-first causal direction preserved (HARD; cold-read failure (iv) prevention)
     - did NOT render NI saturation: 4/13 entries (@28, @29, @31, @35) advisory respected — the foreclosure-quartet standalone bones (@32, @33, @34, @35) breathe with no NI surface (NI:10 @35 is the terminal SVO itself, not an additional cognitive paragraph); the @30 close-evening-review paragraph has no NI fold (despite L7 sitting between two NI-fold paragraphs); density let stand at the foreclosure-quartet
     - did NOT repeat scene-B's "the count let him go past it" closing cadence at scene-C open or close — scene-B's apparatus-release verb-shape held back; scene-C opens on temporal-marker, closes on apparatus-hold (the inversion: scene-B closed on release, scene-C closes on hold; the chapter-rhythm is release→hold→hold)
     - did NOT use "the count" / "the feed" as sentence-openers at L1 — L1 opens with "By evening I had the room-floor to myself" (first-person + temporal marker), preserving scene-shift discontinuity
   bone-walk:
     - @23 (Taylor takes the room-floor) → L1 | first-person temporal-shift entry ("By evening I had the room-floor to myself"); loc-state:9 co-anchor fold (lamp-unlit-because-window's-last-light + still-air + boards-dry-where-lane-was-damp-at-the-wall); state-env:5+6 location+time shift implicit; chapter-rhythm pivot from morning-Rushwick to evening-lodging; coin-laying metaphor closes the paragraph as the evening-replay shape
     - @24 (Taylor runs the Hook-feed) → L2 fused with @25 | "I ran the Hook-feed first" — first apparatus-action on the floor; baseline establishment per scene-map fusion-eligible-run
     - @25 (the Hook-feed resolves) → L2 fused with @24 | "and the feed delivered the count and the body-flags and the gait-records and closed itself out clean, every entry resolved against its return, the lane settling into the form it kept when nothing about it had asked to be remembered" — peak-shadow Hook baseline; flag-002 intransitive-borderline addressed with transitive completion clause ("closed itself out clean, every entry resolved against its return") that gives the resolution explicit objects-of-resolution; baseline-against-which-Rushwick-will-fail established
     - @26 (Taylor runs the rushwick-feed) → L3 fused with @27 | "Then I ran the rushwick-feed" — second apparatus-action; scene-map fusion-eligible-run Rushwick first-pass pair
     - @27 (provisioner-train re-crosses the junction) → L3 fused with @26 | "The morning's coverage of the junction came back the way the Hook had come back, the provisioner-train re-crossing the junction at the hour it had crossed, the count carrying the train east the way the count had carried it east" — peak-shadow replay-content; the parallels-Hook structural cadence is the setup for the @28 break ("came back the way the Hook had come back"); paragraph extends through courier-window + report-entry to register the first-pass attempting to carry forward like the Hook
     - @28 (rushwick-feed holds the color) → L4 STANDALONE | "The rushwick-feed did not settle" leading sentence + color-persistence-across-time + NI:7 apparatus-residue-contrast ("the feed routing the provisioner-train through the same architecture and bringing the architecture back with the train") + state:2 second-length-pass verification ("I ran the pass a second length to see if it was the read and not the feed; the color persisted") — apparatus-correlate paragraph per scene-map peak-shadow @28; apparatus-holds → protagonist-responds causal direction set up for @29
     - @29 (Taylor stops the rushwick-pass) → L5 + L6 (two paragraphs — body-act, then cognitive register) | L5 "My head tilted toward the held color. I stopped the rushwick-pass." (feeling:1 head-tilt + the act of stopping); L6 "The stopping was the body's, before I had a word for what the body was doing…the discipline was what the apparatus was no longer willing to support." (NI:8 INSTRUMENT-COMPLICITY register; the apparatus-meeting-its-own-routing-architecture recognition without on-page Sera-naming; state:3 +1.5 political_register-prot axis carried by the body-act of stopping; state:4 foreclosure carried by the discipline-as-apparatus-refusal close); RECOGNITION-CESSATION peak — the +1.5 axis-move is the body acting before the cognition has the word, then the cognition catching up to name the apparatus-refusal; chapter's central call delivered
     - @30 (Taylor closes the evening review) → L7 | "I closed the evening review. The window's light had thinned to the line above the sill, and I closed the day's coverage out into the form it kept when the day was done, the entries delivered, the count resolved." — closes-evening-review beat; window-light fading carries temporal-close; no NI fold (density advisory)
     - @31 (Taylor files the courier body-record) → L8 | "I filed the courier body-record" leading sentence + cf-d10 face-callback ("The face the alley had returned went into the body-map under the recurring-body anchor I had opened that morning") + state:5 body-record filing + memory:2 verbatim fold (Earth-Bet displacement; "the entry going in the way bodies go into the record when the record is the route they will be moved along later") + state:7 held-face-then-closed-file (oc-courier-body-map.state initiated → filed); carve-out clause: resonance lands here not at @29 peak (peak is the action-in-itself); the @29 recognition's monument-content lands at body-record filing as the parallel-cognition rubric expects
     - @32 (Taylor runs the rushwick flat-read) → L9 STANDALONE single-sentence | "I ran the rushwick flat-read." — bare-form; first attempt of foreclosure-quartet; no aspect, no cadence-decoration; dup-001 SVO repetition begins (distinguished from @34 by the bare-form vs longer aspect-marked form)
     - @33 (provisioner-train holds the rushwick-pass) → L10 STANDALONE | "The provisioner-train held the rushwick-pass" leading sentence + the foreclosure-shape ("would not run as the Hook had run, would not close out clean against its return, would not deliver the junction as a count and only a count") + the door-does-not-open-at-the-turn metaphor close ("The door I had turned did not open at the turn") — foreclosure-quartet first hold; provisioner-train as physical-anchor (scene-map protected-pattern); apparatus-hold rendered as three-would-not-negations chain
     - @34 (Taylor runs the rushwick flat-read) → L11 STANDALONE single-sentence | "I ran the rushwick flat-read again, slower this time, the feed taken at a length deliberate enough to let the neutral read seat if it would seat." — dup-001 distinguishing prose: same bone SVO as @32 ("runs the rushwick flat-read") rendered with distinct cadence (longer sentence; "again, slower this time" aspect-marker; "the feed taken at a length deliberate enough"; conditional "if it would seat") — second-attempt-as-foreclosure-proof per vibes:19 bias; the patience-aspect is the differentiation
     - @35 (courier-walk holds the rushwick-pass) → L12 TERMINAL STANDALONE single-sentence | "The courier-walk held the rushwick-pass." — chapter terminal bone; courier-walk as physical-anchor (scene-map protected-pattern; second of two distinct holds); parallel construction with @33 ("The provisioner-train held the rushwick-pass" / "The courier-walk held the rushwick-pass") delivers foreclosure-quartet structural compound; NOTHING APPENDED after; NI:10 foreclosure-tail-close carried by the SVO itself (the read that does not return); dark-fantasy SOFT-WATCH terminal-cadence honored
   drift-risk: low.
     - @29 split across two paragraphs (L5 body-act + L6 cognitive register): body-act and cognitive-register are two faces of the same recognition-cessation event; the split is the per-bone discipline ("body acts before cognition has the word; cognition catches up to name the apparatus-refusal") — not a fusion (single bone @29 across two paragraphs) and not a CUT/RESHOW; the two paragraphs are the two stages of the @29 peak's delivery; @29 is the chapter's axis-mover and cannot be RENDERED-ILLEGIBLE — the body-act AND the cognitive register are both fully on-page. Flag forward to Phase 2 / Phase 9: if the cold-read flags as over-cognized, the L6 paragraph can compress (the apparatus-as-instrument-recognizing-the-route register is the load-bearing content; the discipline-as-apparatus-refusal close is the foreclosure-anchor; both must remain).
     - L6 paragraph length: long; chose to keep the NI:8 INSTRUMENT-COMPLICITY register intact rather than break the apparatus-meeting-architecture sentence ("the instrument was recognizing the route it carried as the route — not the lane, not the courier, but the architecture the routing went through, and the architecture was the architecture I had not asked the feed to mark"); the architecture-without-Sera-naming is the chapter's central call, and the sentence's reach IS the recognition-shape. If Phase 9 flags as overlong, split point is after "the architecture I had not asked the feed to mark" → "The discipline I had been keeping was the discipline of a neutral read; the discipline was what the apparatus was no longer willing to support." as standalone sentence.
     - @24-@25 fusion + @26-@27 fusion in L2 + L3 — scene-map fusion-eligible-runs; both fusions licensed; Hook baseline establishment + Rushwick first-pass parallel are the two structural setups for the @28 break; the parallels-Hook structural cadence at L3 ("came back the way the Hook had come back") is what makes the L4 break read as DIFFERENCE not as declaration (per scene-map protected-pattern Hook-vs-Rushwick contrast).
     - dup-001 @32 + @34 same-SVO bone repetition: rendered as bare-form @32 + aspect-marked @34; distinguishable per FLAG dup-001 advisory; the duplication IS load-bearing for the foreclosure pattern (two attempts, two holds); if Phase 9 flags as too-similar, the @34 form already carries the deliberate-aspect differentiator ("again, slower this time, the feed taken at a length deliberate enough to let the neutral read seat if it would seat") — further differentiation would risk obscuring the bone-faithfulness.
     - @33 + @35 parallel hold-construction ("The provisioner-train held the rushwick-pass" / "The courier-walk held the rushwick-pass"): structural compound delivers the foreclosure-quartet two-distinct-physical-holds; @33 expands with foreclosure-shape + door-does-not-open metaphor (apparatus-hold mechanism); @35 stays as bare SVO (terminal-bone discipline; nothing appended). The parallel-construction IS the foreclosure delivery; if Phase 9 flags as repetition, the structural parallel is HARD per scene-map protected-pattern.
     - No FAULT-VARIANCE-ABSTRACTION: concrete verbs throughout (tilted / stopped / closed / filed / ran / held / opened / turned / re-crossed / brought); no abstraction to "moved" / "did" / "felt".
     - No Q9 jargon coinages: no stitcher-coined hyphens; "rushwick-feed" / "rushwick-pass" / "Hook-feed" / "body-record" / "body-map" / "rushwick flat-read" / "courier-walk" all bone-faithful or scene-map register-resident.
     - No on-page Sera/Otto/Jarvis naming at @29; force-block discipline preserved (INSTRUMENT-COMPLICITY surfaces as routing-architecture meeting itself); the routing-destination from scene-B @19 is the architecture meeting itself here without articulation (pl-2026-05-28-002 resolved at facet layer; here at @29 Taylor's interior posture acknowledges without naming).
     - No on-page "contempt" naming; vibes:16 surface-token forbidden; the read-failure surfaces as apparatus-refusal not as articulated contempt.
     - No appended wrap-up sentence after @35; terminal-bone HARD constraint preserved.
   flagged-seams (for Phase 2 / 5b / 9):
     - SEAM-6 L6 long sentence ("the instrument was recognizing the route it carried as the route — not the lane, not the courier, but the architecture the routing went through, and the architecture was the architecture I had not asked the feed to mark") — chapter's central INSTRUMENT-COMPLICITY register; intentional reach; if Phase 9 flags as ornate, the architecture-without-Sera-naming is HARD and cannot be cut; split-point after "the architecture I had not asked the feed to mark" is available
     - SEAM-7 @29 split across L5 + L6 (body-act + cognitive register) — defensible per body-acts-before-cognition register; if Phase 9 cold-read reads as over-cognized, L6 can compress but cannot delete (the apparatus-as-instrument-recognizing-the-route register is the +1.5 axis-mover's articulation)
     - SEAM-8 dup-001 @32 + @34 bare-form vs aspect-marked-form — load-bearing for foreclosure pattern; if Phase 9 flags as redundant, the duplication is HARD per FLAG dup-001 advisory and scene-map fusion-eligible-runs explicitly excludes @32-@34 (no fusion eligible)
     - SEAM-9 L8 memory:2 verbatim fold combined with state:5 body-record filing + cf-d10 face-callback — single paragraph carrying three facet loads; cohesive because all three are the body-record filing event; if Phase 9 flags as too-dense, no split point is good — the memory:2 verbatim is locked
     - SEAM-10 L7 close-evening-review beat between two NI-fold paragraphs (L6 + L8) — no NI fold at L7 by design; if Phase 5b NI-author requests NI surface here, L7 has the window-light-thinning detail available to extend with a register-fold, but the density advisory recommended letting the foreclosure-quartet breathe
     - SEAM-11 L1 "set the day on the floor in front of me the way a person lays out coin to count it" — coin-laying metaphor; not stitcher-coined as compound, but borderline reach; chose for evening-replay-shape register + voice-exemplar cadence-prime alignment; if Phase 9 flags as too-pretty, fallback is "set the day on the floor in front of me" without the metaphor extension

## Phase 7 — editorial reflection

mode: strict (cut-aggressiveness)
persona: neutral (no Phase-7-bias overrides)
voice: 1st-person past, contractions OFF
sweep-scope: full draft sentence-by-sentence (mandatory; "0 moves" legitimate only with full sweep present)
draft-input: active-project/draft/b01-c05.phase-6.draft.md (1416 words; 3 scenes; 30 paragraphs)
draft-output: active-project/draft/b01-c05.phase-7.draft.md
total-sentences: 54
total-q-lines: 54
moves-applied: cuts=0, cut-clauses=0, cut-asinines=0, cut-hollows=0, reshows=0, rewords=0, simplify-puncts=0, cut-bones=0
keep-all: Y
verdict: 0 moves — full sweep performed; every sentence load-bearing per bones-walk + scene-window self-audit; no facet register-token leaks; no contractions; no asinine patterns; no anti-jargon coinages; punctuation choices (em-dashes, semicolons) all functional rather than taste-flex per Q6

q-line format: L<n>.<s> [scene]: Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q8 Q9 → verdict
  where Q1=load-bearing, Q2=image-concrete, Q3=cardinal-delivery, Q4=sensory-coverage, Q5=hollow-prose-MATCH, Q6=punct-fancy-MATCH, Q7=pronoun-ambiguity-MATCH, Q8=asinine-pattern-MATCH, Q9=anti-jargon-MATCH
  load-bearing/concrete/cardinal/sensory: y=present, n=absent, n/a=not-at-applicable-beat
  hollow/punct/pronoun/asinine/jargon: n=clean (no match), y=match (triggers move)
  exposition-derived sentences (P2, P8 em-dash folds): Q1/Q5/Q8 pre-cleared per audience-modeling/R2/audit upstream → marked "pre" (treat borderline as KEEP)

### Scene-A (paragraphs P1–P7; bones @1–@7)

L1.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=y(loc-state-sensory-pre-anchor) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: cold-damp/light/shade triple establishes loc-state-pre-anchor; no fancy punct; "stopping at the north face of the junction in shade" is concrete spatial fix not gestural

L2.1 [Scene-A]: Q1=pre Q2=y Q3=n/a Q4=n/a Q5=pre Q6=n Q7=n Q8=pre Q9=n → KEEP
  note: exposition first-mention em-dash-fold for "the Rushwick"; Q1/Q5/Q8 pre-cleared (audience-modeled); em-dash-fold here is the schema-licensed first-mention render-as directive, not a taste flex (Q6=n); 78 words defensible per brief

L3.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: four-word topic sentence; opens the apparatus-bedding-in paragraph

L3.2 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(semicolon-fragment-to-clause-functional) Q7=n Q8=n Q9=n → KEEP
  note: "insect-bodies on lintels, in wall-seams, under cart-shadow" is concrete spatial enumeration; semicolon required (fragment+clause join would be comma splice with comma); "instrument bedding in on new ground" is graph-resident apparatus register, not a Q9 coinage (apparatus/instrument both in lens-vocabulary c01-c04)

L4.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=y(sensory:cart-wheels-grinding) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: provisioner-train SVO arrival; cart-wheels grinding on uneven stone is sensory:auditory-rendered; concrete throughout

L4.2 [Scene-A]: Q1=y Q2=n/a(abstract-but-cognitive-state) Q3=y(stakes-baseline-register) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: three-word axiom "The categorization held." is the chapter's opening +0 cognitive register baseline; load-bearing as the stakes-axiom against which the rushwick-flat-read will fail at scene-C

L4.3 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(colon-introduces-enumeration) Q7=n Q8=n Q9=n → KEEP
  note: colon introduces an enumeration of the read-as-since-coverage; "forward-lean...unhurried-hurry...no affect required" are concrete behavioral categories not abstractions; colon is functional, not flex

L5.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=y(loc-state-sensory) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: train-departure SVO with spatial-fall-off-into-morning-light; concrete

L5.2 [Scene-A]: Q1=y Q2=n/a(cognitive-categorization) Q3=n/a Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: "what read in their gait was not Hook foot-traffic" is the cross-episode register-contrast (substrate-difference) load-bearing for the categorization-transfer chapter-arc

L5.3 [Scene-A]: Q1=y Q2=n/a(cognitive) Q3=n/a Q4=n/a Q5=n Q6=n(semicolon-paired-clauses-rhythmic) Q7=n Q8=n Q9=n → KEEP
  note: semicolon binds two paired clauses (substrate-different / layer-above-unnamed) — rhythmic-parallel function, not taste-flex; "the layer above it stayed unnamed" is the soft-watch register Taylor doesn't fully articulate

L6.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(em-dash-surface-to-read) Q7=n Q8=n Q9=n → KEEP
  note: message-runner gait-read; em-dash separates surface (gait) from the read (accountable-to-someone-above); functional definitional break

L7.1 [Scene-A]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: apparatus-release SVO with spatial-line-where-lane-mouth-widens; "the count holding to its side of the boundary" is the apparatus-cognition load-bearing for the contrast with the rushwick-feed-not-settling at scene-C

### Scene-B (paragraphs P8–P18; bones @8–@22)

L8.1 [Scene-B]: Q1=pre Q2=y Q3=n/a Q4=n Q5=pre Q6=n Q7=n Q8=pre Q9=n → KEEP
  note: exposition em-dash-fold for "the courier" first-mention (three-mornings-running gloss); Q1/Q5/Q8 pre-cleared; em-dash here is schema-licensed exposition fold not flex; "sorted him into the cut his prior sightings had opened" is borderline-metaphor but reads as feed-mechanism (recurring-body-anchor's pre-existing slot in the body-map) — defensible per scene-window self-audit SEAM-1 KEEP

L9.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=y(loc-state-tactile:cool-stone-shade-damp) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: wall-line hold with concrete tactile rendering; "since the count came up" anchors the protected-tradecraft register

L9.2 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=y(sensory:olfactory-tallow-smoke) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: tallow-smoke drift from stitch-house-ward — concrete olfactory landmark naming the ward via graph-resident vocabulary (stitch-house-ward not Q9 per brief)

L9.3 [Scene-B]: Q1=y Q2=n/a(cognitive-triadic) Q3=n/a Q4=n/a Q5=n Q6=n(two-semicolons-triadic-rhythm-functional) Q7=n Q8=n Q9=n → KEEP
  note: triadic cognition (third-sighting / feed-had-him-filed / hold-was-hold-used) binds three simultaneous register-loads as one observation; periods would impose sequential cognition; semicolon-chain is rhythmic-structural not flex

L10.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=y(loc-state-sensory:rough-stone-uneven-floor) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: three-figures arrival with alley-geometry rendered; concrete

L10.2 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(em-dash-image-to-categorization-refusal) Q7=n Q8=n Q9=n → KEEP
  note: alley-mouth-sealed geometry + the categorization-refusal triadic ("not robbery, the approach was wrong, the coordination was wrong"); em-dash separates the image from the refusal-of-the-obvious-read — functional break, not flex

L11.1 [Scene-B]: Q1=y Q2=y Q3=y(stakes-pivot-event) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: six-word standalone paragraph; the pinning act is the scene's pivot event; concrete

L12.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=y(sensory:auditory-spike) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: five-word topic sentence; alley-acoustics introduces the auditory beat

L12.2 [Scene-B]: Q1=y Q2=y Q3=y(apparatus-gap-cardinal) Q4=y(sensory) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: long single-sentence carries the noise-physics + the feed-no-field beat; SEAM-3 split-point was identified but the conjunctive-and join is functional (noise-being-carried-out causally produces feed-has-no-field) — splitting would break the causal continuity; rhythm load-bearing per scene-window self-audit; the comma+and join is natural English, not "fancy punctuation" per Q6

L13.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: courier-raises-spine SVO; standalone paragraph; image-concrete

L14.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: courier-stands SVO; standalone paragraph; image-concrete

L15.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(colon-introduces-form-fields) Q7=n Q8=n Q9=n → KEEP
  note: filing the incident into enforcement-incident form; colon introduces the form-field enumeration (movement-pattern, body-count, etc.) — functional schema-listing not flex; "enforcement-incidents" is graph-resident substance-vocabulary not Q9 coinage

L15.2 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: delivery-to-outbound at filing-close-line; concrete categorization beat

L15.3 [Scene-B]: Q1=y Q2=y Q3=y(report-destination-cardinal) Q4=n Q5=n Q6=n(em-dash-act-to-destination) Q7=n Q8=n Q9=n → KEEP
  note: the report-going-to-Sera-architecture beat without on-page Sera-naming; "the architecture that held someone else's exposure at a length of someone else's arm" carries the routing-destination register at the cardinal stakes beat; em-dash separates act from destination — definitional functional break

L16.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=y(loc-state:opening-clears-east-lane-visible) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: three-figures-exit with concrete alley-opening clearing; "unhurried purpose" is concrete gait-description

L17.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: courier-added-to-body-map state-tracking beat; "no name written into a ledger where his face would have one" is the body-record-as-anonymized-routing register load-bearing for scene-C @31 file-filing

L18.1 [Scene-B]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: courier-takes-junction-corner SVO with "forty feet off from my held line" concrete spatial; "count let him go past it" is apparatus-release cadence

### Scene-C (paragraphs P19–P30; bones @23–@35)

L19.1 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=y(loc-state-sensory:lamp/light/air/boards) Q5=n Q6=n(em-dash-room-to-contrast) Q7=n Q8=n Q9=n → KEEP
  note: scene-shift entry; long sentence (~55 words) carries the room-floor + lamp-unlit + window-light + air-still + indoor-stillness-contrast load; em-dash separates the establishment from the contrast-with-lane — functional contrastive break

L19.2 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=y(feeling:body-posture) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: SEAM-11 coin-laying metaphor; chose KEEP per Taylor-clinical-accounting register move (per-item-counting figure for evening-replay-shape); bones-walk explicitly cites this as the load-bearing register surface; not gestural — concrete physical analogy for the apparatus-routine

L20.1 [Scene-C]: Q1=y Q2=y Q3=y(Hook-baseline-cardinal) Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: long single-sentence Hook-feed baseline-establishment; the parallels-with-Hook structural cadence is the setup for the rushwick break at P22; "closed itself out clean, every entry resolved against its return" gives transitive completion (flag-002 addressed at scene-window self-audit); load-bearing for the contrast

L21.1 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: four-word topic sentence; second-apparatus-action introducing the rushwick-feed pair

L21.2 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: rushwick-replay parallel-Hook content; the came-back-the-way-the-Hook-had-come-back cadence is the setup for the P22 break; concrete provisioner-train re-crossing

L21.3 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: five-word standalone clause within paragraph — "The provisioner-train cleared the junction" — beat-marker; concrete

L21.4 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: feed-keeps-on triadic enumeration (courier-window / side-alley-figures / report-entry); rushwick replay sweeps the scene-B content forward; load-bearing for the architecture-coming-back-with-the-train at P22

L22.1 [Scene-C]: Q1=y Q2=y Q3=y(apparatus-break-cardinal) Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: five-word topic sentence; the DOES-NOT-SETTLE cardinal break-from-Hook; load-bearing

L22.2 [Scene-C]: Q1=y Q2=y Q3=y(color-persistence-cardinal) Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: the color-persistence-across-time beat; "the feed routing the provisioner-train through the same architecture and bringing the architecture back with the train" is the architecture-correlate that sets up the @29 recognition; load-bearing for the chapter-pivot

L22.3 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n(semicolon-test-to-result-functional) Q7=n Q8=n Q9=n → KEEP
  note: second-length-pass verification with semicolon binding test+result; the semicolon ties the deliberate test ("to see if it was the read and not the feed") to its outcome ("the color persisted") — consequence-binding rhythmic function, not flex

L23.1 [Scene-C]: Q1=y(HARD-KEEP) Q2=y Q3=y(feeling-body-act-cardinal) Q4=y(feeling:1) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — body-act of the recognition-cessation; feeling:1 head-tilt; the body acts before cognition has the word; central +1.5 axis-mover physical surface

L23.2 [Scene-C]: Q1=y(HARD-KEEP) Q2=y Q3=y(axis-move-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — "I stopped the rushwick-pass" is the +1.5 axis-move; chapter's central event SVO bone @29 first half

L24.1 [Scene-C]: Q1=y Q2=n/a(cognitive-register) Q3=y(cognitive-naming-of-body-precedence) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: "The stopping was the body's, before I had a word for what the body was doing" — the body-acts-before-cognition register; load-bearing for the recognition-cessation peak's cognitive register

L24.2 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=y(feeling:hand-came-up-off-boards) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: "the hand I had laid flat on the boards came up off the boards" — concrete body-image of the cessation; feeling-register

L24.3 [Scene-C]: Q1=y(HARD-KEEP) Q2=y Q3=y(architecture-naming-cardinal) Q4=n/a Q5=n Q6=n(em-dash-route-to-architecture-functional) Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — the architecture-naming sentence; INSTRUMENT-COMPLICITY register surface ("instrument-complicity" token does NOT appear, verified); em-dash separates the recognition act from the architecture-without-Sera-naming triadic ("not the lane, not the courier, but the architecture"); pl-2026-05-28-002 delivery; cold-read failure (iv) prevention; sentence reach IS the recognition-shape per scene-window self-audit; Q5 borderline-on-length pre-cleared by HARD-keep

L24.4 [Scene-C]: Q1=y Q2=n/a(cognitive-register) Q3=y(discipline-as-apparatus-refusal-close) Q4=n/a Q5=n Q6=n(semicolon-paired-clauses-anaphora-functional) Q7=n Q8=n Q9=n → KEEP
  note: the discipline-as-apparatus-refusal close; semicolon binds two parallel "the discipline" anaphoric clauses — rhythmic parallel function, not flex; load-bearing for the foreclosure-anchor at the cognitive level

L25.1 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: four-word topic sentence; the close-evening-review beat begins; bone @30 SVO

L25.2 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=y(loc-state:window-light-thinned-to-sill-line) Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: window-light-fading carries the temporal-close without re-establishing evening; "the entries delivered, the count resolved" closes the day's coverage; concrete

L26.1 [Scene-C]: Q1=y Q2=y Q3=n/a Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: five-word topic sentence; the file-courier-body-record beat begins; bone @31 SVO

L26.2 [Scene-C]: Q1=y Q2=y Q3=y(memory-resonance-carve-out-cardinal) Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: long single-sentence with the cf-d10 face-callback + memory:2 verbatim Earth-Bet displacement fold + body-record filing + held-face-then-closed-file (oc-courier-body-map.state initiated→filed); resonance-carve-out lands at body-record filing not at @29 peak per parallel-cognition rubric; load-bearing

L27.1 [Scene-C]: Q1=y(HARD-KEEP-standalone) Q2=y Q3=y(foreclosure-attempt-1-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — five-word standalone bare-form; foreclosure-quartet first attempt; dup-001 SVO repetition begins; do-not-fuse

L28.1 [Scene-C]: Q1=y Q2=y Q3=y(foreclosure-hold-1-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: provisioner-train-holds-the-rushwick-pass; physical-anchor hold (scene-map protected-pattern); parallel construction with P30 terminal hold

L28.2 [Scene-C]: Q1=y Q2=y Q3=y(foreclosure-shape-cardinal) Q4=n Q5=n Q6=n(semicolon-replay-setup-to-foreclosure-functional) Q7=n Q8=n Q9=n → KEEP
  note: long sentence; semicolon separates the replay-setup (train re-crossed/feed brought back/architecture came back) from the foreclosure-shape three-would-not chain; structural rhythmic function, not flex; the three would-not-negations are the foreclosure delivery; load-bearing

L28.3 [Scene-C]: Q1=y Q2=n/a(metaphor-but-figural-not-decorative) Q3=y(foreclosure-seal-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: door-does-not-open-at-the-turn metaphor seals the first attempt; the figural-without-decoration register is Taylor's read of the apparatus-refusal — not Q5 hollow (not over-qualified, not told-emotion); the door-turn figure IS the foreclosure shape

L29.1 [Scene-C]: Q1=y(HARD-KEEP-standalone) Q2=y Q3=y(foreclosure-attempt-2-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — dup-001 second-attempt aspect-marked form; same bone SVO as P27 but distinguished by aspect ("again, slower this time"); deliberate-patience differentiator; do-not-fuse

L30.1 [Scene-C]: Q1=y(HARD-KEEP-TERMINAL) Q2=y Q3=y(terminal-foreclosure-confirmation-cardinal) Q4=n/a Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP
  note: HARD-keep per brief — TERMINAL bone @35; courier-walk-holds-the-rushwick-pass; parallel construction with P28 hold delivers the foreclosure-quartet two-distinct-holds compound; NOTHING APPENDED; chapter terminal-bone

### Sweep totals

sentences-counted: 54
q-lines-emitted: 54 (1:1 with sentences; full sweep performed)
keeps: 54
cuts: 0
cut-clauses: 0
cut-asinines: 0
cut-hollows: 0
reshows: 0
rewords: 0
simplify-puncts: 0
cut-bones: 0
verdict: KEEP-ALL (0 moves)

### Flagged seams forward to Phase 8 / 9

- SEAM-3 (P12.2) — long gap-instrument sentence kept whole per scene-window self-audit; causal continuity load-bearing; if Phase 9 cold-read flags as overlong, the split point "...until the alley delivered it" | "and the feed had no field for what the alley delivered" is available but loses the causal-continuity binding
- SEAM-6 (L24.3) — chapter's INSTRUMENT-COMPLICITY architecture-naming sentence kept whole per HARD-keep; if Phase 9 flags as ornate, split-point after "the architecture I had not asked the feed to mark" is available but the unbroken reach IS the recognition-shape per upstream forks
- SEAM-7 (P23+P24 split across body-act and cognitive-register paragraphs) — defensible per body-acts-before-cognition register; if Phase 9 cold-read reads as over-cognized, P24 can compress but cannot delete
- SEAM-8 (P27 + P29 dup-001 same-SVO bare-form vs aspect-marked-form) — load-bearing for foreclosure pattern; do-not-fuse per scene-map fusion-eligible-runs exclusion
- SEAM-9 (P26.2 memory:2 + state:5 + cf-d10 triple-load) — single paragraph carrying three facet loads; cohesive (all three are body-record filing event); memory:2 verbatim is locked
- SEAM-11 (P19.2 coin-laying metaphor) — kept per Taylor-clinical-accounting register move; bones-walk cites as load-bearing register surface

### Rationale for 0-moves outcome

The upstream scene-window forks at Phase 1 (forks 001-003) self-audited heavily — every flagged seam was either justified, fence-cleared, or marked as drift-risk-low with explicit split-point fallbacks. The bones-walk discipline + the scene-window-self-audit pass + the bones-cuttable license exclusion (no anchor cuts available) combine to leave Phase 7 with no actionable taste-cuts that don't violate either the HARD-keep set or the load-bearing bones-walk. The 0-moves outcome is EARNED by the full per-sentence sweep performed above (54 q-lines emitted, 1:1 with sentence count), not skipped. Phase 7 is in keep-the-good-work mode here; the move-pressure correctly belongs at the prior scene-window forks where it was applied.

## Phase 8 — finalize

stable-line-ids: assigned 1-N sequential; no gaps (Phase 7 cuts: 0)
preamble: prepended from active-project/draft/b01-c05.preamble.md (2 italic paragraphs Sera-architecture trio; separated from body by horizontal rule)
scene-callout-suppression: HARD-stripped sed pass on draft/b01-c05.md; no `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` markers in clean draft (URI-SUBSTANCE-OVERHAUL); scene boundaries conveyed by paragraph break only
clean draft: active-project/draft/b01-c05.md (1605 words: ~190 preamble + 1416 body)
annotated draft: SKIPPED (output.mode: not-dual; no project profile; matches c01-c04 precedent — annotated drafts not authored under default mode)

intermediates pruned (default; not --keep-drafts):
  - draft/b01-c05.phase-1.draft.md (assembled scene-A+B+C)
  - draft/b01-c05.phase-6.draft.md (== phase-1, no inline-mechanical changes)
  - draft/b01-c05.phase-7.draft.md (== phase-6, 0 Q-sweep moves)
  - draft/b01-c05.preamble.md (content prepended to clean draft)
  - draft/b01-c05.scene-A.draft.md, scene-B.draft.md, scene-C.draft.md (scene-window fork outputs)

## Phase 8 — STATS

word-count: 1605 (preamble ~190 + body 1416)
sentence-count: 54 (Phase 7 sweep tally)
paragraph-count: 32 (2 preamble + 7 scene-A + 11 scene-B + 12 scene-C)
bones-authored: 35
bones-rendered: 31 (one-bone-one-sentence-or-paragraph)
bones-merged: 4 (@9 fused with @8 scene-B L1; @12 fused with @11 scene-B L3 per fusion-eligible-run; @25 fused with @24 scene-C L2 per Hook-baseline-pair fusion-eligible-run; @27 fused with @26 scene-C L3 per Rushwick-first-pass-pair fusion-eligible-run)
bones-dropped: 0
bones-rendered-illegible: 0
bones-CUT-BONE: 0
facets-authored (per cite-index post-cycle-3 CLEAN): 60 (loc-state=9, NI=10, sensory=2, state=12, mem=2, feel=1, metaphor=0, vibes=20, exposition=4)
facets-rendered:
  - loc-state: 9/9 (all anchors folded into bone sentences per co-anchor fold rule)
  - narrator-interest: 10/10 (one anchor-slip @2→L4 logged; all entries reach prose)
  - sensory: 2/2 (sensory:1 @4 tactile cart-wheel; sensory:2 @14 sound after cycle-2 re-anchor)
  - state-updates: 12/12 (all 12 entries reach prose via co-cited bone or NI co-fold)
  - memory: 2/2 (mem:1 @19 displacement-cue verbatim; mem:2 @31 Earth-Bet-displacement verbatim)
  - feeling: 1/1 (feel:1 @29 head-tilt body-act lead)
  - metaphor: 0/0 (refuse-by-default upheld)
  - vibes: 20/20 (bias-only mode; register-shape applied; no token-bundle phrases imported as prose surface — Q9 fence held on stitcher-coined hyphens)
  - exposition: 4/4 (2 preamble paragraphs + 2 em-dash-fold inline at @2 / @8)
facets-dropped: 0
facets-unrendered-remainder: 0
reshow-count: 0
reword-count: 0
preamble-source: exposition-facet (not legacy-fallback)
exposition entries-rendered: 4 (preamble=2 italic + 2 em-dash-fold first-mention)
exposition refused-at-R2: 3 (scene-orient @1 / @8 / @23 all refused per fire-rule)
exposition cross-episode-register-skipped: ~36 reader-resident terms not re-glossed (flea-bottom / hook / stitch-house-ward / kings-landing / red-keep / etc.)
dialogue-source: not-applicable (no-speech-episode; not legacy-fallback)
dialogue character-files-loaded: 0
dialogue utterances-rendered: 0
dialogue bare-speech-bones: 0
dialogue unmoored-utterances: 0
dialogue speaker-mismatches: 0

## RECONCILE (URI-STITCH-ACCOUNTING-HONESTY)

bones: rendered(31) + merged(4) + dropped(0) + rendered-illegible(0) = 35 ✓ (== authored bone count 35)
facets: rendered(60) + dropped(0) + unrendered-remainder(0) = 60 ✓ (== cite-index facet-entry count 60)
RECONCILE-BALANCE: PASS — both ledgers balance against their authored totals.
unrendered-remainder rationale: 0 — vibes (20 entries) classified as rendered under bias-only mode per Phase 1 fork rendering convention; all other facet types directly surface in prose. No silent dropping.

## Phase 9 — cold-read terminal gate (pending dispatch)

next: dispatch ONE general-purpose agent to cold-read active-project/draft/b01-c05.md per Phase 9 Step 1 prompt
parallel: dispatch /and-review staging b01-c05 reviewer routine (auditor + dramatist) per Phase 9 Step 3
parallel: dispatch ONE auditor for Phase 9 Step 3.5 prose-rationale-mute audit
