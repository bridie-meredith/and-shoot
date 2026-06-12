# hygiene ledger — and-shoot / active-project: taylor-westeros-good-intentions

Append-only. Each run appends a dated entry.

---

## Run 2026-06-12

**Branch:** claude/gifted-hawking-fs3bgq
**Repo state:** Book I complete (b01c01–b01c20 shipped; series-terminal). No active cascade.
**Improvement-loop bootstrap:** ledger created this run (directory was absent).

---

### Sweep findings (severity-ordered)

**SEV-1 — MEDIUM-HIGH: Actor STM/LTM stasis across all 11 actors**

All 11 actors in `active-project/actors/` carry STMs of 2–5 lines and LTMs of 1 line, uniformly reading "Series open; no events yet" (provisioned at `/and-cast` Phase 4, 2026-05-24). Book I is now complete — 20 chapters shipped; actors accumulated 20+ chapters of on-stage movement, moral arc progression, and state change. None of this is recorded in actor memory files. CLAUDE.md Rule §4: "Nothing changes without being recorded." The gap is real.

Affected actors: taylor-hebert-kl-122ac, otto-hightower, wren-stitch-maker-flea-bottom-ward, oswyn-mudway-flea-bottom-elder, septon-halvard-flea-bottom, jarvis-coin-kl-courier, sera-hightower-kl-122ac, criston-cole-122ac, alicent-hightower-122ac, rhaenyra-targaryen-122ac, aemond-targaryen-122ac.

Routing: **oskar** (owns STM formats + memory schemas; studio housing).

---

**SEV-2 — LOW: Dead-letter SOFT parking-lot items targeting shipped chapters**

60 open parking-lot items total; 4 HARD (pl-2026-06-04-002, pl-2026-06-04-c15-004, pl-2026-06-04-c16-001, pl-2026-06-05-c19-deptpass — these are legitimate depth-pass gates for `/and-review verdict b01`).

~13 SOFT items target commands already completed on shipped chapters (b01c01–b01c07): e.g., pl-2026-05-25-006 (/and-stitch b01c01), pl-2026-05-25-007/011/012/015/016 (/and-write b01c01), pl-2026-05-25-014/019 (/and-facets b01c01/b01c02), pl-2026-05-27-002 (/and-write b01c04), pl-2026-05-30-002 (/and-write b01c06), pl-2026-05-31-001/004 (/and-write b01c07). These commands ran and shipped; the SOFT items were never resolved/disposed and will surface forever in Phase 0 scans. Not blocking, but accumulating noise.

Routing: **oskar** (triage/disposition decision — whether to mass-stamp resolved or accept as background noise before book verdict).

---

**SEV-3 — INFO: staff/showrunner/{stm,ltm}.md are empty (0 bytes)**

These are global staff/ stubs, not the active-project showrunner memory. Expected for a repo where showrunner memory lives in active-project/. Not a problem.

---

**SEV-4 — INFO: active-project/staff/showrunner/memory.md is 13,401 lines**

Expected accumulation for a 20-chapter production run. No immediate action.

---

**SEV-5 — INFO: active-project/theater/facets/ has only b01c07 facets**

All other chapter facets archived to theater/_archive/ at /and-stitch per design. Expected.

---

### Action taken

**Routing note to oskar — actor STM/LTM stasis (SEV-1)**

Written to parking lot as pl-2026-06-12-hygiene-001 (SOFT; target: oskar review; scope: active-project/actors/).

Actor memory has not advanced since /and-cast provisioning despite 20 chapters of production. Oskar should decide whether to (a) back-fill STM/LTM from memory.md chapter records before book archival, (b) accept the empty-at-book-close state as acceptable given the books[] chapter tracking in memory.md already holds all substance deltas, or (c) update STM format spec to clarify when actor memory is expected to advance during production. Before active-project/ is archived to projects/, this decision should be made.

---
