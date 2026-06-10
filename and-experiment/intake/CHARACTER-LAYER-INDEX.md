# CHARACTER LAYER — index & status *(the Gael intake)*

**The front door to the character-design work.** Everything below was authored against **live span-A canon**
(Gael · b.84 AC · Jaehaerys father · Alicent mother · escape ~95 AC · the maid = Wylla). It is the
**source of truth for Phase-4 card derivation.** The stale `saerys-*` artifacts (Saerys / Viserys-father /
span-B Dance) are tombstoned/superseded, not deleted.

> **Recovery note for any session:** this branch has repeatedly had its local working tree reset between
> turns while **origin retained the pushed work.** Treat **origin as authoritative** — `git fetch` +
> `git reset --hard origin/<branch>` at the start of a session restores the full state.

---

## Story & comedy architecture (intake/)
| Artifact | What it is |
|---|---|
| `intake/spine.md` | The 3-book outline + tone/comedy architecture + reverse-angle format. Carries: Gael's six gags · the **recurring foil gags** (Alicent's per-chapter "what the hell"; the antagonist faces breaking) · the **three-faces antagonist** framing · the **per-chapter running-gag map** · resolved R2/R3/apex. |
| `intake/character-profiles.md` | Full profiles for the load-bearing roles (see below) + the **scholar ladder** (Barth ↔ the Maester near-miss relay). |
| `intake/character-reactions.md` | Per-foil comedy design (history · foibles · vibes · the tweak) on the coping-loop mechanism; revised after the 3-lens comedy review. |
| `intake/character-arc-ledger.md` | **Motivation (want + need) · state-axes · the growth/setback turn** for every load-bearing role, with per-entry fence-checks. The completeness guarantee: no role is a flat loop; the two designed non-growth roles (Gael's refusal, Jaehaerys's blindness) are dramatized, not absent. Seeds the substance state-axes / run-03 state-ledger. |
| `intake/reconciliation-worksheet.md` | The decisions record (gate rulings §D, comedy architecture §D-comedy, KEEP/ADAPT/SUPERSEDE dispositions §A, Phase-4 checklist §E). |
| `staff/reviews/comedy-angles-review-2026-06-09.md` | The three-lens comedy review (Youjo-Senki / progression-isekai / literary-snob) + the corrections applied. |

## The roles
- **Protagonist** — **Gael** (somewhat simple-minded monomaniac; the deflecting lens; six gags; three-spend fence; the clock stays broken).
- **Supporting protagonist** — **Wylla** (what-the-hell → converted **junior sister cultivator** of the sect that never is; tempered ≠ real cultivator).
- **Antagonist = Westeros itself, three faces** — **Jaehaerys** (institutional / the cage / the betrothal clock), **Otto** (predatory / the bestiary leak), **Septon Barth** (intellectual / closest-miss). Each has a recurring frustrated-plot-collapse gag.
- **Interlude narrator** — **Alicent** (fretting straight-man; the canon babying as cause; the per-chapter "what the hell" gag escalating to the bestiary break).

## Live cards (`and-experiment/warehouse/`)
**Leads:** `gael-targaryen` · `wylla-maid` · **Antagonist faces:** `jaehaerys-i-targaryen` · `otto-hightower` · `septon-barth` · **Narrator:** `alicent-hightower` · **Foils:** `maester-lorren` · `septa-aldith` · `hobb` · `daemon-targaryen` (10 total).
**Tombstoned/superseded:** `saerys-targaryen` → gael · `saerys-maester` → maester-lorren · `saerys-septa` → septa-aldith.
**Era-clean (kept):** the nursery cards (`cissa-nursemaid`, `bessa-wet-nurse`, `wenda-the-rocker`, …).

## Voice exemplars (`and-experiment/persona-exemplars/`)
- `gael-targaryen.md` — breezy, simple-minded, **concrete-action-first** (Rule-22; the opposite of the retired ledger-voice). Supersedes the Saerys exemplar.
- `wylla-maid.md` — plain warm Common Tongue + half-understood convert lingo; the junior-sister true-believer register.

## Seating caveats carried to Phase-4
- **Otto** and **Daemon** — canon birth-years (77 AC / 81 AC) make them too young in span-A as the adult predator/operator the roles need. **Barth is cleanly seated** (Hand 82–98 AC) and eases the Otto load. Settle in Phase-4.
- **Alicent / Jaehaerys** — the AU seating (Alicent as Jaehaerys's queen) is deliberate per GUARD-4; reconcile in Phase-4.
- **Open story slots** — Helaena's role; Alicent's arc-question (act on what the interlude knows? — recommended: knows-and-does-not-act).

---

## The pending decision — Phase-4 (`design/run-03/` migration)
The character layer is complete enough to migrate. **Phase-4 is a re-baseline, not additive,** and has a
dedicated command (**`/and-reoutline`**, the OUTLINE-INTAKE RUNBOOK). It performs irreversible operations:
tokenize `spine.md` into `design/run-03/`, carry KEEP/ADAPT artifacts, archive SUPERSEDE ones with
tombstones, re-found the state-ledger, run `check-threads.py`, and roll `memory.md` + `project-history.md`
forward. **This has not been started and should be run via the command, not hand-rolled** (hand-rolling
risks drift against what the command expects).

**Awaiting your steer — three ways to go:**
1. **Run Phase-4** — invoke `/and-reoutline` to migrate into `design/run-03/` (the worksheet's declared
   next phase).
2. **Keep elaborating the character layer** — exemplars for the three antagonist faces (impersonator-Tier-1
   eligible), or card the minor marks (Lothar Quint, the shipwright's agent, the Braavosi banker).
3. **Pivot** — settle the open seating/story slots (Otto/Daemon ages; Helaena; Alicent's arc) before any
   migration.

*Index authored 2026-06-09 as the capstone to the character-design session. All artifacts are on the branch
at the latest commit; origin is authoritative.*
