---
audit: facets-final-r4
episode: s01e01
date: 2026-05-11
mode: flag-only
status: CLEAN
totals:
  hard: 0
  signal: 3
  exempt: 1
  pass: 8
---

# Facets Final Audit R4 — s01e01

Auditor: cross-cutting graph auditor fork (Phase 5 re-audit, fourth pass)
Trigger: fixer pass addressed r3-signal-001 through r3-signal-005; r4 is independent re-derivation
  confirming closure of all five and re-scanning the full graph for new findings.
Mode: FLAG-ONLY. Independent re-derivation; r3 findings not carried forward; all findings
  re-derived from current file state.

Inputs read:
  - proto-lines: active-project/theater/proto-lines/s01e01.md
  - facets: active-project/theater/facets/tensometer.md (working), tensometer-s01e01.md (archive),
             location-state.md, interest-narrator.md, sensory.md, state-updates.md, memory.md,
             feeling.md, metaphor.md, vibes.md
  - active-project/theater/facets/_cite-index.md
  - active-project/theater/facets/.r2-decisions.md
  - active-project/staff/showrunner/memory.md
  - schemas/facet.schema.md, schemas/audit-report.schema.md
  - design/shoot-v2/rubric-tensometer.md
  - cards/conditions/cond-series-tone-constraints-125ac.card.md (post-amendment)
  - prior audit: active-project/staff/auditor/facets-final-audit-r3.md (context only)

Forbidden (not loaded): behavior cards other than the named tone-law card, vibes-as-bias,
  audience personas, source prose.

---

## Class 1: STRUCTURAL

### Findings

**1-A: PASS** — Tensometer ID monotonicity

Tensometer working file body (active-project/theater/facets/tensometer.md) scanned. Entry IDs run
1–78, skip 79–80, resume 81–92, skip 93 (stripped position), then IDs 93–128 skipping 123 (stripped),
124–128, skip 129 (stripped), 130–142, skip 143–146 (stripped range), 144–146. All post-strip IDs
are positive integers in monotonically non-decreasing order within the surviving body. No alpha-suffix
IDs remain. PASS.

**1-B: PASS** — Out-of-range anchors

Tensometer working file body contains no @495, @504, @506, @516, @517, @518, @525 entries and no
entry anchoring outside the s01e01 aggregate range 1–155. Out-of-range strip from C1 remediation
confirmed complete. PASS.

**1-C: PASS** — state-updates.md frontmatter (r3-signal-001 closure check)

state-updates.md lines 1–5 carry a single conformant frontmatter block:
  facet: state-updates
  sources: [env, oc-broken-maester, oc-dock-runner, oc-tanner-elder, oc-tanner-father,
            oc-tanner-mother, taylor-hebert-flea-bottom]
  note: consolidated by build_cite_index from per-source slices. Single top-of-file frontmatter
        per r3-signal-001.

Per-source divisions below this block are plain `# source: <name>` comment lines. No additional
YAML frontmatter blocks follow. This satisfies the r3-signal-001 criterion. PASS.

**1-D: SIGNAL** — feeling.md multi-source frontmatter blocks

- id: r4-signal-001
- type: flag
- class: STRUCTURAL
- severity: SIGNAL
- what: feeling.md carries a single composite frontmatter block at lines 1–5
  (facet/sources/note per r3-signal-001 pattern), which is correct. However, the per-source
  sections below it — specifically the `# source: oc-broken-maester` section (line 7) — are
  followed by a second YAML block (lines 8–13): `facet: feeling`, `episode: s01e01`,
  `character: oc-broken-maester`, `author: r1-feeling-oc-broken-maester`, `r2-pass:`, `---`.
  The same pattern repeats for subsequent source sections (`# source: oc-dock-runner`,
  `# source: oc-tanner-elder`, `# source: oc-tanner-father`, `# source: oc-tanner-mother`,
  `# source: taylor-hebert-flea-bottom`). Each carries its own `facet:` / `episode:` /
  `character:` / `author:` YAML block after the comment-line header. These are residual
  per-character-slice frontmatter blocks that were not collapsed to plain comments when the
  file was consolidated — the same defect r3-signal-001 addressed in state-updates.md. The
  difference is that state-updates.md received the fix; feeling.md did not.
- why: Downstream parsers that read the composite feeling.md will see six YAML frontmatter
  blocks (one per source section) in addition to the top-of-file block. The `facet:`,
  `episode:`, `character:`, and `author:` metadata for characters 2–6 will be parsed as
  additional frontmatter declarations, not as body text. This is the same downstream-tooling
  integration risk identified for state-updates in r3-signal-001.
- criteria: feeling.md's per-source section headers below the top-of-file frontmatter block
  should be plain comments (or unformatted prose headings), not YAML blocks. The `facet:`,
  `episode:`, `character:`, `author:`, `r2-pass:` fields in each per-source section should be
  converted to `# character: <name>` / `# author: <name>` comment lines, matching the
  pattern state-updates.md now uses.
- routing: dialogue-writer-fork (feeling file consolidation authority)

**1-E: PASS** — Anchor resolution (all facets)

Cite-index back-links verified. All entries marked `back=Y` in the regenerated cite-index resolve
to proto-line IDs within s01e01 aggregate range 1–155. No unresolved anchor found in any active
facet entry. The lonely-entry and bare-protoline lists in the cite-index are internally consistent.
PASS.

**1-F: PASS** — Header/frontmatter presence (single-file facets)

