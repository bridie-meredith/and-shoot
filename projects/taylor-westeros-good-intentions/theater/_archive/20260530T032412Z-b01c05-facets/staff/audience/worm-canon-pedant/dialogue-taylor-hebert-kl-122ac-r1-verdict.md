---
reviewer: worm-canon-pedant
character: taylor-hebert-kl-122ac
chapter: b01c04
facet: dialogue
protocol: V2+V3
date: 2026-05-27
verdict: accept
signal-findings: 1
hard-findings: 0
---

# worm-canon-pedant — dialogue verdict: taylor-hebert-kl-122ac (b01c04)

---

## Scope

Shipped dialogue file: `active-project/theater/dialogue/taylor-hebert-kl-122ac.md`, c04 section.
One shipped entry: ID 4 @7.
Entry ID 5 (@9, work-naming + first-interval) was dropped pre-ship per DEC-0030 (bone consolidated away; utterance authored against a bone the chunk-contract did not mandate). Out of scope — not on disk as a shipped entry.
Sidecar reviewed: `active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`, R1 entries for anchors @7 (entry 1 in sidecar) and @9 (entry 2 in sidecar — drop-documented, not reviewed for verdict).
Proto-lines anchor verified: b01-c04.md @7 carries `[taylor-hebert-kl-122ac:4]`. Resolves correctly. @9 carries no Taylor citation (consistent with drop).

---

## Stage 1 — V2 Strict Affirmative-Demonstration

### [dialogue:4] @7

Line: "Yes. The terms hold with two changes. You will have patterns — what moves through the streets, what does not, where the seams sit — not raw report of who said what to whom. The interval is mine to set. The volume is mine to set."

**Q1 — Affirmative card-signature demonstration:**

That tracks.

The "Yes." opener is the receipt-confirmation shape from base card §Direct-samples. Clean. The em-dash insertion specifying the deliverable ("what moves through the streets, what does not, where the seams sit") is the sensory/tactical specification structure — base card §Cadence, correctly applied. The parallel closer ("The interval is mine to set. The volume is mine to set.") is the possession-of-parameter register, identical syntactic shape, no connective — base card §Syntax parallel-structure for stacked observations, and directly descended from the base-card §Direct-samples voice-tell ("We'll need time to think about it. ... 'Need' not 'want.'" — possession mode, not preference-mode).

What I track specifically: the line is descended from canon Taylor, not imitating her. She names what she will deliver and who owns the parameters. She does not explain why she named those parameters. She does not gesture at what the arrangement costs her or what she is trading. She does not make the reader notice she is being strategic. That restraint is the card, and it is affirmatively present in this line. Nothing in this utterance could sit in Jarvis's mouth without sounding wrong.

Q1: PASS.

**Q2 — Card not violated:**

Earth-Bet proper-noun scan: clean. PRT, Skitter, Brockton Bay, Gold Morning, Khepri, the full canonical hard-fence list — absent. PASS.

Insect-mechanism Earth-Bet jargon: "patterns — what moves through the streets, what does not, where the seams sit." Indirect referent. The fence holds. A competent Westerosi street operative could make this deliverable claim without possessing Taylor's actual capability. The ambiguity is maintained throughout the line; the power stays below the surface. PASS.

Anachronism scan: absent. No okay, yeah, fine, sure, alright. PASS.

Contractions: none. "You will have," "is mine," "does not." Uncontracted throughout. Adult-facing Westerosi formal register per behavior card §Vocabulary Refuses. PASS.

Rhetorical questions: absent. Motivation clauses: absent ("because," "so that," "in order to" — all absent). Apology language: absent. Worm-canon-snark (dry-humor closer, Lisa-cadence aside, Skitter-vintage punchline): absent, correctly so — the moment is the formal acceptance of an arrangement that will end badly; any dry humor would be register-wrong. PASS across all scan dimensions.

Mask-register check: the sidecar deploys the adult KL-122ac instruction-register, not the eleven-year-old child-deferent mask. The line holds that register without softener-leak. No "ser," no "if it please you," no sentence-final child-deferent phrase. No violation of canon-Taylor's cold-utilitarian negotiation voice. PASS on canon-voice grounds.

*Note on card-authority (not a Q2 violation — flag for auditor):* The behavior-card header in the dialogue file reads `taylor-hebert-westeros`. That card's §Register markers define the external/spoken-to-adults register as "child-deferent Westerosi-formal" and states that a long planning sentence delivered aloud to an adult is "a tell — the mask has slipped." The sidecar treats the adult KL-122ac instruction-register as the sanctioned operating mode, not as a slip — referencing "persona card §Voice" for authority. The sidecar's behavior-card-stack is `taylor-hebert-westeros → taylor-hebert (inherits)`, with no separate kl-122ac behavior card listed. The adult register authority is present in the sidecar prose but not in a card section explicitly. This is not a canon-voice violation — the adult instruction-register is squarely descended from Taylor — but the card-authority chain requires sidecar prose to justify a register the cited card does not explicitly sanction as a distinct variant. I flag it; primary resolution lane is auditor.

Q2: PASS.

**Stage 1 verdict: ACCEPT**

---

## Stage 2 — V3 Adversarial Seam-Finding

I reread before emitting clean accepts. Here are the strongest hostile counter-arguments from my lens.

### Seam 1 — Unresolved facet-license citations [SIGNAL]

The sidecar's entry for @7 marks `facet-licenses: [DEFERRED-TO-R2]`. The sidecar was authored R1-blind per Phase 1.5 timing. No R2 resolution is visible in the dispatched sidecar — the sidecar is the R1 drafts file and the deferred citations have not been resolved to concrete `<facet>:<id>` entries.

