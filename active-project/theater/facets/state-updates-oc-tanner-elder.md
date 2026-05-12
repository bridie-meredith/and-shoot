# source: state-updates-oc-tanner-elder

facet: state-updates (slice)
episode: s01e03
author: dialogue-writer fork — oc-tanner-elder
target-scope: actor:oc-tanner-elder.*
---

# Authoring notes

Slice authors only `actor:oc-tanner-elder.*` entries. Co-author seams:
- prop:coin.* (holder, position) at @67 — studio's authority; not authored here. Elder fork co-cites on `actor:oc-tanner-elder.stance-toward-taylor` at the same beat (two-target, same-beat).
- prop:account.* (holder, ink-state, seal-condition) at @138-@140 — studio's authority; not authored here. Elder fork co-cites on `actor:oc-tanner-elder.formal-record-status` at @139 (the seal-beat).
- studio.actors_in_junction / studio.actors_in_writing-room at @136-@137 — studio's authority; elder fork fires `actor:oc-tanner-elder.location` only on the entry-beat per the @57 edric-precedent in the rubric anchors.
- tanner-father's @98 own-state delta (delivering the lord's-man report) — tanner-father fork's authority; not co-authored here.
- messenger @127-@132 is transient (not on active-actor roster) — studio handles; elder fork fires the knowledge-acquisition on the elder at @129.

Hard-fence honor (card §"Hard Fences"): the elder does not warm. None of the four fires encode warmth, affection, concern-for-Tya, curiosity-about-what-she-is, or any softening register. The @67 stance-shift is explicitly bureaucratic / paid-relay-channel (not affective); the @129 knowledge fire is channel-acquisition (not personal); the @137 location is operational commitment; the @139 formal-record-status is structural channel-position. Card-stance preserved.

Per-file cull deltas (delete-only):

- CULLED @5 (clerk speaks to elder) — proto-line is bare ("clerk speaks") with no in-line content specifier; the clerk-tier knowledge flip is inferable from episode plan but not from anchor-verb alone. Reality-axis exposure under strip-test: weak. Refused per "conservative move is to refuse the entry" guidance; the episode-plan-inferred knowledge of bureaucratic touch is downstream-evidenced via @129's senior-operative escalation and folds into that fire's `unknown -> received-senior-operative-written-request` chain (the clerk-tier touch and the senior-operative touch are the same Hightower channel, opening across two tiers).
- CULLED @98 (father speaks to elder) — same speculative-content failure mode as @5. The father's information delivery is downstream-evidenced at @102 (elder relays to Taylor), but the anchor-verb alone is "speaks." Refused on Reality-axis; the village-claim-status field is not a stable tracked extension if the source-beat is bare speech.
- CULLED @50 / @102 position fires — sub-location-within-loc-flea-bottom is permitted (cf. @137) but @50 and @102 are short approach-and-converse beats that resolve back to junction within the same scene (elder is back at junction by @96 implicit, by @127 explicit). Persistence test: weak (≤4 beats each); brief-priority for position is low; refused as density-on-flat for non-load-bearing transitions.
- CULLED @138 (elder writes the account) — transient drafting-state superseded one beat later by @139 sealing. Anti-pattern #7 (lagging/pre-emption) avoidance — fire on the commit-beat (@139), not the in-progress beat. Writing is reversible (could tear up); sealing is the irreversible commit.
- CULLED @136 (elder exits junction) — exit-half of the @136→@137 transition. Position flip-beat is @137 (entry); fire there per @57 edric-precedent ("steps back through the door" was the through-door beat, not the leaving-yard beat). Frugality.
- CULLED a second-field fire at @139 (stance-on-tya) — collapsed into formal-record-status to avoid compound-on-same-operational-shift. The sealing IS the stance-operationalization; tracking both is anti-pattern #4 (compound entry split across fields where the underlying delta is one).

Field extensions documented inline. All four extensions are tracked-state aspects (relationship-role, knowledge, location, record-status) per the rubric's field-extension protocol — none are perception, mood, or stylistic flourish.

---

1 @67 actor:oc-tanner-elder.stance-toward-taylor: conditional-embed-on-trade-reference -> conditional-embed-plus-paid-information-relay
# field-extension: stance-toward-taylor (relationship-role on elder's state schema; tracks the structural stance, not emotional register — card hard-fence on no-warmth preserved; the new value is bureaucratic/transactional, not affective).
# axis: Reality — coin-placement at @67 is the observable, irreversible act ("oc-tanner-elder places the coin"); the wasps @60-@61 already relayed Taylor's dock-side outcome back to the elder, so the coin formalizes a paid-relay relationship beyond the labor-web embed. Persistence: holds forward (informs @103 elder-relays-back, @138 elder-writes-account drawing in part on Taylor's relay-product). Strip-test: without entry, the field reverts to trade-reference-only and the elder's @138 account composition is unmotivated.
# axis: Authority — elder fork on elder field; field-extension licit (relationship-role is tracked structural state, not perception). Card §"Description" establishes "trade-reference" baseline; the extension captures the formalization.
# axis: Frugality — old matches card baseline (conditional embedder on trade-reference); new is a single discrete field-shift, not a compound. Coin-as-prop is studio's authority and not co-written here.
# cross-facet: tens@67=3 (per tensometer.md axis citation summary: "@394: stakes-visibility + reversal-proximity peaks — elder places coin; irreversible registration"). State-update co-citation strongly expected at tens-3 irreversible-registration class — provided. Non-POV actor: narrator-interest co-citation not required.

