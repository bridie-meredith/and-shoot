# Hygiene Ledger — improvement-loop routine

Append-only. Each pass appends a dated block with findings + action taken.

---

## 2026-06-12 — Pass 1

**Sweep scope:** `active-project/` + `staff/admin/` + parking lot + draft files.
**Branch:** `claude/gifted-hawking-4wbexr`
**Project state:** `taylor-westeros-good-intentions` — COMPLETE, archived 2026-06-07. `active-project/` retained alongside `projects/taylor-westeros-good-intentions/` (both present; see Finding 3).

---

### Findings (severity-ordered)

**[MEDIUM] F1 — Duplicate parking-lot ID: `pl-2026-06-05-c17-001`**
- Location: `active-project/staff/showrunner/parking-lot.md` lines 2337 and 2375 (mirrored in `projects/taylor-westeros-good-intentions/staff/showrunner/parking-lot.md`).
- Two genuinely distinct entries were authored with the same ID:
  - Entry A (line 2337): `/and-facets b01c17 Phase 5 audit` — vibes ++ ops + prop-card referrals (signal-008/009). **Status: resolved.**
  - Entry B (line 2375): `/and-stitch b01-c17 Phase 9 cold-read` — b01c17 SHIPPED-WITH-CAVEATS / depth-pass watch. **Status: open.**
- External references (`studio/ltm.md`, `theater/_archive/`) use `pl-2026-06-05-c17-001(b)` which specifically targets sub-item (b) of Entry A. No external references point to Entry B by bare ID.
- Schema (`schemas/parking-lot.schema.md`) requires unique IDs.
- **Action: rename Entry B from `pl-2026-06-05-c17-001` → `pl-2026-06-05-c17-002` in both copies. (Trivial fix — no external reference break.)**

**[MEDIUM] F2 — Admin STM bloated: 116+ entries vs ~20 prescribed**
- File: `staff/admin/stm.md` — 128 lines, contains DEC-0001 through DEC-0116 (all decisions since project start).
- File header: "Pruned to ~20 entries at each session-open; anything still load-bearing gets promoted to LTM first."
- All entries are fully preserved in `decisions.md` (7627 lines, append-only). No information loss if pruned.
- **Route to: admin agent (owns stm.md) — prune to ~20 most recent entries at next session-open, promoting any load-bearing items to ltm.md first.**

**[LOW] F3 — Orphaned draft files at showrunner root (outside `_drafts/`)**
- Files: `b01c09-bones-draft-2026-05-31.md`, `b01c11-bones-draft.md`, `b01c11-draft.md`, `b01c15-bones-draft.md`, `b01c15-draft.md`, `b01c19-bones-draft.md`, `b01c20-draft.md` — sitting in `active-project/staff/showrunner/` directly.
- `_drafts/` directory exists with 51 files; a 2026-05-31-cleanup pass moved earlier files there. These 7 were missed.
- Non-blocking; project is archived.
- **Route to: oskar (foreman) — move these 7 files into `active-project/staff/showrunner/_drafts/` at next available pass.**

**[LOW] F4 — Missing context/grounding ledgers for b01-c16**
- `context-ledger-b01-c16.md` and `grounding-ledger-b01-c16.md` are absent from `active-project/staff/showrunner/`. All flanking chapters (c15, c17) have both.
- May be intentional (c16 Phase 2.5 may have scored FOLLOWABLE×ALIVE without opening the ledger). Project is archived; no chain impact.
- **Route to: oskar (foreman) — confirm whether c16 ledgers were intentionally absent (no spine holes / no grounding adds licensed) or silently dropped. If the latter, note for completeness in project archive.**

---

### Action taken

**F1 fixed (trivial-fix allowlist — schema ID uniqueness):** renamed `pl-2026-06-05-c17-001` → `pl-2026-06-05-c17-002` at Entry B in:
- `active-project/staff/showrunner/parking-lot.md` (line 2375)
- `projects/taylor-westeros-good-intentions/staff/showrunner/parking-lot.md` (same location)

No external references updated (none exist to Entry B by bare ID).

F2–F4: routing notes written above; no file changes beyond this ledger.
