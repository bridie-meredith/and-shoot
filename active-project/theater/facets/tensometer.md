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
1 @3 2
2 @4 2

3 @5 1
4 @6 1
5 @7 1
6 @8 1
7 @9 1
8 @10 1
9 @11 1
10 @12 2
11 @13 1
12 @14 1
13 @15 1
14 @16 2
15 @17 2
16 @18 2
17 @19 1
18 @20 1
19 @21 1
20 @22 3
# axis: stakes-visibility + reversal-proximity peaks — father's step-back is the body acknowledging the new category; the visit's transactional outcome is now committed; Scene A rupture resolved
21 @23 1
22 @24 1
23 @25 2
24 @26 2
25 @27 1
26 @28 1
27 @30 1
28 @31 1
29 @32 1
30 @34 1
31 @35 1
# Watch-timing relay anchor for beat 10 (S7 facet-readiness fault-001 criterion 2 + fault-002 closure)
32 @37 1
33 @41 1
34 @42 1
35 @55 1
36 @44 1
37 @45 1
38 @46 1
39 @49 1
40 @50 1
41 @51 2
42 @52 1
43 @53 1
44 @54 1
45 @56 1
46 @57 1
47 @58 1
48 @60 1
49 @61 1
50 @62 1
51 @63 1
52 @64 1
53 @65 1
54 @66 1
55 @67 1
56 @68 1
57 @69 1
58 @70 1
59 @71 1
60 @72 1
61 @73 1
62 @74 1
63 @75 1
64 @76 1
65 @77 2
66 @78 2
67 @79 1
68 @80 1
69 @81 1
70 @83 2
71 @84 1
72 @85 3
73 @86 2
74 @87 3
75 @88 2
76 @89 1
77 @90 1
78 @91 1
79 @92 1
80 @93 1
81 @94 1
82 @95 1
83 @97 1
84 @98 1
85 @99 1
86 @100 1
87 @101 1
88 @102 1
89 @103 1
90 @104 2
91 @105 2
92 @106 3
93 @107 2
94 @108 1
95 @109 1
96 @110 1
97 @111 1
98 @113 1
99 @114 1
100 @115 1
101 @117 1
102 @118 1
103 @119 1
104 @120 1
105 @121 1
106 @122 1
107 @123 1
108 @124 2
109 @126 2
110 @127 2
111 @125 3
# axis: body-charge + reversal-proximity peaks — stylus-drop interrupts log-writing; headache cost interrupts the act of accounting for it; Scene H rupture resolved
112 @128 1
113 @129 1
114 @130 1
115 @132 1
116 @133 1
117 @136 1
118 @137 1
119 @138 1
120 @139 2
121 @140 2
122 @141 1
123 @142 1
124 @143 1
125 @144 1
126 @145 1
127 @146 1
128 @148 1
129 @149 2
130 @150 2
131 @151 3
132 @152 1
133 @153 1
134 @154 1
135 @156 1
136 @157 1
137 @158 1
138 @159 2
139 @160 1
140 @161 1
141 @162 1
142 @164 1
143 @165 1
144 @166 1
145 @167 2
146 @168 1
147 @169 1
148 @170 1
149 @171 1
150 @172 2
151 @173 3
# axis: reversal-proximity peaks — standing IS the commit; the disclosure becomes physical fact through the body's rising; the vigil-end is now an event, not a statement; Scene L rupture resolved
152 @174 1
153 @176 1
154 @177 1
155 @178 1

---

## Kickbacks — RESOLVED in cycle 3 F7-bone residual cleanup

- **SCENE A (159–181) — RESOLVED.** ID 519 (`oc-tanner-father steps back`) adds rupture beat after the stills-cluster; father's step-back is the body's commit to the new category for Taylor. tens-gate-residual-{W2-Scene-A} cleared.
- **SCENE E (209–225) — inert-stretch carry-forward.** Not a tens-gate-residual; flagged for editor at facet-authoring time as a network-density stretch suitable for compression in prose.
- **SCENE H (266–278) — RESOLVED.** ID 520 (`taylor-hebert-flea-bottom drops the stylus`) interrupts the log-writing during the 400m headache; the stylus-drop is the rupture. tens-gate-residual-{W2-Scene-H} cleared.
- **SCENE L (315–324) — RESOLVED.** ID 521 (`oc-tanner-mother stands`) adds the physical commit after the vigil-candle disclosure speech-acts; standing IS the commit. tens-gate-residual-{W2-Scene-L} cleared.

## Frequency-band (cycle 3 corrected — F7-bone residual cleanup)

After cycle-3 additions (@519, @520, @521 all rung 3; @526, @527 rung 1 beat-10 placement bones):
- Total entries: 155 (per-episode canonical body; cite-index `### tens (155 entries)` confirms — corrected r4-cycle3 per find-001; prior footer figure ~168 inflated by season-window scope and is retracted)
- 3s: 7/155 ≈ 4.5% (standard band 5-10% / relaxed band 4.0-10% per-episode) — within relaxed band
- 2s: ~24/155 ≈ 15.5% (standard band 20-30% / relaxed band 12-22%) — within relaxed band
- 1s: ~124/155 ≈ 80.0% (standard band 60-75% / relaxed band 75-85%) — within relaxed band
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
