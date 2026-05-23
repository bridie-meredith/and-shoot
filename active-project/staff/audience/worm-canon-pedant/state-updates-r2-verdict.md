---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 2
episode: b01c01
date: 2026-05-23
verdict: accept
---

# Verdict reasoning

Two cycle-1 callouts to adjudicate. Walking each.

**[state:10] @20 — auditor-value discrepancy and NI alignment.**

My cycle-1 finding was that fault-012 directed repair against a `<new>` value (`flea-bottom-block-level-with-patrol-rotation`) that does not exist on disk; the on-disk value was already `flea-bottom-block-level-day-count-complete`. The discrepancy meant fault-012's specific criteria were mis-targeted.

Current on-disk state: the Taylor slice (state-updates-taylor-hebert-kl-122ac.md lines 31-42) shows the field value unchanged at `flea-bottom-block-level-day-count-complete`. The comment no longer enumerates patrol-rotation geometry or any other specific sub-acquisition. The comment now says the value reflects "what narrator:7's ledger-close licenses (the count's run finishing intact), not a list of individual acquired sub-fields." Narrator:7's text ("the day closed under the count she had been running") licenses exactly that — a ledger-close on the count, not a named-items acquisition.

The cycle-2 repair (H4) addressed the comment-level seam: the patrol-rotation enumeration that was driving the NI content-alignment concern is stripped. The on-disk value was already clean; now the comment aligns with it. The cycle-1 discrepancy (audit directed against a ghost value) is now moot because the comment that was creating the seam has been corrected. I can verify the actual on-disk field value and comment text independently of what any prior audit report quoted; they now align.

This callout is closed.

**[state:9] @9 — ward-geometry double-register.**

My cycle-1 finding: the field name `knowledge.ward-geometry` sits in a double-register zone — Westerosi city-district ("ward" as in King's Landing ward-arrangement) and Earth-Bet PRT-Ward program — and the file contained no documented disambiguation choice. I required either a disambiguation comment or a field-name change.

Current on-disk state: the Taylor slice carries the inline comment `# field-extension: ward-geometry (b01c01 passive orientation layer)` and the entry comment reads "First day's passive ward-read complete through the held-feet beat." The word "ward" in "ward-read" and "ward-geometry" is contextually anchored to block-level spatial orientation in Flea Bottom (a ward of King's Landing). The auditor's fault-023 sweep ran the extended category-noun scan explicitly, noted the usage, and classified it: "ward appears in 'Flea Bottom ward-arrangement' (exposition:5) and in character name slug suffixes — both are Planetos-register usages (smallfolk-ward as Westerosi social arrangement, not PRT-Ward parahuman-registry designation)."

I require that AU variants name their divergence or that unmarked vocabulary collisions be resolved. The fault-023 finding constitutes the documented decision I was asking for — it is on the record, in the audit report, that the authoring team considered the double-register and classified the usage as Planetos-register. That is the naming of the divergence I required. I would have preferred the disambiguation comment to live in the state-updates file itself rather than in an audit report, but the fault-023 classification is an authoritative, time-stamped, on-disk decision. It holds.

The "ward" vocabulary will only become a lore-leak if the prose renders it in a way that activates the PRT register. As a mechanical field name in the state-updates layer — not rendered prose — the risk is bounded and the disambiguation is documented. I accept this under the AU-names-divergence tolerance.

This callout is closed.

Remaining file review:

The Earth-Bet hard-fence scan returns 0 hits. Extended category-noun sweep returns 0 content hits. The "no power" in the Wren slice comment field (line 9, "capability: static 1/1 (child, no power)") is comment-level metadata, not a content entry. I verified this independently: the line reads `capability: static 1/1 (child, no power)` — this is the file's actor_baselines documentation for a Westerosi child character. "No power" here means no capability change from baseline, not an Earth-Bet power designation. Not a fence breach.

The Wren position and in_scene entries are canonical-correct. The relational-anchor-status non-fire is correctly documented. The Coll zero-entry file is correct for a fixture character.

Taylor's knowledge progression from null → flea-bottom-block-level-passive (@9) → flea-bottom-block-level-day-count-complete (@20) is a coherent tracked arc. The NI co-citation requirement for POV actor-state is met: narrator:2 at @9, narrator:7 at @20. Lore-mechanics: Taylor's shard doesn't have a passive knowledge-accumulation mechanic in canon — she acquires through insects' direct sense. The "passive ward-read" framing could be a tension point. But the context establishes that she is running insects through the block; "passive" here likely means she is not actively deploying special attention, not that she is acquiring knowledge without her power. The field comment says "passive orientation layer" — the insects are the channel; the "passive" qualifier marks the mode (routine scan vs. active investigation), not the absence of her power. That tracks. If later entries claim knowledge she could only have obtained by active insect-sense focus, I will flag it; here the framing is internally consistent.

State graph architecture is coherent. Authorized targets throughout. No cross-POV authoring violations. No drift-old values detected (state:9 old-value null is correct first-touch; state:10 old-value flea-bottom-block-level-passive chains correctly from state:9 new-value).

Accepting.

# Entry-level callouts

None blocking in cycle 2. Cycle-1 callouts resolved.

- [state:9] @9 — ward-geometry double-register: CLOSED per fault-023 documented classification (Planetos-register usage confirmed). disambiguation on-record.
- [state:10] @20 — audit-value discrepancy: MOOT. H4 repair stripped the seam; on-disk value and comment now align with narrator:7. Callout closed.

# Convergence trace

- H4 repair (state:10 comment): CONFIRMED. The specific seam my cycle-1 callout named (comment-level enumeration of sub-acquisitions contradicting the field value) is gone. Comment now restricted to ledger-close framing.
- fault-023 (ward-geometry field name): auditor classification documented. Accepted as the required AU-divergence naming. Callout closed.
- F6 repair (prop:oc-taylor-pack): confirmed per fault-019-cleared. No lore-anchor gap on the pack.
- state:4 @18: not a worm-canon-pedant concern (no Earth-Bet mechanic involved). Advisory left to dark-fantasy-reader.
