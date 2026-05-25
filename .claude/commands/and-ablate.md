---
description: Facet-ablation study for a stitched chapter. Generates 12 prose variants (bones-only + full + 10 leave-one-out facets) via the renderer-minimal agent, then a single ranked-comparison cold-read returns the ranking + per-variant differential notes. Produces evidence for admin process-critic (low-ranked facets become delete/modify proposals). On-demand only. Usage - /and-ablate <book>-<chapter>
---

# /and-ablate

Facet-ablation study. **Does each facet earn its keep?** The chain assumes yes; this command tests that assumption.

For a stitched chapter, render the same bones 12 different ways (bones only; bones + all facets; bones + 9 facets with one held out, ten times). Show all 12 to one cold reader. The cold reader ranks them and articulates the differentials. Bottom-ranked variants identify facets that aren't pulling their weight.

**On-demand only.** No auto-fire. New evidence source for admin process-critic — recurring low-rank facets become `change_type: delete` or `change_type: modify` proposals against the facet rubric.

**Read-only against the chain.** Does not modify bones, facets, dialogue, draft, or render-log.

---

## Phase 0 — Validate

1. Parse `<book>-<chapter>` arg. Bad shape → print usage and exit.
2. Read showrunner memory. Require `chapters[<slug>].stitched == true`. If not stitched, abort: ablation only meaningful against a chapter that has cleared the cold-read terminal gate.
3. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching `/and-ablate` + this scope: HARD → abort unless this run resolves; SOFT → carry to the Phase 4 report.
4. Locate inputs:
   - `bones_path` = `active-project/theater/bones/<book>-<chapter>.md` (required)
   - **Facet bundles** (per-facet, may be a single file or a per-character set):
     - `scene-map` = `active-project/theater/facets/scene-map-<book>-<chapter>.md`
     - `state-updates` = `active-project/theater/facets/state-updates-*.md` (per-character bundle, treated as one facet; falls back to `state-updates.md` if no per-character files exist)
     - `location-state` = `active-project/theater/facets/location-state-<book>-<chapter>.md`
     - `sensory` = `active-project/theater/facets/sensory-<book>-<chapter>.md`
     - `feeling` = `active-project/theater/facets/feeling-*.md` (per-character bundle, treated as one facet; falls back to `feeling.md`)
     - `memory` = `active-project/theater/facets/memory-<book>-<chapter>.md`
     - `vibes` = `active-project/theater/facets/vibes-<book>-<chapter>.md`
     - `metaphor` = `active-project/theater/facets/metaphor-<book>-<chapter>.md`
     - `exposition` = `active-project/theater/facets/exposition-<book>-<chapter>.md`
     - `interest-narrator` = `active-project/theater/facets/interest-narrator-<book>-<chapter>.md`
   - **Dialogue bundle**: all `active-project/theater/dialogue/*.md` (one file per speaker; chapter scope is implicit per active-project). Dialogue is always bundled with `full`.
   - Missing flat-named facets are non-fatal but warn: a chapter genuinely without a facet (e.g. a chapter with no dialogue speakers, no memory beats) is valid; the absent facet's leave-one-out variant becomes equivalent to `full`.
5. Build `staff/ablation/<book>-<chapter>-<timestamp>/` working directory.

---

## Phase 1 — Assemble variant manifest

The standard ablation set is **12 variants**:

| # | label | facet set |
|---|---|---|
| 01 | `bones-only` | none |
| 02 | `full` | all ten facets + dialogue |
| 03 | `leave-out-scene-map` | all except scene-map |
| 04 | `leave-out-state-updates` | all except state-updates |
| 05 | `leave-out-location-state` | all except location-state |
| 06 | `leave-out-sensory` | all except sensory |
| 07 | `leave-out-feeling` | all except feeling |
| 08 | `leave-out-memory` | all except memory |
| 09 | `leave-out-vibes` | all except vibes |
| 10 | `leave-out-metaphor` | all except metaphor |
| 11 | `leave-out-exposition` | all except exposition |
| 12 | `leave-out-interest-narrator` | all except interest-narrator |

