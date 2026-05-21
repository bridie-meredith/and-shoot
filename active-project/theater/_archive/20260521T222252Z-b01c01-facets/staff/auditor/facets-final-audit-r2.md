---
audit: facets-final-r2
episode: b01-c01
date: 2026-05-20
mode: flag-only
status: FINDINGS-PRESENT
totals: 1 HARD / 0 new SIGNAL
prior-audit: active-project/staff/auditor/facets-final-audit.md
fixer-report: active-project/staff/fixer/and-facets-r1-fixes.md
---

# Re-Audit Scope

Focused re-audit. Verifies the 6 HARD findings from facets-final-audit.md (r1) are resolved. Quick structural/constraint sweep on modified files only. Signal findings from r1 carry forward without re-enumeration.

---

## F-001 through F-006 Verdicts

### F-001 — memory:1 @9 — NI-spine-absent — RESOLVED

`# defense: feel-as-spine` annotation block is present in `active-project/theater/facets/memory.md` at lines 7-15, immediately below the `1 @9` entry. The block documents:
- rubric clause invoked: "exceptional with documented author defense"
- rationale: the memory event IS the felt recognition of the rule operating; feel:1 @9 carries the interior register; NI addition would duplicate
- co-citations confirmed: [feel:1, vibes:12]

The defense annotation is present at the correct position and parses cleanly without disrupting the entry body. No cross-facet contract pathology introduced.

**Verdict: RESOLVED**

---

### F-002 — exposition:4 @11 — scene-orient-fire-rule — RESOLVED

Gap-documentation comment is present at line 21 of `active-project/theater/facets/exposition-b01-c01.md`. The comment records the deletion reason (F-002, date, condition-b violation) and preserves the ID gap.

Proto-line @11 (`11 taylor-hebert-kl-122ac lifts the basket`) in `active-project/theater/proto-lines/b01-c01.md` carries `[loc-state:3] [state:2]`. Token `[exposition:4]` is absent.

Cite-index exposition section lists 5 entries (1, 2, 3, 6, 8). exposition:4 is not present.

**Verdict: RESOLVED**

---

### F-003 — exposition:7 @22 — scene-orient-fire-rule — RESOLVED

Gap-documentation comment is present at line 27 of `active-project/theater/facets/exposition-b01-c01.md`. The comment records the deletion reason and ID gap.

Proto-line @22 (`22 wren-stitch-maker-flea-bottom-ward enters the street`) carries `[exposition:8] [loc-state:5] [narrator:5] [state:19] [vibes:17]`. Token `[exposition:7]` is absent.

Cite-index exposition section does not list exposition:7.

**Verdict: RESOLVED**

---

### F-004 — exposition:5+exposition:6 @18 — per-anchor-cap — RESOLVED

Gap-documentation comment for exposition:5 is present at line 23 of `active-project/theater/facets/exposition-b01-c01.md`. exposition:6 body (line 25) is extended with the watch-institution clause as a semicolon-appended contextual phrase. The extended body reads: "the Hook — a curving lane at Flea Bottom's waterfront edge, the slum's lowest margin, where the most transient and least-protected smallfolk keep their rooms; the city-watch, King's Landing's gold-cloaked standing patrol, moves through on a rotation the block knows by sound."

exposition:6 `licensed-by` covers all three active audience personas. The cross-episode register write-back at the bottom of the file records `the-city-watch | first-mention-anchor: @18 | gloss-id: 6 (folded into Hook gloss; F-004 consolidation)`.

Proto-line @18 (`18 the city-watch passes the hook`) carries `[exposition:6] [loc-state:4] [mem:2] [narrator:4] [vibes:15]`. Token `[exposition:5]` is absent. Single exposition entry at @18; per-anchor-cap satisfied.

**Verdict: RESOLVED**

---

### F-005 — interest-narrator AP-template-saturation — RESOLVED

All 6 entries of `active-project/theater/facets/interest-narrator.md` verified. Scanning for "X is what Y" predicate-nominative inversion construction:

- Entry 1 @4: "the network has him before he has her." — no hit
- Entry 2 @6: "the block reads on a second pass — which courts feed which alleys, who owes the well-step, where the watch does not turn." — no hit
- Entry 3 @15: "every body within the block is legible and she touches none of them; passive holds, day-long, a continuous suppression cost." — no hit
- Entry 4 @18: "boots strike behind the wall, four spans and tracked through the feed without head-turn; staying invisible costs more in dense streets than she would have estimated." — no hit
- Entry 5 @22: "a girl comes in through the swarm before she comes in through the door; the entry is filed without a name above the line." — no hit
- Entry 6 @27: "she will not write the name above the block, not in the feed and not on the page she keeps for herself." — no hit

Saturation: 0/6 = 0%. Threshold is ≥40%. Threshold not reached.

Secondary check on rewritten entries 2, 4, 6: no new AP patterns introduced. Bodies are syntactically distinct constructions; no emerging repetition pattern detected.

