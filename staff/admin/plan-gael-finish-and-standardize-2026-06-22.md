# Plans — Finish gael-cultivation-comedy + Harden & Standardize the Process

**Date:** 2026-06-22 · **Branch:** `claude/gael-comedy-voice-review-ucwq18`
**Decisions (principal, 2026-06-22):** (1) Production venue = **here in and-shoot** (re-activate gael,
lift the migration freeze). (2) Finish bar = **stitched + cohered consolidated manuscript** per book;
polish (`/and-wrap`) stays deferred.

This document drafts two plans:
- **Plan A** — produce → render → revise gael into a finished (cohered-manuscript) product.
- **Plan B** — harden the local process from the review lessons + the full notes-harvest, then lift it
  to the repo standard.

The two interleave: Plan B Track 1 (exemplar + hygiene fixes) and the Track-2 continuity instruments must
be in place **before** Plan A's `/and-cast` gate and chapter production; Plan A's Book-I run is the **live
proving ground** for the hardened process (Plan B Track 3 validation).

> Sources: the comedy voice review (`projects/gael-cultivation-comedy/staff/reviews/
> comedy-voice-review-2026-06-22.md`) + a full process-lesson harvest across the project's `intake/`,
> `convergence/`, `design/`, `staff/`, and `staff/admin/` notes + `scripts/check-threads.py` (2026-06-22).

---

# PLAN A — Finish gael (and-shoot venue, cohered-manuscript bar)

**Starting state:** gael has a complete 3-book tokenized outline (`design/run-04/series-outline.md`,
19 beats, check-threads PASS), full comedy architecture (`intake/spine.md`), a ~14-member cast with
warehouse cards, and **2 of N** voice exemplars. It has **no and-shoot substance contracts** and
**no drafted prose**. The work is to bridge the planning into and-shoot's substance schema, then run
the proven production chain per `RUNBOOK.md`.

### Phase 0 — Re-activation + freeze-lift (one-time)
- Promote gael into the free `active-project/` slot. **Copy, don't move** (preservation invariant) —
  the `projects/gael-cultivation-comedy/` archive stays as provenance.
- Tombstone `MIGRATED-TO-AND-WRITE.md` → "re-activated in and-shoot 2026-06-22 for production;
  supersedes the and-write migration for the production venue." Record a **DEC** for the reversal.
- **Open decision (principal):** is the and-write `serial` copy now abandoned/downstream, or kept in
  sync? (Drives Plan B Track 3.4.) Recommend: and-shoot becomes canonical for production; and-write
  reconciled later.
- Stand up `active-project/staff/showrunner/memory.md` for the re-activated project.

### Phase 1 — Substance-contract backfill (serial planning → and-shoot schema)
The bridge. Re-run the and-shoot front half **using existing gael material as input**, not from scratch.
- Scaffold `active-project/` (audience trio, cast cards, exemplars, warehouse already exist in the
  archive — port them). **Open decision:** run `/and-project` fresh-seeded from the intake vs.
  hand-scaffold to match (since `/and-project` is non-re-runnable).
- `/and-series` — series chunk + structural commitments from the spine (3 books; length ranges;
  POV-locked-Gael + Wylla/Alicent interludes; cyclical=no; series-end = the escape, HYBRID/Dance parked).
- `/and-substance series` — the **signature**: state axes + **cost ledger** (the curdle ladder
  R0→R1→R2→R3→apex maps directly) + **antagonist pressure** (Westeros-as-three-faces) + chunk_targets +
  per-book Δ. Per **DEC-0115**, the signature must declare a **readability/concreteness floor** as a
  non-negotiable constraint the comic register coexists with.
- **Voice readiness (Plan B Track 1, EXECUTED HERE — not just a precondition):** author the 4 missing
  marquee exemplars (Alicent interlude-narrator, Barth, Jaehaerys, Otto) + retire the stale ones, so
  every POV / interlude / recurring-comedy voice is primed before any prose is rendered. This is the
  unblock for `/and-cast` Phase 5 *and* the hard precondition for Phase 2 voice fidelity. Listed inside
  Plan A so Plan A is self-contained on voice readiness.
- `/and-cast` — provision the roster from existing cards + **fire the series-level audit (the ONE
  blocking human checkpoint)**. ⚠ Phase 5 margit gate blocks on missing exemplars → satisfied by the
  Voice-readiness step above.
