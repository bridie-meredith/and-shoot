---
audit: facets-final-r5
episode: s01e01
date: 2026-05-11
mode: flag-only
status: CLEAN
totals:
  hard: 0
  signal: 2
  exempt: 1
  pass: 9
---

# Facets Final Audit R5 — s01e01

Auditor: cross-cutting graph auditor fork (Phase 5 re-audit, fifth pass)
Trigger: r4-signal-001 (feeling.md multi-source YAML blocks) and r4-signal-002 (mem:9 Earth-Bet
  slug) addressed by fixer. r5 is independent re-derivation confirming closure of both and
  re-scanning full graph for any new findings.
Mode: FLAG-ONLY. Independent re-derivation; r4 findings not carried forward unless independently
  re-derived from current file state.

Inputs read (independent re-derivation):
  - proto-lines: active-project/theater/proto-lines/s01e01.md
  - facets: active-project/theater/facets/tensometer-s01e01.md (archive),
             active-project/theater/facets/location-state.md,
             active-project/theater/facets/interest-narrator.md,
             active-project/theater/facets/sensory.md,
             active-project/theater/facets/state-updates.md,
             active-project/theater/facets/memory.md,
             active-project/theater/facets/feeling.md,
             active-project/theater/facets/metaphor.md,
             active-project/theater/facets/vibes.md
  - active-project/theater/facets/_cite-index.md
  - active-project/theater/facets/.r2-decisions.md (not re-read at r5 — Phase 4 consolidation
    not mutated between r4 and r5; cite-index is live authority)
  - active-project/staff/showrunner/memory.md
  - schemas/facet.schema.md, schemas/audit-report.schema.md
  - design/shoot-v2/rubric-tensometer.md (including §Frequency-band exemptions)
  - cards/conditions/cond-series-tone-constraints-125ac.card.md
  - prior audit: active-project/staff/auditor/facets-final-audit-r4.md (context only;
    not carried forward)

Forbidden (not loaded): behavior cards, vibes-as-bias, audience personas, source prose.

---

## Class 1: STRUCTURAL

### 1-A: PASS — feeling.md top-of-file frontmatter (r4-signal-001 closure check)

feeling.md scanned from line 1.

Lines 1–5:
```
---
facet: feeling
sources: [oc-broken-maester, oc-dock-runner, oc-tanner-elder, oc-tanner-father, oc-tanner-mother, taylor-hebert-flea-bottom]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---
```

Single conformant YAML frontmatter block at file open. PASS on frontmatter-exists criterion.

### 1-B: PASS — feeling.md per-source section format (r4-signal-001 closure check — primary)

r4-signal-001 identified that per-source sections within feeling.md carried secondary YAML
frontmatter blocks (`facet:` / `episode:` / `character:` / `author:` / `r2-pass:` / `---`)
after each `# source:` comment-line header, matching the defect r3-signal-001 addressed in
state-updates.md. The criterion was: convert those per-source YAML blocks to plain comment lines.

Independent scan of each per-source section in the current feeling.md:

**# source: oc-broken-maester** (line 7):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: oc-broken-maester  author: r1-feeling-oc-broken-maester  r2-pass: r2-judge-oc-broken-maester`
This is a `#`-prefixed comment line. No subsequent `---` YAML block follows before the first
entry line (`1 @129 oc-broken-maester: ...`). CLEAN.

**# source: oc-dock-runner** (line 13):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: oc-dock-runner  author: r1-feeling-author  r2-judge: r2-feeling-judge-oc-dock-runner (2026-05-11)`
Plain comment. No YAML block between this comment and entry `2 @143 oc-dock-runner: ...`. CLEAN.

**# source: oc-tanner-elder** (line 105):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: oc-tanner-elder  author: feeling-author-oc-tanner-elder  r2-pass: judge (2026-05-11)`
Plain comment. No YAML block between comment and entry `3 @90 oc-tanner-elder: ...`. CLEAN.

**# source: oc-tanner-father** (line 163):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: oc-tanner-father  author: R1 feeling fork — oc-tanner-father  r2-judge: 2026-05-11 — KEEP x3, ADD x0, DELETE x0, CAP-REFUSAL x1 (graph-aware re-pass)`
Plain comment. No YAML block before entry `5 @14 oc-tanner-father: ...`. CLEAN.

**# source: oc-tanner-mother** (line 301):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: oc-tanner-mother  author: r1-feeling-fork-oc-tanner-mother  r2-pass: 2026-05-11 (graph-aware judge; B-locked-rubric v2; C-arbiter v2)`
Plain comment. No YAML block before entry `8 @43 oc-tanner-mother: ...`. CLEAN.

**# source: taylor-hebert-flea-bottom** (line 385):
Following line reads: `# slice file — facet: feeling  episode: s01e01  character: taylor-hebert-flea-bottom  author: r1-feeling-fork  r2-judge: 2026-05-11 (graph-aware pass, locked-rubric discipline)`
Plain comment. No YAML block before entry `10 @20 taylor-hebert-flea-bottom: ...`. CLEAN.

All six per-source sections carry plain `# slice file — ...` comment headers. No secondary YAML
frontmatter blocks present. **r4-signal-001 CLOSED. PASS.**

### 1-C: PASS — state-updates.md frontmatter (carry-forward from r3-signal-001 / r4 confirm)

state-updates.md lines 1–5 confirmed carrying single conformant frontmatter block:
```
---
facet: state-updates
sources: [env, oc-broken-maester, oc-dock-runner, oc-tanner-elder, oc-tanner-father, oc-tanner-mother, taylor-hebert-flea-bottom]
note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter per r3-signal-001.
---
```
Per-source divisions use plain `# source: <name>` comment headers. No secondary YAML blocks.
Consistent with r4 pass. PASS.

### 1-D: PASS — Tensometer ID monotonicity

tensometer-s01e01.md body scanned. Entry IDs run with documented gaps from prior strip
(IDs 79–80, 123, 129, 143–146 absent due to C1 remediation). Surviving IDs are positive
integers in monotonically non-decreasing order. No alpha-suffix IDs in the finalized per-episode
file (alpha-suffix convention applies only to -window- intermediate files per schema). PASS.

### 1-E: PASS — Out-of-range anchors

