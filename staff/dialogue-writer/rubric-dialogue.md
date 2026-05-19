# Rubric — dialogue facet

Authority: `schemas/dialogue.schema.md` is the authoritative entry shape. This rubric is the working discipline the R1 + R2 dialogue-writer follows. Evidence backing every clause lives in `design/shoot-v2/round-trip-method.md` and `design/shoot-v2/dialogue-corpus.md` (v1 round-trip tuning on s01e01–s01e06, 2026-05-06).

Distilled from v1 round-trip work; not re-tuned for v2 — lifted into the facet pipeline as-is.

---

## What dialogue is for

Dialogue captures **what the speaker says** at a proto-line anchor — verbatim utterance, in the speaker's voice, on their behavior card's register. The stitcher renders dialogue entries unchanged under their `@<proto-line-id>` anchor; the stitcher edit budget ("and" only) means voice quality is sourced *here*, not recoverable downstream.

Dialogue is one lens among ten. It carries what the other lenses cannot: the speaker's own words. NI captures attention; feeling captures somatic show; memory captures monument-reach; sensory captures world-perception; dialogue captures *spoken board-move*.

### Distinction from adjacent facets

- **NI** (POV-only): what the narrator's attention lands on. Dialogue is what the POV (or any speaker) *says* — separate from what they attend to.
- **feeling**: somatic tell at the anchor. Dialogue may co-fire with feeling; the body bears the cost while the mouth makes the move.
- **memory**: monument-reach. Dialogue may invoke a monument (or refuse to invoke one); the memory facet flags the reach, dialogue carries the speech-act.
- **exposition**: reader-orientation. Dialogue is in-narrator; if a term needs glossing, exposition handles it, not the speaker.

---

## The two-question gate (Q1 + Q2)

Every chosen line must answer both, AND-gated:

- **Q1 — Affirmatively demonstrates ≥1 card signature.** Without this clause, the line is on-card; *with* this clause, the line *demonstrates* the card. Inoffensive ≠ on-card (v1 V2 rubric). The chosen draft must cite which card §-sections it demonstrates.
- **Q2 — Card not violated.** The line must not violate any §forbidden vocabulary, §forbidden cadence, or §hard fence on the card or any card in the composition stack.

V1 lift on this rubric: 40% → 94% (originals → regenerated round-2). Identical rubric across rounds.

---

## Eight writer patterns (load-bearing — v1 round-trip)

These are the *generation-time* disciplines that produced the v1 lift. They are not optional; departing from them recovers the original failure modes.

1. **Per-behavior-card forks.** One fork per distinct behavior card present in the cast. A single fork authors all speakers sharing that card. Cross-contamination prevention is structural — Taylor's chassis bled into every speaker when one writer handled multiple registers.
2. **Card-stack load order, fully read before drafting.** Leaf → `inherits:` parent → universal overlay → `references:` adjacent cards → speaker persona + ltm. Margit composes. Leaf last so per-character voice is the most-recent context the model attends to.
3. **Blind to originals.** Forbidden inputs: show files, source prose, prior dialogue corpus, other R1 facet outputs. Authoring is from intent + cards only. Eliminates paraphrase bias.
4. **Intent specifies state, not text.** Required state fields per beat: board-move (what the line does) + register state (e.g. for Taylor: mask ON / SLIPPING / OFF) + rung within card (functionary vs knight-administrator within noble-courtly) + distance + public-vs-private framing. Text-paraphrase intents collapse back to the original.
5. **Multi-draft + chosen-mark + rejection notes.** 2–3 drafts per intent. Chosen draft marked. Each rejected draft has a one-sentence rejection note. The reviewer tests the *claim* (why this draft, not B/C), not just the line.
6. **Affirmative card-features citation per chosen line.** Chosen draft lists which card signatures it demonstrates, with §-section citations. Becomes the audience's hostile target in V3 seam-finding.
7. **Explicit anti-patterns in every brief.** Project-specific contamination named: em-dash + semicolon spine, modern HR-speak, deposition cadence, nominalizations substituting for plain English. Negative space matters as much as positive.
8. **Calibration anchor per batch.** One intent that maps to a known-strong target. Prevents whole-batch upward drift. v1's anchor was Plumm/NC-4; for v2 dogfood the rule is "highest-tens anchor with all four lens facets fired AND a v1-strong line on the same card."

## V2 facet-citation extension (graph-aware addition)

Chosen drafts cite **both** card signatures AND licensing facet entries:

