---
facet: state-updates
sources: [env, oc-broken-maester, oc-tanner-elder, oc-tanner-father, taylor-hebert-flea-bottom]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---

# source: env
facet: state-updates
scope: environmental
episode: s01e03
author: studio (env R1 fresh fork)
---
# source: state-updates-env

# Field-extension register
#
# The following OC prop slugs are introduced in this episode as oc-* field extensions.
# No formal prop cards exist in cards/props/ for any of these (INDEX.md confirmed empty).
# Each extension is documented here per rubric §"Field-extension protocol".
#
# oc-record-book-market-junction  — the clerk's official record book at the market-side junction;
#   fields: physical_condition (open/closed), clerk-1-entry (absent/dictated), position (location)
#   # field-extension: new OC prop, first-touch this episode; clerk-1 scene track
#
# oc-taylor-log                   — Taylor's personal working log; held and carried by Taylor;
#   fields: physical_condition (open/closed)
#   # field-extension: new OC prop, first-touch this episode; recurs every log scene
#
# oc-record-book-apothecary       — the apothecary's record book used by clerk-2;
#   fields: physical_condition (open/closed), clerk-2-entry (absent/written), holder (second-clerk/apothecary-surface)
#   # field-extension: new OC prop, first-touch this episode; clerk-2 scene track
#
# oc-coin                         — the coin the elder places into Taylor's palm;
#   fields: holder (oc-tanner-elder/mid-air-between-them/taylor-hebert-flea-bottom)
#   # field-extension: new OC prop, single-scene; load-bearing for the village-claim / coin-transfer turn
#
# oc-maester-pen                  — the broken maester's writing pen;
#   fields: physical_condition (writing/set)
#   # field-extension: new OC prop; tens=3 (@90) reversal-proximity peak; pen-set terminates writing session
#
# oc-elder-account                — the written and sealed account the elder composes and hands to the middleman;
#   fields: physical_condition (blank/written), seal-condition (unsealed/sealed), holder (oc-tanner-elder/middleman)
#   # field-extension: new OC prop; tens=3 (@139) structural climax; institutional state-change on village-claim axis

# ---
# SCENE: first clerk / market-side junction (@3–@13)
# Tens cluster: @7=2, @8=2, @11=3 (stakes-visibility + reversal-proximity peak)
# ---

1 @7 oc-record-book-market-junction.physical_condition: closed -> open

2 @8 oc-record-book-market-junction.clerk-1-entry: absent -> dictated

3 @9 oc-record-book-market-junction.physical_condition: open -> closed

4 @11 oc-record-book-market-junction.position: market-junction -> beyond-Fish-Gate
# cross-facet: tens=3 @11, stakes-visibility + reversal-proximity; record physically exits Taylor's observable range; irreversible

# ---
# SCENE: first log entry / waking dawn (@14–@16)
# Tens cluster: @14=1, @15=1, @16=1 — establishing-entry; first log of episode
# ---

5 @14 oc-taylor-log.physical_condition: closed -> open

6 @16 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: log entry / pre-dawn write (@29–@31)
# Tens cluster: @25=1, @26=2, @27=2 — waking sequence context; log entry anchors dawn surveillance close
# ---

7 @29 oc-taylor-log.physical_condition: closed -> open

8 @31 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: second clerk / apothecary (@33–@45)
# Tens cluster: @39=2, @40=2, @41=1, @42=3 (stakes-visibility peak — irreversible second commit)
# ---

9 @39 oc-record-book-apothecary.physical_condition: closed -> open

10 @40 oc-record-book-apothecary.clerk-2-entry: absent -> written

11 @41 oc-record-book-apothecary.physical_condition: open -> closed

12 @42 oc-record-book-apothecary.holder: second-clerk -> apothecary-surface
# cross-facet: tens=3 @42, stakes-visibility; release is the irreversible sealing of the second commit

# ---
# SCENE: coin transfer / elder–Taylor (@66–@71)
# Tens cluster: @66=2, @67=3, @68=3 (double-peak — elder places coin / Taylor closes fist)
# ---

13 @67 oc-coin.holder: oc-tanner-elder -> mid-air-between-them
# cross-facet: tens=3 @67, stakes-visibility + reversal-proximity; coin leaves elder's possession

14 @68 oc-coin.holder: mid-air-between-them -> taylor-hebert-flea-bottom
# cross-facet: tens=3 @68, body-charge; Taylor's fist closes on coin — double-tap with @67

15 @69 oc-taylor-log.physical_condition: closed -> open

16 @71 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: maester writes / sets pen (@87–@94)
# Tens cluster: @89=2, @90=3 (reversal-proximity peak — pen-set terminates session)
# ---