Per rubric §V2 facet-citation extension, URI-FACETS-CYCLE-1 (2026-05-19): "A sidecar that documents the facet-license axis in R1-blind placeholder form (e.g., 'facet-licenses: [DEFERRED-TO-R2]') and is not resolved at R2 with a concrete `<facet>:<id>` citation is a SIGNAL finding per entry." Citation-completeness is enumerated per entry, not per file. The sidecar's identification of candidate axes (feel @7 for bodily-stillness; state-updates @7 for social_tether-antag +0.5; sensory @7 for the cooper's-yard ambient) does not satisfy the per-entry resolution requirement — it names where R2 should look without confirming the citations resolve on disk.

This is the same class of finding the rubric records from cycle-1 audience convergence: "cape-fic-reader and worm-canon-pedant independently attacked dialogue-coll sidecar's R1-blind placeholder citation."

**[dialogue:4] @7 — SIGNAL: `facet-licenses: [DEFERRED-TO-R2]` — no R2 resolution in sidecar. Candidate axes named (feel @7, state-updates @7, sensory @7) but not confirmed against locked graph. Per rubric §citation-completeness / URI-FACETS-CYCLE-1.**

### Seam 2 — Card-authority chain for adult instruction-register [soft — auditor-lane]

The dialogue file header cites `behavior-card: taylor-hebert-westeros`. The taylor-hebert-westeros card's §Register markers define external/spoken-to-adults as child-deferent Westerosi-formal. The deployed register is adult instruction. The sidecar labels this "adult KL-122ac variant" and reads against "persona card §Voice" — but the cited behavior-card-stack does not contain a kl-122ac behavior card. The card itself knows that adult planning-register surfaces as mask-slip; the sidecar treats adult instruction-register as the sanctioned operating mode.

From my lens: the line is canonically correct Taylor voice. The question is whether the piece knows what rules it is operating by. If the adult register is sanctioned, that sanction should appear in a behavior card section, not only in sidecar prose. If the adult register is a mask-slip being deployed at scale, the surrounding prose should carry that cost visibly. The sidecar claims sanction; the card does not explicitly provide it. Future entries under the same authority chain have a gap in the guard.

This is auditor-lane primary. I note it because card-authority is how I verify the piece knows the rules it is operating by — and clean-seeming authority chains that rest on sidecar prose rather than card text are where future drift enters.

**[dialogue:4] @7 — soft flag: behavior-card header cites taylor-hebert-westeros; card's external register is child-deferent; deployed register is adult instruction. Sidecar prose provides rationale; no explicit card section or kl-122ac card in the stack sanctions adult register as a distinct operating mode. Auditor-lane.**

### Seam 3 — "Ignorance played correctly" check [clean — no seam]

Taylor names "patterns" as her deliverable. The specificity of "what moves through the streets, what does not, where the seams sit" names the shape of pattern-reading but not the mechanism. I tested whether this specificity implies superhuman analytical resolution — whether a Westerosi street operative without parahuman capability could plausibly make the same claim. They could. The claim is specific but not anomalous. The fence holds; the ambiguity is earned.

No seam.

### Seam 4 — Canon-Taylor in constraint-negotiation vs. deployed register [clean — no seam]

Canon Taylor at the negotiation-mode moments that are most comparable (the Coil arrangement, the Travelers détente, the Undersiders-vs-Tagg standoff) operates from cold, transactional, assertion-of-terms, no decoration. She names what she will deliver; she names who owns the parameters; she does not explain why. The deployed line is squarely in that mode. The Westerosi constraint adds uncontracted forms and period-plausible vocabulary without distorting the base register. The descended voice is visible underneath. This tracks.

No seam.

---

## Running tally

| Finding | Class | Anchor | Rubric authority |
|---------|-------|--------|-----------------|
| Facet-license citations unresolved from DEFERRED-TO-R2 | SIGNAL | @7 | rubric §citation-completeness / URI-FACETS-CYCLE-1 |
| Adult instruction-register not explicitly sanctioned by cited behavior card | soft / auditor-lane | @7 | rubric §hard fences §behavior-card-compliance |

Strong seams: 0
SIGNAL findings: 1
Hard findings: 0
Clean reads: voice-register (descended from canon Taylor), lore-fence (indirect referent held), Earth-Bet scan (clean), anachronism scan (clean), contraction check (clean), motivation-clause check (clean), lore-leak check (clean), canon-personality check (clean), Q1 affirmative demonstration (present)

---

## VERDICT

**ACCEPT**

One SIGNAL finding (facet-license citations unresolved from R2 placeholder status). One soft flag (card-authority chain, auditor-lane). No hard findings. No canon-personality violation. No lore leak. No Earth-Bet contamination. No power-mechanics overreach.

The line is canonically descended Taylor — cold, transactional, assertion-of-terms, no decoration, no motivation-talk. The indirect-referent fence for the bug-feed capability is maintained. The possessed-parameter register ("is mine to set") and the receipt-confirmation opener ("Yes.") are affirmative card-signature demonstrations.

The SIGNAL routes to R2 dialogue-judge: resolve concrete `<facet>:<id>` citations for entry 4 @7 against the locked graph. Candidates from the sidecar: feel @7 (bodily-stillness hold), state-updates @7 (social_tether-antag +0.5 axis-move capture), sensory @7 (cooper's-yard ambient at first bell). Each candidate must resolve to an entry on disk at the named anchor; walk-failure is HARD per entry.

The soft card-authority flag routes to auditor: confirm that adult KL-122ac instruction-register is explicitly sanctioned by a behavior card in the stack, or that the taylor-hebert-westeros card's "mask-slip" category is the intended frame for this deployment and the surrounding prose carries that cost.

Wiki tab stays open. Keep reading.