- `/and-substance book b01` (then b02, b03) — book drama + per-chapter Δ + chapter chunks + handoff.
- **Carry the continuity instruments across — don't re-invent (Track B2):** port the **GUARDS register**,
  the **PLANT/FIRE thread tokens + `thread-config.txt`**, the **state-ledger**, and the **time-anchor**
  into the active-project as live continuity surfaces, and **re-run `scripts/check-threads.py` to confirm
  PASS** on the converted contracts before any bones are authored. These are the cross-beat continuity
  checks the project already relied on; they must keep running through production.
- **Resolve the upstream gates the notes surface (preconditions, surfaced in Phase-0 pre-flight per
  B1.5 — do not let them evaporate again):** the cultivation-library **ruling-blocks T-1/T-2/T-3** gate
  Book-III cards; open **parking-lot SOFT items** (II.4 maimed-lady name+card; III.2 spared-rival
  name+card; black-cells location card; the `BLACK-CELLS`/`MISSING-SERVANTS` token-vs-register decision);
  the standing **Otto/Daemon AU-seating** call; the ~18 P1 / 8 P2 / 4 P3 **card-authoring backlog**.

### Phase 2 — Per-chapter production (RUNBOOK "Producing a chapter")
Per chapter unit (≈19–21: Book I = I.1–I.5 + Interlude; Book II = II.1–II.8; Book III = III.1–III.6 +
Epilogue — map to a `b<NN>c<MM>` scheme in Phase 1):
- `/and-substance chapter` → `/and-write` → `/and-review bones` → `/and-facets` → `/and-stitch`
  (Phase 9 cold-read + Phase 10 forward-thread). Use `--cascade`. Drive cap-bounded FAILs per RUNBOOK R2;
  single end-of-run summary per R4; silent mid-run per R3.
- **Voice check:** leads (gael, wylla) + the new antagonist/foil exemplars auto-resolve at dispatch
  (Rule 16); `active-project/voice-exemplar.md` calibrates `/and-stitch` Phase 4 voice-embodiment
  (Rule 22, no ledger register).
- **Readability check:** bones `FOLLOW-FAIL` pre-check → facets Phase 2.5 `FOLLOWABLE×ALIVE` → stitch
  Phase 9 naive-follow.
- **Plot check:** scene-conflict + dramatic-shape (chapter substance) → bones fidelity (`/and-review
  bones`) → forward-thread (stitch Phase 10).
- **Continuity check (per chapter, not just per book):** after each chapter's bones, re-run
  `check-threads.py` against the updated contracts + the state-ledger blast-radius table to confirm no
  PLANT/FIRE / GIFT→spend / curdle-rung break was introduced (Track B2.1/B2.4).
- **Soak / emotional-landing check (named gate):** does the dramatic + horror weight get room to *land*
  under the breezy comic lens — the project's "comedy on top, the reader keeps the ledger underneath"
  thesis? Mechanically covered by facets Phase 2.5 aliveness axis (`ALIVE`/`AIRLESS`) + grounding-ledger,
  `/and-stitch` Phase 6 buildup-preservation, and the dramatist dramatic-shape review — elevated here to
  a first-class gate because the breezy register is precisely what can steamroll the weight (acute in
  Book III's horror undertow; the dead hatchling / executed servants / mother's grief must register).
- **Escalation check (gag discipline):** each recurring gag must demonstrably *build* toward a payoff,
  not merely recur ("recurrence cosplaying as escalation" — the 3-lens comedy-review finding). Staged,
  not asserted. (Track B1.7.)

### Phase 3 — Cross-chapter cohere + per-book QA
- Per book, after its chapters ship: `/and-cohere b0X` (cross-chapter cold-read; consumes revise queue;
  re-cascades until PASS-COHERE) — the **prose-level coherence loop** that complements the thread-level
  `check-threads.py` (Track B2.1/B2.2).
- Build consolidated `active-project/draft/b0X-manuscript.md` (derived; never hand-edit).
- `/and-review verdict b0X` (orchestrator-critic run-judge). `/and-postop` at book-mid + book-close.

### Phase 4 — Targeted revision pass (RUNBOOK revision protocol)
- Scope from cohere/postop/verdict queues + principal direction only (no invented targets).
- Discipline: archive-before-mutate, one reason at a time, `/and-write revise` → chain, re-thread,
  re-cohere, **re-run `check-threads.py`**, rebuild manuscript, stamp parking-lot resolution. Use the
  **state-ledger blast-radius table** to scope the ripple before editing (B2.4).
- **Watch-list from the voice review:** F5 documentary-channel density (Rule 22 texture); Book-III
  horror undertow rendered person-first ("they took her down to the black cells and she did not come back
  up"); the III.6 absent-arrival blank-line device; the mirror-flip asymmetry holding (awe withheld from
  Gael).

