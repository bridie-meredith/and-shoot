facet: tensometer
episode: s01e03
bones: 330-494 (+ interpolated narrative-scope: 497, 498, 499, 503, 507, 513, 514, 522, 523, 524)
author: dramatist (Phase 7 finalization from s01-window-03, revised 2026-05-11 per URI-028)
---

# URI-028 carry-forward note (2026-05-11; tens re-anchored 2026-05-11)

The bones header is now expressed in the URI-028 honest form: contiguous range 330-494 plus interpolated narrative-scope bones whose file-position falls inside the e03 cut window. Boundary-carry bones 513, 514 are W3-open carry-throughs from e02's close region. Late-rescue bones 522, 523, 524 are the cycle-3 F7-bone rescue rupture additions for Scenes 330-342, 361-375, and 477-494 respectively; bones 497, 498, 499, 503, 507 are earlier cycle additions whose file-position falls inside the e03 window. The interpolated list is exhaustive for this window per the `s01.bones.md` file-position scan.

s01e03.md's per-episode body was mechanically split correctly: it already contains all 10 interpolated bones renumbered to per-episode local IDs in narrative file-order (e.g. boundary-carry season-513 → local-1; season-522 → local-11; season-523 → local-42; season-524 → local-162; season-497 → local-31; etc.). The bug was only in the tens file: window-03 retained season-global anchors (@330, @522, @523, @524, etc.) instead of being re-anchored to per-episode local IDs at Phase 7 Step 4.

**Re-anchored 2026-05-11** (URI-028 cleanup pass). Every tens-entry anchor below has been translated from season-global ID to per-episode local ID via narrative-file-order walk against s01.bones.md. Mapping integrity: 165 local-bone positions parsed; 155 season-bones matched; 2 orphan entries pruned (`# 21 @353` and `# 107 @447` — season-bones deleted in earlier cycles, tens entries not pruned at the time). The body now correctly cross-references s01e03.md. Total active tens entries post-prune: ~153.

# Boundary-carry bones (W3 open, post-cycle-1 regen)
0a @1 2
0b @2 2
# 0c @515 removed (proto-line deleted in cycle 2 fixer)

