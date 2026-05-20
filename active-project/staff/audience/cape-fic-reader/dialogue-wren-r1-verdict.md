---
reviewer: cape-fic-reader
facet: dialogue
character: wren-stitch-maker-flea-bottom-ward
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: accept
---

# Verdict reasoning

## Stage 1 — V2 strict

**Entry 1 — @23** "You walked the block three times this morning. Mistress Coll knows your name and you've not been here a fortnight."

Q1 (affirmative demonstration): The line demonstrates the card's pattern-noticer signature without hedging or asking. She names two discrete data points — the route-pattern and the social-recognition — and lets the implication sit. The "three times" count is the trained-observer tell. The "Mistress Coll" address is correct smallfolk-register for the trade-elder. This is not merely on-card; it actively shows the reader the information-asymmetry structure: Wren already has a model of Taylor's movements on day one. That asymmetry reshapes the board. Q1: PASS.

Q2 (no card violation): No forbidden vocabulary, no precocious-wise framing, no em-dash + semicolon chassis, no Latinate nominalizations, no Earth-Bet substring, no follow-up question pressed. The fortnight / additive-run-on cadence is correct Westerosi smallfolk. Hard fence 2 (she does not ask the question) is respected. Q2: PASS.

**Entry 1 verdict: ACCEPT**

Q1 + Q2 both pass. The line is earning its anchor slot — it opens an asymmetry the reader can track.

---

**Entry 2 — @26** "The flies were on the meat-stall and they were not on your hand. The stall is closer."

Q1 (affirmative demonstration): She names the absence-comparison — where the flies were NOT — and stops. She does not ask why. "The stall is closer" is the child-precision close: she is counting proximity, not theorizing capability. This is the witness-vocabulary card signature in its most load-bearing form: the reader can see that she has observed something that should not be observable by a child without framework, and she has reported it flat. The information-asymmetry stakes go up. This line does the structural work the drafts sidecar claims. Q1: PASS.

Q2 (no card violation): No forbidden vocabulary. No hedge. No follow-up question. Smallfolk register ("meat-stall"). Additive flat sentences. No em-dash + semicolon. The critical Q2 test: does she demonstrate insect-network awareness that a Flea Bottom child should not have? No — she reports a comparison (the stall is closer, the flies were not on you). She is naming proximity and absence, not capability or network-knowledge. The insect-network prohibition is not tripped because she does not know what she is seeing. She sees absence-of-flies-where-the-warmer-food-source-is-closer and reports it. A Flea Bottom child who spends time near a meat-stall knows flies go to meat. She is naming the anomaly in that ordinary knowledge, not revealing Taylor's power mechanic. Hard fence 2 (does not press for cause) is respected: "The stall is closer" is the observation that closes the statement, not a question in disguise. Q2: PASS.

**Entry 2 verdict: ACCEPT**

Q1 + Q2 both pass. The line escalates the asymmetry correctly.

---

**Per-entry summary:** 2/2 ACCEPT.

**File-level verdict: ACCEPT**

---

## Stage 2 — V3 adversarial seam-finding

This reviewer's hostile lens: information-asymmetry integrity and who-knows-what-when coherence.

**Seam 1 — @23: Coll recognition as a knowledge vector.**
The strongest attack here is on "Mistress Coll knows your name." Wren is telling Taylor that a named block-fixture already knows Taylor. This is information Wren has that the reader should verify Wren could plausibly have — and she could. She is on this street, she knows the block-fixture as a neighbor-figure, she would know if Coll had addressed Taylor by name. This is not a lore leak. The seam closes on inspection.