tensometer.md, tensometer-s01e01.md, location-state.md, interest-narrator.md, sensory.md,
metaphor.md, and vibes.md each carry a single conformant frontmatter block. The consolidated
state-updates.md and feeling.md both carry single top-of-file blocks (feeling.md's per-source
secondary blocks are filed at 1-D above). PASS on single-file facets; see 1-D for feeling.md.

**1-G: PASS** — Proto-body integrity

Proto-lines file header states aggregate_range 1–155 with interpolated narrative-scope bones noted
as absent from body per URI-028. Body contains bones 1–159 with documented time-skip blanks. All
non-blank bone IDs in the body fall within 1–155. URI-028 carry-forward note accurate. PASS.

---

## Class 2: FREQUENCY-BAND

### Independent baseline recount

From tensometer.md working file body, counting all non-comment lines in format `<id> @<pid> <r>`:

Rungs verified by direct scan of entries:
- 3s: entries at @15, @43, @75, @86, @90, @134, @140, @151 = **8 entries**
- 2s: entries at @7, @11, @13, @14, @66, @74, @76, @82, @84, @104, @105, @106, @111, @112,
      @122, @130, @131, @132, @138, @139, @140 = let me recount from the body.

Re-scan from body order: entries rated 2 are IDs 7(@7), 11(@11), 13(@13), 14(@14), 40(@42),
62(@66), 69(@74), 71(@76), 82(@87), 84(@89), 104(@111), 105(@112), 106(@113), 122(@131),
130(@139), 132(@141), 133(@142), 138(@148), 139(@149), 140(@150), 142(@152) = **21 entries**

Total entries: 141.

Verification: 8 (3s) + 21 (2s) + 112 (1s) = 141. Consistent.

Rates:
- 3s: 8/141 = 5.67% ≈ 5.7%
- 2s: 21/141 = 14.89% ≈ 14.9%
- 1s: 112/141 = 79.43% ≈ 79.4%

Standard band: 1s 60-75% / 2s 20-30% / 3s 5-10%.
Breaches: 2s below floor (14.9% vs 20%); 1s above ceiling (79.4% vs 75%).
3s: 5.7% is WITHIN the standard band (5-10%).

### Exemption 5 evaluation — flag-005

Per `design/shoot-v2/rubric-tensometer.md` §"Frequency-band exemptions / Exemption 5 — Tone-law-
licensed slow-burn register":

**(a) Tone-law card loaded; card body contains required vocabulary:**

showrunner/memory.md `series.behaviors` lists `cond-series-tone-constraints-125ac`. Card is loaded.

Card body check (post-amendment). The card §"The Prohibited Registers" now contains a paragraph
titled "Tensometer register characterization:" (line ~51) that states verbatim: "This project
authors in the slow-burn / low-rupture-density register, with foreknowledge-clamp as primary
register. The standard tens frequency-band gate (1s 60-75% / 2s 20-30% / 3s 5-10%) does not apply
to seasons authored under this tone-law; see §'Relaxed tens frequency-band for this config
(URI-034 Exemption 5)' below."

Rubric criterion (a) requires at least one of: `slow-burn`, `low-rupture-density`,
`quiet-observer-register`, `foreknowledge-clamp-as-primary-register`, or an explicit declaration
that the standard tens frequency-band does not apply.

The post-amendment card body contains:
- token "slow-burn" (exact, in the "slow-burn / low-rupture-density register" phrase)
- token "low-rupture-density" (exact)
- the phrase "foreknowledge-clamp as primary register" (matching the rubric's
  `foreknowledge-clamp-as-primary-register` token in meaning and near-exact form)
- explicit declaration: "The standard tens frequency-band gate (1s 60-75% / 2s 20-30% /
  3s 5-10%) does not apply to seasons authored under this tone-law"

Criterion (a): SATISFIED. All four conditions present; only one is required.

**(b) Card specifies quantified relaxed band:**

Card body now contains §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)"
(line ~87) specifying:
- 1s: 75-85%
- 2s: 12-22%
- 3s: 4.5-10% season-average, 4.0-10% per-episode

This is the quantified relaxed-band specification the criterion requires. The tensometer.md
footer's criterion (b) quotation matches this section accurately.

This episode's per-episode rates: 1s 79.4% (within 75-85%), 2s 14.9% (within 12-22%),
3s 5.7% (within 4.0-10% per-episode AND within standard band 5-10%). All three rungs fall
inside the relaxed band.

Criterion (b): SATISFIED.

**(c) 3s rung discipline:**

Per-episode 3s: 5.7% ≥ 4.0% per-episode floor. PASS.

Season-average 3s from showrunner/memory.md per_episode_tens_band_verdict:
- s01e01: 3s = 5.7% (8/141, current file)
- s01e02: 3s = 4.2%
- s01e03: 3s = 4.5%
- Season average: (5.7 + 4.2 + 4.5) / 3 = 14.4 / 3 = 4.8% ≥ 4.5% season floor. PASS.

Note: showrunner/memory.md records s01e01 3s as 5.0% (pre-r3-signal-004 figure) and
per_episode_tens_band_verdict shows 1s 80.1% / 2s 14.9% / 3s 5.0%. After r3-signal-004 fix
(@134 rung 1→3), the live body now shows 3s 5.7% / 1s 79.4% (one entry shifted from 1 to 3,
reducing 1s by one count). The showrunner memory's per_episode_tens_band_verdict field has
not been updated to reflect the post-fix rates (it still shows 5.0%/80.1%). This is a minor
metadata lag; the live tensometer body is authoritative. Season-average recomputed:
(5.7 + 4.2 + 4.5) / 3 = 4.8%; still above the 4.5% floor.

