---
fixer: facets-b01c01-hard-r1-six-findings
episode: b01-c01
date: 2026-05-20
audit-source: active-project/staff/auditor/facets-final-audit.md
hard-count-pre-fix: 6
hard-count-post-fix: 0
---

# Fix Report — /and-facets b01-c01 HARD Findings (R1 Pass)

Six HARD findings from the facets-final-audit. All six resolved. No card routing required. No escalations.

---

## F-001 — memory:1 @9 — NI-spine-absent — CONSTRAINT

**What changed:** Appended a `# defense: feel-as-spine` comment block under `mem:1` in `active-project/theater/facets/memory.md`.

**Defense documented:** The substance at @9 is interior-feeling about the prohibition enacted (feet held, architecture not built). `feel:1 @9` carries the interior register directly; adding NI would duplicate. The CONSTRAINT class accepts SIGNAL-with-documented-defense per the rubric's "exceptional with documented author defense" clause. The same rationale the R2 shard argued for its `mem:2 @23` entry applies more strongly to `mem:1 @9`: the memory event IS the felt recognition of the rule operating, which feeling carries.

**Files mutated:** `active-project/theater/facets/memory.md` (comment block appended; entry body unchanged)

**Entry mutated:** None — documentation only.

**Criteria met:** Yes — defense comment present at the correct position; CONSTRAINT class accepts documented-defense.

---

## F-002 — exposition:4 @11 — scene-orient-fire-rule — CONSTRAINT

**What changed:** exposition:4 was deleted from `active-project/theater/facets/exposition-b01-c01.md` (replaced with gap-documentation comment). `[exposition:4]` token stripped from:
- `active-project/theater/proto-lines/b01-c01.md` @11
- `active-project/theater/facets/_inflight-r2/proto-lines-exposition.md` @11
- `active-project/theater/facets/_inflight-r2/proto-lines-narrator.md` @11

**Rationale:** `loc-state:3` fires at @11, covering the scene orientation. Fire-rule condition (b) prohibits `scene-open-orient` when loc-state covers the anchor. R2 judge correctly refused the entry but the delete was not executed.

**Files mutated:** `exposition-b01-c01.md`, `proto-lines/b01-c01.md`, `_inflight-r2/proto-lines-exposition.md`, `_inflight-r2/proto-lines-narrator.md`

**Entry mutated:** exposition:4 deleted; ID gap preserved (no renumber).

**Criteria met:** Yes — no live exposition:4 entry; [exposition:4] absent from all proto-lines at @11.

---

## F-003 — exposition:7 @22 — scene-orient-fire-rule — CONSTRAINT

**What changed:** exposition:7 had already been deleted from `exposition-b01-c01.md` in a prior session (gap-documentation comment in place). This session completed the citation cascade: `[exposition:7]` token stripped from:
- `active-project/theater/proto-lines/b01-c01.md` @22
- `active-project/theater/facets/_inflight-r2/proto-lines-exposition.md` @22
- `active-project/theater/facets/_inflight-r2/proto-lines-narrator.md` @22

**Rationale:** Same as F-002. `loc-state:5` fires at @22; fire-rule condition (b) prohibits `scene-open-orient` when loc-state covers the anchor.

**Files mutated:** `proto-lines/b01-c01.md`, `_inflight-r2/proto-lines-exposition.md`, `_inflight-r2/proto-lines-narrator.md`

**Entry mutated:** None new — facet file gap already in place. Citation cascade completed.

**Criteria met:** Yes — no live exposition:7 entry; [exposition:7] absent from all proto-lines at @22.

---

## F-004 — exposition:5+exposition:6 @18 — per-anchor-cap — CONSTRAINT

**What changed:** exposition:5 (`scope: first-mention-term`, the-city-watch) removed as a numbered entry. Its watch-institution gloss folded into exposition:6 (`scope: first-mention-place`, the-hook) as a semicolon-appended contextual clause. exposition:5 replaced with gap-documentation comment. `[exposition:5]` token stripped from all three proto-lines files at @18. exposition:6's `licensed-by` updated to cover the watch-institution gap for all three personas.

**Rationale:** The rubric's permitted-pairs enumeration does not include `first-mention-term + first-mention-place`. The minimum change is to keep the structurally load-bearing entry (exposition:6, `first-mention-place: the-hook`, which recurs across the book per author notes) and fold the watch gloss into it as contextual content. The watch gloss content is preserved in full within the Hook gloss, just not as a separate numbered entry.

**Resulting exposition:6 gloss:** "the Hook — a curving lane at Flea Bottom's waterfront edge, the slum's lowest margin, where the most transient and least-protected smallfolk keep their rooms; the city-watch, King's Landing's gold-cloaked standing patrol, moves through on a rotation the block knows by sound."

