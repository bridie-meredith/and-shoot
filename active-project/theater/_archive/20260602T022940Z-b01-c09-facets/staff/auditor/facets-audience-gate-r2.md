# /and-facets b01c08 Phase 5b — audience-gate aggregation (final cycle 2)

date: 2026-05-31
aggregation_rule: URI-AUDIENCE-AGGREGATION-RULE (3-of-3 strict; single dissent fails the facet)
precondition: Phase 5 audit cycle 3 CLEAN (HARD=0; all consolidation-renumbering faults resolved cycle 1→2)
cycles: 2
final_status: ALL-FACETS-ACCEPT

reviewers:
  active_audience: cape-fic-reader, dark-fantasy-reader, worm-canon-pedant
  sensory_specialists: sensory-disambiguation-pedant, sensory-modality-coverage, sensory-old-state-reader

---

## Per-facet final-cycle verdicts (cycle 2 where re-fired; cycle 1 otherwise)

| Facet | cape-fic | dark-fantasy | worm-canon | specialist trio | aggregate | cycle |
|-------|----------|--------------|------------|-----------------|-----------|-------|
| location-state | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |
| interest-narrator | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 2 |
| sensory | — | — | — | ACCEPT/ACCEPT/ACCEPT | ACCEPT 3/3 | 2 |
| state-updates | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |
| memory | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |
| feeling | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 2 |
| metaphor | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |
| vibes | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 2 |
| exposition | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |
| dialogue (oswyn) | ACCEPT | ACCEPT | ACCEPT | — | ACCEPT 3/3 | 1 |

**All 10 facets: ACCEPT 3/3 strict aggregate.**

---

## Cycle 1 → Cycle 2 remediation summary

4 facets failed cycle 1 strict 3/3 ACCEPT (each by single-persona dissent); cycle-2 fixer pass remediated all 4 to 3/3 ACCEPT.

### NI — cape-fic REVISE → ACCEPT
- **Findings**: AP-009 chassis cap violated (NI:2@8 + NI:6@24 both inverted-predicate); mask-too-perfect missing foreknowledge-clamp at NI:3@13; apparatus-register carry from c07.
- **Fix**: NI:3@13 final clause reformed to add foreknowledge-clamp register ("interior noting the weight and filing it flat"); NI:6@24 third clause reformed from generalizing rule-statement to specific perceptual registration ("water-point approach holding its feed-weight unchanged under the new cover"). INVIOLABLE core text preserved verbatim. AP-009 cap now ≤1 (NI:2@8 sole remaining inverted-predicate).
- **Cycle 2 verdicts**: cape-fic ACCEPT (cap resolved + clamp visible); dark-fantasy ACCEPT (foreknowledge register stronger via mechanism vs. result; Khepri-echo discipline preserved); worm-canon ACCEPT (Earth-Bet fence clean + reader-side recognition preserved).

### sensory — old-state-reader REVISE → ACCEPT
- **Finding**: sensory:1 @10 old-state "feed-station-working-quiet" had no anchor in locked graph; loc-state:4 @9 silent on sound baseline; SEAM-010 carve-out resolved negatively now that loc-state was authored (HARD UNANCHORED-OLD-STATE).
- **Fix**: loc-state:4 @9 updated to add `sensory: enclosed-receipt-quiet`; sensory:1 old-state retied to verbatim match. SEAM-010 carve-out retired.
- **Cycle 2 verdicts**: all 3 specialists ACCEPT.

### vibes — worm-canon REVISE → ACCEPT
- **Finding**: vibes:5 keyword `rising-entrapment` (hyphenated, rubric-correct) vs `active-project/actors/aemond-targaryen-122ac/vibes.md` `rising entrapment` (spaced). String-lookup `++` op-coherence gate failed to resolve.
- **Fix**: Actor vibes file edited to hyphenate keyword.
- **Cycle 2 verdicts**: all 3 active audience ACCEPT (cape-fic + dark-fantasy carried; worm-canon REVISE → ACCEPT).