```
chosen: "Twelve, septon."
card-signatures: §Cadence (clipped reply); §Syntax (vocative-suffix as ward-deference)
facet-licenses: feeling-taylor:7 (somatic tell — held breath at the anchor)
                memory-taylor:3 (monument adjacent — sept-grain count)
```

The slip / register-shift / weighted-monument does not have to land in the surface of the utterance alone — it lands in the slot, with adjacent fired facets carrying co-load. This is the structural answer to v1's open "invisible slip" problem.

**Citation-completeness is a hard requirement at audit (CONSTRAINT § citation-completeness).** A chosen line missing either citation axis is a SIGNAL finding; missing both is HARD.

**Citation-completeness is enumerated per entry, not per file (URI-FACETS-CYCLE-1, 2026-05-19).** Audit enumerates every chosen-mark entry in every drafts sidecar and verifies that BOTH `card-signatures:` AND `facet-licenses:` are populated post-R2 — at the entry's `chosen:` block, not at a file-level summary section. A sidecar that documents the facet-license axis in R1-blind placeholder form (e.g., "facet-licenses: [DEFERRED-TO-R2]") and is not resolved at R2 with a concrete `<facet>:<id>` citation is a SIGNAL finding per entry. A sidecar that block-asserts citation-completeness ("all entries cite both axes — see above") without per-entry resolution is a SIGNAL escalation to HARD on cycle-2 (the assertion does not survive per-entry verification). **Citation resolution to the locked graph.** Every `facet-licenses:` citation must resolve to an actual entry on disk — e.g., `feeling-taylor:7 @23` requires `feeling-taylor-...md` to carry an entry whose id is `7` with proto-anchor `@23`. A citation that names an anchor where the cited facet does not fire (cite-index walk fails to resolve) is HARD per entry. Promoted from audience-gate cycle-1: cape-fic-reader and worm-canon-pedant independently attacked dialogue-coll sidecar's R1-blind placeholder citation; cycle-1 also surfaced dialogue-wren sidecar citing `feel-wren:@22` when the cite-index resolves `feel:2` only at `@21` — 3-of-3 audience convergence on the citation-resolution failure.

---

## Contamination disciplines (R2 graph context filtering)

R1 is blind. R2 reads the locked graph. Filtering the graph payload prevents voice pickup from other agents' registers:

1. **Filter to facts, not prose.** Sensory / loc-state / state-updates entries are already terse and structured — pass verbatim. Feeling / memory / NI / vibes — pass somatic-tell text / monument-name / interest-focus / vibe-target fields only, *stripped of rationale prose*. The cite-index walk per anchor gates this filtering.
2. **Filter to the speaker's own perspective slices.** Speaker's own `feeling-<slug>` is first-class. Other characters' feeling at the same anchor is *room temperature* — pass as one-line abstract (`mira:tense-shoulders-on-the-board`), not full entry. NI is first-class only when speaker IS POV; for non-POV speakers, NI is third-person-about-them and risks pickup — pass as one-line abstract if at all.

---

## Hard fences

- **Earth-Bet proper-noun scan across utterance text.** Case-insensitive substring scan against the canonical hard-fence list (Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea — refresh against canonical list at every audit). Any hit is HARD.
- **Monument naming rules from behavior card.** Speakers do not name monuments they cannot have. Speakers do weight monuments they would carry. Auditor checks against behavior card § memory monuments.
- **Forbidden vocabulary from behavior card.** Cards specify forbidden words per register. Auditor flags violations as AP-SCAN.

---

## Per-anchor caps

- **≤3 utterances per anchor.** Multi-utterance exchanges at one anchor should split across anchors when natural. >3 indicates the bone is overloaded; flag for re-shape upstream, not papered over.
- **No two utterances of the same speaker at the same anchor unless they are a deliberate single-turn split** (e.g. interruption-of-self, beat-and-clarify). Multi-entry single-turn must be justified in the drafts sidecar.

---

## Sparsity

Unconstrained — dialogue is content, not flag. Sparsity follows what the proto-line bones call for: a speaking-heavy episode has more dialogue, a silent episode has less. The FREQUENCY-BAND audit class does not gate dialogue on sparsity, only on per-anchor caps.

---

## V2 reviewer protocol (audience-gate Phase 5b)

Two-stage per reviewer per character file:

### Stage 1 — V2 strict affirmative-demonstration

Per entry: ACCEPT (Q1 + Q2 both pass) / REVISE / FAIL. Persona-distinct lenses (atmosphere / board-move / voice-precision — or facet-equivalents from the active audience). Inoffensive lines fail Q1; on-card-but-violating fail Q2.

