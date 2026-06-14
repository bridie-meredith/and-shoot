# Project History — the continuous development record

**What this is.** The **production-time** chronology of `and-experiment`: the layers the project
passed through, in order, with what each one established, what it superseded, and what un-reconciled
drift it left behind. This is the "history that explains the current state" — read it when something in
the repo seems to contradict something else, or when you need to know *which assumption a file was born
under*.

**This is the production clock, not the story clock.** Dates here are **calendar dates** (when *we*
made decisions) + CL-/Round numbers. For in-world dates / Gael's age / the series span, see
`design/time-anchor.md`. The two are easy to confuse; keep them apart.

**The one-sentence summary.** The whole project was built in **four days (2026-06-05 → 06-08)** but it
moved through **eight conceptual layers**, and because each layer staged its changes without migrating
the layers beneath it, the repo currently holds three different era-assumptions and two different
series-spans at once — all reconciled (for time) by `time-anchor.md`, and (for premises) pending the
run-03 migration.

**Authored:** 2026-06-08 (reconstructed from git log + the CL change-log + the convergence ledger).

---

## The reconciliation principle (why drift is everywhere but nothing is lost)

The project follows **"stage, don't overwrite"** (`design/convergence-process.md` +
`run-02/README.md`): a new decision is *staged* in a working layer (the ledger, a new run, the intake)
while the baseline beneath it is **preserved untouched** as the historical record. This is why
`convergence/` is frozen, why the ledger still says "Saerys," why cards still say "Viserys-as-father" —
none of it is a bug; it's preserved provenance waiting for a migration to roll it forward. The cost of
that discipline is **drift**: at any moment, older layers contradict newer ones. `time-anchor.md` (for
time) and the eventual run-03 migration (for everything else) are how the drift gets retired.

---

## The eight layers (in order)

