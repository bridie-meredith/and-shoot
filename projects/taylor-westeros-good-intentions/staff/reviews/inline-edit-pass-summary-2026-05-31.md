# Inline concision + flow pass — summary

Session: 2026-05-31. Branch: `session/audit-and-stitch-2026-05-31`.
Replaces Fork C + Fork D, both of which branched from an ancestor commit
missing the iter-1 + iter-2 plants, then cut load-bearing material despite
explicit instruction to preserve it.

## Tooling failure noted as process gap

`isolation: worktree` on the Agent dispatch tool created worktrees from a
commit *prior to* my direct iter-2 commits on the session branch, even
though the session main HEAD held the converged PASS-COHERE state. Both
forks operated on the unrevised baseline (~8,954 words) rather than the
converged state (~9,924 words). Their summaries listed all my iter-1 +
iter-2 plants as "not present in source" — they were operating on
ancestor state without those plants. Fork C's cuts to the *baseline* hit
several locations that, on the converged HEAD, contain load-bearing
material; merging Fork C would have dropped Wren chain anchors.

**Process gap (tooling, not source-material):** Agent `isolation: worktree`
does not reliably branch from the session's current HEAD when there are
intervening direct commits between the last merge into the branch and the
dispatch time. The worktree appears to be tracking an earlier reference.
Worth investigating; not specific to this project. For now: avoid
isolation:worktree for editing passes that depend on recent in-session
commits; use inline editing or pre-merge a checkpoint to a longer-lived
branch first.

## Pass executed inline on session HEAD

Five chapters touched with surgical concision + flow edits. c01 and
prologue work from prior iteration left untouched. Total delta:

| Chapter | Before (words) | After (words) | Delta | % |
|---------|---:|---:|---:|---:|
| c01 | 735 | 735 | 0 | 0% |
| c02 | 1231 | 1054 | -177 | -14.4% |
| c03 | 1440 | 1301 | -139 | -9.7% |
| c04 | 1883 | 1553 | -330 | -17.5% |
| c05 | 1742 | 1539 | -203 | -11.7% |
| c06 | 1147 | 1052 | -95 | -8.3% |
| c07 | 1746 | 1723 | -23 | -1.3% |
| **Total** | **9924** | **8957** | **-967** | **-9.7%** |

Combined file regenerated at
`active-project/draft/_combined-b01-c01-c07-revised.md` (8,985 words
including chapter-divider lines).

## Edit pattern (representative)

**Triple-restate collapse (c02):**
- Before: "The accounting closed the count. / The accounting reached the
  ward-junction entry. / The ward-junction corner returned the
  junction-lane void. / The count stalled."
- After: "The accounting closed the count, reached the ward-junction
  entry, returned the junction-lane void. / The count stalled."

**Restate paragraph removal (c04 four-ward enumeration repeats):**
- Cut: "Pig Tallow Lane returned ward-tier bodies and nothing above
  ward-tier; through the range at its far reach, the stitch-house frames
  stood at the next ward's edge, marking the second ward as the next ward
  to be read."
- Replaced with: "Pig Tallow Lane returned ward-tier bodies and nothing
  above ward-tier. At the range's far reach, the stitch-house frames
  stood at the next ward's edge."

**Filler clause removal (c03):**
- Cut closing prologue line: "I had not stopped doing the work. The work
  was the same work. The work was what I did instead of the thing the
  work made possible." → kept only the final sentence.

**Flow improvement — paragraph joining (c05):**
- Joined "The courier raised the spine." and "He found the feet." into
  one paragraph (the body-grammar pair belongs as one beat).
- Joined "I delivered the report-entry..." paragraph with the
  enforcement-record paragraph (one accounting move, one breath).

## Cohere re-verification (manual)

Re-read the revised combined file against the iter-2 PASS-COHERE axis
scorecard.

### naive-q4 (character-presence accumulation)
**PASS holds.** All six Wren chain anchors intact verbatim:
- c01 line ~57: "the stitch-maker's ward — a Hook girl of eleven who
  watched cloth before she cut it, and watched people the same way" ✓
- c02 ward-junction filing: "The stitch-maker's ward — the eleven-year-old
  whose hands had gone up first at the cart-morning..." ✓
