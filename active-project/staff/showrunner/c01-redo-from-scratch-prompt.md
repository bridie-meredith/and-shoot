# Prompt: retry b01c01 from scratch

Saved: 2026-05-24
Context: b01c01 shipped to main (PR #57). Post-ship 8-fork audit suite converged on prose-surface-of-substance gap. The substance contract is sound; the chapter under-renders it. This prompt is for redoing c01 from scratch *with* the post-ship lessons baked in, in case the depth pass via `/and-write revise --from-signals` doesn't go far enough.

---

## Paste-ready prompt

```
I want to retry b01c01 from scratch. The current version shipped to main (PR #57)
with cold-read PASS but the post-ship 8-fork audit suite converged on a prose-
surface-of-substance gap: the substance contract is sound, but the chapter under-
renders it. Reports live at active-project/staff/reviews/*-b01c01-* and the audit
suite prompts at active-project/staff/showrunner/post-ship-audit-prompts-b01c01.md.

Keep:
- The series chunk, book chunk, chapter chunk, and scene chunks in showrunner
  memory (chapters[b01c01] is sound — the contract delivered at the rationale
  layer, just not at the prose layer)
- The cast (Taylor, Coll, Wren — all three earned their slots in the audit; Wren
  is the strongest forward-plant in the chapter)
- The substance contract: knowledge axis 0.48 Δ, hinge dramatic_shape, 9 held-
  capability bones, goal triplet (rule intact / the ward / the child who will pay)
- The closing image (Wren names the flies; "There were flies on the meat-stall.
  There weren't any on your hand.") — all four post-ship reader-experience forks
  flagged this as the moment that earned the chapter

Discard:
- The current draft/b01-c01.md (preserve as archive/draft/b01-c01.shipped-2026-05-24.md
  for diff-against-future-version reference)
- The render-log, facets, and bones — they'll be re-emitted
- The 11 deferred staging-review SIGNAL findings — they predicted the audit
  finding; rather than apply them piecemeal, re-author with the body-staging
  requirement built into the bone-decomposition itself

Author with these baked in:

1. PROSE-LAYER OPPOSING-FORCE on held bones. Phase 6 bone-gate audits at
   rationale layer; the prose surface needs the same check. For each axes_held
   capability bone, the prose must show the opposing-force pushing AND the
   discipline resisting in body or sensory or spatial terms — not as a label
   ("I held"), not as a register-tic ("I held the eyes"), but as a felt act.
   The cluster the audit found (@9 @19 @24 @27 @29) was rationale-correct and
   prose-mute. /and-write Phase 6 should be extended (or a new check added at
   Phase 7) to fail when held bones name the OF in rationale but the prose
   trace is label-only.

2. OPENING PARAGRAPH ECONOMY. The current L1 ("subsistence-class permanent —
   the anonymous copper-star transaction purchasing entry") is the single
   most-flagged drag point across all four reader-experience forks. The
   chapter pays Flea Bottom rent and explains the economic primitive in the
   same breath. Three of four readers said they finished only because the
   chapter was 27 lines. The opening either earns the apparatus (pays a
   cost-bearer beat that justifies the systems-analyst voice immediately)
   or strips it (renders entry-paid as embodied action, lets the apparatus
   surface gradually as Taylor's register reveals itself).

3. REGISTER-AS-MANNERISM CHECK. Three iterations of "I held the eyes" in
   27 lines is the discipline tic showing through. /and-write should flag
   repeated bone-internal idioms (>2 iterations of the same load-bearing
   phrase) as a SIGNAL — promotes the audience taste-call ("register-becoming-
   mannerism" from worm-canon-pedant) into a mechanical check.

4. SOCIAL-COVER PHYSICS legibility. The cold-read recovered summary misread
   Taylor as "posing as a net-mender" — she is paying for a corner and using
   Coll's proximity as cover without explicit arrangement. C02/c03/c04 all
   depend on this physics being legible to a first reader. Render the
   distinction on the page (e.g. the copper-star going to a building-keeper,
   not to Coll; Coll's eye-lift as registering-without-claiming).

5. WARM-BODY → BUG-PRESENCE primitive. L7's "warm body" is the wrong organ
   for Taylor's power — canon reads bug-presence (chemical, vibration), not
   mammalian thermal. One-word swap, but worth catching.

Pipeline path:
1. /and-substance chapter b01c01 redo — re-author the chapter chunk to
   absorb (1) and (2) into pov_narrator + scene_conflict. Likely small
   edits, not a full re-author.
2. /and-write b01c01 redo — bones from scratch with the new prose-layer
   OF requirement on held bones (4 and 5 fold into per-bone rationale).
3. /and-review bones b01c01 — mandatory.
4. /and-facets b01c01 — facets from scratch.
5. /and-stitch b01c01 — Phase 9 cold-read terminal gate. The new URI-
   STITCH-SIGNAL-CLUSTER soft-gate fires if the same body-staging cluster
   reappears.
6. /and-postop b01c01 — routine 3-fork (substance + naive + persona).
   Diff against the shipped version's audit findings: did we move the
   needle?

The cap-burn @8 bare-speech-bone for Coll is the one open question: in the
redo, does Coll get a real dialogue facet (and an entry in cards/personas/)
or stay silent? The post-ship dramatist verdict said no downstream chapter
assumes the deleted line was rendered, so silent is defensible. Decide at
scene-decomposition time.
```

---

## Why this prompt instead of revise --from-signals

`revise --from-signals` is the right call when the chapter is 80% there and
the cluster is 20% of the work. The audit suggests the chapter is closer to
70-75% — the substance is real and the closing pays, but the opening drag
and the held-bone prose-mute pattern are systemic enough that bone-by-bone
edits may not converge. If after one revise pass the same cluster reappears
in /and-postop, lift to this from-scratch prompt instead of grinding more
revisions.

The contract itself does NOT need re-authoring. The chapter chunk is sound;
the failure is one level down, at decomposition + prose-render. From-scratch
here means /and-write redo + downstream, not /and-substance chapter redo.
