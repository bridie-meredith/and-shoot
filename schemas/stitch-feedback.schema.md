# Stitch Feedback Schema

Line-keyed feedback that routes back into the active profile and persona on re-stitch. The user reads the annotated polish file, identifies lines that read wrong, writes feedback here. The Stitcher's next `/and-stitch` dispatch consumes the feedback as patches.

Schema authority: this file.

Status: **draft (tuning)**.

---

## File path

`active-project/staff/stitcher/feedback-<episode-slug>.md`

One feedback file per episode. Optional — if absent, the stitcher runs without per-episode feedback. Pattern-level feedback also accumulates here before promotion to the persona.

---

## File structure

```markdown
# feedback — <episode-slug>
profile: <path to active profile>
persona: <active-persona-slug>
last-stitch: <ISO date>
last-render-log: <path to render-log this feedback addresses>

---

## Line-level (one-shot patches)

[L<N>] <feedback text>
[L<N>..L<M>] <feedback text>          # range form
[L<N>] CUT                             # explicit cut directive
[L<N>] KEEP                            # explicit keep directive (revert a Phase 7 cut)
[L<N>] RESHOW-ACCEPT                   # accept the reshow at this line
[L<N>] RESHOW-REVERT reason: <reason>  # revert reshow, restore original
[L<N>] REWORD-ACCEPT
[L<N>] REWORD-REVERT reason: <reason>
[L<N>] <free-form note>

---

## Pattern-level (persona tuning candidates)

PATTERN: <one-line description>
DETAIL: <multi-line context if needed>
SCOPE: <persona-slug | episode | scene>
SEEN-AT: [L<N>], [L<N>], ...           # examples in this episode
PROPOSED-RULE: <rule statement>

---

## Promoted patterns (resolved into persona)

PROMOTED <date>:
  pattern: <description>
  target-persona: <slug>
  rule-added: <rule statement>
  applied-from: this feedback file
  examples: [L<N>], ...
```

---

## Line-level entries

### Format

```
[L<N>] <free-form feedback OR directive>
```

`<N>` is the stable line-ID assigned at Phase 8 of the previous stitch run. IDs are preserved across re-stitches; if a line was cut and the user wants it back, the ID still resolves (the cut is logged).

### Directives (machine-actionable)

| Directive | Effect on re-stitch |
|---|---|
| `CUT` | Add `[L<N>]: cut` to the active profile's `anchor-overrides`; the originating fork re-runs and the cut is forced |
| `KEEP` | Add `[L<N>]: keep` to overrides; reverts a Phase 7 cut |
| `RESHOW-ACCEPT` | The reshow at this line is good; record positive signal for the persona |
| `RESHOW-REVERT reason: <reason>` | Reverts the reshow; restores the original facet content; logs the revert reason for tuning |
| `REWORD-ACCEPT` | Same as RESHOW-ACCEPT for a REWORD move |
| `REWORD-REVERT reason: <reason>` | Reverts the reword |
| `LENS: <lens-name>` | Force the lens hierarchy at this line's source anchor (override Phase 1's decision) |
| `MERGE: <other-line-id>` | Force merge with the named line at Phase 3 (overrides protected-pattern protection) |
| `UNMERGE` | Force un-merge if the line came from a Phase 3 merge |

### Free-form notes

Free-form notes are not machine-actionable but inform pattern-level entries. The stitcher's next dispatch reads them and the user (or a tuning agent) may promote them to PATTERN entries.

Examples:
```
[L23] too cognitive — try sensory-leads here instead
[L45] perfect, no notes
[L67] body anchor is missing; show me the mother's stillness, not just the verdict
[L18..L22] this whole opening reads as stage direction — find more interior register
```

### Routing on re-stitch

