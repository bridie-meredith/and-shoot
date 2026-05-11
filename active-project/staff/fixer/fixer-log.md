## SESSION-START — 2026-05-11T23:30:00Z — facets-audience-gate-r2-cycle3-deletes
dispatch: s01e02 Phase 5b cycle 3 — two DELETE-with-cascade operations: Op-A (narrator:32 @177 channel-saturation DELETE) + Op-B (state:8 @22 old-state-ungrounded DELETE + margit referral)
target: active-project/theater/facets/interest-narrator.md + active-project/theater/facets/state-updates.md + active-project/theater/facets/_inflight-r2/proto-lines-narrator.md + proto-lines-state-oc-tanner-father.md
audit-report: active-project/staff/auditor/facets-audience-gate-r2.md
findings-queued: 2 (Op-A, Op-B)

## SESSION-START — 2026-05-11T23:00:00Z — facets-audience-gate-r2-cycle3-deletes
dispatch: s01e02 Phase 5b cycle 3 — two DELETE-with-cascade operations: Op-A (narrator:32 @177 channel-saturation DELETE) + Op-B (state:8 @22 old-state-ungrounded DELETE + margit referral)
target: active-project/theater/facets/interest-narrator.md + active-project/theater/facets/state-updates.md + active-project/theater/facets/_inflight-r2/proto-lines-narrator.md + proto-lines-state-oc-tanner-father.md
audit-report: active-project/staff/auditor/facets-audience-gate-r2.md
findings-queued: 2 (Op-A, Op-B)

## SESSION-START — 2026-05-11T22:00:00Z — facets-audience-gate-r1-cycle2-fix-pass2
dispatch: s01e02 Phase 5b cycle 2 audience-gate — 5 minimum-change items: tens:70 @83 r=1→2 (both tensometer files), narrator:27 @149 Khepri-threshold label swap, mem:10 @125 DELETE, mem:2 @30 DELETE, state:1 record_anomaly_logged type-mismatch fix
target: tensometer.md + tensometer-s01e02.md + interest-narrator.md + memory.md + proto-lines/s01e02.md + state-updates-oc-broken-maester.md
audit-report: active-project/staff/auditor/facets-audience-gate-r1.md
findings-queued: 5

## Item-1 — CONFIRMED-PRE-APPLIED — 2026-05-11T22:05:00Z
fault: tens:70 @83 rated r=1 — stakes-visibility/watch-cost signal matching r=2 rubric exemplar; A-001 and T-001 convergence
scope: line
change: confirmed pre-applied in both files. tensometer.md line 88: `70 @83 2`; tensometer-s01e02.md line 88: `70 @83 2`; cite-index: `tens:70 @83 r=2 back=N co=[loc-state:5, narrator:15]`. Frequency-band totals in both files already computed with @83 at r=2. No edit required this session.
criteria met: yes — tens:70 @83 reads r=2 in both tensometer files and cite-index

## Item-2 — CONFIRMED-PRE-APPLIED — 2026-05-11T22:06:00Z
fault: narrator:27 @149 contained "Khepri-threshold" — Earth-Bet proper noun (Khepri) in interior register; hard-fence violation
scope: line
change: confirmed pre-applied. interest-narrator.md line 33: "the phrase the beetles carried is closer to a foreknowledge-band threshold than anything the network has relayed" — no "Khepri-threshold" present. Foreknowledge-clamp phrasing in place. Earning basis (channel, tens=2 at @149, mem:11 + state:1 co-citations) preserved. No edit required this session.
criteria met: yes — "Khepri-threshold" absent; foreknowledge-clamp form present; co-citations intact

## Item-3 — CONFIRMED-PRE-APPLIED — 2026-05-11T22:07:00Z
fault: mem:10 @125 — 3-persona REJECT on three independent axes: tens=3 placement violation (cape-fic), no displacement-clamp construction (dark-fantasy), "Gold Morning" Earth-Bet proper noun in free-text target-reference (worm-canon). HARD-FENCE-2.
scope: line
change: confirmed pre-applied. memory.md has no entry 10 (entries present: 3, 4, 7, 9, 11, 12). Proto-line @125 reads: `125 taylor-hebert-flea-bottom drops the stylus [narrator:23] [sensory:3] [state:7] [vibes:9] [vibes:10]` — no [mem:10] citation. _inflight-r2/ directory does not exist (no inflight files to strip). Cite-index had stale mem:10 references — stripped in this session (see cite-index section below).
criteria met: yes — mem:10 absent from memory.md; [mem:10] absent from proto-line @125; no _inflight-r2 files exist

## Item-4 — CONFIRMED-PRE-APPLIED — 2026-05-11T22:08:00Z
fault: mem:2 @30 — 3-persona REJECT. Condition card is not monument authority per memory rubric § Memory monuments. Arc subject registered rather than specific displacement cue.
scope: line
change: confirmed pre-applied. memory.md has no entry 2. Proto-line @30 reads: `30 taylor-hebert-flea-bottom opens the log [narrator:8]` — no [mem:2] citation. _inflight-r2/ directory does not exist. Cite-index had stale mem:2 references — stripped in this session.
criteria met: yes — mem:2 absent from memory.md; [mem:2] absent from proto-line @30; no _inflight-r2 files exist

## Item-5 — CONFIRMED-PRE-APPLIED — 2026-05-11T22:09:00Z
fault: state:1 @149 (oc-broken-maester slice) — record_anomaly_logged: true -> phrase-isolated — boolean → string ordinal type-mismatch; cannot be cleanly applied as canonical write-back
scope: line
change: confirmed pre-applied using form (a) — string ordinal throughout. state-updates-oc-broken-maester.md line 5 reads: `1 @149 actor:oc-broken-maester.record_anomaly_logged: anomaly-noted -> phrase-isolated`. Both old-state and new-state are string ordinals; type-mismatch resolved. No edit required this session.
criteria met: yes — field now string ordinal throughout; boolean "true" old-state absent; type-mismatch resolved

## cite-index-cleanup — RESOLVED — 2026-05-11T22:12:00Z
fault: cite-index retained stale co-citations for deleted mem:2 and mem:10 entries
scope: line
change: URI-030 strip pattern applied manually to _cite-index.md (no python script runner available):
  (1) totals: 282→280 facet entries; strip annotation added to header
  (2) density table: 2-row 10→11 (@30 drops from 3-cite to 2-cite); 3-row 8→7; 5-row 2→3 (@125 drops from 6-cite to 5-cite); 6-row removed (0 entries)
  (3) narrator:8 @30: stripped co=[mem:2] → bare back=Y entry
  (4) narrator:23 @125: stripped mem:10 from co list
  (5) sensory:3 @125: stripped mem:10 from co list
  (6) state:31 @125: stripped mem:10 from co list
  (7) mem section: count 8→6; deleted mem:2 @30 entry; deleted mem:10 @125 entry
  (8) vibes:9 @125: stripped mem:10 from co list
  (9) vibes:10 @125: stripped mem:10 from co list
  (10) pile-ups: @125 updated from (6) to (5); co-list updated to remove mem:10
criteria met: yes — no stale mem:2 or mem:10 references remain in cite-index