tensometer-s01e01.md body contains no anchors outside the s01e01 aggregate range 1–155.
Confirmed @495, @504, @506, @516, @517, @518, @525 absent from body. C1 strip confirmed
complete. PASS.

### 1-F: PASS — Anchor resolution (all facets)

Cite-index back-links verified. All entries marked `back=Y` in the cite-index resolve to
proto-line IDs within 1–155. No unresolved anchor found. The lonely-entry list (feel:7 @93,
state:17 @144, and scattered tens entries) all carry `back=Y` — they are undecorated by other
facets but their own anchors resolve to proto-lines within range. PASS.

### 1-G: PASS — Header/frontmatter presence (all single-file facets)

tensometer-s01e01.md, location-state.md, interest-narrator.md, sensory.md, metaphor.md,
vibes.md each carry a single conformant frontmatter block. The consolidated state-updates.md
carries single top-of-file frontmatter (per 1-C). feeling.md carries single top-of-file
frontmatter (per 1-A). No secondary YAML blocks in any file. PASS.

### 1-H: PASS — feeling.md ID monotonicity

feeling.md consolidated body runs IDs 1 through 13 across six source sections sequentially:
oc-broken-maester: 1
oc-dock-runner: 2
oc-tanner-elder: 3, 4
oc-tanner-father: 5, 6, 7
oc-tanner-mother: 8, 9
taylor-hebert-flea-bottom: 10, 11, 12, 13

Monotonically increasing, no gaps, no repeats. Consistent with cite-index `feel (13 entries)`.
PASS.

### 1-I: PASS — Proto-body integrity

Proto-lines file header states aggregate_range 1–155 with URI-028 carry-forward note. Body
contains bones 1–159 with documented time-skip blanks (24, 35, 47, 62, 71, 80, 84, 97, 108,
119, 128, 138, 147, 156). All non-blank bone IDs fall within 1–155. URI-028 carry-forward note
accurate and consistent with tensometer-s01e01.md §"URI-028 carry-forward note". PASS.

---

## Class 2: FREQUENCY-BAND

### Independent baseline recount

From tensometer-s01e01.md working file body, full scan of `<id> @<pid> <r>` lines:

3s entries: @15=3, @43=3, @75=3, @86=3, @90=3, @134=3, @140=3, @151=3 → **8 entries**

2s entries: @7=2, @11=2, @13=2, @14=2, @42=2, @66=2, @74=2, @76=2, @87=2, @89=2, @111=2,
@112=2, @113=2, @131=2, @139=2, @141=2, @142=2, @148=2, @149=2, @150=2, @152=2 → **21 entries**

1s entries: total 141 - 8 - 21 = **112 entries**

Verification: 8 + 21 + 112 = 141. Consistent with file §Frequency-band: "Total entries: 141".

Rates:
- 3s: 8/141 = 5.67% ≈ 5.7%
- 2s: 21/141 = 14.89% ≈ 14.9%
- 1s: 112/141 = 79.43% ≈ 79.4%

Standard band: 1s 60-75% / 2s 20-30% / 3s 5-10%.
Breaches detected: 2s below floor (14.9% vs 20%); 1s above ceiling (79.4% vs 75%).
3s: 5.7% is within the standard band (5-10%). No 3s breach.

### Exemption 5 evaluation — flag-005 re-verification

Per `design/shoot-v2/rubric-tensometer.md` §"Frequency-band exemptions / Exemption 5":

**(a) Tone-law card loaded; card body contains required vocabulary:**

showrunner/memory.md `series.behaviors` lists `cond-series-tone-constraints-125ac`. Card is
active. Card §"The Prohibited Registers" / "Tensometer register characterization:" contains:
"This project authors in the slow-burn / low-rupture-density register, with foreknowledge-clamp
as primary register. The standard tens frequency-band gate (1s 60-75% / 2s 20-30% / 3s 5-10%)
does not apply to seasons authored under this tone-law."

Tokens present: `slow-burn` (exact), `low-rupture-density` (exact), `foreknowledge-clamp as
primary register` (rubric matches `foreknowledge-clamp-as-primary-register`), plus explicit
tens-gate exemption declaration. Criterion (a): **SATISFIED.**

**(b) Card specifies quantified relaxed band:**

Card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" specifies:
- 1s: 75-85%
- 2s: 12-22%
- 3s: 4.5-10% season-average, 4.0-10% per-episode

Per-episode actual: 1s 79.4% (within 75-85%), 2s 14.9% (within 12-22%), 3s 5.7% (within
4.0-10% per-episode, and also within standard 5-10%). All three rungs within the card's relaxed
band. Criterion (b): **SATISFIED.**

**(c) 3s rung discipline:**

Per-episode 3s 5.7% ≥ 4.0% per-episode floor. PASS.

Season-average 3s (from showrunner/memory.md per_episode_tens_band_verdict, using live-body
figure for s01e01):
- s01e01: 5.7% (live body count)
- s01e02: 4.2%
- s01e03: 4.5%
- Season average: (5.7 + 4.2 + 4.5) / 3 = 4.8% ≥ 4.5% season floor. PASS.

(c.i) All named scenes carry peaks: tensometer §"3s justified" section lists @15, @43, @75, @86,
@90, @134, @140, @151 covering scenes A, C, F, H, L, M, N. Transit-excepted scenes B/D/G/I/K
and KICKBACK-declared scenes E/J are properly excepted. PASS.

(c.ii) Cycle-3 F7-bone rescue scenes used screen-writer rupture additions not scalar inflation,
per tensometer footer documentation. AP4 honored. PASS.

Criterion (c): **SATISFIED.**

**(d) Season-wide scope:**

Card §"Duration": "Persistent across all four seasons. Series-defining rules." Sibling episodes
s01e02 and s01e03 independently file Exemption 5 claims against this same card per showrunner
memory. Criterion (d): **SATISFIED.**

**Exemption 5 verdict: EXEMPT-TONE-LAW-SLOW-BURN**

All four criteria (a)–(d) satisfied with quoted evidence from the live card body. The 2s/1s
standard-band breaches are fully absorbed by the card's relaxed band. flag-005 (prior UPHELD-HARD
from r2, closeable per r4) closes as `exempt-tone-law-slow-burn`. No HARD finding.

