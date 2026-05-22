---
reviewer: worm-canon-pedant
facet: dialogue
character: coll-net-mender-flea-bottom
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: accept
---

# Verdict reasoning

## Stage 1 — V2 strict

**Entry under review:** `1 @8 | "There's mending if you can hold a needle."`

This reviewer's primary concern at dialogue review is voice-register fidelity and hard-fence compliance — specifically, whether `cond-westerosi-witness-vocabulary` is observed and whether the Earth-Bet noun fence is clean.

**Q1 — Affirmatively demonstrates ≥1 card signature?**

Yes. Running the card-signature inventory the sidecar supplies:

- §Voice "trade-worker register; observation, state, no interpretation": the line demonstrates this directly. "There's mending" is an observation of work-state. "If you can hold a needle" is a condition, not an interpretation of Taylor or a prediction about her. The register is demonstrably trade-worker mode.
- §Voice tells "does not speculate": the conditional is a test. Coll is not speculating about whether Taylor can hold a needle; he is setting the criterion and leaving the outcome open. This is the specific form of non-speculation the card identifies — not "she looks like she could" (speculation), but "if you can" (condition that the work will answer).
- §Hard Fences §1 (never names): the line names only the work and the work-tool. Taylor is addressed by implication only, through the conditional. No name, no label, no category. The contrast with Gylda's function (names the pattern once) is preserved.
- `cond-westerosi-witness-vocabulary` compliance: Coll is not in witness-vocabulary mode. He has not yet accumulated the pattern (state.md: `taylor_pattern_registered: not-yet`). The card scopes witness-vocabulary to description/reporting of Taylor's capability; this line is not that. On-card.

Q1: PASS.

**Q2 — Card not violated?**

Critical checks for this reviewer:

1. Earth-Bet hard-fence scan: "There's mending if you can hold a needle." — no Earth-Bet proper-noun hits. Clean.

2. `cond-westerosi-witness-vocabulary` prohibitions: no parahuman vocabulary. No capability-attribution. Coll is not describing Taylor's power; he is offering a work-spot. The behavior card's prohibitions do not apply to this line's content domain.

3. `cond-earth-bet-noun-fence` (referenced by `cond-westerosi-witness-vocabulary`): this card governs what Taylor does not say. Coll is not Taylor; the fence applies to Taylor's speech. Not applicable here. But the cross-contamination risk — Coll using vocabulary that sounds like Taylor's register — is worth checking. "There's mending if you can hold a needle" has no Taylor-register bleed. It is trade-worker Flea-Bottom smallfolk register throughout.

4. §Hard Fences §2 (non-interpretive): the line makes no interpretive moves about Taylor. The work-test conditional is not an assessment of her character, origin, or capability. On-card.

5. State.md check — `taylor_pattern_registered: not-yet`. This is Day 1 of Taylor's arrival. Coll has not accumulated the pattern. The line is consistent with this state: the offer is the generic work-spot-cover-handshake, not a pattern-informed response. If the line had said something like "I've seen you passing" or "you look like you know nets" — that would be a state-consistency violation. It does not. PASS.

6. `cond-kl-social-physics-122ac` (referenced in sidecar): the work-tested lateral cover-handshake is the correct smallfolk social-physics mechanism for admitting a stranger to a block-spot. The keeper's admission licenses the work-offer. No social-physics violation.

Q2: PASS.

**V2 verdict: ACCEPT.**

The line is correctly sourced from the card and the behavior condition stack. It does not violate any hard fence. It demonstrates card signatures affirmatively. Citation-completeness is satisfied. The Earth-Bet noun fence is clean. State consistency with `taylor_pattern_registered: not-yet` is confirmed.

**Facet-license citation check:**

- `state:6 @8`: cite-index entry present. `back=Y co=[coll-net-mender-flea-bottom:1, state:13]`. The dialogue entry is the back-cited source. Resolution: CONFIRMED.
- `state:13 @8`: cite-index entry present. `back=Y co=[coll-net-mender-flea-bottom:1, state:6]`. Resolution: CONFIRMED.
- Non-fires at `loc-state @8` and `narrator @8`: cite-index confirms no entries at @8 for these facets. Non-fire is structural. The sidecar's documentation of the non-fire reasoning is acceptable as rubric-carve-out analog for expected-slot non-fires. ACCEPTED.
- Both citation axes (card-signatures + facet-licenses) are populated and resolve on disk. Citation-completeness: PASS.