### Stage 2 — V3 adversarial seam-finding

For every line, accepts included, each persona produces the strongest hostile counter-argument from its lens. Aggregate the strongest as the seam. Persona-distinct constraint: seams must differ by lens so they aren't generic craft-criticism.

Facet evidence is fair attack surface: "the chosen draft cites `feeling-taylor:7` as license, but that entry is a held-breath tell that doesn't carry register-slip in stitch — the slip claim is unsupported."

### Aggregation

Strict 3-of-3 ACCEPT per character per `/and-facets` audience-gate convention (URI-AUDIENCE-AGGREGATION-RULE). Single dissent fails the character — defaulted to revise.

### Convergence

Failed characters route callouts to fixer. Fixer dispatches dialogue-writer in **defense-or-revise mode** (v1 R3 protocol):

- Per line with a seam: defend with card + facet citations, OR revise.
- Defended accept stays as is.
- Revision means the seam was load-bearing; revisions get full multi-draft + chosen-mark + rejection-notes treatment.

Cycle cap: 3 per `/and-season` convention.

---

## R1 vs R2 differences

**R1 (blind):** dialogue-writer reads behavior card stack + speaker persona/ltm/stm/state + base proto-lines + upstream `tensometer.md` + this rubric. Authoring is from intent (derived per-beat from cast + tens + speaker-state) + cards only. Forbidden: other R1 facet outputs, show files, source prose.

**R2 (graph-aware):** dialogue-writer re-runs in judge mode with all nine other R1 facet files + cite-index. Decisions per existing entry:

- KEEP — card signature affirmatively demonstrated; facet-license citations resolve in locked graph; somatic-tell / monument adjacency claimed by the chosen draft is structurally present.
- DELETE — card signature missing (inoffensive); forbidden vocabulary; facet-license citation does not resolve; hard-fence hit; other facets render the same content (DEDUP with NI, feeling, memory).
- REWRITE (delete + new ID) — internal mini-V3 surfaces a closable seam; revised draft cites different facet license or different §-section.

Add-cap: ≤3 per character per run. Adds are exceptional — R1 covers the speaking beats; R2 adds only when a beat is genuinely silent that the card + graph license a line for.

---

## Audit classes (Phase 5)

Dialogue feeds into existing facet-audit classes; this section names dialogue-specific clauses:

- **STRUCTURAL** — every entry's `@<proto-line-id>` resolves to a proto-line; every `<character-slug>:<id>` citation in proto-lines resolves to an existing entry; entry-ID monotonicity per-character; behavior-card slug in header matches a real card.
- **CONSTRAINT § behavior-card-compliance** — every entry respects the card's §hard fences, §forbidden vocabulary, §monument rules.
- **CONSTRAINT § citation-completeness** — every chosen-mark entry in the drafts sidecar has both card-signature §-cite AND facet-license citation (post-R2). Missing one axis: SIGNAL. Missing both: HARD.
- **CONSTRAINT § earth-bet-hard-fence** — proper-noun scan across utterance text. Any hit: HARD.
- **AP-SCAN** — em-dash + semicolon chassis on non-Taylor speakers (v1 anti-pattern); modern HR-speak in Westerosi register; deposition cadence in non-administrative speakers; nominalizations substituting for plain English in colloquial-register speakers.
- **DEDUP** — utterance content rendered by NI / feeling / memory at the same anchor (the speaker says aloud what another facet already shows — the dialogue or the other facet must yield).
- **FREQUENCY-BAND** — per-anchor cap ≤3 utterances; no sparsity gate.

---

## Files

- **Output (canonical):** `active-project/theater/dialogue/<character-slug>.md` per `schemas/dialogue.schema.md`.
- **Drafts sidecar:** `active-project/staff/dialogue-writer/<character-slug>.drafts.md` — multi-draft + chosen-mark + rejection notes + card-signature citations + facet-license citations. Audit reads this for CONSTRAINT § citation-completeness.
- **R2 decision shard:** `active-project/staff/dialogue-writer/r2-decision-shard-<character>.md` — KEEP / DELETE / REWRITE per entry, folded into `.r2-decisions.md` at Phase 4.
- **Annotated proto-lines copies:** `_inflight/proto-lines-dialogue-<card>.md` (R1) and `_inflight-r2/proto-lines-dialogue-<character>.md` (R2) — citations `[<character-slug>:<id>]` appended to speaking-beat anchors.
