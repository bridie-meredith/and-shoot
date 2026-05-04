# Coach Tuning Harness — Pulp-Enthusiast Failures
## Project: taylor-hebert-westeros | Episode: s01e01

Pulp-enthusiast's hot buttons:
- Slice-of-life filler when the plot is live
- Offscreen threats with offscreen consequences
- Three paragraphs of agonized decision-making
- Vague consequences
- One complication per scene with padding around it

The persona accepts: escalation, board-worsening, tactical moves that work unexpectedly, on-screen cost.

---

## Pattern 1 — Interior-inventory opening (bullet 1)

**Bullet:** [STUDIO scene open — Taylor in sickroom, septon dying, morning light]

**What failed (attempts 1–2):**
- Attempt 1: Fear rendered as compulsive cataloguing. "Information-gathering was the only way she knew how to be afraid." → REJECT. Static internal loop. Nothing external registered.
- Attempt 2: "Through the three beetles... the morning was cold and entirely uninterested." → REJECT (also wcp-rejected for fauna mechanics). No board change. Slice-of-life.

**What worked (attempt 3):**
"The sound from the next room was worse. She knew it before she was fully awake — the wet pull of it, the catch and the not-quite-release — and she had the bowl in her hands and was moving before she had decided to move."

**What changed:** Entered through the external threat (the worsening breathing), not through her interior state. Body-in-motion before thought. The threat registers as a board change (worse than yesterday). "She was moving before she had decided to move" — the reflex carries the urgency pulp-enthusiast needs.

**Coach rule:** Opening lines in a slow scene must register something that is WORSE than it was before the line began. The board change does not need to be large — it needs to be visible. Worsening breathing, a clock starting, someone doing something that cannot be undone.

---

## Pattern 2 — Domestic action with interior reflection (bullet 2)

**Bullet:** taylor-hebert-westeros sets a clay cup of water on the floor beside the pallet

**What failed (attempts 1–3):**
- Attempt 1: "Through the beetles... the morning was cold and uninterested." → REJECT (fauna mechanics + no escalation)
- Attempt 2: Careful geometry of cup placement + census math running underneath. → REJECT. Re-describes what we already know. No new information.
- Attempt 3: Every reflex for being watched un-deployed, holding very still, "he was looking at her." → REJECT. Interior inventory. Three-part analysis of what she didn't do.

**What the final NEEDS_EDIT line was:** She didn't deploy her reflexes, he was looking at her. Dark-fantasy-reader and worm-canon-pedant accepted. Pulp-enthusiast rejected all three attempts.

**Diagnosis:** This bullet is structurally incompatible with pulp-enthusiast in isolation. The action (setting a cup down) is a domestic care beat with no escalation available inside it. The escalation is in the septon's eyes finding her — but that belongs to bullet 3's setup, not this action. Coach cannot manufacture board-change where the bullet has none.

**Coach rule for this pattern:** When a bullet is a pure domestic action with no internal escalation (object placement, care gesture, maintenance task), check whether the *consequence of the action* is visible in the same line. If the cup placement causes him to stir, that's a board change. If she sets the cup and he's already looking at her, that's a board change. Without a consequence, this bullet type will fail pulp-enthusiast regardless of prompt quality. Flag it.

**Recommended prompt strategy:** Combine the action with its immediate physical result. "She sets the cup. He hears it. He turns." This covers bullet 2 AND bullet 3's setup in a single line — which is technically scope creep but passes the pulp-enthusiast threshold.

---

## Pattern 3 — Information delivery by a dying character (bullet 3)

**Bullet:** septon-dying-protector turns his head toward Taylor and says the census rider came through Millfall yesterday

**What failed (attempts 1–3):**
- Attempt 1: Clean measured delivery. "The census rider stopped at the mill last night... he will be here before the morning office." → REJECT. Pure threat-delivery. Offscreen danger.
- Attempt 2: [Content drift — impersonator changed "census rider/Millfall" to "the maester comes Tuesday."] Physical cost of speaking prominent, but "texture not escalation." → REJECT.
- Attempt 3: Census rider, Millfall, specific time window (terce to midday). Physical cost prominent. → REJECT. "Setup delivery, clock-handoff, not a complication landing."

**What Attempt 3 produced (NEEDS_EDIT):**
"Millfall," Aldric said, and it cost him: his chest lifted wrong, the wet drag in it audible in the pause before the next word came. "Census rider. Yesterday." He stopped, steadied, his eyes finding her face and holding it the way a man holds something he is about to hand over. "By terce if he rode fast. Midday if he did not."

Dark-fantasy-reader: ACCEPT. Worm-canon-pedant: ACCEPT. Pulp-enthusiast: REJECT.

**Diagnosis:** Pulp-enthusiast's rejection is structural to Scene 1 of this episode. A sickroom scene where a dying man delivers a countdown is setup by design — the officer does not arrive until Scene 3. No prompt revision will satisfy "board-worsening right now" when the board is functioning correctly as dramatic setup. The three failures are not coach failures — they are persona-structure mismatches.

**Coach rule for this pattern:** When the scene is doing legitimate dramatic work (building toward a payoff in a later scene), and pulp-enthusiast rejects for "no board change," flag this to the orchestrator as a structural mismatch rather than retrying with the same approach. Attempt 3's line is good prose doing correct setup work. The persona card may need recalibration for scenes before the inciting incident.

---

## Summary: Coach checklist for pulp-enthusiast in audience

Before generating the prompt for each bullet, ask:

1. **Is something visibly worse at the end of this line than at the start?** If not, find what changes and put it at the end.
2. **Is the threat on-screen or off-screen?** Pulp-enthusiast accepts an on-screen cost (a man spending breath to speak, Taylor moving before she decides). Pulp-enthusiast rejects an off-screen threat named in dialogue. If the threat is only in words, make the act of speaking the cost.
3. **Is the action the consequence, or is there a visible consequence of the action?** Setting a cup down is not escalation. Setting a cup down and hearing him stir is.
4. **Is this interior-inventory?** If the character is cataloguing their own fear, defenses, or calculation without any external change, pulp-enthusiast will reject. Redirect: what does the body do, not what does the mind assess.
5. **Is this Scene-1 setup before the inciting incident?** If yes, flag to orchestrator: pulp-enthusiast may be structurally incompatible with this scene. Consider whether the episode plan needs earlier action entry, or whether the persona card needs a "legitimate setup beats" exception.

---

## Content drift note (septon bullet 3)

Impersonator drifted "census rider came through Millfall" (the bullet) to "the maester comes Tuesday" (different plot beat). Coach prompt did not quote the bullet verbatim as an anchor. Fix: always include the verbatim bullet text at the top of the prompt as a hard constraint: "The line must contain [exact information from bullet]. Do not substitute."