17 @92 oc-taylor-log.physical_condition: closed -> open

18 @94 oc-taylor-log.physical_condition: open -> closed

19 @90 oc-maester-pen.physical_condition: writing -> set
# cross-facet: tens=3 @90, reversal-proximity; discrete termination of pen-scratch session — persistent (maester does not resume within episode)
# field-extension: oc-maester-pen (new OC prop; pen-set is a tracked-state transition, not a momentary motor event; persists through end of observed session)

# ---
# SCENE: overnight network / perimeter walk / Red Keep sighting (@110–@125)
# Tens cluster: @118=2, @119=2, @121=2, @125=2
# Operational-radius advancement: range reaches 600m (episode goal); fires on @125 (facing Red Keep; radius
# confirmed at new ceiling)
# ---

20 @125 studio.fauna_sense_status.operational_radius: 400m -> 600m
# cross-facet: tens=2 @125; operational-radius advancement is persistent and irreversible within the episode;
# @125 is the beat where the Red Keep (400m beyond ceiling) comes into bearing — the radius ceiling is confirmed here

# ---
# SCENE: elder's account / middleman dispatch (@136–@143)
# Tens cluster: @138=2, @139=3 (structural climax — three axes: stakes-visibility + reversal-proximity + body-charge),
# @140=2, @143=2
# ---

21 @138 oc-elder-account.physical_condition: blank -> written

22 @139 oc-elder-account.seal-condition: unsealed -> sealed
# cross-facet: tens=3 @139, three-axis climax; sealing is irreversible; institutional state-change on village-claim axis

23 @140 oc-elder-account.holder: oc-tanner-elder -> middleman

# ---
# SCENE: perimeter circuit / transit (@148–@161)
# Studio location transitions: Taylor exits and re-enters loc-flea-bottom-base
# ---

24 @148 studio.active_location: loc-flea-bottom-base -> in-transit

25 @161 studio.active_location: in-transit -> loc-flea-bottom-base

# ---
# SCENE: denouement log entries (@162–@165)
# Tens cluster: @162=3 (reversal-proximity + body-charge, denouement registration), @163=1, @164=1, @165=1
# ---

26 @163 oc-taylor-log.physical_condition: closed -> open

27 @165 oc-taylor-log.physical_condition: open -> closed

# source: oc-broken-maester
# source: state-updates-oc-broken-maester

facet: state-updates
episode: s01e03
target-scope: actor:oc-broken-maester
author: dialogue-writer-fork:oc-broken-maester
---

# Per-character slice. Single-pass author + cull complete.
#
# Floor-defense note: oc-broken-maester is sparse on-stage in s01e03 outside the closing
# log-construction beat. The on-stage cluster (@73-90: market trip, return, pen-set)
# consists of micro-position transitions within the eastern-quarter location anchor and a
# terminal motor event at @90 (pen-set, tens 3).
#
# Prior-pass culls (this pass):
#
# - CULL @74 location: upper-room-above-apothecary -> eastern-quarter-street. Authority
#   mismatch + transient. The actor's state.md `location` field carries the location-card
#   slug (loc-eastern-quarter-apothecary), not sub-position labels. The eastern-quarter-
#   street sub-position is studio's spatial_layout, not actor:slug.location. Reality check
#   compounds: the card-slug doesn't change across the market trip — he stays in the
#   eastern quarter complex throughout. Persistence test REJECT: reverts at @88, ~14
#   beats later. Anti-pattern #8 (transient-posture as state) + authority cross-license.
#
# - CULL @88 location: eastern-quarter-street -> upper-room-above-apothecary. Same
#   issue: paired revert beat with @74 cull above. Authority + transience.
#
# - REANCHOR documentation_status flip from @90 to @164. Per the brief: "ambient signal
#   (e02) to formal log-entry register (e03 close: 'two log entries written side-by-
#   side')". The "two log entries written side-by-side" is Taylor's log pairing the
#   maester's anomaly with the Hightower file at season terminus. The maester's own pen-
#   activity at @90 closes one writing session in his own records — but his records have
#   always been formal log entries (stm: "Keeps active records of everything he observes;
#   thirty years of such records"), so the "ambient -> formal" delta does not describe
#   his own register at all; it describes how this character exists in the protagonist's
#   record. The flip-beat is the writing beat at @164, not the pen-set at @90. Anti-
#   pattern #7 (pre-empting / lagging) honored — fire on the flip-beat where the field
#   actually mutates.
#
# Skips with floor defense:
#
# - @90 pen-set: tens 3 beat. Posture (`actor:oc-broken-maester.posture: writing ->
#   pen-set-down`) would be transient — no subsequent maester move within e03 for the
#   posture to load-bear into. Anti-pattern #8 (posture-as-state requires multi-beat
#   persistence AND load-bearing). A `stats.record_anomaly_logged` flip is unavailable —
#   the stat is already true at e03 open. A per-session entry counter would be a field-
#   extension too granular to defend. The 3-rating earns tensometer co-citation and
#   narrator-interest fire on Taylor's side (the pen-scratch she hears); no maester-
#   actor-state delta. Refusal-CORRECT per ceiling-defense.
#
# - @73, @75, @77-78, @83-88: sub-position walks (descend stair, alley, market, stall,
#   ascend stair, upper room). Studio's spatial_layout authority. No maester actor-state
#   field flips.
#
# - awareness_of_taylor stays `low` through e03 per card hard fence 2 ("He does not know
#   what Taylor is") + stm ("Has not yet correlated the insect anomaly with the Flea
#   Bottom girl"). No delta.
#
# - Upper-room surveillance condition: per card §"Through-wall observation (load-
#   bearing)", Taylor's insect network has been reaching his upper room from story open.
#   The e03 density-up (beetles relay pen-scratch at @89) is a studio fauna_sense_status
#   delta on the network's coverage of him, not a condition delta on the maester actor
#   target. Register-shift, not state-change.
#
# - Brake-position structural state: "still un-heard" per the brief and card hard fence 4
#   ("Nothing he says lands until too late"). No delta in e03.
#
# Single fire below: the brief's explicitly-flagged meaningful delta — the crossing from
# ambient signal (e02) to formal log-entry register at e03 close.

