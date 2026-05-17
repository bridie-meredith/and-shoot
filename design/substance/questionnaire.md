# Substance Questionnaire — Screen-writer's Authoring Rubric

The 1–9 archetype questionnaire is the rubric the **screen-writer agent** consults when proposing a series signature at `/and-substance series` Phase 4. It is **not** a user-facing prompt sequence — the user does not answer these questions directly. The screen-writer reads the brief + series chunk + structural commitments, runs through these questions on the user's behalf, and proposes a draft signature. The user then edits the draft.

This document is the rubric. The user-flow is documented in `plan.md § /and-substance Phase 4 substance questionnaire user-flow (B2)`.

---

## How the rubric is used

1. **Screen-writer reads** `project.brief` + `project.constraints` + `series.chunk` + `series.structure.*`.
2. **For each universal axis** (~9: wealth / health / community / emotional / capability / knowledge / reputation / agency / trust), the screen-writer answers the questions in this rubric to land:
   - `start_rank` (1-9) per perspective (protagonist / antagonist / world)
   - `end_rank` (1-9) per perspective
   - per-rank anchor text (`one_means`, `five_means`, `nine_means`) calibrated to the story-world
3. **Screen-writer drafts** the cost-ledger entries (gain ↔ cost pairings) and antagonist-pressure entries.
4. **Screen-writer writes** the draft to `staff/showrunner/signature-draft.md`.
5. **User edits** any rank, anchor, axis, or cost-ledger entry inline.
6. **User types `accept`.** The edited draft moves to `series.substance.*`.

---

## Per-archetype question banks

### Protagonist perspective

**Wealth.**
- What does the protagonist have at story open in material terms? Coin, property, access to food, security from cold/hunger.
- What's the natural ceiling in this world? What is "rich" — landowner-rich, merchant-rich, royal-rich?
- Where in that ceiling does the protagonist sit at start? At end?

**Health.**
- Is the protagonist's body intact at start? Any injuries / chronic conditions / disability that affects what they can do?
- Does the story require physical action they currently can or can't perform?
- Does the protagonist age, get wounded, recover, weaken across the series?

**Community.**
- Who knows the protagonist's name at start? Who would help if they asked?
- Is the protagonist embedded in any community (village / order / guild / family)?
- Does the protagonist gain a constituency? Lose one?

**Emotional.**
- What is the protagonist's emotional baseline at start — grieving / functional / hopeful / shattered?
- Is there an emotional wound that defines the protagonist? Does the series heal it, deepen it, or recontextualize it?
- At end, is the protagonist self-secure or still fragile?

**Capability.**
- What's the central task of the story (combat / scheming / surviving / governing / building)?
- How competent is the protagonist at that task at start? Helpless / amateur / professional / virtuoso?
- Does the series make them more capable? Less capable? Differently capable?

**Knowledge.**
- What does the protagonist know at start that matters? What don't they know?
- What revelations does the series surface?
- At end, does the protagonist know more than the people around them, the same, less?

**Reputation.**
- What's the external read on the protagonist at start? Unknown / despised / respected / feared / loved?
- Whose read matters in this story? The reputation among nobles, peasants, allies, enemies?
- Does the reputation shift? Become more accurate to who they are, less accurate, polarized?

**Agency.**
- How much control does the protagonist have over their own life at start? Free / coerced / imprisoned / paralyzed?
- What's the agency-arc — gain control, lose control, exchange one cage for another?
- At end, can the protagonist direct outcomes? At what scope — self / family / region / world?

**Trust.**
- Who does the protagonist trust at start? Who trusts them?
- Are there betrayals in the story? Restorations? New trusts formed?
- At end, what does the trust-network look like?

---

### Antagonist perspective

The antagonist (or antagonistic force) gets its own per-axis ranks where relevant. Not every axis is in motion from the antagonist perspective — only the ones the antagonist actually pressures or possesses.

