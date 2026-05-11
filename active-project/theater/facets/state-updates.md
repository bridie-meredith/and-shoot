# source: env
facet: state-updates-env
episode: s01e01
author: studio
scope: environmental + location + prop (actor state excluded — per-character forks)
---

# State-Updates — Environmental Scope

## loc-card field legend
- studio.active_location — current active location-card in scope
- studio.doors_and_shutters — door/gate open/closed state
- studio.fauna_sense_status — insect/animal network positional coverage per species
- studio.ambient — ambient actor presence and conditions
- prop:oc-travel-pack — project-original prop (no warehouse card; oc-* extension, flagged below)

---

1 @15 studio.doors_and_shutters.tanner-room-door: closed -> open
# tens:1(@15)=3, reversal-proximity peak — door-swing ruptures father-Taylor standoff

2 @26 studio.fauna_sense_status.flies: none -> tanner-yard-perimeter
# first-touch establishment: flies spread and cover yard perimeter (persistent through tanner-setting; re-established at @99)

3 @27 studio.fauna_sense_status.beetles: none -> tanner-yard-wall
# first-touch establishment: beetles cover yard-wall (persistent through tanner-setting; re-established at @100)

4 @29 studio.fauna_sense_status.wasps: none -> tanner-south-wall
# first-touch establishment: wasps position at south-wall as relay-infrastructure (verb is relay but function is positional; persistent through tanner-setting; re-established at @101)

5 @91 prop:oc-travel-pack.position: stored-tanner-home -> carried-by-taylor
# field-extension: oc-travel-pack has no warehouse card; project-original prop established here as the named prop the tanner-elder routes Taylor with; extension licit under field-extension protocol (prop is tracked-state, not perception)
# tens entry @91 = 1; genuine prop-state change, persistence confirmed to @104

6 @98 studio.active_location: uncarded-tanner-setting -> loc-flea-bottom
# first carded location arrival; prior state = tanner-village (no loc card; noted as uncarded baseline)
# loc-flea-bottom.card.md present in active-project/warehouse/

7 @99 studio.fauna_sense_status.flies: tanner-yard-perimeter -> immediate-block
# network re-establishment in loc-flea-bottom; species coverage resets to new location

8 @100 studio.fauna_sense_status.beetles: tanner-yard-wall -> market-side-junction
# network re-establishment in loc-flea-bottom; beetles cover market-side junction

9 @101 studio.fauna_sense_status.wasps: tanner-south-wall -> Fish-Gate-margin
# network re-establishment in loc-flea-bottom; wasps cover Fish Gate margin

10 @103 studio.active_location: loc-flea-bottom -> loc-flea-bottom-base
# Taylor enters her lodging; persistent for remainder of episode
# loc-flea-bottom-base.card.md present in active-project/warehouse/

11 @104 prop:oc-travel-pack.position: carried-by-taylor -> set-at-loc-flea-bottom-base
# same oc-* extension as entry 5; pack set down at base; persistent for remainder of episode
# tens entry @104 = 1; prop state change confirmed

12 @110 studio.fauna_sense_status.beetles: market-side-junction -> market-side-junction+eastern-quarter-approach
# additive expansion — beetles extend coverage without vacating market-side junction

13 @112 studio.fauna_sense_status.spiders: none -> ceiling-corners
# first-touch establishment for spiders at loc-flea-bottom-base; persistent, used at @124 relay

14 @134 studio.fauna_sense_status.beetles: market-side-junction+eastern-quarter-approach -> silent
# tens entry @134 (@518 aggregate) = 3, reversal-proximity peak — sustained surveillance plateau collapses into discrete absence; the laugh's effect registers through the network's silence
# cross-facet: strongly expected co-citation at this tens=3 beat (W1-Scene-L rupture)

15 @139 studio.ambient.watch-patrol-presence: absent -> Fish-Gate-margin
# field-extension: watch-patrol-presence added to studio.ambient (new field; not currently tracked); extension licit — this is a tracked-state-aspect (positional) not a perception; Watch patrol presence directly drives dock-runner evasion at @143-@144
# tens entry @139 = 2; persistent through the dock-runner interaction sequence (@139-@146)

---

## Relay beats — NONE (explicit refusals)

@111 the flies relay the doorframe — NONE. Flies already at immediate-block; relay is transient data-transmission, not positional change. anti-pattern #9 (density-on-flat) if fired.
@115 the beetles relay the sound — NONE. Beetles already covering; relay transient.
@121 the flies relay the Fish Gate margin — NONE. Flies coverage established at @99; relay is communication, not positional delta.
@122 the beetles relay the market-side junction — NONE. Coverage established at @100.
@123 the wasps relay the south-wall colony — NONE. Coverage established at @101.
@124 the spiders relay the room — NONE. Coverage established at @112.
@131 the beetles relay the south-wall footfall — NONE. Relay transient.
@140 the flies relay the Watch position — NONE. Flies coverage established; relay transient.
@142 the flies relay oc-dock-runner — NONE. Relay transient.
@146 the flies relay oc-dock-runner — NONE. Relay transient.

