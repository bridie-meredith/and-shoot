# /and-facets b01-c01 — R2 shared brief (Phase 3)

## Chapter context

(Same as R1; refer to R1 shared brief at `_inflight/_shared-brief.md` for full context.)

- Slug: b01c01 / file form b01-c01
- POV: taylor-hebert-kl-122ac
- Cast: taylor-hebert-kl-122ac, coll-net-mender-flea-bottom, wren-stitch-maker-flea-bottom-ward
- Locations: flea-bottom
- 27 bones; flat-IDs 1-29 with gaps at 10, 21 (time-skip blanks); scenes A @1-9, B @11-20, C @22-29 (all flat-low rhythm-shape)

## R2 dispatch discipline

- **Graph-aware:** every judge sees the locked R1 graph (all facet files + per-character dialogue files + cite-index). None sees the others' R2 mutations.
- **Self-scoped deletion only:** a judge may DELETE only its own facet's entries. Cross-facet deletion belongs to Phase 5 audit.
- **Citation cascade on the author's proto-lines copy:** when you delete `<own>:<id>`, strip `[<own>:<id>]` from every proto-line in your `_inflight-r2/` copy.
- **Add-cap ≤5 per judge per run** (metaphor ≤3 per refuse-by-default; exposition ≤3; dialogue ≤3 per character).
- **No reordering of existing IDs.** Deleted IDs leave gaps. New entries get next-available IDs per facet.
- **Provisional-anchor binding:** R1 metaphor / vibes entries with descriptive `licensed-by:` hints get resolved here. A judge whose hint cannot resolve cleanly against the locked graph deletes the entry as unanchorable.
- **Locked-rubric + arbiter discipline:** carry `design/shoot-v2/r2-judge-tuning/B-locked-rubric.md` and `C-arbiter-protocol.md`; §Form re-test before every KEEP / DELETE / REVISE verdict.
- **Position-gate (G5) on adds:** every add carries a position-category note (approach-zone / peak / trailing-edge / post-peak / quiet-beat / denouement). All three scenes are `flat-low` / quiet-beat in this chapter.

## R1 graph inputs (every judge reads)

- `active-project/theater/proto-lines/b01-c01.md` (canonical merged proto-lines; post-Phase 2)
- `active-project/theater/facets/_cite-index.md`
- `active-project/theater/facets/location-state.md`
- `active-project/theater/facets/interest-narrator.md`
- `active-project/theater/facets/sensory.md`
- `active-project/theater/facets/state-updates.md` (consolidated; per-source slices preserved as `# source:` markers)
- `active-project/theater/facets/memory.md`
- `active-project/theater/facets/feeling.md` (consolidated)
- `active-project/theater/facets/metaphor.md`
- `active-project/theater/facets/vibes.md`
- `active-project/theater/facets/exposition-b01-c01.md`
- `active-project/theater/dialogue/taylor-hebert-kl-122ac.md`
- `active-project/theater/dialogue/coll-net-mender-flea-bottom.md`
- `active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md`
- `active-project/theater/facets/scene-map-b01-c01.md`

## Output paths

- Mutated facet file: in-place at `active-project/theater/facets/<facet>.md` (or per-character slice; or `theater/dialogue/<character>.md` for dialogue)
- Annotated proto-lines copy: `active-project/theater/facets/_inflight-r2/proto-lines-<facet>.md` (or `-<character>.md` for per-character forks)
- Decision-shard: `active-project/staff/<facet>/r2-decision-shard.md` (or `r2-decision-shard-<character>.md` for per-character)

## Position-gate context (all three scenes are flat-low)

Every bone in this chapter is in a `flat-low` / quiet-beat scene. No peak-bones, no peak-shadow-bones. Approach-zone reasoning applies throughout. The chapter is baseline-establishment; intentional near-zero substance_delta on most axes.

## Known R1 seams (surfaced by R1 authors; verify in R2)

- **AP8 fault in vibes v21** — token `the-gap-in-the-ledger-begins-here` parses as a sentence (finite verb). Vibes R1 author flagged; not re-judged in R2 (vibes-judging deferred), but auditor will flag at Phase 5. R2 metaphor / dialogue / memory judges may treat this as a known seam.
- **Cross-facet sound-baseline gap at @17** — sensory refused @17 (boots strike the cobbles) because no loc-state entry establishes a sound baseline; loc-state @17 names a discrete Watch-footfall sensory event. R2 may want to retire one or the other (this is a contradiction — Phase 5 audit territory).
- **Feeling cross-facet @27** — Taylor's `feel:2` (hand-stops) and Wren's `feel:3` (eyes-stay) co-cite at @27; check for NI/dialogue redundancy.
- **State-updates-taylor** field-extensions (7) — many `actor:taylor.*` extension-fields used (lodging-payment-status, knowledge.flea-bottom-geometry, knowledge.coll-pattern, inventory.pack, inventory.needle, social-state.with-coll, social-state.with-wren). Auditor will validate under Reality axis; if R2 judges find any duplicating NI / feeling / memory at the same anchor, surface as DEDUP candidates for Phase 5.
- **Memory mem:2 target-reference** — free-text gloss, no monument-card resolution (`monument-flea-bottom-hook-coercive-geometry` margit-referral candidate). SIGNAL only.
- **Exposition sparsity 29.6%** — above 1-5% band. Cold-start chapter override declared by R1 author (preamble + context + first-mentions for chapter 1 of 18).

## Hard fences (absolute; same as R1)

- No Earth-Bet proper nouns (case-insensitive substring scan; slug components count)
- POV: Taylor first-person only
- Magic dormant on KL court layer
- Theme never spoken on-page
- 122 AC Westerosi register

## §Form re-test (operationalisation of G1, every KEEP / DELETE / REVISE)

Before each verdict, re-read the entry text and ask:
1. Is the SVO body intact in the proto-line cite?
2. Does the entry's content satisfy its facet's rubric ACCEPT signature, not REJECT?
3. Does the entry's cross-facet co-citations resolve in the locked graph?

If any answer is no, the entry fails Form and gets DELETE or REVISE.
