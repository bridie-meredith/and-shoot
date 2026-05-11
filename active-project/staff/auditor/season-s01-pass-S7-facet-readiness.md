---
report: season-audit-pass-S7-facet-readiness
scope: season
target: s01
pass: S7
timestamp: 2026-05-11
verdict: FACET-GAPS
---

# Season s01 — Pass S7 Facet Readiness Audit

## Scope

Check axes: for each of the 26 content beats traversed by s01.bones.md, verify that citable bones exist for each downstream facet author (location-state, state-updates, tensometer, dialogue, narrator-interest, sensory, feeling, memory-flag, metaphor). Flag over-dense stretches (10+ beats per scene without inflection point) and under-dense stretches (beat with zero supporting bones).

Source files:
- `active-project/theater/proto-lines/s01.bones.md`
- `active-project/staff/showrunner/season-s01-plan.md` (beat definitions)
- `active-project/staff/screen-writer/s01-content-beats-draft.md` (beat prose authority)

---

## Preflight findings

### F-PRE-1 — No facet files exist

**type:** fault

**what:** `active-project/theater/facets/` — none of the expected facet files are present. Not tensometer, location-state, state-updates, feeling, sensory, memory, metaphor, narrator-interest, interest-aud-*, or vibes.

**why:** Pass S7 checks for the existence of citable bones PER FACET AUTHOR — it presupposes that facet authoring is either in progress or that the bones themselves are the seed material. The absence of all facet files is consistent with S7 being a pre-authoring readiness check (facets are authored downstream). This audit therefore evaluates the bones as the raw material facet authors will read, rather than verifying already-authored facets. The verdict is about whether bones supply sufficient anchors — not whether facets have been written.

**criteria:** No fixer action. This is an expected state at S7. Facet authoring has not yet begun. The audit proceeds against bones-as-raw-material.

---

## Beat-by-beat facet readiness review

### Beat 1 — Taylor wakes; father's tell-audit; village category closes (bones 1–23)

**Bones present:** 1 (wakes), 2 (exhales), 3 (straightens spine), 4 (father enters room), 5 (mother enters room), 6 (mother sets morning bowl), 7 (father faces Taylor), 8 (Taylor reaches for salt), 9 (father pivots toward mother), 10 (Taylor draws the salt), 11 (father pivots toward Taylor), 12 (dogs enter yard), 13 (Taylor holds chin), 14 (father stills), 15 (door swings open), 16 (Taylor pivots toward door), 17 (father tilts head), 18 (mother faces door), 19 (father steps toward yard), 20 (Taylor lowers bowl), 21–23 (log open/write/close).

**location-state:** ANCHOR PRESENT. Bones 1–20 physically situate the scene (the room, the morning meal, the yard). Location slug in character name (flea-bottom) does not match — Taylor is still in the tanner-village in beat 1, but the character slug is `taylor-hebert-flea-bottom` throughout. The bones do not carry a location-state anchor (no `loc-tanner-village` reference). The beat-1 location is the tanner-family home. Flag: location-state author will need to infer from context; no explicit loc slug cited in any bone.

**state-updates:** ANCHOR PRESENT. Bones 6 (bowl set), 10 (salt drawn), 12 (dogs enter), 19 (father steps toward yard), 20 (bowl lowered) are physical state-change events. Adequate.

