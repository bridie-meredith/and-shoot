---
reviewer: cape-fic-reader
facet: state-updates
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

Most of the entry work is clean. The prop/env layer (pack grounded, needle cycles, net-condition, thermal, folded-net) tracks correctly — all genuine persistent mutations with clear acquisition paths. The capability-silence on @15/@18/@22 is exactly the constraint-honoring move: insect-sense at-passive, no deployment threshold crossed, no fire. That discipline is what earns tactical trust in a power-set like this. The cull notes are sound — transient locomotion dropped, eye-movements dropped, posture-as-state correctly refused.

The problem is a delivery failure, not an entry-quality failure. The `# rubric-carve-out` annotation block — the on-file defense justifying why 8 of 9 taylor-state entries carry no NI co-citation — exists in the per-character source file (`state-updates-taylor-hebert-kl-122ac.md`) but did not make it into the consolidated `state-updates.md` at the required position. The consolidated file goes from frontmatter close (`---` at line 5) directly to `# source: env` at line 7. The auditor's fault-001 is correct.

From a who-knows-what-when perspective this matters concretely: anyone reading the consolidated file to audit or write against it sees 8 taylor-state entries — including two knowledge.* entries and two social-state.* entries, which the rubric explicitly calls out as requiring NI co-citation — with zero on-file defense. The defense is real; it just isn't attached to the deliverable. That breaks the information-chain in exactly the direction that causes downstream corruption: the state gets written to canonical memory, and the next chapter's author inherits entries they cannot verify were legitimate.

The fix is mechanical — place the carve-out annotation block at the correct position in the consolidated file. Entry content does not need revision.

# Entry-level callouts

[state-updates:state:11] @6 — `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped`
The one taylor-state knowledge entry that has NI co-citation (narrator:2 @6 confirmed). This is the clean case. Its correctness makes the remaining 8 entries' NI-absence more visible in the consolidated file, because a reader can see the pattern and then see it break without explanation at the file level.

[state-updates:state:8] @20 — `actor:taylor-hebert-kl-122ac.knowledge.coll-pattern: unread -> day-cycle-pattern-read`
knowledge.* field. Rubric requires NI co-citation. Defense exists in the source file (day-close tick in flat-low; NI:4 @18 carries the cost register; trailing edge of scene-B doesn't require a third NI fire). That defense is reasonable — I accept it. But it is not in the consolidated file. Without the carve-out annotation at the correct position, this entry reads as a missed fire against the rubric's POV co-citation requirement.

[state-updates:state:17] @25 — `actor:taylor-hebert-kl-122ac.social-state.with-wren: unknown-ward -> spoken-once`
social-state.* field. Rubric requires NI co-citation. Defense exists in the source file (speech-act IS the delta-producer; NI:6 @27 resolves two beats later). I accept the defense — the speech act at @25 is the state-change moment, and NI trailing two beats is defensible. But again: not in the consolidated file. Same problem.

[state-updates:state:13] @8 — `actor:taylor-hebert-kl-122ac.social-state.with-coll: unobserved-block-fixture -> acknowledged-once-by-block-fixture`
social-state.* field. Rubric requires NI co-citation. Defense in source file: spoken-acknowledgment beat carried by dialogue:coll:1 + state-on-bone; narrator:2 @6 establishes the block-reading interiority this lands inside. Defensible. Not in consolidated file. Same structural problem.

[state-updates:state:6] @8 — `actor:coll-net-mender-flea-bottom.social-engagement-with-taylor: unspoken-block-stranger -> minimal-verbal-exchanged`
Non-POV actor. No NI co-citation required. Field-extension inline documented. The entry is clean; the field-extension note is present. No complaint.

[state-updates:state:7] @12 — `actor:coll-net-mender-flea-bottom.work-state: between-days -> at-work-on-net`
Lonely entry in the cite-index (no co-location, no inbound license). The reality axis holds: Coll's work-state does flip at @12 and persist through @20. The pay-off at state:8 (day-packed-net-folded) makes the chain real. But the consolidated file has no annotation addressing the lone-entry status. Given the absence of the top-of-file carve-out, this entry looks more vulnerable than it is.

# Convergence trace

[state-updates:state:11] @6 — directly overlaps fault-001 (F-006 UNRESOLVED from auditor r2): the auditor confirms this is the one co-cited entry; its correctness makes the remaining 8 entries' gap more visible. The auditor's criteria (b) require the carve-out to classify each of the 8 uncovered entries explicitly.

[state-updates:state:8] @20 — directly overlaps fault-001 criteria (b) and (c): knowledge.coll-pattern is in the "accepted-with-defense" subclass; the carve-out must cite §Anti-patterns #9 (density-on-flat) as the reason NI entries were not added.

[state-updates:state:17] @25 — directly overlaps fault-001 criteria (b): social-state.with-wren is in the "accepted-with-defense" subclass; must be named explicitly in the consolidated file.

[state-updates:state:13] @8 — overlaps fault-001 criteria (b): social-state.with-coll is the other "accepted-with-defense" entry; same requirement.

[state-updates — file-level] — fault-001 is the direct auditor finding this verdict converges on. The rubric-carve-out annotation is present in the per-character source file and absent from the consolidated deliverable. The fixer report claimed the fix was executed; the mutation did not reach the target file. This is the single actionable item.