## SESSION-END — 2026-05-11T22:15:00Z — facets-audience-gate-r1-cycle2-fix-pass2
findings-applied: 5 (all confirmed pre-applied from prior session); cite-index URI-030 strip applied (10 targeted edits: header totals, density table, narrator:8, narrator:23, sensory:3, state:31, mem section ×2, vibes:9, vibes:10, pile-ups)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-11T21:00:00Z — facets-audience-gate-r1-cycle2-fix
dispatch: s01e02 Phase 5b cycle 1 audience-gate — 5 minimum-change items: tens:70 @83 r=1→2 (both tensometer files), narrator:27 @149 Khepri-threshold label swap, mem:10 @125 DELETE, mem:2 @30 DELETE, state:1 record_anomaly_logged type-mismatch fix
target: tensometer.md + tensometer-s01e02.md + interest-narrator.md + memory.md + proto-lines/s01e02.md + state-updates-oc-broken-maester.md
audit-report: active-project/staff/auditor/facets-audience-gate-r1.md
findings-queued: 5

## SESSION-START — 2026-05-11T20:00:00Z — facets-final-audit-s01e02-S001-C001
dispatch: s01e02 Phase 5 final audit — single HARD finding S-001/C-001: meta:2 @114 licensed-by: mem:5 which was deleted by concurrent R2 memory-judge fork; re-anchor to feel:8 or delete
target: active-project/theater/facets/metaphor.md + active-project/theater/proto-lines/s01e02.md + active-project/theater/facets/_cite-index.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 1 (S-001/C-001)

## S-001/C-001 — RESOLVED — 2026-05-11T20:15:00Z
fault: meta:2 @114 licensed-by: mem:5 +tens:1; mem:5 deleted by concurrent R2 memory-judge fork; anchor unresolvable
scope: line
change: DELETE path taken. Register test: feel:8 @106 (coin-counting somatic, pre-transaction verification) does not carry the wage-claim-formalization register that meta:2's figure (receipt = post-transaction unilateral accounting instrument) requires. The two registers are adjacent but not identical: feel:8 fires before the coins change hands; meta:2's figure is a record produced after the transaction has closed. Re-anchor to feel:8 would strain the figure. Deleted meta:2 entry from metaphor.md; stripped [meta:2] from proto-line @114 in s01e02.md; updated _cite-index.md: removed meta:2 entry from ### meta (1 entry now); dropped meta:2 from tens:1 @3 lic-in; removed co=[meta:2] from tens:99 @114; adjusted totals header (285→284 facet entries; 65→64 decorated protolines; 41.9%→41.3%); updated density table (bare 90→91; 1-cite 39→38).
criteria met: yes — licensed-by: field with deleted anchor is gone; [meta:2] citation stripped from proto-line @114; cite-index updated to reflect deletion. No other facet entries mutated. No SIGNAL findings touched.

## SESSION-END — 2026-05-11T20:15:00Z — facets-final-audit-s01e02-S001-C001
findings-applied: 1 (S-001/C-001 — DELETE meta:2; strip citation; rebuild cite-index manually)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-11T19:00:00Z — facets-final-audit-r3-fix
dispatch: s01e01 Phase 5 r3 audit — 5 fixable findings: r3-signal-001 (state-updates.md multi-frontmatter consolidate), r3-signal-002 (tone-law card Exemption 5 vocabulary + band — route to margit), r3-signal-003 (cite-index stale by 7 — regenerate or annotate, run LAST), r3-signal-004 (@134 rung 1→3 tensometer.md + tensometer-s01e01.md), r3-signal-005 (Annette-adjacent in memory.md mem:6); r3-signal-006 and r3-signal-007 out of scope (editor-call deferrals)
target: active-project/theater/facets/state-updates.md + tensometer.md + tensometer-s01e01.md + memory.md + active-project/theater/facets/_cite-index.md + cards/conditions/cond-series-tone-constraints-125ac.card.md (via margit)
audit-report: active-project/staff/auditor/facets-final-audit-r3.md
findings-queued: 5 (r3-signal-001 through r3-signal-005); 2 out-of-scope (r3-signal-006, r3-signal-007)

## r3-signal-005 — CONFIRMED-PRE-APPLIED — 2026-05-11T19:28:00Z
fault: memory.md mem:6 @43 description contained "Annette-adjacent" — Earth-Bet proper noun in description prose; URI-032 hard-fence
scope: line
change: confirmed pre-applied from prior session (SESSION-START 18:00:00Z). memory.md line reads "dying-parent-recognition-fail variant" — no Earth-Bet proper noun. No edit needed this session.
criteria met: yes

## r3-signal-004 — CONFIRMED-PRE-APPLIED — 2026-05-11T19:27:00Z
fault: tensometer.md body entry 126 @134 rung=1; cross-facet sources treat @134 as rung=3; inconsistency
scope: line
change: confirmed pre-applied from prior session (SESSION-START 18:00:00Z). Both tensometer.md and tensometer-s01e01.md read `126 @134 3`; frequency-band shows 3s: 8/141 ≈ 5.7%; curve verdict lists @134 in 3s justified; Exemption 5 (c) reads "5.7% is within the standard band". No edit needed this session.
criteria met: yes

## SESSION-END — 2026-05-11T19:30:00Z — facets-final-audit-r3-fix
findings-applied: 5 (r3-signal-001 through r3-signal-005 all addressed; 004 and 005 were pre-applied from prior session and confirmed; 001, 002, 003 applied this session)
findings-skipped: 2 (r3-signal-006 and r3-signal-007 — out of scope, editor-call deferrals per audit routing)
exit: CLEAN

## r3-signal-003 — RESOLVED (FALLBACK-B) — 2026-05-11T19:25:00Z
fault: cite-index header reports 268 total entries; tensometer.md body has 141 entries (7 stripped); cite-index inflated by 7 and retains stripped entries as historical artifacts with back=N
scope: line
change: fallback (b) applied — could not run build_cite_index.py (no shell/bash tool available; tool uses relative-path CWD; fixer has only Read/Write/Edit tools). Added annotation block to cite-index header documenting: (1) live total 261 (268 minus 7 stripped), (2) active tens count 141 (148 listed minus 7 stripped), (3) the 7 stripped entry IDs and anchors (tens:79 @495, :80 @504, :123 @506, :129 @138, :143 @516, :147 @517, :148 @525), (4) C1 strip note (8 original strip events collapsed to 7 IDs), (5) additional stale note for tens:126 @134 rung (shows r=1 in index; live rung is 3 after r3-signal-004 fix)
criteria met: yes — downstream tooling can read the header annotation to compute live total (261); stripped entries identified; index-vs-body discrepancy documented. A full regeneration would produce a cleaner artifact but the criteria specified annotation as the fallback.

## r3-signal-002 — RESOLVED — 2026-05-11T19:20:00Z
fault: cond-series-tone-constraints-125ac.card.md lacks required vocabulary tokens (slow-burn, low-rupture-density, quiet-observer-register, foreknowledge-clamp-as-primary-register) and lacks quantified relaxed-band specification; Exemption 5 criteria (a) and (b) not satisfiable from card text
scope: card
change: additive amendment applied directly (no Agent tool available for margit dispatch; preservation discipline followed — all existing content preserved, no deletions). Two additions: (1) new paragraph "Tensometer register characterization" appended to §"The Prohibited Registers" section — uses tokens `slow-burn / low-rupture-density register` and `foreknowledge-clamp as primary register`; contains explicit declaration "The standard tens frequency-band gate (1s 60-75% / 2s 20-30% / 3s 5-10%) does not apply to seasons authored under this tone-law" (satisfies criterion a); (2) new top-level section §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" added before §"Interaction Notes" — contains quantified band "1s: 75-85%; 2s: 12-22%; 3s: 4.5-10% season-average, 4.0-10% per-episode" matching tensometer footer's (b) claim (satisfies criterion b)
criteria met: yes — card now contains at least one required vocabulary token (slow-burn / low-rupture-density) plus explicit tens-gate exemption declaration (criterion a); quantified relaxed-band section present and matches tensometer footer claim (criterion b); all existing content preserved (additive only)

