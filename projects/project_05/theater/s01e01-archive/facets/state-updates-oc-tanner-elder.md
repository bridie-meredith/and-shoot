# slice file — facet: state-updates  episode: s01e01  author: dialogue-writer-fork-oc-tanner-elder  scope: actor:oc-tanner-elder
# Plain comments here so build_cite_index does not stack YAML blocks in the consolidated state-updates.md (r3-signal-001).

1 @85 actor:oc-tanner-elder.location: loc-flea-bottom -> tanner-family-yard
2 @95 actor:oc-tanner-elder.location: tanner-family-yard -> on-road-to-flea-bottom
3 @148 actor:oc-tanner-elder.location: on-road-to-flea-bottom -> flea-bottom-market-side-junction

# Seam: the elder's position flips happen off-screen. He travels from Flea Bottom (state.md baseline) to the tanner village before @85; from village to road at the gate-cross (Taylor's @94, no elder-subject beat); from road to KL market-side junction between @96 and @148. Each entry fires on the first observable beat that confirms the new location, not the literal flip-beat. Flagged for cross-facet review with studio (location-state) and potentially with the dialogue-writer for Taylor (whose @94 "crosses the yard gate" is the only on-stage gate-cross). If studio's location-state file carries an elder co-location entry at any of these beats, alignment is required.

# Reality: all three are persistent location flips, not transient postures. Elder remains at each new location across multiple subsequent beats (in-yard @85-@94; on-road @95-@96; market-side @148-@155).
# Authority: elder fork writes actor:oc-tanner-elder.location. Field is on state.md schema.
# Frugality: <old> for entry 1 matches state.md baseline (loc-flea-bottom). Each <new> chains correctly to the next <old>.
# Cross-facet: tens=3 at @90 (routing) and @151 (Taylor speaks back) do NOT fire state-updates on the elder — the routing-act at @90 enacts a pre-committed placement (no elder-side field flip; placement is already in STM as historical), and @151 is Taylor's irreversible commit not the elder's.
# Skips: @86 (speaks-to, no field change), @88 (Taylor subject, no elder change), @90 (routes-Taylor enacts pre-committed placement; no elder-side field flip; tens=3 but consumer-side validator @64-class does not apply — this is not a registration of an irreversible record-mutation against the elder), @96 (durative motion, location already flipped at @95), @148 dual-fire risk: @148 is elder-subject "speaks to dock-runner" which is the first observable beat at market-side; the location-flip is anchored here; the speech-verb itself does not change location. @150 (dock-runner speaks to elder), @151 (elder speaks to Taylor) — same location as @148, no further flips.