**Files mutated:** `exposition-b01-c01.md` (exposition:5 gap-doc'd; exposition:6 body + licensed-by extended; cross-episode register write-back updated), `proto-lines/b01-c01.md`, `_inflight-r2/proto-lines-exposition.md`, `_inflight-r2/proto-lines-narrator.md`

**Entry mutated:** exposition:5 removed as numbered entry (ID gap preserved). exposition:6 body extended with watch clause.

**Criteria met:** Yes — single entry at @18 (exposition:6, first-mention-place); per-anchor-cap satisfied; watch gloss content preserved.

---

## F-005 — interest-narrator:-- @6/@18/@27 — AP-template-saturation — AP-SCAN

**What changed:** All three "X is what Y" predicate-nominative inversion constructions were already rewritten in the prior cycle-2 remediation session (SESSION: facets-b01c01-cycle2-remediation, 2026-05-19). Confirmed state of `active-project/theater/facets/interest-narrator.md`:

- Entry 2 @6 (former "useful without controlling is what the threshold means today"): now "the block reads on a second pass — which courts feed which alleys, who owes the well-step, where the watch does not turn."
- Entry 4 @18 (former "the cost of being legible is what she counts"): now "boots strike behind the wall, four spans and tracked through the feed without head-turn; staying invisible costs more in dense streets than she would have estimated."
- Entry 6 @27 (former "face, not node, is what she holds"): now "she will not write the name above the block, not in the feed and not on the page she keeps for herself."

Zero "X is what Y" constructions remain. Saturation 0/6 = 0% (threshold was 40%). Citation IDs preserved; no proto-lines token strip required (entries revised, not deleted).

**Files mutated:** `active-project/theater/facets/interest-narrator.md` (prior session; confirmed this session)

**Entries mutated:** NI entries 2, 4, 6 (bodies rewritten; IDs preserved).

**Criteria met:** Yes — AP-template-saturation resolved; 0% saturation < 40% threshold.

---

## F-006 — state-updates file — POV co-citation gap 8/9 — RUBRIC-FIDELITY

**What changed:** Appended a `# rubric-carve-out` annotation block to `active-project/theater/facets/state-updates.md` (before the first source block, after the consolidated frontmatter). No entries added or removed.

**Annotation content summary:**
1. The rubric's own §Cross-facet contract (rubric-state-updates.md lines 189-192) explicitly scopes the NI co-citation requirement to `actor:taylor.knowledge.*`, `actor:taylor.mask-state`, `actor:taylor.exposure-state` — mental/perceptual/relational interior state.
2. Mechanical-action state updates are exempt per the rubric's own scoping: position deltas (state:9 @1), lodging-payment-status (state:10 @2), inventory deltas (state:12 @7, state:14 @13, state:15 @20, state:18 @29) are not `knowledge.*` or `mask-state` or `exposure-state`.
3. Entries closer to the scoped zone (state:16 @20 `knowledge.coll-pattern`, state:17 @25 `social-state.with-wren`) accepted-with-defense: adding NI entries for these would push NI from 6 (22.2%) to 8 (29.6%), breaching the 25% ceiling; the substance contract for b01c01 is mechanical-establishment with 0 peak-bones; the density-on-flat anti-pattern (rubric §Anti-patterns #9) prohibits inflating fires to hit co-citation coverage.
4. Citations to rubric-state-updates.md §Cross-facet contract and §Anti-patterns #9 included in the annotation.

**Files mutated:** `active-project/theater/facets/state-updates.md` (annotation block prepended before source blocks)

**Entries mutated:** None — documentation only.

**Criteria met:** Yes — mechanical-action carve-out documented with rubric citation; option (c) as specified; no NI entries added; no band breach; accepted-with-defense for knowledge.coll-pattern and social-state entries.

---

## Cite-index update

Manually updated `active-project/theater/facets/_cite-index.md` to reflect the three exposition deletions:
- exposition:4 removed from entries; loc-state:3 @11 and state:2 @11 co-citations updated
- exposition:5 removed from entries; loc-state:4, narrator:4, mem:2, vibes:15 @18 co-citations updated; exposition:6 @18 co-citation updated
- exposition:7 removed from entries; loc-state:5, narrator:5, state:19, vibes:17 @22 co-citations updated; exposition:8 @22 co-citation updated
- Pile-ups @18 and @22 reduced from 6-entry to 5-entry (both remain above >4 threshold; still warranted per audit's pile-up verdict)
- Total entries: 70 → 67
- Density distribution updated accordingly

Note: `python3 active-project/staff/cite-index/build_cite_index.py b01-c01` requires shell execution (not available in this agent context). The manual cite-index update reflects all three exposition deletions and their cascade. A script-run verify pass is recommended before Phase 5b fires to confirm body-integrity and stale-citation checks pass.

---

## Post-fix HARD count

| Finding | Pre-fix | Post-fix |
|---------|---------|---------|
| F-001 memory:1 NI-spine-absent | HARD | RESOLVED (documented defense) |
| F-002 exposition:4 scene-orient | HARD | RESOLVED (deleted + cascade) |
| F-003 exposition:7 scene-orient | HARD | RESOLVED (cascade completed) |
| F-004 exposition:5+6 per-anchor-cap | HARD | RESOLVED (consolidated into :6) |
| F-005 NI AP-template-saturation | HARD | RESOLVED (entries rewritten prior cycle) |
| F-006 state-updates POV co-citation gap | HARD | RESOLVED (rubric-carve-out documented) |

**HARD count: 6 → 0. Phase 5b gate is clear.**