### feeling — dark-fantasy REVISE → ACCEPT
- **Findings**: feel:2@8 (Phase 2.5 INVIOLABLE) NI:2-redundant; feel:3@13 (Phase 2.5 INVIOLABLE) form-fail negation-as-body-tell + NI:3-redundant.
- **Fix**: feel:2@8 reformed "her breath holds at the circuit-close" → "her step lands at the circuit-close" (proprioceptive register distinct from NI:2's cognitive-accounting); feel:3@13 reformed "her hand does not pause at the name" → "her hand sets on the next entry" (positive body-act enacting discipline as physical progression; NI:3's reformed "filing it flat" complementary not redundant).
- **Cycle 2 verdicts**: cape-fic ACCEPT (cycle-1 ACCEPT preserved + revisions strengthened); dark-fantasy ACCEPT (both Q1-redundancy and form-fail resolved); worm-canon ACCEPT (Earth-Bet + KL-122ac somatic register preserved).

---

## Convergence trace (PROP-0011)

- **Auditor findings (final-cycle Phase 5 cycle 3)**: 0 HARD / 5 SIGNAL
- **Audience callouts (across all reviewers, cycle 1 — deduped)**: 4 single-persona REVISEs across 4 facets (NI / sensory / vibes / feeling); audience-side specialist HARD at sensory:1 unanchored-old-state
- **Shared findings**: NONE (auditor consolidation-renumbering HARDs ≠ audience taste/form/anchor REVISEs)
- **Audience-only findings**: AP-009 chassis cap (NI cape-fic); vibes:5 keyword serialization (worm-canon); sensory:1 unanchored-old-state (specialist, HARD); feel:2/3 form-fail + NI-redundancy (dark-fantasy)
- **Auditor-only findings**: 5 consolidation citation HARDs cycle 1 (all closed cycle 2)
- **Bidirectional loop verdict**: `one-sided` — both paths fired with substantive findings but no overlap. Auditor caught mechanical consolidation/ID issues; audience caught form/anchor/redundancy issues. Healthy in the sense that each path closed its own findings; one-sided in the sense that no finding was independently caught by both.

---

## Cap-refusals (across all reviewers, all cycles)

- NI cycle-1 cap-refusals: 8 (@23, @20, @12, @7, @10, @14, @3, @5)
- Memory cycle-1 cap-refusals: 10
- Feeling-taylor cycle-1 cap-refusals: 5 (s03 cap unused-by-design)
- Feeling-oswyn cycle-1 cap-refusal: 1 (@18)
- Metaphor cycle-1: ACCEPT-REFUSE confirmed (zero entries by discipline)
- Total cap-refusals: 24 across roughly 240 candidate seams (~10% — within budget)

## Process gaps captured

1. **Slice-consolidation citation drift (PROP candidate)**: `build_cite_index.py` renumbers slice IDs (feeling, state-updates) on consolidation but does not cascade renumbering into proto-line citation tokens. R1 authors write `[<prefix>:<local-id>]` from their slice; after consolidation those tokens silently point at wrong consolidated entries. Stale-cite check verifies ID resolution, not semantic correctness. Pattern recurs whenever a slice has content out-of-order or behind another slice in the consolidation walk. Audited cycle 1 caught 5 HARDs in this class; fixer cycle 1.5 remediated via inflight + canonical proto-lines edits.

2. **cite_index_hash provenance**: R2 shards across 6 judges carry mixed token forms (some computed SHA256, some structured-marker placeholders). The authoritative SHA256 was computed by the exposition R2 judge; other shards' tokens are stylistic markers. Cross-session staleness check at Phase 6 persist works against the computed hash. SIGNAL not HARD.

3. **R1 author inflight emit non-standardization**: 4 R1 authors (feel-taylor, feel-oswyn, meta, exposition) emitted non-canonical inflight files (delta-style content instead of byte-identical bones-copy + citation tokens). Mechanical rebuild required at Phase 2 merge. PROP candidate: standardize R1 inflight emit contract more explicitly.

4. **Verdict file path drift**: 2 cycle-2 verdicts (NI worm-canon, feeling worm-canon) wrote to `active-project/audience/` instead of canonical `active-project/staff/audience/`. Manual normalization required at Phase 6.

5. **Phase 5b worm-canon-pedant verdict mtime drift**: NI worm-canon cycle-2 verdict wrote to non-canonical path; corrected pre-persist.

## Audit trail

- Phase 5 cycle 1: 5 HARD / 5 SIGNAL → cycle 2 fixer → Phase 5 cycle 2: 0 HARD / 6 SIGNAL → cycle 3: 0 HARD / 5 SIGNAL
- Phase 5b cycle 1: 6 ACCEPT facets / 4 REVISE facets → cycle 2 fixer → Phase 5b cycle 2: ALL 4 ACCEPT 3/3 → ALL 10 facets ACCEPT 3/3
- Audience cycles used: 2 / 3 (cap not burned)