**tensometer:** ANCHOR PRESENT. Bones 7/8/9/10/11 (father's tell-audit sequence), 12 (dogs enter — tell-moment), 13 (Taylor holds chin — body-charge anchor), 14 (father stills — rupture-proximity). Sufficient escalation ladder for dramatist.

**dialogue:** GAP. Beat 1 contains zero `<speaker> speaks to <listener>` bones. The beat as described in the plan is observational — the father is running a behavioral audit, not a dialogue exchange. The plan prose does not mandate spoken dialogue in beat 1, but the bones record no verbal exchange at all across the entire morning meal sequence (bones 1–23). The narrator-interest facet and feeling facets can carry the weight; dialogue facet has no anchor in this beat by design.

**narrator-interest:** ANCHOR PRESENT. Bones 7, 8, 10, 11, 12, 13, 14, 16 are all POV-observable physical events that the narrator can register. Adequate.

**sensory:** ANCHOR PRESENT. Bones 2 (exhale), 6 (bowl set), 12 (dogs enter yard — sound), 15 (door swings open). Multiple modality candidates. Adequate.

**feeling:** ANCHOR PRESENT. Bones 13 (Taylor holds chin — body-charge), 14 (father stills), 7/9/11 (father facing/pivoting — repeated orientation gesture). Adequate somatic-tell anchors for feeling author.

**memory-flag:** ANCHOR PRESENT. Bone 8 (Taylor reaches for salt) is the plan-named tell — the salt-reach without hesitation. Memory-flag author has a specific citable anchor.

**metaphor:** THIN but not absent. No explicit charged-image bones in beat 1; metaphor is refuse-by-default anyway (editor taste call). No gap.

**beat 1 verdict:** READY with one notation: location-state author must infer tanner-village as location; no explicit loc slug in beat 1 bones. Flag below.

---

### Beat 2 — 300m inventory from yard; 300m map; shard running local-only (bones 25–34)

**Bones present:** 25 (Taylor crosses yard), 26 (flies spread yard perimeter), 27 (beetles spread yard-wall), 28 (Taylor walks yard boundary), 29 (wasps relay south-wall return), 30 (Taylor walks yard boundary), 31 (Taylor exhales), 32–34 (log).

**location-state:** ANCHOR PRESENT. Still tanner-village yard. Same location-slug gap as beat 1 (no explicit loc citation).

**state-updates:** THIN. Insects spreading is state-change for the network, but no prop or actor state changes visible. No explicit network-state bone. The "300m inventory" as a state event has no dedicated state bone — the spread/relay pattern is the closest.

**tensometer:** GAP. All 8 non-log bones in beat 2 are ambient (insects spread, Taylor walks boundary, Taylor exhales). No escalation, no charge, no peak. The beat functions as transit/inventory. Tensometer author will assign all 1s, which is correct per rubric — but there is no 2-or-3 anchor anywhere in beat 2. This is a scene-as-transit (legitimate) but the rubric requires dramatist to flag explicitly. Not a fault in bones; flag for dramatist.

**dialogue:** GAP (by design — no dialogue in beat 2 per the plan).

**narrator-interest:** ANCHOR PRESENT. Bone 26/27/29 (insect spread relays) are the POV mechanism for the range inventory. Adequate.

**sensory:** THIN. Bone 31 (exhale) is the only clear sensory inflection. Beat 2 is largely silent perimeter-mapping. Flag: sensory author has minimal material.

**feeling:** ANCHOR PRESENT. Bone 31 (exhale) and 28/30 (Taylor walks boundary — repetitive motion as somatic pattern) give feeling author something to work with.

**memory-flag:** GAP. No memory-flag candidate bones in beat 2. Beat 2 is first-occurrence data; no callback possible yet. Expected absence.

**metaphor:** N/A (no anchor).

**beat 2 verdict:** READY. Tensometer will be all-1 (transit beat). Sensory is thin but within acceptable range for a mapping beat.

---

### Beat 3 — Mother's song; mother's foreclosure (bones 36–46)

**Bones present:** 36 (mother enters room), 37 (mother sets afternoon bowl), 38 (mother opens mouth), 39 (mother sings first note), 40 (mother sings second note), 41 (mother sings third note), 42 (Taylor holds eyes), 43 (mother drops song), 44 (mother sets bowl), 45 (mother faces wall), 46 (mother exits room).

**location-state:** ANCHOR PRESENT. Bones 36/44/46 anchor interior room setting. Same location-slug gap as beats 1–2.

**state-updates:** ANCHOR PRESENT. Bones 37 (bowl set), 43 (song dropped — state change for mother), 46 (mother exits). Adequate.

**tensometer:** ANCHOR PRESENT. Bones 39/40/41 (three notes — escalation ladder), 43 (mother drops song — rupture/peak), 45 (mother faces wall — body-charge post-peak). This is the strongest tensometer ladder in the first cluster of beats. Adequate for a 1→2→2→3→2→1 shape.

**dialogue:** GAP. The three-note sequence is physical action, not `speaks to`. No dialogue bone in beat 3 by design. The beat is gestural/somatic throughout. Dialogue facet has no anchor; narrator-interest and feeling carry it.

**narrator-interest:** ANCHOR PRESENT. Bones 39/40/41/43 (the song sequence) are the POV's primary registration events. Adequate.

**sensory:** STRONG ANCHOR. Bones 39/40/41 are sound-modality events (three notes). This is the clearest sensory anchor in the first cluster. Adequate.

**feeling:** STRONG ANCHOR. Bone 43 (mother drops song) and 45 (mother faces wall) are textbook somatic-tell candidates. Beat 3 is the primary feeling-flag beat in the early cluster.

**memory-flag:** ANCHOR PRESENT. Bone 43 (mother drops song) is a callback anchor — later memory-flags at beats 17 (vigil ends) and 26 (denouement) can cite this moment. Adequate.

**metaphor:** N/A (no licensed anchor yet).

**beat 3 verdict:** FACET-READY. Strongest facet density of the first three beats.

---

### Beat 4 — Father reorders labor; structural withdrawal (bones 48–60)

**Bones present:** 48 (father assigns task), 49 (father routes mother), 50 (father routes neighbor-boy), 51 (Taylor enters yard edge), 52 (father crosses yard), 53 (Taylor lifts feed bucket), 54 (father crosses pit), 55 (Taylor crosses yard perimeter), 56 (father routes mother), 57 (father routes neighbor-boy), 58–60 (Taylor logs).

**location-state:** ANCHOR PRESENT. Yard/pit locations cited in bones 51/52/54/55. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 48/49/50 (routing assignments), 53 (bucket lifted). Adequate.

**tensometer:** ANCHOR PRESENT. The beat is ambient-pressure: father's routing is the tell. Bones 48/49/50 (routing sequence) and 54 (father crosses pit — physical separation) give a 1→1→2→1 shape. Not a peak beat; appropriate for beat 4's function (structural withdrawal, not confrontation).

**dialogue:** GAP. Beat 4 has no `speaks to` bones. The plan describes routing "through routing, not declaration." The absence of dialogue is structurally correct. Dialogue facet has no anchor in beat 4.

**narrator-interest:** ANCHOR PRESENT. Bone 51 (Taylor enters yard edge — the peripheralization) and 53 (Taylor lifts feed bucket) are the POV registration of the structural fact. Adequate.

**sensory:** THIN. No clear sensory inflection bones. Beat 4 is silent (no song, no speech, no acute sound event). Sensory author has minimal material; expected for a transitional/routing beat.

**feeling:** ANCHOR PRESENT. Bone 53 (Taylor lifts bucket — body registering the assignment) and 55 (Taylor crosses perimeter) give feeling author somatic anchors.

**memory-flag:** GAP. No callback candidates in beat 4.

**metaphor:** N/A.

**beat 4 verdict:** READY. Dialogue gap is structurally correct. Sensory thin but expected.

---

### Beat 5 — Lord's man quarterly pass; file opens (bones 62–77)

**Bones present:** 62 (reeve enters yard), 63 (reeve speaks to father), 64 (father speaks to reeve), 65 (Taylor crosses yard), 66 (reeve slows step), 67 (reeve speaks to father), 68 (father speaks to reeve), 69 (reeve exits); 71 (lord's man enters village), 72 (lord's man speaks to reeve), 73 (reeve speaks to lord's man), 74 (lord's man opens record book), 75 (lord's man writes entry), 76 (lord's man closes record book), 77 (lord's man exits).

**location-state:** ANCHOR PRESENT. Bones 62 (reeve enters yard), 65 (Taylor crosses yard), 71 (lord's man enters village). Two distinct micro-locations within beat 5 (yard, then village street). Adequate.

**state-updates:** ANCHOR PRESENT. Bones 74/75/76 (record book opened, written, closed) — this is the canonical state-update for the file-opens event. Adequate.

**tensometer:** ANCHOR PRESENT. Bone 63/64 (reeve speaks to father — exchange at 2), 66 (reeve slows step — body-charge toward Taylor at 2-proximity), 67/68 (second exchange — escalation), 75 (lord's man writes entry — registration peak at 3). The file-opening write is the beat's structural peak. Adequate.

**dialogue:** ANCHOR PRESENT. Bones 63 (reeve speaks to father), 64 (father speaks to reeve), 67 (reeve speaks to father), 68 (father speaks to reeve), 72 (lord's man speaks to reeve), 73 (reeve speaks to lord's man). Multiple dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 65 (Taylor crosses yard — moves through the event), 66 (reeve slows — POV registers the slowdown). The POV is present for part of beat 5; the lord's-man sequence (71–77) is observed through village ambient, not direct POV proximity. This is a POV-observability question the narrator-interest author must resolve.

**sensory:** THIN. No acute sensory events. Beat 5 is procedural (record-keeping). Expected thin.

**feeling:** ANCHOR PRESENT. Bone 66 (reeve slows step — body-charge toward Taylor), 65 (Taylor crosses yard under observation). Adequate.

**memory-flag:** GAP. First occurrence of the lord's-man recording mechanism. No prior callback.

**metaphor:** N/A.

**beat 5 verdict:** READY. Note: bones 71–77 (lord's man sequence) are narrator-distant (POV is not physically present); narrator-interest author should receive a signal that this sub-sequence is observation-via-network rather than direct POV. The bones carry no explicit POV-marker for this transition.

---

### Beat 6 — Taylor chooses KL; tanner-elder routes her; arrival at Flea Bottom base; 300m map in 48 hours (bones 79–92, then 94–103)

**Note:** The season plan places beats 6 and 7 as sequential — beat 6 is the routing and arrival, beat 7 is the first map and catalog. The bones span bones 79 (first log in this cluster) through 103 (log close after setting pack at base). Line 24 is a time-skip marker (blank numbered line). Lines 35, 47, 61, 70, 78, 82 are also time-skip markers.

**Bones present (beat 6):** 79 (Taylor opens log), 80 (Taylor writes), 81 (Taylor closes log); 83 (elder speaks to Taylor), 84 (elder speaks to Taylor — second bone), 85 (Taylor faces elder), 495 (Taylor speaks to elder), 504 (Taylor stills), 86 (elder routes Taylor), 87 (Taylor lifts pack), 88 (mother faces door), 89 (father holds feet), 90 (Taylor crosses gate), 91 (elder walks road), 92 (Taylor walks road); then 94 (Taylor enters flea-bottom), 95 (flies spread immediate block), 96 (beetles spread market-side junction), 97 (wasps spread Fish Gate margin), 98 (Taylor walks alley), 99 (Taylor enters base), 100 (Taylor sets pack), 101–103 (log).

**location-state:** ANCHOR PRESENT. Bone 90 (crosses gate — village exit), 92 (walks road), 94 (enters flea-bottom), 98 (walks alley), 99 (enters base). Three location transitions in beat 6. Adequate.

**state-updates:** ANCHOR PRESENT. Bone 87 (pack lifted), 100 (pack set at base). Actor state changes at both ends of the journey. Adequate.

**tensometer:** ANCHOR PRESENT. Bones 83/84 (elder speaks to Taylor — 1-2), 86 (elder routes Taylor — commitment bone), 90 (Taylor crosses gate — irreversible transition, 2-3 candidate), 504 (Taylor stills — body-charge), 495 (Taylor speaks to elder — dialogue bone). The gate-crossing is the beat's peak.

**dialogue:** ANCHOR PRESENT. Bones 83, 84, 495 (elder speaks to Taylor twice; Taylor speaks to elder). Adequate.

**narrator-interest:** ANCHOR PRESENT. Bones 88 (mother faces door), 89 (father holds feet), 90 (Taylor crosses gate). The departure bones are strong narrator-interest anchors.

**sensory:** ANCHOR PRESENT. Bones 90/92 (crossing the gate, walking the road — transition from village to road is a sensory context shift). 94 (entering flea-bottom — new sensory environment). Adequate.

**feeling:** ANCHOR PRESENT. Bones 89 (father holds feet), 504 (Taylor stills), 88 (mother faces door). Strong somatic-tell pool for the departure sequence.

**memory-flag:** GAP. First occurrence of the routing event.

**metaphor:** N/A.

**beat 6 verdict:** FACET-READY.

---

### Beat 7 — 300m sphere catalog; dark as primary operational fact (bones 105–116)

**Bones present:** 105 (Taylor walks perimeter), 106 (beetles spread eastern-quarter approach), 107 (flies relay doorframe), 108 (spiders spread ceiling corners), 109 (Taylor writes entry), 110 (Taylor walks perimeter), 111 (maester speaks to room), 112 (beetles relay sound), 113 (Taylor writes entry), 114 (Taylor opens log), 115 (Taylor writes entry), 116 (Taylor closes log).

**location-state:** ANCHOR PRESENT. Bones 105/110 (Taylor walks perimeter — flea-bottom-base area). Location established by the preceding bones (99, 99). Adequate.

**state-updates:** THIN. No explicit prop/actor state changes in beat 7 bones. The network spread bones (106-108) are state events for the insect network but no actor or prop state changes occur.

**tensometer:** ANCHOR PRESENT. Bone 111 (maester speaks to room — first maester acoustic register, 2-candidate), 112 (beetles relay sound — relay of the maester event, 1-2). Beat 7 is largely ambient/mapping (1s) with the maester's voice as the single escalation candidate.

**dialogue:** PARTIAL GAP. Bone 111 (`the maester speaks to the room`) is not a `<speaker> speaks to <listener>` dialogue bone — it is ambient speech, no named listener. Per the schema, dialogue bones require `<speaker> speaks to <listener>`. Bone 111 is not a valid dialogue-anchor. Beat 7 has no valid dialogue anchor. The plan describes the maester as "reads aloud while he works" — the bone renders this as ambient, which is correct. Dialogue facet has no anchor in beat 7.

**narrator-interest:** ANCHOR PRESENT. Bone 107 (flies relay doorframe — acoustic detection), 111 (maester speaks to room — the acoustic find), 112 (beetles relay sound). The maester-discovery sequence is the narrator-interest focus of beat 7.

**sensory:** ANCHOR PRESENT. Bone 111 (maester speaks to room — sound modality, acoustic discovery event), 112 (beetles relay sound — sound relay). Sound inflection point. Adequate.

**feeling:** THIN. No strong somatic-tell anchor. Beat 7 is observational. Bone 109/110/113 (Taylor writes, walks, writes) are repetitive motion without a charged somatic moment.

**memory-flag:** GAP. First occurrence.

**metaphor:** N/A.

**beat 7 verdict:** READY. Feeling thin but within acceptable range for a mapping beat. Dialogue absence by design.

---

### Beat 8 — Dock-runner Watch-pattern event; Taylor watches; first transaction (bones 118–155)

**Note:** This beat covers two sub-scenes: (a) the Watch/runner incident observed through the wall (bones 118–143), and (b) the dock-runner approaching through elder for Watch-pattern information (bones 145–155). The time-skip marker at 144 separates them.

**Bones present:** 118 (full perimeter walk), 119–122 (flies/beetles/wasps/spiders relay), 123 (Taylor writes entry), 124–126 (log sequence), then 128 (maester crosses room), 129 (maester speaks — ambient), 130 (beetles relay footfall), 131 (Taylor straightens spine), 506 (maester laughs), 132–134 (log); then 136 (Watch patrol crosses Fish Gate), 137 (flies relay Watch), 138 (dock-runner enters Fish Gate margin), 139 (flies relay runner), 140 (runner pivots), 141 (runner exits), 142 (Taylor holds feet), 143 (flies relay runner); then (after 144 skip) 145 (elder speaks to dock-runner), 146 (runner approaches junction), 147 (runner speaks to elder), 148 (elder speaks to Taylor), 149 (Taylor faces runner), 150 (runner speaks to Taylor), 151 (Taylor speaks to runner), 152 (runner exits), 153–155 (log).

**location-state:** ANCHOR PRESENT. Bones 136 (Watch patrol at Fish Gate margin), 138 (runner enters Fish Gate margin), 146 (runner approaches junction). Two distinct locations cited. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 140/141 (runner pivots, runner exits — state change for runner). The information handoff at 151 is a state event with no explicit state-update bone (the handoff is the `Taylor speaks to runner` bone but no prop/actor-state change bone).

**tensometer:** ANCHOR PRESENT. Bone 136 (Watch patrol — 2), 138 (runner enters — 2), 140 (runner pivots — turn-proximity 2-3), 141 (runner exits — resolution, descent to 1-2), 131 (Taylor straightens spine — body-charge, 2), 506 (maester laughs — release, 1). Second sub-scene: 150 (runner speaks to Taylor — 2), 151 (Taylor speaks to runner — information handoff, 2-3 candidate). Adequate shape.

**dialogue:** ANCHOR PRESENT. Bones 145 (elder speaks to dock-runner), 147 (runner speaks to elder), 148 (elder speaks to Taylor), 150 (runner speaks to Taylor), 151 (Taylor speaks to runner). Five valid dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 137/139/143 (fly relays of Watch and runner), 142 (Taylor holds feet — POV freeze on the event). Strong narrator-interest anchor pool.

**sensory:** ANCHOR PRESENT. Bone 131 (Taylor straightens spine — tactile/body), 506 (maester laughs — sound). Adequate.

**feeling:** ANCHOR PRESENT. Bones 131 (Taylor straightens spine — body-charge), 142 (Taylor holds feet — body-charge under observation). Two feeling-flag candidates in beat 8.

**memory-flag:** GAP. First occurrence of dock-runner and Watch-pattern information exchange.

**metaphor:** N/A.

**beat 8 verdict:** FACET-READY.

---

### Beat 9 — Family visits KL; father spots strategic-scan tell; mother quieter on walk home (bones 157–185)

**Note:** Time-skip markers at 156 and 157/158 (two consecutive empty IDs) precede this beat. Bones 159–181 cover the junction meeting; 183–185 are the log close.

**Bones present:** 159 (father crosses junction), 160 (mother crosses junction), 161 (elder greets father), 162 (elder greets mother), 163 (Taylor approaches junction), 164 (the arrival enters junction), 165 (Taylor pivots toward arrival), 166 (father holds step), 167 (Taylor faces father), 168 (father speaks to Taylor), 169 (Taylor speaks to father), 170 (father stills), 171 (mother stills), 172 (father lifts trade goods), 173 (father speaks to elder), 174 (elder speaks to father), 175 (mother faces Taylor), 176 (mother speaks to Taylor), 177 (Taylor speaks to mother), 178 (mother pivots toward road south), 179 (father pivots toward road south), 180 (father exits junction), 181 (mother exits junction); 183–185 (log).

**location-state:** ANCHOR PRESENT. Bones 159/160/163 (junction). Market-side junction. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 161/162 (greetings — social-network state), 172 (father lifts trade goods). Adequate.

**tensometer:** STRONG ANCHOR. Beat 9 has the clearest tensometer ladder so far. Bones 165 (Taylor pivots toward arrival — body-charge 2), 166 (father holds step — reversal-proximity 2-3), 167 (Taylor faces father — confrontation alignment 2-3), 168/169 (father/Taylor exchange — dialogue on the strategic-scan tell), 170/171 (father stills, mother stills — double-peak registration), 172 (father lifts trade goods — action that deflects the peak), 180/181 (exits — denouement). The double-still at 170/171 is the beat's 3-candidate.

**dialogue:** ANCHOR PRESENT. Bones 161 (elder greets father), 162 (elder greets mother), 168 (father speaks to Taylor), 169 (Taylor speaks to father), 173 (father speaks to elder), 174 (elder speaks to father), 176 (mother speaks to Taylor), 177 (Taylor speaks to mother). Eight dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 164 (the arrival enters junction — the trigger for the strategic-scan tell), 165 (Taylor pivots toward arrival — the tell itself), 166 (father holds step — POV-visible registration of being watched). Strong.

**sensory:** THIN. No acute sensory inflection bones in beat 9. The scene is social/behavioral. Expected thin.

**feeling:** STRONG ANCHOR. Bones 166 (father holds step), 167 (Taylor faces father — confrontation posture), 170 (father stills), 171 (mother stills). Multiple somatic-tell candidates across three characters.

**memory-flag:** ANCHOR PRESENT. Bone 165 (Taylor pivots toward arrival — the strategic-scan) is the anchor for a memory-flag callback to beat 1 (salt-reach without hesitation — the earlier tell). Beat 9 is the second family-audit event; memory-flag author can cite beat 1 bones from this anchor.

**metaphor:** N/A.

**beat 9 verdict:** FACET-READY. Strongest facet density so far in the season.

---

### Beat 10 — Three weeks of whisper-chain mapping; weather data routing; "odd but functional" read (bones 187–207)

**Note:** This is the most bone-sparse beat in the season for a narratively dense content beat. The bones cover: 187 (flies relay junction conversation), 189 (time-skip), 190 (wasps relay Fish Gate margin traffic), 191 (time-skip), 193 (time-skip), 194 (time-skip), 195 (Taylor enters base), 199 (time-skip), 200 (flies relay weather-pattern data), 201–202 (Taylor writes log), 203/204 (time-skips), 500 (Taylor closes log), 508 (elder pauses), 501 (elder speaks to the carter), 502 (wasps relay the pass), 205–207 (Taylor opens/writes/closes log).

**location-state:** THIN. Bone 195 (Taylor enters base) establishes base. Bones 187/190 (flies/wasps relay) are network-position bones but no explicit location citation for the junction or Fish Gate margin as scenes Taylor inhabits. Beat 10's "three weeks of network-ambient listening" is largely rendered through relay bones rather than Taylor physically inhabiting locations.

**state-updates:** ANCHOR PRESENT. Bone 200 (flies relay weather-pattern data — network routing as state event), 501/508 (elder pauses, elder speaks to carter — network social event). The elder's routing action (501) is a state event.

**tensometer:** THIN. Bones in beat 10 are almost all 1s (ambient relay, log writing). Bone 501 (elder speaks to carter — information routing) is a 1-2 candidate at best. No peak in beat 10. This is a transit/mapping beat across three weeks. Dramatist must flag as scene-as-transit. No fault in bones.

**dialogue:** ANCHOR PRESENT. Bone 501 (elder speaks to the carter) is a valid dialogue anchor. One anchor total — thin but present.

**narrator-interest:** ANCHOR PRESENT. Bones 187/190/200/502 (relays) are the POV's network-ambient data. Adequate.

**sensory:** THIN. Bone 200 (weather-pattern data — possibly thermal/humidity signal) is the only candidate. Sensory author has minimal material in beat 10.

**feeling:** THIN. No somatic-tell anchor in beat 10. Beat 10 is network-ambient by design. Expected thin.

**memory-flag:** THIN. Bone 187 (flies relay junction conversation) could be a callback to earlier junction scenes (beats 5/9), but this is a weak anchor.

**metaphor:** N/A.

**beat 10 verdict:** FACET-GAPS — see finding F-001.

---

### Beat 11 — Range expands ~30m; overnight operation; headache onset; log with grid notation (bones 209–230)

**Bones present:** 209 (flies spread overnight network), 210 (wasps spread dock-side alleys), 211 (beetles spread south-wall colony), 212 (spiders spread eastern-quarter approach), 213 (Taylor exhales), 214 (flies relay junction return), 215 (wasps relay Fish Gate perimeter), 216 (beetles relay south-wall return), 217 (spiders relay window), 218 (Taylor exhales), 219 (flies spread northern block), 220 (wasps spread eastern-quarter adjacent), 221 (Taylor exhales), 222 (Taylor walks perimeter), 223 (Taylor writes entry), 224 (Taylor writes entry), 225 (Taylor exhales), 226 (headache wakes Taylor), 227 (Taylor holds eyes), 228–230 (log).

**location-state:** ANCHOR PRESENT. Bones 219/220 (northern block, eastern-quarter adjacent — new perimeter geography). The location-state author can anchor the expanded perimeter to these bones. Adequate.

**state-updates:** FAULT ANCHOR PRESENT but sparse. Bone 222 (Taylor walks perimeter — new perimeter, state change for range), 226 (headache wakes Taylor — physiological state change). The range-expansion event itself has no explicit state-update bone. The spread bones (209-212) and relay bones (214-217) are action bones, but "range expanded 30m" as a canonical state-change has no single citable bone. The log entries (228-230) carry this but per schema, log-writing bones are write-actions, not state-update bones. Flag: state-updates author needs to anchor the range-expansion state-change; the closest available bones are 219/220 (new geography reached) and 222 (perimeter walk after expansion). Thin but workable.

**tensometer:** ANCHOR PRESENT. Bone 226 (headache wakes Taylor — body-charge, physiological rupture) and 227 (Taylor holds eyes — body-charge against pain) are the beat's peak candidates at 2-3. The spread/relay sequence (209-220) is 1. The three exhales (213/218/221/225) track the physiological cost in real time.

**dialogue:** GAP. No dialogue in beat 11. Overnight network operation — solo beat by design.

**narrator-interest:** ANCHOR PRESENT. Bones 213/218/221/225 (repeated exhales — POV tracking the cost), 226 (headache onset — internal state registered as physical event), 222 (perimeter walk after expansion). Strong NI pool for the cost-tracking register.

**sensory:** ANCHOR PRESENT. Bone 226 (headache wakes Taylor — thermal/pressure sensory event), 213/218/221/225 (exhales — breath modality). Adequate.

**feeling:** ANCHOR PRESENT. Bones 226 (headache wakes), 227 (Taylor holds eyes), 213/221/225 (exhales as somatic cost-markers). Strong feeling anchor.

**memory-flag:** THIN. Beat 11 is the first range-expansion; no prior range-expansion to callback. Later beats (14/19/24) will callback to beat 11.

**metaphor:** N/A.

**beat 11 verdict:** READY.

---

### Beat 12 — Eviction observed; Taylor logs with children's ages and rent debt (bones 232–244)

**Bones present:** 232 (lord's man enters alley), 233 (lord's man speaks to tenant family), 234 (lord's man's man breaks door latch), 235 (lord's man's man moves possessions), 236 (tenant family exits dwelling), 237 (neighbors press doorways), 238 (flies relay alley event), 239 (beetles relay door lintel), 240 (flies relay wall), 241 (neighbors withdraw), 242–244 (Taylor logs).

**location-state:** ANCHOR PRESENT. Bone 232 (alley), 234 (door latch — dwelling). Alley two-room dwelling. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 234 (door latch broken — prop state change), 235 (possessions moved — prop state change), 236 (family exits — actor state change). Multiple explicit state-update anchors.

**tensometer:** ANCHOR PRESENT. Bones 233 (lord's man speaks to family — 2), 234 (door latch breaks — physical rupture, 3-candidate), 235 (possessions moved — 2), 236 (family exits — resolution, 2-1), 237 (neighbors press doorways — ambient witness, 1-2), 241 (neighbors withdraw — release, 1). The door-latch break is the beat's 3-candidate.

**dialogue:** PARTIAL. Bone 233 (lord's man speaks to tenant family) — `tenant family` is a group listener, not a named individual. Per schema, this is valid form (`speaks to <group>`). Adequate.

**narrator-interest:** ANCHOR PRESENT. Bones 238/239/240 (relay bones covering the event), 237 (neighbors press doorways — ambient witness register). The network-observation-of-eviction is the NI focus. Adequate.

**sensory:** ANCHOR PRESENT. Bone 234 (door latch breaks — tactile/sound), 235 (possessions moved — sound). Sound inflection events. Adequate.

**feeling:** ANCHOR PRESENT. Bone 237 (neighbors press doorways — collective body-charge, somatic witness register), 241 (neighbors withdraw — collective release). Non-POV feeling anchors. Taylor's own feeling has no explicit somatic-tell bone in beat 12 (she observes through the network, does not physically attend).

**memory-flag:** ANCHOR PRESENT. Bone 234 (door latch breaks) is the anchor for the plan-noted memory-flag: "This entry will not exist in the log by s03 — a fact that has no weight yet." The memory-flag author for s03 will cite this beat 12 bone. In s01, no prior callback.

**metaphor:** N/A.

**beat 12 verdict:** FACET-READY. Taylor's own feeling is thin (she is network-only in this beat), but the structural observation-at-distance makes this expected.

---

### Beat 13 — Family second visit; father states customary wage-claim; partial payment; surface formalizes (bones 246–264)

**Bones present:** 246 (father enters junction), 247 (mother enters junction), 248 (father faces Taylor), 249 (father speaks to Taylor), 250 (Taylor faces father), 251 (Taylor speaks to father), 252 (father speaks to Taylor), 253 (Taylor exhales), 254 (Taylor opens purse), 255 (Taylor extends coins), 256 (father takes coins), 257 (father speaks to Taylor), 258 (Taylor faces father), 259 (father exits), 260 (mother exits); 262–264 (log).

**location-state:** ANCHOR PRESENT. Market-side junction (carried from previous junction scenes).

**state-updates:** ANCHOR PRESENT. Bones 254 (purse opened), 255 (coins extended — prop state change), 256 (father takes coins — prop transfer, actor state change). The payment exchange is a clean state-update anchor sequence.

**tensometer:** STRONG ANCHOR. Bones 249/251/252 (three-turn dialogue exchange — 2), 253 (Taylor exhales — body-charge post-statement, 2), 254/255/256 (purse-open, coins-extend, father-takes — commitment sequence, 2-3), 257 (father speaks to Taylor — post-payment statement, 2-3 candidate). The coins-extend/take sequence is the beat's peak.

**dialogue:** STRONG ANCHOR. Bones 249, 251, 252, 257 — four dialogue anchors in a tight exchange. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 253 (Taylor exhales), 254 (opens purse — the decision enacted). Strong NI anchor pool.

**sensory:** THIN. No acute sensory event. The scene is transactional. Expected thin.

**feeling:** STRONG ANCHOR. Bones 253 (Taylor exhales — somatic response), 255 (Taylor extends coins — body-charge commitment), 258 (Taylor faces father — post-payment orientation). Strong feeling anchor.

**memory-flag:** ANCHOR PRESENT. Bone 255/256 (coins extend/take) is a callback anchor to beat 3 (mother's song, mother's foreclosure) — the first formal formalizing of the claim begun in the grief sequence.

**metaphor:** N/A.

**beat 13 verdict:** FACET-READY.

---

### Beat 14 — Range crosses 400m; autumn relay; clinical log (bones 266–278)

**Bones present:** 266 (flies spread autumn-density network), 267 (wasps spread dock-side relay), 269 (spiders spread eastern-quarter relay), 270 (Taylor walks perimeter), 271 (Taylor writes entry), 272 (Taylor writes entry), 273 (Taylor exhales), 274 (headache wakes Taylor), 275 (Taylor holds eyes), 505 (Taylor lowers chin), 276–278 (log).

**Note:** Bone 268 is a gap (deleted ID).

**location-state:** ANCHOR PRESENT. Bone 266/267/269 (autumn network spread — new perimeter geography). The perimeter walk (270) confirms the expanded boundary. Adequate.

**state-updates:** THIN. Same structural gap as beat 11: range-expansion state-change has no dedicated state-update bone. Bones 266/267/269 (network spread) and 270 (perimeter walk) are the closest anchors.

**tensometer:** ANCHOR PRESENT. Bone 274 (headache wakes Taylor — 2-3), 275 (Taylor holds eyes — body-charge), 505 (Taylor lowers chin — body-charge post-headache, 2). Similar shape to beat 11. Adequate.

**dialogue:** GAP. No dialogue in beat 14. Solo range-expansion beat.

**narrator-interest:** ANCHOR PRESENT. Bones 273/275/505 (exhale, holds eyes, lowers chin — the cost-tracking sequence). Adequate.

**sensory:** ANCHOR PRESENT. Bone 274 (headache — pressure/pain), 273 (exhale). Adequate.

**feeling:** ANCHOR PRESENT. Bones 274/275/505 (headache, holds eyes, lowers chin). Strong somatic-tell anchor.

**memory-flag:** ANCHOR PRESENT. Beat 14's range expansion is the second expansion event; bones 274/275 are callbacks to beat 11's 226/227 (headache wakes, holds eyes). Memory-flag author can cite this pattern.

**metaphor:** N/A.

**beat 14 verdict:** READY.

---

### Beat 15 — Visitor at maester's door; 40-minute low-register conversation; maester becomes variable (bones 280–294)

**Bones present:** 280 (visitor enters side alley), 281 (visitor enters stairwell), 282 (time-skip), 283 (time-skip), 284 (visitor enters upper room), 285 (visitor speaks to maester), 286 (maester speaks to visitor), 287 (beetles relay register), 288 (Taylor holds feet), 289 (visitor exits upper room), 290 (visitor exits stairwell), 291 (visitor exits side-alley door), 292–294 (log).

**Note:** Two consecutive time-skip markers (282, 283) within beat 15 compress the 40-minute conversation into a skip. This is structurally unusual — the conversation itself is elided, and only the acoustic register is relayed (287).

**location-state:** ANCHOR PRESENT. Bones 280 (side alley), 281 (stairwell), 284 (upper room). Three micro-location transitions. Adequate.

**state-updates:** THIN. Bone 285/286 (exchange) and 287 (beetle relay of register) do not produce explicit actor/prop state changes. The visitor's departure (289-291) is the closest actor-state event.

**tensometer:** ANCHOR PRESENT. Bone 280 (visitor enters alley — 2, unusual hour), 281 (enters stairwell — 2, building toward), 284 (enters upper room — 2-3, the approach completing), 285/286 (exchange at too-low register — 2-3, the unreadable conversation), 287 (beetles relay register — POV attempting to read at 3 proximity), 288 (Taylor holds feet — body-charge at the not-reading moment), 289 (visitor exits — resolution, 2-1). The double time-skip (282/283) creates a structural gap between stairwell entry and upper-room entry. Flag: the 40-minute conversation is compressed to two time-skips followed by relay. Tensometer author cannot assign a scalar to deleted IDs 282/283.

**dialogue:** ANCHOR PRESENT. Bone 285 (visitor speaks to maester), 286 (maester speaks to visitor). Two dialogue anchors — but the conversation content is specifically noted in the plan as "at a register too low for clear acoustic capture." These bones are dialogue anchors that will produce dialogue-file entries, but the plan states the content is unreadable. Dialogue author must produce entries that reflect the low-register constraint.

**narrator-interest:** ANCHOR PRESENT. Bone 287 (beetles relay register — the failed read), 288 (Taylor holds feet — body-charge at the limit of what she can read). The not-reading is the NI focus. Adequate.

**sensory:** ANCHOR PRESENT. Bone 287 (beetles relay register — acoustic/sound modality, specifically the register of the voice below Taylor's reading threshold). Strong sensory anchor.

**feeling:** ANCHOR PRESENT. Bone 288 (Taylor holds feet — body-charge). Strong feeling anchor.

**memory-flag:** THIN. First occurrence of the visitor event.

**metaphor:** N/A.

**beat 15 verdict:** READY with flag: the two consecutive time-skip markers (282/283) compress the conversation. This is an intentional bone-level gap (the conversation is narratively elided), not a missing bone. Tensometer author must treat 282/283 as absent; no scalar assignment possible for deleted IDs.

---

### Beat 16 — Maester arrives as named presence; chain-stripped determination; logged (bones 296–313)

**Bones present:** 296 (beetles relay rhythm), 297 (beetles relay phrase), 298 (beetles relay rhythm), 496 (Taylor stills), 299–301 (log); then 305 (broken-maester exits apothecary), 306 (broken-maester enters side alley), 309 (broken-maester enters upper room), 310 (beetles relay broken-maester), 311–313 (log).

**Note:** Bones 302, 303, 304 (between 301 and 305) and 307/308 (between 306 and 309) are gap IDs (deleted). This beat has notable deletions.

**location-state:** ANCHOR PRESENT. Bone 305 (exits apothecary — implies ground-floor apothecary location), 306 (enters side alley), 309 (enters upper room). Location transitions adequate.

**state-updates:** ANCHOR PRESENT. Bone 305-309 tracks maester's movements through three location transitions — these are actor-state changes. The "named presence" determination is Taylor's recognition event — bone 496 (Taylor stills) is the body-anchor for this recognition event.

**tensometer:** ANCHOR PRESENT. Bones 296/297/298 (beetle relays of rhythm/phrase/rhythm — the acoustic evidence accumulating, 1-2 escalation), 496 (Taylor stills — body-charge at the recognition moment, 2-3), 305-309 (maester's movement sequence — 1-2, confirmation by physical movement data). The beat has a clear peak at 496.

**dialogue:** GAP. No `speaks to` bones in beat 16. The maester's "spoken phrases" are relayed through beetles (297) as acoustic data, not as a dialogue bone. No dialogue anchor in beat 16.

**narrator-interest:** ANCHOR PRESENT. Bones 296/297/298 (the rhythm of the maester's notation — acoustic pattern recognition), 496 (Taylor stills — recognition event). Strong NI anchor.

**sensory:** ANCHOR PRESENT. Bones 296/297/298 (beetle relays — sound modality, pattern recognition). Adequate.

**feeling:** ANCHOR PRESENT. Bone 496 (Taylor stills — body-charge at recognition). Adequate.

**memory-flag:** ANCHOR PRESENT. Bone 297 (beetles relay phrase — acoustic fragment) is the anchor for the recognition event. The memory-flag author can cite the pattern-recognition accumulation here.

**metaphor:** N/A.

**beat 16 verdict:** READY. Note: gap IDs 302/303/304 and 307/308 represent deleted bones; these do not affect facet coverage.

---

### Beat 17 — Third family visit; mother alone; vigil candle statement; grief changed shape (bones 315–328)

**Bones present:** 315 (mother enters flea-bottom-base), 316 (mother enters base room), 317 (mother faces Taylor), 318 (mother sits), 319 (Taylor faces mother), 320 (mother speaks to Taylor), 321 (Taylor speaks to mother), 322 (mother speaks to Taylor), 323 (mother exhales), 324 (mother exits base room); 326–328 (log).

**location-state:** ANCHOR PRESENT. Bone 315/316 (mother enters base/base room — establishes interior of flea-bottom-base). Adequate.

**state-updates:** ANCHOR PRESENT. Bone 318 (mother sits — actor state), 324 (mother exits — actor state). Adequate.

**tensometer:** ANCHOR PRESENT. Bone 317 (mother faces Taylor — reversal-proximity, 2), 318 (mother sits — body-charge, settling-in to a difficult conversation, 2), 320/321/322 (three-turn dialogue exchange, 2), 323 (mother exhales — body-charge after the vigil statement, 2-3), 324 (mother exits — resolution, 1). The vigil statement itself (in the dialogue at 322) is the beat's 3-candidate; bone 322 is the anchor.

**dialogue:** STRONG ANCHOR. Bones 320, 321, 322 — three dialogue anchors. The vigil-candle statement lives in bone 322. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 318 (mother sits), 320 (mother's first speech — the question), 323 (mother exhales — post-statement somatic release). Strong NI pool.

**sensory:** THIN. No acute sensory event. Beat 17 is intimate/verbal. Expected thin.

**feeling:** STRONG ANCHOR. Bones 317 (mother faces Taylor — confrontation alignment), 318 (mother sits — deliberate settling), 323 (mother exhales — somatic release after the vigil statement). Strong feeling anchor for both characters.

**memory-flag:** STRONG ANCHOR. Bone 320/322 (mother's statements) are callback anchors to beats 3 (the song, the foreclosure) and 6 (Taylor crosses gate — departure). Beat 17 is the explicit narrative callback to beat 3. Memory-flag author has a strong citable chain: bone 43 (mother drops song) → bone 322 (vigil candle stopped).

**metaphor:** CANDIDATE. The vigil-candle statement ("I stopped when it became clear that waiting for Tya was not the same as waiting for what came back") is the season's highest-density figurative language moment. If the metaphor-flag editor licenses a figure here, bone 322 is the anchor. Editor taste call; not a gap.

**beat 17 verdict:** FACET-READY. Best facet density of any single-character dialogue beat in s01.

---

### Beat 18 — Hightower clerk maps Flea Bottom labor web; elder describes Taylor; file entered (bones 330–342)

**Bones present:** 330 (clerk enters junction), 331 (clerk faces elder), 332 (clerk speaks to elder), 333 (elder speaks to clerk), 334 (clerk opens record book), 335 (clerk writes entry), 336 (clerk closes record book), 337 (clerk exits junction), 338 (flies relay clerk), 339 (flies relay junction return), 340–342 (Taylor logs).

**location-state:** ANCHOR PRESENT. Bone 330 (clerk enters junction — market-side junction). Adequate.

**state-updates:** ANCHOR PRESENT. Bones 334/335/336 (record book opened/written/closed — the file-entry event as state-update). Adequate.

**tensometer:** ANCHOR PRESENT. Bone 332/333 (clerk-elder exchange — 2), 335 (clerk writes entry — registration moment, 3-candidate), 337 (clerk exits — resolution, 1-2). Similar shape to beat 5 (lord's man quarterly pass). Adequate.

**dialogue:** ANCHOR PRESENT. Bones 332 (clerk speaks to elder), 333 (elder speaks to clerk). Two dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bones 338/339 (fly relays of clerk's departure). Taylor observes the clerk through the network. Adequate.

**sensory:** THIN. No acute sensory event. Expected thin (procedural beat).

**feeling:** THIN. No strong somatic-tell anchor for Taylor (she is network-observing). Bone 338/339 are relay bones, not body-charge bones. Beat 18 is observation-at-distance.

**memory-flag:** ANCHOR PRESENT. Bone 332/333 (clerk-elder exchange) is a callback anchor to beat 5 (lord's man quarterly pass — "comes back wrong" category). The Hightower-apparatus contact pattern opens here; memory-flag author can cite beat 5 bones.

**metaphor:** N/A.

**beat 18 verdict:** READY. Feeling thin (Taylor is network-only); expected.

---

### Beat 19 — Range crosses 500m; early winter expansion; maester's full vertical inside radius (bones 344–359)

**Bones present:** 344 (flies spread winter-onset network), 345 (wasps spread dock-side alleys), 346 (beetles spread south-wall colony), 347 (spiders spread eastern-quarter relay), 350 (beetles spread apothecary ground floor), 351 (Taylor walks perimeter), 352/353 (Taylor writes two entries), 354 (Taylor exhales), 355 (headache wakes Taylor), 356 (Taylor holds eyes), 497 (Taylor faces wall), 357–359 (log).

**Note:** Bones 348/349 are gap IDs (deleted).

**location-state:** ANCHOR PRESENT. Bone 350 (beetles spread apothecary ground floor — the new element inside the expanded radius). This is the key location-state event in beat 19. Adequate.

**state-updates:** THIN. Same structural gap as beats 11 and 14: range-expansion state-change has no dedicated state-update bone. Bone 350 (apothecary ground floor now inside radius) is the best available anchor.

**tensometer:** ANCHOR PRESENT. Bone 355 (headache wakes — 2-3), 356 (Taylor holds eyes — body-charge), 497 (Taylor faces wall — body-charge, post-headache orientation). Pattern mirrors beats 11 and 14.

**dialogue:** GAP. Solo expansion beat.

**narrator-interest:** ANCHOR PRESENT. Bone 350 (apothecary ground floor now inside radius — the operational significance is the maester's vertical is now complete), 354/356/497 (cost-tracking sequence). Adequate.

**sensory:** ANCHOR PRESENT. Bone 355 (headache — pressure/pain sensory event). Adequate.

**feeling:** ANCHOR PRESENT. Bones 355/356/497 (headache, holds eyes, faces wall). Somatic-tell pool for cost-tracking.

**memory-flag:** ANCHOR PRESENT. The headache-onset pattern (355/356) is the third occurrence of this specific beat (beats 11/14/19); memory-flag author can now establish the pattern as a recurring anchor chain.

**metaphor:** N/A.

**beat 19 verdict:** READY.

---

### Beat 20 — Second clerk; apothecary owner names Taylor; file entry wrong framework (bones 361–375)

**Bones present:** 361 (second clerk enters eastern-quarter adjacent), 362 (second clerk enters apothecary), 363 (second clerk speaks to owner), 364 (owner speaks to clerk), 365 (clerk speaks to owner), 366 (owner speaks to clerk), 367 (clerk opens record book), 368 (clerk writes entry), 369 (clerk closes record book), 370 (second clerk exits), 371 (flies relay doorframe), 372 (flies relay second clerk), 373–375 (log).

**location-state:** ANCHOR PRESENT. Bone 361 (eastern-quarter adjacent street), 362 (enters apothecary). Location transition. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 367/368/369 (record book sequence — file-entry event). The "apothecary owner names Taylor" moment lives in the dialogue at 363-366. The state-update is the book entry (368). Adequate.

**tensometer:** ANCHOR PRESENT. Bones 363-366 (two-round exchange — 2), 368 (clerk writes entry — registration, 3-candidate), 370 (clerk exits — resolution, 1-2). The naming-and-recording event (368) is the beat's 3-anchor. Adequate.

**dialogue:** STRONG ANCHOR. Bones 363, 364, 365, 366 — four dialogue anchors in two-round exchange. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 371 (flies relay doorframe — network covers the exchange from outside), 372 (flies relay clerk departure). Taylor is outside the apothecary, observing through the doorframe insects. The NI author must handle that Taylor cannot enter the space — bones 371/372 mark the network limit.

**sensory:** THIN. No acute sensory events. Beat 20 is indoor procedural. Expected thin.

**feeling:** THIN. Taylor is network-observing. No somatic-tell bones for Taylor in beat 20.

**memory-flag:** ANCHOR PRESENT. Bone 368 (clerk writes entry — the second file entry) is a callback to bone 335/75 (clerk writes entry in beat 18; lord's man writes in beat 5). Memory-flag author has a three-link chain: beat 5 → beat 18 → beat 20. Adequate.

**metaphor:** N/A.

**beat 20 verdict:** READY.

---

### Beat 21 — Elder routes task; Taylor accepts; burns dock-side cluster; position upgrades (bones 377–398)

**Bones present:** 377 (elder approaches Taylor), 378 (elder speaks to Taylor), 379 (Taylor faces elder), 380 (Taylor speaks to elder), 381 (elder speaks to Taylor); 383 (Taylor enters dock-side alley), 384 (wasps spread dock-side cluster), 385 (flies spread dock-adjacent labor web), 386 (Taylor speaks to dock-side cluster), 387 (wasps relay dock-side return), 388 (wasps relay labor-web path), 389 (dock-side cluster thins), 390 (flies retract), 391 (Taylor exits dock-side alley), 392 (elder speaks to Taylor), 393 (Taylor extends palm), 394 (elder places coin), 395 (Taylor closes fist), 396–398 (log).

**location-state:** ANCHOR PRESENT. Bones 383 (dock-side alley), 391 (Taylor exits dock-side alley). Adequate.

**state-updates:** ANCHOR PRESENT. Bones 389 (dock-side cluster thins — network state change, the burn-down), 390 (flies retract — network state change), 393/394/395 (palm extended, coin placed, fist closed — prop state changes). Adequate.

**tensometer:** ANCHOR PRESENT. Bone 378/380/381 (elder-Taylor exchange — 2), 384/385 (cluster spread, labor web spread — deployment, 2), 386 (Taylor speaks to dock-side cluster — active routing, 2-3 candidate), 389 (cluster thins — the cost registering in real time, 3-candidate), 393/394/395 (payment sequence — 1-2). The cluster-thinning (389) is the structural peak of beat 21 — the cost of the upgrade landing.

**dialogue:** ANCHOR PRESENT. Bones 378, 380, 381, 392 — four dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 386 (Taylor speaks to dock-side cluster — the moment she routes through her own observation surface), 389 (cluster thins — POV registers the cost). Strong NI anchor.

**sensory:** THIN. No acute sensory inflection events. Expected thin.

**feeling:** ANCHOR PRESENT. Bones 393 (Taylor extends palm), 395 (Taylor closes fist — body-charge, receiving payment for the network-cost). Strong somatic-tell anchor.

**memory-flag:** ANCHOR PRESENT. Bone 389/390 (cluster thins, flies retract) are callbacks to beat 8 (dock-runner/Watch transaction — first use of this observation surface). Memory-flag author can trace the dock-side cluster through beats 8 and 21.

**metaphor:** N/A.

**beat 21 verdict:** FACET-READY.

---

### Beat 22 — Broken maester walks to dried-beetle stall; stall-keeper names coordination anomaly; maester's extended session (bones 400–422)

**Bones present:** 400 (maester descends stair), 401 (maester exits apothecary), 402 (maester enters eastern-quarter alley), 403 (beetles relay footfall), 404 (maester enters eastern-quarter market), 405 (maester approaches stall), 406 (maester speaks to stall-keeper), 407 (stall-keeper speaks to maester), 408 (maester speaks to stall-keeper), 409 (stall-keeper speaks to maester), 410 (maester faces jars), 411 (maester exits stall), 412 (beetles relay maester), 413 (maester enters apothecary), 414 (maester ascends stair), 415 (maester enters upper room), 416 (beetles relay onset), 417 (beetles relay cessation), 503 (Taylor holds feet), 420–422 (log).

**Note:** Bones 418/419 are gap IDs (deleted).

**location-state:** ANCHOR PRESENT. Bones 400/401 (stair/apothecary exit), 402 (eastern-quarter alley), 404 (eastern-quarter market), 405 (stall approach), 411/413 (stall exit, apothecary re-entry). Five location transitions. Adequate.

**state-updates:** ANCHOR PRESENT. Bones 400/401/402/404 (maester's movement through multiple locations — actor state changes), 416/417 (beetles relay onset/cessation — the extended pen-scratch session, begins and ends). Adequate.

**tensometer:** ANCHOR PRESENT. Bones 403 (beetles relay footfall — 1, initial tracking), 406-409 (two-round stall exchange — 2), 410 (maester faces jars — reversal-proximity, 2), 411 (exits stall — 1-2), 416 (beetles relay onset — 2, extended session begins), 417 (beetles relay cessation — 2, session ends, information boundary), 503 (Taylor holds feet — body-charge at the not-knowing moment, 2-3). The extended-session onset/cessation (416/417) and Taylor's holds-feet (503) form the beat's late peak.

**dialogue:** ANCHOR PRESENT. Bones 406, 407, 408, 409 — four dialogue anchors in a two-round stall exchange. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bones 403/412 (beetle relay of maester's movement), 416/417 (onset/cessation of extended session), 503 (Taylor holds feet — the recognition of significance). Strong NI pool.

**sensory:** ANCHOR PRESENT. Bones 416/417 (beetles relay onset/cessation — sound modality, pen-scratch rhythm). The stall exchange has sound elements in bones 406-409. Adequate.

**feeling:** ANCHOR PRESENT. Bone 503 (Taylor holds feet — body-charge at the information-limit). Strong feeling anchor.

**memory-flag:** STRONG ANCHOR. Bone 406/407/408/409 (stall exchange about insect coordination anomaly) is the key callback anchor in s01. The stall-keeper's mention of insect coordination anomalies is the maester beginning to connect Taylor's network to an anomaly — this is the first moment in s01 where external observation approaches naming her. Memory-flag author has a strong anchor here that will chain forward to s02 beats.

**metaphor:** N/A.

**beat 22 verdict:** FACET-READY. Beat 22 is one of the season's most facet-rich beats.

---

### Beat 23 — Father at junction; wage claim now on lord's record; village-claim closes from outside (bones 424–436)

**Bones present:** 424 (father enters junction), 425 (father approaches elder), 426 (father speaks to elder), 427 (elder faces father), 428 (elder speaks to father), 429 (father exits junction), 430 (elder approaches Taylor), 431 (elder speaks to Taylor), 432 (Taylor faces elder), 433 (Taylor exhales), 434–436 (log).

**location-state:** ANCHOR PRESENT. Market-side junction (continuous from prior junction scenes). Adequate.

**state-updates:** ANCHOR PRESENT. Bone 426/428 (father's statement to elder, elder's response — the formal-record notification is the state event). No prop state change but the actor-state (Taylor's awareness of the external record) is anchored by bone 431/432.

**tensometer:** ANCHOR PRESENT. Bones 426/428 (father-elder exchange — 1-2), 431 (elder speaks to Taylor — information delivery, 2), 432 (Taylor faces elder — 2), 433 (Taylor exhales — body-charge, the weight of the information landing, 2-3 candidate). Beat 23 is a quiet-peak beat — no confrontation, no visible rupture, but the information is irreversible.

**dialogue:** ANCHOR PRESENT. Bones 426, 428, 431 — three dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bone 432 (Taylor faces elder — POV receives the information), 433 (Taylor exhales — POV registers the weight). Adequate.

**sensory:** THIN. No acute sensory event. Expected thin.

**feeling:** ANCHOR PRESENT. Bone 433 (Taylor exhales — somatic response to the news of the external record). Adequate.

**memory-flag:** ANCHOR PRESENT. Bone 431 (elder speaks to Taylor about the lord's-man record) is a callback to beats 5 (lord's man records "behavior irregular") and 13 (partial payment formalizes the claim). The memory-flag chain: beat 5 bone 75 → beat 13 bone 255/256 → beat 23 bone 431. Adequate.

**metaphor:** N/A.

**beat 23 verdict:** READY.

---

### Beat 24 — Range reaches ~600m; overnight operation; Red Keep distance known and unrecorded (bones 438–507)

**Bones present:** 438 (flies spread overnight network), 439 (wasps spread Fish Gate margin), 440 (beetles spread south-wall colony), 441 (spiders spread eastern-quarter relay), 444 (beetles spread south-wall perimeter), 445 (Taylor walks perimeter), 446/447 (two write entries), 448 (Taylor exhales), 449 (headache wakes Taylor), 450 (Taylor holds eyes), 498 (Taylor faces wall), 499 (Taylor straightens spine), 451–453 (log), 507 (Taylor faces the Red Keep).

**Note:** Bones 442/443 are gap IDs (deleted).

**location-state:** ANCHOR PRESENT. The overnight network spread covers Fish Gate margin (439), south-wall colony (440/444), eastern-quarter relay (441). Perimeter walk (445) confirms the expansion. Bone 507 (Taylor faces the Red Keep) is a new location-state anchor — Taylor's orientation toward the Red Keep from the base. Adequate.

**state-updates:** THIN. Range-expansion state-change gap persists (same as beats 11/14/19). Bone 507 (Taylor faces the Red Keep) is a notable state bone: this is the first explicit spatial relationship between Taylor's position and the Red Keep. Adequate.

**tensometer:** ANCHOR PRESENT. Bone 449 (headache wakes — 2-3), 450 (Taylor holds eyes — body-charge), 498 (Taylor faces wall — post-headache body orientation), 499 (Taylor straightens spine — resolution charge), 507 (Taylor faces the Red Keep — the season's final awareness-of-distance bone, 2-3 candidate). Beat 24 has the richest tensometer anchor pool among the range-expansion beats because of bone 507.

**dialogue:** GAP. Solo overnight operation.

**narrator-interest:** ANCHOR PRESENT. Bone 507 (Taylor faces Red Keep — the distance-is-known-and-unrecorded moment) is the strongest NI anchor in all range-expansion beats. The plan specifies "the log does not record the distance to the Red Keep" — this is a non-recording, an intentional omission. The NI author can cite bone 507 as the moment the narrator registers what the log omits.

**sensory:** ANCHOR PRESENT. Bone 449 (headache — pressure/pain), 448 (exhale). Adequate.

**feeling:** ANCHOR PRESENT. Bones 449/450/498/499/507 (headache, holds eyes, faces wall, straightens spine, faces Red Keep). Richest feeling-anchor pool of any range-expansion beat.

**memory-flag:** STRONG ANCHOR. Bone 507 (Taylor faces Red Keep) is the memory anchor for the season's structural through-line: range-expansions across beats 11/14/19/24, each with headache cost, each with the Red Keep still beyond ceiling. Memory-flag author can build the full chain here: beat 11 → beat 14 → beat 19 → beat 24, with bone 507 as the terminal anchor.

**metaphor:** CANDIDATE. Bone 507 (Taylor faces the Red Keep — the distance known and unrecorded) is the closest thing to a licensed metaphor moment in s01. The spatial relationship between the protagonist and the factional seat of power, measured and suppressed in the same beat, has the structural figure that could earn a metaphor-flag. Editor taste call; not a gap.

**beat 24 verdict:** FACET-READY.

---

### Beat 25 — Messenger to elder; written account delivered; Hand's file completes under wrong framework (bones 455–475)

**Bones present:** 455 (messenger enters junction), 456 (messenger faces elder), 457 (messenger speaks to elder), 458 (elder faces messenger), 459 (elder speaks to messenger), 460 (messenger exits junction), 461 (flies relay messenger), 462 (flies relay messenger — two relay bones), 463 (Taylor holds feet); then 465 (elder exits junction), 466 (elder enters writing room), 467 (elder writes account), 468 (elder seals account), 469 (middleman takes sealed account), 470 (middleman exits writing room), 471 (flies relay junction departure), 472 (Taylor holds feet — two holds-feet bones), 473–475 (log).

**location-state:** ANCHOR PRESENT. Bones 455 (junction — established location), 466 (writing room — new micro-location), 470 (middleman exits writing room). Adequate.

**state-updates:** ANCHOR PRESENT. Bones 467 (elder writes account), 468 (elder seals account — prop state change), 469 (middleman takes sealed account — prop transfer). Adequate.

**tensometer:** ANCHOR PRESENT. Beat 25 is the season's marked PEAK. Bones 457/459 (messenger-elder exchange — 2-3), 460 (messenger exits — post-exchange resolution, 2), 463 (Taylor holds feet — first body-charge at the limit of observation, 2-3), 467/468/469 (account written, sealed, taken — sequential commitment beats, 3-3-2), 472 (Taylor holds feet — second body-charge at the information-limit, 2-3). The double holds-feet (463/472) bracket the off-stage writing event. The account-sealed-and-taken sequence (467-469) is the season's peak tensometer cluster. Adequate.

**dialogue:** ANCHOR PRESENT. Bones 457 (messenger speaks to elder), 459 (elder speaks to messenger). Two dialogue anchors. Adequate.

**narrator-interest:** ANCHOR PRESENT. Bones 461/462 (two fly relays of the messenger), 463 (Taylor holds feet — the limit of what the network can observe), 472 (Taylor holds feet — the limit of what can be observed off-stage). The double holds-feet are the NI focus of beat 25. Strong.

**sensory:** THIN. No acute sensory events. Beat 25 is procedural at the limit of observation. Expected thin for the off-stage portion (467-469).

**feeling:** ANCHOR PRESENT. Bones 463 (Taylor holds feet), 472 (Taylor holds feet — two distinct instances of the same somatic-tell). Note: per the feeling schema, per-character per-scene cap is ≤1 (hard). Two holds-feet bones in one beat (463/472) means the feeling author must choose one; both cannot fire. This is a constraint-the-schema-imposes on the bones, not a gap.

**memory-flag:** ANCHOR PRESENT. Bone 467 (elder writes account) and 469 (middleman takes account) are the peak callback anchors for the Hightower-apparatus arc: beats 5 → 18 → 20 → 25. The file completing under the wrong framework (stated in the plan, not in the bones) is a NI and memory-flag territory.

**metaphor:** N/A (peak beat, but metaphor requires feeling or memory anchor — the feeling schema constraint on the double holds-feet limits this; editor may decline).

**beat 25 verdict:** FACET-READY with one per-schema note: bones 463 and 472 are two holds-feet bones in one beat; per feeling schema per-scene cap ≤1 hard, the feeling author must select one. Not a fault in bones; a constraint the feeling-author must honor.

---

### Beat 26 — Denouement walk; two log entries side-by-side; reader-level asymmetry (bones 477–494)

**Bones present:** 477 (Taylor exits base), 478 (Taylor enters first alley), 479 (Taylor walks first alley), 480 (Taylor enters south alley), 481 (Taylor walks south alley), 482 (Taylor enters Fish Gate margin), 483 (Taylor walks margin), 484 (beetles spread south-wall colony), 485 (Taylor walks south-wall colony), 486 (Taylor crosses market-side junction), 487 (Taylor enters eastern-quarter approach), 488 (spiders relay window), 489 (Taylor walks eastern-quarter approach), 490 (Taylor enters base), 491–494 (log — four write/close bones).

**location-state:** STRONG ANCHOR. Beat 26 traces Taylor's perimeter walk through six distinct location segments (bones 477-490). This is the most geographically detailed location-state sequence in s01. Adequate.

**state-updates:** THIN. No prop or actor state changes during the walk. Bone 484 (beetles spread south-wall colony) is a network-state event. The log entries (491-494) are the write-action bones. The denouement beat is architecturally a return-to-baseline, not a state-change beat. Expected thin.

**tensometer:** ANCHOR PRESENT. The denouement beat is structurally post-peak. Tensometer will be 1s throughout, with the possible exception of bones 491-494 (two log entries side-by-side — the simultaneous recording of the two apparatuses). The plan specifies four log write/close bones (491, 492, 493, 494) where previous beats have three (open/write/close). This extra bone is the denouement's structural tell: two entries, not one. Tensometer author may assign 2 to bones 492/493 (the two parallel entries being written) as the denouement's quiet registration. Adequate.

**dialogue:** GAP. Solo perimeter walk — no dialogue in beat 26 by design.

**narrator-interest:** STRONG ANCHOR. Bones 491-494 (the four-log sequence) are the NI focus: the narrator records two external records, notes they are on separate institutional tracks, and closes without speculating. The NI author's primary anchor is 492/493 (the two entries), with 494 (close) as the final non-speculation beat.

**sensory:** ANCHOR PRESENT. Bone 484 (beetles spread south-wall colony — sound/tactile, the colony texture at the densest point), 488 (spiders relay window — sound relay). Adequate.

**feeling:** THIN. No somatic-tell bones during the walk. Bone 479/481/483/485/489 are motion bones. Beat 26 is structurally a non-feeling beat — the denouement operates through action (walking) and recording (logging), not somatic register. Expected thin.

**memory-flag:** STRONG ANCHOR. Bones 492/493 (two side-by-side log entries) are the terminal callback for all major memory chains in s01: beat 5 → beat 23 (village-claim, lord's man record) and beats 18/20/25 (Hightower-apparatus file chain). The denouement is the memory-flag author's aggregation beat.

**metaphor:** CANDIDATE. The plan explicitly names this the "reader-level asymmetry registers what Taylor cannot" beat. If the metaphor-flag editor licenses any figure in s01, beat 26 is the most defensible location. The architecture-has-changed-but-she-does-not-know-what-file structure carries the season's central figure. Editor taste call; not a gap.

**beat 26 verdict:** FACET-READY.

---

## Over-dense / Under-dense stretch findings

### F-001 — Beat 10: Under-dense for a three-week narrative span

**type:** fault

**what:** Beat 10 (bones 187–207) covers "three weeks of network-ambient listening; begins routing weather-pattern data and Watch-movement timing anonymously." The bones covering this three-week span are: 187 (flies relay junction conversation), 189/190/191/193/194 (time-skips and one relay bone), 195 (Taylor enters base), 199 (time-skip), 200 (flies relay weather-pattern data), 201-202 (log), 203/204 (time-skips), 500 (Taylor closes log), 508 (elder pauses), 501 (elder speaks to carter), 502 (wasps relay pass), 205-207 (log). Only 10 substantive bones (non-skip, non-log) cover three weeks of the most operationally complex beat in the first half of s01 — the beat where Taylor maps the whisper-chain architecture and begins anonymous routing.

**why:** The facet authors — especially location-state, feeling, sensory, and tensometer — have insufficient material to distinguish beat 10 from a pure transit beat. The plan specifies this as an active intelligence beat (chain architecture mapping, anonymous routing, "odd but functional" read established). The bones do not carry bones representing: (a) Taylor inhabiting the junction or Fish Gate margin across the three weeks (no movement bones beyond entering base once at 195), (b) the anonymous routing event itself (only bone 200 — weather-pattern data relay — is present; Watch-movement timing routing has no bone), (c) the "odd but functional" read being established (no social-interaction bones other than elder-speaks-to-carter at 501). The NI and feeling authors will work primarily from the four relay bones (187/190/200/502) and the log sequences.

**criteria:** Beat 10 bones must supply at least one anchor per under-covered facet: a movement bone establishing Taylor's presence at the chain (junction or Fish Gate margin, not just base); a bone representing the Watch-movement timing routing (parallel to the weather-data relay at 200); and a social-context bone establishing the "odd but functional" ambient read (e.g., a chain-node interaction bone, even brief). The existing time-skip structure can remain; the bones must be added within that structure.

---

### F-002 — Range-expansion beats (11/14/19/24): state-updates facet has no explicit range-state-change bone in any expansion beat

**type:** flag

**what:** Beats 11, 14, 19, and 24 each represent a range-expansion event. None of them contain a bone that explicitly records the range-state change as a physical actor-state event. The spread bones (flies/wasps/beetles/spiders spread) are network-deployment actions; the perimeter-walk bones confirm boundary existence; but no bone names the protagonist's range as a state-change event (e.g., "the sphere extends 30 meters" is not renderable as SVO without a subject acting). The log-write bones (write the entry) carry the clinical notation in the plan — but per schema, log-write bones are action bones, not state-update anchors.

**why:** The state-updates facet author sources from bones that mark `<target>.<field>: <old> -> <new>`. The range-expansion is the most load-bearing recurring state-change in s01. If the state-updates author has no explicit anchor for the range field change, they must infer it from the network-spread bones — which are physically plausible but formally ambiguous. Downstream: the state-update-to-stitch pipeline cannot verify range-expansion state without an explicit anchor.

**criteria:** This is a flag, not a fault. The state-updates author should be briefed that the range-expansion state-change is inferrable from the perimeter-walk bones (28/30 in beat 2; 222 in beat 11; 270 in beat 14; 351 in beat 19; 445 in beat 24) and the new-geography spread bones, even though no explicit state-change bone names the protagonist's range field. If the state-updates author cannot resolve from this pool, a fixer must add a single state-annotation bone per expansion beat.

---

### F-003 — Beat 10, bones 187–194: dense time-skip cluster creates a narrative hole

**type:** fault

**what:** Bones 187, 189, 190, 191, 193, 194 — of these, bones 189, 191, 193, 194 are consecutive time-skip markers (bare numbered IDs with no content), with only 187 (relay) and 190 (relay) as substantive bones. Four time-skip markers in a span of eight IDs creates a sequence of gaps that reads as a four-segment time-skip with only two thin relay bones anchoring each end.

**why:** Per the proto-line schema, time-skip markers indicate non-trivial elapsed intervals. Four time-skips in rapid succession, with only relay bones between them, means the stitcher will render four chapter-break-or-paragraph-break markers in close proximity. For a beat that covers three weeks of active operation, this is structurally appropriate for time-compression — but combined with F-001 (under-dense bones overall), the result is that the stitcher has nearly no material to render for beat 10 beyond two relay bones flanking four breaks. The reader-facing output will be four-break plus two minimal relay observations plus log — approximately 6-8 rendered lines for a three-week beat that is architecturally load-bearing (it establishes Taylor's operational integration into Flea Bottom).

**criteria:** The time-skip markers themselves are acceptable (compression of three weeks is appropriate). But within or adjacent to this cluster, at least two substantive bones must be added to give the stitcher material between breaks. See F-001 criteria — the bones identified there would satisfy this requirement. F-001 and F-003 have the same fix target; one fixer pass resolves both.

---

### F-004 — Missing POV-marker for the narrator-distant sub-sequence in beat 5

**type:** flag

**what:** Beat 5 bones 71–77 (lord's man enters village, speaks to reeve, writes entry, exits) occur in a location where Taylor is not physically present. The bones 63–69 establish Taylor physically present in the yard (bone 65: Taylor crosses yard); bones 71–77 shift to the village street scene without a POV-distance marker. Per the proto-line schema, POV transitions are "inline (interlude beats are flagged inline, not as section breaks)." There is no inline POV-marker between bone 69 (reeve exits yard) and bone 71 (lord's man enters village).

**why:** The narrator-interest author for beat 5 must determine whether bones 71–77 are observable from Taylor's physical position (in the yard, at the tanner-family home) or whether they are narrative-reported events (learned later, reconstructed). The plan states "The record exists before Taylor knows the lord's man visited" — meaning Taylor does NOT observe this in real-time. Without a POV-marker, the narrator-interest and sensory facet authors may incorrectly treat bones 71–77 as direct-POV events.

**criteria:** A POV-distance marker or a relay-bone should precede bone 71 to signal that the lord's-man sequence is not direct-POV observation. Alternatively, if the season schema's POV-transition conventions are sufficient (the character slug `the lords-man` rather than `taylor-hebert-flea-bottom` as subject is the implicit signal), the flag is advisory only. Flag for Phase 7 episode-boundary assignment to resolve.

---

### F-005 — Beat 8 time-skip marker at 144 may incorrectly compress the dock-runner approach (two-day elapsed time)

**type:** flag

**what:** Bone 144 is a single time-skip marker between the Watch/runner-exit sequence (141-143) and the dock-runner-approaching-via-elder sequence (145-155). The plan specifies "Two days later, the runner approaches the market-side junction." A single time-skip marker is formally correct for elapsed time; however, the proximity of bones 141/143 (runner exits, flies relay runner) to bone 144 (time-skip) to bone 145 (elder speaks to dock-runner) may not signal the two-day interval clearly enough for location-state and NI authors to distinguish these as temporally separate scenes rather than a continuous beat.

**criteria:** This is advisory. The single time-skip marker is per-schema. If location-state authors and NI authors are briefed that bone 144 marks a two-day gap, no fix is needed. If the Phase 7 episode-boundary assignment does not produce a clear episode-break here, the single time-skip may be worth expanding to two (per the schema: "Multiple consecutive blank-numbered lines indicate a longer skip").

---

### F-006 — Beat 25: two `taylor-hebert-flea-bottom holds the feet` bones in one beat raises feeling-schema cap conflict

**type:** flag

**what:** Bones 463 (Taylor holds feet) and 472 (Taylor holds feet) both appear in beat 25. Per the feeling schema, per-character per-scene cap is ≤1 (hard). If beat 25 constitutes one scene for scene-boundary purposes, the feeling author must select one of 463/472 — the other cannot fire.

**why:** If the feeling author selects bone 463 (first holds-feet, at the point the network cannot follow the messenger further), they lose the feeling anchor at bone 472 (second holds-feet, after the off-stage writing event). The two holds-feet instances bracket a structurally significant off-stage event (elder writes and seals account). Losing one leaves the beat's second half without a Taylor-feeling anchor. This is a planning constraint embedded in the bones, not a schema violation.

**criteria:** Flag for feeling author and for Phase 7 episode-boundary assignment: if beat 25 is assigned across an episode boundary (messenger exchange in one episode, elder writing in the next), the per-scene cap applies per episode — 463 fires in one episode, 472 in the next, and the cap is satisfied. If beat 25 is one episode, one of the two holds-feet bones must remain unused by the feeling author.

---

### F-007 — Over-dense scan: beat 9 contains 23 bones with no tensometer inflection point visible in the pure-action bones

**type:** flag

**what:** Beat 9 (bones 159–181) runs 23 substantive bones without a time-skip marker. The plan describes the father spotting the strategic-scan tell and leaving with a new unnamed problem. The bones execute this through a continuous junction scene. 23 bones without a time-skip is not per-se an over-dense flag (the 10+ threshold is for scenes without inflection, not for scenes with dialogue exchanges). However, the tensometer author must supply escalation from the ambient (159-164 = 1s) through the approach/pivot/confrontation sequence (165-172 = 2s, with 170/171 as the double-still peak at 3) to the departure (178-181 = 1s). This is a complete shape — 1→2→3→2→1 — across 23 bones. Not a fault.

**criteria:** Advisory. Tensometer author should note the double-still at bones 170/171 (father stills, mother stills) as the beat's 3-cluster. The adjacency test applies: the 3 should sit next to the 2s at 165-169. No fault in bones; tensometer ladder is readable.

---

### F-008 — Beat 7: over-dense scan — 12 consecutive bones (105–116) with only one potential 2-rated bone (111)

**type:** flag

**what:** Bones 105–116 (beat 7) contain 12 substantive bones with only one escalation candidate (111: maester speaks to room). Per the rubric's curve-shape requirement, scenes must show at minimum one moment that earns a 2 or 3. Bone 111 is the sole non-1 candidate in this run; all other bones are ambient/transit/log.

**why:** If the tensometer author assigns bone 111 as a 2, the scene-as-transit rubric exception is satisfied. If the maester's ambient voice does not clear the rubric's 2-threshold (speaking-as-default is rated 1 per the rubric: "Speaking is by itself a 1"), then beat 7 has no escalation bones and qualifies for a dramatist's "scene-as-transit" explicit flag. The maester's ambient voice may clear 2 on the stakes-visibility axis (public-speech risk from an unknown source being detected — this is a watch-cost) but the rubric is strict: "Rating 2/3 because the scene has stakes when this beat doesn't carry them on its face" is anti-pattern 1.

**criteria:** Flag for tensometer author: bone 111 (maester speaks to room) must be evaluated on the rubric's 2-threshold. If it clears, beat 7 has its required escalation. If it does not clear, the dramatist must flag beat 7 as scene-as-transit with explicit exemption documented. Either outcome is acceptable; the tensometer author must make the call explicitly rather than silently.

---

## Aggregate facet coverage summary

| Beat | loc-state | state-upd | tens | dialogue | NI | sensory | feeling | memory | metaphor |
|------|-----------|-----------|------|----------|----|---------|---------|--------|----------|
| 1 | flag* | OK | OK | absent† | OK | OK | OK | OK | N/A |
| 2 | flag* | thin | 1s | absent† | OK | thin | OK | absent† | N/A |
| 3 | flag* | OK | OK | absent† | OK | OK | OK | OK | cand |
| 4 | flag* | OK | OK | absent† | OK | thin | OK | absent† | N/A |
| 5 | OK | OK | OK | OK | flag‡ | thin | OK | absent† | N/A |
| 6 | OK | OK | OK | OK | OK | OK | OK | absent† | N/A |
| 7 | OK | thin | OK§ | absent† | OK | OK | thin | absent† | N/A |
| 8 | OK | OK | OK | OK | OK | OK | OK | absent† | N/A |
| 9 | OK | OK | OK | OK | OK | thin | OK | OK | N/A |
| 10 | thin | OK | thin | thin | OK | thin | thin | thin | N/A |
| 11 | OK | thin | OK | absent† | OK | OK | OK | thin | N/A |
| 12 | OK | OK | OK | OK | OK | OK | thin | OK | N/A |
| 13 | OK | OK | OK | OK | OK | thin | OK | OK | N/A |
| 14 | OK | thin | OK | absent† | OK | OK | OK | OK | N/A |
| 15 | OK | thin | OK | OK | OK | OK | OK | thin | N/A |
| 16 | OK | OK | OK | absent† | OK | OK | OK | OK | N/A |
| 17 | OK | OK | OK | OK | OK | thin | OK | OK | cand |
| 18 | OK | OK | OK | OK | OK | thin | thin | OK | N/A |
| 19 | OK | thin | OK | absent† | OK | OK | OK | OK | N/A |
| 20 | OK | OK | OK | OK | OK | thin | thin | OK | N/A |
| 21 | OK | OK | OK | OK | OK | thin | OK | OK | N/A |
| 22 | OK | OK | OK | OK | OK | OK | OK | OK | N/A |
| 23 | OK | OK | OK | OK | OK | thin | OK | OK | N/A |
| 24 | OK | thin | OK | absent† | OK | OK | OK | OK | cand |
| 25 | OK | OK | OK | OK | OK | thin | flag§§ | OK | N/A |
| 26 | OK | thin | OK | absent† | OK | OK | thin | OK | cand |

*Location slug gap: tanner-village bones carry no explicit loc-slug for beats 1-4. Location-state author must infer from context.
†Dialogue absent by structural design — solo beats or purely gestural beats. Not a fault.
‡POV-distance marker absent for bones 71-77 in beat 5.
§Beat 7: maester's voice (bone 111) may not clear rubric's 2-threshold. Flag F-008.
§§Beat 25: double holds-feet bones (463/472) — feeling schema per-scene cap ≤1 applies; see F-006.
thin = material exists but is minimal; sensory/state-updates/feeling authors should be advised they have a sparse pool.
absent† = structural absence by design (no dialogue, no callback yet); not a facet gap.

---

## Classified findings

```yaml
audit:
  scope: season
  target: s01
  pass: S7-facet-readiness
  timestamp: 2026-05-11
  verdict: FACET-GAPS
  findings:
    - id: fault-001
      type: fault
      what: >
        Beat 10 bones (187–207): three-week operational beat (whisper-chain mapping, anonymous routing,
        "odd but functional" read established) has only 10 substantive non-log non-skip bones. Missing:
        movement bone placing Taylor at the junction or Fish Gate margin during the three weeks; Watch-movement
        timing routing bone (parallel to weather-data relay at bone 200); social-context bone establishing
        the "odd but functional" ambient read from chain-node interaction.
      why: >
        Facet authors for location-state, feeling, sensory, and tensometer have insufficient material to
        distinguish beat 10 from a pure transit beat. The beat is architecturally load-bearing — it establishes
        Taylor's operational integration into Flea Bottom — but bones give facet authors approximately 6-8
        renderable lines across a three-week span. NI and feeling authors have near-zero anchors.
      criteria: >
        Beat 10 bones must include at minimum: one movement bone placing Taylor at a chain node location
        (junction or Fish Gate margin) during the three-week period; one routing-action bone representing
        Watch-movement timing information passing through the chain (parallel structure to bone 200 weather
        relay); one social-context bone representing an ambient chain-node interaction (brief; does not need
        to be a named-character `speaks to` bone — an observed interaction bone is sufficient). Existing
        time-skip structure may remain; the new bones must fall within the existing ID sequence.

    - id: fault-002
      type: fault
      what: >
        Beat 10 bones 187–194: four time-skip markers (189, 191, 193, 194) in an 8-ID span, flanked by
        only two relay bones (187, 190). Combined with F-001 (under-dense substantive bones), the stitcher
        has near-zero material between four consecutive chapter-break signals for beat 10's three-week span.
      why: >
        The stitcher renders time-skip markers as chapter-break or paragraph-break. Four consecutive breaks
        with minimal flanking material produces a reader-facing sequence of approximately: one relay observation,
        four breaks, one relay observation, four log entries. For a three-week beat that is the season's
        operational integration beat, this is structurally insufficient. Downstream stitcher output will
        under-represent beat 10 relative to its narrative function.
      criteria: >
        Same fix target as fault-001. Adding the specified bones within the existing ID sequence will supply
        material between the time-skip markers. One fixer pass resolves both fault-001 and fault-002.

    - id: fault-003
      type: flag
      what: >
        Range-expansion state-change has no explicit actor-state bone in beats 11, 14, 19, or 24. The
        protagonist's insect-control range field changes in each of these beats, but no bone names this
        as a state event. State-updates author must infer from perimeter-walk bones and network-spread bones.
      why: >
        The state-updates facet is the source for batched memory write-back at cross-facet consistency.
        If the range-expansion state-change is not anchored to a specific bone, the state-updates author
        may omit it or anchor it inconsistently across the four expansion beats, producing write-back
        inconsistencies at the memory-write phase.
      criteria: >
        State-updates author must be briefed that perimeter-walk bones (222, 270, 351, 445) and new-geography
        spread bones (219/220 in beat 11; 266/267/269 in beat 14; 347/350 in beat 19; 438-441/444 in beat 24)
        are the intended range-expansion anchors. If the author cannot resolve the range field consistently
        from this pool, a single state-annotation bone per expansion beat must be added. Resolution is author-call
        first; fixer only if author flags inability to resolve.

    - id: fault-004
      type: flag
      what: >
        Beat 5, bones 71–77 (lord's man enters village, speaks to reeve, writes entry, exits): no POV-marker
        or relay-bone signals that Taylor is not physically present for this sub-sequence. Taylor is in the
        yard at bones 63–69; the lord's man sequence occurs in the village street without a POV-distance marker.
      why: >
        Narrator-interest and sensory facet authors may incorrectly treat bones 71–77 as direct-POV events.
        The plan explicitly states Taylor does not know the lord's man visited. If NI and sensory authors
        supply direct-observation entries for 71–77, the stitcher will render Taylor perceiving events she
        does not observe — a constraint violation (cond-fauna-control-rules and POV consistency both require
        correct POV scoping).
      criteria: >
        NI and sensory facet authors must treat bones 71–77 as narrator-absent (Taylor does not perceive
        these events in real-time). If the episode-boundary assignment in Phase 7 does not resolve this
        ambiguity, a POV-distance relay bone (or inline POV marker per schema convention) should be added
        before bone 71.

    - id: fault-005
      type: flag
      what: >
        Beat 8, bone 144: single time-skip marker between runner-exit (bone 141) and elder-speaks-to-runner
        (bone 145) for a plan-specified two-day elapsed interval. The schema permits a single time-skip for
        any non-trivial elapsed interval, but this specific interval (two days) is narratively significant
        (the runner recalibrates and then deliberately approaches). Single time-skip may not signal the
        deliberateness of the two-day interval to location-state and NI authors.
      why: >
        If location-state and NI authors do not distinguish bones 136–143 (Watch/runner incident) and
        bones 145–155 (runner approaches via elder) as temporally separated by two days, they may treat
        them as a continuous scene. Location-state entries that inherit the prior environment without a
        time-marker would produce an incorrect scene frame for the second sub-beat.
      criteria: >
        Advisory. If the Phase 7 episode-boundary assignment places an episode break between bones 143
        and 145, the two-day gap is structurally resolved. If not, the single time-skip at 144 should be
        expanded to two consecutive time-skip markers (143/144 → 143, 144, [new-id]) to signal a longer
        skip per the schema's "multiple consecutive blank-numbered lines indicate a longer skip" convention.

    - id: fault-006
      type: flag
      what: >
        Beat 25, bones 463 and 472: two `taylor-hebert-flea-bottom holds the feet` bones in one beat.
        Feeling schema per-character per-scene cap is ≤1 (hard). If beat 25 is one scene, the feeling
        author must select one of the two bones; the other cannot fire.
      why: >
        The two holds-feet instances bracket the off-stage account-writing event (bones 467–469). If the
        feeling author selects bone 463 (first holds-feet), the beat's second half (after the account is
        sealed) has no Taylor-feeling anchor. If the feeling author selects bone 472 (second holds-feet),
        the approach sequence (455–463) has no Taylor-feeling anchor. The structural intent appears to
        require both to fire — but the schema prevents this within one scene.
      criteria: >
        Phase 7 episode-boundary assignment should determine whether bones 455–463 and 465–475 fall in
        the same episode or separate episodes. If separate, the per-scene cap allows both to fire. If
        same episode, the feeling author must choose one and document the selection with justification.
        This flag should be forwarded to the Phase 7 write-out handler.

    - id: fault-007
      type: flag
      what: >
        Beat 7, bone 111 (maester speaks to room): the tensometer author must evaluate whether ambient
        overheard speech clears the rubric's 2-threshold. The rubric explicitly states: "Speaking is by
        itself a 1" and "Rating 2/3 because the scene has stakes when this beat doesn't carry them on its
        face" is anti-pattern 1 (ambient escalation). If bone 111 does not clear, beat 7 has no escalation
        bones and requires an explicit dramatist "scene-as-transit" flag.
      why: >
        Beat 7 is structurally important (first maester detection) but the bones for the detection event
        are all relay bones (ambient/indirect). If the tensometer for beat 7 is all-1s without a
        scene-as-transit flag, the stitcher will treat the entire beat as compressible — including bone 111
        (the maester discovery). Compressing the discovery event is a narrative structure fault.
      criteria: >
        Tensometer author must: (a) evaluate bone 111 on the rubric's 2-threshold (stakes-visibility:
        is the overheard voice a watch-cost at the proto-line level, or only at the scene-frame level?);
        (b) if 111 clears as a 2, assign accordingly and document the axis-citation; (c) if 111 does not
        clear, assign 1 and flag bone 111 as "discovery-beat, scene-as-transit exemption required" for
        the dramatist's explicit documentation. Either path is acceptable; the tensometer author must not
        silently assign 1 and let the stitcher compress this bone without review.

    - id: fault-008
      type: flag
      what: >
        Beats 1–4 (bones 1–60): no explicit location slug appears in any bone for the tanner-village
        setting. Character slug is `taylor-hebert-flea-bottom` throughout, which identifies the character
        by destination-city, not origin-location. The location-state author for beats 1–4 must infer that
        the setting is the tanner-village (loc-tanner-village) from context, not from any cited loc slug.
      why: >
        The location-state facet supplies `<location-slug> | <time> | <weather> | <conditions>` entries.
        If the location slug for beats 1–4 is not inferable, the location-state author may supply a generic
        or incorrect slug, which propagates to stitcher rendering (wrong set, wrong conditions). The
        `loc-tanner-village` slug appears in the showrunner's memory stage-elements list but is not cited
        in any beat 1–4 bone.
      criteria: >
        Location-state author must be briefed that beats 1–4 are set in loc-tanner-village (per
        showrunner memory stage-elements). The loc slug should be confirmed against the active warehouse
        before authoring entries. If loc-tanner-village is not in the active warehouse's loc cards,
        Margit must be notified to onboard the card before location-state authoring begins.
```

---

## Verdict

**FACET-GAPS**

Two faults (fault-001/fault-002 share one fix target — beat 10 bone-density) are blocking: facet authors for beat 10 cannot produce material-sufficient facet files from current bones. Six flags require author-side judgment or Phase 7 coordination; none block facet authoring for the other 25 beats.

The 25 remaining beats are structurally FACET-READY for their respective facet authors with the advisory notes recorded above. The beat-10 bone-density fault must be resolved before the facet authoring pass for beat 10 begins.