- id: flag-005-r5-confirm
- type: pass
- class: FREQUENCY-BAND
- status: EXEMPT-TONE-LAW-SLOW-BURN
- what: tensometer-s01e01.md frequency-band section; Exemption 5 claim under
  `cond-series-tone-constraints-125ac`
- verdict: All four criteria satisfied on independent re-read of live card. Exemption stands.

---

## Class 3: METADATA-INCONSISTENCY

### 3-A: PASS — interest-narrator.md density metadata

interest-narrator.md carries pre-R2 figure 38/155 = 24.5% marked `[SUPERSEDED — pre-R2 figure;
see post-R2 density below]` and confirmed post-R2 density 39/155 ≈ 25.2%. Cite-index records
39 narrator entries. Consistent. PASS.

### 3-B: PASS — tensometer-s01e01.md header bones field

Frontmatter `bones: 1-155 (+ interpolated narrative-scope: 495, 504, 506, 516, 517, 518, 525)`.
Matches proto-lines file header. Frequency-band section reports 141 total entries; independent
recount confirms 141. PASS.

### 3-C: PASS — Cite-index totals

Cite-index header: "totals: 261 facet entries; 135/146 protolines decorated (92.5%)."

Per-facet entry counts from cite-index body:
- tens: 141
- loc-state: 3
- narrator: 39
- sensory: 5
- state: 34
- mem: 7
- feel: 13
- meta: 1
- vibes: 18
Sum: 141+3+39+5+34+7+13+1+18 = 261. Matches stated total. PASS.

### 3-D: PASS — showrunner/memory.md per_episode_tens_band_verdict consistency

Memory record shows s01e01: {1s: 80.1, 2s: 14.9, 3s: 5.0}. These are pre-r3-signal-004 figures.
Live body shows 1s: 79.4%, 2s: 14.9%, 3s: 5.7% after the @134 rung 1→3 correction. The memory
field is a recorded snapshot, not the canonical source; the discrepancy (0.7 points on 3s and 1s)
is traceable to the documented rung correction and does not affect any classification. No
downstream consumer is gated on the memory snapshot. PASS. (Note for showrunner: update snapshot
to {1s: 79.4, 2s: 14.9, 3s: 5.7} at next memory sync.)

---

## Class 4: CURVE-SHAPE

### 4-A: PASS — @134 rung alignment (confirmed)

tensometer-s01e01.md body entry 126: `126 @134 3`. Rung is 3.
Cite-index: `tens:126 @134 r=3 back=Y co=[mem:4, narrator:34, state:14]`. Consistent.
Curve verdict "3s justified" section includes @134: "reversal-proximity peaks — beetles fall
silent; the network's collective absence-act IS the Scene L rupture (KICKBACK-3 RESOLVED at
Phase 3 cycle 3)." No contradiction between body, archive, curve verdict, and cite-index. PASS.

### 4-B: PASS — Scene-level shape (full scan)

Scene A (@1–@23): 1/1/1/1/1/1/2/1/1/1/2/1/2/2/3=@15/1/1/1/1/1/1/1/1.
Rise via rungs 2/@7, 2/@11, 2/@13, 2/@14 into @15=3; release @16=1. Shape: PASS.

Scene B (@25–@34): transit exception declared. No 3 required. EXEMPT.

Scene C (@36–@46): 1/1/1/1/1/1/1/2/@42/3=@43/1/1/1.
Rise via @42=2 into @43=3; release @44=1. Shape: PASS.

Scene D (@48–@60): transit exception declared. No 3 required. EXEMPT.

Scene E (@62–@70): KICKBACK-1 declared (rise without peak; reeve-slowing raises watch-cost
but no registration beat; correctly handled as kickback, not scalar inflation). KICKBACK-DECLARED.

Scene F (@71–@83): ..1/1/2=@74/3=@75/2=@76/1=@77/1/1/1/1...
Rise via @74=2 into @75=3; release @76=2→@77=1. Shape: PASS.

Scene G/H (@85–@96): Approach zone G (transit exception granted) into climax cluster H.
H peaks: @86=3 (elder routes Taylor, routing-as-irreversible-commitment) and @90=3 (gate-
crossing, point of no return). Pattern: rise @85=1, @86=3, @87=2, @88=1, @89=2, @90=3.
The 3→3 double-tap (@86/@90) satisfies the rubric condition "second 3 reverses or commits
the first" — @90 commits @86's routing-act as the gate-cross. Shape: PASS.

Scene I (@97–@107): transit exception declared. No 3 required. EXEMPT.

Scene J (@108–@127): KICKBACK-2 declared (sustained 2s without rupture; KICKBACK flag correct;
not scalar inflation). KICKBACK-DECLARED.

Scene K (@120–@127): transit exception declared. EXEMPT.

Scene L (@128–@137): @129=1, @130=1, @131=2, @132=1, @133=1, @134=3, @136=1.
Direct 1→3 jump at @134 documented as canonical sudden-turn (sudden-fauna-silence rupture;
KICKBACK-3 RESOLVED with @134=3). Shape: PASS (documented sudden-turn per curve verdict).

Scene M (@139–@146): @139=2, @140=3, @141=2, @142=2.
Rise via @139=2 into @140=3; release @141=2. Shape: PASS.

Scene N (@148–@155): @148=2, @149=2, @150=2, @151=3, @152=2, @153=1.
Rise via @148=2/@149=2/@150=2 into @151=3; release @152=2/@153=1. Shape: PASS.

**Episode-level act structure:** climax cluster in Scene H (@86, @90) as the densest pair of 3s,
with Scene N's @151 as a secondary resolved-commit peak. Peak density in mid-to-late episode,
not first-third. No structural inversion. PASS.

**Flatlining:** no run of 30+ consecutive beats rated 1 only. Scene J is the longest low-density
zone (KICKBACK-2 declared). No flatline in PASS-required zones. PASS.

**CURVE-SHAPE verdict: SHAPE-CLEAN.** All named scenes pass or carry documented kickback/transit
exceptions. No residual shape anomaly.

---

## Class 5: CONTRADICTION

### 5-A: PASS — @134 rung cross-facet