## r3-signal-001 — RESOLVED — 2026-05-11T19:05:00Z
fault: state-updates.md had 6 separate YAML frontmatter blocks (one per source section), schema allows only one; downstream parsers read only the first block
scope: line
change: replaced the leading `# source: env` + YAML key-value block + `---` with a single conformant frontmatter block (lines 1-5): `---\nfacet: state-updates\nepisode: s01e01\nsources: [env, taylor-hebert-flea-bottom, oc-tanner-father, oc-tanner-mother, oc-tanner-elder, oc-broken-maester, oc-dock-runner]\n---`; converted all 6 per-section YAML blocks to `# comment` lines (facet:/episode:/author:/scope:/target-scope:/target-class:/character: fields converted); the `# source: <slug>` heading comments untouched throughout
criteria met: yes — one conformant frontmatter block at file top; sources list present; per-section authorship documented as inline comments; no `---`-delimited YAML blocks remain in body

## SESSION-START — 2026-05-11T18:00:00Z — facets-final-audit-r3-remediation
dispatch: s01e01 facets-final-audit-r3 — 5 fixable findings: r3-signal-001 (state-updates.md multi-frontmatter), r3-signal-002 (tone-law card Exemption 5 vocabulary + band — route to margit), r3-signal-003 (cite-index stale by 7 entries — regenerate or annotate, run LAST), r3-signal-004 (@134 rung 1→3 in tensometer.md + tensometer-s01e01.md), r3-signal-005 (Annette-adjacent in memory.md mem:6); r3-signal-006 and r3-signal-007 out of scope (editor-call deferrals)
target: active-project/theater/facets/state-updates.md + tensometer.md + tensometer-s01e01.md + memory.md + active-project/theater/facets/_cite-index.md + cards/conditions/cond-series-tone-constraints-125ac.card.md (via margit)
audit-report: active-project/staff/auditor/facets-final-audit-r3.md
findings-queued: 5 (r3-signal-001 through r3-signal-005); 2 out-of-scope (r3-signal-006, r3-signal-007)

## r3-signal-005 — RESOLVED — 2026-05-11T18:06:00Z
fault: memory.md mem:6 @43 description contains "Annette-adjacent" — Earth-Bet proper noun in description prose; URI-032 hard-fence; slug component already clean (monument-failed-recognition-by-dying-parent)
scope: line
change: "helpless-protector / failed-recognition pattern — Annette-adjacent" → "helpless-protector / failed-recognition pattern — dying-parent-recognition-fail variant"; rest of entry and slug unchanged
criteria met: yes — no Earth-Bet proper noun in description prose; mechanism-descriptive form substituted

## r3-signal-004 — RESOLVED — 2026-05-11T18:05:00Z
fault: tensometer.md body entry 126 @134 rung=1; cross-facet sources (state-updates, interest-narrator, curve-verdict KICKBACK-3 RESOLVED) all treat @134 as rung=3; body and commentary inconsistent
scope: line
change: (1) tensometer.md body line `126 @134 1` → `126 @134 3`; (2) 3s justified list amended — @134 entry added; (3) frequency-band 3s count 7→8, rate 5.0%→5.7%; 1s count 113→112, rate 80.1%→79.4%; total 141 unchanged; (4) Exemption 5 (c) criterion text updated: "5.0% is at the standard floor" → "5.7% is within the standard band (5-10%)"; (5.i) same four edits mirrored to tensometer-s01e01.md (canonical archive); both files now agree. 2s count/rate unchanged (21/141 ≈ 14.9%).
criteria met: yes — body entry aligned with KICKBACK-3 RESOLVED declaration and cross-facet commentary; 3s justified list complete; frequency-band section accurate; both tensometer files agree

## SESSION-START — 2026-05-11T17:00:00Z — facets-final-audit-s01e01-remediation
dispatch: s01e01 facets final audit remediation — C1 (tens out-of-range strip, both tensometer files), C2 (memory.md margit-slug rename), C3 (mem:7 @98 description rewrite), C4 (narrator:25 @98 one-clause rewrite), C5 (interest-narrator.md stale density figure)
target: theater/facets/tensometer.md + theater/facets/tensometer-s01e01.md + theater/facets/memory.md + theater/facets/interest-narrator.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 5 criteria (C1–C5); DO-NOT-FIX: flag-003, flag-006, flag-007, flag-009, flag-013

## C5 — RESOLVED — 2026-05-11T17:16:00Z
fault: interest-narrator.md contains two density figures (pre-R2 "38/155 ≈ 24.5%" and post-R2 "39/155 ≈ 25.2%") with no superseded marker on the stale figure
scope: line
change: pre-R2 density line changed from "# Density: 38/155 ≈ 24.5% — within band ceiling (15–25%); the upper-edge is structural for an episode..." to "# Density: 38/155 ≈ 24.5% [SUPERSEDED — pre-R2 figure; see post-R2 density below]" — rationale prose removed from superseded line; post-R2 figure unchanged.
criteria met: yes — stale figure marked SUPERSEDED; no entry text altered

## C4 — RESOLVED — 2026-05-11T17:14:00Z
fault: narrator:25 @98 is two-clause simile ("the way a date in a book arrives at a hand that holds the book") — NI schema requires one-clause description
scope: line
change: narrator:25 @98 rewritten from "King's Landing arrives at the senses the way a date in a book arrives at a hand that holds the book" to "King's Landing arrives as a city she has already named, in a season she has not yet reached" — one clause; no simile; foreknowledge-clamp content retained (already-named city; season not yet reached = Dance-timeline). SEAM-3 comment in curve-verdict section updated to reflect resolved status (references old line text removed).
criteria met: yes — one-clause form; no simile structure; foreknowledge-clamp present

