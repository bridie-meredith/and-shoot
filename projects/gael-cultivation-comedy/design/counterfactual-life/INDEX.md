# Counterfactual-Life Library — Master Index

**What this library is:** Project-scoped authoring substrate for `and-experiment`. It reconstructs
**the ordinary life Gael would have lived if she had never been the protagonist** — the life of a
trueborn Targaryen princess in the Red Keep during Jaehaerys I's long peace, lived straight, with no
past life, no cultivation, no plot. Servants, handlers, routines, the daily timetable, the calendar,
the expectations, the rules spoken and unspoken, the calibrated rewards and punishments.

It is the *negative space* of the story. Every chapter of the outline shows Gael **deviating from**
this baseline (meditating instead of attending needlework; running a heist instead of a nap;
performing compliance she does not feel). You cannot write a deviation legibly without the norm it
deviates from. This library is that norm — the lived texture the bones, facets, and stitch passes
draw from to ground a scene in a real household instead of a generic castle.

**Relationship to the rest of `design/`:**
- `cultivation-library/` defines the *interior* well (what Gael thinks she is doing — the
  broken-clock genre register).
- **This library defines the *exterior* well** (what the household sees her doing, and what it
  expects her to be doing instead). The two are a matched pair: the comedy and the horror both live
  in the gap between them, and this library is the *exterior* half of that gap.
- `run-01/constraints.md` §1–2 is the *institutional* bedrock (the offices, the canon laws, the six
  loopholes). This library is the *lived* extension: it takes those institutions and renders them as
  named people, hours of the day, and concrete routine. Where constraints.md says "the septa is the
  central handler," this library says what the septa does at the third hour after dawn.

**Hard fence (one line):** This is the **un-lived** life — the counterfactual baseline, NOT what
happens on the page. Nothing here asserts a plot beat. It is the default the plot departs from. When
a beat in the outline contradicts the baseline, **the outline wins and the contradiction is the
point** (that is a deviation, and the seam map below names it). The baseline never overrides a
ratified GUARD or outline beat; it furnishes the room they happen in.

**Authored:** 2026-06-08

---

## ⚠️ Naming / era note (read first)

This library is written to the **ratified live layer**, not to the warehouse cards:

| Role | This library (live layer) | Stale warehouse cards still say |
|---|---|---|
| Protagonist | **Gael** | `saerys-targaryen` |
| King / father | **Jaehaerys I** ("the Old King" / "the Conciliator") | `viserys-i-targaryen` (as father-king) |
| Queen / mother | **Alicent** (AU: stands where canon has Alysanne) | Alicent ✔ |
| Younger sister | **Helaena** | Helaena ✔ |
| The nephew | Viserys (minor, demoted) | — |