28 @164 actor:taylor-hebert-flea-bottom.knowledge.maester-in-log: unknown -> named-in-log-paired-with-hightower-file
# field-extension: knowledge.maester-in-log (Taylor's epistemic act — she writes the maester's anomaly into her log at @164 and pairs it with the Hightower file; the state mutation is on Taylor's knowledge, not on the maester's own actor state; the maester remains unaware; moved from oc-broken-maester.documentation_status per worm-canon cross-POV-authority callout — the delta belongs on the POV actor who performed the act)
# cross-facet: tensometer @164 reads 1 in the per-episode file (settling beat; season's reader-asymmetry committed at @162 tens:3); fire on the flip-beat where Taylor writes the entry (@164), not the decision beat (@162) per anti-pattern #7

# source: oc-tanner-elder
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

29 @67 actor:oc-tanner-elder.stance-toward-taylor: conditional-embed-on-trade-reference -> conditional-embed-plus-paid-information-relay
# field-extension: stance-toward-taylor (relationship-role on elder's state schema; tracks the structural stance, not emotional register — card hard-fence on no-warmth preserved; the new value is bureaucratic/transactional, not affective).
# axis: Reality — coin-placement at @67 is the observable, irreversible act ("oc-tanner-elder places the coin"); the wasps @60-@61 already relayed Taylor's dock-side outcome back to the elder, so the coin formalizes a paid-relay relationship beyond the labor-web embed. Persistence: holds forward (informs @103 elder-relays-back, @138 elder-writes-account drawing in part on Taylor's relay-product). Strip-test: without entry, the field reverts to trade-reference-only and the elder's @138 account composition is unmotivated.
# axis: Authority — elder fork on elder field; field-extension licit (relationship-role is tracked structural state, not perception). Card §"Description" establishes "trade-reference" baseline; the extension captures the formalization.
# axis: Frugality — old matches card baseline (conditional embedder on trade-reference); new is a single discrete field-shift, not a compound. Coin-as-prop is studio's authority and not co-written here.
# cross-facet: tens@67=3 (per tensometer.md axis citation summary: "@394: stakes-visibility + reversal-proximity peaks — elder places coin; irreversible registration"). State-update co-citation strongly expected at tens-3 irreversible-registration class — provided. Non-POV actor: narrator-interest co-citation not required.