2 @129 actor:oc-tanner-elder.knowledge.hightower-file-channel: none -> senior-operative-formal-written-request-received
# field-extension: knowledge.hightower-file-channel (knowledge field; canonical analog to actor:taylor.knowledge.record-state in s01e01 rubric anchors). Tracks elder's awareness that an upstream channel above clerk-tier has opened on his placement.
# axis: Reality — messenger delivers the senior-operative's formal written request at @129 ("the messenger speaks to oc-tanner-elder"); the request artifact itself is the content the messenger speaks of — written-form is what the messenger conveys (vs. @5's bare clerk-speech which has no specified artifact). Persistence: drives @137 entry-to-writing-room and @138 composition; without this knowledge, the elder has no addressee for the @138 account. Strip-test: load-bearing for the entire @136-@141 sequence.
# axis: Authority — elder fork on elder knowledge field; field-extension licit (knowledge is the rubric's named tracked-state aspect). Card §"Description" + ltm establish no prior Hightower-channel awareness (elder operates on broker-cut economics, not aristocratic-channel knowledge); new value is a specific, named channel.
# axis: Frugality — old=none (verified against ltm/stm/card); new is a single discrete field-shift. The "formal written request" qualifier is load-bearing (distinguishes this from the clerk-tier @5 touch); not redundant with @67 (stance) or @139 (record-status) — knowledge of the channel is distinct from operational engagement with it.
# cross-facet: tens@129=2 (irreversible knowledge acquisition; messenger delivery cannot be unheard). Non-POV actor: narrator-interest co-citation not required.

3 @137 actor:oc-tanner-elder.location: market-side-junction -> writing-room
# field-extension: sub-location within loc-flea-bottom. Card §state.md baseline is loc-flea-bottom; the writing-room is a discrete operational sub-location load-bearing for the @138-@139 commit sequence. Default location-after-episode reverts to loc-flea-bottom unless next episode opens with elder elsewhere (handled at showrunner write-back).
# axis: Reality — discrete persistent position change ("oc-tanner-elder enters the writing room"); persists @137-@141 minimum (composition + sealing + handoff to middleman). Load-bearing for @138 + @139. Strip-test: without entry, the sealing at @139 has no scene-location-of-record. Fire-beat is @137 (entry), not @136 (exit) per @57 edric-precedent.
# axis: Authority — elder fork on elder location field; sub-location extension is licit-per-rubric (the writing-room is a recurrent operational space for the broker class; not invented for this episode).
# axis: Frugality — old=market-side-junction (recurrent location across episode: @4-@10 first-clerk scene, @96-@101 father scene, @127-@132 messenger scene); new=writing-room. One entry, one field. No co-fire on door-state or junction-roster (those are studio).
# cross-facet: tens@137=1 (low-rung position transition, but discrete and load-bearing for the climax @139). Non-POV actor: narrator-interest co-citation not required.

4 @139 actor:oc-tanner-elder.formal-record-status: not-on-record-channel -> sealed-account-relayed-up-hightower-channel
# field-extension: formal-record-status (tracked-state aspect; parallel to actor:taylor.administrative-status in s01e01 rubric anchors). Tracks elder's structural position relative to upstream file-channels.
# axis: Reality — irreversible sealing of the written account at @139 ("oc-tanner-elder seals the account"). Sealing is the commit-act: ink dries, seal sets, account cannot be retracted from the channel once handed to the middleman at @140. Persistence: permanent (the account exists in the Hightower channel from this beat forward; downstream-episode-load-bearing). Strip-test: without entry, the elder's structural shift from passive placement-broker to active upstream-reporter is unrecorded; the season's third-act architecture-change is missing canonical anchoring.
# axis: Authority — elder fork on elder field; field-extension licit (record-status is the canonical extension type per rubric §calibration anchors). Old=not-on-record-channel (verified: no prior formal-record relationship to any aristocratic channel in card/ltm/stm); new=specific channel and artifact.
# axis: Frugality — old=baseline-none; new is a single discrete field-shift. Stance-toward-taylor at this beat would be a compound second-fire — collapsed (the sealing operationalizes the @67 stance; the operational shift is one delta, not two). Prop:account.seal-condition is studio's authority and fires separately (no overlap).
# cross-facet: tens@139=3 (structural climax of episode per tensometer.md: "@468: three axes light (stakes-visibility + reversal-proximity + body-charge) — elder seals account; structural climax"). State-update co-citation STRONGLY expected at tens-3 irreversible-registration class — provided. Non-POV actor: narrator-interest co-citation not required (Taylor does not perceive the sealing directly; flies-relay at @142 mediates her perception but the canonical state lives on the elder, not on Taylor's knowledge).
