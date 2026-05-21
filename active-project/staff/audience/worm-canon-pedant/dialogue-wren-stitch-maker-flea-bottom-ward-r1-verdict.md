---
reviewer: worm-canon-pedant
facet: dialogue-wren-stitch-maker-flea-bottom-ward
cycle: 1
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

The line has voice. The card-signature work is real — the stacked declaratives, the were/weren't inversion, the occurrence-order report. That part holds.

The problem is the facet-license citation. The chosen-mark entry in the sidecar carries `facet-licenses: [DEFERRED-TO-R2 — feeling/NI at @19 expected to carry the eyes-down recessed posture + held-attention somatic tell; resolve to concrete <facet>:<id> @19 at R2 against locked graph]`. That is the R1-blind placeholder. The R2.6 shard resolved it to vibes:13 @19. The sidecar was not updated.

Per rubric (URI-FACETS-CYCLE-1): "A sidecar that documents the facet-license axis in R1-blind placeholder form and is not resolved at R2 with a concrete <facet>:<id> citation is a SIGNAL finding per entry." The auditor filed this as flag-009. The rubric makes this a SIGNAL, not a HARD.

But this reviewer's lens is citation precision and whether the piece knows what it is doing. The worm-canon-pedant tests whether the work's internal accounting is clean. A chosen-mark entry at cycle-1 whose facet-license axis is documented in a resolved shard but not written back into the sidecar means the sidecar cannot be read as a self-contained authoring record. That is an accounting failure. The shard says one thing; the sidecar says another. This reviewer cannot accept an entry whose primary citation document still reads DEFERRED when the resolution was available and should have been written back.

The fix is minimal: update the sidecar's Draft B chosen block `facet-licenses:` field to `vibes:13 @19`. One line. The content of the line is accepted; the record of the line is not.

Verdict: REVISE — not on voice, not on content, but on citation-completeness sidecar write-back. Route to dialogue-writer (wren fork) per auditor flag-009 routing. Once the sidecar `facet-licenses:` field is updated to `vibes:13 @19`, this entry should re-accept without another full V2/V3 pass.

---

# Stage 1 V2

## Entry wren:1 @19

**Utterance:** "The flies were round you again. They were round you on Tickler's Lane two days gone, and the lane went quiet after. It goes quiet where you've been. I weren't looking for it. I just saw."

**Q1 — Affirmative card-signature demonstration:**

From the worm-canon-pedant lens — voice-register precision, internal accounting, and whether the line's authoring record demonstrates the piece knows exactly what it is doing:

- §smallfolk Cadence: demonstrated. Four stacked declaratives; no subordinating conjunctions chaining them. The pattern is: observation, reiteration-with-location, generalization, disavowal-of-intent, flat close. Occurrence order is preserved.
- §smallfolk Syntax: "I weren't" — singular subject, plural verb — class-marker confirmed. "Two days gone" — lived-time marker confirmed. Both are cited in the sidecar with §-section. The citations are accurate.
- §persona Voice tells: the three cited tells (reports before interprets, does not hedge, enacts not-asking by absence) are all present and independently verifiable from the surface of the utterance. "The flies were round you" is before "It goes quiet where you've been" — observation precedes generalization. "I just saw" is flat with no qualifier. No question is reached for. All three are demonstrated, not merely avoided.
- §cond-westerosi-witness-vocabulary: the insect-event frame is used without reaching for "witchery." This is correct for the registered relationship mode (not-fearful, has-decided-not-to-make-it-a-problem).

Q1: PASS on voice and register.

**Q2 — Card not violated:**

- Earth-Bet hard-fence: CLEAN. No Brockton Bay, no Skitter, no PRT, no Endbringer, no Cauldron terminology. The auditor confirmed this.
- Hard Fence 2 (not-asking enacted by absence, not announcement): held. The line ends on "I just saw" — no question, no negation-of-question.
- Hard Fence 1 (no framework-claim, no precocity): the generalization "It goes quiet where you've been" is the seam the writer flagged. As written it stops short of mechanism-claim. The drafts sidecar defends it. Q2 holds on Hard Fence 1.

Q2: PASS on card compliance.

**Facet-licenses citation:**

This is where Q1's full gate fails for this reviewer. The rubric's Q1 requires affirmative demonstration with §-citation — the sidecar's Draft B chosen block does this for card-signatures. But the V2 facet-citation extension (rubric §V2 facet-citation extension, graph-aware addition) adds a second citation axis: `facet-licenses:` must also be populated post-R2 with a concrete `<facet>:<id>` reference.

The sidecar reads: `facet-licenses: [DEFERRED-TO-R2 — feeling/NI at @19 expected to carry the eyes-down recessed posture + held-attention somatic tell; resolve to concrete <facet>:<id> @19 at R2 against locked graph]`.

