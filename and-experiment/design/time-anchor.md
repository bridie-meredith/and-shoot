# Time Anchor — the single source of truth for "when"

**Status:** THE authority for story-time on the **live Gael layer**. Supersedes
`design/run-02/timeline-and-family-tree.md` **§1 (WHEN)** and every scattered era/age claim in older
artifacts (see the drift table, §5). Where any other file disagrees with this one about a date, an
age, or the series span, **this file wins** and the other file is stale. Family tree (timeline §2),
magic rules (timeline §3), and the fence reconciliation (timeline §4) are NOT superseded here — only
*time*.

**Why this file exists.** The project moved its era once (Viserys I → Jaehaerys I, CL-002) and
rescoped its span once (Dance-finale → childhood-escape, the outline intake) — but each move left the
prior time-assumption alive in files that were never reconciled. The result is that "when is this
story / how old is Gael / how long does it run" has three different answers scattered across the repo.
This file pins one answer and makes the drift visible. Development chronology that produced the mess:
`staff/showrunner/project-history.md`.

**Authored:** 2026-06-08.

---

## 1. The two clocks (don't confuse them)

There are two unrelated "times" in this project and most of the confusion comes from mixing them:

| Clock | What it measures | Where it lives | Reckoned in |
|---|---|---|---|
| **STORY time** | when the fiction is set; Gael's age; the series span | this file (§2–§4) | AC (After the Conquest) + Gael's age |
| **PRODUCTION time** | when *we* made each decision; which layer supersedes which | `project-history.md` + git/CL log | calendar dates (2026-06-05 … ) + CL-/Round numbers |

This file is the **story clock**. When someone says "the timeline is confusing," ask which clock they
mean — the in-world dates (here) or the development history (`project-history.md`).

---

## 2. Story-time anchor (RATIFIED)

**Era.** The reign of **Jaehaerys I** ("the Old King" / "the Conciliator") — the long peace, the
height of Targaryen dragon-numbers. *Not* Viserys I's reign; *not* the Dance lead-up. (GUARD-4,
CL-002. This **retired** the run-01/convergence/cards assumption of the Viserys-I era — see §5.)

**The anchor formula (PINNED).** Gael is **born ~84 AC**. Therefore, for any scene:

> **`Gael's age = year_AC − 84`**  ·  **`year_AC = 84 + Gael's age`**

This single equation is the anchor. Every age below is derived from it; every date below is derived
from it. (The rename Saerys→Gael did **not** move the birth year; the formula is unchanged from
timeline §1.)

**The canon weather window (84 → ~95 AC).** The whole series sits inside the Conciliator's peace:
- Dragons are **abundant** (the Dragonpit full) → magical fuel is plentiful, which matters for the
  cultivation acquisition-engine.
- The realm is **stable and at peace**. The Great Council (101 AC), Jaehaerys's death (103 AC), and
  the Dance (129–131 AC) are **all future and out of frame** — the nearest, Jaehaerys's death, falls
  ~8 years *after* the series ends (see §4).
- Gael is **setting-blind** throughout: she never names Westeros, the Targaryens, the era, or any of
  this. The reader sees the Conciliator's peace; she sees a sect/clan in a golden age.

**Consistency rule (enforce on every chapter):** a chapter must place Gael's age at `year_AC − 84`
AND keep the political weather at "stable long peace." Nothing in the realm tilts toward succession or
war inside the series window — that only begins after 101 AC, long after the last page.

---

## 3. Per-book & per-chapter anchor table (the Gael / intake structure)

Derived from `intake/tentative-outline.md` (3 books: the cage / the blind machine / the narrow
escape) via the §2 formula. **This replaces the old "Book I = 84–93 AC" pin**, which assumed the
pre-intake 11-chapter Book I; the intake consolidated Book I to **5 chapters + the Alicent interlude**,
ending at ~age 6. The intake's per-chapter ages form a clean, continuous 84→95 sequence with **no real
overlap** (the apparent overlap in the stale memory.md book-deltas is the retired 11-ch numbering).

