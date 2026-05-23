character: taylor-hebert-kl-122ac
episode: b01c01
r2-layer: R2.6 dialogue judge
run-mode: adversarial-low-volume (one-line POV speaker; Q1/Q2 strict)
cite-index-hash: c9d9284f144d447503712cabdad2b985e60c03d16234c1821562fac039c8113c
generated: 2026-05-23
---

# R2.6 dialogue decision-shard — taylor-hebert-kl-122ac — b01c01

## Inventory

| id | anchor | utterance | decision |
|----|--------|-----------|----------|
| 1  | @25    | "There's no work here. Go on."          | REWRITE (delete + new id 2) |
| 2  | @25    | "Nothing for you here. Go on."          | NEW (R2 replacement for id 1) |

Pre-R2 fires: 1. R2 deletes: 1 (REWRITE delete-component). R2 adds: 1 (REWRITE add-component). R2 net fires: 1.
ADD-cap usage: 0/3 (REWRITE does not consume add-cap).
Earth-Bet proper-noun hits (utterance + objective): **0**.
Sidecar-absent-flag: **TRUE** (R1 did not produce taylor-hebert-kl-122ac.drafts.md; R2 authored forward; see SIGNAL in drafts sidecar).

## Per-entry decision rationale

### Entry id 1 @25 — "There's no work here. Go on." — DECISION: REWRITE

**Q1 (affirmatively demonstrates ≥1 card signature on Westerosi variant):** FAIL.

The line carries base-card §Cadence (period over exclamation; trailing fragment "Go on.") and base-card §Direct samples register (deferral / minimum-surface refusal echoing "We'll need time to think about it"), so it is technically on-card-as-base. But the role brief and Q1 strict require affirmative demonstration on a **Westerosi variant signature** — "her speech here is Flea Bottom register, not Earth-Bet first-person tactical chassis — she's masking." The contracted expletive-subject opening "There's" is the most Earth-Bet-coded surface in the line; it is the chassis-marker that would let this utterance pass verbatim in a contemporary Earth-Bet scene with no register-shift. The kl-122ac variant card §Voice explicitly modifies the base: "She has the working vocabulary of the streets but the accent is wrong in a way no one can place." The R1 line does not surface the variant — neither in vocabulary (no Flea-Bottom-adjacent term), nor in syntax (uses Earth-Bet base contraction), nor in idiom (no Westerosi anchor). Inoffensive ≠ on-card (v1 V2 rubric, copied into rubric §Q1).

**Q2 (no card-§ violations):** PASS.

No Earth-Bet proper noun in utterance or objective. No em-dash + semicolon chassis (AP1 chassis-contamination). No forbidden vocabulary (no *okay, fine, yeah, hi, bye, sure, alright*; no analytic-vocabulary; no HR-speak; no deposition cadence). No nominalization. No monument-naming violation. Hard fences clean.

**DEDUP check:** No facet fires at @25 per cite-index (bare proto-line). DEDUP does not fire. Per rubric §discipline: "Her one line at @25 is a deflection (minimum-surface), not interior — DEDUP should not fire" — confirmed.

**Decision logic:** Per rubric §R2 differences, REWRITE = "internal mini-V3 surfaces a closable seam; revised draft cites different facet license or different §-section." The Q1 fail on Westerosi-variant signature is the closable seam: the board-move is correct, the register-anchor is missing. Revise rather than delete; the speech-beat at @25 is required by the chapter substance (s03n04: "Taylor's deflection ('There's no work here. Go on.') is a speech-act that confirms: no name given, no claim made, no information exchanged; the deflection is the operating rule's surface response"). Deleting without replacement would leave the rule's surface action mute at the beat the substance contract designs for it.

Per rubric §Edits: "If a rewrite is needed, the entry is deleted and a new entry with a new ID replaces it." Id 1 deleted; new id 2 issued at the same anchor.

### Entry id 2 @25 — "Nothing for you here. Go on." — DECISION: NEW (R2 issue)

**Q1 (affirmatively demonstrates ≥1 card signature on Westerosi variant):** PASS.