The R2.6 shard resolved this to `vibes:13 @19`. The cite-index confirms: `vibes:13 @19 back=Y co=[wren-stitch-maker-flea-bottom-ward:1]`. The resolution exists. But the sidecar — the document this reviewer reads to audit citation-completeness — still carries the R1 placeholder.

Rubric: "A sidecar that documents the facet-license axis in R1-blind placeholder form and is not resolved at R2 with a concrete <facet>:<id> citation is a SIGNAL finding per entry." SIGNAL. Auditor flag-009 filed this.

For this reviewer: the sidecar is the citation-completeness record. If the sidecar says DEFERRED and the shard says resolved, the sidecar has not been updated. Reading the sidecar alone — which is how the citation-completeness check works — the entry fails the facet-license axis of Q1. The shard is external corroboration, not the primary record.

**Stage 1 verdict: REVISE** — voice and card-compliance pass; facet-license citation axis in the sidecar is not resolved at the primary record level.

---

# Stage 2 V3 seams

Strongest hostile counter-argument from the worm-canon-pedant lens:

**Seam — the generalization "It goes quiet where you've been" and the boundary between observational and categorical knowledge.**

Worm-canon-pedant's lens: ignorance must be played correctly. A character knows what they have a path to knowing. Applied here: Wren has observed flies at Taylor's person on two named occasions (Tickler's Lane; the current encounter, "again"). She has observed that "the lane went quiet after" on the named occasion. She generalizes: "It goes quiet where you've been."

The hostile reading: "where you've been" is an unbounded generalization across all locations Taylor has occupied. To make that generalization from two data points — Tickler's Lane and the current scene — is an inductive leap the evidence barely supports. More precisely: she has one confirmed quiet-aftermath (Tickler's Lane). The current scene (@19) is the second flies-observation but the "quiet after" for this scene would be the quiet that is currently in progress — she is speaking during the aftermath, not after observing a second quiet-aftermath independently. That means her generalization rests on one confirmed data point and one in-progress instance.

That's not precocious — children generalize aggressively from small samples. But the text authorizes this as a pattern-report, and a worm-canon-pedant asks: is the evidence base legible to the reader? The "again" in "The flies were round you again" signals prior observations, not just Tickler's Lane. So there are more than two data points in Wren's observational history. But the reader only sees two named instances in the text. "Again" does the work of asserting a pattern without showing all the data.

This is not a card violation — the sidecar correctly notes that a generalization over multiple named instances is still observational. But the hostile reading is: a reader without access to the drafts sidecar's defense will hear "It goes quiet where you've been" as Wren claiming broader knowledge of Taylor's operational pattern than two named data points license. The sentence has the cadence of a conclusion, not a report.

This is lens-distinct from cape-fic-reader's stitch-isolation concern (that the facet graph at @19 is sparse) and from dark-fantasy-reader's affect concern (that the calm is unearned). This reviewer's concern is epistemics: does the line's knowledge-claim match what Wren demonstrably has access to knowing?

The fix, if one is needed, is the one the sidecar proposes: "drop 'It goes quiet where you've been' and keep only the two named instances." That collapses the generalization back to report. Whether that fix is warranted depends on whether the reader has been given "again" as sufficient evidence of a pattern. Judgment call; this reviewer reads "again" as doing enough work to license the generalization, barely.

Severity: the seam is real but the line accepts on worm-canon-pedant's epistemic axis. The pattern-knowledge is licensed by "again" establishing prior observation. The seam is not a revise trigger from Stage 2; the revise trigger is Stage 1's citation-completeness failure.

---

# Convergence trace

- Auditor flag-009 (SIGNAL, RUBRIC-FIDELITY): "Three dialogue sidecar chosen-mark `facet-licenses:` fields carry R1-blind placeholder `facet-licenses: [DEFERRED-TO-R2...]` form that was not updated in the sidecar at R2 write-back. Affected entries: wren:1 @19..." — this is the primary finding this verdict is built on. The auditor's routing is: dialogue-writer (wren-stitch-maker-flea-bottom-ward fork). This reviewer's REVISE verdict is the audience-level pressure on the same finding.
- Auditor Class 8 CONSTRAINT — Earth-Bet hard-fence scan CLEAN on wren:1 @19 — confirms Hard Fence 1 + 2 hold on the utterance text itself.
- Cite-index `vibes:13 @19 co=[wren-stitch-maker-flea-bottom-ward:1]` — the facet-license resolution is real; the cite-index reflects it. The sidecar does not. The verdict is not that the license doesn't exist; it's that the citation record is incomplete.
- Drafts sidecar self-flag (board-move boundary seam) — convergent with this reviewer's Stage 2 epistemic concern; the writer already named the seam and defended it. The defense is accepted for Stage 2. The Stage 1 citation failure stands independently.