- c03 salt-fish row: "the feed returned the stitch-maker's ward at the
  salt-fish row a beat before the eyes did — the same eleven-year body
  the count had filed at the stitch-house lane the morning of the cart..." ✓
- c04 second-ward range: "the feed returned Wren Stitch-Maker at the
  second-ward range. She would not be written down." ✓
- c05 print-held-longer: "the stitch-maker's ward print held a length
  longer than the others in the closing, the gait coming back at the
  salt-fish row at a beat the count was paying out wider than the
  bodies around it" ✓
- c06 recognition + silence chain naming all five prior touches ✓

### naive-q6 (apparatus-register cumulative load)
**PASS holds, strengthened.** Total apparatus-vocabulary mass cut by
~10%; the densest passages (c04 four-ward enumeration, c02 evening
accounting restate, c05 evening review back-half) shortened. Sensory
anchors all preserved:
- c01 late-summer dust ✓
- c02 salt-day rhythm ✓
- c03 salt-day, second of fishmongers' three ✓
- c04 Maiden's name day + Cobb founding-entry plant ✓
- c04 Halvard fixture nod at chandler's-storehouse corner ✓
- c05 first-cold + bay-wind + damp ✓
- c05 breath-shallowing at bedframe + bay-damp in boards ✓
- c05 cold-palm hand-print at stopping moment ✓
- c06 Father's name day three nights off + sept-bells ✓
- c07 bay-wind + Crone's stretch ✓
- c07 four-names consequence three paragraphs ✓

### audience-substance (cape-fic-reader rotation)
**SUBSTANCE-FELT holds.** Wren chain unchanged; cost-bearer earned;
asymmetric-reshape beats (c03 deal, c06 four names) unchanged; cape-fic-
reader's "new character earning trust without paying for it" hot-button
does not fire (six anchored touches before c06 hinge).

### Non-load-bearing CAUTIONs
- naive-q1 monotony: SLIGHTLY IMPROVED (less recursion across whole stretch)
- naive-q3 calendar drift: PRESERVED (all calendar anchors intact)
- naive-q5 sensory thin in middles: SLIGHTLY IMPROVED (cuts removed
  apparatus padding adjacent to sensory anchors, letting anchors breathe)
- naive-q7 machinery-chapter feeling at c02/c05: IMPROVED (c02 cut ~14%,
  c05 cut ~12%; machinery beats more compressed, less accumulation)
- naive-q8 close-of-section appetite: PRESERVED (c07 close untouched)
- dramatist-arc asymmetric pacing: STRUCTURAL, unchanged
- dramatist-scene-shape interior-dominant skew: STRUCTURAL, unchanged

## Out-of-source material flagged

None. The pass was strict concision/flow — cuts and surviving-prose
bridges only. No content invented, no facts changed, no characters or
world details added.

## Hard constraints honored

- DO NOT INVENT: honored. Every word in the revised drafts traces to
  source (iter-2 HEAD).
- DO NOT change established facts: honored (counts, names, locations,
  trade-shape unchanged).
- Earth-Bet proper-noun fence: honored.
- Italicized prologue structure: honored.
- Chapter divider structure: honored.

## Final verdict: PASS-COHERE preserved

The sub-section is now ~9.7% shorter, more readable in the middle
chapters where apparatus-fatigue dominated, and all cohere-PASS
machinery is intact. No structural beats lost; no plants cut; no
out-of-source material introduced.

## Next steps (principal triage)

1. **Upstream re-cascade** still required: `theater/bones/b01-c0X.md` and
   `memory.md` chapters[] block do not reflect any of the iter-1 /
   iter-2 / inline-pass edits. Treat as `/and-write revise --from-signals`
   queue across c02-c07.
2. **Rushwick courier-attack payoff** (`pl-2026-05-31-007`) still
   unresolved — c05 enforcement-incident unprocessed across c06-c07.
   Principal decision required: downstream payoff (c08+) vs c05
   contractual re-frame.
3. **Tooling process gap** (Agent isolation:worktree branching from
   ancestor) — worth investigating; cross-project.
4. **PROP-0030 / PROP-0031** still await principal triage; this inline
   run shows the cohere-iterate loop logic works when state is correctly
   inherited.