### L0 — run-01 bible · 2026-06-05 (`d3c3ebf`, `b404b8d`)
The grounded bedrock. `design/run-01/{idea-board,constraints,treatment,book-outlines}.md`.
- **Established:** the premise (dragonless setting-blind reincarnator; cultivation-as-grief-armor; the
  cage + six loopholes + ship-heist toolkit); the institutional ground-truth (household offices,
  septa-handler, Maegor's, the Dragonpit).
- **Time-assumption:** **Saerys**, youngest daughter of **Viserys I & Alicent**, **b. ~116 AC**, Dance
  era **~119–131 AC**. ← the original era.
- **Left behind:** `constraints.md` is still written to this era. (Its *institutions* are
  era-agnostic and still good; only its dates are retired — `time-anchor.md` §5.)

### L1 — outline convergence · 2026-06-05 (`d3c3ebf` … `1144ace`; ledger Rounds 0–3)
The 3-lens convergence loop (`convergence/round-01..03`) fused run-01 into one accepted outline.
- **Established:** `convergence/round-03/fusion-v2.md` (the ★ accepted outline); the three rhymes
  (one-method-three-Locks; gift→spend; reagent↔geography↔tone); **the Cauldron-Belly** + **poison-path
  + mithridatism** (Round 3 principal enrichment); the cast (Daenys the lover; Ser Harwin; Nymeria).
- **Time-assumption:** unchanged from L0 (Viserys-I, Saerys); **span B** — to the Dance, the
  "dead-dragon field" finale.
- **Left behind:** `convergence/**` is **frozen** (never edited again); reads as Viserys-I + span B.

### L2 — chapter convergence · 2026-06-05 (`a7855e4` … `8034510`)
A sub-loop expanded the spine into a **30-chapter (10/10/10)** outline
(`convergence/chapters/round-02/fusion.md`).
- **Established:** the chapter-granularity build target; `chapters-ledger.md`.
- **Time-assumption:** unchanged (Viserys-I, Saerys, span B).

### L3 — card build + cultivation library · 2026-06-05/06 (margit; `58f6cd1` … `4d2303d`, PR #98)
Reverse-derivation of apparatus from the outline. The 9-doc `cultivation-library/`; the warehouse card
set (`saerys-*`, `viserys-i-targaryen`, `helaena-122ac`, locations, props, conditions); the showrunner
`memory.md` written as a normal project.
- **Established:** the authoring substrate; the card warehouse; `memory.md` as state-of-record.
- **Time-assumption:** unchanged — **this is why the cards say Saerys + Viserys-as-father, and why
  `memory.md` says "Viserys I, ~119–131 AC."** They were born in the L0 era and never migrated.
- **Left behind:** the largest pool of stale naming/era artifacts (drift table, `time-anchor.md` §5).

### L4 — run-02 re-axis + state ledger · 2026-06-06 (`48d1808`, `a2957cd`, `5f10ac6`)
The principal re-axed the books around **two desires** (RESOURCE vs SOLITUDE) —
`design/restructured-books-two-desires.md` — and built the change-propagation instrument
`run-02/book-i-state-ledger.md` + the thread-checker (`scripts/check-threads.py`).
- **Established:** the two-desires frame; the per-chapter state ledger; the "stage a note → recompute →
  thread-audit" loop.
- **Time-assumption:** still Saerys / span B (era not yet moved).

### L5 — run-02 CL revisions · 2026-06-07 (`5822edd` … `b4a254d`; ledger Rounds 4–8)
Five chapter-note enrichments, staged in the ledger (baseline preserved). **This is where the era
moved.**
- **CL-001** — I.1 rewritten: dying reincarnated *infant*; *living* egg from Alicent; cultivation
  founded via sympathetic resonance; egg drained dead. Ratified GUARD-1/2/3.
- **CL-002** — ⭐ **THE ERA MOVE.** Viserys-I → **Jaehaerys I**. Jaehaerys = King/father; Alicent =
  Queen/mother (AU for Alysanne); Helaena = sister; Viserys → nephew. **Saerys b. ~84 AC**; Book I
  84–93. New authority `timeline-and-family-tree.md`. Also: cultivation is *real* (GUARD-1 rev-2).
  Span B kept ("Dance 129 recommended").
- **CL-003** — inserted I.2 toddler heist → **Book I = 11 chapters**.
- **CL-004** — acquisition (not charity) as the engine; **retracted the blood-path** (GUARD-1 rev-3,
  materials-only).
- **CL-005** — no healing hand (energy never spent outward).
- **Time-assumption after L5:** **Jaehaerys era** (fixed) — but still **Saerys**, still **span B**,
  still **11-ch Book I to age 9 / 93 AC**.
- **Left behind:** the ledger + timeline carry Jaehaerys but pre-date the rename and the span rescope.
  `memory.md`/`world-notes`/cards/constraints were **not** updated → the Viserys-I drift persists
  below this layer.

### L6 — outline intake / re-baseline · 2026-06-07 (`c0da10a`, `4fdb1f2`, `f422a9a`)
The principal brought a whole new tentative outline; the `intake/` scaffold + `/and-reoutline` runbook
were built; `intake/tentative-outline.md` was dropped (Book I REBOOT + full Books II & III).
- **Established (latest story layer):** **name SETTLED → Gael** (GUARD-4); the **3-book structure**
  (the cage / the blind machine / the narrow escape); the **maid** co-protagonist; the **ship**
  ending; visible dragon-kill at I.1; explicit isekai-awareness; lesbian MC.
- **Time-assumption — ⭐ THE SPAN RESCOPE.** Era intact (Jaehaerys), but the series is rescoped to a
  **childhood escape ending ~age 11 (~95 AC)** — **span A**. Book I consolidated to **5 ch + interlude
  (ends ~age 6)**, not 11 ch to age 9. The Dance finale, R4, and the longevity payoff are silently
  dropped.
- **Left behind:** the migration to `design/run-03/` is **NOT done** — the reconciliation worksheet is
  blank. So the intake (Gael, span A) sits *on top of* the ledger/timeline (Saerys, span B, 11-ch) and
  everything below (Viserys-I cards/memory). **This is the present state.** The era is twice-removed
  from the cards; the span is once-removed from the timeline.

### L7 — current scaffolding · 2026-06-08 (`fbb30d6`, this work)
Authoring forward on the live Gael layer while the migration is pending.
- `design/counterfactual-life/` — the ordinary-princess-life source library (authored to Gael /
  Jaehaerys / span-A).
- `design/time-anchor.md` + this file — pinning the story clock and recording the production clock.
- **Time-assumption:** the live layer — Gael, Jaehaerys, **span A** (with the span flagged for a
  principal ruling, `time-anchor.md` §4).

---

### L8 — run-03 intake migration (span-A REBOOT) · 2026-06-09 (`/and-reoutline`; merged to main)
The re-baseline ran. The Gael intake (`intake/spine.md` + the full character layer) became live canon;
span-B (Saerys / Viserys-father / the Dance) retired to provenance (parked, not deleted).
- **Character layer (authored + merged to main):** 5 profiles · 10 live span-A cards + 2 lead exemplars ·
  the 3-lens comedy review · the reframed spine (three-faces antagonist, per-chapter running-gag map,
  scholar ladder, gag ⑦ death-flags, Gael simple-minded, Wylla's conversion) · open slots resolved.
- **Phase-4:** `design/run-03/series-outline.md` (tokenized; check-threads PASS, R0–R4) · run-02 Book-I
  outline archived w/ tombstone · convergence-ledger Round 9 · saerys-* cards/exemplar tombstoned.
- **Cutover:** `memory.md` rolled forward to span-A · `time-anchor.md` §4 span fork **RULED HYBRID**
  (span A now, the Dance parked).
- **Still pending (staged):** `timeline-and-family-tree.md` §2 family-tree re-derive · state-ledger
  re-found on the 3-book structure. Open call: Otto/Daemon AU-age (default) vs rename.
- **Time-assumption:** Gael, Jaehaerys, **span A (84→95)** — now ruled, not flagged.

---

## Where the truth currently lives (quick map)

| Question | Authority |
|---|---|
| When / age / span (story time) | **`design/time-anchor.md`** |
| Who's who (family tree) + how magic works | `design/run-02/timeline-and-family-tree.md` §2–4 |
| Ratified premises (the GUARDS) | `intake/GUARDS-register.md` |
| The current story structure (chapters/beats) | **`design/run-03/series-outline.md`** (tokenized) + `intake/spine.md` (narrative) |
| Ordinary-life texture (servants/day/expectations) | `design/counterfactual-life/` |
| Per-chapter state vectors + blast radius | `design/run-02/book-i-state-ledger.md` (⚠ pre-intake: Saerys/11-ch/span-B) |
| The frozen pre-change baseline | `convergence/**` (❄ never edit) |
| Development history (this clock) | **this file** |

---

## The migration that retired the drift — DONE 2026-06-09 (L8)

The run-03 migration (`/and-reoutline`, a REBOOT) **ran and merged to main.** It created
`design/run-03/` from the intake (tokenized outline, check-threads PASS); carried the GUARDS + settled
the span fork (HYBRID); archived the superseded run-02 Book-I outline + the saerys-* cards/exemplar to
tombstones (never deleted); built the 10 live span-A cards; and rolled `memory.md` + this file forward.

**Residual (staged, tracked in `design/run-03/README.md` + worksheet §E):** two ADAPT carry-overs
remain — `timeline-and-family-tree.md` §2 family-tree re-derive (Gael/Jaehaerys/Alicent + seat the
antagonist faces) and the state-ledger re-found on the 3-book structure. One open creative call gates
the family tree: **Otto/Daemon seating — AU-age (default/recommended) vs rename.** Everything else is
on the live span-A layer.

---

*Authored 2026-06-08. Companion to `staff/showrunner/memory.md` (the state-of-record) and
`design/time-anchor.md` (the story clock). Registered in `memory.md` routing.*
