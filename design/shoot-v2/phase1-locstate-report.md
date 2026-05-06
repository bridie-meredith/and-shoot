# Location-State Facet — Phase 1 Lock Report

Phase 1 (reviewer-tuning) of the shoot-v2 facet-tuning process for the location-state facet. Run 2026-05-06.

**Outcome:** rubric locked at V2. Baseline-to-beat: 46% aggregate accept under V2 strict. Six systemic faults named. Floor defended on the e06 remote-recon block and two specific load-bearing entries.

---

## Inputs

- **Rubric:** `design/shoot-v2/rubric-location-state.md` — three axes (necessity, interestingness, frugality) + six anti-patterns + cross-axis tests.
- **Corpus:** `design/shoot-v2/loc-state-candidates.md` — 65 candidate entries seeded permissively from s01e01–e06 proto-lines (1101 proto-lines → 65 candidates → V2 outcome).
- **Reviewers:** dark-fantasy-reader, pulp-enthusiast, worm-canon-pedant (active audience).
- **Proto-line corpus:** `active-project/theater/proto-lines/s01e0{1..6}.md`.

---

## Trajectory

| Round | Stage | Accept | Notes |
|---|---|---|---|
| 1 | V1 lenient (per persona) | 65/65 (100%) ×3 | Schema-form + plausible-anchor only. Floor-ceiling — does no work; baseline by design. |
| 1.5 | V2 strict (per persona) | DFR 22/65 (34%) · PUL 28/65 (43%) · WCP 37/65 (57%) | Same locked rubric, three lenses. |
| 1.5 | V2 strict (aggregate ≥2/3) | **30/65 (46%)** | The number to beat in writer-tuning. |

V1→V2 lift on lenient floor: 100% → 46% = **−54 points**. The rubric does work proportional to the dialogue facet's V2 bite (40% locked floor there). For lift comparison, V2-aggregate 46% is the **baseline-to-beat** when a writer fork later regenerates a corpus from intent + cards.

---

## Per-persona profiles

- **dark-fantasy-reader (34% accept; strictest).** Cuts hard on persistence-as-state, mood-painting on stillness, and inherited re-naming. Accepts sparse threshold-crossings, light-event with menace, doorframe-cold contact. Floor-defense: #22 (light-on-rushes makes Taylor's spatial-avoidance legible as menace), #52 (gatehouse-lantern at half a league anchors entire surveillance sequence's distance-constraint).
- **pulp-enthusiast (43% accept; middle).** Forward-momentum lens. Accepts gate-events, scene-population beats that change the board (three women at kiln wall, arch-entry of inspector party). Cuts prop-placements, transit-through-known-terrain. Floor-defense: #63 (hoof-on-cobble half-a-league north — herald-at-wall canonical case).
- **worm-canon-pedant (57% accept; most permissive).** Accepts perception-mediated and fauna-feed beats where Taylor's swarm-network demands spatial resolution. Six floor-defenses on the e06 remote-recon block (#52–#56, #63). Embraces darkness-navigation contact-beats (altar-table edge meeting hip) and predawn yard re-entry with new tactical-loaded conditions (Rowan-occupying-doorway, gate-ahead).

The three lenses split honestly. WCP's wider floor catches genuine canon-load (Phase 0 note #14 lives there). DFR's tighter rejection catches set-dressing.

---

## Aggregate accepts (30 entries)

Unanimous (3/3): #3, #7, #10, #11, #12, #18, #24, #27, #28, #38, #42, #50, #57, #58, #60, #61 — 16 entries.

Split with floor-defense as decisive vote: #22, #52, #53, #54, #55, #56, #63 — 7 entries (the remote-recon and light-event block).

Two-of-three accepts (no floor-defense): #5, #14, #17, #20, #29, #33, #45 — 7 entries.

The 7 accepts in the last group are the **seam zone**. They sit at the rubric threshold and one persona's cut is defensible. Notable: **#5 (twelve feet of packed dirt)** — within-scene movement in the same sept-yard already anchored by #3. DFR cut on frugality; PUL+WCP kept on "the surface and distance is what the move turns on." This is exactly the user-flagged risk: even V2 lets some within-scene blocking through. See *Suspect seam* below.

---

## Defended floor (entries that survive on rubric pushback)

The audience defended 7 entries the form-rubric *might* have cut. Floor-defense is a tuning signal — the rubric must not push these to 0%.

