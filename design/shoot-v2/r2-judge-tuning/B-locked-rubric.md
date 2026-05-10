---
phase: B — locked R2 rubric (revised: justification-first)
project: R2 hybrid judge tuning
date: 2026-05-10
status: LOCKED — do not soften before Phase F audience verdict on a re-run corpus
parent: design/shoot-v2/r2-judge-tuning/A-corpus.md
companion: design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md
---

# Phase B — Locked R2 Rubric (Justification-First)

This is the discipline R2 (the graph-aware hybrid judge) must honor at every layer (R2.1–R2.4 in `and-facets-r2.md`), regardless of which facet is being judged. It sits **on top of** each facet's content rubric — R2 inherits the facet rubric for content; applies these gates for judge-mode discipline.

## Core principle — taste over arithmetic

R2's job is **forming a justification** for why each entry stays, leaves, or gets added — not running a checklist. Each verdict must be defensible as **a taste-argument with reasoning**: this is what the entry does, this is why it works or doesn't, this is what the rubric is reaching for here.

This aligns with the project-wide direction (URI-017 Threshold Discipline: "rubric arithmetic is advisory, taste authoritative"). R2 reviewers were drifting toward mechanical pattern-matching against the rubric's named anti-patterns; that pattern-matching is what produced F-R2-1 through F-R2-4. The fix is not better mechanics; it is **the reviewer holding themselves to taste-justification**, with the rubric serving as the vocabulary in which taste-arguments are expressed.

The arbiter (see `C-arbiter-protocol.md`) intervenes when justifications slip back into mechanical citation.

## Hard fences (absolute; not negotiable)

These are **not** taste calls. R2 honors them as fences:

