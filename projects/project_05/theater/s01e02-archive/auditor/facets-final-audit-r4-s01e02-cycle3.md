---
audit: facets-final-r4-cycle3
episode: s01e02
date: 2026-05-11
mode: flag-only
status: FINDINGS-PRESENT
remediation-context: cycle-3 post-fix (four parallel re-dispatches — loc-state R1 re-author, fixer DELETE narrator:32 + state:8-stance-on-tya, memory R2 structural rebuild: mem:9 relocate + mem:12 delete + mem:13 add)
totals: 0 HARD + 5 SIGNAL findings across 4 facets (plus 5 carry-forward SIGNAL advisories unchanged)
note: filename disambiguates s01e02 cycle-3 from s01e01 r4 (active-project/staff/auditor/facets-final-audit-r4.md is s01e01's r4 audit — separate episode, same r-number; per-episode numbering collided)
---

# /and-facets s01e02 — Phase 5 mechanical audit r4 (post-cycle-3)

## Headline

**FINDINGS-PRESENT — HARD=0, SIGNAL=5 new + 5 carry-forward.** Phase 5b gate not blocked; HARD=0 holds.

## STRUCTURAL findings (0)

None.

## FREQUENCY-BAND findings (0 breaches)

Tens: 155 working-body entries; 7 threes / 155 = 4.5%; 2s ≈ 15.5%; 1s ≈ 80.0%. EXEMPT-UNDER-TONE-LAW (URI-034 Exemption 5) holds. Memory 6 entries; narrator 36; loc-state 13. All within their bands. See METADATA find-001 for the tens-footer count discrepancy.

## METADATA-INCONSISTENCY findings (1 — SIGNAL)

- **find-001 (SIGNAL)** — `tensometer.md` footer claims "Total entries: ~168" but the canonical per-episode body is 155 entries (cite-index `### tens (155 entries)`). The ~168 figure inflates by including F7-bone-rescue bones from season-window scope. Cosmetic. Recompute ratios against 155 (still within relaxed band) and update footer.

## CURVE-SHAPE verdict

- **Episode-level: SHAPE-OK.** Cycle-3 mutations are entry-level deltas in non-tensometer facets. r3 SHAPE-OK carries forward.
- Three named scenes carry peaks (Scene A @22, Scene H @125, Scene L @173). Additional r=3 beats at @85, @87, @106, @151.
- Adjacency: @18→@20→@22 (r=2→r=1→r=3) within tolerance (r3 A-001 resolved).
- No 30+-entry r=1 flatline stretches.

## CONTRADICTION findings (0)

None.

## DEDUP findings (1 — SIGNAL)

- **find-002 (SIGNAL) — URI-CONSOLIDATION-CITE-DRIFT** — proto-lines @145 and @173 carry `[state:8]` citations that now resolve to `proximity-to-taylor @22` (current state:8 after the cycle-3 delete renumbered the consolidated IDs). The citations were authored against the pre-delete numbering when state:8 referred to the stance-on-tya-category entry at @22. Renumbering on slice-consolidation shifted IDs without cascade-correcting proto-line tokens. Structurally inherent to the build_cite_index slice flow; pre-existing pipeline bug; not introduced by cycle-3 work. Classified SIGNAL per dispatch instruction. Surface to URI-CONSOLIDATION-CITE-DRIFT tracking.

## SUPERFLUOUS findings (0)

None.

## CONSTRAINT findings (2 — SIGNAL)

- **find-003 (SIGNAL) — memory without NI-spine, mem:9 @90** — after relocation from @87 to @90, mem:9 lacks an NI co-cite at @89, @90, or @91. Nearest NI entries are narrator:18 @88 and narrator:19 @100. Per CONSTRAINT class 8, memory without NI-spine is a violation. The relocation brief justified @90 on rubric grounds (trailing-edge quiet beat, "wrong kind of quiet" register) but did not address NI-spine. Resolution paths: (a) NI author adds an entry at @89 or @90; (b) memory-judge documents a rubric-exception defense (apparatus-silence IS the register; NI would be redundant with what the silence is).

- **find-004 (SIGNAL) — vibes:1/:2/:3 licensed-by stale pre-consolidation slice ID** — vibes entries @22 carry `licensed-by: state-update-oc-tanner-father:2` references. After cycle-3 DELETE of the stance-on-tya-category entry (oc-tanner-father slice entry-2), this reference no longer resolves. The vibes licensed-by format uses the per-character slice ID space; the deletion makes at least one reference unresolvable. Fixer path: remove the `state-update-oc-tanner-father:2` references from vibes:1, vibes:2, vibes:3 licensed-by; re-anchor to surviving slice entries (or remove the reference if no surviving entry supports the license).

## AP-SCAN findings (0 new)

Carry-forward A-002 (meta:1 @89 AP7 tens=1) advisory unchanged.

## TASTE-FLAG findings (0 new)

Carry-forward audience-gate callouts are Phase 5b decisions.

## PILE-UP REVIEW (6 pile-ups)

| Anchor | Co-located | Verdict |
|--------|-----------|---------|
| @173 | 10 (feel:1, narrator:31, sensory:5, state:4, state:8*, state:9*, vibes:18, :19, :22, :23) | warranted (r=3 Scene L rupture; effective 9 excluding cite-drift state:8) |
| @22 | 7 | warranted (r=3 Scene A rupture) |
| @20 | 5 | **find-005 (SIGNAL) — over-decoration borderline** at r=1 quiet beat after mem:13 add (4 → 5). Softened by mem:13 NI co-cite (narrator:5) presence; arc-linchpin role (customary-wage claim named). Editor advisory at wrap. |
| @107 | 5 | warranted (r=2 coin-exchange) |
| @125 | 5 | warranted (r=3 stylus-drop) |
| @159 | 5 | warranted (r=2 maester ambient→named) |

\* state:8/state:9 on @173 stale per find-002.

## Earth-Bet hard-fence (full substring scan)

**CLEAN.** Case-insensitive substring scan across all text fields of all 9 facets, cite-index, proto-lines against the proper-noun list. No violations. mem:13 target slug `cond-westerosi-customary-authority-125ac` has no Earth-Bet components.

## Audit summary

- Total entries reviewed: 281
- **HARD: 0**
- **SIGNAL: 5 new** (find-001 metadata, find-002 cite-drift, find-003 mem:9 NI-spine, find-004 vibes licensed-by stale, find-005 @20 pile-up borderline) **+ 5 carry-forward** advisory (F-002, M-001, M-002, A-002, S-002 unchanged)
- **CURVE-SHAPE:** SHAPE-OK
- **Tens-band:** EXEMPT-UNDER-TONE-LAW

## Routing

- find-001: cosmetic; studio/dramatist tensometer-footer update
- find-002: URI-CONSOLIDATION-CITE-DRIFT tracking (structural pipeline bug; no episode-scope fixer)
- find-003: memory-judge fork (rubric-exception defense) OR NI author (narrow-scope add)
- find-004: showrunner / fixer (remove stale `state-update-oc-tanner-father:2` from vibes:1/:2/:3 licensed-by)
- find-005: editor advisory at wrap

Phase 5b cycle 3 may fire: HARD=0 satisfied.