1 @3 1
2 @4 2
3 @5 1
4 @6 1
5 @7 2
6 @8 2
7 @9 1
7a @11 3
# axis: stakes-visibility + reversal-proximity peaks — clerk crosses Fish Gate with the file entry; the recording physically leaves Taylor's observable range; Scene 330-342 rupture resolved
8 @10 1
9 @12 1
10 @13 1
11 @14 1
12 @15 1
13 @16 1
14 @18 1
15 @19 1
16 @20 1
17 @21 1
18 @22 1
19 @23 1
20 @24 1
# 21 @353 — orphan (season-bone 353 deleted in earlier cycle; tens entry pruned at URI-028 re-anchor 2026-05-11)
22 @25 1
23 @26 2
24 @27 2
25 @28 1
26 @29 1
27 @30 1
28 @31 1
29 @33 1
30 @34 1
31 @35 1
32 @36 1
33 @37 1
34 @38 1
35 @39 2
36 @40 2
36a @42 3
# axis: stakes-visibility peaks — second clerk releases the record book; the entry is sealed; the file's second commit is irreversible; Scene 361-375 rupture resolved
37 @41 1
38 @43 1
39 @44 1
40 @45 1
41 @46 1
42 @47 1
43 @48 1
44 @50 2
45 @51 2
46 @52 1
47 @53 1
48 @54 2
49 @56 1
50 @57 1
51 @58 1
52 @59 2
53 @60 1
54 @61 1
55 @62 2
56 @63 1
57 @64 1
58 @65 1
59 @66 2
60 @67 3
61 @68 3
62 @69 1
63 @70 1
64 @71 1
65 @73 1
66 @74 1
67 @75 1
68 @76 1
69 @77 1
70 @78 1
71 @79 1
72 @80 1
73 @81 1
74 @82 1
75 @83 2
76 @84 2
77 @85 1
78 @86 1
79 @87 1
80 @88 1
81 @89 2
82 @90 3
83 @91 2
84 @92 1
85 @93 1
86 @94 1
87 @96 1
88 @97 2
89 @98 2
90 @99 1
91 @100 2
92 @101 2
93 @102 2
94 @103 2
95 @104 1
96 @105 2
97 @106 1
98 @107 1
99 @108 1
100 @110 1
101 @111 1
102 @112 1
103 @113 1
104 @114 1
105 @115 1
106 @116 1
# 107 @447 — orphan (season-bone 447 deleted in earlier cycle; tens entry pruned at URI-028 re-anchor 2026-05-11)
108 @117 1
109 @118 2
110 @119 2
111 @120 1
112 @121 2
113 @122 1
114 @123 1
115 @124 1
116 @125 2
117 @127 1
118 @128 2
119 @129 2
120 @130 1
121 @131 2
122 @132 1
123 @133 2
# @462 orphan removed (proto-line deleted in cycle 1 dedup)
125 @134 2
126 @136 1
127 @137 1
128 @138 2
129 @139 3
130 @140 2
131 @141 1
132 @142 1
133 @143 2
134 @144 1
135 @145 1
136 @146 1
137 @148 1
138 @149 1
139 @150 1
140 @151 1
141 @152 1
142 @153 2
143 @154 1
144 @155 1
145 @156 1
146 @157 1
147 @158 1
148 @159 2
149 @160 1
150 @161 1
150a @162 3
# axis: reversal-proximity + body-charge — wall-facing IS the decision to record the close-states as coincidence; the season's terminal reader-asymmetry is committed through Taylor's body before the log entries; denouement registration resolved
151 @163 1
152 @164 1
# @493 orphan removed (proto-line deleted in cycle 1 dedup)
154 @165 1

---

## Frequency band (cycle 3 F7-bone residual cleanup)

After cycle-2 rerates (@335 3→2, @368 3→2), orphan removals (@462, @493, 0c@515), cycle-2 boundary-carry additions (0a@513, 0b@514), and cycle-3 rupture additions (@522, @523, @524 all rung 3):

- Total entries: ~155
- 3s: 7/155 ≈ 4.5% (standard band 5-10% / relaxed band 4.0-10% per-episode) — within relaxed band; below standard floor by 0.5 points
- 2s: ~47/155 ≈ 30.3% (standard band 20-30%) — at upper edge of standard band
- 1s: ~101/155 ≈ 65.2% (standard band 60-75%) — within standard band

3-frequency at 4.5% is an honest improvement from the cycle-1 reading of 2.6%. The three cycle-3 rupture additions (@522, @523, @524) provide scene-level structural resolution: each named scene now carries a legitimate 3. Scalar inflation refused per AP4.

### Frequency-band exemption claim (URI-034, 2026-05-11)

Per `design/shoot-v2/rubric-tensometer.md` §"Frequency-band exemptions" / **Exemption 5 — Tone-law-licensed slow-burn register**, the 3s rung's below-standard-floor reading is exempt-under-tone-law. Note: 2s and 1s are within the standard band — this episode's third-window pacing carries the season's higher-rupture-density region (Hightower files closing, denouement walk) and matches the standard band more closely than s01e01/e02. Only the 3s rung needs the exemption.

Quoted positive criteria:

- **(a) tone-law citation:** `cond-series-tone-constraints-125ac` is loaded in `showrunner-memory.series.behaviors`. Card §"The Primary Register: Contemplative-Procedural-Horror" declares slow-burn / low-rupture-density register.
- **(b) quantified relaxed band:** card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" specifies "3s: 4.5-10% season-average, 4.0-10% per-episode." This episode's 3s rate (4.5%) is at the relaxed season-average floor and 0.5 points above the relaxed per-episode floor.
- **(c) 3s rung discipline:** per-episode 3s rate 4.5% ≥ relaxed per-episode floor 4.0%; (c.i) every named scene in this episode carries a peak per Screen-writer kickback §RESOLVED declarations (Scene 330-342 by @522, Scene 361-375 by @523, Scene 477-494 by @524) plus the structural climax @468 (sealed account); (c.ii) scalar inflation refused per AP4. Season-average 3s rate across s01: 21/464 ≈ 4.5%, at the season-avg floor.
- **(d) season-wide scope:** the tone-law applies across all four planned seasons of this series; s01e01 and s01e02 file their own Exemption 5 claims against the same card.

**Exemption verdict:** EXEMPT-UNDER-TONE-LAW.

Active 3s: @394 (coin placed), @395 (Taylor closes fist), @417 (maester sets the pen), @468 (elder seals account), @522 (clerk crosses Fish Gate), @523 (second clerk releases record book), @524 (Taylor faces wall at denouement).

## Screen-writer kickback (cycle 3 resolution)

- **Scene 330–342 (first Hightower clerk) — RESOLVED.** ID 522 (`the clerk crosses the Fish Gate`) adds rupture: the file physically leaves Taylor's observable range. Stakes-visibility + reversal-proximity 3. tens-gate-residual-{W3-Scene-330-342} cleared.
- **Scene 361–375 (second clerk, apothecary) — RESOLVED.** ID 523 (`the second clerk releases the record book`) adds rupture: the sealing of the entry is irreversible. Stakes-visibility 3. tens-gate-residual-{W3-Scene-361-375} cleared.
- **Scene 477–494 (full circuit denouement walk) — RESOLVED.** ID 524 (`taylor-hebert-flea-bottom faces the wall`) adds registration: the physical commitment to recording the close-states as coincidence. Reversal-proximity + body-charge 3. tens-gate-residual-{W3-Scene-477-494} cleared.

tens-gate-residual-{W3-structural-3-deficit} partially resolved: scene-level rupture criteria met in all named scenes. Window 3-frequency improved to 4.5%; below 5% floor remains noted.

## Curve verdict

Rise-peak-fall present at window scope. Structural climax at @468 (sealed account). Active 3s at @394, @395, @417, @468, @522, @523, @524 form credible escalation; clerk scenes now carry rupture peaks; denouement registration now anchored. Window 3 passes curve-shape review. 3-frequency at 4.5% noted (below 5% floor but scene-level criteria now met).

## Screen-writer flag (advisory)

Maester-market trip (IDs 400–422) carries no rupture bone. Buy/refuse decision at stall is implied not explicit (@410 faces jars + @411 exits without purchase). If scene intends dramatic weight beyond transit, a commit bone is missing. Flagged for screen-writer awareness.

## Axis citations summary

3s justified:
- @394: stakes-visibility + reversal-proximity peaks — elder places coin; irreversible registration
- @395: body-charge peaks — Taylor closes fist on coin; double-tap with @394 (two parties committing the same turn)
- @417: reversal-proximity peaks — oc-broken-maester sets the pen; the discrete act of stopping his writing reverses prior motion (the pen-scratch session terminates)
- @468: three axes light (stakes-visibility + reversal-proximity + body-charge) — elder seals account; structural climax
- @522: stakes-visibility + reversal-proximity peaks — clerk crosses Fish Gate; the entry-bearing file physically leaves Taylor's observable range; recording is beyond reach
- @523: stakes-visibility peaks — second clerk releases the record book; the entry is sealed; irreversible second commit
- @524: reversal-proximity + body-charge peaks — wall-facing IS the decision to record the close-states as coincidence; the season's terminal reader-asymmetry committed through Taylor's body before the log entries

Previously rated 3, downgraded in cycle 2:
- @335 (3→2): clerk writes entry; rubric-compliant rating 2 (plot-importance inflation; cycle 2 finding)
- @368 (3→2): second clerk writes entry; same pattern