## Door state — open-through-episode note

studio.doors_and_shutters.tanner-room-door opened at @15. No subsequent beat closes it in this episode (father exits through yard @19; mother re-enters room @36 — door already open). State persists at open through end of tanner-setting. Not re-tracked after Taylor departs at @94 (no further reference to tanner-room-door).

## Field-extension summary

- prop:oc-travel-pack — project-original prop; no warehouse card; extension licit per rubric §Field-extension protocol. Recommend margit referral for warehouse card authoring between episodes.
- studio.ambient.watch-patrol-presence — new subfield on studio.ambient; tracks named external actor-group positional presence when it constitutes a persistent ambient hazard condition. Distinct from actor-state (Watch patrol has no per-actor fork). Licit extension.

---

## Curve-shape self-check

- Total entries: 15
- Total proto-lines: ~155 (non-blank)
- Fire rate: ~9.7% — within 8–18% band
- Target diversity: studio.active_location (2), studio.doors_and_shutters (1), studio.fauna_sense_status (8), studio.ambient (1), prop:oc-travel-pack (2) — five field-families across two target classes (studio + prop). Target diversity: PASS
- Density alignment: fires cluster around location transitions (@98, @103), network-establishment zones (@26-29, @99-101, @110-113), and the tens=3 peak (@134). Approach zone @1-24 is nearly silent (one door-state fire on the tens=3 rupture only). Ratio check: fires-per-beat in non-1 zones materially exceeds 1-only zones. PASS
- No actor:* entries authored (scope restriction honored)
- No narrator-interest co-citation required (studio.* and prop:* entries; no actor:POV entries)

# source: oc-broken-maester
facet: state-updates
episode: s01e01
author: dialogue-writer-fork:oc-broken-maester
target-scope: actor:oc-broken-maester
---

# (no entries)

# Authoring notes — SKIP-CORRECT for all maester-anchored beats
#
# oc-broken-maester proto-line anchors in s01e01: @114, @129, @130, @133.
# Per rubric § Reality / Anti-pattern #1 (registration-as-state) and
# Anti-pattern #10 (stylistic noting), none of these beats carry a
# persistent mutation of a tracked field on the maester's state schema
# (location / condition / inventory / stats{awareness_of_taylor,
# record_current_year, record_anomaly_logged}).
#
# - @114 "the maester speaks to the room" — verbalization. No field flips.
#   Speech is not a tracked state. SKIP-CORRECT.
# - @129 "the maester crosses the room" — intra-location position shift
#   inside his upper apothecary room. His tracked `location` field stays
#   at loc-eastern-quarter-apothecary across the beat; no sub-position
#   field exists on his state schema and the shift fails the persistence
#   test (no load-bearing persistent orientation past the beat). Refusing
#   field-extension per the conservative-move clause; this is a transient,
#   not a tracked-state aspect. SKIP-CORRECT.
# - @130 "oc-broken-maester speaks to the room" — verbalization. No field
#   flips. The maester does not know Taylor is the listener and does not
#   correlate her to the insect anomaly (STM: "Has not yet correlated the
#   insect anomaly with the Flea Bottom girl"). `awareness_of_taylor`
#   stays at `low`. SKIP-CORRECT.
# - @133 "the maester laughs" — momentary motor event (rubric § Reality
#   REJECT-signature "stylistic noting" / "transient-posture"). Tensometer
#   reads the rupture through the network's response at @134 (`the beetles
#   fall silent`, ID 518 upstream) — that rupture is the *insect-network's*
#   absence-act and routes to studio / non-maester targets, not to the
#   maester's canonical state. The laugh itself does not persistently flip
#   any maester-field. SKIP-CORRECT.
#
# No `awareness_of_taylor: low -> *` fire in this episode: the maester's
# correlation of insect-anomaly to Taylor is structurally deferred past
# s01e01 (card § "Nothing he says lands until too late"; STM "has not yet
# correlated"). Firing here would pre-empt the season arc.
#
# No `record_anomaly_logged: false -> true` fire: per STM the anomaly is
# already logged at episode open ("Has been aware of unusual insect
# behavior in his upper rooms for some weeks; noted in records"). First-
# touch baseline is already `true`; no flip.
#
# No `location: * -> *` fire: maester remains at
# loc-eastern-quarter-apothecary throughout the episode (he never exits
# the room in the proto-line file; the room is established as his upper
# room of the apothecary).
#
# Cross-facet check: tensometer cluster at proto-lines @129-@134 carries
# rungs 2/2/3/2/2/1 with rupture at upstream ID 518 (`the beetles fall
# silent`) — that rupture is honored by studio's fauna_sense_status /
# insect-network state, not by maester-actor state. No @64-class strong-
# expect on oc-broken-maester in this episode. Cross-facet contract
# satisfied with zero fires.

