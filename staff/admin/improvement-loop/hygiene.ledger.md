# hygiene ledger — artur (janitor)
# One entry per run. Append-only.

---

## Run 2026-06-11

### Sweep scope
- `active-project/staff/showrunner/parking-lot.md` (86 items)
- `active-project/staff/showrunner/memory.md` (13,401 lines)
- `active-project/staff/showrunner/cascade-checkpoint.md`
- `active-project/staff/showrunner/` — ledger files, context/grounding ledgers
- `active-project/staff/` — STM/LTM file sizes
- `active-project/theater/facets/`
- `active-project/staff/showrunner/_drafts/` (51 files)

### Findings (severity order)

**1. TRIVIAL — Duplicate 3-line section-header comment in parking-lot.md (lines 1126-1131)**
File: `active-project/staff/showrunner/parking-lot.md`
The comment block:
```
    # ── Session 2026-05-31 cold-read audit findings (sub-section b01 c01-c07) ──
    # Source: active-project/draft/_combined-b01-c01-c07-audit.md
    # Branch: session/audit-and-stitch-2026-05-31
```
appears twice in immediate succession (lines 1126-1128 and lines 1129-1131). The second copy is a paste duplicate.
**→ FIXED this run** (removed duplicate 3-line block).

**2. SOFT — Asymmetric ledger pair: grounding-ledger-b01-c19.md exists, context-ledger-b01-c19.md absent**
Expected by PROP-0020/0022 (Rule 17): /and-facets Phase 2.5 emits both files together. c19 has bones + draft; grounding-ledger but no context-ledger. Possibly the c19 facets run emitted only one file (silent-write pattern). Not a blocker (cascade-checkpoint is COMPLETE; no-ledger-revision run skipped the full facets chain). Route to **oskar** to confirm whether c19 /and-facets Phase 2.5 emitted both files at the time, and whether the missing context-ledger warrants a targeted /and-facets phase-2.5 spot-check.

**3. SOFT — Missing both ledgers for b01-c16 (context-ledger and grounding-ledger absent)**
c16 has bones + draft but neither context-ledger nor grounding-ledger. Consistent with c16 running before PROP-0020/0022 wiring, OR the facets pass not having emitted Phase 2.5 files. Same resolution path as finding #2. Route to **oskar** — confirm whether c16 preceded Phase 2.5 wiring and is therefore exempt, or whether it is a silent-write miss.

**4. SOFT — Stale `current` field in cascade-checkpoint.md**
`cascade-checkpoint.md` reads `status: COMPLETE` (all 20 chapters no-ledger-revised) but the `current` field still points to `{chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}`. The `status: COMPLETE` field correctly names the outcome; the `current` field is a cosmetic artifact of the last chapter processed. Not blocking anything. Route to **oskar** — if it causes orientation confusion on session re-open, a one-line update to `current: {chapter: b01c20, step: "COMPLETE"}` or nulling the field would close it.

**5. SOFT — 51 files in showrunner/_drafts/, oldest dated 2026-05-24**
Many are bones-drafts and attempt-level artifacts from early chapters (b01c01-b01c07). The archive subdir exists at `_drafts/2026-05-31-cleanup/`. Files pre-dating that cleanup may be candidates for archiving or deletion, but content ownership is oskar/showrunner's. Not touching without explicit clearance. Route to **oskar** for a _drafts/ triage pass.

**6. SOFT — Large memory.md (13,401 lines)**
Expected for a 20-chapter book-length project with per-bone substance deltas. No schema violation; the schema requires per-bone deltas in showrunner memory. Not actionable as a hygiene fix. No route needed; noting for the record.

**7. SOFT — 86 parking-lot items, many open SOFT items targeting scope: "*"**
Items pl-2026-05-31-004 through pl-2026-06-01-cohere-005 are open SOFT items from a c01-c07 sub-section audit; most target `/and-write scope: "*"` depth-pass revisions. These are legitimate open findings awaiting principal-directed revision passes, not orphaned entries. No action needed.

### Action taken
**Fixed finding #1**: removed duplicate 3-line comment block at lines 1129-1131 of `active-project/staff/showrunner/parking-lot.md`.

Findings #2-5 routed to **oskar** via this ledger (no parking-lot items written — these are hygiene observations about ledger files and checkpoint state, not cross-chunk watch items for future command invocations).
