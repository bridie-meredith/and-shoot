# /and-facets b01-c06 — audience-gate consolidated report (cycle 1)

episode: b01c06
date: 2026-05-30
cycle: 1 / 3
reviewers: cape-fic-reader, dark-fantasy-reader, worm-canon-pedant (active-audience fallback, 8 facets + dialogue); sensory-disambiguation-pedant, sensory-modality-coverage, sensory-old-state-reader (sensory specialists)
aggregation: strict 3-of-3 ACCEPT per facet (URI-AUDIENCE-AGGREGATION-RULE; single dissent fails)

## Per-facet aggregate (cycle 1)

| facet | cape-fic | dark-fantasy | worm-canon | sensory specialists | AGG |
|---|---|---|---|---|---|
| location-state | accept | accept | accept | — | **ACCEPT** |
| state-updates | accept | accept | accept | — | **ACCEPT** |
| feeling | accept | accept | accept | — | **ACCEPT** |
| exposition | accept | accept | accept | — | **ACCEPT** |
| dialogue (wren) | accept | accept | accept | — | **ACCEPT** |
| sensory | — | — | — | accept / accept / accept | **ACCEPT** |
| interest-narrator | revise | revise | revise | — | **FAIL (3R)** |
| vibes | revise | revise | revise | — | **FAIL (3R)** |
| memory | accept | revise | accept | — | **FAIL (1R)** |
| metaphor | accept | accept | revise | — | **FAIL (1R)** |

6 ACCEPT / 4 FAIL → remediation cycle 1 (fixer → re-audit → re-fire 5b on the 4 failed facets).

## Consolidated revise callouts (deduped by [facet:id])

### interest-narrator (FAIL 3R)
- **[interest-narrator:4] @22 — 3-of-3 REVISE.** "the seal is the breach …" re-fires the X-is-Y inverted-predicate chassis after its licensed single use at narrator:2 @8. Reads as template/author-signature, not Taylor's clinical cognition. **Converges with auditor AP-SCAN AP-010 (narrator:4 named repair candidate, 29% saturation).** REPAIR: keep the framework-operates-correctly-with-wrong-premise substance; render it in clinical data-register WITHOUT the inverted-predicate form.
- **[interest-narrator:6] @12 — worm-canon.** "the record was always the route" backward-narrativizes/personifies the instrument. REPAIR: keep the node-vs-name category precision; drop the personification.
- **[interest-narrator:3] @13 — cape-fic (secondary).** "the step the record has been waiting four months for her to take" gives the record agentive patience. **Converges with auditor TASTE-FLAG (voice-fidelity).** REPAIR: drop the agentive-record framing.

### vibes (FAIL 3R)
- **[vibes:5] @8 — 3-of-3 REVISE.** `licensed-by: ... canon:wren-d14-routing-gap-failure` uses a DOWNSTREAM canon event (d14) as a license source in a b01c06 file — foreknowledge the chapter hasn't earned (the FACET knowing Wren's arc terminus). Token "omitted-from-the-substrate-she-will-fall-through" reaches forward. REPAIR: strip the d14 canon-citation; re-anchor on chapter-attested license (proto:8 + world-build:cond-road-to-hell-chain-shape) and present-state token language ("name-withheld-from-record", "protection-as-the-routing-gap" stand on their own; soften "she-will-fall-through" to present-risk). Audience-ONLY catch (auditor read the tag as benign metadata).
- **[vibes:13] @24 — worm-canon.** Same `canon:wren-d14-routing-gap-failure` license on the tragic-causal entry. REPAIR: strip d14; re-anchor on chapter-attested state.

### memory (FAIL 1R)
- **[memory:2] @19 — dark-fantasy.** "a body that does not know how it is held" is forward-consequence (pre-echo of the send / Sera's fate), not the backward-reach the monument-callback license requires (the callback must point at what was BUILT — the arrangement / Otto-trade). REPAIR: re-word the callback gloss to point backward at the established arrangement, not forward at Sera's future. Audience-only catch.

### metaphor (FAIL 1R — taste conflict)
- **[metaphor:1] @24 — worm-canon REVISE; cape-fic + dark-fantasy ACCEPT (praised).** worm-canon (voice-precision specialist): the "tidy, complete, correct" sardonic-recognition simile requires Taylor to stand outside her own cognition and observe its elegance — out of her clinical cost-moment register; NI:5 @24 already renders the two-substrate contrast (canon-correct). cape-fic + dark-fantasy valued the false-completion aesthetic as a distinct layer. DISPOSITION: strict 3-of-3 requires worm-canon's REVISE be met; a reword that keeps the simile keeps the out-of-register altitude → minimum-change-to-meet-criteria = **DELETE meta:1** (aligns with metaphor's refuse-by-default discipline; the beat survives via NI:5 + feel:2 @24, so no structural loss). The 2/3 praise is recorded; the deletion is a register-fidelity call, not a quality dismissal.

## Convergence trace
- Auditor findings (Phase 5): 0 HARD, 10 SIGNAL.
- Audience callouts (deduped): 6 ([interest-narrator:4/:6/:3], [vibes:5/:13], [memory:2], [metaphor:1]).
- Shared (audience + auditor both flagged): [interest-narrator:4] @22 (AP-010), [interest-narrator:3] @13 (TASTE-FLAG). → **bidirectional loop: VALIDATED** (≥1 shared finding).
- Audience-only: [vibes:5]/[vibes:13] (d14 foreknowledge leak), [memory:2] (forward-reach), [metaphor:1] (register altitude) — the adversarial readers caught voice-drift the mechanical scan could not articulate. This is the gate earning its keep.

## Routing
Remediation cycle 1 → fixer (consolidated callouts above) → re-run cite-index → re-fire Phase 5 auditor → re-fire Phase 5b for {interest-narrator, vibes, memory, metaphor} only (the 6 passed facets do not re-fire). Cap: 3 cycles.
