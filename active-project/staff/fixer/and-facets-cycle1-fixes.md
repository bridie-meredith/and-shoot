# Fix log — /and-facets b01c02 cycle-1 HARD findings

## SESSION-START — 2026-05-21T13:00:00Z — facets-b01c02-cycle1-fixes
dispatch: resolve 2 HARD findings (fault-001 CONSTRAINT, fault-002 RUBRIC-FIDELITY) from active-project/staff/auditor/facets-final-audit.md for chapter b01c02; SIGNAL findings not in scope
target: active-project/staff/exposition-author/glossed-terms.md + active-project/theater/facets/state-updates.md + active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + active-project/theater/proto-lines/b01-c02.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 2

## SESSION-START — 2026-05-21T14:00:00Z — facets-b01c02-cycle1-hard-fixes
dispatch: resolve 2 HARD findings (fault-001 CONSTRAINT, fault-002 RUBRIC-FIDELITY) from facets-final-audit.md for b01c02; minimum change only; SIGNAL findings not in scope
target: active-project/staff/exposition-author/glossed-terms.md + active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + active-project/theater/proto-lines/b01-c02.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 2

## fault-001 — NO-CHANGE-NEEDED — 2026-05-21T14:05:00Z
fault: glossed-terms.md stale water-carrier + near-witness entries and wrong @5 anchor on pressed-labor-sweep
scope: line
change: none — file already satisfies all three criteria
detail: water-carrier struck at line 19 (# STRUCK: comment with R2.5 rationale); near-witness struck at line 20 (# STRUCK: comment); pressed-labor-sweep first-mention-anchor already reads @4 at line 21
criteria met: yes — no spurious change applied
files touched: none

## fault-002 — RESOLVED — 2026-05-21T14:08:00Z
fault: state:13 POV actor-state entry anchored @26 with no narrator-interest co-citation at @26; narrator:5 fires at @25; cross-facet contract requires same-anchor NI co-citation for all actor:taylor.* entries
scope: line (two file edits; consolidated state-updates.md entry 13 was already @25 and required no edit)
change: (1) state-updates-taylor-hebert-kl-122ac.md entry 3: @26 → @25. (2) b01-c02.md: [state:13] moved from @26 to @25; @25 now [mem:2] [narrator:5] [state:6] [state:13] [vibes:11]; @26 now [state:7] only.
criteria met: yes — state:13 @25; narrator:5 @25 is NI co-citation spine; semantic coherence: @25 is the ledger-gap strike bone, the moment the categorical recognition surfaces before the held-hand disciplines against it; underline @26 is the physical act, correctly separated
files touched:
  - active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md
  - active-project/theater/proto-lines/b01-c02.md

## SESSION-END — 2026-05-21T14:08:00Z — facets-b01c02-cycle1-hard-fixes
findings-applied: 1 (fault-002)
findings-skipped: 1 (fault-001 — NO-CHANGE-NEEDED; criteria pre-satisfied)
exit: CLEAN