## Stage 2 — V3 adversarial seam-finding

**Strongest hostile read from this lens:**

The worm-canon-pedant's attack surface on a Coll line is not Taylor's canonical behavior (Coll is a Westerosi original character, not a Worm canon entity). The attack surface is instead:

**The behavior-card state-consistency check at a tighter granularity.** The sidecar documents that state:6 @8 fires the mutation `social-engagement-with-taylor: unspoken-block-stranger -> minimal-verbal-exchanged`. This is a new-field extension. The state.md does not carry a `social-engagement-with-taylor` field at project-open — the field is being created at @8 by the dialogue line. The `field-extension` note in the state-updates file covers this: "new field for tracking first-touch verbal contact between block-fixture and Taylor; tracked-state aspect, not perception; persistence absolute past beat."

The attack: if the field is being created at @8, the prior state "unspoken-block-stranger" is retrojected (the character had no tracked value for this field before the extension). A strict state-tracking reader asks: was the prior state correctly unset, or is "unspoken-block-stranger" a value that had to exist before it could transition? The state-updates file's field-extension note handles this — field-extensions establish the field with an acknowledged prior-to-extension baseline. The rubric permits this; the note is on-file.

More pointedly: the cite-index back-citation for `coll-net-mender-flea-bottom:1` correctly identifies the dialogue entry as the source of the state-mutation. The cross-citation between state:6 and state:13 and the dialogue entry is the correct structure. No audit finding bears on this entry; the r2 audit's fault-001 is about the taylor-source rubric-carve-out annotation in state-updates.md, not about the coll-source entries.

**A narrower attack:** The sidecar's facet-license record notes "expected slot `narrator @8` — does not resolve." The NI file carries no entry at @8. This is structurally documented. But the worm-canon-pedant's concern is: if the swarm-feed registration of Coll's working-posture happened at @4 (narrator:1 @4: "the network has him before he has her"), and the dialogue line at @8 is the first spoken exchange, does Taylor's NI register being addressed? The NI file does not fire at @8. The sidecar's defense is that @6's narrator:2 carries the block-reading interiority that frames @8. This is acceptable — NI does not need to fire at every state-mutation; the rubric-carve-out in state-updates documents this explicitly for the social-state.with-coll entry.

The reviewer does not find a Worm-canon violation here because Coll is not a Worm character. The strongest available attack — state-field retrojection — is handled on-file. The citation-resolution walk is clean.

**Seam verdict:** No seam that rises to a revision demand. The field-extension note deserves to be read once by the stitcher to confirm the "unspoken-block-stranger" baseline reads correctly given that Coll has been in Taylor's swarm-awareness since @4. But this is not a line failure.

# Entry-level callouts

`[dialogue:coll-net-mender-flea-bottom:1 @8]` @field-extension-retrojection — state:6 @8 creates `social-engagement-with-taylor` as a new field with retrojected prior-baseline "unspoken-block-stranger." The state-updates file's field-extension note covers this. Stitcher should confirm that the reader's tracking of the prior Coll-Taylor relationship (non-verbal, swarm-registered since @4) aligns with the retrojected baseline. Not a citation failure; a consistency-awareness note.

# Convergence trace

- Sidecar's R2 facet-license record: `state:6 @8` and `state:13 @8` both verified. The back-citation structure in the cite-index is correctly bidirectional (both entries cite `coll-net-mender-flea-bottom:1`; the dialogue entry cites both state entries in the sidecar's `facet-licenses:` block). Graph-walk resolves cleanly.
- Cite-index lonely-entry note at `state:7 @12`: `coll-net-mender-flea-bottom pulls the net` is a round-2 deletion candidate. Not a dialogue-entry concern; Coll's @8 entry is not lonely (co-citations present). Flagged for awareness only.
- Auditor r2 fault-001: scoped to taylor-source rubric-carve-out annotation in state-updates.md. The coll-source entries (state:6, state:7, state:8) do not carry the same annotation requirement (they are not POV-actor entries; the cross-facet NI co-citation contract scopes to mental/perceptual/relational state mutations of the POV actor). Not convergent with the coll dialogue entry.
- NI non-fire at @8: consistent with the cite-index (no narrator entry at @8). State-updates rubric-carve-out annotation documents the social-state.with-coll @8 NI-absent defense explicitly. Convergent across auditor, sidecar, and this reviewer's check.
