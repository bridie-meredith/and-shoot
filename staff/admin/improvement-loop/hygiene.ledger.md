# Hygiene Ledger — and-shoot
# Agent: artur (janitor)
# Schema: severity-ordered findings; one action per run; append-only.

---

## Run 2026-06-11 (branch: claude/gifted-hawking-kx44rd)

### Scope
Full sweep: STM/memory files, parking-lot, theater artifacts, state files, catalogue drift,
internal path references, proto-lines, facets, ARCHIVE_NOTE.

### Findings (severity order)

#### 1. MEDIUM — Orphaned duplicate in proto-lines (naming-convention violation)
**File:** `active-project/theater/proto-lines/b01c19.md`
**Duplicate of:** `active-project/theater/proto-lines/b01-c19.md`
**Evidence:** Both files are 39 lines; `diff` exits 0 (byte-for-byte identical).
**Root cause:** Non-canonical name written at emit time (missing hyphen between `b01` and `c19`);
canonical convention is `b<NN>-c<MM>` with hyphen (cf. b01-c18.md, b01-c20.md in same directory).
**Risk:** Phase-0 path-scanning agents may load the wrong slug; downstream consumers citing
`b01c19` would resolve to a stale/wrong proto-lines reference.
**Action taken:** Deleted `b01c19.md` (trivial-fix allowlist: naming-convention duplicates).

#### 2. SOFT — Facets catalogue description drift in ARCHIVE_NOTE
**File:** `active-project/ARCHIVE_NOTE.md` line 34
**Claim:** `theater/bones|facets|dialogue/ — full pipeline state`
**Actual state:** `theater/facets/` only holds c07 facets (13 files);
c01–c06 + c08–c20 facets are in `theater/_archive/` subdirectories.
The description overstates what the live facets directory contains.
**No action (routes to margit/showrunner):** Update ARCHIVE_NOTE line 34 to note that
c01–c06 + c08–c20 facets are archived under `theater/_archive/`, or promote the live
facets to match the claim. This is a completed/archived project — the factual claim
should match the directory state for future reader navigation.
**Routing:** margit (catalogue gatekeeper) or showrunner (memory holder).

#### 3. SOFT — proto-lines absent from ARCHIVE_NOTE inventory
**File:** `active-project/ARCHIVE_NOTE.md` line 34
**Gap:** `theater/proto-lines/` is not mentioned; it holds b01-c18.md, b01-c19.md,
b01-c20.md (now just two after finding-1 fix). Future readers navigating by ARCHIVE_NOTE
will not know proto-lines artifacts exist for the back third of the book.
**Routing:** showrunner to add a proto-lines line to the "Where things are" section.

#### 4. INFO — parking-lot.md size
`active-project/staff/showrunner/parking-lot.md` is 2973 lines. Append-only by schema;
no resolved item deletion expected. Functional but dense. No action.

#### 5. INFO — improvement-loop directory absent at sweep start
`staff/admin/improvement-loop/` did not exist. Created this run (ledger creation).

---

### Action taken
**FIXED:** Deleted `active-project/theater/proto-lines/b01c19.md` — exact duplicate of
`b01-c19.md`, non-canonical name format. No downstream consumers reference this slug
(proto-lines are consumed by chapter slug `b01-c19`).