Affirmative demonstration cited (multi-axis):
1. **taylor-hebert §Syntax** — Subject-implied opening. "Nothing for you here" drops the expletive subject ("There is/are") and opens on the noun phrase. This is one of the base card's named signatures: "Many lines start with a noun phrase rather than a pronoun. 'The anchor is compromised.' 'The chain-ring.' 'Coffee.' She drops the pronoun when the topic-noun does the work."
2. **taylor-hebert §Cadence** — Fragments are intentional. "Go on." is a two-word imperative fragment, in the canonical pattern with "Status." / "Dark." / "Coffee." Trailing fragment ending on the load-bearing verb-phrase, not on a softener.
3. **taylor-hebert §Direct samples** — "We'll need time to think about it" deflection-by-precision pattern: the line says no without saying no; closes the exchange without naming the closure. "Nothing for you here. Go on." is the same move at lower register-height (street, not negotiating-table).
4. **taylor-hebert-kl-122ac §Voice (KL modifications)** — "She has the working vocabulary of the streets but the accent is wrong in a way no one can place." The line is plain in the street register; the *absence* of any Westerosi-idiom-anchor (no *aye, ser, lass, m'lady, mayhap*) is the deliberate non-performance prescribed by the variant card. She has the vocabulary but not the idiom — exactly the doubled register the variant card describes.
5. **taylor-hebert-kl-122ac §Voice (forbidden registers)** — No theme-narration, no naive-register, no Earth-Bet proper noun, no Skitter/Khepri self-identification, no road-to-hell meta-view. The minimum-surface deflection is in-bounds across all card-§ forbidden lists.

**Q2 (no card-§ violations):** PASS.

Re-tested per rubric §Hard fences and §Audit classes:
- Earth-Bet proper-noun scan (utterance + objective): clean (0 hits).
- AP-SCAN (em-dash + semicolon chassis on non-Taylor speakers): not applicable — speaker IS Taylor; base-card §Cadence em-dash usage is licensed for her chassis but is NOT in this utterance regardless.
- AP-SCAN (modern HR-speak in Westerosi register): clean.
- AP-SCAN (deposition cadence in non-administrative speakers): clean — fragments + imperative, not deposition-build.
- AP-SCAN (nominalizations substituting for plain English): clean — "Nothing" is a pronoun in this construction, not a nominalization; "Go on" is verb-particle.
- Forbidden vocabulary per westeros-smallfolk §Refuses to say (read for cross-contamination check): no *okay, fine, alright, yeah, sure, hi* (which would be the chassis-contamination this card warns against). She does not pick up smallfolk idiom either (she is not smallfolk; her cover is foreign-woman-with-street-vocabulary).
- Monument-naming: no monuments named (correct register for deflection-beat).
- POV §Voice tells (taylor-hebert): "Pause habits. When she pauses inside a line of dialogue, it's because she is choosing the next word, not because she is hesitating. The reader should feel the cost of the choice." The sentence-break between "Nothing for you here." and "Go on." reads as the cost-of-choice pause: she could have stopped after one sentence; the second sentence is the closure she chose to add. Both sentences are short; the gap is the pressure.

**Facet-license resolution (per rubric §V2 facet-citation extension URI-FACETS-CYCLE-1):**

Three citations, all resolving in locked graph (cite-index hash c9d9284f...):
- `state-updates-taylor-hebert-kl-122ac:5 @20` — file present; entry 5 fires at @20 (day-close knowledge state). Resolves.
- `interest-narrator:5 @24` — file present; entry 5 fires at @24 (the held assessment surfaces). Resolves per cite-index `narrator:5 @24 back=Y`.
- `vibes:9 @27` — file present; entry 9 fires at @27 (the deflection landed; Wren not filed). Resolves per cite-index `vibes:9 @27 back=Y co=[feel:3, vibes:10] lic-out=[feeling:3, proto:27]`.

All three citations pass the rubric's resolution gate ("Every facet-licenses citation must resolve to an actual entry on disk — a citation that names an anchor where the cited facet does not fire (cite-index walk fails to resolve) is HARD per entry.").

### Refusals (ADD-considered, REFUSED): @26 + @27

Two anchors in scene C are non-speaking Taylor-POV beats where an R2 ADD was considered and refused under the ≤3 ADD-cap. Both refusals rest on base-card §Voice tells citations:

- **@26** (wren-...-ward speaks; the flies-not-on-Taylor payload): adding a Taylor reaction-utterance here would force speech into the chapter's payload moment. taylor-hebert §Voice tells "the held silence after a question" — "When asked something she does not want to answer, she does not deflect or hedge — she goes silent. The silence stretches past the conversational threshold; she lets it. The interlocutor either fills the silence or moves on. She does not." Wren's flies-observation is precisely such a question (named-observation-without-the-follow-up-question per wren drafts sidecar entry 2 @26). Taylor's register-correct response is silence; the chapter substance s03n06 @27 explicitly makes the held-eyes the rule's catch. ADD REFUSED.

- **@27** (taylor-hebert-kl-122ac holds the eyes; the closing held bone): the rule catches and closes mid-cycle per s03n06. taylor-hebert §Voice tells "Refusal to look directly" — "Certain topics… appear in the prose as gaps. The narration moves around them. When she does name them, the reader should mark the moment because the cost of the naming is part of the line." Speaking at @27 would constitute naming what the rule has just refused to file. The held-eyes IS the register; the silent face IS the line. ADD REFUSED.

The chapter substance is structurally designed for one Taylor speech beat in scene C (s03n04 @25 only); R2 does not exceed the substance's speech-budget. ADD-cap: 0/3 consumed.

---

## SIGNAL — sidecar-absent-flag

R1 dialogue-writer fork for taylor-hebert-kl-122ac did not produce a drafts sidecar at `active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`. Wren and Coll drafts sidecars exist (the same R1 run produced both). Per rubric §Files: "Drafts sidecar: active-project/staff/dialogue-writer/<character-slug>.drafts.md — multi-draft + chosen-mark + rejection notes + card-signature citations + facet-license citations. Audit reads this for CONSTRAINT § citation-completeness." Absent sidecar = absent multi-draft + chosen-mark + rejection notes + card-signatures + facet-licenses for the one R1 chosen entry (id 1 @25). This is a SIGNAL finding under CONSTRAINT § citation-completeness at the entry level (URI-FACETS-CYCLE-1).

R2 has authored the sidecar forward (drafts sidecar Entry 1 carries the analysis that would have lived there from R1 + the R2 REWRITE rationale + the resolved facet-licenses), so the citation-completeness gate now passes per-entry post-R2. The upstream R1 gap is preserved as a SIGNAL for fixer / pipeline audit. Recommendation: fixer should not block on this — R2 has covered the gap forward; the SIGNAL is informational, pertaining to R1 fork hygiene.

---

## Verdict summary

- Decisions: 1 REWRITE (id 1 → id 2 at @25); 0 KEEP; 0 DELETE-other; 0 ADD; 2 REFUSED-ADD (@26, @27).
- Net dialogue entries post-R2: 1 (id 2 @25).
- Q1 + Q2 status post-R2: PASS (id 2).
- Earth-Bet hard-fence scan (utterance + objective across all final entries): 0 hits.
- Citation-completeness post-R2 (CONSTRAINT § citation-completeness URI-FACETS-CYCLE-1): PASS per entry (id 2 has both card-signatures and facet-licenses, all facet citations resolve in locked graph at cite-index SHA c9d9284f...).
- Sidecar-existence post-R2: PASS (authored forward by R2; R1 absence preserved as SIGNAL).
- AP1 chassis-contamination scan (em-dash + semicolon spine that the planetos variant forbids): clean.
- DEDUP check (Taylor POV vs NI / feel / memory at @25): no facets fire at @25 (bare proto-line); DEDUP does not engage.
- ADD-cap consumption: 0/3.
- Per-anchor cap: 1/3 at @25.

**Headline:** R1 sidecar absent + R1 utterance Q1-failed on Westerosi-variant signature; R2 rewrote the @25 deflection from "There's no work here. Go on." to "Nothing for you here. Go on." (drops Earth-Bet chassis contraction, surfaces base-card subject-implied-opening signature, preserves minimum-surface board-move) and authored the missing sidecar forward.