# entries: 0
# pre-cull authored: 0
# cull deletions: 0
# seams flagged: none (see authoring notes)

# source: oc-dock-runner
facet: state-updates
episode: s01e01
target-class: actor:oc-dock-runner
author: dialogue-writer-fork:oc-dock-runner (R1)
---

16 @141 actor:oc-dock-runner.position: loc-flea-bottom -> fish-gate-margin
17 @144 actor:oc-dock-runner.position: fish-gate-margin -> loc-flea-bottom
18 @149 actor:oc-dock-runner.position: loc-flea-bottom -> market-side-junction
19 @155 actor:oc-dock-runner.position: market-side-junction -> loc-flea-bottom

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

# source: oc-tanner-elder
facet: state-updates
episode: s01e01
author: dialogue-writer-fork-oc-tanner-elder
scope: actor:oc-tanner-elder
---

20 @85 actor:oc-tanner-elder.location: loc-flea-bottom -> tanner-family-yard
21 @95 actor:oc-tanner-elder.location: tanner-family-yard -> on-road-to-flea-bottom
22 @148 actor:oc-tanner-elder.location: on-road-to-flea-bottom -> flea-bottom-market-side-junction

# Seam: the elder's position flips happen off-screen. He travels from Flea Bottom (state.md baseline) to the tanner village before @85; from village to road at the gate-cross (Taylor's @94, no elder-subject beat); from road to KL market-side junction between @96 and @148. Each entry fires on the first observable beat that confirms the new location, not the literal flip-beat. Flagged for cross-facet review with studio (location-state) and potentially with the dialogue-writer for Taylor (whose @94 "crosses the yard gate" is the only on-stage gate-cross). If studio's location-state file carries an elder co-location entry at any of these beats, alignment is required.

# Reality: all three are persistent location flips, not transient postures. Elder remains at each new location across multiple subsequent beats (in-yard @85-@94; on-road @95-@96; market-side @148-@155).
# Authority: elder fork writes actor:oc-tanner-elder.location. Field is on state.md schema.
# Frugality: <old> for entry 1 matches state.md baseline (loc-flea-bottom). Each <new> chains correctly to the next <old>.
# Cross-facet: tens=3 at @90 (routing) and @151 (Taylor speaks back) do NOT fire state-updates on the elder — the routing-act at @90 enacts a pre-committed placement (no elder-side field flip; placement is already in STM as historical), and @151 is Taylor's irreversible commit not the elder's.
# Skips: @86 (speaks-to, no field change), @88 (Taylor subject, no elder change), @90 (routes-Taylor enacts pre-committed placement; no elder-side field flip; tens=3 but consumer-side validator @64-class does not apply — this is not a registration of an irreversible record-mutation against the elder), @96 (durative motion, location already flipped at @95), @148 dual-fire risk: @148 is elder-subject "speaks to dock-runner" which is the first observable beat at market-side; the location-flip is anchored here; the speech-verb itself does not change location. @150 (dock-runner speaks to elder), @151 (elder speaks to Taylor) — same location as @148, no further flips.

# source: oc-tanner-father
facet: state-updates
episode: s01e01
target-scope: actor:oc-tanner-father
author: dialogue-writer-fork:oc-tanner-father
---

23 @4 actor:oc-tanner-father.location-sub: outside-tanner-room -> tanner-room
# field-extension: location-sub (room/yard sub-granularity within loc-tanner-village; load-bearing for Scene A standoff geometry and Scene D yard reentry)
24 @19 actor:oc-tanner-father.location-sub: tanner-room -> tanner-yard
# persistent through episode close; load-bearing for Scenes E/F/G/H (reeve interaction, task-routing, Taylor's departure)

# source: oc-tanner-mother
facet: state-updates
episode: s01e01
character: oc-tanner-mother
author: dialogue-writer-fork:oc-tanner-mother
scope: actor:oc-tanner-mother.* only
---

25 @5 actor:oc-tanner-mother.position: elsewhere-in-cottage -> in-the-room
26 @36 actor:oc-tanner-mother.position: elsewhere-in-cottage -> in-the-room
27 @46 actor:oc-tanner-mother.position: in-the-room -> elsewhere-in-cottage

# field-extension: position (sub-location within loc-tanner-village cottage — new field for s01e01 cottage-room blocking; tracked-state aspect, not perception; persistence verified across the room/exit chain at bones 5-46)

