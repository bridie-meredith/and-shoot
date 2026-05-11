facet: tensometer
episode: s01e02
bones: 159-328 (+ interpolated narrative-scope: 496, 500, 501, 502, 505, 508, 509, 510, 519, 520, 521, 526, 527, 528)
author: dramatist (Phase 7 finalization from s01-window-02, revised 2026-05-11 per URI-028)
---

# URI-028 carry-forward note (2026-05-11; tens re-anchored 2026-05-11)

The bones header now declares the full narrative-scope roster per the URI-028 fix in `.claude/commands/and-season.md` Phase 7 Step 1. Boundary-carry bones 511, 512 are W2-open carry-throughs (file-position immediately after s01e01's cut at 155); they belong to e02 per the boundary-carry discipline. Cycle-3 F7-bone rescue bones in this episode: 519 (Scene A rupture), 520 (Scene H rupture), 521 (Scene L rupture). Other late-rescue bones whose file-position falls inside the e02 cut window: 496, 500, 501, 502, 505, 508, 509, 510, 526, 527, 528.

s01e02.md's per-episode body was mechanically split correctly: it already contains all 14 interpolated bones renumbered to per-episode local IDs in narrative file-order (e.g. boundary-carry season-511 → local-3; season-519 → local-22; season-520 → local-125; season-521 → local-173; season-496 → local-151; etc.). The bug was only in the tens file: window-02 retained season-global anchors (@159, @519, @521, etc.) instead of being re-anchored to per-episode local IDs at Phase 7 Step 4.

**Re-anchored 2026-05-11** (URI-028 cleanup pass). Every tens-entry anchor below has been translated from season-global ID to per-episode local ID via narrative-file-order walk against s01.bones.md. Mapping integrity: 178 local-bone positions parsed; 155 season-bones matched; 0 unresolved anchors (no orphan tens entries in e02). The body now correctly cross-references s01e02.md.

# Boundary-carry bones (W2 open, post-cycle-1 regen)
0a @3 2
0b @4 2

1 @5 1
2 @6 1
3 @7 1
4 @8 1
5 @9 1
6 @10 1
7 @11 1
8 @12 2
9 @13 1
10 @14 1
11 @15 1
12 @16 2
13 @17 2
14 @18 2
15 @19 1
16 @20 1
17 @21 1
17a @22 3
# axis: stakes-visibility + reversal-proximity peaks — father's step-back is the body acknowledging the new category; the visit's transactional outcome is now committed; Scene A rupture resolved
18 @23 1
19 @24 1
20 @25 2
21 @26 2
22 @27 1
23 @28 1
24 @30 1
25 @31 1
26 @32 1
27 @34 1
27a @35 1
# Watch-timing relay anchor for beat 10 (S7 facet-readiness fault-001 criterion 2 + fault-002 closure)
28 @37 1
29 @41 1
29a @42 1
29b @55 1
30 @44 1
31 @45 1
32 @46 1
33 @49 1
33a @50 1
34 @51 2
35 @52 1
36 @53 1
36a @54 1
37 @56 1
38 @57 1
39 @58 1
40 @60 1
41 @61 1
42 @62 1
43 @63 1
44 @64 1
45 @65 1
46 @66 1
47 @67 1
48 @68 1
49 @69 1
50 @70 1
51 @71 1
52 @72 1
53 @73 1
54 @74 1
55 @75 1
56 @76 1
57 @77 2
58 @78 2
59 @79 1
60 @80 1
61 @81 1
62 @83 1
63 @84 1
64 @85 3
65 @86 2
66 @87 3
67 @88 2
68 @89 1
69 @90 1
70 @91 1
71 @92 1
72 @93 1
73 @94 1
74 @95 1
75 @97 1
76 @98 1
77 @99 1
78 @100 1
79 @101 1
80 @102 1
81 @103 1
82 @104 2
83 @105 2
84 @106 3
85 @107 2
86 @108 1
87 @109 1
88 @110 1
89 @111 1
90 @113 1
91 @114 1
92 @115 1
93 @117 1
94 @118 1
95 @119 1
96 @120 1
97 @121 1
98 @122 1
99 @123 1
100 @124 2
101 @126 2
102 @127 2
102a @125 3
# axis: body-charge + reversal-proximity peaks — stylus-drop interrupts log-writing; headache cost interrupts the act of accounting for it; Scene H rupture resolved
103 @128 1
104 @129 1
105 @130 1
106 @132 1
107 @133 1
108 @136 1
109 @137 1
110 @138 1
111 @139 2
112 @140 2
113 @141 1
114 @142 1
115 @143 1
116 @144 1
117 @145 1
118 @146 1
119 @148 1
120 @149 2
121 @150 2
122 @151 3
123 @152 1
124 @153 1
125 @154 1
126 @156 1
127 @157 1
128 @158 1
129 @159 2
130 @160 1
131 @161 1
132 @162 1
133 @164 1
134 @165 1
135 @166 1
136 @167 2
137 @168 1
138 @169 1
139 @170 1
140 @171 1
141 @172 2
141a @173 3
# axis: reversal-proximity peaks — standing IS the commit; the disclosure becomes physical fact through the body's rising; the vigil-end is now an event, not a statement; Scene L rupture resolved
142 @174 1
143 @176 1
144 @177 1
145 @178 1

---

## Kickbacks — RESOLVED in cycle 3 F7-bone residual cleanup

- **SCENE A (159–181) — RESOLVED.** ID 519 (`oc-tanner-father steps back`) adds rupture beat after the stills-cluster; father's step-back is the body's commit to the new category for Taylor. tens-gate-residual-{W2-Scene-A} cleared.
- **SCENE E (209–225) — inert-stretch carry-forward.** Not a tens-gate-residual; flagged for editor at facet-authoring time as a network-density stretch suitable for compression in prose.
- **SCENE H (266–278) — RESOLVED.** ID 520 (`taylor-hebert-flea-bottom drops the stylus`) interrupts the log-writing during the 400m headache; the stylus-drop is the rupture. tens-gate-residual-{W2-Scene-H} cleared.
- **SCENE L (315–324) — RESOLVED.** ID 521 (`oc-tanner-mother stands`) adds the physical commit after the vigil-candle disclosure speech-acts; standing IS the commit. tens-gate-residual-{W2-Scene-L} cleared.

## Frequency-band (cycle 3 corrected — F7-bone residual cleanup)

After cycle-3 additions (@519, @520, @521 all rung 3; @526, @527 rung 1 beat-10 placement bones):
- Total entries: ~168
- 3s: 7/168 ≈ 4.2% (standard band 5-10% / relaxed band 4.0-10% per-episode) — within relaxed band at 0.2 points above the relaxed per-episode floor
- 2s: ~24/168 ≈ 14.3% (standard band 20-30% / relaxed band 12-22%) — within relaxed band
- 1s: ~137/168 ≈ 81.5% (standard band 60-75% / relaxed band 75-85%) — within relaxed band
- Scalar inflation refused (AP4 honored). Scene-level rupture criteria met in all named scenes (A, H, L). Beat-10 bones (@526, @527) rated 1 — procedural placement, no rupture.

### Frequency-band exemption claim (URI-034, 2026-05-11)

Per `design/shoot-v2/rubric-tensometer.md` §"Frequency-band exemptions" / **Exemption 5 — Tone-law-licensed slow-burn register**, this episode's frequency-band ratios are exempt-under-tone-law. Quoted positive criteria:

- **(a) tone-law citation:** `cond-series-tone-constraints-125ac` is loaded in `showrunner-memory.series.behaviors`. The card §"The Primary Register: Contemplative-Procedural-Horror" declares slow-burn / low-rupture-density register.
- **(b) quantified relaxed band:** the card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" specifies "1s: 75-85%; 2s: 12-22%; 3s: 4.5-10% season-average, 4.0-10% per-episode." This episode's per-episode rates (1s 81.5%, 2s 14.3%, 3s 4.2%) all fall inside the relaxed band.
- **(c) 3s rung discipline:** per-episode 3s rate 4.2% ≥ relaxed per-episode floor 4.0%; (c.i) every named scene in this episode carries a peak per the Kickbacks section's RESOLVED declarations (Scene A by @519, Scene H by @520, Scene L by @521); (c.ii) scalar inflation refused per AP4. Season-average 3s rate computed across s01: 21 3s / 464 entries ≈ 4.5%, at the season-avg floor.
- **(d) season-wide scope:** the tone-law applies across all four planned seasons of this series; s01e01 and s01e03 file their own Exemption 5 claims against the same card.

**Exemption verdict:** EXEMPT-UNDER-TONE-LAW.

## Window shape

Two legitimate peaks (234/236 eviction, 255 coin-exchange) + one compact (496). Eviction is window climax (middle third); coin-exchange is secondary; rhythm-stilling is tertiary. Scenes flanking climax (A before, H and L after) underloaded.

Shape: partial rise-peak-fall with climax in middle third.