(c.i) Every named scene carries its peak: curve verdict "3s justified" section lists @15, @43,
@75, @86, @90, @134, @140, @151 — 8 entries covering all named scenes (A/C/F/H/L/M/N) plus
transit-excepted scenes (B/D/G/I/K). KICKBACK-1 (Scene E) and KICKBACK-2 (Scene J) are
declared kickbacks rather than scalar inflations. KICKBACK-3 (Scene L) RESOLVED with @134=3.
All named scenes covered. PASS.

(c.ii) Cycle-3 F7-bone rescue scenes used screen-writer rupture additions, not dramatist scalar
inflation. Documented in tensometer footer. PASS.

Criterion (c): SATISFIED.

**(d) Season-wide scope:**

`cond-series-tone-constraints-125ac` card §"Duration": "Persistent across all four seasons.
Series-defining rules." The exemption applies series-wide. Sibling episodes s01e02 and s01e03
independently file Exemption 5 claims against the same card. Criterion (d): SATISFIED.

**Exemption 5 verdict: EXEMPT-TONE-LAW-SLOW-BURN**

All four criteria (a), (b), (c), (d) are satisfied with quoted positive evidence from the
post-amendment card body. flag-005 (prior UPHELD-HARD from r2) closes as:
`exempt-tone-law-slow-burn` under rubric §"Exemption 5". No HARD finding. r3-signal-002 CLOSED.

- id: flag-005-closure
- type: pass
- class: FREQUENCY-BAND
- what: tensometer.md frequency-band section; Exemption 5 claim under
  `cond-series-tone-constraints-125ac` post-amendment
- why: (a) card body contains required vocabulary tokens ("slow-burn", "low-rupture-density",
  "foreknowledge-clamp as primary register") and explicit tens-gate exemption declaration;
  (b) card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" specifies
  quantified band 1s 75-85% / 2s 12-22% / 3s 4.5-10% season-avg / 4.0-10% per-episode;
  (c) per-episode 3s 5.7% ≥ 4.0% floor, season-avg 4.8% ≥ 4.5% floor, all named scenes
  carry peaks, AP4 honored; (d) tone-law is series-wide. All criteria satisfied.
- status: EXEMPT-TONE-LAW-SLOW-BURN

---

## Class 3: METADATA-INCONSISTENCY

### Findings

**3-A: PASS** — interest-narrator.md density metadata

interest-narrator.md carries `[SUPERSEDED — pre-R2 figure; see post-R2 density below]` on the
pre-R2 38/155 = 24.5% line and a confirmed post-R2 density of 39/155 ≈ 25.2%. Consistent. PASS.

**3-B: PASS** — tensometer.md header bones field

Frontmatter states `bones: 1-155 (+ interpolated narrative-scope: 495, 504, 506, 516, 517, 518,
525)`. Matches proto-lines file header. Frequency-band section accurately reports 141 total entries.
PASS.

**3-C: PASS** — Cite-index totals (r3-signal-003 closure check)

Cite-index header states: "totals: 261 facet entries; 135/146 protolines decorated (92.5%)".

Per-facet entry counts from cite-index body:
- tens: 141 entries
- loc-state: 3
- narrator: 39 (including narrator:41 at @14, added in R2)
- sensory: 5
- state: 34
- mem: 7
- feel: 13
- meta: 1
- vibes: 18
Sum: 141+3+39+5+34+7+13+1+18 = **261**. Matches stated total.

This is a live-graph figure. The prior stale count of 268/148 (cited in r3-signal-003) was the
pre-regeneration state, which included 7 stripped out-of-range tensometer entries in the index
total. The cite-index regeneration (r3-signal-003 fix) removed those 7 stripped entries from the
active count. The current 261 total reflects the live graph with 141 active tensometer entries.
r3-signal-003 CLOSED. PASS.

**3-D: PASS** — showrunner/memory.md per_episode_tens_band_verdict consistency

The memory record shows s01e01: {1s: 80.1, 2s: 14.9, 3s: 5.0} — these are the pre-r3-signal-004
figures. After the @134 rung 1→3 fix, the live tensometer body shows 1s: 79.4%, 2s: 14.9%,
3s: 5.7%. The memory field has not been updated. This is a cosmetic metadata lag (the live body
is authoritative; the memory field is a recorded snapshot). The discrepancy is 0.7 points on 3s
and 0.7 points on 1s — not material enough to change any classification. The Exemption 5 verdict
holds under either figure. Filing as PASS (not a SIGNAL) because: (i) the memory field is a
convenience index, not the canonical source; (ii) the discrepancy is traceable to the documented
r3-signal-004 rung correction; (iii) no downstream consumer is gated on the memory snapshot
figure rather than the live tensometer body. Note for showrunner: update per_episode_tens_band_verdict
for s01e01 from {3s: 5.0, 1s: 80.1} to {3s: 5.7, 1s: 79.4} at next memory sync.

---

## Class 4: CURVE-SHAPE

### Findings

**4-A: PASS** — @134 rung alignment (r3-signal-004 closure check)

Tensometer working file body, entry 126: `126 @134 3`. Rung is 3.

tensometer-s01e01.md (archive) line 135: `126 @134 3`. Rung is 3. Both files consistent.

Curve verdict "3s justified" section lists @134 explicitly: "reversal-proximity peaks — beetles
fall silent; the network's collective absence-act IS the Scene L rupture (KICKBACK-3 RESOLVED at
Phase 3 cycle 3)." @134 is now on the justified list alongside @15, @43, @75, @86, @90, @140,
@151.

