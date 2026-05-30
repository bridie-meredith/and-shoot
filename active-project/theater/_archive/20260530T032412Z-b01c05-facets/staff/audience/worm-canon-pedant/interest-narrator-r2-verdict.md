---
reviewer: worm-canon-pedant
facet: interest-narrator
episode: b01c04
phase: 5b-adversarial
cycle: 2
date: 2026-05-27
verdict: revise
prior-cycle: 1
prior-cycle-file: active-project/staff/audience/worm-canon-pedant/interest-narrator-r1-verdict.md
cycle-2-scope: re-review post DEC-0034 structural fix (preamble arithmetic correction only; content items not addressed)
---

# interest-narrator — cycle-2 re-review (b01c04)

*[Loading the R2.1 file. DEC-0034 structural pass corrected the preamble. Content was not touched. Reading the preamble first to confirm arithmetic, then returning to the three content items from cycle-1.]*

---

## (d) Documentation fix — carve-out preamble arithmetic

**Cycle-1 finding:** preamble claimed 7 mandatory fires but auditor pass-004 confirmed 6 SEAM anchors; @8 reference was orphaned (no narrator:N @8 entry in the file); non-mandatory count was internally inconsistent.

**Cycle-2 check:**

The post-fix preamble now reads:

> state-co-citation-mandatory: 6 entries (narrator:3 @9, narrator:11 @15, narrator:4 @18, narrator:6 @22, narrator:13 @27, narrator:7 @31)
> non-state-mandatory structural fires: 5 entries (narrator:1 @6, narrator:8 @36, narrator:9 @38, narrator:10 @7, narrator:12 @23)
> total: 6 + 5 = 11 entries. Arithmetic now closes.

Cross-checking against the actual entry list in the file body: @6, @7, @9, @15, @18, @22, @23, @27, @31, @36, @38 — 11 entries, all present. The @8 orphan reference is gone. The mandatory count (6) matches auditor pass-004. The non-mandatory count (5) is internally consistent and each named entry exists in the file.

**(d) is resolved. The arithmetic closes. The preamble is now machine-parsable without a false-positive fail risk.**

---

## (a) narrator:7 @31 — tense-register failure + AP10 chassis

**Cycle-1 finding (hard flag):** present-perfect "has just paid in full" reads as post-hoc accounting, not pre-calc surfacing. Taylor does not discover costs; she tracks them through execution. Past-perfect required. AP10 chassis ("the half-step of yard-air... is the exposure") compounds the frame-assignment register. Combined: tense failure + AP10 = block-level revise.

**Cycle-2 check:**

Current file text:

> 7 @31 the half-step of yard-air between her hand and his is the exposure she has just paid in full

The entry is unchanged from cycle-1. "Has just paid" is still present-perfect. "Is the exposure" is still the AP10 definitional-collapse chassis. Neither finding was addressed.

This is the file's clearest voice-register failure and it remains unaddressed.

**(a) not resolved. Still a hard flag. No change in disposition.**

---

## (b) narrator:3 @9 — AP10 chassis / event-registration gap

**Cycle-1 finding (secondary target):** "no longer a question of whether; has just become a question of how much" — AP10 chassis framing a category-shift rather than registering a perceptual event. The entry names the analytical conclusion (question-type has changed) rather than the perceptual channel that told her so (what she heard or did not hear in Jarvis's cadence).

**Cycle-2 check:**

Current file text:

> 3 @9 the lever is no longer a question of whether; it has just become a question of how much

Entry is unchanged. The chassis is the same. "No longer a question of X; has just become a question of Y" is the inverted-predicate template. The entry is still summarizing the frame-shift rather than registering what in Jarvis's cadence produced that read. "Has just become" is also present-perfect — same tense-register flag that fires hard on narrator:7 applies here at lower intensity (this is a peak-bone where present-perfect is more defensible, but the channel problem is primary and the tense is a compounding issue, not the block).

**(b) not resolved. Soft flag status unchanged.**

---

## (c) narrator:13 @27 — unanchored relative reference

**Cycle-1 finding (secondary target):** "the load she has carried before" — comparative without a named reference point. Taylor's interior register requires concrete anchors (counts, prior-scene references). The prior load is implied but unnamed. Rubric ACCEPT signature: specificity, distances in paces or counts, observations that name the chemistry or mechanics.

**Cycle-2 check:**

Current file text:

> 13 @27 the fourth ward opens to the feed; the saturation-cost has gone past the load she has carried before

Entry is unchanged. "The load she has carried before" is still unanchored. The three-ward spread from scene-B is the natural reference point — it is the named prior configuration in this chapter. The entry does not name it. The comparative remains below Taylor's interior register specificity standard.

**(c) not resolved. Soft flag status unchanged.**

---

## Summary of cycle-2 findings

| finding | type | status |
|---------|------|--------|
| (d) preamble arithmetic mismatch | documentation | **FIXED** — arithmetic closes; @8 orphan removed; 6+5=11 confirmed |
| (a) narrator:7 @31 tense-register + AP10 | content / hard | **NOT ADDRESSED** |
| (b) narrator:3 @9 AP10 chassis | content / soft | **NOT ADDRESSED** |
| (c) narrator:13 @27 unanchored comparative | content / soft | **NOT ADDRESSED** |

One of four cycle-1 items resolved. Three content items unaddressed.

---

## Running tally

Clean entries (carry forward from cycle-1, no new questions): narrator:1 @6, narrator:4 @18, narrator:6 @22, narrator:8 @36, narrator:9 @38, narrator:10 @7, narrator:11 @15, narrator:12 @23.

Still flagged: narrator:7 @31 (hard), narrator:3 @9 (soft), narrator:13 @27 (soft).

The documentation fix is confirmed and does not need to be re-flagged. The three content findings are escalated from cycle-1 advisory to cycle-2 demand per persistent-memory rule: if a persona noted it in round 1 and it is unaddressed in round 2, the note becomes a demand.

---

## VERDICT

**verdict: revise**

Reason: the arithmetic fix (d) closes correctly and is accepted. The three content findings — (a) tense-register + AP10 on narrator:7 @31, (b) AP10 chassis on narrator:3 @9, (c) unanchored comparative on narrator:13 @27 — were not addressed in this structural pass. All three remain open. Per cycle escalation: these are no longer advisory. They are demanded revisions before this facet can pass.

**Demands (escalated from cycle-1):**

- `[interest-narrator:7] @31` — DEMAND. Rewrite to past-perfect ("had already priced" / "had already calculated") and strip the AP10 definitional-collapse chassis. Surface the perceptual event: what she registers at the moment the sheet crosses from inside the feed's envelope to outside it. The cost was known before the handoff; register the execution, not the accounting.

- `[interest-narrator:3] @9` — DEMAND. Rewrite away from the AP10 category-shift chassis. Name the perceptual event in Jarvis's cadence that closed the conditional — what she did not hear that told her the whether-question was finished.

- `[interest-narrator:13] @27` — DEMAND. Replace "the load she has carried before" with the concrete prior count. The three-ward spread from scene-B is the natural anchor; name it or name the equivalent.

**Documentation status:** (d) accepted. Preamble arithmetic is closed and needs no further action.