tensometer body, cite-index (r=3), state-updates commentary ("tens entry @134 (@518 aggregate)
= 3, reversal-proximity peak"), and interest-narrator SEAM-2 note all agree @134 = rung 3.
No contradiction. PASS.

### 5-B: PASS — State chain consistency

Taylor: loc-tanner-village → loc-flea-bottom (@98, state:31) → loc-flea-bottom-base (@103,
state:32). Consistent with proto-lines @98 "enters loc-flea-bottom" and @103 "enters
loc-flea-bottom-base."

oc-dock-runner: loc-flea-bottom → fish-gate-margin (@141, state:16) → loc-flea-bottom (@144,
state:17) → market-side-junction (@149, state:18) → loc-flea-bottom (@155, state:19). Chain
consistent; each <old> matches prior <new>.

oc-tanner-elder: loc-flea-bottom → tanner-family-yard (@85, state:20) → on-road (@95, state:21)
→ flea-bottom-market-side-junction (@148, state:22). Consistent.

oc-tanner-father: location-sub outside-tanner-room → tanner-room (@4, state:23) → tanner-yard
(@19, state:24). Consistent.

oc-tanner-mother: position elsewhere → in-the-room (@5, state:25) → in-the-room (@36, state:26)
→ elsewhere-in-cottage (@46, state:27). Consistent with documented offstage-exit assumption.

Taylor inventory: [] → [travel-pack] (@91, state:30) → [] (@104, state:33). Consistent.
prop:oc-travel-pack: stored-tanner-home → carried-by-taylor (@91, state:5) → set-at-loc-flea-
bottom-base (@104, state:11). Consistent and complementary to inventory entries.

PASS.

### 5-C: PASS — Location-state vs state-updates consistency

loc-state:1 @98 and state:6/@31 @98 both fire on Flea Bottom arrival. Consistent.
loc-state:2 @103 and state:10/@32 @103 both fire on Flea Bottom Base arrival. Consistent.
loc-state:3 @152 Watch-passage condition consistent with state:15 @139 watch-patrol arrival
and elapsed beats to @152. PASS.

---

## Class 6: DEDUP

### 6-A: PASS — No duplicate IDs within any facet file

All nine facet files: no ID repeated within a file. state-updates.md IDs 1–34 across six source
sections: sequential and unique. feeling.md IDs 1–13 across six source sections: sequential and
unique. PASS.

### 6-B: PASS — No duplicate anchor+content entries

Multi-fire instances on the same anchor verified from cite-index:
- @43: vibes:8 and vibes:9 — distinct keywords/targets (grief-without-object vs asking-around-
  the-edge). Non-duplicate.
- @77: vibes:2 and vibes:17 — distinct targets (taylor-hebert-flea-bottom vs episode-scope). Non-duplicate.
- @90: vibes:3 and vibes:10 — distinct character targets (Taylor vs elder). Non-duplicate.
- @103: vibes:15 and vibes:16 — distinct keywords (first-lodging-anchored vs maester-connectivity-
  established); state:10 and state:32 — complementary fields (location + placement-status). Non-duplicate.
- @130: vibes:11 and vibes:18 — distinct targets (actor:oc-broken-maester vs episode-scope). Non-duplicate.
- @91: state:5 (prop:oc-travel-pack.position) and state:30 (actor:taylor-hebert-flea-bottom.inventory)
  — complementary fields on different target namespaces. Non-duplicate.

No within-facet-same-anchor content duplication found. PASS.

---

## Class 7: SUPERFLUOUS

### 7-A: PASS — Lonely entries rubric scrutiny

Cite-index lonely entries (no co-location, no inbound license):
- tens:69 @74 / tens:71 @76: rung-2 approach/release beats adjacent to @75=3 (Scene F). Approach
  and release rungs for a peak; structural purpose is the curve, not co-citation. Not superfluous.
- tens:82 @87: rung-2 decay beat post-@86=3 (Scene H). Release; structural. Not superfluous.
- tens:104 @111 / tens:106 @113: rung-2 plateau beats in Scene J's sustained-surveillance
  zone (KICKBACK-2). Sustained-2 without rupture is the KICKBACK-2 condition; the entries are
  structurally correct documentation of the flatline pattern. Not superfluous.
- tens:133 @142: rung-2 continuation after @140=3 and @141=2 in Scene M. Release/continuation.
  Not superfluous.
- tens:140 @150: rung-2 approach to @151=3 in Scene N. Approach beat. Not superfluous.
- state:17 @144: oc-dock-runner.position fish-gate-margin → loc-flea-bottom. Position flip on
  exit. Persistent state change (runner exits FGM; the position is tracked for scene continuity).
  Not superfluous.
- feel:7 @93: oc-tanner-father "he sets the eyes on the work and does not lift them to the gate."
  @93 is rated tens=1 in the working file (NOT rung 3). The rubric note: "tens rating=1 and
  off-anchor vibes are never superfluous." Per schema and Phase 5 rubric, the tens=1 lonely
  feeling entry is structurally exempt from superfluous classification. Additionally the entry
  carries documented multi-justification (5/5) and card-match. Not superfluous.

PASS. All lonely entries serve structural or rule-exempt purpose.

### 7-B: PASS — Relay-beat NONE entries in state-updates.md

The relay-beats NONE section explicitly declines 10 relay-transient beats with documented
rationale per anti-pattern #9 (density-on-flat). These are non-entries. PASS.

---

## Class 8: CONSTRAINT

### Earth-Bet proper-noun scan (URI-032) — independent re-derivation

Hard-fence: Brockton Bay, Skitter, Lung, Khepri (as proper noun outside canon-tagged archival
uses), Bakuda, PRT, Annette, Coil, Dinah, Undersiders, Taylor Hebert (as surname), Worm, Earth
Bet, and derivatives in slug components or entry text.

**memory.md — all seven entries (independent full scan):**

mem:3 @92: "the woman's face holds the wood and what she will not turn to watch has the shape
she will not name -> (earth-bet: refusal-to-look / locker-tutor / helpless-protector pattern;
margit-referral candidate for monument-locker)"
Slug component "monument-locker": "locker" is mechanism-descriptive (a physical container / the
event-type). Not an Earth-Bet proper noun. Description tokens "earth-bet" (category tag, not
a proper noun slug component), "locker-tutor", "helpless-protector": mechanism-descriptive.
CLEAN.

mem:4 @134: "the network drops out and the absence has the shape of an arrival she has felt come
this way before -> (earth-bet: fauna-silence-at-scale / arrival-pattern; margit-referral
candidate for monument-fauna-silence-at-scale)"
Slug "monument-fauna-silence-at-scale": mechanism-descriptive. CLEAN.

mem:5 @22: "the log holds the salt-reach and what the salt-reach cost the mother is what the log
does not hold -> (project-condition: clinical-self-erasure / log-omission-architecture;
cond-clinical-self-erasure anchor)"
No Earth-Bet proper noun. CLEAN.

mem:6 @43: "the song stops on the third note and what the third note was reaching for is the
silence the body should have filled -> (earth-bet: helpless-protector / failed-recognition
pattern — dying-parent-recognition-fail variant; margit-referral candidate for
monument-failed-recognition-by-dying-parent)"
Slug "monument-failed-recognition-by-dying-parent": mechanism-descriptive; "dying-parent" is
a relational description, not an Earth-Bet proper noun. "Annette-adjacent" has been removed
(r3-signal-005 fix confirmed at r4; still absent on r5 read). CLEAN.

mem:7 @98: "the name of the city holds a season she has not entered and the season she has not
entered is the one she knows the shape of -> (westeros: foreknowledge-clamp on succession-window
/ Dance-timeline; margit-referral candidate for monument-dance-of-dragons)"
"Westeros" is the in-world setting of ASOIAF/GOT; it is not an Earth-Bet entity. Slug
"monument-dance-of-dragons" is Westerosi-world terminology. CLEAN.

mem:8 @114: "the man speaks to a room with no listener and the shape of what he says is the
shape of a voice she has heard be correct in a tongue no one in the room is listening for ->
(earth-bet: dying-tutor / right-but-unhearable pattern; margit-referral candidate for
monument-failed-recognition-by-dying-parent / tutor-side)"
"earth-bet" is category tag. "dying-tutor" and "right-but-unhearable" are mechanism-descriptive.
No Earth-Bet proper noun as slug component. CLEAN.

mem:9 @154: "the word she gives the runner is the word she has given before to a person she
could have burned and did not -> (earth-bet: peer-trust-test / non-retaliation-as-trust-token
pattern; margit-referral candidate for monument-peer-trust-non-retaliation)"
URI-032 check: slug components are "peer-trust-test", "non-retaliation-as-trust-token",
"monument-peer-trust-non-retaliation". ALL are mechanism-descriptive. "non-retaliation-as-
trust-token" and "monument-peer-trust-non-retaliation" describe the behavioral pattern without
naming any Earth-Bet proper noun. "Undersiders" has been removed (r4-signal-002 fix confirmed).
**r4-signal-002 CLOSED. CLEAN.**

**All other facet files — Earth-Bet scan:**

interest-narrator.md: no Earth-Bet proper nouns in entry text. Reference to "Earth-Bet-shadow-
via-gap" in a comment line (not an entry). CLEAN.

feeling.md: no Earth-Bet proper nouns in any of the 13 entry lines. CLEAN.

metaphor.md: entry meta:2 @73 "the record book is a door already shut | licensed-by: memory:3
+tens:1". No Earth-Bet proper noun. Refusal section references "worm-canon register" (a
descriptive term for the rubric's AP5 fence, not a proper-noun slug). CLEAN.

sensory.md: five entries; no Earth-Bet proper nouns. CLEAN.

state-updates.md: 34 entries; no Earth-Bet proper nouns in any entry text or target field.
CLEAN.

location-state.md: three entries; no Earth-Bet proper nouns. CLEAN.

vibes.md: 18 entries; no Earth-Bet proper nouns in any entry text or target or licensed-by
field. CLEAN.

tensometer-s01e01.md: scalar entries carry no text content beyond rung. Curve-verdict prose
uses Westerosi-world terminology only. CLEAN.

**8-A: PASS** — URI-032 Earth-Bet hard-fence scan. All memory.md entries including mem:9
confirmed CLEAN post-fix. All other facet files CLEAN.

### 8-B: PASS — Series-law constraint check

Laws from showrunner/memory.md verified:
- cond-shard-behavioral-weight: no escalation-reflex violations in episode-1 facets. CLEAN.
- cond-no-parahuman-infrastructure: no parahuman infrastructure in facet entries. CLEAN.
- cond-smallfolk-political-physics: all cast interactions consistent with smallfolk political
  physics. CLEAN.
- cond-feudal-hierarchy-law: no hierarchy violations. CLEAN.
- cond-fauna-control-rules / cond-fauna-control-rules-125ac-addendum: network within 300m
  sphere. Khepri-mantle sealed at story-open per proto-lines. No mantle use in s01e01 facets.
  CLEAN.
- cond-reincarnation-mechanics-125ac: Taylor wakes in Tya's body per episode-open; no mechanic
  violation in facet content. CLEAN.
- cond-series-tone-constraints-125ac: no triumph beats, no catharsis, no momentum-driven
  adventure pacing visible in facet entries. The 79.4% rung-1 tensometer distribution and 25.2%
  narrator-interest density confirm contemplative-procedural register. CLEAN.

### 8-C: PASS — Lore constraint check

cond-westerosi-superstition-frame / cond-crownlands-superstition-frame-125ac: no anachronistic
knowledge or world-mechanic violation in any facet entry. CLEAN.

### 8-D: PASS — Memory / NI-spine co-citation constraint

All seven memory entries checked for NI-spine co-citation:
- mem:3 @92: cite-index shows co=[feel:9, narrator:24, tens:87]. narrator:24 present. PASS.
- mem:4 @134: co=[narrator:34, state:14, tens:126]. narrator:34 present. PASS.
- mem:5 @22: co=[narrator:7, state:28, tens:22]. narrator:7 present. PASS.
- mem:6 @43: co=[feel:8, narrator:12, sensory:3, tens:41, vibes:8, vibes:9]. narrator:12 present. PASS.
- mem:7 @98: co=[loc-state:1, narrator:25, sensory:4, state:6, state:31, tens:92, vibes:13].
  narrator:25 present. PASS.
- mem:8 @114: co=[narrator:29, tens:107, vibes:5]. narrator:29 present. PASS.
- mem:9 @154: co=[feel:13, narrator:40, state:34, tens:145]. narrator:40 present. PASS.

All seven memory entries are co-cited with a narrator-interest entry on the same anchor. PASS.

### 8-E: PASS — Metaphor licensed-by anchor resolution

meta:2 @73: "licensed-by: memory:3 +tens:1"
memory:3 resolves: mem:3 @92 in the locked memory.md (cite-index confirms `mem:3 @92 back=Y`).
tens:1 resolves: tens:1 @1 in tensometer (cite-index confirms `tens:1 @1 r=1 back=Y`).
Both anchors resolve. PASS.

Note: the cite-index records `meta:2 @73 back=Y lic-out=[memory:3, tens:1]` — the field
notation uses "memory:3" (not "mem:3"), which is the description-text form from the R1 metaphor
file. This is a display inconsistency in the `lic-out` field (the file uses "memory:3" vs the
cite-index prefix "mem:3"), but both resolve to the same entry and the anchor is confirmed
resolvable. No functional constraint violation. Not filed as a finding given the rubric's
tolerance for provisional `licensed-by:` resolution forms in R2.

### 8-F: PASS — Vibes licensed-by anchor resolution

All 18 vibes entries scanned for resolvable `licensed-by:` anchors:
- vibes:1: licensed-by proto:1/2/3 (resolve), canon:taylor-inhabiting-tya-body-at-story-open
  (narrative canon reference, not a facet entry; acceptable for vibes world-build anchors). PASS.
- vibes:2: licensed-by proto:77, tens:3 (tens:3=@3 resolves), state-update-taylor:2 (state:29=@90
  Taylor.placement-status resolves via naming convention). PASS.
- vibes:7: licensed-by proto:48, feeling-oc-tanner-father:1 (feel:6=@48 resolves). PASS.
- vibes:12: licensed-by proto:143/144/140, state-update-oc-dock-runner:4 (state:19=@155
  resolves via dock-runner state chain). PASS.
- Remaining vibes entries reference proto: anchors + state-update: cross-references and
  world-build: canon anchors. All proto: anchors are within s01e01 range. No forward-citing
  licensed-by (referencing a facet entry that does not yet exist). PASS.

No vibes entries carry unresolvable anchors. PASS.

### 8-G: PASS — POV-perceptual access on NI

interest-narrator.md entries reviewed for POV-perceptual access violations (NI firing on content
Taylor cannot perceive through swarm-relay or direct observation). Episode-scope perceptual
channel is Taylor's 300m sphere fly/beetle/wasp/spider network plus direct line-of-sight.

Checked entries anchored at non-direct-perception beats:
- narrator:25 @98, narrator:26 @99, narrator:27 @103: Taylor arriving and setting up — direct
  perception. CLEAN.
- narrator:29 @114: "the maester speaks to a room with no listener; she is the listener the
  room does not contain." Taylor is receiving via beetle relay established at @110-@112. Perceptual
  access via established relay. CLEAN.
- narrator:30 @124: "the spiders return the room's ceiling-corners..." — spiders established at
  @112. CLEAN.
- narrator:31 @130 / narrator:34 @134: maester content received via beetle relay. CLEAN.
- narrator:36 @140 / narrator:37 @143: dock-runner perception via fly relay (@142). CLEAN.

No POV-perceptual access violations found. PASS.

---

## Class 9: AP-SCAN

**AP-1 (ambient escalation):** Re-scanned tensometer for ambient/transitional beats rated 2 or 3
when face charge does not support it. All rung-2 entries verified against the three axes:
@7 (father faces Taylor — watch-cost); @11 (pivots toward Taylor — re-engagement); @13 (chin-hold
— body-cost); @14 (stills — assessment-charge); @42 (eye-hold — approach to @43=3); @66
(reeve-slowing — watch-cost); @74 (lords-man speaks to reeve — approach); @76 (lords-man opens
record book — approach); @87 (Taylor faces elder — pre-routing tension); @89 (stillness — held-
against-turn); @111-@113 (sustained surveillance plateau); @131 (south-wall footfall — rhythm
anomaly); @139-@142 (Watch presence / relay sequence); @148-@150 (approach to elder-commitment
exchange). All rung-2 entries carry named face-charge per the rung-2 test. No ambient escalation
found. PASS.

**AP-2 (speech-beat default):** Speech-act proto-lines rated 2/3 checked:
@86 (elder routes Taylor — routing IS the irreversible commitment, rated on the act not the
speech; rubric permits non-1 when the speech-act IS the commit); @150=2 (dock-runner speaks to
elder — approach-to-commitment sequence, 2 is for proximity, not the speech content); @148=2
(elder speaks to dock-runner — same). @130=1 (maester speaks to room). @153=1 (runner speaks to
Taylor). @154=1 (Taylor speaks to runner). All justified against rubric axes. No auto-default
found. PASS.

**AP-3 (feeling — named-feeling vocabulary):** All 13 feeling.md entries scanned. No "feels"
verb, no named-feeling tokens, no hedges (like/as if/almost/nearly/kind of). Body register
only across all six character forks. PASS.

**AP-4 (inflation):** KICKBACK-1 (Scene E) and KICKBACK-2 (Scene J) declared as kickbacks not
scalar inflations. KICKBACK-3 (Scene L) resolved via rung correction at @134=3, not via
inflating adjacent entries. AP4 clean throughout. PASS.

**AP-5 (metaphor at peaks — Earth-Bet leak risk):** meta:2 @73 at tens=1. Not a peak. Memory
anchor (mem:3) grounds the figure in the refusal-to-look / locker-tutor monument scope (Westerosi
execution, not Earth-Bet cape-fic register). AP5 violation not present. PASS.

**AP-6 (metaphor voice register):** "a door already shut" — spare, non-ornate, Taylor's
procedural register. PASS.

**AP-7 (metaphor at tens≠3 — default-refuse discipline):** meta:2 @73 is at tens=1, but R1
metaphor rubric allows tens≠3 with ≥2 supporting layers (memory:3 + tens:1 = 2 layers). R2
metaphor judge retained the entry under this threshold. The @39 candidate (tens=3) was
correctly refused under AP-7 default-refuse. AP-7 discipline honored. PASS.

**AP-8 (posture-as-state in state-updates):** Multiple explicit NONE-CORRECT refusals for
orientation/posture beats documented in state-updates.md (oc-tanner-mother @18/@45/@92, oc-dock-
runner @143, maester @129). Pattern anti-pattern-clean. PASS.

**AP-9 (density-on-flat):** Relay-transient beats explicitly refused across 10 NONE-CORRECT
entries in state-updates.md. PASS.

**AP-10 (stylistic noting):** oc-broken-maester state-updates section correctly refuses all four
maester anchors (@114, @129, @130, @133) as verbalization or transient motor events. PASS.

**AP-12 (non-POV metaphor):** meta:2 @73 anchors on Taylor's POV perception. The lords-man
pro-line @73 is within Taylor's observation range (she is present in the scene, per proto-lines
@71–@78). POV-appropriate. PASS.

