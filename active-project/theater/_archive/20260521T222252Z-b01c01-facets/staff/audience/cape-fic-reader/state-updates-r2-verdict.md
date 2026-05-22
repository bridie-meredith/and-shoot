---
reviewer: cape-fic-reader
facet: state-updates
cycle: 2
episode: b01-c01
date: 2026-05-20
verdict: accept
---

# Verdict reasoning

Cycle-1 complaint was a single delivery failure: the rubric-carve-out annotation block was authored in the per-character source slice but did not propagate to the top-of-file position in the consolidated state-updates.md. The consolidated file ran straight from frontmatter close to `# source: env` with nothing between them. That meant any reader auditing the consolidated file saw 8 taylor-state entries — including knowledge.* and social-state.* class, both requiring NI co-citation per rubric — with zero on-file defense. Information chain broken exactly where downstream corruption risk is highest.

Cycle-2 fixer inserted the full carve-out block between the frontmatter close (line 5) and `# source: env` (now line 39). Lines 7-38 of the current state-updates.md are the carve-out. The block covers:

- state:11 @6 (knowledge.flea-bottom-geometry) — NI-spine present, confirmed ✓
- state:13 @8 (social-state.with-coll) — NI-absent; defense: spoken-acknowledgment carried by dialogue:coll:1, narrator:2 @6 establishes the interiority block
- state:16 @20 (knowledge.coll-pattern) — NI-absent; defense: day-close flat-low, NI:4 @18 carries cost register, third NI fire would breach band ceiling
- state:17 @25 (social-state.with-wren) — NI-absent; defense: speech-act IS the delta-producer, NI:6 @27 resolves two beats later
- state:9, :10, :12, :14, :15 — mechanical-action class, carve-out exemption applies

The who-knows-what-when chain is now readable before you reach any of the entries it defends. That is what was missing and that is now present. The four "accepted-with-defense" entries are named explicitly with their individual rationales. The band-ceiling collision is explained (6/27 = 22.2%, within 15-25% band; adding NI fires to satisfy mechanical state pairing would push past ceiling). The mechanic-action exemption class is stated.

The capability-silence discipline flagged correct in Cycle 1 remains intact. No new entries on @15, @18, or @22. No deployment threshold crossed, no capability field fired. The cull notes in the taylor-hebert source section are unchanged and correct.

The lonely entry at state:7 @12 (coll work-state open) still carries no co-location. I raised this in Cycle 1 as a concern that looked worse without the carve-out. With the carve-out present and explaining the file-level context, the lone work-state entry reads as what it is: an honest open to a two-entry work-cycle chain (state:7 opens at @12, state:8 closes at @20). Reality axis holds; frugality holds; the cycle-pair makes the lone opener legible. Not a blocking concern.

No new problems introduced by the Cycle-2 fix. The fix was position-only, minimum-change; entry content untouched. All Cycle-1 complaints resolved.

Accept.

# Entry-level callouts

[state-updates:state:11] @6 — `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped`
Clean in Cycle 1, clean now. NI co-citation confirmed (narrator:2 @6 in cite-index). Carve-out's first coverage note makes the clean-case explicit. No issue.

[state-updates:state:16] @20 — `actor:taylor-hebert-kl-122ac.knowledge.coll-pattern: unread -> day-cycle-pattern-read`
knowledge.* field. Rubric requires NI co-citation. Defense now at file-top in the carve-out: flat-low scene-B close, NI:4 @18 carries cost register, band-ceiling collision documented. The information chain for this entry now works from the top of the deliverable. Cycle-1 complaint closed.

[state-updates:state:17] @25 — `actor:taylor-hebert-kl-122ac.social-state.with-wren: unknown-ward -> spoken-once`
social-state.* field. Rubric requires NI co-citation. Defense now at file-top: speech-act IS the delta-producer; NI:6 @27 resolves the interior register two beats later. The highest-stakes state write in the chapter has on-file justification at the point where a reader first encounters the file. Cycle-1 complaint closed.

[state-updates:state:13] @8 — `actor:taylor-hebert-kl-122ac.social-state.with-coll: unobserved-block-fixture -> acknowledged-once-by-block-fixture`
social-state.* field. Defense now at file-top: acknowledgment-beat carried by dialogue:coll:1 + state-on-bone; narrator:2 @6 establishes the interiority that this lands inside. Cycle-1 complaint closed.

# Convergence trace

[state-updates — file-level / fault-001] — Cycle-1: carve-out absent from consolidated file top. Cycle-2 fix: carve-out inserted at lines 7-38 between frontmatter close and `# source: env`. Position requirement satisfied. Fault-001 closed.

[state-updates:state:16] @20 — Cycle-1 convergence with fault-001 criteria (b) and (c). Carve-out now names knowledge.coll-pattern in "NI-absent; defensible" subclass with explicit flat-low/band-ceiling rationale. Criteria met. Closed.

[state-updates:state:17] @25 — Cycle-1 convergence with fault-001 criteria (b). social-state.with-wren named at file-top with speech-act defense. Criteria met. Closed.

[state-updates:state:13] @8 — Cycle-1 convergence with fault-001 criteria (b). social-state.with-coll named at file-top with acknowledgment-block defense. Criteria met. Closed.
