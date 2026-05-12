# Dialogue Tuning — V2 (facets-as-lenses re-fit)

Authority for the dialogue authoring + review pass that fires after `/and-facets` clears. Supersedes the v1 round-trip protocol as the operational design; v1's learnings are preserved here as load-bearing input, not as a competing pipeline.

V1 source: `design/shoot-v2/round-trip-method.md` (round-trip tuning on s01e01–s01e06 dialogue corpus).
V1 corpus: `design/shoot-v2/dialogue-corpus.md`.

Status: design (not yet wired). Implementation lands as either `/and-facets` Phase 5c or a chained `/and-dialogue` command.

---

## What v1 settled (preserved)

Eight patterns from the round-trip tuning carry forward unchanged. These are the protocol floor.

1. **Per-behavior-card forks, not per-character forks.** Cross-contamination at generation time is the original failure mode — Taylor's em-dash + semicolon chassis bled into every speaker when one writer handled multiple registers. One fork per behavior card present in the episode prevents this structurally. A single fork authors across all speakers sharing that card.
2. **Card-stack load order, read before drafting.** Leaf card → parent (`inherits:`) → universal overlay → adjacent class/region cards (`references:`) → speaker persona + ltm. Margit composes the stack; the fork sees concatenated text with leaf last so the per-character voice is the most-recent context.
3. **Blind to originals.** Writer fork is forbidden to read show files or prior corpus. Authoring is from intent + cards (+ facets, in v2) only. Eliminates paraphrase bias.
4. **Intent specifies state, not text.** Board-move + register state (mask ON/SLIPPING/OFF for doubled-register cases) + rung-within-card + distance + public-vs-private framing. Text-paraphrase intents collapse back to the original.
5. **Multi-draft + chosen-mark + rejection notes.** Writer produces 2–3 drafts per intent, marks the chosen one, briefly justifies why each rejected draft is rejected. Reviewer can test the *claim* not just the line.
6. **Affirmative card-features citation per chosen line.** Writer lists which card signatures the chosen draft demonstrates (with §-section citations). Becomes the audience's hostile target in the seam-finding pass.
7. **Explicit anti-patterns in every brief.** Project-specific contamination named (em-dash + semicolon spine, modern HR-speak, deposition cadence). Negative space matters as much as positive.
8. **Calibration anchor per batch.** One intent that maps to a known-strong target (Plumm/NC-4 was v1's anchor). Prevents whole-batch upward drift.

## What v1 settled about the reviewer (preserved)

Two stages, both load-bearing:

- **V2 strict affirmative-demonstration rubric.** ACCEPT only if the line **affirmatively demonstrates** at least one signature feature of the assigned card AND does not violate it. Inoffensive ≠ on-card. v1 lift was +54 points under identical rubric (40% on originals → 94% on regenerated round-2 lines).
- **V3 adversarial seam-finding.** For every line, accepts included, each persona produces its strongest hostile counter-argument; aggregate the single strongest as "the seam." Output is *defense scaffolding*, not new verdicts. Constraint: challenges must be persona-distinct (atmosphere / board-move / voice-precision) so the seam isn't generic craft-criticism.

Convergence: writer defends-or-revises per seam. Defended accept stays. Revision means the seam was load-bearing; revisions get multi-draft + chosen-mark treatment.

## What v1 surfaced and left open (carry forward as test cases)

- **The doubled-register problem.** Taylor carries Earth-Bet base + Westeros leaf; contradiction is load-bearing AND the primary attack surface. v3 audience flagged: "the slip is invisible to a reader who hasn't been told to look for it." V2 hypothesis: facet adjacency makes the slip visible — `feeling-taylor:<id>` co-cited at the same anchor as the slipping line carries the somatic tell that licenses the slip. Verify in dogfood.
- **One-word-line floor.** "Twelve." rejected; "Twelve, septon." accepted. Open whether card can demonstrate on surface area below ~3 words. V2: cited facet adjacency may license shorter surface because the slot's work is shared across the graph, not done by the utterance alone.
- **Cross-line dependencies.** TH-3 and S-2 depended on each other (Rowan's pastoral concern reads as correct perception only if Taylor's "twelve" was wrong-in-mouth). v1 audience reviewed in isolation. V2: the cite-index walk per anchor is the structural fix — co-cited facets travel together.
- **Reviewer/writer asymmetry.** Both reload cards and cite the same rubric. Works because writer cites *which signatures the line demonstrates* and reviewer tests whether each lands. V2 preserves this and adds: writer cites *which facet entries license the choice*; reviewer tests both axes.

---

## What v2 changes — facets-as-lenses

V1 wrote dialogue blind to the rest of the graph because the rest of the graph didn't exist. V2 reads the locked graph per anchor and uses it the way the proto-line bones use it: as the structured context that prevents the writer from inventing what the rest of the pipeline has already established.

### Round-trip intent fields, now derived from facets

| v1 hand-authored intent field | v2 derivation from locked graph |
|---|---|
| mask state (ON/SLIPPING/OFF) | speaker's `feeling-<slug>` entry at the anchor (somatic-tell pressure) + memory monument adjacency |
| rung within card | speaker persona + addressee cast at anchor |
| distance / public-vs-private | `location-state` at anchor (who's in the room) + cast at anchor |
| board-move | the proto-line itself (SVO + cited objective) |
| register pressure | `memory` (monument adjacent?) + episode vibe-cloud |
| perceptual frame | `sensory` at the anchor (what speaker hears/smells while speaking) |
| narrator-attention shape | `interest-narrator` at anchor — only when speaker IS POV |

### Two contamination disciplines

Facet text is in other agents' registers (showrunner vibes prose, impersonator-authored feeling, dramatist tens notes). Two filters prevent voice pickup:

1. **Filter to facts, not prose.** Pass facet *fields* not facet *rationale*. Sensory / loc-state / state-updates entries are already terse and structured — pass verbatim. Feeling / memory / NI / vibes — pass the somatic-tell text / monument-name / interest-focus / vibe-target fields only, stripped of rationale prose. The cite-index walk gates this filtering.
2. **Filter to the speaker's own perspective slices.** Speaker's own `feeling-<slug>` is first-class. Other characters' feeling at the same anchor is *room temperature* — pass as one-line abstract (`mira:tense-shoulders-on-the-board`), not full entry. NI is first-class only when speaker is POV; for non-POV speakers NI is third-person-about-them and risks pickup — pass as one-line abstract if at all.

### Facet citations as second-axis evidence

V1 chosen drafts cited card §-sections. V2 chosen drafts cite **both** card signatures AND licensing facet entries:

```
chosen: "Twelve, septon."
card-signatures: §Cadence (clipped reply); §Syntax (vocative-suffix as ward-deference)
facet-licenses: feeling-taylor:7 (somatic tell — held breath at the anchor)
                memory-taylor:3 (monument adjacent — sept-grain count)
```

This is the structural answer to v1's "slip is invisible" open question. The slip doesn't have to land *in the surface of the utterance alone* — it lands in the slot, with adjacent fired facets carrying co-load.

### Hard vs soft input

**Facets are a hard input.** A speaker beat whose anchor cannot resolve through the cite-index fails the dispatch — same argument as the bone-gate (URI-026): deformed inputs shouldn't be rescued by downstream skin. Sparse anchors are an upstream defect; flag back to the facet authors. Writer does not paper over.

---

## Phase shape

Whether this lands inside `/and-facets` (Phase 5c) or as a chained `/and-dialogue`, the internal shape is the same five-step sequence:

```
5c.1 — intent compile (coach-shaped fork)
        Reads locked graph + cite-index + cast at every speaking anchor.
        Emits per-beat intent briefs in v1's tuned format
        (board-move / mask state / rung / distance / public-vs-private)
        with derivation traced to specific facet entries.

5c.2 — writer fanout (per-behavior-card forks; one Agent block, parallel)
        Each fork receives:
          - its behavior card stack (margit-composed)
          - intent briefs for every beat its card covers
          - filtered facet slice per beat (see disciplines above)
          - anti-pattern list (project-specific contamination)
          - one calibration-anchor intent (v1-strong target)
        Each fork emits: per-character dialogue file(s) it covers,
        with multi-draft + chosen-mark + card-signature citations
        + facet-license citations per chosen line.

5c.3 — V2 audience pass (per-character, parallel block)
        Strict affirmative-demonstration rubric.
        Reads: dialogue file + behavior card stack + the proto-line
        with its full decoration tail + cited facet entries.
        Verdict per line: ACCEPT (signature demonstrated, no violation)
        / REVISE / FAIL. Persona-distinct lenses.

5c.4 — V3 seam-finding (per accepted line)
        Each persona produces strongest hostile counter-argument.
        Aggregate strongest as the seam. Persona-distinct: atmosphere
        / board-move / voice-precision. Facets are fair attack surface:
        "the slip claims license from feeling-taylor:7, but that entry
        is a held-breath tell that doesn't read as register-slip in
        stitch." Output is defense scaffolding.

5c.5 — writer defense-or-revise (per line with seam)
        Writer fork re-loads (fresh fork, same brief structure).
        Per line: defend with card + facet citations, OR revise.
        Revisions get multi-draft + chosen-mark.
        Cycle cap: borrow audience-gate's 3-cycle convention.
```

### What ends up on disk

- `active-project/theater/dialogue/<character-slug>.md` — per the existing `schemas/dialogue.schema.md`. The writer fork's multi-draft + chosen-mark + citations live in a sidecar `<character-slug>.drafts.md` under `active-project/staff/dialogue-writer/`, not in the canonical file (which the stitcher reads).
- `active-project/staff/audience/<persona-slug>/dialogue-<character>-r<N>-verdict.md` — per-persona V2 verdicts + V3 seams. Same shape as the facet audience-gate verdicts.
- `active-project/staff/dialogue-writer/<character-slug>-r<N>-defense.md` — defense-or-revise output per cycle.

---

## Convergence and cap-burn

- V2 audience produces aggregate per-character verdict (3-of-3 ACCEPT per line, or revise/fail routes through V3 seam → defense).
- Cycle cap: **3 dialogue cycles** per `/and-season` convention.
- Cap-burn: orchestrator-critic verdict goes NOT-SUCCESSFUL with failing characters named; user escalation; dialogue files persist as best-effort with cap-burn flag in showrunner memory.

## Convergence with the bidirectional loop

The facet audit + audience-gate already have a bidirectional convergence trace (auditor finding + audience callout overlap = `validated`). Dialogue adds a third path: facet citations in dialogue chosen drafts. If a chosen draft cites `feeling-taylor:7` as license and the V3 seam attacks that same entry, the convergence trace records it. Three-way overlap (auditor flagged + audience flagged + dialogue-writer cited) on the same facet entry is the strongest signal that the entry is load-bearing — and the strongest signal that it's a load-bearing failure if any of the three calls it suspect.

---

## Open questions

1. **Intent-compiler ownership.** Coach was the bullet-to-prompt translator in shoot-v1; retiring with the impersonator. Either resurrect coach as the intent-compiler (canonical translator role) or assign to a fresh fork class (`dialogue-intent`). Lean: coach — the role is the same shape (structured input → structured prompt), just with a different input format.
2. **POV speaker's dialogue + narrator-interest interaction.** When the POV character speaks, their utterance lands adjacent to NI entries the same character is generating-as-narrator. Two voices for one head. Open whether the writer fork for POV needs to read its own NI entries as register evidence (likely yes, with the same fact-filter discipline) or as a forbidden cross-contamination source (no — same head, same voice).
3. **Cross-card co-authored beats.** Two speakers from different behavior cards at the same anchor (Taylor + Plumm exchange). Each card's fork authors its own speaker's line, but the lines need to read as an exchange — call-and-response, beat-and-counter. Open whether the per-card forks need to see each other's *intent briefs* (probably yes, since intent is structured) but not each other's *drafts* (no — that's cross-contamination). Or whether a paired-line review pass is needed at V3.
4. **Hard-input failure routing.** When a speaker beat fails because the anchor's facet decoration is sparse, the writer flags it back. Open: does that re-fire `/and-facets` (full re-run, expensive) or does it route to a targeted facet-author dispatch (cheap, but breaks the locked-graph contract)? Lean: surface as TASTE-FLAG → AP-SCAN promotion path, accumulate evidence, re-fire `/and-facets` only when the pattern repeats across beats.
5. **Calibration anchor selection.** V1's Plumm/NC-4 was hand-picked from the corpus. V2 needs a programmatic selection rule — probably "highest-tens anchor with all four lens facets fired and a known-strong v1 line." Worth encoding so the rule survives across projects.

---

## Migration

- **First dogfood:** re-shoot s01e01 dialogue under the v2 protocol. Direct A/B against the v1 round-trip output. Audience pass blind to which is which.
- **Metric:** v3 seam-defensibility rate. v1 baseline is "% of accepts that survive seam-finding without revision." v2 should materially improve this because the seams that v1 couldn't close (the invisible-slip problem) should close on facet-adjacency citation.
- **Anti-regression:** v2 must not regress on v1's affirmative-demonstration rate (94% on round-2 lines). If the facet integration loosens the writer's discipline — facet citations substituting for card-signature citations rather than supplementing — the rubric should catch that as a card-signature-missing finding regardless of how strong the facet license is.