No new AP-SCAN findings.

---

## Class 10: TASTE-FLAG

TASTE-FLAG covers patterns the audience may flag as entertainment concerns. Mode: SIGNAL only.
r3-signal-006 and r3-signal-007 are editor-call deferrals that have persisted across r3, r4,
and now r5. Independent re-derivation below confirms whether the conditions persist.

### 10-A: SIGNAL — interest-narrator density at 25.2% (carry-forward from r3-signal-006 / r4-signal-003)

Independent re-derivation: cite-index records 39 narrator entries; proto-lines count 155 non-
blank bones. 39/155 = 25.16% ≈ 25.2%. Rubric band 15-25%. Breach of ceiling by 0.2 percentage
points. Condition unchanged from r4.

- id: r5-signal-001
- type: flag
- class: TASTE-FLAG
- severity: SIGNAL
- what: interest-narrator.md post-R2 density 39/155 ≈ 25.2%, against rubric ceiling 25%.
  Overage is 0.2 percentage points (less than one entry above ceiling at 155 proto-lines).
  The R2 add of narrator:41 @14 pushed the file from 24.5% to 25.2%. Condition persists
  unchanged from r3-signal-006 / r4-signal-003.
- why: Nominal rubric ceiling breach. The practical rendering effect is negligible. The R2 add
  is well-defended (scene-A peak-approach gap, cost-tracking channel, non-redundant with feel:5).
  This is a taste flag, not a structural constraint failure.