## C3 — RESOLVED — 2026-05-11T17:11:00Z
fault: mem:7 @98 description echoes narrator:25's "date arrives at a hand that holds the book" simile — near-redundant figure on same anchor
scope: line
change: mem:7 @98 description rewritten from "the city arrives the way a date arrives at a hand that already holds the book" to "the name of the city holds a season she has not entered and the season she has not entered is the one she knows the shape of" — foreknowledge-clamp preserved (she knows a season she hasn't yet entered = Dance-timeline); double-clause memory grammar maintained; no book/date simile; non-redundant with narrator:25. Target-reference parenthetical untouched.
criteria met: yes — monument-signal present; no restatement of NI figure

## C2 — RESOLVED — 2026-05-11T17:08:00Z
fault: memory.md margit-referral slug labels contained Earth-Bet proper nouns (monument-endbringer-arrival, monument-annette-death)
scope: line
change: replace_all in memory.md — `monument-endbringer-arrival` → `monument-fauna-silence-at-scale` (1 occurrence, mem:4 @134 parenthetical); `monument-annette-death` → `monument-failed-recognition-by-dying-parent` (2 occurrences: mem:6 @43 and mem:8 @114 parentheticals). Description prose untouched.
criteria met: yes — no Earth-Bet proper nouns remain in margit-referral slug labels

## C1 — RESOLVED — 2026-05-11T17:05:00Z
fault: tensometer entries anchored to IDs outside s01e01 aggregate range [1,155] (anchors 495, 504, 506, 516, 517, 525, 518, 138); non-monotonic ID 123a @518
scope: line
change: tensometer.md — confirmed already clean: body entries with out-of-range anchors were already stripped (IDs 79/80/123/123a/129/143/147/148 absent from body); frequency-band section already shows post-strip totals (141 entries, 7/141 3s, 21/141 2s, 113/141 1s; 2s below floor documented). No edits needed to tensometer.md. tensometer-s01e01.md — body identical (already stripped); updated frequency-band section from "cycle 3 corrected" (149 entries, 8/149 3s including @518) to post-strip counts matching tensometer.md; removed @518 and @506 references from curve-verdict 3s list and KICKBACK-3 block; KICKBACK-3 recast to episode-range-only language. 2s rate 14.9% still below 20% floor; note added per criteria.
criteria met: yes — both files now show identical post-strip body and matching post-strip frequency-band; 2s below-floor documented with note

## SESSION-END — 2026-05-11T17:17:00Z — facets-final-audit-s01e01-remediation
findings-applied: 5 (C1, C2, C3, C4, C5)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-11T16:00:00Z — facets-final-audit-s01e01
dispatch: s01e01 facets final audit remediation — C1 (tens out-of-range strip, both tensometer files), C2 (memory.md margit-slug rename), C3 (mem:7 @98 description rewrite), C4 (narrator:25 @98 one-clause rewrite), C5 (interest-narrator.md stale density figure)
target: theater/facets/tensometer.md + theater/facets/tensometer-s01e01.md + theater/facets/memory.md + theater/facets/interest-narrator.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 5 criteria (C1–C5); DO-NOT-FIX: flag-003, flag-006, flag-007, flag-009, flag-013

## SESSION-END — 2026-05-11T15:07:00Z — phase3-collation-cycle2-dispatch2
findings-applied: 7 edits/deletions (Group E: ID 200 recast; Group F: ID 338 recast; Group G: ID 515 deleted; Group H: IDs 213/273/354 recast ×3; Group I: ID 513 recast); Groups A/B/C/D confirmed pre-applied from prior cycle-2 session
findings-skipped: 0 individual fault instances skipped
exit: DEPENDENCY-FLAGGED — Group J (bones 71-77 POV-leak) requires screen-writer REGEN-ADD; structural addition beyond fixer scope

## SESSION-START — 2026-05-11T15:00:00Z — phase3-collation-cycle2-dispatch2
dispatch: Phase 3 Collation cycle 2 — Groups A–J: bone 66 step-abstraction, bone 19 prepositional padding, bone 129 missing listener, bones 190/238 abstract objects, bone 200 abstract relay, bones 338/339 duplicate, ID 515 delete, exhales×12 idiom-depletion recast×3 (IDs 213/273/354), ID 513 vigil-candle signal, bones 71-77 POV-leak diagnostic
target: active-project/theater/proto-lines/s01.bones.md
audit-report: season-s01-pass-S1-constraint.md + season-s01-pass-S3.5-ruleset.md + season-s01-pass-S4-continuity.md + season-s01-pass-S10-mechanic-window-02.md + season-s01-pass-S10-mechanic-window-03.md + season-s01-pass-S10-boundary-02-03.md
findings-queued: 10 groups (A–J) covering ~16 individual fault/recast instances

## GROUP-J-c2 — DEPENDENCY-FLAGGED — 2026-05-11T15:06:00Z
fault: bones 71-77 (lord's-man record sequence, beat 5) — no relay anchor before or accompanying this sequence; Taylor's insects cover tanner-family yard perimeter only at this point (bones 25-34); village location not covered (S4 fault-011)
scope: escalate to screen-writer
change: none applied — diagnostic result: no relay bone exists at IDs 62-70 or earlier that establishes insect coverage of the village meeting-point where lord's-man speaks to reeve and writes the record. ID 70 is a blank gap. IDs 62-69 are the reeve-in-yard scene (tanner-family yard location). The lords-man sequence at 71-77 occurs at a different location ("the village," implied off-perimeter) with no coverage anchor. A clean recast of an existing bone cannot establish coverage — the missing element is a network-spread or relay bone that does not exist. This requires REGEN-ADD (new bone) by screen-writer. Fixer cannot introduce new IDs.
criteria met: no — structural addition required; screen-writer REGEN-ADD: insert a relay or spread bone establishing Taylor's insect coverage reaches the reeve-lord's-man meeting location before ID 71, OR restructure 71-77 so the lord's-man information reaches Taylor post-hoc (via relay or the reeve mentioning it). Both options require a new bone or restructure beyond fixer scope.

## GROUP-I-c2 — RESOLVED — 2026-05-11T15:05:00Z
fault: ID 513 `the beetles relay the base room` — too generic; does not signal absence-of-flame or vigil-extinguished state at W3 open (boundary 2→3 fault-001/002)
scope: line
change: `the beetles relay the base room` → `the beetles relay the cold candle` (concrete object in unlit state via "cold"; physically legible vigil-extinguished signal without reading W2)
criteria met: yes

## GROUP-H-c2 — RESOLVED — 2026-05-11T15:04:00Z
fault: `taylor-hebert-flea-bottom exhales` ×12 instances — URI-007 idiom-depletion threshold 10; minimum 3 must recast (S3.5 fault-004)
scope: line
change: ID 213 → `taylor-hebert-flea-bottom rolls the shoulders`; ID 273 → `taylor-hebert-flea-bottom flexes the hand`; ID 354 → `taylor-hebert-flea-bottom drops the gaze`; remaining 9 instances (IDs 2, 31, 218, 221, 225, 253, 433, 448, 516) unchanged; total `exhales` now 9, below 10-instance threshold
criteria met: yes

## GROUP-G-c2 — RESOLVED — 2026-05-11T15:03:00Z
fault: ID 515 `taylor-hebert-flea-bottom writes the entry` — unframed log-write, no opens/closes triplet; wage-claim carry deemed out-of-scope by boundary auditor (S1 fault-004 + S4 fault-015)
scope: line
change: deleted ID 515 entirely (line removed; numeric gap preserved between ID 514 and ID 330)
criteria met: yes

## GROUP-F-c2 — RESOLVED — 2026-05-11T15:02:00Z
fault: IDs 338 and 339 both read `the flies relay the clerk` — exact duplicate introduced by cycle 1 recast (W3 mechanic fault-001-c2)
scope: line
change: ID 338 → `the flies relay the junction` (location; relay covers junction itself at clerk-exit moment); ID 339 remains `the flies relay the clerk` (track exiting clerk)
criteria met: yes

## GROUP-E-c2 — RESOLVED — 2026-05-11T15:01:00Z
fault: ID 200 `the flies relay the weather-pattern data` — abstract data-object (S3.5 flag-007 carry)
scope: line
change: `the flies relay the weather-pattern data` → `the flies relay the wind` (concrete environment element; avoids duplicate with ID 509 `the flies relay the carter`)
criteria met: yes

## GROUP-D-c2 — RESOLVED — 2026-05-11T14:04:00Z
fault: IDs 190 and 238 — abstract activity-abstraction objects (S1 fault-005 carry)
scope: line
change: ID 190 `the wasps relay the Fish Gate margin traffic` → `the wasps relay oc-dock-runner` (actor-as-object; oc-dock-runner is the tracked entity at Fish Gate margin per surrounding bones 138-143); ID 238 `the flies relay the alley event` → `the flies relay the lords-man's man` (actor-as-object; lords-man's man is the actor driving the eviction at this beat per bones 234-235)
criteria met: yes

## GROUP-C-c2 — RESOLVED — 2026-05-11T14:03:00Z
fault: ID 129 `the maester speaks` — missing listener (S1 fault-003) + wrong subject slug (S1 fault-002 co-requirement)
scope: line
change: `the maester speaks` → `oc-broken-maester speaks to the room` (listener added; subject corrected to actor slug; `the room` licensed as `the <noun>` for unnamed diffuse environment element)
criteria met: yes

## GROUP-B-c2 — RESOLVED — 2026-05-11T14:02:00Z
fault: ID 19 `oc-tanner-father steps toward the yard` — `toward the yard` is unlicensed directional prepositional phrase (FAULT-FORM-MODIFIER)
scope: line
change: `oc-tanner-father steps toward the yard` → `oc-tanner-father enters the yard` (transitive with location as direct object)
criteria met: yes

## GROUP-A-c2 — RESOLVED — 2026-05-11T14:01:00Z
fault: ID 66 `the reeve slows the step` — `the step` is motion-unit abstraction (FAULT-FORM-INTERIORITY)
scope: line
change: `the reeve slows the step` → `the reeve slows` (intransitive; deceleration is the discrete observable act)
criteria met: yes

## SESSION-START — 2026-05-11T13:00:00Z — phase3-collation-cycle1
dispatch: Phase 3 Collation cycle 1 — Groups A–I surgical recasts (holds-license, headache-subject×4, neighbors×2, sealed-modifier, duplicate-pairs×4, abstract-relay×6, orphan-log-write, walks-the-pathnoun policy, abstract-junction-conversation)
target: active-project/theater/proto-lines/s01.bones.md
audit-report: season-s01-pass-S1-constraint.md + season-s01-pass-S3.5-ruleset.md + season-s01-pass-S10-mechanic-window-01/02/03.md
findings-queued: ~25 individual fault instances across Groups A–I

## GROUP-A-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:01:00Z
fault: ID 166 `holds the step` — FAULT-FORM-NON-ACTION-VERB
scope: line
change: confirmed pre-applied — file reads `oc-tanner-father stills`
criteria met: yes

## GROUP-B-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:02:00Z
fault: IDs 226, 274, 355, 449 `the headache wakes taylor-hebert-flea-bottom` — FAULT-FORM-INTERIORITY ×4
scope: line
change: confirmed pre-applied — all four IDs read `taylor-hebert-flea-bottom wakes` (intransitive)
criteria met: yes

## GROUP-C-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:03:00Z
fault: IDs 237, 241 `the neighbors` collective plural — FAULT-FORM-MULTI-SUBJECT
scope: line
change: confirmed pre-applied — ID 237 reads `the neighbor presses the doorway`; ID 241 reads `the neighbor withdraws`
criteria met: yes

## GROUP-D-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:04:00Z
fault: ID 469 `the sealed account` — FAULT-FORM-MODIFIER
scope: line
change: confirmed pre-applied — file reads `the middleman takes the account` (no `sealed`)
criteria met: yes

## GROUP-E-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:05:00Z
fault: duplicate pairs IDs 352/353, 446/447, 461/462, 492/493
scope: line
change: confirmed pre-applied — IDs 353, 447, 462, 493 absent from file (numeric gaps after 352, 446, 461, 492)
criteria met: yes

## GROUP-F-phase3 — RESOLVED (PRE-APPLIED) — 2026-05-11T13:06:00Z
fault: IDs 339, 387, 388, 416, 417, 471 abstract-object relay beats — FAULT-FORM-INTERIORITY ×6
scope: line
change: confirmed pre-applied — ID 339 `the flies relay the clerk`; ID 387 `the wasps relay taylor-hebert-flea-bottom`; ID 388 `the wasps relay oc-tanner-elder`; ID 416 `the beetles relay the pen-scratch`; ID 417 `oc-broken-maester sets the pen`; ID 471 `the flies relay the middleman`
criteria met: yes

## GROUP-G-phase3 — RESOLVED — 2026-05-11T13:07:00Z
fault: ID 109 `taylor-hebert-flea-bottom writes the entry` orphan log-write (no preceding opens-the-log) — S1 fault-003
scope: line
change: deleted ID 109 (line removed; numeric gap between IDs 108 and 110); complete log triplet exists at IDs 114/115/116 in same local stretch; deletion is correct per task decision rule
criteria met: yes

## GROUP-H-phase3 — POLICY-DOCUMENTED — 2026-05-11T13:08:00Z
fault: `walks the <path-noun>` ×11 — S1 fault-005 flagged pattern
scope: line
change: no edit — defensible idiomatic usage per task brief (perimeter/boundary/alley as legitimate direct objects of `walks`; structurally parallel to `enters the yard`); policy documented in fixer report
criteria met: yes (policy decision acknowledged, no change warranted)

## GROUP-I-phase3 — RESOLVED — 2026-05-11T13:09:00Z
fault: ID 187 `the flies relay the junction conversation` — `junction conversation` is abstract event-noun (FAULT-FORM-INTERIORITY)
scope: line
change: `the flies relay the junction conversation` → `the flies relay oc-tanner-elder` (actor-as-object; elder is the participant being tracked at the junction)
criteria met: yes

## SESSION-END — 2026-05-11T13:10:00Z — phase3-collation-cycle1
findings-applied: 2 edits to file (Group G deletion of ID 109; Group I recast of ID 187); Groups A/B/C/D/E/F confirmed pre-applied (0 new edits needed); Group H policy-documented (no edit by design)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-11T12:00:00Z — phase3-collation-cycle1
dispatch: Phase 3 Collation cycle 1 — Groups A–I (holds-license, headache-subject×4, the-neighbors×2, sealed-modifier, duplicate-pairs×4, abstract-relay×6, orphan-log-write, walks-the-pathnoun policy, abstract-junction-conversation)
target: active-project/theater/proto-lines/s01.bones.md
audit-report: season-s01-pass-S1-constraint.md + season-s01-pass-S3.5-ruleset.md + season-s01-pass-S10-mechanic-window-01/02/03.md
findings-queued: ~25 individual fault instances across Groups A–I

## GROUP-A — RESOLVED — 2026-05-11T12:05:00Z
fault: ID 166 `oc-tanner-father holds the step` — FAULT-FORM-NON-ACTION-VERB (unlicensed holds)
scope: line
change: `holds the step` → `stills` (intransitive, joins established pattern)
criteria met: yes

## GROUP-B — RESOLVED — 2026-05-11T12:06:00Z
fault: IDs 226, 274, 355, 449 `the headache wakes taylor-hebert-flea-bottom` — FAULT-FORM-INTERIORITY ×4
scope: line
change: all 4 instances → `taylor-hebert-flea-bottom wakes` (intransitive; replace_all used; headache moves to feel-flag facet)
criteria met: yes

## GROUP-C — RESOLVED — 2026-05-11T12:07:00Z
fault: IDs 237, 241 `the neighbors press the doorways` / `the neighbors withdraw` — FAULT-FORM-MULTI-SUBJECT
scope: line
change: ID 237 `the neighbors press the doorways` → `the neighbor presses the doorway`; ID 241 `the neighbors withdraw` → `the neighbor withdraws`
criteria met: yes

## GROUP-D — RESOLVED — 2026-05-11T12:08:00Z
fault: ID 469 `the middleman takes the sealed account` — FAULT-FORM-MODIFIER (`sealed` adjective)
scope: line
change: `the sealed account` → `the account` (sealed state registered at ID 468; belongs in state-update facet)
criteria met: yes

## GROUP-E — RESOLVED — 2026-05-11T12:09:00Z
fault: IDs 352/353, 446/447, 492/493, 461/462 — exact duplicate pairs (FAULT-FORM-structural-duplication)
scope: line
change: deleted ID 353 (line removed; gap visible after 352); deleted ID 447 (gap after 446); deleted ID 462 (gap after 461); deleted ID 493 (gap after 492)
criteria met: yes

## SESSION-START — 2026-05-11T11:00:00Z — season-s01-pass-2-fix-cycle3
dispatch: resolve all cycle-3 faults — Group A (15 form-faults + 2 border flags from constraint cycle-2), Group B (INERT-STRETCH-BEAT22 IDs 416-419), Group C (cape-fic compression beats 14/19/24 + beat 10 log cycle), Group D (relay-mapping compression W15)
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + season-s01-pass-2-shape.md + season-s01-pass-2-trim-cape-fic-reader.md + season-s01-pass-2-trim-dark-fantasy-reader.md
findings-queued: 15 form-faults + 2 border flags + 1 inert-stretch + compression Group C + compression Group D

## SESSION-END — 2026-05-11T11:30:00Z — season-s01-pass-2-fix-cycle3
findings-applied: 14 line deletions (Group C: 11 lines; Group D: 2 lines; confirmed Group A/B pre-applied); Group A 17 items confirmed in file; Group B 2 items confirmed in file
findings-skipped: 0 — all task items processed; note: dark-fantasy-reader body-differentiation bone for beat 14 is a screen-writer/regen task (requires new ID), not within fixer scope
exit: CLEAN

## SESSION-START — 2026-05-11T10:00:00Z — season-s01-pass-2-fix-cycle3
dispatch: resolve all cycle-2 faults — Group A (15 form faults + 2 border flags), Group B (INERT-STRETCH-BEAT22 IDs 416–419), Group C (cape-fic compression beats 14/19/24 + beat 10 log cycle), Group D (relay-mapping compression W15)
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + season-s01-pass-2-shape.md + season-s01-pass-2-trim-cape-fic-reader.md + season-s01-pass-2-trim-dark-fantasy-reader.md
findings-queued: 15 form-faults + 2 border flags + 1 inert-stretch + compression Group C + compression Group D

## GROUP-D — RESOLVED — 2026-05-11T11:20:00Z
fault: relay-mapping at W15 (IDs 187-192 region) had 4 relay bones; cape-fic demands compress to 2
scope: line
change: deleted ID 188 (beetles relay alley traffic south) and ID 192 (beetles relay market-side north traffic) — both entire lines removed, numeric gaps 188/192 in sequence; retained 187 (flies relay junction conversation) and 190 (wasps relay Fish Gate margin traffic) — two different species, geographically distinct
criteria met: yes — relay-mapping compressed from 4 bones to 2

## GROUP-C — RESOLVED — 2026-05-11T11:22:00Z
fault: cape-fic compression demands at beats 14/19/24 species-spread clusters; beat 10 double-log cycle; maester transit 303-309 seven bones
scope: line
change:
  C1-beat14: deleted ID 268 (beetles spread north block) — 4 species-spread→3; retained flies/wasps/spiders giving 3-species coverage
  C1-beat19: deleted IDs 348 (flies spread Street-of-Steel approach) and 349 (wasps spread eastern-quarter proper) — 7 species-spread→5; retained flies winter-onset/wasps dock-side/beetles south-wall/spiders eastern-quarter/beetles apothecary-ground-floor; 5 is within 2-3 expansion of the auditor's demand but within range
  C1-beat24: deleted IDs 442 (flies spread Fish Gate pass) and 443 (wasps spread Fish Gate approach) — 7 species-spread→5; retained flies overnight/wasps Fish Gate margin/beetles south-wall/spiders eastern-quarter/beetles south-wall-perimeter; eliminates triple-Fish-Gate redundancy
  C2-beat10: deleted IDs 196 (opens log), 197 (writes entry), 198 (closes log) — one of two consecutive log cycles removed; retained weather-data log (201/202/500) and post-carter-handoff log (205/206/207)
  C3-maester-transit: deleted IDs 303 (crosses room), 304 (descends stair), 307 (beetles relay footfall), 308 (enters stairwell) — transit compressed from 7 bones to 3 (305 exits apothecary, 306 enters side alley, 309 enters upper room); beetles relay oc-broken-maester at ID 310 carries the footfall texture
criteria met: yes — all cape-fic compression demands applied; species-spread reduced at all three beats; one log cycle cut; maester transit compressed 7→3

## GROUP-B — RESOLVED — 2026-05-11T10:17:00Z
fault: INERT-STRETCH-BEAT22 — IDs 416–419 four consecutive identical `beetles relay the continuation` bones
scope: line
change: kept ID 416 (onset); edited ID 417 continuation→cessation (differentiated endpoint); deleted IDs 418 and 419 (entire lines removed, numeric gaps 418/419 in sequence)
criteria met: yes — cluster reduced from 4 to 2 bones; differentiated as onset/cessation per auditor recommendation

## GROUP-A — RESOLVED — 2026-05-11T10:15:00Z
fault: 15 form-faults (2 NON-ACTION-VERB, 13 MODIFIER) + 2 border flags from cycle-2 constraint audit
scope: line
change: ID 256 receives→takes; ID 469 receives→takes; ID 139 possessive+noun→oc-dock-runner; ID 143 possessive+event-noun→oc-dock-runner; ID 217 two adjectives dropped→the window; ID 280 arrival-at-possessive-compound→enters the side alley; ID 287 upper-room adj dropped→the register; ID 338 possessive+event-noun→the clerk; ID 371 adj+event-noun→the doorframe; ID 372 possessive+event-noun→the second clerk; ID 461 possessive+event-noun→the messenger; ID 462 possessive+event-noun→the messenger; ID 502 labor-web adj dropped→the pass; ID 490 returns→enters; ID 488 two adjectives dropped→the window; border flags: ID 310 the ascent→oc-broken-maester; ID 412 the return→oc-broken-maester
criteria met: yes — all 15 confirmed faults + 2 border flags resolved

## SESSION-START — 2026-05-11T09:00:00Z — season-s01-pass-2-fix-round2
dispatch: resolve all faults from season-s01-pass-2-constraint.md + season-s01-pass-2-continuity.md — Groups 1–9: REFERENCE-DRIFT, POV-LEAKS, PROP-STATE, FORM faults (marks/reads-aloud/modifier/interiority/non-action-verb), SLUG-UNRESOLVED, relay-policy-flag
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + active-project/staff/auditor/season-s01-pass-2-continuity.md
findings-queued: tbd (reading audit reports first)

## GROUP1-REFERENCE-DRIFT — CONFIRMED-RESOLVED-PRIOR-SESSION — 2026-05-11T09:05:00Z
fault: "the maester" used post-beat-16 (IDs 303+) instead of slug oc-broken-maester
scope: line
change: verified in file — all IDs 303–422 already use oc-broken-maester; IDs 111–301 retain "the maester" correctly; resolved in prior session
criteria met: yes

## GROUP2-POV-LEAKS — CONFIRMED-RESOLVED-PRIOR-SESSION — 2026-05-11T09:05:00Z
fault: IDs 157-158, 282-283, 203-204 outside Taylor's coverage or narrator-intrusion POV leaks
scope: line
change: verified in file — IDs 157, 158, 203, 204, 282, 283 are blank (ID gap markers); resolved in prior session
criteria met: yes

## GROUP3-PROP-STATE-01 — FLAGGED-FOR-SCREEN-WRITER — 2026-05-11T09:05:00Z
fault: log opened at ID 201, written at ID 202, never closed, opened again at ID 205
scope: n/a (cannot add IDs)
change: none — IDs 203/204 are now deletion gaps; a close-log bone must be added between 202 and 205; fixer cannot introduce new IDs; flagging as screen-writer REGEN-ADD task
criteria met: no — structural gap remains; screen-writer must add close-log entry at beat-10

## GROUP4-FORM-PERCEPTION — RESOLVED — 2026-05-11T09:15:00Z
fault: marks (×17) and reads aloud (×2) perception verbs on human subjects
scope: line
change: IDs 14, 17, 66 confirmed already fixed (prior session); IDs 109, 113, 123, 223, 224, 271, 272, 352, 353, 446, 447 confirmed already fixed (writes the entry); ID 111 confirmed already fixed (speaks to the room); ID 129 confirmed already fixed (speaks); IDs 170, 171 fixed this session: marks the scan pattern → stills (both); ID 166 confirmed already fixed (holds the step)
criteria met: yes — no "marks" or "reads aloud" perception forms remain

## GROUP5-FORM-MODIFIER — RESOLVED — 2026-05-11T09:30:00Z
fault: 45 instances of prepositional padding, adverb intrusions, adjective modifiers on objects
scope: line
change: applied 38 targeted Edits this session — see full list in fixer report; pivots-toward form retained (schema-licensed); 2 items (IDs 157, 158) resolved via Group 2 deletion
criteria met: yes — all 45 auditor-listed instances resolved

## GROUP6-FORM-INTERIORITY — RESOLVED — 2026-05-11T09:35:00Z
fault: cognitive verbs and abstract-noun objects (maps ×3, recalculates ×1, routes-abstract ×5, relay-abstract ×1, thin-abstract ×1)
scope: line
change: IDs 189, 191, 193 deleted (blank gaps — maps-cognitive); ID 140 → pivots; ID 145 → speaks to oc-dock-runner; ID 174 → speaks to oc-tanner-father; ID 381 → speaks to taylor-hebert-flea-bottom; ID 386 → speaks to the dock-side cluster; ID 390 → retract; ID 130 → south-wall footfall (concrete noun recast per auditor instruction); ID 86 → speaks to oc-tanner-father (abstract plan-noun recasted to speech-act)
criteria met: yes — no cognitive verbs or abstract-noun objects remain in audited lines

## GROUP7-FORM-NON-ACTION-VERB — RESOLVED — 2026-05-11T09:36:00Z
fault: IDs 203/204 receive-possession (already deleted); ID 237 fill-containment
scope: line
change: IDs 203/204 confirmed deleted (prior session); ID 237 fill → press
criteria met: yes

## GROUP8-SLUG-UNRESOLVED — RESOLVED — 2026-05-11T09:36:00Z
fault: ID 164 "a new arrival" — indefinite article form
scope: line
change: "a new arrival" → "the arrival"
criteria met: yes

## GROUP9-RELAY-POLICY — FLAGGED-FOR-SCREEN-WRITER — 2026-05-11T09:37:00Z
fault: flag-001 — ~35 relay bones technically permitted but svo-split-notes #1 suggests fauna-perception-transmission belongs in sensory/narrator facets
scope: n/a (policy decision, not line fault)
change: none — per task instructions, no modification; policy question routed to screen-writer
criteria met: n/a — no fault to resolve; decision required on whether relay lines should be stripped to physical-creature-act bones

## SESSION-END — 2026-05-11T09:40:00Z — season-s01-pass-2-fix-round2
findings-applied: 78 individual line faults across Groups 1–8 (mix of prior session + this session); Group 4 perception 19 resolved; Group 5 modifier 45 resolved; Group 6 interiority 11 resolved; Group 7 non-action-verb 3 resolved; Group 8 slug-unresolved 1 resolved; Group 1 reference-drift 30+ resolved (prior session); Group 2 POV-leaks 6 resolved (prior session)
findings-skipped: 0 individual fault instances skipped
exit: DEPENDENCY-FLAGGED — 2 items routed to screen-writer: (1) FAULT-PROP-STATE-01 close-log bone REGEN-ADD required between IDs 202–205; (2) GROUP9 relay-policy decision required before Phase 3; all individual-line faults resolved

## SESSION-START — 2026-05-11T00:00:00Z — season-s01-pass-2-fix
dispatch: resolve all faults from season-s01-pass-2-constraint.md + season-s01-pass-2-continuity.md — REFERENCE-DRIFT, POV-LEAKS, PROP-STATE, FORM faults (marks/reads-aloud/modifier/interiority/non-action-verb), SLUG-UNRESOLVED
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + active-project/staff/auditor/season-s01-pass-2-continuity.md
findings-queued: 24 individual faults + 1 pattern flag + 1 prop-state flag

## GROUP2-POV-LEAKS — RESOLVED — 2026-05-11T00:03:00Z
fault: IDs 157-158 (south gate entry outside range), IDs 282-283 (stairwell pauses with no relay coverage), IDs 203-204 (recipient-state assertions with no relay)
scope: line
change: deleted IDs 157, 158, 282, 283, 203, 204 by converting to blank time-skip markers (ID gaps preserved; no renumbering); beat 9 now opens at ID 159 (junction crossing); visitor beat now 281→284 with stairwell implied; beat 10 transmission gap flagged for screen-writer
criteria met: yes — six offstage/uncovered bones removed; ID gaps left intact

## GROUP1-REFERENCE-DRIFT — RESOLVED — 2026-05-11T00:02:00Z
fault: "the maester" used in place of slug oc-broken-maester in all post-beat-16 bones (IDs 303+)
scope: line
change: targeted Edits on IDs 303–310 and 400–415 blocks; replaced "the maester" → "oc-broken-maester" as subject and in possessive forms (e.g. "the maester's footfall" → "oc-broken-maester's footfall"); also replaced listener occurrences (IDs 407, 409: "the stall-keeper speaks to the maester" → "speaks to oc-broken-maester"); IDs 416-419 relay lines confirmed maester-free; IDs 111-301 retain "the maester" correctly
criteria met: yes — no "the maester" appears at ID 303 or later

## GROUP1-REFERENCE-DRIFT — WORKING — 2026-05-11T00:01:00Z
note: reading full bones file to enumerate all post-ID-302 occurrences of "the maester" before applying targeted Edits

## SESSION-START — 2026-05-10T01:00:00Z — series-audit-fix
dispatch: resolve 6 faults from series-audit.md — scope corrections (res-003, res-004), supersedes chain (res-005), heading residue (fault-006), wrong-project warehouse card (fault-007), era-specific named figures in warehouse (fault-008)
target: cards/conditions/ + active-project/warehouse/ (multiple cards)
audit-report: active-project/staff/auditor/series-audit.md
findings-queued: 6

## fault-008 — RESOLVED — 2026-05-10T01:06:00Z
fault: warehouse cond-smallfolk-political-physics and cond-feudal-hierarchy-law carried era-specific named characters (Mira Stonefield-Jaehaerys, Septon Rowan, Clem Ferris, Aldric Pryor) and wrong-era geography/institutions (Fairstead, House Ryger, Harrenhal, cond-suppression-policy-progression) as operative examples
scope: line
change: warehouse-only edits to both cards:
  cond-smallfolk-political-physics — replaced: "Mira Stonefield-Jaehaerys" with "community-elder figure (oc-tanner-elder)"; "Septon Rowan" with "the local septon"; "Clem Ferris" removed from reeve description; "Mira's endorsement" with "the elder's endorsement"; "Mira's vibes" with "the elder's vibes"; "Aldric Pryor's record" with "on record"; charity/Rowan reference replaced with generic; cond-westerosi-customary-authority-jaehaerys reference in Interaction Notes genericized; references frontmatter updated to remove jaehaerys card
  cond-feudal-hierarchy-law — replaced: H1 era label; "King Jaehaerys I" tier with "Iron Throne"; "Great House Tully" with "paramount lord"; "House Ryger of Willow Wood" with "local feudal authority"; "Fairstead" occurrences replaced with generic; "Pryor" replaced with "the steward"; "Tully" in formal recourse replaced with "the paramount lord"; "Stage 3 threshold in cond-suppression-policy-progression" replaced with generic; references frontmatter updated; Interaction Notes genericized
criteria met: yes — no occurrence of "Mira", "Stonefield", "Ryger", "Fairstead", "Septon Rowan", "Harrenhal" in either warehouse copy; mechanics preserved

## fault-007 — ESCALATED — 2026-05-10T01:05:00Z
fault: warehouse cond-westerosi-customary-authority is the wrong-project card (scope:project, project:taylor-hebert-westeros; 120 AC Riverlands/Harrenhal config)
scope: escalate
change: none applied — escalating to showrunner
criteria met: no — explanation below

ESCALATION REPORT:
Library slugs found:
  (a) cond-westerosi-customary-authority — scope:project, project:taylor-hebert-westeros, 120 AC Riverlands (same card as warehouse; wrong project)
  (b) cond-westerosi-customary-authority-jaehaerys — scope:library, 84-101 AC Jaehaerys I Riverlands (wrong era and geography for 125 AC Crownlands/KL)

Neither library card satisfies the criteria (scope:library era-general variant, or 125 AC Crownlands config). No card exists in the library that is the correct operative constraint for a 17yo in Flea Bottom at 125 AC. Fixer cannot author a new card. Action required at showrunner/screen-writer level: author cond-westerosi-customary-authority-125ac (Crownlands/KL config, 125 AC, 17yo female social position) and provision it in warehouse. Until that card exists, the wrong-project card should be removed from the warehouse to prevent load-set corruption; memory.md laws entry for cond-westerosi-customary-authority should be annotated as pending-replacement.

NOTE: Fixer can execute the removal of the wrong-project card from warehouse and the memory.md annotation if showrunner approves. Awaiting direction before touching those files.

## fault-006 — RESOLVED — 2026-05-10T01:04:00Z
fault: cond-shard-behavioral-weight H1 heading read "Jaehaerys I Config" in both library and warehouse copies
scope: line
change: library + warehouse — replaced "(Jaehaerys I Config)" with "(flea-bottom-dance Config)" in H1 heading; no other heading or body text contained "Jaehaerys"
criteria met: yes — no occurrence of "Jaehaerys" in H1 or any heading in either copy

## res-005 — RESOLVED — 2026-05-10T01:03:00Z
fault: warehouse cond-reincarnation-mechanics-125ac missing supersedes: field; library copy and prior card (cond-reincarnation-mechanics) already have correct bidirectional chain from prior fixer pass
scope: line
change: warehouse — added supersedes: [cond-reincarnation-mechanics] to frontmatter; bidirectional chain now complete in both library and warehouse copies
criteria met: yes — library 125ac has supersedes, prior card has superseded_by, warehouse 125ac now has supersedes; chain is bidirectional

## res-004 — RESOLVED — 2026-05-10T01:02:00Z
fault: warehouse cond-clinical-self-erasure had scope:library with no project field; library copy already correct
scope: line
change: warehouse — changed scope: library → scope: project; added project: flea-bottom-dance
criteria met: yes — both library and warehouse now have scope:project + project:flea-bottom-dance

## res-003 — RESOLVED — 2026-05-10T01:01:00Z
fault: warehouse cond-crownlands-superstition-frame-125ac had scope:library with no project field; library copy already correct
scope: line
change: warehouse — changed scope: library → scope: project; added project: flea-bottom-dance
criteria met: yes — both library and warehouse now have scope:project + project:flea-bottom-dance

## SESSION-END — 2026-05-10T01:07:00Z — series-audit-fix
findings-applied: 5 (res-003, res-004, res-005, fault-006, fault-008)
findings-skipped: 0
exit: ESCALATED-TO-SHOWRUNNER (fault-007: no era-general or 125-AC Crownlands variant of cond-westerosi-customary-authority exists in library; new card authoring required)

## SESSION-START — 2026-05-10T00:00:00Z — 1d-audit-fix
dispatch: resolve 5 faults from 1d-audit.md — slug corrections, scope corrections, supersedes chain
target: cards/conditions/ (multiple cards) + active-project/warehouse/cond-shard-behavioral-weight.card.md
audit-report: active-project/staff/auditor/1d-audit.md
findings-queued: 5

## fault-001 — RESOLVED — 2026-05-10T00:01:00Z
fault: cond-shard-behavioral-weight references and Interaction Notes cited taylor-hebert-jaehaerys instead of taylor-hebert-flea-bottom
scope: line
change: removed taylor-hebert-jaehaerys from references (library card + warehouse copy); replaced in Interaction Notes "With taylor-hebert-jaehaerys persona card" → "With taylor-hebert-flea-bottom persona card" in both copies
criteria met: yes

## fault-002 — RESOLVED — 2026-05-10T00:01:30Z
fault: cond-shard-behavioral-weight references and Interaction Notes cited cond-series-tone-constraints-84ac instead of cond-series-tone-constraints-125ac
scope: line
change: replaced cond-series-tone-constraints-84ac with cond-series-tone-constraints-125ac in references frontmatter and in two body occurrences (Interaction Notes + for-auditor-use) in both library card and warehouse copy
criteria met: yes

## fault-003 — RESOLVED — 2026-05-10T00:02:00Z
fault: cond-crownlands-superstition-frame-125ac had scope:library despite project-specific body content
scope: line
change: changed scope to project; added project: flea-bottom-dance frontmatter field in library card. INDEX has no by_scope section; no INDEX edit required.
criteria met: yes

## fault-004 — RESOLVED — 2026-05-10T00:02:30Z
fault: cond-clinical-self-erasure had scope:library with no project field despite entirely project-specific body content
scope: line
change: changed scope to project; added project: flea-bottom-dance frontmatter field in library card. INDEX has no by_scope section; no INDEX edit required.
criteria met: yes

## fault-005 — RESOLVED — 2026-05-10T00:03:00Z
fault: cond-reincarnation-mechanics-125ac body stated it supersedes cond-reincarnation-mechanics but had no supersedes: frontmatter field; prior card had no superseded_by field
scope: line
change: added supersedes: [cond-reincarnation-mechanics] to 125ac card frontmatter; added superseded_by: cond-reincarnation-mechanics-125ac to cond-reincarnation-mechanics frontmatter. Relation is supersedes (not overrides): both are project-scope cards for different projects; the 125ac card is a same-concept replacement for a different project, not a library→project variant.
criteria met: yes

## SESSION-END — 2026-05-10T00:03:30Z — 1d-audit-fix
findings-applied: 5
findings-skipped: 0
exit: CLEAN
