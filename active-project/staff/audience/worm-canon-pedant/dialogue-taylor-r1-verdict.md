---
reviewer: worm-canon-pedant
facet: dialogue
character: taylor-hebert-kl-122ac
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

## Stage 1 — V2 strict affirmative-demonstration

### Entry 1 @25 — "There's no work here. Go on."

**Q1 — Affirmative demonstration of ≥1 card signature:**

PASS — but narrow, and with a specific canon-register note.

The worm-canon-pedant checks: does the voice match source register? Is this clearly descended from the original without being a tribute act?

"There's no work here. Go on." — canon-Taylor's speech register is economical under load, declarative, and refuses follow-up bids when she has made a decision. The two-clause structure (prohibition stated → close given) maps to Taylor's documented reasoning architecture in Worm: she names the constraint, then gives the response that flows from the constraint. That is not a coincidence; it is `leaf §Signature Moves / The second answer`, which the sidecar correctly identifies as the carrying signature.

The specific canon-alignment: in Worm, Taylor's dialogue under operational conditions is consistently terse — short declaratives, no hedging, no warmth performance. "There's no work here. Go on." is within that register. The KL modifications (shorter sentences under insect-feed load, functional descriptions, absent Earth-Bet vocabulary) are correctly enacted. The line does not import any anachronistic speech marker. Q1: PASS.

**Q2 — Card not violated:**

Full fence scan:
- Earth-Bet proper nouns: zero. The sidecar's scan list is comprehensive and the line is clean.
- Parahuman vocabulary (Manton effect, trigger, shaker, master, etc.): absent. "Work" is Common Tongue. "Go on" is Common Tongue.
- Cape names (Skitter, Khepri, Weaver): absent.
- Modern speech markers: the contraction "There's" is the only item worth scrutiny. The sidecar defends it as spoken-street register. Canon-Taylor does contract in spoken dialogue — Worm canon does not hold Taylor to uncontracted formal register in casual street speech. The KL modification toward a more formal register (leaf §Voice / KL modifications) is about Earth-Bet vocabulary absence and the accent, not about prohibition on contractions. "There's" is within range. The uncontracted form would have been equally acceptable, but this is not a violation.
- Theme on-page: none.
- Operating rule named explicitly: none. Taylor does not say "I have a rule about this." She enacts it.
- Multi-shard hijack implication: none. The line makes no capability claim.
- Optimistic register, Lisa-register, Jack-without-subtext: none of these contamination vectors present.

Q2: PASS.