# Seams flagged for cross-facet review:
# - Offstage exit between @6 and @36. Mother enters at @5, sets bowl at @6, is on-stage facing the door at @18, then off-bone until @36 re-entrance. No proto-line records her exit between @19 (father exits the yard) and @36 (afternoon re-entrance). Entry 2's old=elsewhere-in-cottage assumes an offstage exit during the @24/@35 time-skips. The position chain is consistent under that assumption. If cross-facet review requires an on-bone exit, that is a screen-writer kickback (missing exit-bone), not a state-update authoring fault.
# - @18 (faces the door), @45 (faces the wall), @92 (faces the door): NONE — transient orientation, resolves within adjacent beats; anti-pattern #8 (posture-as-state). The persistence test fails: orientation does not carry load past the immediate beat-cluster.
# - @6 (sets the morning bowl), @37 (sets the afternoon bowl), @44 (sets the bowl): NONE on actor:oc-tanner-mother. Bowl-as-prop is studio's domain (prop:* target, holder field). Transient mother-as-carrier hand-state is not a tracked actor-state field on her card; firing inventory here would be anti-pattern #10 (stylistic) on the actor side. Cross-author dependency: studio fork is expected to write prop:*.holder for these beats.
# - @38-@41 (opens the mouth, sings notes 1-3): NONE — singing is a behavioral act, not a tracked-field mutation; voice/song-state is not on her schema. Anti-pattern #1 (registration-as-state) if forced.
# - @43 (drops the song) — tens=3 reversal-proximity peak. NONE-CONFIRMED. The song-test is the mother's deliberate Tya-probe; Taylor's non-response is registered by the mother as evidence. Hard fence #1 on her card ("She does not resolve. The ambiguity is permanent.") forbids a knowledge-state flip to resolved/confirmed. Accumulation-of-evidence as a tracked field would be anti-pattern #10 (stylistic) AND would soft-violate the fence. Narrator-interest (Taylor's POV) may register the mother's affect; the mother's own canonical state stays silent. Refusal-CORRECT. Cross-facet note: tens=3 here is registration-class for the mother (the cessation IS the reversal, but the reversal lives in Taylor's reading, not in a mother-state mutation). The tensometer locked file lists @43 as reversal-proximity peak — state-updates honors the @64-style co-citation expectation only where a tracked field on the mother actually flips, which here it does not.
# - @92 (faces the door at Taylor's departure with the elder): NONE — transient orientation; witnessing Taylor's gate-crossing is perception, not a tracked mother-state field. Hard fence #3 ("She does not ask Taylor to explain") reinforces silence here — her witnessing does not commit to a posture-state-shift.

# source: taylor-hebert-flea-bottom
facet: state-updates
episode: s01e01
author: dialogue-writer-fork-taylor-hebert-flea-bottom
target-class: actor:taylor-hebert-flea-bottom
---

28 @22 actor:taylor-hebert-flea-bottom.research_log_active: false -> true
# field flips at first log-write (@22); persists through episode close (every subsequent log open/write/close beat depends on log being active). @21 is open-without-content; the entry-write at @22 is the flip-beat (anti-pattern #7 avoidance).
29 @90 actor:taylor-hebert-flea-bottom.placement-status: tanner-village-ward -> flea-bottom-placed
# field-extension: placement-status (new field for s01e01 — tracks Taylor's village→KL administrative placement by the elder). Subject of @90 is the elder; field on Taylor flips per @48-anchor precedent (other-subject acts on Taylor's tracked field). Tens@90=3 reversal-proximity (the routing itself is the irreversible turn). Persistence: she does not return to the village.
30 @91 actor:taylor-hebert-flea-bottom.inventory: [] -> [travel-pack]
# inventory acquires travel-pack; persists @91 through @104 setting-down. Anchor verb `lifts` is the flip-beat.
31 @98 actor:taylor-hebert-flea-bottom.location: loc-tanner-village -> loc-flea-bottom
# location field flips at the `enters` verb; transit beats (@94 gate-crossing, @96 road-walking) are non-persistent on this field. Persists until @103 enters-base.
32 @103 actor:taylor-hebert-flea-bottom.location: loc-flea-bottom -> loc-flea-bottom-base
# location field flips at `enters loc-flea-bottom-base`. Persists through episode close (she does not exit the base after @103).
33 @104 actor:taylor-hebert-flea-bottom.inventory: [travel-pack] -> []
# inventory empties at `sets the travel pack`. Persists through episode close — the pack lives at the base.
34 @154 actor:taylor-hebert-flea-bottom.network-anchor: none -> dock-runner-contact-established
# field-extension: network-anchor (new field for s01e01 — tracks Taylor's KL contact network nodes). Anchored on Taylor's speech-back (her irreversible social commit), not on @151 (dock-runner-to-her) or @153 (dock-runner-to-her again). Tens cluster @151=3 reversal-proximity supports the commit-beat fire. Persistence: contact established for downstream s01e02+ network work.