**Seam 2 — @26: The "stall is closer" line as capability reveal.**
The genuine hostile reading: a reader who knows the insect-network power mechanic could read "the flies were not on your hand" as Wren demonstrating she has noticed a capability signature, which the task prompt identifies as the threshold-tripping moment for Taylor at @27. The question is whether the line itself leaks insect-network-awareness or merely reports an empirical observation. On close reading it does not leak: "the stall is closer" is the child's naive explanation for why the absence is notable — she is saying flies normally go to the nearest food, so the fact that they were not on the closer hand is strange. She is working from ordinary cause-and-effect about insects (meat draws flies; close things draw flies more than far things), not from knowledge of Taylor's capability. The seam is real — this line is the one moment that could be read as precocious insect-knowledge — but the specific phrasing anchors it in proximity-logic that an eleven-year-old near a Hook meat-stall would have. The seam is closable without revision.

**Seam 3 — facet-citation completeness (the open wound).**
The drafts sidecar carries `facet-licenses: [DEFERRED-TO-R2]` on both entries. The rubric (§V2 facet-citation extension) is explicit: citation-completeness is a hard requirement at audit; a sidecar with R1-blind placeholders not resolved at R2 is a SIGNAL finding per entry. The cite-index shows:
- @23: co=[vibes:18, wren-stitch-maker-flea-bottom-ward:1, state:20] — wren-dialogue:1 is the back-citation; vibes:18 (@23, "first-question-seeds-the-silence") is a direct license; state:20 (@23, social-engagement not-engaging → engaging-taylor) fires at the same anchor.
- @26: the cite-index carries NO dialogue entry at @26. Wren's second speech has no `co=` entry in the cite-index at @26. The feel:2 and feel:3 entries fire at @27 (Taylor's hand-stop), not @26. The vibes:21 fires at @27. The @26 anchor is bare in the cite-index except for what the dialogue file itself provides.

The sidecar's R2-deferred facet-license placeholder for entry 2 (@26) faces a harder resolution problem than entry 1: the cite-index walk at @26 finds no co-firing facet entries to cite. The auditor's Phase 5 report (fault-001) is specifically about state-updates but the pattern is the same: a deferred citation that, when the cite-index is walked, finds no co-firing license to cite. This is the seam the auditor's SIGNAL S-015 (if carried forward) would name — the @26 anchor is effectively bare, and the dialogue file's own entry is the only decoration on it. The facet-license citation for entry 2 will require the dialogue-writer to either claim a vibes:20 license (which fires at @25, one beat prior, not @26) or acknowledge that the @26 anchor has no co-firing license entry.

This seam does not change the Stage 1 verdict (it is a citation-completeness issue, not a Q1/Q2 failure) but it is the adversarial pressure point: if the R2 walk cannot resolve facet-licenses for entry 2, the sidecar will carry a SIGNAL finding at audit.

# Entry-level callouts

`[dialogue:wren:2 @26]` — The @26 anchor is bare in the cite-index. When the R2 dialogue-writer walks the cite-index to populate `facet-licenses:`, no co-firing entry resolves at @26 (feel:2 and feel:3 fire at @27; vibes:21 fires at @27; state:20 fires at @23). The entry's structural weight is high (this is the threshold-tripping line) but the cite-index walk will return no co-citation. The R2 dialogue-writer must either: (a) argue that vibes:20 @25 (atonement / prohibition-holds-through-child-question) licenses the @26 slot as the beat that produces the @27 somatic response — a one-beat-offset license with documented rationale; or (b) flag that @26 is a bare anchor and the dialogue entry is the sole decoration, which is structurally permitted but must be documented to avoid SIGNAL escalation.

# Convergence trace

- S-015 (if it exists in the 15 carried-forward signal findings) or equivalent: facet-citation-resolution failures at specific anchors — the @26 bare-anchor problem here is the same class as the cycle-1 lesson named in the rubric (feel:2 @22 mis-resolved to @21). Auditor finding pattern: CONSTRAINT § citation-completeness per entry, SIGNAL per entry where facet-license is deferred and the cite-index walk fails to resolve.
- Auditor fault-001: state-updates rubric-carve-out absent — unrelated to dialogue directly, but demonstrates the same pattern of deferred documentation that the drafts sidecar's R2-deferred placeholder exhibits. The audience's callout at @26 is the dialogue-equivalent of fault-001: a gap that the mechanical scan will eventually surface.
