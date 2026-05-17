# slice file — facet: state-updates-env  episode: s01e01  author: studio  scope: environmental + location + prop (actor state excluded — per-character forks)
# The consolidated state-updates.md carries the single top-level frontmatter for downstream tooling per r3-signal-001. Plain comments here so the consolidator does not stack YAML blocks.

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