**STAGE 1 OVERALL: ACCEPT** — Q1 demonstrated via `leaf §Signature Moves / The second answer` (Taylor's documented reasoning architecture enacted in spoken form); Q2 full fence clean.

**Critical citation-completeness failure — SIGNAL finding:**

The worm-canon-pedant's tallying mechanism has flagged the following: the drafts sidecar entry for the chosen draft lists `facet-licenses: [DEFERRED-TO-R2]`. Per rubric CONSTRAINT § citation-completeness, URI-FACETS-CYCLE-1, this is a SIGNAL finding. The rubric clause is unambiguous: "A sidecar that documents the facet-license axis in R1-blind placeholder form (e.g., 'facet-licenses: [DEFERRED-TO-R2]') and is not resolved at R2 with a concrete `<facet>:<id>` citation is a SIGNAL finding per entry."

The cite-index resolves the licenses mechanically: `state:17 @25` (co-cited `taylor-hebert-kl-122ac:1` and `vibes:20`) and `vibes:20 @25` (lic-out includes proto:25). Both are on disk with correct back-links. The resolution was not written into the sidecar. This is the same class of failure as the auditor's fault-001 (r2 report) — the annotation was required, acknowledged in the author's own seam notes, and not executed.

---

## Stage 2 — V3 adversarial seam-finding

### Against "There's no work here. Go on." (accepted in Stage 1)

**Strongest hostile counter-argument from the worm-canon-pedant lens:**

The worm-canon-pedant does not attack the line's voice fidelity — that passes. The attack targets the epistemological structure: what does Taylor *know* at bone 25, and does the line's shape match what she knows?

At bone 25, per state-updates entry 17: `social-state.with-wren: unknown-ward → spoken-once`. That is the state delta. Taylor has been running passive insect-sense (interest-narrator entry 5 @22: "a girl comes in through the swarm before she comes in through the door; the entry is filed without a name above the line.") — which means Taylor has already parsed Wren through insect-sense *before* the verbal exchange. Wren is not unknown-ward in the sense that Taylor has no information about her; Wren has already been filed in the insect-feed as an entity, though unnamed.

The worm-canon-pedant checks: does the line's shape respect this specific epistemic state? "There's no work here" — Taylor is framing the response as a statement about the board situation, not about Wren specifically, which is correct for a person who has already assessed Wren via insect-sense and is choosing not to signal that assessment in the verbal register. The line is appropriately impersonal relative to the knowledge state.

"Go on." — is this the right close for someone who has already read this child through 400m of insect-sense before she "enters the street" at @22? Yes, because the operating rule precisely requires that the capability-driven assessment not appear in the verbal register. The line's correct impersonality is a demonstration of the suppression cost, not an error in knowledge representation.

But here is the residual attack: the sidecar's Seam 1 acknowledges a "bone 23 dependency" — the line's force depends on Wren's actual line at bone 23 being a bid for proximity rather than a flat factual ask. The worm-canon-pedant notes that canon-Taylor's reply architecture is highly context-dependent; "There's no work here" as a response to a flat factual question (e.g., "Do you mend nets?") is fine; as a response to a bid for proximity it is the correct second-answer close. If Wren's @23 line (which is a separate dialogue entry in the Wren dialogue file, which this review has not been dispatched to judge) is not in fact a proximity bid, the first clause fails to close what it claims to close. This is a structural dependency the dialogue file for Taylor cannot resolve unilaterally — it requires cross-file verification at the Wren dialogue gate.

The worm-canon-pedant flags this as a seam, not a revise trigger for this entry: the line is internally consistent with what Taylor knows and how she speaks. The dependency is real but lives upstream of this entry.

**Seam verdict:** The line passes the canon-voice gate. The citation deferral is the revise trigger — not voice, not fence. The cross-file Wren-dependency is a flag for the Wren-dialogue review cycle, not this one.

---

# Entry-level callouts

**[dialogue:taylor-hebert-kl-122ac:1] @25 — facet-license DEFERRED-TO-R2 not resolved**
Rubric CONSTRAINT § citation-completeness, URI-FACETS-CYCLE-1 requires concrete `<facet>:<id>` citations at R2. The sidecar remains in R1-blind placeholder state. Resolution: `state:17 @25` + `vibes:20 @25` (both confirmed in cite-index, both back-linked to `taylor-hebert-kl-122ac:1`). Sidecar Seam 4 names the correct licenses but does not execute resolution. This is a SIGNAL finding per rubric; escalates to HARD on cycle-2 if unaddressed.

**Cross-file dependency note — not a callout on this character, flag only:**
`[dialogue:wren:@23]` — the @25 Taylor line's first-clause force depends on Wren's @23 line being a bid for proximity. Verify at Wren-dialogue gate. If Wren's line is a flat factual question, the Taylor sidecar's defense changes shape (deflection-by-non-engagement rather than prohibition-close); line still holds but the claim in the sidecar needs updating.

# Convergence trace

- Citation-completeness failure converges with auditor fault-001 (r2 report): same failure class (annotation required, acknowledged in author notes, not executed in file).
- `state:17 @25` cite-index entry: back=Y, co=[taylor-hebert-kl-122ac:1, vibes:20] — mechanical resolution confirmed, sidecar write only needed.
- `vibes:20 @25` cite-index entry: back=Y, co=[state:17, taylor-hebert-kl-122ac:1], lic-out=[proto:25, proto:27] — mechanically valid license; proto:25 is the @25 anchor.
- Canon-voice note: the two-clause declarative-then-imperative is within Taylor's documented speech register across Worm arcs 1-30; no canon contradiction.
