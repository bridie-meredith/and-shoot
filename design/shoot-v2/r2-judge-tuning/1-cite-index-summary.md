---
phase: B1 — cite-index inspection (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
inputs: active-project/theater/facets/_cite-index.md (post-R2 state at commit 0996013 + downstream housekeeping)
status: AUTHORED — cite-index counts captured at-rest; pre-R2 baseline diff blocked (see 1-baseline-reconstruction.md)
---

# Phase B1 — Cite-Index Summary

## Purpose

Plan B B1 step 1: read the cite-index at-rest and produce a one-page per-facet summary of R2 mutations + citation deltas + lonely-entry deltas. Pairs with `1-baseline-reconstruction.md` for the pre-revision-baseline read.

## At-rest cite-index totals (post-R2 / post-Phase-5 audit-driven housekeeping)

Source: `active-project/theater/facets/_cite-index.md` as of 2026-05-10.

| Metric | Count |
|---|---|
| Total facet entries | 205 |
| Decorated protolines | 38 / 102 (37.3%) |
| Bare protolines (0 citations) | 64 |
| Pile-ups (>4 citations / protoline) | 7 (one each at counts 5, 5, 5, 6, 7, 10, 16) |
| Lonely entries (no co-cite at anchor) | 8 (per cite-index lonely section; provenance noted in `_cite-index.md` header) |

## Per-facet entry counts (current at-rest)

| Facet | File | Lines | Approximate entry count |
|---|---|---|---|
| tens (tensometer) | `tensometer.md` | 115 | 102 |
| sensory | `sensory.md` | 13 | (per `_cite-index.md` per-facet section) |
| state-updates | `state-updates.md` | 33 | as cite-indexed |
| location-state | `location-state.md` | 14 | as cite-indexed |
| narrator-interest | `interest-narrator.md` | 38 | 24 (per 0996013 commit message: 19K / 2D / 5A → 24) |
| memory | `memory.md` | 18 | 8 (per 0996013: 4K / 0D / 4A → 8) |
| feeling | `feeling.md` | 42 | 12 (per 0996013: 11K / 1D / 2A → 12, Taylor 5 / mother 4 / father 3) |
| metaphor | `metaphor.md` | 12 | 1 (per 0996013: 1K / 0D / 0A → 1; 6 candidates considered, all cut) |
| vibes | `vibes.md` | 60 | as cite-indexed |

(Exact entry counts per facet are recoverable from `_cite-index.md` per-facet sections; the table above pairs file-line counts with the 0996013 commit message's R2-decision summary for the four midband facets.)

## R2-touched midband facets — entry-level scope

Per the R2 commit (`0996013` "Round 2 complete: s01e01 faceted-r2"):

- **narrator-interest:** R1 21 → R2 24. 19K / 2D / 5A. Two deletes opened narrator slots; five adds cleared ≤5 cap exactly.
- **memory:** R1 4 → R2 8. 4K / 0D / 4A. No deletes; doubled the entry count.
- **feeling:** R1 11 → R2 12. 11K / 1D / 2A. Taylor 5 (was 4); mother 4 (was 4); father 3 (was 3). Single delete; two adds.
- **metaphor:** R1 1 → R2 1. 1K / 0D / 0A. Six candidates considered; all refused. Refuse-by-default discipline visible in this number.

**R2-touched-entry total (across all four midband facets):** 35 KEEP / 3 DELETE / 11 ADD. Net +8 entries (37 → 45). Adds dominate the mutation surface — F-R2-2 (multi-justification under-strictness on adds) and F-R2-3 (lonely-entry adjacent-context) are the load-bearing failure modes for the corpus.

## Citation accrual

Per `0996013`: 38 → 39 protolines decorated; 5 cascade strips + 8 add-writes; net +3 citations. The cascade-strip count (5) traces to the 3 R2 deletes on narrator-interest + feeling, with associated cite-cascades.

## Lonely-entry surface

Per `0996013`: 11 → 8. Four R1 lonelies resolved by R2.1 (NI) adds providing co-cite; one cascade orphan surfaced at `tens:21 @25` from `narrator:8` deletion; two new R2 adds at bone-only protolines (`feel:13 @129`, `feel:14 @36`) — these two are the structural F-R2-3 candidates. Adds at bare protolines have no co-cite by construction; they are the test for the at-rest discipline.

## Pile-ups

Pile-ups unchanged through R2 (7 at-rest, 7 post-R2). R2 did not concentrate citations; the mutation surface is at the lonely / bare end, not the pile-up end. This is consistent with R2's job of filling the graph rather than thickening already-thick anchors.

## Bare protolines

64 → 63. R2 added 8 citations across 1 protoline net (the 7 strip-cascades returned existing protolines to bare; the new co-cites cleared one). Bare-protoline reduction is small.

## Implications for B2b-baseline

The 11 R2-add entries are the F-R2-2/3 test surface. The 3 R2-delete entries are F-R2-1 test surface (each delete may have replaced an entry with a revision or cleared without replacement; the commit summary doesn't disambiguate). The 35 R2-keep entries are not in scope for failure-mode counting — they are the mass that did not change.

The cite-index does not by itself reveal F-R2-1 instances (form-drift on revisions). That requires reading the entry pre and post revision, which is what Plan B B2b-baseline asks for and what `1-baseline-reconstruction.md` documents as blocked at this revision of the repo.

## What this summary cannot answer without a baseline

- Which existing entries were revised (versus kept-with-no-edit) at R2.
- The text of any pre-R2 entry that was deleted or revised.
- The pre-R2 state of `_cite-index.md` for diff against the current state.

These are the data that `1-baseline-reconstruction.md` would carry. See that file for the recovery plan.