Authority: `intake/tentative-outline.md` (GUARD-4 name SETTLED: Gael) + `intake/GUARDS-register.md`
GUARD-4 + `design/run-02/timeline-and-family-tree.md` §1–2. The warehouse cards (`saerys-*`,
`viserys-i-targaryen` as father) predate the CL-005 era ruling and the Gael rename; they are stale
and pending the run-03 migration. **When a card and this library disagree on a name or the era, this
library's layer is correct and the card is the thing to fix.** Specific *servant* names below are
**overridable placeholders** (naming is partly a principal call — cf. the still-open "what is the
maid's name?" question); the *functions* are the durable content.

Era anchor (PINNED, timeline §1): Jaehaerys's long peace; dragons abundant; Gael **b. ~84 AC**;
Book I ≈ **84–93 AC** (infant → age 9). Any routine below is the routine of *that* court in *that*
peace.

---

## The four documents

| File | Domain (one line) | Reach for it when authoring… |
|---|---|---|
| `the-household.md` | **The servants & handlers** — every person in Gael's daily orbit by function and rank; the below-stairs economy; the Kingsguard/gate watch; where the Book II maid comes from. | any scene with a body-servant, nurse, septa, maester, steward, guard, or below-stairs figure; "who is in the room"; who files reports; whose routine a heist exploits. |
| `the-day.md` | **Routines & patterns** — the hour-by-hour timetable across four age phases (swaddled infant → toddler → little princess → schoolroom child), plus the weekly Faith rhythm, the annual court calendar, meals, dress/the body, and sleep. | any "what is she supposed to be doing right now" question; pacing a day; the surveillance schedule a deviation has to fit inside; what the household believes the missing hours contained. |
| `the-script.md` | **Expectations & behaviors** — the "good princess" rubric, the Faith's gender-script, the dynasty/marriage machinery and its clock, the social meaning of dragonlessness, and the calibrated reward-and-punishment ladders. | the compliance mask; what "performing piety" actually performs; the betrothal pressure; the cost of defiance; what the family wants her to *be*; the unsaid rules. |
| `INDEX.md` | this file — orientation + the seam map + candidate cards + open questions. | first stop; the seam map is the production tool. |

Reading order: `INDEX` → `the-household` (the people) → `the-day` (what they do, when) →
`the-script` (why, and what it costs to refuse). The three docs are peers; each is standalone for its
domain.

---

## The seam map (the production tool)

For every ordinary-life element, where the MC-plot **hides inside it, exploits it, or subverts it.**
This is the table to scan when you want to ground a beat — find the ordinary thing, and the right-hand
column tells you the deviation already in the outline. Outline citations are to
`intake/tentative-outline.md`.

| Ordinary-life element (the baseline) | Where the plot uses / subverts it (the deviation) |
|---|---|
| The cradle-egg, placed to be **prayed over** (like canon Rhaena) | She **grinds and eats it** (I.1). The most sacred furniture of her station is her first reagent. |
| The wet-nurse / nursery watch — an infant is **never unobserved** | The cultivation must happen in the *gaps*: when "monitored by worried nanny + Alicent," she stops (I.1 step 6). The watch IS the obstacle. |
| The doting nanny, the soothing toy | The hard wooden toy (expressed interest, indulged) is the tool she chips the shell with (I.1 step 4–5). Indulgence is weaponised. |
| The maester's visit — routine concern for an odd child | The reconnaissance + the heist (I.2): his cabinet is the target; "exploit toddler-underestimation to escape minders." |
| **Septa-as-handler** + the lesson timetable | The schedule she escapes; meditation replaces needlework; the lesson-block is the alibi-frame for the missing hours. (`the-day` Phase 2–3.) |
| Needlework / deportment / "stillness" as the core curriculum | The trained stillness becomes the **meditation cover** and the compliance mask (I.3 "outward compliance"). The cage trains the exact skill the escape needs. |
| Daily devotions in the family sept | She "attends with appropriate piety" and **counts acoustics and candle-intervals** (loc-maegors-holdfast). Performed faith over genuine; the anti-Faith curdle (I.3). |
| The **cage is the attendant, not the door** | Every operation is "how do I account for the next two hours" — subtract a watcher, not unlock a wall. The whole heist-method (sight→plan→implement→reward) is a *watcher-accounting* problem. |
| The King's indulgence of a "miracle child" | The **King's-hand note** — the master key that overrules every chaperone (loophole 1). His love is the cage AND the skeleton key. |
| **A new maid assigned after a reshuffle** (ordinary household churn) | The Book II maid — her one channel to the outside, face/hands/legs of the startup (II.1). She is recruited *out of this roster*. |
| The below-stairs servant economy (patronage, not coin) | Loophole 5: she becomes the person below-stairs people owe; the gate guard who is "a beneficiary of below-stairs faction patronage" (loc-maegors-holdfast). The maid recruits a cousin (II.2). |
| Charity / tending the sick — an **expected, unsupervised** noble duty | Loophole 2 `[KEYSTONE]`: the sick-house / apothecary cover for the whole trade-and-medicine network. |
| The "delicate / sickly princess" excused from duties | Loophole 3: performed illness — "the scholar-princess has always been delicate" buys unmonitored hours (III.4 delay tactic). |
| **Eccentric-royal latitude** — "it's the dragon blood" | Loophole 4: the deviance budget. Helaena already spends it on insects; Gael spends it on "collecting." |
| Stewardship — a noblewoman runs accounts & the household book | Loophole 6 + the double-entry cover: "doodling" no one audits because a girl can't be running anything (II.2 sexism-as-cover). |
| The **betrothal clock** (betrothed young ~2–7, wed ~13) | The Northern pacification-marriage — the maximum threat to SOLITUDE; the deadline the ship races (II.4, III.4). |
| **Dragonlessness** = value-collapse to pure bloodline; pity/mockery | "Dragonbane" epithet (I.1); a dragonless princess is spent cheap on a minor lord (Alicent interlude). The discount is the stakes. |
| Targaryen **incest-marriage norm** | The Daemon appraisal + the modern-revulsion horror (I.4); the purification obsession is born from it. |
| Being dressed, bathed, hair-tended — **the body is handled, never private** | Privacy is an *achievement*, not a default; every excursion (III.2) is stolen from a life with no unwatched body. The tempering of the maid (III.5) is the one body she acts *on*, not *through*. |
| Sleeping never alone (a body-servant on a truckle bed) | The night excursions (III.2) require the maid to perform "the princess is meditating and must not be disturbed" — defeating the never-alone rule. |
| The calibrated punishment ladder (doubled septa-hours; the **sept** as disposal) | I.3 "doubled septa training. Pure punishment." The septa herself is *sent to a sept* (saerys-septa card) — the disposal mechanism turned on the handler. |

**How to use it:** identify the ordinary element a scene touches; the right column is the deviation
already planned; write the scene so the baseline is legible *under* the deviation (the reader should
feel the normal day the strange day is wearing as a disguise).

---

## Servant cards (BUILT) — the women around Gael

The body/nursery servant **personas are now authored** (2026-06-08) — 10 cards across four categories
(wet-nurses, nursemaids/nannies, chamber-maids, tiring-women), with reasonable per-category profiles
and a maid-candidate menu (OQ-CL2). Roster + profiles: **`the-household-roster.md`**. Cards live in
`active-project/warehouse/` (`mella-wet-nurse`, `bessa-wet-nurse`, `mistress-bryony`,
`cissa-nursemaid`, `wenda-the-rocker`, `nona-chambermaid`, `pella-chambermaid`, `marra-chambermaid`,
`mistress-orla-wardrobe`, `nesta-tiring-girl`). The septa is already carded (`saerys-septa`). Still
unbuilt (future batch): the **maester**, the **masters of accomplishments**, the **companion girls**.

## Candidate cards (for principal triage — conditions/remaining personas)

Flagged where this library's content might warrant a card if a beat makes it load-bearing. All
project-scoped; none are library-scope personas/locations.

| Slug | Class | Source doc | One-line purpose |
|---|---|---|---|
| `cond-royal-household-roster` | condition | the-household | The named establishment of Gael's household — every office, current holder (placeholder names), wage/loyalty, reporting line — as a single quick-ref the impersonator/studio can consult for "who is in the room." |
| `cond-princess-daily-horarium` | condition | the-day | The hour-by-hour timetable per age phase, formatted as a surveillance-schedule lookup (when is she watched, by whom, how the gap opens). |
| `cond-court-calendar-jaehaerys-peace` | condition | the-day | The annual cycle (name-days, the seven feast-days, court occasions, seasonal provisioning) — the rhythm beats must place themselves against. |
| `cond-good-princess-rubric` | condition | the-script | The deportment/Faith/dynasty expectation-set as the explicit standard the compliance mask performs against — auditor calibration for "is she on-mask here." |
| `cond-betrothal-machinery` | condition | the-script | How a match is actually made (who decides, the steps, the clock) — production reference for the betrothal-clock beats. |
| ~~`persona: the-head-nursemaid`~~ | persona | the-household | ✅ BUILT as `mistress-bryony` (+ the full nursery/body-servant roster — see above). |
| `persona: the-grand-maester` | persona | the-household | The household maester (era-correct; see canon-uncertain #1) — likely load-bearing by I.2 (the heist target). NOT YET BUILT (next batch). |

The **Book II maid** is deliberately NOT listed as a candidate here: she is a principal-naming
decision still open, and she is a co-protagonist, not household furniture. This library only describes
the *roster she is drawn from* (the-household §"the seam: where the maid comes from").

---

## `[canon-uncertain]` worklist

Items to verify against Fire & Blood / canon in a future fidelity pass.

1. **The Grand Maester during Jaehaerys's reign in our window (~84–93 AC).** Canon cycles several
   (Benifer, Elysar, later Runciter); the exact holder in 84–93 is fuzzy and AU-perturbed anyway. The
   household maester is kept as a function here; name/identity hedged.
2. Whether a Targaryen royal nursery used **milk-kin / "milk-brother" politics** in *this* generation
   (the device is canon under Viserys I; projecting it onto Jaehaerys's nursery is an inference).
3. The precise **High Septon / Faith posture toward the incest compromise** in the Jaehaerys peace as
   it would shape a princess's devotional script (the compromise is canon; its day-to-day catechism is
   invented).
4. Exact **betrothal ages** as a norm vs. cited instances (Baela & Rhaena betrothed ~2; Helaena wed
   ~13 are instances; the *range* is generalised here).
5. Whether the AU substitution (Alicent for Alysanne as Jaehaerys's queen) perturbs the **number and
   identity of nursery-sharing siblings** — the baseline assumes a populated royal nursery but does
   not pin the full sibling set (that's a family-tree call, timeline §6 open).

---

## Open questions (for the principal)

- **OQ-CL1 — Granularity of save.** This library is authored as design-reference (the
  cultivation-library model). Promote any of it to *cards* now (see candidate list), or leave as
  reference until a beat makes it load-bearing? (Default: leave as reference; promote on demand.)
- **OQ-CL2 — The maid's origin.** The baseline says the Book II maid is drawn from the post-Daemon
  household reshuffle (II.1). Is she (a) an existing junior body-servant promoted, (b) a fresh outside
  hire, or (c) a below-stairs faction recruit? This shapes how much of the roster she already knows.
- **OQ-CL3 — Servant names.** Adopt the placeholder names, replace them, or defer to a margit naming
  pass (mindful of the CLAUDE.md name-novelty caution about library-slug leakage)?
- **OQ-CL4 — Sibling set.** How populated is the royal nursery Gael shares (beyond Helaena)? Affects
  the household scale and the milk-kin device (canon-uncertain #2, #5).

---

*Authored 2026-06-08. Library location: `active-project/design/counterfactual-life/`. Process that
produced it (and reusable for other characters): `design/counterfactual-baseline-process.md`.
Registered in `staff/showrunner/memory.md` (routing) and pointed to from
`staff/showrunner/world-notes.md`. Carried as KEEP/reference through any `/and-reoutline` migration —
see `intake/INTAKE-RUNBOOK.md` artifact manifest.*