30 @129 actor:oc-tanner-elder.knowledge.hightower-file-channel: none -> senior-operative-formal-written-request-received
# field-extension: knowledge.hightower-file-channel (knowledge field; canonical analog to actor:taylor.knowledge.record-state in s01e01 rubric anchors). Tracks elder's awareness that an upstream channel above clerk-tier has opened on his placement.
# axis: Reality — messenger delivers the senior-operative's formal written request at @129 ("the messenger speaks to oc-tanner-elder"); the request artifact itself is the content the messenger speaks of — written-form is what the messenger conveys (vs. @5's bare clerk-speech which has no specified artifact). Persistence: drives @137 entry-to-writing-room and @138 composition; without this knowledge, the elder has no addressee for the @138 account. Strip-test: load-bearing for the entire @136-@141 sequence.
# axis: Authority — elder fork on elder knowledge field; field-extension licit (knowledge is the rubric's named tracked-state aspect). Card §"Description" + ltm establish no prior Hightower-channel awareness (elder operates on broker-cut economics, not aristocratic-channel knowledge); new value is a specific, named channel.
# axis: Frugality — old=none (verified against ltm/stm/card); new is a single discrete field-shift. The "formal written request" qualifier is load-bearing (distinguishes this from the clerk-tier @5 touch); not redundant with @67 (stance) or @139 (record-status) — knowledge of the channel is distinct from operational engagement with it.
# cross-facet: tens@129=2 (irreversible knowledge acquisition; messenger delivery cannot be unheard). Non-POV actor: narrator-interest co-citation not required.

31 @137 actor:oc-tanner-elder.location: market-side-junction -> writing-room
# field-extension: sub-location within loc-flea-bottom. Card §state.md baseline is loc-flea-bottom; the writing-room is a discrete operational sub-location load-bearing for the @138-@139 commit sequence. Default location-after-episode reverts to loc-flea-bottom unless next episode opens with elder elsewhere (handled at showrunner write-back).
# axis: Reality — discrete persistent position change ("oc-tanner-elder enters the writing room"); persists @137-@141 minimum (composition + sealing + handoff to middleman). Load-bearing for @138 + @139. Strip-test: without entry, the sealing at @139 has no scene-location-of-record. Fire-beat is @137 (entry), not @136 (exit) per @57 edric-precedent.
# axis: Authority — elder fork on elder location field; sub-location extension is licit-per-rubric (the writing-room is a recurrent operational space for the broker class; not invented for this episode).
# axis: Frugality — old=market-side-junction (recurrent location across episode: @4-@10 first-clerk scene, @96-@101 father scene, @127-@132 messenger scene); new=writing-room. One entry, one field. No co-fire on door-state or junction-roster (those are studio).
# cross-facet: tens@137=1 (low-rung position transition, but discrete and load-bearing for the climax @139). Non-POV actor: narrator-interest co-citation not required.

32 @139 actor:oc-tanner-elder.formal-record-status: not-on-record-channel -> sealed-account-relayed-up-hightower-channel
# field-extension: formal-record-status (tracked-state aspect; parallel to actor:taylor.administrative-status in s01e01 rubric anchors). Tracks elder's structural position relative to upstream file-channels.
# axis: Reality — irreversible sealing of the written account at @139 ("oc-tanner-elder seals the account"). Sealing is the commit-act: ink dries, seal sets, account cannot be retracted from the channel once handed to the middleman at @140. Persistence: permanent (the account exists in the Hightower channel from this beat forward; downstream-episode-load-bearing). Strip-test: without entry, the elder's structural shift from passive placement-broker to active upstream-reporter is unrecorded; the season's third-act architecture-change is missing canonical anchoring.
# axis: Authority — elder fork on elder field; field-extension licit (record-status is the canonical extension type per rubric §calibration anchors). Old=not-on-record-channel (verified: no prior formal-record relationship to any aristocratic channel in card/ltm/stm); new=specific channel and artifact.
# axis: Frugality — old=baseline-none; new is a single discrete field-shift. Stance-toward-taylor at this beat would be a compound second-fire — collapsed (the sealing operationalizes the @67 stance; the operational shift is one delta, not two). Prop:account.seal-condition is studio's authority and fires separately (no overlap).
# cross-facet: tens@139=3 (structural climax of episode per tensometer.md: "@468: three axes light (stakes-visibility + reversal-proximity + body-charge) — elder seals account; structural climax"). State-update co-citation STRONGLY expected at tens-3 irreversible-registration class — provided. Non-POV actor: narrator-interest co-citation not required (Taylor does not perceive the sealing directly; flies-relay at @142 mediates her perception but the canonical state lives on the elder, not on Taylor's knowledge).

# source: oc-tanner-father
# source: state-updates-oc-tanner-father

facet: state-updates
episode: s01e03
target-scope: actor:oc-tanner-father
author: dialogue-writer-fork:oc-tanner-father
---

33 @96 actor:oc-tanner-father.location: loc-tanner-village -> market-side-junction
34 @98 actor:oc-tanner-father.claim-status: informal-private -> customary-wage-claim-registered-with-elder  # field-extension: claim-status (new field for s01e03 village-claim formalization tracking; tracked-state aspect per card §"claim-formality escalation")
35 @101 actor:oc-tanner-father.location: market-side-junction -> loc-tanner-village-returning

