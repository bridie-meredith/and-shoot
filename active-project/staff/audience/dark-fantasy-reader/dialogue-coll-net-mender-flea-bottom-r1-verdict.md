---
reviewer: dark-fantasy-reader
facet: dialogue-coll-net-mender-flea-bottom
cycle: 1
episode: b01c01
date: 2026-05-23
verdict: revise
---

# Stage 1 — V2 strict

- entry 1 (@8): Q1 **fail** §citation-completeness / §affirmative-demonstration; Q2 **pass**; verdict: **REVISE**.

Q1 reasoning: The sidecar claims three card-signatures from §Voice — "offer work without asking," "flat delivery," "short sentences for observations" — and they are plausibly demonstrated in the line's surface. However, the required second citation axis (facet-licenses) is structurally broken. The sidecar cites `exposition:2 @4` as the facet-license, but exposition:2 fires at @4, not at @8 where the speech-act lands. A cross-bone citation four protolines upstream of the speaking anchor is not a co-fire at the anchor; it is a prior-context gloss. The rubric (CONSTRAINT § citation-completeness) requires that the facet-license citation resolve to an entry whose proto-anchor matches or is co-incident with the speech anchor — not an arbitrary prior bone on the same character. The cite-index confirms this: exposition:2 @4 is a lonely entry with back=Y but no co-citations and no dialogue entry at @4. The @8 anchor has no co-located lens facets beyond the dialogue citation itself. The sidecar's R2 resolution note explicitly acknowledges that loc-state:4 @11 was rejected as a cross-scene citation and replaced — but the replacement (exposition:2 @4) is still a cross-anchor citation, merely a closer one. The rubric's citation-resolution rule ("a citation that names an anchor where the cited facet does not fire" → HARD per entry) applies here: exposition:2 fires at @4, not @8. The facet-license axis is unresolved at the speaking anchor. Q1 fails on the citation-completeness axis.

Q2 reasoning: No Earth-Bet proper-noun hits. No forbidden vocabulary detectable without the physical card file (which does not exist at `cards/dialects/coll-net-mender-flea-bottom.card.md` — the file was absent from disk). The behavior card absence is itself a structural problem (cannot confirm §hard fences), but the surface of the line — "There's mending if you can hold a needle." — shows no anachronistic register, no HR-speak, no deposition cadence, no nominalizations. Q2 passes conditionally on the surface; cannot fully confirm without the card.

---

# Stage 2 — V3 adversarial (dark-fantasy lens)

- entry 1 (@8): The line does not smell like Planetos. It smells like generic medieval-labor-offer NPC.

The hostile seam: "There's mending if you can hold a needle" is a competent flat offer and the sidecar is correct that it demonstrates the fixture-not-confidant register at the syntactic level — one clause, no elaboration, capability-gate only. But the dark-fantasy test is not "does this read as flat?" It is "does this carry the weight of this specific slum, this specific economy, this specific city?" The answer is no.

Flea Bottom is a place where people do not ask what strangers are because the knowledge would cost them something — because knowing is a liability in a city where the City Watch sells its silence, where a stranger's provenance can make you complicit. Coll's silence is not incuriosity; it is a survival discipline. The line does not encode that. "If you can hold a needle" is a qualification about physical competence. It is not a qualification that carries the slum's logic — the offer says nothing that distinguishes Coll from a net-mender in any medieval fiction. There is no texture of King's Landing superstition, no embedded cost (the offer is given as freely as air), no trace of the economic calculus that makes a fixture-not-confidant different from a generous bystander.

The world is not pushing back in this line. The offer arrives with no friction. For this reader, that is the seam: the line earns the card-register (flat, short, no social bid) but does not earn the setting. Generic medieval-NPC inflection.

Secondary seam: The behavior card cannot be verified — the card file does not exist on disk at the cited path. This means the §Voice citations in the sidecar are self-referential (citing a card the reviewer cannot read). The Q1 claim cannot be fully validated, which in hostile-default mode is a fail condition.

---

# Verdict reasoning

The line is syntactically on-card and passes the surface Q2 scan, but the facet-license citation is a cross-anchor near-miss (exposition:2 fires at @4, not @8), the behavior card does not exist at the path the sidecar cites, and the line itself carries no Planetos-specific weight — it is a flat medieval-labor offer that could belong to any slum in any city. The card-register is demonstrated; the setting is not. For a world that should cost something to stand in, this offer is free.

---

# Entry-level callouts

- [coll-net-mender-flea-bottom:1] @8 — facet-license citation resolves to exposition:2 @4, a different protoline anchor; the @8 speaking bone has no co-located lens facets and no in-anchor facet-license; citation-completeness fails at the entry level per rubric CONSTRAINT § citation-completeness (cross-bone citation ≠ co-fire at anchor). Missing behavior card file at `cards/dialects/coll-net-mender-flea-bottom.card.md` prevents full Q2 §hard-fence verification; Q1 §-section cite claims cannot be audited against source.
- [coll-net-mender-flea-bottom:1] @8 — line carries flat-factual card-register but no Planetos-specific weight; indistinguishable from generic medieval-labor-offer NPC; fixture-not-confidant survival logic (silence-as-liability-management in a city where knowledge implicates) is absent from the utterance's surface and from any co-located facet at @8 that would carry it adjacently.

---

# Convergence trace

- fault-013 (auditor): exposition:1 licensed-by form gap (cape-fic-reader attestation not in-file). Not directly overlapping, but the same citation-form discipline failure: sidecar facet-license citing a non-co-incident anchor mirrors the pattern the auditor flagged at the exposition licensed-by level.
- fault-016 (auditor): scene-C approach zone atmosphere thin; @8 is scene-A and this finding is scene-C, but both share the same root pattern — anchor beats with thin co-located facet coverage leaving the dialogue line without cross-facet texture.
- CONSTRAINT § citation-completeness (rubric, not a specific auditor fault-ID): the rubric's per-entry citation-completeness rule (missing both axes = HARD per entry; missing one = SIGNAL per entry) is directly implicated. The auditor's URI-FACETS-CYCLE-1 note (promoted from prior audience-gate) names this exact pattern — cross-anchor citation that does not survive per-entry verification. This verdict converges with that promotion path: the audience attack confirms the citation-resolution failure the rubric's CONSTRAINT class names.
- Behavior-card absence: no auditor finding covers the missing card at `cards/dialects/coll-net-mender-flea-bottom.card.md` — this is an independent finding with no auditor overlap.