- **#22 — light-on-rushes (sept-nave, e03).** The wedge of morning light through an open side door is *operative menace*: Taylor's subsequent positioning (PL8 holds feet outside the light) only reads as deliberate spatial-avoidance with the light cited as a condition. Without it, she is "just standing in a room." Atmosphere with teeth, not mood-painting.
- **#52 — gatehouse-lantern at half a league (e06 remote-recon anchor).** Distance is the load-bearing constraint of Taylor's perception apparatus. Strip the entry and the entire e06 surveillance sequence loses its keystone — every subsequent light-event (#54, #55, #56, #57) inherits from this distance-context.
- **#53 — mouse-warm at hip-seam (e06 sept-yard wall).** Fauna-feed event. The seam-at-hip + mouse-warm names the spatial and thermal resolution Taylor's passive feed delivers; the feed-spike (PL21) only resolves with the loc-state cited.
- **#54, #55 — second light, third light (e06 gatehouse-distant).** Each new light is a discrete state-change at the same remote location; sequencing matters as a signal (rider-prep, not guard-change).
- **#56 — gate-yard at fifty feet (e06).** Bird closes distance; the smear-resolves-to-surfaces is a perceptual threshold-crossing requiring new sub-location and lit-conditions citation.
- **#63 — hoof on cobbles half a league north (e06).** Auditory detection. Sound-carrying + cobble-surface as named conditions — the exact "herald at the wall" case the user articulated. Without sound-carrying named, hoof-arrival at Taylor's position has no mechanism.

The remote-recon block alone (#52–#57, plus #53, #63) is **9 entries of unambiguous floor**. Phase 0 note #14 is now operationally answered: remote-recon beats survive as loc-state when the perception-cost depends on a named location fact, not as a separate proto-line class.

---

## Six systemic faults (consolidated across personas)

These are the failure modes the original 65-candidate corpus exhibits. They name what the V2 rubric is *for*.

1. **Persistence-as-state.** Single largest fault. "Holds," "stays," "stands," "sits," "lies" anchors treated as state-changes. Includes the user's herald/cart distinction inverted: corpus fired on carts. ~11 rejects.
2. **Inherited re-naming on within-scene movement.** Re-citing the same location at every actor step rather than firing on environment turnover. ~10 rejects. Most acutely in the e05 village-common scene (the scene fires four actor steps in a row, none earning a new entry).
3. **Plan-bullet residue.** s01e05 nearly entirely converted from shoot-v1 STUDIO scene-summaries; prop-placements (trestle, satchel, scroll) routed to loc-state instead of state-updates. ~4 rejects clustered.
4. **Actor/animal state laundered as loc-state.** Conditions like `lodge-doorway-occupied`, `three-bodies-entering` (when stillness), `rowan-five-paces`, `mouse-warm` describe actor positions or fauna events, not location conditions. ~5 rejects (with WCP defending some on fauna-feed grounds).
5. **Mood-painting on stillness.** Atmospheric observations ("the road holds the silence," "the grey holds the road," "the nave-cold settles") anchored on perception beats. The project's sensory register makes this especially tempting and especially wrong. ~5 rejects.
6. **Time/weather padding.** Entries distinguishable from predecessors only by marginal label variation (`sun-cresting` vs. `sun-up`; `cold` vs. `cold-deepening`) without the conditions or sensory note doing new work. ~3 rejects.

---

## Suspect seam — entry #5

Entry #5 (`@14 sept-yard | dawn | clear | packed-dirt-line | twelve feet of packed dirt to the line's open spot`) was accepted 2/3 (PUL + WCP) and rejected by DFR on frugality. It is the cleanest example of *within-scene movement that the rubric currently licenses but might not should*.

The user-flagged tightening — "movement that crosses a boundary or turns over the environment frame, not within-scene navigation" — would convert #5 to REJECT and bring aggregate accept to **29/65 = 45%**. Marginal numerical effect; meaningful philosophical effect (the rubric becomes "loc-state fires on boundaries and frame-turnovers, full stop").

**Decision held for Phase 2.** Under the locked V2, #5 is in. If writer-fork output later replicates the surface-and-distance focus on within-scene moves and the audience pushes back, the rubric tightens at that point. Reviewer-pushback within Phase 2 is the legitimate channel for this adjustment, not pre-tightening.

---

## Lock declaration

V2 of `design/shoot-v2/rubric-location-state.md` is **locked**. It will not soften between Phase 1 and Phase 2. Lift numbers in subsequent rounds are only meaningful under this fixed rubric.

Subsequent phases (per `design/shoot-v2/facet-tuning-process.md`):

- **Phase 2 — writer fork.** Studio (or a per-location fork) reads location cards + rubric and authors fresh loc-state entries from intent + cards, blind to this candidate corpus. Sample size 15–20 across stratified location-slugs. Re-run audience under same locked V2.
- **Phase 3 — adversarial seams.** Per-persona hostile counter-arguments on accepts; aggregate to one seam per unit.
- **Phase 4 — defense or revision.** Studio fork defends-or-revises.
- **Phase 5 — final adjudication.** Audience under same locked V2; cross-unit dependency check (e.g. light-condition #22 paired with avoidance-blocking PL8); shippability assessment.

---

## Artifacts

- Rubric: `design/shoot-v2/rubric-location-state.md`
- Candidate corpus: `design/shoot-v2/loc-state-candidates.md`
- V1 reviews: `active-project/audience/<persona>/loc-state-v1-review.md` (×3)
- V2 reviews: `active-project/audience/<persona>/loc-state-v2-review.md` (×3)
- This report: `design/shoot-v2/phase1-locstate-report.md`