### Phase 5 — Final assembly
- Three cohered book manuscripts (+ optional single series manuscript). Terminal deliverable under
  polish-deferred.

---

# PLAN B — Harden the process, then standardize it

## Track B1 — Close the review findings + add recurrence guardrails
Each item: **Fix** (immediate) + **Guardrail** (prevents recurrence — the actual ask). All guardrails are
filed through the repo's own change-control: an admin **process-proposal** (`staff/admin/
process-proposals.md`, `schemas/admin-proposal.schema.md`) + a **DEC** — so the process changes are
themselves traceable. (Admin's process-critic discriminates content-failure vs process-failure via "could
a stricter version of the existing gate have caught this without becoming a different kind of gate?" —
`staff/admin/methodology.md`.)

1. **Missing marquee exemplars (F1/F6).**
   - Fix: author 4 load-bearing exemplars — `alicent-hightower` (interlude narrator + reclaimed warm-cage
     DNA), `septon-barth`, `jaehaerys-i-targaryen`, `otto-hightower` (voice notes already pulled), per
     `schemas/persona-exemplar.schema.md` + `staff/margit/exemplar-authoring-process.md`.
   - Guardrail: non-lead Tier-1 exemplars were *optional/queued*, not gated. Strengthen `/and-cast`
     Phase 5 margit gate to block on **every Tier-1 cast member** missing an exemplar (POV /
     interlude-narrator / recurring-comedy roles = impersonator-eligible = Tier-1). Wire into `and-cast`
     body + Rule 16.

2. **Stale exemplars mislabeled `dispatch-status: active` (F2/F3).**
   - Fix: retire `saerys-targaryen` / `saerys-septa` / `viserys-i` (`superseded` + `superseded_by`);
     re-home the septa register to `septa-aldith`; fold viserys warm-cage into Alicent.
   - Guardrail: `dispatch-status` is unmaintained (all 9 say `active`, incl. a superseded one). Add an
     enforced lifecycle enum (`active|superseded|reference|parked`) to the exemplar schema + a margit
     validation: `superseded_by` ⇒ `superseded`; an exemplar whose `persona-ref` doesn't resolve to a
     live/library card is flagged (hook into staleness-cascade).

3. **Exemplar↔cast roster drift (F1/F4).**
   - Fix: author an exemplar-coverage manifest for gael (live persona → exemplar; reference/parked).
   - Guardrail: margit coverage report at `/and-cast` + a `/and-review cast` sub-check that diffs roster
     vs. exemplar set (orphans + gaps). Adjacent to the CLAUDE.md "name-novelty / library-slug leak" OOS
     item — same family; consider folding.

4. **Rule-22 ledger-register cumulative texture (F5).**
   - Guardrail: add a **documentary-channel-density** check to `/and-stitch` Phase 9 + the audience
     cold-read cards — distinct from the per-line ledger ban. The reverse-angle format concentrates
     documentary register (letters/reports/gossip-logs); flag when it dominates a chapter even where each
     instance is individually licensed as character/channel.

5. **Meta-lesson: "optional next-step work silently never happens" (root of F1/F6 + the "nothing
   drafted / where are we" confusion).** The project paused at a decision point with named-but-unexecuted
   work, changed homes, and the queue evaporated into an index paragraph.
   - Guardrail: route "pending optional elaboration" through the **parking lot** (owning command +
     status), not prose in an index. Strengthen production-chain Phase-0 to surface **pre-production
     readiness gaps** (exemplar coverage, substance-contract completeness, open ruling-blocks, card
     backlog) as explicit pre-flight blocks.

6. **Rename / era-reseat drift across layers (harvest B).** Saerys→Gael residue persisted for months
   (`the-factor` still cites `saerys-targaryen`); mis-ERA'd cards (`helaena-122ac`, `viserys-i`-as-father)
   are *worse than mis-named* — "do NOT co-cast with the correct-era cards as-is" (`time-anchor.md §5`).
   - Fix: single-pass cross-reference sweep for residual `saerys-*` / wrong-era references.
   - Guardrail: on any rename or era-reseat, dispatch a **fixer to update ALL cross-references in one
     pass** (not scattered); margit flags any card whose name/era doesn't match the live frame. Extends
     B1.2's staleness check.

7. **Running-gag "recurrence cosplaying as escalation" (harvest B; the 3-lens comedy review).** "Only the
   bestiary and Hobb genuinely build toward a payoff; the others are recurrence cosplaying as escalation,"
   root-caused to "asserted-not-staged."
   - Guardrail: an **escalation-audit before bones commit** — each recurring gag must demonstrably build
     toward a payoff, staged on the page, not asserted. Wire as a dramatist/auditor check at
     `/and-write` (surfaced as the Plan A Phase-2 escalation check).

8. **Authority-supersession opacity (harvest B; layered run-01→04).** Finding the canonical file required
   consulting multiple "SUPERSEDED by" header notes; recurring mistake = treating a stale layer as canon.
   - Guardrail: one **visible drift table** per project (✅ CURRENT / ⚠ STALE / ❌ SUPERSEDED + a router),
     the `time-anchor §5` pattern generalized beyond time to any cross-layer authority. Never delete;
     always route. (Pairs with Track B2.5.)

## Track B2 — Continuity & coherence machinery (standardize the reusable instruments)
The cross-beat **coherence** and **continuity** checks the project ran (mostly at outline/beat level,
since no prose existed yet). Each must (a) keep running on gael through production [Plan A linkage] and
(b) become a repo-standard instrument. For each: *what it is · how it's standardized.*

- **B2.1 — `check-threads.py` + the thread-config exception model (the flagship — most portable).**
  Mechanical PLANT/FIRE causal-thread checker: orphaned plants, unplanted fires, `GIFT:`→spend ordering,
  curdle-rung completeness; non-zero exit on any new break (`scripts/check-threads.py`). The
  `thread-config.txt` `ALIAS` / `PLANT-ONLY` / `PAYOFF-ONLY` discipline declares *intentional non-1:1* so
  only NEW breaks surface (`design/run-04/thread-config.txt`). **Standardize:** a repo-wide continuity
  gate run at every outline/contract change + folded into `/and-review consistency` / `/and-cohere`;
  every project carries a `thread-config` with declared exceptions.

- **B2.2 — Cross-chapter cohere (the prose-level coherence loop).** `/and-cohere` + `/and-review cohere` —
  the existing and-shoot cross-chapter cold-read that consumes a revise queue until PASS-COHERE. This *is*
  the "between-chapters coherence check" at the prose level; it pairs with B2.1 (thread level).
  **Standardize:** make cohere cadence explicit in the new-work runbook (per-book + at sub-section
  boundaries), not opt-in-by-vibe.

- **B2.3 — GUARDS register (ratified-premise anchoring — highest-leverage continuity instrument).**
  Numbered, revisioned load-bearing premises with HONORED / RE-RATIFY / DROP checks, "never silently
  break one," and "ratify smuggled premises explicitly"; FENCE > FROZEN-CHAPTER > LOCKED-BEAT granularity
  (`intake/GUARDS-register.md`). **Standardize:** a GUARDS register is a standard planning surface;
  `/and-series` + `/and-substance` author and re-check it each pass; no silent fence breach.

- **B2.4 — State-ledger + blast-radius + change-propagation loop.** Per-chapter state vectors + a
  per-chapter downstream-break ("blast radius") table + the formal loop: slot → recompute ripple →
  **mechanical** (`check-threads.py`) **+ judgment** (dramatist shape / audience taste / auditor drift)
  audit → flag-with-options → minimal re-thread + a **separate opt-in Opportunities block**
  (`design/run-02/book-i-state-ledger.md`). **Standardize:** adopt the blast-radius table as the
  revision-impact surface in the RUNBOOK revision protocol. (Plan A: Books II–III blast-radius accrues as
  chapters are produced — currently incomplete.)

- **B2.5 — Single continuity authority + visible drift table.** One authority per contested fact + a
  ✅/⚠/❌ router, never delete (`design/time-anchor.md`). **Standardize:** generalize beyond time to any
  cross-layer authority (this is also B1.8's guardrail).

- **B2.6 — Convergence "fusion not selection" loop + scoped re-validation.** Diverge (lensed A/B/C
  generators) → critic emits a converged **skeleton** → **fusion** passes (not re-divergence) → 6-criteria
  test (Structure/Drama/Comedy/Theme/Canon-fit/"the rhymes hold"), **4-round cap**, a blocker retired only
  by a beat on the page; scoped re-check (guards-honored + did-criteria-regress) on already-converged
  spines (`design/convergence-process.md`). **Standardize:** the optional premise-development front-end
  for a new work — richer Round-0 seed → faster convergence.

- **B2.7 — Counterfactual-baseline + seam-map (optional worldbuilding pass).** Negative-space
  worldbuilding — "you draw the figure by carving out the ground"; deliverable is the seam map (per
  ordinary element: where the plot hides-in / exploits / subverts it) — "a baseline with no seam map is
  inert lore" (`design/counterfactual-baseline-process.md`). **Standardize:** an optional setting-heavy
  worldbuilding pass.

- **B2.8 — Coverage-audit (two-axis) + the OUTLINE-INTAKE runbook.** Margit two-axis coverage audit
  (entities-met × system-framework) → HAVE/GAP/REUSED + P1–P4 + ruling-block gates
  (`staff/margit/coverage-audit-2026-06-06.md`); the `/and-reoutline` re-baseline protocol with its five
  decision rules — provenance-sacred / premises-beat-structure / tentative-is-OK / reuse>rebuild /
  one-human-gate (`intake/INTAKE-RUNBOOK.md`). **Standardize:** generalize the coverage-audit template;
  `/and-reoutline` already carries the intake runbook.

## Track B3 — Lift the process to the repo standard (authoring new works)
**Tension to resolve first:** and-shoot's existing standard is the **substance pipeline**
(`/and-project`→`/and-series`→`/and-substance`→`/and-cast`→chain). The gael process pioneered
**spine-first** authoring (idea-injection into a living spine + per-chapter multiple-choice narrowing —
formalized as the `serial` type in and-write). "Standardize the gael process" = reconcile these.

- **B3.1 — Decide the model (open decision, recommend):** *augment*, not *replace*. Keep the proven
  substance pipeline; import the spine-first + continuity instruments (Track B2) — the spine as a richer
  planning artifact feeding `/and-substance`; per-chapter narrowing as an `/and-substance chapter`
  enhancement; the serial `/spine`,`/narrow`,`/chapter` ideas as front-end options.
- **B3.2 — Generalize project-activation:** a new-work template/checklist embedding the hardened gates —
  exemplar-coverage, substance-contract completeness, the Track-B2 continuity instruments (GUARDS +
  thread-config + check-threads + state-ledger + drift-table), Rule-22/readability tracks,
  consolidated-manuscript discipline.
- **B3.3 — Codify in the authoritative surfaces:** `CLAUDE.md` (rules + standardized flow); `RUNBOOK.md`
  (add a "Starting a new work" protocol beside "Producing a chapter" / "Revisions"; add the
  **origin-authoritative session-recovery rule** — `git fetch` + `git reset --hard origin/<branch>` at
  session-open when local trees reset between turns, per `CHARACTER-LAYER-INDEX.md`); command bodies
  (`.claude/commands/*.md`); schemas (exemplar lifecycle, coverage manifest, thread-config); library
  assets (margit QC, exemplar-authoring-process, the continuity-instrument process docs, audience /
  orchestrator-critic cards).
- **B3.4 — Reconcile with and-write** (if it stays alive) so the repos don't re-diverge — ties to Plan A
  Phase 0.
- **B3.5 — Validation:** the gael Book-I run (Plan A Phase 2) is the **live proving run** for the hardened
  gates — the same "validate on a live chapter" discipline used for PROP-0032 / the readability overhaul.

---

## Cross-plan order of operations
1. **B1 immediate fixes** (4 exemplars + hygiene + coverage manifest + the rename/era sweep) — required
   before Plan A `/and-cast`.
2. **A Phase 0–1** (re-activate + substance-contract backfill) — with B1 guardrails + the Track-B2
   continuity instruments ported and `check-threads.py` PASS confirmed.
3. **A Phase 2, Book I** — the live proving run (B3.5).
4. **Harvest** → refine B1/B2 guardrails + begin B3 codification.
5. **A Books II–III + cohere + revise** (Phases 2–4).
6. **B3 full standardization** + optional and-write reconciliation.

## Open decisions to confirm before execution
- Plan A Phase 0: is and-write's serial copy abandoned or kept in sync?
- Plan A Phase 1: `/and-project` fresh-seed vs. hand-scaffold the active-project (non-re-runnable command).
- Plan A Phase 1: the `b<NN>c<MM>` chapter-numbering scheme for the 19–21 beat units.
- Plan A Phase 1: resolve the standing **Otto/Daemon AU-seating** call + the **T-1/T-2/T-3** ruling-blocks
  (gate Book-III cards) before their dependent chapters.
- Plan B B3.1: augment vs. replace the substance front-end with spine-first (recommend augment).
- Whether B1/B2 guardrails ship as admin process-proposals for principal triage (the repo's normal path)
  or are applied directly this session.