- criteria: No action required unless the editor observes that the scene-A narrator-interest
  cluster renders as too dense in the stitched manuscript. If so, narrator:41 @14 is the cull
  candidate (R2-added; weakest cap defense in scene A).
- routing: editor (at stitch review); no fixer dispatch required
- status: editor-call deferral; carry-forward from r3-signal-006 / r4-signal-003

### 10-B: SIGNAL — feeling.md per-character sparsity below 2% for non-POV characters
  (carry-forward from r3-signal-007 / r4-signal-004)

Independent re-derivation: from cite-index `feel (13 entries)`:
- taylor-hebert-flea-bottom: 4 entries (@20, @66, @94, @154) = 4/155 = 2.6%
- oc-tanner-father: 3 entries (@14, @48, @93) = 3/155 = 1.9%
- oc-tanner-mother: 2 entries (@43, @92) = 2/155 = 1.3%
- oc-tanner-elder: 2 entries (@90, @151) = 2/155 = 1.3%
- oc-broken-maester: 1 entry (@129) = 1/155 = 0.6%
- oc-dock-runner: 1 entry (@143) = 1/155 = 0.6%

Rubric band: 2-5% per episode per character. oc-tanner-father (1.9%), oc-tanner-mother (1.3%),
oc-tanner-elder (1.3%), oc-broken-maester (0.6%), oc-dock-runner (0.6%) all below 2% floor.
Only Taylor-as-POV is above floor. Condition unchanged from r4-signal-004.

