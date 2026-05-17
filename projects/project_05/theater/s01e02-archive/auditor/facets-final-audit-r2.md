---
audit: facets-final-r2
episode: s01e02
date: 2026-05-11
mode: flag-only
status: CLEAN
remediation-context: r1 HARD S-001/C-001 resolved via DELETE (fixer pass 1 of 1 budget)
totals: 0 HARD + 7 SIGNAL
---

# Re-audit summary

## HARD-RESOLVED verification

- **metaphor.md contains only meta:1 (no meta:2).** File body: one entry only — `1 @89 simile: the flies are an ear pressed to a wall | licensed-by: feel:7 +tens:1`. meta:2 entry is absent. CONFIRMED.
- **Canonical proto-line @114 has no [meta:2] citation.** Line reads bare: `114 taylor-hebert-flea-bottom writes the entry` with no inline facet citations. @114 also appears in the cite-index's "Bare protolines" list, confirming zero citations attach to it. CONFIRMED.
- **Cite-index `### meta` section lists 1 entry.** Header: `### meta (1 entries)`. Single entry: `meta:1 @89 back=Y co=[vibes:12, vibes:13] lic-out=[feel:7, tens:1]`. CONFIRMED.
- **No surviving reference to mem:5 anywhere in the graph.** The `### mem` section carries IDs 2, 3, 4, 7, 9, 10, 11, 12 — mem:5 absent. No occurrence of `mem:5` found in metaphor.md, vibes.md, interest-narrator.md, feeling.md, memory.md, or the cite-index. CONFIRMED.

## New-HARD scan

None introduced.

- **Anchor-resolution sweep (meta:2 as anchor in downstream entries).** No entry in vibes.md, interest-narrator.md, feeling.md, or memory.md carries a `licensed-by:` or co-cite reference to `meta:2`. The deletion left no orphaned downstream references.
- **Bidirectional citation integrity.** The cite-index `### meta` section contains only meta:1. No `lic-in`, `co=`, or `lic-out` field in any cite-index entry references meta:2. No stale back-reference exists anywhere in the graph.
- **Cite-index entry-count consistency.** r1 total was 285 facet entries (155 tens + 12 loc-state + 37 NI + 5 sensory + 34 state + 8 memory + 9 feeling + 2 metaphor + 23 vibes). Post-deletion: 285 − 1 = 284. Cite-index header declares `totals: 284 facet entries`. Count is consistent with exactly one deletion and no other structural change.

## SIGNAL inheritance from r1

The following 7 SIGNAL findings are carried forward unchanged from r1. They are advisory and do not block Phase 5b.

- **S-002** — state-updates consolidated file has duplicate source-header lines (cosmetic merge artifact; routed to studio build process)
- **F-002** — feeling aggregate sparsity 5.8% marginally above 5% ceiling; per-character rates all clean; rubric scope ambiguous (routed to feeling authors + editor; track against s01e03)
- **M-001** — NI shard frontmatter mis-uses f-r2-counts as K/A verdict counts; consolidator already corrected; source shard preserved for traceability
- **M-002** — oc-tanner-elder feeling shard classifies a REVISE verdict as F-R2-3; consolidated total (1) below SIGNAL threshold; taxonomy note for future shards
- **A-001** — tens approach @83-@84 lacks r=2 ramp before @85 latch-break peak; 1→3 adjacency gap; routed to dramatist for axis-citation review
- **A-002** — metaphor:1 @89 fires at tens=1; AP7 default-refuse discipline; R2 judge defense documented; Phase 5b audience-gate candidate
- **T-001** — eviction approach @83-@84 momentum-stall candidate; atmosphere-thin under contemplative-procedural-horror register; overlaps A-001; routed to Phase 5b audience

## Verdict

CLEAN HARD=0 — ready for Phase 5b.