Cite-index: `tens:126 @134 r=3 back=Y co=[mem:4, narrator:34, state:14]`. Rung 3 confirmed
in the index.

Cross-facet commentary check:
- state-updates.md entry 14 @134: "# tens entry @134 (@518 aggregate) = 3, reversal-proximity
  peak" — consistent with body rung 3.
- interest-narrator.md SEAM-2 note: "tens=3 on @134 (beetles fall silent)" — consistent.
- oc-broken-maester state-updates notes: "Tensometer reads the rupture through the network's
  response at @134 (`the beetles fall silent`, ID 518 upstream) — that rupture is the
  *insect-network's* absence-act" — consistent.

The r3-signal-004 cross-facet contradiction (body rung 1 vs cross-facet commentary asserting
rung 3) is resolved. Body, archive, curve verdict, and cross-facet commentary are now aligned
on @134 = rung 3. r3-signal-004 CLOSED. PASS.

**4-B: PASS** — Scene-level shape (all named scenes)

Scanned tensometer body for rise/peak/release shape across all named scenes:

Scene A (waking, @1-@23): rise via 1/1/1/1/1/1/2/1/1/1/2/2/2 into @15=3; release @16=1. PASS.
Scene B (@25-@34, yard-map): transit exception declared. No 3 expected. EXEMPT.
Scene C (@36-@46, mother-sings): rise 1/1/1/2 into @43=3; release @44=1. PASS.
Scene D (@48-@60, task): transit exception declared. No 3 expected. EXEMPT.
Scene E (@62-@70, reeve): KICKBACK-1 declared. Rise without peak; correctly handled as
  kickback, not scalar inflation. KICKBACK-DECLARED.
Scene F (@71-@83, lords-man): rise via 1/1/2/3 into @75=3; release @76=2→@77=1. PASS.
Scene G (@85-@96, routing, partially transit): climax cluster in H; transit exception for G
  approach. EXEMPT.
Scene H (peaks at @86 and @90): @86=3 (routing), @90=3 (gate-crossing). Rise via 1/2/1/2 into
  @86=3; second 3 at @90 commits the routing as gate-crossing. 3→3 double-tap where second
  commits first: per rubric "3→3 only when the second 3 reverses or commits the first." PASS.
Scene I (@97-@107, FB entry): transit exception declared. No 3 expected. EXEMPT.
Scene J (@108-@127, perimeter): KICKBACK-2 declared. Sustained-2 without rupture; correctly
  handled as kickback. KICKBACK-DECLARED.
