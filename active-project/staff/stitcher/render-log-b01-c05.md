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