For each pressured axis:
- **Pressure source** — what is doing the pressuring (a named character, an institution, an environmental force, a hostile structure)?
- **Cost curve** — does the pressure escalate / oscillate / cap-out / collapse across the series?
- **Antagonist Δ** — does the antagonist gain/lose on this axis themselves across the series? (A villain whose reputation rises while the protagonist's also rises produces a different arc from one whose reputation collapses.)

---

### World perspective

Some axes track the world-state rather than a character — useful for stories where the world itself transforms (war breaks out, magic returns, a system collapses).

- Which axes move at the world-scale? (Wealth: kingdom prosperity. Knowledge: lore lost or recovered. Trust: faith in institutions.)
- Is the world-Δ a backdrop to the protagonist's arc or the actual subject of the story?
- For cyclical books (`series.structure.cyclical: true`): which world axes drift across cycles? Which stay reset? (HP pattern: world drifts forward across books; Hogwarts as setting resets each year.)

---

## Anchor calibration

The 1–9 scale is **per-story**. Rank 9 wealth in a Westeros story is "Lannister-rich"; rank 9 wealth in a coffeeshop story is "owns the coffeeshop free and clear." The screen-writer's job in Phase 4a is to write the rank-1 / rank-5 / rank-9 anchors as concrete sentences calibrated to the story-world.

Calibration questions per axis:
- **Rank 1 anchor:** what is the *bottom* of this axis as the story-world defines it? Who in the story-world sits at rank 1?
- **Rank 5 anchor:** what does "ordinary functional" look like? The median citizen / median peer / median expectation.
- **Rank 9 anchor:** what is the *top* visible in this story? Not the abstract Platonic top — the top the story-world can show, the top any character in the story actually reaches or competes against.

Anchors are one-line each. If the anchor needs more than one line, it's underspecified; tighten it.

---

## Cost-ledger entries

For each major gain in the series-Δ, the screen-writer drafts a cost-ledger entry:

```yaml
- id: <ledger-entry-id>
  gain: <axis-slug> +<delta>
  cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
  anchor:
    book: <book-slug>
    chapter: <chapter-slug> | null
    scene: <scene-slug> | null
```

Per-cost rubric:
- Is the gain free, or does something get paid? If free, the bone-gate will HARD-fault it as `SUBSTANCE-SUSPECT-cheap-gain` — don't ship cheap gains.
- If a cost is paid, is it on another axis (the canonical case) or on opportunity / journey?
- At what level does the cost get paid — series, book, chapter, scene? Write the anchor at the coarsest level you know; refinement happens at downstream chunker passes.

---

## Antagonist pressure entries

For each axis the antagonist (or world) pressures, the screen-writer drafts:

```yaml
- axis: <axis-slug>
  pressure_source: <one line>
  cost_curve: <one line>
```

Per-entry rubric:
- What is doing the pressing? Be specific — name the character or institution.
- How does the pressure change across the series? Escalates monotonically / escalates then breaks / oscillates / caps-out / collapses?
- Is the pressure visible to the protagonist? (Antagonist whose pressure is invisible to the protagonist produces a different drama than one whose pressure the protagonist can see and resist.)

---

## Worked example — trace from brief to signature

**Brief.** *"A young woman raised in Flea Bottom learns she's a bastard Targaryen and must survive the Red Keep before her presence destabilizes the realm."*

**Series chunk** *(after `/and-series` Phase 2):* *"Maya's discovery of her bloodline drags her from the cellar of King's Landing into the throne-room politics that will either kill her or rewrite the line of succession. The court's small council moves first; Maya learns the language second; the realm reads the result third."*

**Screen-writer's questionnaire trace (protagonist perspective):**

| axis | start_rank | end_rank | rationale |
|---|---|---|---|
| wealth | 1 | 6 | Flea Bottom start (no coin, no roof); end with crown-funded household but contested |
| health | 6 | 4 | Functional at start (laborer); end carrying a scar and an addiction |
| community | 3 | 5 | Has a couple of Flea Bottom relations; gains court allies but loses the cellar circle |
| emotional | 4 | 3 | Grief-baseline at start; end more shattered for what she's seen, though more self-secure too — net -1 |
| capability | 2 | 6 | Cannot read at start; ends fluent in court protocol + small-blade combat |
| knowledge | 1 | 8 | Knows nothing about her bloodline or the court at start; ends as informational hinge |
| reputation | 2 | 9 | Unknown bastard at start; named heir presumptive at end |
| agency | 2 | 5 | Coerced by hunger at start; autonomous within court scope at end (still constrained by politics) |
| trust | 4 | 2 | Trusts a handful at start; betrayals across the series leave end-state trust-poor |

**Cost-ledger entries (draft):**

```yaml
- id: cl01
  gain: reputation +7
  cost: trust -2
  anchor: { book: b03, chapter: null, scene: null }
- id: cl02
  gain: capability +4
  cost: opportunity-missed:never returned to the cellar
  anchor: { book: b01, chapter: null, scene: null }
- id: cl03
  gain: knowledge +7
  cost: emotional -1
  anchor: { book: b02, chapter: null, scene: null }
```

**Antagonist-pressure entries (draft):**

```yaml
- axis: reputation
  pressure_source: small council faction allied to the established heir
  cost_curve: escalates then breaks at the throne-room reveal in b03
- axis: agency
  pressure_source: court protocol itself (the constraints of being claimed)
  cost_curve: monotonic; the more she is recognized, the less she can move freely
```

The user reads this draft, edits any rank or anchor or cost-ledger entry, then types `accept` to commit.

---

## What this rubric does NOT do

- It does not author the cost-ledger anchors at fine grain. Anchors are coarse-first; downstream `/and-substance book` and `/and-substance chapter` refine them when authoring the deeper chunks.
- It does not validate the signature against the chunk. That's `/and-substance series` Phase 5 (audience + dramatist + auditor review).
- It does not enforce a fixed axis-set. The 9-axis baseline is a recommendation; the user may add domain-specific axes (e.g. "magic capacity" in a fantasy series, "social rank" in a Regency story) or remove ones that don't apply.