**Verdict: RESOLVED**

---

### F-006 — state-updates file — POV co-citation gap — UNRESOLVED

**What was required:** A `# rubric-carve-out` annotation block documenting the mechanical-action carve-out with rubric citation (rubric-state-updates.md §Cross-facet contract scope + §Anti-patterns #9), placed between the consolidated frontmatter close and the first source block in `active-project/theater/facets/state-updates.md`.

**What the file contains:** The consolidated frontmatter closes at line 5 (`---`). Line 7 opens `# source: env` immediately, with no intervening annotation block. The `# rubric-carve-out` heading does not appear anywhere in the file. The pre-existing `# POV co-citation expectation (R2 will resolve):` comment block in the taylor-hebert-kl-122ac source slice (lines 73-75) remains from the R1 author and does not constitute the required defense annotation — it is a forward-looking note to R2, not a post-R2 resolution record with rubric citations.

**Why this matters:** The RUBRIC-FIDELITY HARD finding (r1) required documented evidence that the co-citation gap on 8 of 9 taylor-state entries is justified by rubric-scoped exemption and anti-pattern defense. Without the annotation, the gap has no on-file defense. The fixer report claims the fix was executed but the mutation did not reach the file.

**id:** fault-001
**type:** fault
**what:** `active-project/theater/facets/state-updates.md` — `# rubric-carve-out` annotation block absent; file goes directly from consolidated frontmatter close to `# source: env` with no intervening documentation
**why:** The RUBRIC-FIDELITY HARD finding (F-006, r1) required a documented rubric-scoped carve-out covering mechanical-action entries and the density-on-flat anti-pattern defense for knowledge.coll-pattern and social-state.with-wren entries; without this record the 8/9 co-citation gap is undefended on-file; downstream auditors and Phase 5b gate cannot verify the RUBRIC-FIDELITY criteria are met
**criteria:** Insert `# rubric-carve-out` annotation block in state-updates.md between the consolidated frontmatter close (`---` at line 5) and `# source: env` (line 7); block must: (a) cite rubric-state-updates.md §Cross-facet contract scoping clause (knowledge.*, mask-state, exposure-state only); (b) classify each of the 8 uncovered taylor-state entries by exempt category (mechanical-action, inventory, position, lodging) or accepted-with-defense (knowledge.coll-pattern @20, social-state.with-wren @25); (c) cite rubric-state-updates.md §Anti-patterns #9 (density-on-flat) as the reason NI entries were not added for the accepted-with-defense entries; (d) state explicitly that the carve-out resolves F-006 from the r1 audit

**Verdict: UNRESOLVED**

---

## New Findings Introduced by Fixer Changes

None. The fixer's four file-mutating operations (memory.md annotation, exposition-b01-c01.md deletions and body extension, interest-narrator.md rewrites, proto-lines token strips) do not introduce new constraint, AP-scan, frequency-band, or structural findings. Verified:

- exposition:6 body extension does not create a new per-anchor-cap issue (single entry at @18)
- exposition:6 licensed-by covers all three audience personas; no orphaned license
- Remaining exposition entries (1, 2, 3, 6, 8) have valid sources; ID gaps at 4, 5, 7 are documented; monotonicity is preserved (gaps are intentional, not renumber failures)
- interest-narrator rewritten entries introduce no new repetition pattern; entry count is unchanged at 6; band position unchanged (6/27 = 22.2%, within 15-25% ceiling)
- cite-index totals updated correctly: 67 entries (down from 70); pile-up counts at @18 and @22 reduced from 6 to 5; both remain above the >4 threshold; warranted verdicts from r1 still hold

---

## Signal Findings from Prior Audit — Carry Forward

All 15 SIGNAL findings (S-001 through S-015) from `active-project/staff/auditor/facets-final-audit.md` carry forward unchanged. The fixer's scope did not touch any of the signal-generating surfaces (slug headers, shard records, vibes dual-anchor citations, sensory/feeling frequency-band positions, metadata fence formats, CURVE-SHAPE label, TASTE-FLAG entries, AP registration-vocabulary advisory).

No regression introduced by fixer changes in signal territory.

---

## Audit Summary

**HARD findings:**
- F-001: RESOLVED
- F-002: RESOLVED
- F-003: RESOLVED
- F-004: RESOLVED
- F-005: RESOLVED
- F-006: UNRESOLVED → fault-001 (state-updates rubric-carve-out annotation absent)

**New HARD findings from fixer changes:** 0

**Total HARD count post-fix: 1**

**SIGNAL findings:** 15 (carry-forward from r1; no new signals)

---

## Phase 5b Gate

**HARD = 1. Phase 5b: BLOCK.**

Fixer must insert the `# rubric-carve-out` annotation block in `active-project/theater/facets/state-updates.md` per the criteria in fault-001 above. Re-audit of F-006 only is sufficient; all other HARD findings are resolved.