Per-episode aggregate all-character combined: 13/155 = 8.4%, well within any reasonable
aggregate band.

- id: r5-signal-002
- type: flag
- class: TASTE-FLAG
- severity: SIGNAL
- what: Non-POV per-character sparsity below 2% for oc-tanner-father (1.9%), oc-tanner-mother
  (1.3%), oc-tanner-elder (1.3%), oc-broken-maester (0.6%), oc-dock-runner (0.6%). Rubric floor
  is 2% per-character per-episode. Condition persists unchanged from r3-signal-007 / r4-signal-004.
- why: Individual per-character sparsity is low because each non-POV character appears in
  limited scenes with limited per-scene-cap availability. The aggregate (8.4%) is healthy.
  The per-character rubric floor may require calibration for non-POV characters with limited
  scene presence; this is a forward pin for the editor, not a structural constraint failure.
- criteria: No mandatory action. Editor should review at stitch whether assembled feeling.md
  renders as adequately somatic for non-POV characters given their limited scene presence.
- routing: editor (at stitch review); no fixer dispatch required
- status: editor-call deferral; carry-forward from r3-signal-007 / r4-signal-004

### 10-C: PASS — Narrative interest channel coverage

interest-narrator.md covers all 8 tens=3 peaks (@15, @43, @75, @86, @90, @134, @140, @151).
Scene B/D/K silence preserved. Fauna-deviation channel not saturated. PASS.

---

## Class 11: PILE-UP REVIEW

Cite-index identifies five pile-ups (> 4 co-located facets):

**@98** (8 co-located facets): loc-state:1, mem:7, narrator:25, sensory:4, state:6, state:31,
tens:92, vibes:13.
Proto-line: "taylor-hebert-flea-bottom enters loc-flea-bottom."
Each facet fires on a distinct dimension: location-state (environment); memory (Dance-foreknowledge
clamp); narrator (perceptual arrival + city-she-has-already-named); sensory (smell-delta); state:6
(Taylor.location flip) + state:31 (studio.active_location flip); tensometer rung 1 (transitional);
vibes (operational-territory-open). No content redundancy across the eight fires.
**VERDICT: WARRANTED.**

**@43** (7 co-located facets): feel:8, mem:6, narrator:12, sensory:3, tens:41, vibes:8, vibes:9.
Proto-line: "oc-tanner-mother drops the song."
Scene C's tens=3 peak. Convergence at 3-peak expected per cross-facet contract. Each fires
distinctly: feeling (mother's hands-still somatic); memory (helpless-protector/failed-recognition
monument); narrator (silence-as-Tya-shaped-absence); sensory (song→silence sound-drop);
tensometer rung 3; vibes:8 (grief-without-object) + vibes:9 (asking-around-the-edge — distinct
keywords and relational framings). No content redundancy.
**VERDICT: WARRANTED.**