- POV-perceptual-access (narrator-interest, memory, feeling).
- Hard-fence vocabulary lists (no Earth-Bet proper nouns; no listed forbidden constructions per facet).
- Self-scoped deletion authority (R2 cannot delete other facets' entries).
- Add-cap (≤5 per facet; ≤3 metaphor; ≤5 per character feeling).
- Schema/citation integrity (cascade strips on delete; protoline citation lists track entries).

Violations of fences are not subject to taste argument. R2 refuses the verdict.

## The four gates — reformulated as taste-questions

Each gate names a question the reviewer must hold themselves to. The reviewer's verdict is justified by **answering the question**, not by passing a check.

### Gate G1 — "Does the revision still earn its place when I read it cold?"

**Failure mode addressed:** F-R2-1 (form-discipline drift on revisions).

**The question:** when R2 revises an entry, the reviewer must set down the seam they were authoring against and re-encounter the entry as if seeing it for the first time. The taste-question is: *if this were a fresh R1 entry I had never seen before, would I keep it?*

**What this is not:** running §Form / Q1 / Q2 as three checkboxes. The reviewer reads the revision aloud (mentally). If the cold-read produces unease or the impulse to keep editing, the entry has not earned its keep yet.

**Justification format:** the reviewer writes 2–3 sentences explaining what the cold-read produces. Examples of good justification: "The cold read still trips on 'the way an estimate gets one' — the comparison construction reads as estimative-of-the-feeling rather than the cost-accountant register the revision was reaching for. The revision answered the angular-measurement seam but didn't earn the form." Examples of insufficient justification (would trigger arbiter intervention): "§Form: PASS, AP6: PASS, Q1: PASS." That's mechanical recitation, not taste-argument.

**Arbiter check:** does the justification name something **specific to this entry** (a phrase, a register-shift, a moment) rather than reciting rubric labels?

### Gate G2 — "Why does this entry want to be added — and is that wanting honest?"

**Failure mode addressed:** F-R2-2 (multi-justification under-strictness on adds).

**The question:** when R2 considers adding an entry, the reviewer asks *why this entry, here?* Two honest motives: the at-rest evidence (the proto-line, the cards, the persona's lived state) is calling for it; OR the graph reveals an obligation (a tens=3 peak with no memory or NI is a structural absence). The dishonest motive: the graph reveals a niche and the reviewer fills it because there is room.

The graph-revealed niche **enables** the question; it does not **answer** it. The answer comes from at-rest evidence.

**What this is not:** counting multi-justification slots (3 of 5, 4 of 5). The reviewer should know, from reading the proto-line and the cards, whether the entry is *wanted* there. If the wanting only appears when the niche is pointed out, that is the dishonest motive.

**Justification format:** the reviewer writes a paragraph (4–8 sentences) tracing the motive. "I see this proto-line tracks Taylor's swarm-sense suppression as a flat administrative line — there's no internal register of the cost. The card has 'cost-tracking' as a load-bearing trait. The proto-line is asking for an entry, not because R1 missed it, but because the suppression scene now reads at-rest as too clean. So I add a feeling entry tracking the suppression-cost." That's taste. Compare to: "Multi-justification: PROTO-LINE-AT-ANCHOR ✓, CARD-§ ✓, PERSONA-STM ✓. Add." Mechanical.

**Arbiter check:** does the justification trace from at-rest reading to the add, or does it work backward from the niche?

### Gate G3 — "Does this entry hold up when I block out what comes next?"

**Failure mode addressed:** F-R2-3 (lonely-entry adjacent-context dependency).

**The question:** for any lonely entry (no co-cited facets at the anchor proto-line), the reviewer asks *if I cover the next proto-line with my hand and read just this one + the entry, does it still work?* If the entry's reading depends on the speech that follows or the action that resolves it, the entry is not at rest — it is leaning on what comes next.

**What this is not:** a literal masking process. It is a discipline of attention — the reviewer should be able to articulate what the entry *does at its anchor* without referring to the adjacent stream.

**Justification format:** the reviewer says, in their own words, what the entry contributes at its anchor proto-line. If the contribution can only be stated as "it sets up what comes next" or "it pays off what came before," the entry has failed the at-rest test.

**Arbiter check:** does the justification stand when adjacent context is omitted from the description? A good justification reads correctly even if the surrounding proto-lines are absent from the discussion.

### Gate G4 — "Does the facet, as a whole, feel patterned in a way it shouldn't?"

**Failure mode addressed:** F-R2-4 (cross-character + within-character pattern blindness).

**The question:** at the close of each R2 layer, the reviewer reads the full facet file end-to-end (or skims it, holding all entries in attention) and asks: *does anything feel formulaic? Does the same somatic-tell repeat across characters? Does the same construction template appear within a character? Does a low-frequency word (weight, hold, press) saturate?*

**What this is not:** counting instances against thresholds. It is the reviewer's ear catching a pattern that wasn't there entry-by-entry. The pattern is real if and only if the reviewer can articulate why it bothers them.

**Justification format:** the reviewer names the pattern in their own words and points to specific instances. "Three characters all do the same somatic-tell category at the column-tracing scene — Taylor with her hands, mother with her shoulders, the clerk with his jaw. The scene was supposed to play three different cost-registers; instead it plays one register triplicated. I'd cut two of the three." Compare to mechanical: "Cross-character same-strategy: 3 instances. SIGNAL." That doesn't say what is wrong.

**Arbiter check:** does the pattern flag come with **what specifically should change** as a consequence? A pattern flag without a remediation argument is mechanical; a pattern flag with "I'd cut these, here's why" is taste-justification.

## Decision-log discipline

Each R2 layer produces a decision-log shard at `active-project/staff/<facet>/r2-decision-shard.md` (feeling: per-character `r2-decision-shard-<character-slug>.md`). **Every verdict is one free-prose paragraph followed by one verdict line — no labeled subfields.** The labeled-subfield template that PLAN v1 used was itself checklist-shaped, which is the failure mode the locked rubric is fixing (audit SIGNAL-004).

The shard's frontmatter carries failure-mode counts the orchestrator-critic Phase 6 reads:

```yaml
---
facet: <facet-name>
episode: <slug>
layer: R2.<n>
character: <slug>           # only for feeling per-character shards
f-r2-counts: {f-r2-1: <n>, f-r2-2: <n>, f-r2-3: <n>, f-r2-4: <n>}
---
```

The body is free prose. One block per existing-entry decision and per new entry. Reviewer voice throughout. Each block ends with a single verdict line:

```
<facet>:<id> @<proto-line> — <reviewer's paragraph: what the cold read produced; what the entry does or doesn't do at-rest; for revisions, what specifically the cold-read found; for adds, the at-rest motive traced from reading not niche; for the entry's contribution at the anchor without leaning on adjacent context>.
VERDICT: KEEP | DELETE (cascade <n>) | REVISE | ADD
```

Pattern-scan paragraph at end-of-layer (one prose paragraph in reviewer voice — what the reviewer's ear catches across the full facet, with specific instances and what would change as a consequence; if nothing patterned, a single sentence saying so):

```
PATTERN-SCAN: <paragraph>
```

Cap-refusals (one prose line per refused candidate, naming what the reviewer didn't believe in):

```
CAP-REFUSAL: <facet>:<id-candidate> @<proto-line> — <reason in reviewer's voice>
```

Arbiter intervention traces (per `C-arbiter-protocol.md`) append inline beneath the affected verdict:

```
[ARBITER T1: <intervention reason>]
<facet>:<id> @<proto-line> — <revised reviewer paragraph>.
VERDICT (revised): KEEP | DELETE | REVISE | ADD
```

If two interventions exhaust without a non-mechanical justification, mark the verdict `DISCIPLINE-FAIL` and increment the appropriate `f-r2-counts:` entry in frontmatter.

The free-prose discipline is structural, not stylistic. Labeled subfields invite the reviewer to fill the slots; the prose-paragraph requires the reviewer to carry the argument as a single thought. The reviewer's voice is what the rubric is reaching for.

## What the locked rubric does NOT do

- Does not gate **content** decisions — R2 still inherits each facet's rubric for what the entry should look like. The facet rubric provides the **vocabulary** for taste-arguments; it does not replace them.
- Does not change the add-cap, deletion authority, layer order, or schema/citation rules. Those are fences.
- Does not introduce a new agent class — the four R2 layer impersonators/editor are the same; they receive the locked rubric + arbiter protocol as discipline in their dispatch payload.

## Locking discipline

This rubric is **locked** as of 2026-05-10 in its justification-first form. Per Phase 1 of the facet-tuning template:

> Once V2 is set, do not soften it for later rounds. Lift numbers are only honest under fixed rubrics.

Revisions allowed only at Phase F (validation re-run audience verdict) with audience-confirmed evidence the gate is over-strict. The four gates may have **emphasis** recalibration but not **structural** removal.

## Phase C entry point

Phase C — Tightened audience attack — runs the existing s01e01 R2 outputs through audience adjudication using **G1–G4 as taste-questions, not mechanical checks**. Audience question per entry: did the R2 reviewer produce a real taste-justification, or did they pattern-match to the rubric? Per-persona verdicts, aggregated.

The arbiter (main session) intervenes during Phase C if audience verdicts themselves slip into mechanical recitation — see `C-arbiter-protocol.md`.

Output: `D-tightened-attack.md`. (Phase numbering shifts: arbiter protocol takes the C slot; tightened attack moves to D.)