# source: taylor-hebert-flea-bottom
# source: state-updates-taylor-hebert-flea-bottom

36 @8 actor:taylor-hebert-flea-bottom.knowledge.first-clerk-record: unknown -> recorded-at-elder
37 @11 actor:taylor-hebert-flea-bottom.knowledge.first-clerk-record: recorded-at-elder -> file-crossed-fish-gate-beyond-range
# 38 deleted — log_entries_episode counter chain removed per cape-fic density-on-flat callout (11 counter entries deleted; cascade: [state:38] removed from proto-line @15)
39 @22 actor:taylor-hebert-flea-bottom.stats.fauna_control_radius_m: 300 -> 400
40 @22 actor:taylor-hebert-flea-bottom.swarm_network_composition: single-species-local -> multi-species-coordinated-flies-wasps-beetles-spiders
# 41 deleted — log_entries_episode counter, cascade: [state:41] removed from proto-line @24
42 @26 actor:taylor-hebert-flea-bottom.physical_condition: intact -> sleep-cycled-night-one
# 43 deleted — log_entries_episode counter, cascade: [state:43] removed from proto-line @30
44 @40 actor:taylor-hebert-flea-bottom.knowledge.second-clerk-record: unknown -> recorded-at-apothecary
45 @42 actor:taylor-hebert-flea-bottom.knowledge.second-clerk-record: recorded-at-apothecary -> entry-sealed-irreversible
# 46 deleted — log_entries_episode counter, cascade: [state:46] removed from proto-line @47
47 @67 actor:taylor-hebert-flea-bottom.inventory: [] -> [coin-from-elder]
# 48 deleted — log_entries_episode counter, cascade: [state:48] removed from proto-line @70
# 49 deleted — log_entries_episode counter, cascade: [state:49] removed from proto-line @93
50 @103 actor:taylor-hebert-flea-bottom.knowledge.father-petitioned-elder: unknown -> known-via-elder
# 51 deleted — log_entries_episode counter, cascade: [state:51] removed from proto-line @107
52 @114 actor:taylor-hebert-flea-bottom.stats.fauna_control_radius_m: 400 -> 500
# 53 deleted — log_entries_episode counter, cascade: [state:53] removed from proto-line @116
54 @118 actor:taylor-hebert-flea-bottom.physical_condition: sleep-cycled-night-one -> sleep-cycled-night-two
# 55 deleted — log_entries_episode counter, cascade: [state:55] removed from proto-line @123
56 @125 actor:taylor-hebert-flea-bottom.knowledge.red-keep-beyond-ceiling: unknown -> known-400m-beyond-current-radius
57 @133 actor:taylor-hebert-flea-bottom.knowledge.messenger-to-elder: unknown -> messenger-observed-at-junction
58 @142 actor:taylor-hebert-flea-bottom.knowledge.formal-account-sealed: unknown -> sealed-and-handed-to-middleman
# 59 deleted — log_entries_episode counter, cascade: [state:59] removed from proto-line @145
60 @155 actor:taylor-hebert-flea-bottom.stats.fauna_control_radius_m: 500 -> 600
61 @162 actor:taylor-hebert-flea-bottom.knowledge.record-discipline-state: parallel-logs-honest -> close-states-recorded-without-cause-assigned
# 62 deleted — log_entries_episode counter, cascade: [state:62] removed from proto-line @164

# field-extension: knowledge.first-clerk-record (per-episode awareness field tracking the first Hightower clerk's record event and its disposition; persistent past beat — Taylor carries the knowledge forward)
# field-extension: knowledge.second-clerk-record (parallel field for second clerk at apothecary)
# field-extension: knowledge.father-petitioned-elder (awareness of family-side pressure routed through elder)
# field-extension: knowledge.red-keep-beyond-ceiling (geographic awareness: at 500m she can register the Red Keep as 400m beyond reach)
# field-extension: knowledge.messenger-to-elder (Hightower-side senior-operative trace)
# field-extension: knowledge.formal-account-sealed (written request by elder to Hightower apparatus has departed via middleman)
# field-extension: knowledge.record-discipline-state (her own log-discipline state — flips at @162 wall-facing, the denouement commitment to record close-states as coincidence; baseline parallel-logs-honest established at project-setup)
# field-extension: log_entries_episode (per-episode log counter; resets at episode open, tracks per-beat log writes)
# field-extension: swarm_network_composition (deployment composition of insect network; flips at @22 when the coordinated multi-species sweep is established)