**@103** (7 co-located facets): loc-state:2, narrator:27, state:10, state:32, tens:97, vibes:15,
vibes:16.
Proto-line: "taylor-hebert-flea-bottom enters loc-flea-bottom-base."
Second carded location arrival. Each fires distinctly: location-state (room environment +
floor-anchor); narrator (exit-count + roofline-to-spiders pre-scan); state:10 (Taylor.location
flip to base) + state:32 (studio.active_location flip to base); tensometer rung 1; vibes:15
(first-lodging-anchored) + vibes:16 (maester-connectivity-established — distinct keywords,
distinct relational content). No content redundancy.
**VERDICT: WARRANTED.**

**@90** (6 co-located facets): feel:3, narrator:23, state:29, tens:85, vibes:3, vibes:10.
Proto-line: "oc-tanner-elder routes taylor-hebert-flea-bottom."
Scene H climax first peak (tens=3). Each fires distinctly: feeling (elder's eyes-already-past);
narrator (gate-as-last-zero-cost-threshold); state:29 (Taylor.placement-status flip);
tensometer rung 3; vibes:3 (Taylor: the-Tya-shaped-debt / debt-fixed-body-mobile) + vibes:10
(elder: conditional-ledger — distinct character targets). No content redundancy.
**VERDICT: WARRANTED.**

**@154** (5 co-located facets): feel:13, mem:9, narrator:40, state:34, tens:145.
Proto-line: "taylor-hebert-flea-bottom speaks to oc-dock-runner."
Each fires distinctly: feeling (hand-stillness during the commit); memory (peer-trust-test /
non-retaliation-as-trust-token); narrator (first-irreversible-said + city-will-route-it);
state:34 (Taylor.network-anchor flip); tensometer rung 1. The non-peak rung-1 pile-up is a
documented SEAM-1 in interest-narrator (tens-undercall on @154 vs NI's irreversibility read;
tens locked; both entries independently defensible). No content redundancy.
**VERDICT: WARRANTED.**

**Overall pile-up verdict: ALL FIVE WARRANTED.** No pile-up creates a finding.

---

## R4 Signal Closure Report

| Signal ID | Class | Fix applied | R5 status |
|-----------|-------|-------------|-----------|
| r4-signal-001 | STRUCTURAL | feeling.md per-source YAML blocks replaced with plain `# slice file — ...` comment headers; build_cite_index regenerated; single top-of-file frontmatter confirmed | CLOSED — PASS |
| r4-signal-002 | CONSTRAINT | mem:9 @154 slug components revised: "undersiders-trust-pattern" → "non-retaliation-as-trust-token pattern"; "monument-undersiders-trust" → "monument-peer-trust-non-retaliation" | CLOSED — PASS |
| r4-signal-003 | TASTE-FLAG | Editor-call deferral; condition unchanged (density 25.2% at ceiling); carry-forward as r5-signal-001 | CARRY-FORWARD |
| r4-signal-004 | TASTE-FLAG | Editor-call deferral; condition unchanged (non-POV per-character sparsity below floor); carry-forward as r5-signal-002 | CARRY-FORWARD |

---

## Audit Summary

| Class | Findings | HARD | SIGNAL | Status |
|-------|----------|------|--------|--------|
| 1 STRUCTURAL | r4-signal-001 CLOSED | 0 | 0 | PASS |
| 2 FREQUENCY-BAND | flag-005 confirmed EXEMPT | 0 | 0 | EXEMPT-TONE-LAW-SLOW-BURN |
| 3 METADATA-INCONSISTENCY | memory snapshot lag noted | 0 | 0 | PASS |
| 4 CURVE-SHAPE | @134=3 confirmed; all scenes PASS | 0 | 0 | SHAPE-CLEAN |
| 5 CONTRADICTION | none | 0 | 0 | PASS |
| 6 DEDUP | none | 0 | 0 | PASS |
| 7 SUPERFLUOUS | none | 0 | 0 | PASS |
| 8 CONSTRAINT | r4-signal-002 CLOSED; all eight sub-checks PASS | 0 | 0 | PASS |
| 9 AP-SCAN | none | 0 | 0 | PASS |
| 10 TASTE-FLAG | 2 carry-forward editor-call deferrals | 0 | 2 | SIGNAL |
| 11 PILE-UP | all five warranted | 0 | 0 | PASS |

**HARD: 0**
**SIGNAL: 2** (r5-signal-001 [editor-call carry-forward], r5-signal-002 [editor-call carry-forward])
**EXEMPT: 1** (flag-005 EXEMPT-TONE-LAW-SLOW-BURN)

**flag-005: EXEMPT-TONE-LAW-SLOW-BURN** — all four criteria (a)–(d) independently verified on
live card body. Exemption confirmed.

**CURVE-SHAPE: SHAPE-CLEAN** — @134=3 confirmed; all named scenes pass or hold documented
kickback/transit exceptions. Scene H 3→3 double-tap satisfies rubric's commit-of-first condition.
No residual shape anomaly.

---

## Routing Block

| Finding | Class | Routing |
|---------|-------|---------|
| r5-signal-001 | TASTE-FLAG | editor (at stitch review); no fixer dispatch; narrator:41 @14 is the cull candidate if density renders too dense |
| r5-signal-002 | TASTE-FLAG | editor (at stitch review); no fixer dispatch; no add candidates defensible without cap violations |

No HARD findings. No fixer dispatch required. No cross-facet delete authority invoked.

---

## Episode Status

**Status: CLEAN** (HARD = 0; r4-signal-001 CLOSED; r4-signal-002 CLOSED; the two editor-call
carry-forwards persist as SIGNAL only and require no fixer dispatch.)

r4-signal-001 fix confirmed: all six per-source sections in feeling.md now carry plain comment
headers. No secondary YAML blocks.

r4-signal-002 fix confirmed: mem:9 @154 description uses "non-retaliation-as-trust-token
pattern" and "monument-peer-trust-non-retaliation" — mechanism-descriptive, no Earth-Bet proper
noun in any slug component.

The orchestrator-critic Phase 6 can proceed toward SUCCESS: HARD = 0, all six fixer-addressed
signals from r3/r4 confirmed CLOSED, flag-005 confirmed EXEMPT-TONE-LAW-SLOW-BURN, CURVE-SHAPE
CLEAN. Only two editor-call SIGNAL carry-forwards remain, both by design.
