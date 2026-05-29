# c05 three-FAIL trace — evidence archive

**Purpose:** preserved evidence base for PROP-0019 validation. The b01-c05 chapter's three consecutive Phase 9 cold-read FAILs are the case study that motivated the upstream-cold-read + assembled-prose-coherence proposal (`staff/admin/process-proposals.md § PROP-0019`).

**Use:** in a future session, re-run the new upstream gates against this evidence to verify they catch what they're designed to catch. See `archive/c05-three-fail-trace/NEXT-SESSION-PROMPT.md` for the test protocol.

## Artifacts

| File | What it is |
|------|-----------|
| `fail-1-coldread.md` | Phase 9 cold-read report after first stitch attempt. Class A: central event not recovered. |
| `fail-2-coldread.md` | Phase 9 cold-read report after /and-write revise --from-signals + re-cascade. Mixed: central event recovered; CONTINUE=NO on 5 complaints including sexual-assault read. |
| `fail-2-draft.md` | The draft that produced FAIL #2 (preserves the "below the register I would have called human" phrasing at @14). |
| `fail-3-coldread.md` | Phase 9 cold-read report after @13 pin→strike recast + scene-B re-render. Class B: central event recovered; CONTINUE=NO on design-inherent concerns; sexual-assault read REMEDIATED. |
| `final-draft-shipped-with-caveats.md` | The terminal deliverable. Shipped per DEC-0044 referencing PROP-0018 Class B. |

## Decision trail (live in `staff/admin/decisions.md`)

- **DEC-0041** — after FAIL #2, principal escalation; chose third-revise-cycle (spec default). Admin's ESCALATE block named Class A/B discrimination without proposing.
- **DEC-0042** — after FAIL #2, revise scope = (B) recast @13 verb pin → strike; chunk authority authorizes; not substance-contract overwrite.
- **DEC-0043** — after FAIL #3, admin process-critic proposed PROP-0018 (Class A/B routing).
- **DEC-0044** — after FAIL #3, principal disposition = ship-with-caveats under PROP-0018 Class B logic. 5 caveats logged at `chapters[b01c05].cold_read.caveats`.

## Proposals motivated by this trace

- **PROP-0018** — Phase 9 Class A/B disposition discriminator (terminal-gate level). Status: open / pending principal triage.
- **PROP-0019** — Upstream chunk-cold-read at `/and-substance chapter` Phase 5.5 + assembled-prose coherence review at `/and-stitch` Phase 8.5. Status: open / wired into command bodies; pending validation against this archive.