**Dialogue is bundled with the `full` set and is never the held-out facet.** Dialogue is verbatim content — leaving it out produces a chapter with mute characters, which is a useful negative-control variant but not a comparable ablation (you're testing facet contribution, not character-presence). If you want a dialogue ablation specifically, run `/and-ablate <chapter> --include-dialogue-ablation` as a 13th variant (not standard).

Write the manifest to `<work-dir>/manifest.md` with rows `{variant_num, label, facet_paths[]}`.

---

## Phase 2 — Render variants (12 parallel dispatches)

Fan out 12 `renderer-minimal` dispatches in parallel. Each carries:
- `subagent_type: renderer-minimal`
- `bones_path`
- `facet_paths` per the manifest
- `output_path: <work-dir>/variant-<NN>-<label>.md`
- `variant_label`

Wait for all 12 to return. Validate: every output file exists, every output has the required frontmatter, every output has non-trivial prose body (≥ bones_count sentences as a sanity floor). Re-dispatch any failed variant once; second failure → abort with the failed variant list.

---

## Phase 3 — Ranked cold-read

Single `general-purpose` dispatch. The cold reader is **uninformed** about the chain — no bones, no facets, no contract. They receive only the 12 prose files and a prompt.

Prompt structure (rendered into the dispatch):

```
You are a careful reader doing a comparison study.

You will read 12 versions of the same chapter. They differ only in their
materials of origin — same events, same characters, same scenes, but
rendered with different supporting material. You do not know what was
varied.

Tasks:
1. Read all 12 versions.
2. Rank them 1 (best) to 12 (worst). "Best" = most coherent, vivid,
   continues-reading-yes, satisfying as a chapter on its own terms.
3. For each rank position, write one sentence explaining what that
   variant did or didn't do that placed it there.
4. Note any clusters: variants that read similarly (and what they shared).
5. Note any outliers: variants that were strikingly worse or better, and
   in what dimension (event clarity, atmosphere, character interiority,
   sensory grounding, voice).
6. One closing paragraph: across these 12 variants, what dimension of
   prose mattered most to your read?

Do not invent meta-knowledge ("variant 7 was missing sensory because…").
You don't know what was varied. Describe what you experienced.
```

Variants are passed in a randomized order so the cold reader cannot infer the manifest from position. Record the position-to-variant mapping in the work-dir for de-anonymization at Phase 4.

---

## Phase 4 — Persist report

Write `active-project/staff/reviews/ablation-<book>-<chapter>-<timestamp>.md`. Structure:

```markdown
# Ablation study — <book>-<chapter>

## Manifest
| # | label | facets included | facet held out | rendered prose path |

## Cold-reader ranking (de-anonymized)
| rank | variant # | label | one-line differential |

## Cluster notes
<cold-reader's cluster observations, with variants named>

## Outlier notes
<cold-reader's outlier observations, with variants named>

## Closing observation
<the cold reader's "what mattered most" paragraph>

## Differential attribution
For each leave-one-out variant, the delta from `full`:
- leave-out-<facet>: rank <N> vs full rank <M>; delta <±K>; one-line interpretation

## Bottom-of-list candidates (admin process-critic input)
Facets whose leave-one-out variant ranked at or above the `full` variant
(i.e. the chapter was no worse — or better — without them). These are
candidates for `change_type: delete` or `change_type: modify` proposals.

## Top-of-list facets (load-bearing confirmed)
Facets whose leave-one-out variant dropped sharply below full. These are
confirmed load-bearing; do not propose changes against them on this
chapter's evidence.
```

Surface report path + summary to caller.

---

## Phase 5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; always fires)

Every ablation produces process-relevant evidence regardless of outcome — even a study where every facet earns its keep is evidence (the chain is well-tuned, no `delete` proposals warranted, log `OK` and move on).

Dispatch:
- `subagent_type: admin`
- prompt carries:
  - `mode: process-critic`
  - `trigger.reason: on-demand`
  - `trigger.source_report: <Phase 4 persist path>`
  - `trigger.source_verdict: ablation:<bottom-candidate-count>-low-rank-facets`
  - `gate_path: .claude/commands/and-ablate.md#phase-3`
  - `secondary_gate_paths: [<paths of the rubric files for each bottom-of-list facet>]` — admin's proposal target when a facet underperforms is usually the facet's rubric, not the ablation command itself.

Admin reads the ranking + `staff/admin/process-proposals.md` (to detect prior ablation evidence on the same facet — recurrence is the threshold for `delete`; first-occurrence low-rank is `modify` or `OK`). Returns logged in the ablation report tail under `## admin-process-critic`. See CLAUDE.md Rules §13.

---

## Phase 6 — Memory write

Update showrunner memory:
- `chapters[<slug>].ablations[]` append: `{ran_at, work_dir, report_path, bottom_candidates: [<facet-slugs>], top_facets: [<facet-slugs>]}`.

Print final summary: report path, top-3 and bottom-3 facets, admin verdict.

---

## What this command does not do

- Does not modify bones, facets, dialogue, draft, render-log, or any chain artifact. Read-only.
- Does not dispatch `/and-stitch` phases. The renderer-minimal agent is a different renderer; ablation variants are NOT comparable to shipped chapters from `/and-stitch`. They are comparable to each other.
- Does not auto-fire. On-demand only.
- Does not implement admin's proposals. Admin appends to `process-proposals.md`; the principal triages.
- Does not gate the chain. An ablation that reveals a weak facet does not block the next chapter — it produces evidence for the principal to act on.

---

## Cost shape

Per run: 12 `renderer-minimal` dispatches (sonnet, single-shot, ~bones+9 facets read per dispatch) + 1 `general-purpose` ranked cold-read (12 prose files in, ranked report out) + 1 `admin` process-critic dispatch. Roughly 14 model dispatches per ablation.

Across a 10-chapter book fully ablated: ~140 dispatches. That is the cost of testing the facet-value assumption end-to-end on a book. Run selectively.

---

## When to run

- After a chapter ships and you want to know which facets carried it.
- When you suspect a facet has been quietly low-value across recent chapters (admin will already have flagged this via STM pattern detection if the signal is strong).
- At book midpoint or close, as a one-shot before book-level audits.
- When considering a `change_type: delete` proposal against a facet — ablation is the evidence the principal needs before approving the deletion.

Not after every chapter. Not as part of `--cascade`. Not as a gate.