| Feedback type | Routes to |
|---|---|
| `CUT` / `KEEP` / `MERGE` / `UNMERGE` | Profile's `anchor-overrides:` block, keyed by source anchor (resolved from line-ID via render-log) |
| `LENS:` | Profile's `anchor-overrides:` block, sets `phase-1.lens-leads-override` for that anchor |
| `RESHOW-REVERT` / `REWORD-REVERT` | Profile's `anchor-overrides:` block, sets `phase-7.<move>-revert` for that anchor; reason logged in persona's `## Tuning notes` if recurring |
| `RESHOW-ACCEPT` / `REWORD-ACCEPT` | Positive signal; no profile change; reinforces persona's current bias |
| Free-form | Surfaces in the next run's `staff/stitcher/feedback-pending-review.md` for human or tuning-agent review |

---

## Pattern-level entries

### Format

```
PATTERN: <one-line description>
DETAIL: <multi-line context>
SCOPE: <persona-slug | episode | scene>
SEEN-AT: [L<N>], [L<N>], ...
PROPOSED-RULE: <rule statement>
```

### Examples

```
PATTERN: NI two-clause structures with non-sentient negation tail
DETAIL: The structure "[sentient subject] [knew/has X]; [non-sentient subject] [didn't know/has not Y]"
        treats the second clause as adding contrast, but the contrast is vacuous when the
        non-sentient subject couldn't be expected to know.
SCOPE: worm-tight
SEEN-AT: [L20]
PROPOSED-RULE: Q8 fires automatically on this structural pattern; cut tail at semicolon.

PATTERN: feel-clause always leads at peak-bones when feel is co-cited
DETAIL: Body before meaning. The mother's stillness should land before the silence's named
        significance. Sensory-spike rule 2 should be overridden by feel at peak-bones (per
        the scene-map's per-scene peak-bones[] list).
SCOPE: worm-tight
SEEN-AT: [L25] (Scene C)
PROPOSED-RULE: At any bone in scene-map peak-bones[] with feel firing, feel leads regardless of sensory tag.
```

### Promotion

Pattern-level feedback is reviewed (by the user or a tuning agent) and promoted into the active persona's `## Tuning notes` section. Promotion is explicit:

1. Add `PROMOTED <date>:` block to this file recording the promotion
2. Append the rule to the persona card's `## Tuning notes`
3. Reference the source feedback entry

Pattern entries that haven't been promoted are advisory only; the stitcher does not auto-apply them. Promotion is the discipline that prevents pattern-level feedback from accumulating into uncontrolled persona drift.

---

## Re-stitch scope

The profile's `feedback.re-stitch-scope` controls what re-runs when feedback lands:

- **`fork-only`** — re-run only the originating fork(s) for the affected anchor(s). Cheapest; risks downstream inconsistency if local-flow or buildup-preservation made decisions based on the now-cut line.
- **`fork-plus-downstream`** (default) — re-run originating forks AND downstream phases whose log entries reference the affected anchor or line-ID. Surgical and consistent.
- **`full`** — re-run the entire chain. Most expensive; needed only when feedback affects global behavior (e.g. persona change, profile rewrite).

The default surgical scope means most feedback is cheap to apply. A handful of line-level notes triggers a handful of fork re-runs.

---

## Validation faults

- `FAULT-FEEDBACK-UNKNOWN-LINE-ID` — `[L<N>]` references an ID not in the prior render-log
- `FAULT-FEEDBACK-INVALID-DIRECTIVE` — directive name not in the recognized set
- `FAULT-FEEDBACK-MISSING-REVERT-REASON` — `RESHOW-REVERT` / `REWORD-REVERT` without `reason:`
- `FAULT-FEEDBACK-PATTERN-NO-SCOPE` — PATTERN block without `SCOPE:` field

---

## What the feedback file is not

- Not a place to rewrite facets. Facet content is authored upstream of the stitcher.
- Not a place to rewrite bones. Bones live in `theater/bones/<book>-<chapter>.md` and are authored by `/and-write` (the substance-overhaul replacement for the pre-overhaul `/and-protolines` + `/and-season` bone-gate chain).
- Not a substitute for profile or persona files. Long-term tuning lives in profiles and personas; the feedback file is the bridge.
- Not a journal. One-line entries per line-ID; PATTERN blocks for promotion-candidates. No retrospectives.