### Book I — *the cage* (5 ch + interlude) · age 0 → ~6 · **84 → ~90 AC**
| Ch | Beat (short) | Age | year AC |
|----|---|---|---|
| I.1 | dragonbane (infant; eats the egg) | infant (0–1) | 84 |
| I.2 | the-heist (maester's still-room) | ~2–3 | 86–87 |
| I.3 | the-cage (Jaehaerys's talk; septa doubled) | ~3–5 | 87–89 |
| I.4 | valyrian-beauty (Daemon appraisal) | ~5–6 | 89–90 |
| I.5 | the-bond-breaker (Daemon's dragon drained) | ~6 | 90 |
| Interlude | Alicent POV; the betrothal seed | ~6 | 90 |

### Book II — *the blind machine* (8 ch) · age ~6 → ~9 · **~90 → ~93 AC**
| Ch | Beat (short) | Age | year AC |
|----|---|---|---|
| II.1 | the recluse (the maid arrives) | ~6–7 | 90–91 |
| II.2 | the startup | ~7 | 91 |
| II.3 | the world map (reagent map) | ~7–8 | 91–92 |
| II.4 | the betrothal (Northern match; the clock) | ~8 | 92 |
| II.5 | the compromise (maid pressured) | ~8–9 | 92–93 |
| II.6 | the source (source-not-pool reframe) | ~8–9 | 92–93 |
| II.7 | the threat (maid endangered) | ~9 | 93 |
| II.8 | nothing here is mine (the ship plan) | ~9 | 93 |

### Book III — *the narrow escape* (6 ch) · age ~9 → ~11 · **~93 → ~95 AC**
| Ch | Beat (short) | Age | year AC |
|----|---|---|---|
| III.1 | the commission (ship ordered) | ~9 | 93 |
| III.2 | the excursions (first time outside) | ~9–10 | 93–94 |
| III.3 | the greedy factor | ~10 | 94 |
| III.4 | the deadline (betrothal accelerates) | ~10 | 94 |
| III.5 | the tempering (the one external spend) | ~10–11 | 94–95 |
| III.6 | the narrow escape (the ship sails) | ~11 | 95 |
| Epilogue | two girls on a ship, sailing south | ~11 | ~95 |

**Series span: 84 → ~95 AC · Gael age 0 → ~11 · ~11 years, entirely inside the long peace.**

> Ages are deliberately ranged (a chapter may cover months). If a beat needs a firmer age, pin it and
> back-solve the year with §2; if it needs a firmer year, do the inverse. Birth year is movable ±a few
> years if a later beat demands it (timeline §6) — but if you move it, you move the *whole* table, and
> you update this file, not a chapter in isolation.

---

## 4. The one open fork — the series SPAN (needs a principal ruling)

This is the single genuine time-contradiction left by the layering, and it is a **story decision, not
a reconciliation** — so it is flagged, not silently resolved (per the project's "ratify smuggled
premises" rule). The two newest authoritative layers disagree:

| | **A — short / escape span** (the intake) | **B — long / Dance span** (the old timeline) |
|---|---|---|
| Ends | childhood escape; two girls on a ship | the Dance of the Dragons |
| Final age / year | ~11 / ~95 AC | ~45 / 129 AC (unaged via longevity) |
| Books II–III cover | ~90–95 AC (a few years) | 93 → 129 AC (decades) |
| Climax | the narrow escape (III.6) | III.5 "a battlefield of dragon-corpses" |
| Curdle ladder tops at | R2–R3 (maid-threat / factor); tempering = the **anti-curdle** | R4 (the dead-dragon field) |
| Jaehaerys's death (103) | **after** the series — out of frame | mid-series — the father-king "spend" |
| Source | `intake/tentative-outline.md` (latest layer; GUARD-4 name SETTLED) | `timeline-and-family-tree.md` §5 ("Dance — RECOMMENDED") |

**These are incompatible.** The intake didn't argue against the Dance; it **rescoped past it** — its
whole structure (3 books, the maid, the ship, the ages above) only closes on span A, and it silently
drops span B's R4 apex, the dead-dragon finale, the longevity payoff, and the Jaehaerys-death spend.

**Working default (this file): span A (short / escape), as tabled in §3.** Rationale: the intake is
the latest ratified layer; the active scaffolding (the counterfactual-life library; this anchoring) is
all on the Gael/intake track; and span A is internally complete while span B is now orphaned by the
intake's structure.

**⚠ Principal ruling required to make it official.** Adopting span A formally **retires**: the
Dance-of-the-Dragons finale, curdle rung **R4** (dead-dragon field), the "will the immortal come down
at 45" longevity tragedy, and Jaehaerys's 103 AC death as the father-king gift→spend. Those were
"RECOMMENDED" by the old timeline and are load-bearing in the frozen `convergence/` outline and the
run-02 ledger's cross-book invariants. If the principal wants span B (or a hybrid — escape now, Dance
in a later book), §3 changes wholesale. **Until ruled: §3 is the working assumption; do not build
late-series beats that depend on the Dance without confirming.**

---

## 5. Drift table — every time-bearing artifact & its status

The anchoring made visible: which files carry which time-assumption, and what to do. "Stale" ≠ wrong
to keep — these are preserved history; they just must **defer to this file** on time.

| Artifact | Time-assumption it carries | Status | Action |
|---|---|---|---|
| **this file** | Jaehaerys; b.84; span A (84→95) | ✅ CURRENT | the authority |
| `timeline-and-family-tree.md` §1 | Jaehaerys; b.84; **Book I 84–93**; span B recommended | ⚠ PARTLY STALE | §1 superseded here (Book-I end-date + span); §2–6 still good. Header note added. |
| `intake/tentative-outline.md` | Jaehaerys (era intact); **Gael**; span A | ✅ CURRENT (story) | the structure §3 is derived from |
| `intake/GUARDS-register.md` GUARD-4 | Jaehaerys; b.84; "Dance = candidate climax" | ⚠ PARTLY STALE | era/birth current; the "Dance candidate" clause is span B — defer to §4. |
| `staff/showrunner/memory.md` | **Viserys I, ~119–131 AC**; Saerys; old book-deltas | ❌ STALE | constraints.settings + book-deltas predate CL-002 + the intake. Defer-note added (routing). Full fix = run-03 migration. |
| `staff/showrunner/world-notes.md` "Settings" | **Viserys I, ~119–131 AC** | ❌ STALE | already flagged in the counterfactual-life edit; defer-note here. |
| `design/run-01/constraints.md` | **Viserys I**; Saerys b.~116 | ❌ STALE (era) | frozen bedrock — KEEP as historical; the *institutions* (offices/loopholes) are era-agnostic and still good; only its dates/era are retired. |
| `convergence/**` (fusion-v2, ledger, chapters) | Viserys-I-implicit → CL-002 Jaehaerys; **span B** | ❄ FROZEN | never edited (baseline record). Reads as span B. Superseded by the intake; carried as history. |
| `design/run-02/book-i-state-ledger.md` | Jaehaerys (CL-002); Saerys; **11-ch Book I to 93**; span B invariants | ⚠ STALE (structure) | era right, but pre-intake (11-ch, Saerys, R4/Dance invariants). Run-03 migration ADAPTs it. |
| warehouse cards (`saerys-*`, `viserys-i-targaryen` as father) | mixed; Saerys; Viserys-as-father | ❌ STALE (naming) | naming drift already flagged in counterfactual-life INDEX; run-03 migration fixes. |

**Pattern:** everything authored **on or before 2026-06-06** carries the Viserys-I/Saerys/span-B
assumption; **CL-002 (06-07)** fixed the era but kept Saerys + span B + 11-ch Book I; **the intake
(06-07, later)** fixed the name + span + Book-I structure but didn't migrate the downstream files.
The run-03 migration (`/and-reoutline`) is the event that will retire the ❌/⚠ rows; until then, this
file is the bridge.

---

## 6. How to use this file

1. **Placing a scene in time:** read the age off §3, or compute it with §2. State the year only if a
   scene needs it (Gael is setting-blind — years are author-facing, never on the page).
2. **Checking a claim:** if another file gives a different age/year/span, it's in the §5 drift table —
   this file wins.
3. **Late-series beats:** confirm the §4 span ruling before building anything that depends on the
   Dance, the dead-dragon field (R4), or Jaehaerys's death.
4. **Moving the anchor:** if the birth year or span changes, edit **this file** (the whole §3 table
   re-derives from §2), then propagate — never patch a single chapter's date in isolation.
5. **Production-time questions** ("why does X say Viserys?", "what superseded what?"): not here — see
   `staff/showrunner/project-history.md`.

---

*Authored 2026-06-08. Peer authorities: `timeline-and-family-tree.md` (family + magic, non-time),
`intake/GUARDS-register.md` (premises). Development chronology: `staff/showrunner/project-history.md`.
Registered in `staff/showrunner/memory.md` (routing).*