Scene K (@120-@127, full perimeter): transit exception declared. EXEMPT.
Scene L (@128-@137, laugh): @134=3 (beetles fall silent). Rise via @129=1/@130=1/@131=2 into
  @132=1/@133=1/@134=3; release @136=1. The adjacency pattern is 2/@131 then two 1s then 3 —
  the 1→3 direct-jump at @134 is a "true sudden turn" (rubric: "direct 1→3 jumps are flagged
  as either misratings or true sudden-turns; either is a kickback signal"). However the curve
  verdict explicitly justifies this as a sudden-fauna-silence rupture (a canonical sudden-turn
  class in the rubric's calibration corpus), not a misrating. The KICKBACK-3 RESOLVED declaration
  covers this. The 1→3 jump is a documented sudden-turn, not ambient escalation. PASS (with
  documented sudden-turn note).
Scene M (@139-@146, Watch/runner): @140=3 (dock-runner pivots). Rise via @139=2 into @140=3;
  release @141=2/@142=2. PASS.
Scene N (@148-@155, commit): @151=3 (Taylor speaks back). Rise via @148=2/@149=2/@150=2 into
  @151=3; release @152=2/@153=1. PASS.

**Overall CURVE-SHAPE verdict: CLEAN.** All named scenes pass or have documented kickback/transit
exceptions. KICKBACK-3 is RESOLVED with the @134=3 alignment. No residual shape anomaly. The
prior r3 SHAPE-PARTIAL verdict upgrades to SHAPE-CLEAN.

---

## Class 5: CONTRADICTION

### Findings

**5-A: PASS** — @134 rung cross-facet (r3-signal-004 resolved)

The r3-signal-004 contradiction (body rung 1 vs cross-facet commentary at rung 3) is resolved.
Tensometer body, archive, curve verdict, cite-index, state-updates commentary, and interest-
narrator SEAM-2 note all agree @134 = rung 3. No contradiction present. PASS.

**5-B: PASS** — State chain consistency

State-updates chains verified against proto-lines and location-state:
- Taylor location: loc-tanner-village → loc-flea-bottom (@98) → loc-flea-bottom-base (@103).
  Consistent with proto-lines @98 "enters loc-flea-bottom" and @103 "enters loc-flea-bottom-base".
- oc-dock-runner position: loc-flea-bottom → fish-gate-margin (@141) → loc-flea-bottom (@144)
  → market-side-junction (@149) → loc-flea-bottom (@155). Consistent.
- oc-tanner-elder location: loc-flea-bottom → tanner-family-yard (@85) → on-road (@95) →
  flea-bottom-market-side-junction (@148). Consistent.
- oc-tanner-father location-sub: outside-tanner-room → tanner-room (@4) → tanner-yard (@19).
  Consistent.
- oc-tanner-mother position: elsewhere → in-the-room (@5) → in-the-room (@36) →
  elsewhere-in-cottage (@46). Consistent with documented offstage exit assumption.
- Taylor inventory: [] → [travel-pack] (@91) → [] (@104). Consistent.
PASS.

**5-C: PASS** — Location-state vs state-updates consistency

loc-state entry 1 @98 / state entry 6 @98: both fire on flea-bottom arrival. Consistent.
loc-state entry 2 @103 / state entry 10 @103: both fire on flea-bottom-base arrival. Consistent.
loc-state entry 3 @152 Watch-passage condition: consistent with state entry 15 @139 watch-patrol
arrival and the elapsed-beat sequence to @152. PASS.

---

## Class 6: DEDUP

### Findings

**6-A: PASS** — No duplicate IDs within any facet file

All nine facet files: no entry ID repeated within a file. state-updates.md runs IDs 1–34 across
six source sections; sequential uniqueness confirmed. feeling.md runs IDs 1–13 across six source
sections; sequential uniqueness confirmed. PASS.

**6-B: PASS** — No duplicate anchor+content entries

Multi-fire instances on the same anchor: vibes @43 (vibes:8, vibes:9 — distinct keywords/targets),
vibes @77 (vibes:2, vibes:17 — distinct keywords), vibes @90 (vibes:3, vibes:10 — distinct
character targets), vibes @103 (vibes:15, vibes:16 — distinct keywords on same loc target),
vibes @130 (vibes:11, vibes:18 — distinct targets/keywords), state @91 (state:5 prop-field +
state:30 actor-inventory-field — complementary fields, not duplicates). All substantively
non-duplicate. PASS.

---

## Class 7: SUPERFLUOUS

### Findings

**7-A: PASS** — Out-of-range tensometer entries

Tensometer body contains no entry anchoring outside aggregate range 1–155. C1 strip confirmed
complete at 1-B. PASS.

**7-B: PASS** — Relay-beat NONE entries in state-updates.md

The relay-beats NONE section explicitly declines 10 relay-transient beats with documented
rationale. These are non-entries (no `<id> @<pid>` format). PASS.

**7-C: PASS** — Narrative comments in facet files

Extensive authoring notes, cull records, seam flags, and decision rationale appear as comments
in multiple facet files. These are not entries; they are permitted per schema and are standard
authoring practice. PASS.

---

## Class 8: CONSTRAINT

### Earth-Bet proper-noun scan (URI-032)

Mandatory hard-fence scan of all facet file entry text and slug components for Earth-Bet proper
nouns. Scan targets: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Annette, Coil, Dinah,
Undersiders, Taylor Hebert (as name), Worm, Earth Bet, and derivatives.

**memory.md — all entries:**
- mem:3 @92: "refusal-to-look / locker-tutor / helpless-protector pattern; margit-referral
  candidate for monument-locker" — CLEAN. No Earth-Bet proper noun.
- mem:4 @134: "fauna-silence-at-scale / arrival-pattern; margit-referral candidate for
  monument-fauna-silence-at-scale" — CLEAN.
- mem:5 @22: "project-condition: clinical-self-erasure / log-omission-architecture;
  cond-clinical-self-erasure anchor" — CLEAN.
- mem:6 @43: "helpless-protector / failed-recognition pattern — dying-parent-recognition-fail
  variant; margit-referral candidate for monument-failed-recognition-by-dying-parent" —
  CLEAN. "Annette-adjacent" language removed per r3-signal-005 fix; replacement "dying-parent-
  recognition-fail variant" contains no Earth-Bet proper noun. r3-signal-005 CLOSED. PASS.
- mem:7 @98: "westeros: foreknowledge-clamp on succession-window / Dance-timeline; margit-
  referral candidate for monument-dance-of-dragons" — CLEAN (Westeros is in-world, not
  Earth-Bet).
- mem:8 @114: "earth-bet: dying-tutor / right-but-unhearable pattern; margit-referral candidate
  for monument-failed-recognition-by-dying-parent / tutor-side" — CLEAN. "dying-tutor" and
  "right-but-unhearable" are mechanism-descriptive; "earth-bet" is a category tag, not a
  proper-noun slug component.
- mem:9 @154: "earth-bet: peer-trust-test / undersiders-trust-pattern; margit-referral candidate
  for monument-undersiders-trust" — "undersiders-trust-pattern" and "monument-undersiders-trust"
  contain "Undersiders" as a slug component.

  URI-032 check: "undersiders" in the slug. "Undersiders" is an Earth-Bet proper noun (the gang
  from Brockton Bay). Per URI-032 and `design/shoot-v2/rubric-memory-flags.md` §"Form": "slug
  components mandate mechanism-descriptive form; Earth-Bet proper nouns forbidden."
  The slug "monument-undersiders-trust" uses "undersiders" as a slug component. This is a
  URI-032 violation in mem:9.

  Scope note: r3-signal-005 in r3 concerned "Annette-adjacent" in the description prose of
  mem:6 and noted the URI-032 scope question (slug components vs description prose). The r3
  criterion was met by removing "Annette-adjacent" from the description. The current scan finds
  "Undersiders" in the slug component of mem:9 — this is the HARD scope of URI-032 (slug
  components are explicitly prohibited, per the process-gap note in showrunner/memory.md:
  "slug components mandate mechanism-descriptive form; Earth-Bet proper nouns forbidden").

- id: r4-signal-002
- type: flag
- class: CONSTRAINT
- severity: SIGNAL
- what: memory.md entry mem:9 @154 description: "earth-bet: peer-trust-test / undersiders-trust-
  pattern; margit-referral candidate for monument-undersiders-trust." The margit-referral slug
  component "undersiders-trust" and the proposed monument slug "monument-undersiders-trust"
  contain "undersiders" — the Earth-Bet gang name (Brockton Bay street-gang roster; Worm canon).
  URI-032 hard-fence prohibits Earth-Bet proper nouns as margit-referral slug components.
- why: If the monument slug "monument-undersiders-trust" propagates to margit's warehouse
  index, the Worm-canon proper noun surfaces in Westerosi-world production tooling. The
  slug component is the exact target URI-032 was authored to prohibit (showrunner/memory.md
  URI-032 note: "slug components mandate mechanism-descriptive form; Earth-Bet proper nouns
  forbidden").
- criteria: mem:9 @154 margit-referral slug component and monument slug must be revised to
  mechanism-descriptive form without Earth-Bet proper nouns. Acceptable replacement example:
  "monument-peer-trust-non-retaliation" or "monument-trust-withheld-burn-test" or equivalent
  mechanism-descriptive slug that does not use the Earth-Bet gang name. The monument concept
  (trust extended to someone Taylor could have burned and did not) is sound; the slug naming
  the pattern by Worm-canon faction is the violation.
- routing: memory author (dialogue-writer-fork:taylor-hebert-flea-bottom); margit (slug
  validation at promotion)

**All other facet files — Earth-Bet scan:**
- interest-narrator.md: no Earth-Bet proper nouns in entry text. "Earth-Bet-shadow-via-gap"
  in a comment, not an entry. CLEAN.
- feeling.md: no Earth-Bet proper nouns in any entry text. CLEAN.
- metaphor.md: no Earth-Bet proper nouns. CLEAN.
- sensory.md: no Earth-Bet proper nouns. CLEAN.
- state-updates.md: no Earth-Bet proper nouns in entry text. CLEAN.
- location-state.md: no Earth-Bet proper nouns. CLEAN.
- vibes.md: no Earth-Bet proper nouns in entry text. (vibes:12 cites "state-update-oc-dock-
  runner:4" license — the dock-runner is an OC, not an Earth-Bet entity.) CLEAN.
- tensometer.md: no Earth-Bet proper nouns. CLEAN.

**8-B: PASS** — Series-law constraint check

Laws from showrunner/memory.md checked against episode facet content:
- `cond-shard-behavioral-weight`: No escalation-reflex violations in episode-1 facets.
  Taylor's de-escalation cost not tested in s01e01. CLEAN.
- `cond-no-parahuman-infrastructure`: No parahuman infrastructure in facet entries. CLEAN.
- `cond-smallfolk-political-physics`: All interactions (tanner-family, reeve, lords-man, elder,
  dock-runner) consistent with smallfolk political physics. CLEAN.
- `cond-feudal-hierarchy-law`: No hierarchy violations. CLEAN.
- `cond-fauna-control-rules` / `cond-fauna-control-rules-125ac-addendum`: Network operates within
  300m sphere. Khepri-mantle sealed at story-open; no mantle use. CLEAN.
- `cond-reincarnation-mechanics-125ac`: Taylor wakes in Tya's body. No mechanic violations. CLEAN.
- `cond-series-tone-constraints-125ac`: No triumph beats, no catharsis, no momentum-driven
  adventure pacing visible in facet entries. 80% rung-1 tensometer distribution and 25.2%
  narrator-interest density confirm contemplative-procedural register. CLEAN.

**8-C: PASS** — Lore constraint check

- `cond-westerosi-superstition-frame` / `cond-crownlands-superstition-frame-125ac`: No
  anachronistic knowledge or world-mechanic violation in any facet entry. CLEAN.

---

## Class 9: AP-SCAN

**AP-1 (ambient escalation):** No transitional beat elevated above its face charge. Yard-crossing,
log-closing, relay beats consistently rated 1. PASS.

**AP-2 (speech-beat default):** All "speaks to" proto-lines checked:
@85 (elder speaks to father) = rung 1; @86 (elder speaks to Taylor) = 3 — justified as
routing-as-irreversible-commitment (the routing-act, not the speech-content, is rated);
@88 (Taylor speaks to elder) = 1; @130 (maester speaks to room) = 1; @148 (elder speaks to
runner) = 2 (approach-to-commitment arc); @150 (runner speaks to elder) = 2; @153 (runner
speaks to Taylor) = 1; @154 (Taylor speaks to runner) = 1. No speech-beat auto-default found.
PASS.

**AP-3 (feeling — named-feeling vocabulary):** All feeling.md entries scanned. No "feels" verb,
no named-feeling tokens (fear, grief, anger, etc.), no hedges (like/as if/almost/nearly).
Body register only throughout all 13 entries across 6 character forks. PASS.

**AP-4 (inflation):** KICKBACK-1 (Scene E) and KICKBACK-2 (Scene J) declared as kickbacks
rather than scalar inflations. KICKBACK-3 (Scene L) RESOLVED via rung correction at @134, not
via inflating adjacent entries. AP4 honored throughout. PASS.

**AP-5 (metaphor at peaks — Earth-Bet leak risk):** Single surviving metaphor entry meta:2 @73
anchors at tens=1 (not a peak). Licensed by memory:3. No Earth-Bet cape-fic leak found in
the metaphor. The tens=1 placement is within rubric tolerance given the memory anchor. PASS.

**AP-6 (metaphor voice register):** "a door already shut" — spare, non-ornate. PASS.

**AP-8 (posture-as-state in state-updates):** Multiple explicit NONE-CORRECT refusals for
orientation beats documented in state-updates.md. Pattern confirmed anti-pattern-clean. PASS.

**AP-9 (density-on-flat):** Relay-transient beats explicitly refused across 10 NONE-CORRECT
entries. PASS.

**AP-10 (stylistic noting):** oc-broken-maester state-updates section correctly refuses all
four maester anchors as verbalization or transient motor events. PASS.

No new AP-SCAN findings.

---

## Class 10: TASTE-FLAG

TASTE-FLAG covers patterns the audience may flag as entertainment concerns — not constraint
violations. Mode is flag-only; taste flags are SIGNAL only. r3-signal-006 and r3-signal-007
are editor-call deferrals; they are re-fired as SIGNAL carry-forwards if they persist.

**10-A: PASS** — Narrative interest channel coverage

interest-narrator.md covers all 8 tens=3 peaks (@15, @43, @75, @86, @90, @134, @140, @151).
Scene-B/D/K silence preserved. Fauna-deviation channel not saturated (8 distinct deviation-types
across the episode). PASS.

**10-B: SIGNAL** — interest-narrator density at 25.2% (carry-forward from r3-signal-006)

- id: r4-signal-003 (carry-forward; corresponds to r3-signal-006, r1 flag-006)
- type: flag
- class: TASTE-FLAG
- severity: SIGNAL
- what: interest-narrator.md post-R2 density 39/155 ≈ 25.2%, against rubric band 15–25%.
  Overage is 0.2 percentage points (less than one entry above ceiling at 155 proto-lines).
  The R2 add of narrator:41 @14 pushed the file from 24.5% to 25.2%.
- why: The rubric ceiling is 25%; 25.2% nominally breaches it. The R2 add is well-defended
  (scene-A peak-approach gap, cost-tracking channel, non-redundant with feel:5). The practical
  effect on the stitcher is negligible. This is a taste flag, not a structural constraint
  failure.
- criteria: No action required unless the editor observes that the scene-A narrator-interest
  cluster renders as too dense in the stitched manuscript. If so, narrator:41 @14 is the
  cull candidate (R2-added, weakest cap defense in scene A).
- routing: editor (at stitch review); no fixer dispatch required
- status: editor-call deferral; carry-forward from r3-signal-006

**10-C: SIGNAL** — feeling.md per-character sparsity below 2% for non-POV characters
  (carry-forward from r3-signal-007)

- id: r4-signal-004 (carry-forward; corresponds to r3-signal-007, r1 flag-007 scope)
- type: flag
- class: TASTE-FLAG
- severity: SIGNAL
- what: oc-tanner-mother at 2/155 = 1.3%; oc-tanner-elder at 2/155 = 1.3%; oc-broken-maester
  at 1/155 = 0.6%; oc-dock-runner at 1/155 = 0.6%. All four below the 2% per-episode band
  floor. oc-tanner-father at 3/155 = 2.0% exactly at floor. Only taylor-hebert-flea-bottom
  (4/155 = 2.6%) is above floor. Per-episode aggregate all-character combined: 13/155 = 8.4%,
  well within any reasonable aggregate band.
- why: Individual per-character sparsity is low for non-POV characters because each appears
  in limited scenes with limited cap availability. The rubric note on the per-character vs
  per-aggregate interpretation is a reasonable defense. The per-character floor may need
  calibration for non-POV characters with limited scene presence; this is a forward pin for
  the editor, not a fixer dispatch.
- criteria: No mandatory action. Editor should review at stitch whether the assembled feeling.md
  renders as adequately somatic for non-POV characters given their limited scene presence.
- routing: editor (at stitch review)
- status: editor-call deferral; carry-forward from r3-signal-007

---

## Class 11: PILE-UP REVIEW

Cite-index identifies five pile-ups (> 4 co-located facets):

**@98** (8 co-located facets): loc-state:1, mem:7, narrator:25, sensory:4, state:6, state:31,
tens:92, vibes:13. Proto-line: "taylor-hebert-flea-bottom enters loc-flea-bottom."
Each facet fires on a distinct dimension of the Flea Bottom arrival: location-state records the
environment; memory records the Dance-foreknowledge clamp; narrator registers perceptual arrival;
sensory flags smell-delta; two state-updates (location + network re-establishment); tensometer
rung 1 (transitional, correct); vibe-update for operational-territory-open. No redundancy.
WARRANTED.

**@43** (7 co-located facets): feel:8, mem:6, narrator:12, sensory:3, tens:41, vibes:8, vibes:9.
Proto-line: "oc-tanner-mother drops the song."
Scene C's tens=3 peak. Convergence at 3-peak is expected per cross-facet contract. Each facet
fires on a distinct dimension: feeling (mother's hands-still somatic), memory (helpless-
protector/failed-recognition monument), narrator (silence-as-Tya-shaped-absence), sensory
(song→silence sound-drop), tensometer rung 3, two vibes with distinct keywords on mother.
No redundancy. WARRANTED.

**@103** (7 co-located facets): loc-state:2, narrator:27, state:10, state:32, tens:97, vibes:15,
vibes:16. Proto-line: "taylor-hebert-flea-bottom enters loc-flea-bottom-base."
Second carded location arrival. Each facet fires on a distinct dimension. Tensometer rung 1
(entering-a-room is transitional, correct). WARRANTED.

**@90** (6 co-located facets): feel:3, narrator:23, state:29, tens:85, vibes:3, vibes:10.
Proto-line: "oc-tanner-elder routes taylor-hebert-flea-bottom."
Scene H climax first peak (tens=3). Each facet fires distinctly: feeling (elder's eyes-already-
past), narrator (gate-as-last-zero-cost-threshold), state-update (Taylor's placement-status),
tensometer rung 3, two vibes on distinct character targets. WARRANTED.

**@154** (5 co-located facets): feel:13, mem:9, narrator:40, state:34, tens:145.
Proto-line: "taylor-hebert-flea-bottom speaks to oc-dock-runner."
Each facet fires on a distinct dimension at the first-irreversible-social-commit beat. Tensometer
rung 1 (the speech-act reads quiet per AP-2; the commitment charge is in the narrator/memory
channel, not on the face of the beat). The non-peak pile-up is a known SEAM-1 discrepancy flagged
by the interest-narrator author; each fire is independently defensible. WARRANTED.

**Overall pile-up verdict: ALL FIVE WARRANTED.** No pile-up creates a finding.

---

## R3 Signal Closure Report

| Signal ID | Class | Fix applied | R4 status |
|-----------|-------|-------------|-----------|
| r3-signal-001 | STRUCTURAL | state-updates.md now carries single top-of-file frontmatter; per-source headers are plain `# source:` comments | CLOSED — PASS |
| r3-signal-002 | FREQUENCY-BAND | cond-series-tone-constraints-125ac.card.md amended with "Tensometer register characterization" paragraph (tokens slow-burn/low-rupture-density/foreknowledge-clamp + explicit tens-gate exemption) and §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" with quantified band | CLOSED — EXEMPT-TONE-LAW-SLOW-BURN |
| r3-signal-003 | METADATA-INCONSISTENCY | Cite-index regenerated; totals now show 261 (live graph state, not stale 268); tens count shows 141 (not inflated 148) | CLOSED — PASS |
| r3-signal-004 | CURVE-SHAPE / CONTRADICTION | tensometer.md entry 126 @134 updated 1→3; "3s justified" list includes @134; frequency-band section updated to 3s = 8/141 = 5.7% | CLOSED — PASS |
| r3-signal-005 | CONSTRAINT | memory.md mem:6 @43 description stripped "Annette-adjacent"; replaced with "dying-parent-recognition-fail variant" | CLOSED — PASS |
| r3-signal-006 | TASTE-FLAG | Editor-call deferral; condition unchanged (density 25.2% at ceiling) | CARRY-FORWARD as r4-signal-003 |
| r3-signal-007 | TASTE-FLAG | Editor-call deferral; condition unchanged (non-POV per-character sparsity below floor) | CARRY-FORWARD as r4-signal-004 |

---

## Audit Summary

| Class | Findings | HARD | SIGNAL | Status |
|-------|----------|------|--------|--------|
| 1 STRUCTURAL | 1 signal (1-D feeling.md) | 0 | 1 (r4-signal-001, new) | 1 pass |
| 2 FREQUENCY-BAND | flag-005 closure | 0 | 0 | EXEMPT-TONE-LAW-SLOW-BURN |
| 3 METADATA-INCONSISTENCY | memory snapshot lag (noted, not filed) | 0 | 0 | pass |
| 4 CURVE-SHAPE | pass | 0 | 0 | SHAPE-CLEAN |
| 5 CONTRADICTION | pass | 0 | 0 | pass |
| 6 DEDUP | pass | 0 | 0 | pass |
| 7 SUPERFLUOUS | pass | 0 | 0 | pass |
| 8 CONSTRAINT | 1 signal (r4-signal-002, new — mem:9 Undersiders slug) | 0 | 1 | 1 pass |
| 9 AP-SCAN | pass | 0 | 0 | pass |
| 10 TASTE-FLAG | 2 signals (carry-forwards) | 0 | 2 (r4-signal-003, r4-signal-004) | -- |
| 11 PILE-UP | all warranted | 0 | 0 | pass |

**HARD: 0**
**SIGNAL: 4** (r4-signal-001 [new], r4-signal-002 [new], r4-signal-003 [carry-forward editor-call],
r4-signal-004 [carry-forward editor-call])

**flag-005: EXEMPT-TONE-LAW-SLOW-BURN** — all four criteria satisfied by post-amendment card.

**CURVE-SHAPE: SHAPE-CLEAN** — @134=3 confirmed; all named scenes pass or are transit-exempt or
  carry documented kickback declarations. No residual shape anomaly.

---

## Routing Block

| Finding | Class | Routing |
|---------|-------|---------|
| r4-signal-001 | STRUCTURAL | dialogue-writer-fork (feeling.md consolidation; collapse per-source YAML blocks to plain comments per state-updates.md pattern) |
| r4-signal-002 | CONSTRAINT | memory author (dialogue-writer-fork:taylor-hebert-flea-bottom) — revise mem:9 slug/monument name; margit (slug validation at promotion) |
| r4-signal-003 | TASTE-FLAG | editor (at stitch review) — no fixer dispatch |
| r4-signal-004 | TASTE-FLAG | editor (at stitch review) — no fixer dispatch |

---

## Episode Status

**Status: CLEAN** (HARD = 0; r3-signal-001 through r3-signal-005 all confirmed CLOSED; the two
editor-call carry-forwards persist as SIGNAL only; two new SIGNALs identified).

The two new SIGNALs (r4-signal-001, r4-signal-002) are fixable without graph reconstruction:
- r4-signal-001 requires collapsing feeling.md per-source YAML blocks to plain comments —
  a format operation, not a content change.
- r4-signal-002 requires renaming the mem:9 monument slug to mechanism-descriptive form
  without the Earth-Bet proper noun.

Neither new SIGNAL creates a HARD finding. The orchestrator-critic verdict at Phase 6 can move
toward SUCCESS on this episode: HARD = 0, all five fixer-addressed r3 signals confirmed closed,
flag-005 confirmed EXEMPT-TONE-LAW-SLOW-BURN, CURVE-SHAPE CLEAN.
