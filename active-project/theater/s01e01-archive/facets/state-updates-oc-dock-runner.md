# slice file — facet: state-updates  episode: s01e01  target-class: actor:oc-dock-runner  author: dialogue-writer-fork:oc-dock-runner (R1)
# Plain comments here so build_cite_index does not stack YAML blocks in the consolidated state-updates.md (r3-signal-001).

1 @141 actor:oc-dock-runner.position: loc-flea-bottom -> fish-gate-margin
2 @144 actor:oc-dock-runner.position: fish-gate-margin -> loc-flea-bottom
3 @149 actor:oc-dock-runner.position: loc-flea-bottom -> market-side-junction
4 @155 actor:oc-dock-runner.position: market-side-junction -> loc-flea-bottom

# field-extension: position sub-location values (fish-gate-margin, market-side-junction) — sub-zones within loc-flea-bottom; tracked-state-aspect per calibration anchor @57 edric.position (fine-grained position values are licit). Pre-episode baseline: state.md location=loc-flea-bottom (broad). Sub-zones resolve into loc-flea-bottom on exit; non-zone presence in Flea Bottom remains loc-flea-bottom.

# Sparsity: 4 fires across 9 dock-runner-involved beats (141, 143, 144, 146, 148, 149, 150, 153, 155). Position-flips only; entries cluster on the FGM-evasion (@141, @144) and the junction-exchange (@149, @155). No fires in non-dock-runner beats.

# Refusals (NONE-CORRECT):
#   @143 oc-dock-runner pivots — transient posture (anti-pattern #8 posture-as-state). Tens=1. Pivot is the motor moment preceding exit at @144; orientation does not persist as load-bearing posture state.
#   @146 the flies relay oc-dock-runner — Taylor's surveillance side; no field on the runner changes.
#   @148 oc-tanner-elder speaks to oc-dock-runner — runner-as-listener; verbal instruction is registration, not canonical mutation on the runner. The runner's consequent action (approach @149) carries the position-update; the instruction itself does not.
#   @150 oc-dock-runner speaks to oc-tanner-elder — dialogue act; speaking does not flip a tracked field on the speaker.
#   @153 oc-dock-runner speaks to taylor-hebert-flea-bottom — first on-stage exchange with Taylor. knowledge.taylor-assessment field-extension considered and REFUSED: per character card and STM, the runner's "knew the girl was dangerous before she had done anything dangerous" reads as standing character-perception mode, not a discrete on-screen commit-beat. Conservative refusal per rubric Floor Defense (sparsity load-bearing; over-firing corrupts canonical memory). Seam flagged below for cross-facet review if narrator-interest or feeling-flags fire on a paired beat.

# Cross-facet checks:
#   Tens contract: no @39-class held-against-turn beats among dock-runner anchors. No @64-class strong-expect-registration beats on dock-runner targets. Tens scalars (@141=2, @144=1, @149=2, @155=1) consistent with sparse position-flip firing.
#   Narrator-interest contract: oc-dock-runner is non-POV; per rubric POV-restriction, non-POV actor-state shifts do NOT require narrator-interest co-citation. Taylor's perception of the runner (the flies-relay beats @142, @146) is narrator-interest territory, not state-updates.
#   POV / authorship: actor:oc-dock-runner.* is oc-dock-runner-fork authority. No cross-POV authoring. studio.* and prop:*.* deliberately not authored here (studio fork's domain).

# Seams (flagged for cross-facet review):
#   SEAM-1 @153 knowledge-assessment field. Candidate fire `actor:oc-dock-runner.knowledge.taylor-assessment: unknown -> dangerous-directional-known` REFUSED on Floor-Defense grounds (character-card standing-mode, not discrete-event). If narrator-interest fires on @153 capturing the runner's reading of Taylor, or if feeling-flags fires on a paired beat (@152 face-to-face / @153 first address) — re-examine. Risk if missed: s01e02 trust-ledger references will lack a canonical baseline.
#   SEAM-2 tens-file curve-verdict prose drift. Tens verdict annotation reads "@140: reversal-proximity peaks — dock-runner pivots; evasion enacted" but proto-line 140 is `the flies relay the Watch position` and dock-runner-pivots is proto-line 143 (tens=1). The verdict-prose IDs appear offset from actual proto-line IDs in the dock-runner block. Not load-bearing for state-updates authoring (entries anchor on proto-line IDs, not on verdict-prose labels) but worth flagging to dramatist for verdict cleanup.
#   SEAM-3 @149 "approaches the market-side junction" — anti-pattern #7 (pre-emption) consideration: "approaches" can read as approach-not-arrival. Resolved by forward-reference: @150 the runner speaks to the elder at the junction; the position-flip must land by @150. Firing on @149 as the arrival-beat (approach terminates with arrival in this SVO frame); @150 would also be defensible. Held at @149.
