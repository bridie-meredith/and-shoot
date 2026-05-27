---
name: cond-taylor-pov-behavior
class: condition
scope: project
project: taylor-westeros-good-intentions
world: planetos
origin: authored
quality: full
references:
  - cond-earth-bet-noun-fence
---

# Taylor POV Behavior — Authoring Constraints (Series-Wide)

## Description

Series-wide authoring constraints for Taylor Hebert's POV. Governs register, POV scope, interiority rules, and the theme-silence constraint. These are production rules — they apply to every agent authoring Taylor's voice, interiority, or scene-level perspective. Load this card for any scene written in Taylor's first-person POV or any scene where Taylor is the POV lens.

## Sensory Impact

None. A behavior constraint card. Its expression is the quality of prose in Taylor's POV: compressed, analytical, morally precise, and without authorial theme-narration rising above the character's own perspective.

## Duration

Persistent across all chapters.

## POV Scope — First Person Only

**This project is first-person Taylor POV throughout.** Taylor's voice is "I" — not close-third, not omniscient, not limited-third. Every chapter defaults to first-person Taylor.

**Layer scope.** "First-person throughout" applies to **rendered prose** — the chapter draft delivered by `/and-stitch`. Planning chunks (scene chunks authored by `/and-substance chapter`) are conventionally written in third-limited named-subject form ("Taylor walks," "She does not review") for screen-writer clarity; this is pipeline convention, not a POV violation. Bones (authored by `/and-write`) use third-person-named-subject SVO form by mechanical design. The first-person transformation is the responsibility of `/and-write` Phase 1 (which works in named-subject SVO) and `/and-stitch` render phases (which produce the final first-person prose). Chunk-layer and bones-layer third-limited form is NOT a POV violation.

**Non-Taylor chapters:** Permitted only as marked interludes. The default expectation for this single-book project is no interludes unless `cond-kl-court-state-122ac` or substance planning escalates a reason. Any chapter not explicitly marked as interlude is Taylor first-person. An unmarked non-Taylor POV chapter is a structural violation.

**Maester-chronicler coda:** The coda is not a POV chapter — it is a register-break, a different document arriving at the book's close. It is not governed by the first-person rule because it is not a narrative POV; it is an archival voice. Governed separately by `cond-maester-chronicler-voice`.

## Register — Cold-Utilitarian

**The primary register:** Cold, functional, analytical. Taylor's inner voice organizes experience into threat-maps, resource-assessments, and operational sequences. She does not narrate feeling before narrating what is happening; she narrates what is happening and what to do about it, and feeling is present in the gaps.

**What cold-utilitarian is not:** Affectless, robotic, or dissociated. Taylor has emotions. They surface in the prose as brief legible signals — the body-register of cold, fear, grief, anger — before the analytical voice reasserts. Cold-utilitarian means the analytical register is the primary mode, not that emotion is absent. Prose that reads as purely affectless is wrong; prose that is primarily affective rather than analytical is also wrong.

**Compression:** Taylor's inner voice does not over-explain. She does not repeat observations. She does not narrate process if the result can carry the weight. Sentences are load-bearing; sentences that are not are cut. Long subordinated explanations of what Taylor thinks and why belong to a different POV register than this one.

**Pace:** The inner voice moves fast. Taylor's cognition runs at tactical pace. Interior reflection happens in the gaps between action beats, not as extended set-pieces. A paragraph of interior weight is permitted when it is earned. A full chapter of interior processing without external action is a register violation.

## Moral Accounting — Explicit

**Taylor's moral accounting is explicit and systematic in inner monologue.** She tracks the ledger. She knows what each trade costs. She does not suppress the cost; she acknowledges it and proceeds. This is the cold-utilitarian doing its work: she is not a person who commits bad acts without recognizing them as bad. She recognizes them and categorizes them as acceptable costs toward a sufficient goal.

**The ledger is load-bearing for the story's irony.** The reader watches Taylor's ledger — the explicit cost-tracking — and watches it consistently undercount the true cost. Taylor's moral accounting is rigorous within its frame; the frame is wrong. The prose does not correct the frame from above the character's perspective.

**No sentimentality in the ledger.** The moral accounting is not softened by Taylor's emotional responses to the costs she accepts. She knows Nessa is a cost she is not willing to name in her prevention-logic. The prose may show this as an accounting anomaly — the one item she does not put in the ledger — without making it sentimental. The anomaly is the tell; the sentimentality would defuse it.

## Affect — Suppressed, Not Absent

**Affect appears in the prose as brief, specific, physical signals.** Cold in the chest before a decision. The shortness of breath that is not quite fear. The specific weight of recalling Nessa's age. These signals appear and the analytical voice moves on; they do not become dwelling.

**Taylor does not identify her emotions with the labels Taylor understands from Earth-Bet.** She may notice the body-signal without naming it. The reader reads the signal. The naming — "I was afraid" — is rarer than the signal itself.

**Gold Morning weight:** Present throughout. Not as explicit grief-processing but as an underlying texture — the way she measures everything against the scale of what she has already survived, the way her threat-assessments have a ceiling much higher than any Westerosi character's, the way she experiences Westerosi political instability as small relative to what she came from while simultaneously knowing that "small" is relative and the Dance will still kill thousands. This double register (everything here is small; the small things still kill Nessa) is the affect texture of the whole project.

## Theme Silence — Hard Rule

**Taylor does not narrate theme.** The road-to-hell-is-paved-with-good-intentions irony is never voiced by Taylor, never approached as a concept by Taylor, never placed in Taylor's inner monologue as a generalization about her situation. She does not have the meta-view of her own story. She is inside it.

**The prose voice does not narrate theme.** No authorial voice above Taylor's layer comments on the irony of her choices. No narrative framing signals to the reader "this is where she went wrong." The wrong-ness is structural — it emerges from the sequence of events and their consequences, legible to the reader without being announced.

**Applicable scope:** This silence governs both Taylor's explicit inner monologue and the selection of what her POV notices and emphasizes. Taylor's attention in the prose should not be staged to point at the thematic irony. Her attention follows her analytical priorities — what is the threat, what is the resource, what needs to happen next. The irony is visible to the reader in the gap between what Taylor prioritizes and what the story's outcome requires.

## Interaction Notes

**With `cond-earth-bet-noun-fence`:** That card governs what vocabulary Taylor may and may not use (Earth-Bet proper nouns). This card governs the register and structure of her POV. Both must be loaded for any scene-level authoring review of Taylor's voice.

**With `cond-shard-behavioral-weight`:** The escalation bias the Shard imparts is felt in the moral accounting — the consistent slight over-weighting of confrontational options. Taylor's moral accounting is explicit (this card); the Shard makes the accounting reliable but biased (that card). Both must be loaded for scene-level decision-making beats.

**For auditor use:** Flag any chapter not marked interlude whose **rendered draft** (the `/and-stitch` output at `draft/<book>-<chapter>.md`) is not in Taylor's first-person. Do NOT flag scene chunks or bones files for being in third-person named-subject form — this is pipeline convention at the planning and bone-authoring layers; the first-person transformation happens at `/and-stitch`. The auditor's POV check applies to the rendered draft layer only. Flag any extended interior sequence (more than a paragraph) with no external action anchor. Flag any moment where Taylor's inner monologue states or approaches the thematic irony as a generalization about her choices. Flag any scene where affect is absent rather than suppressed — Taylor with no emotional signal in a high-stakes scene is a register violation in the other direction.
