# PROP-0019-A — revised-vs-original command rerun comparison (b01-c05)

**Date:** 2026-05-29
**Branch:** claude/intelligent-gauss-qacpV
**What this is:** the A/B the principal asked for — rerun the two re-scoped commands on the latest fully-realized chapter (b01-c05) and compare revised-command output to original-command output.

**Why b01-c05:** it is the latest chapter with the full artifact set (scene chunks + bones + facets + shipped draft); b01-c06 is `planned` (chapter chunk only, no scene chunks, no draft), so the affected commands cannot run on it. c05 is also the chapter the *original*-command outputs already exist for (PROP-0019 validation Tests 1 & 3), giving a controlled comparison where the only variable is the command-body change.

---

## What changed in the command bodies (commits 826729a + this commit)

| Command | Phase | Change |
|---|---|---|
| `/and-substance chapter` | 5.5 | New verdict `PASS-CHUNK-VOICE-RISK`; new Step 2.5 voice-density guard (Signal A = excused load-bearing confusion; Signal B = abstraction-dense central event); new Q7 "CONFUSIONS (no charity)" + strict-CONTINUE; `voice_risk` memory block. Does NOT block — arms Phase 8.5. |
| `/and-stitch` | 8.5 | Check 3 addendum `central-event-muffle`, armed when upstream verdict == `PASS-CHUNK-VOICE-RISK`; consumes `voice_risk_carry`. |

A logic bug in the first edit was caught *by this rerun* and fixed (see "Bug surfaced" below).

---

## Rerun 1 — `/and-substance chapter b01c05` Phase 5.5

Same chunk text fed to both runs; only the prompt/classification logic differs.

| | ORIGINAL Phase 5.5 (Test 1) | REVISED Phase 5.5 (this rerun) |
|---|---|---|
| Report | `chunk-coldread-b01c05-validation.md` | `chunk-coldread-b01c05-revised-rerun.md` |
| Summary maps to goal? | Yes | Yes |
| CONTINUE | yes | yes (Q5) / **yes-but-excused** (Q7 strict) |
| Q7 no-charity confusions | *(not asked)* | courier-targeting causality **withheld**; resentment payoff **"asserted, not motivated"**; Sera/Jarvis/Hook unexplained — reader excused all as "missing prior-chapter setup" |
| **Verdict** | **`PASS-CHUNK`** (clean — banks a clean pass) | **`PASS-CHUNK-VOICE-RISK`** (Signal A + Signal B) |
| Downstream effect | none — proceeds silently | writes `voice_risk_carry`; arms Phase 8.5 central-event-muffle |

**The difference is the whole point.** The original gate banked a clean `PASS-CHUNK` on the canonical dense-voice chapter — exactly the false-PASS the validation flagged. The revised gate recovers the same event and still continues, but refuses to call it clean: it fires Signal A (the reader only continued by *excusing* causality/payoff confusions) and Signal B (the central beating is rendered in s02 purely through feed/instrument abstraction — "the feed flags the contact", "contact complete", "it logs: brief contact, courier retained on feet" — never as a concrete strike). Result: `PASS-CHUNK-VOICE-RISK`, which proceeds (the chunk design is sound) but hands the downstream layer a specific thing to check.

## Rerun 2 — `/and-stitch b01-c05` Phase 8.5 (shipped draft)

Same draft fed to both runs; revised run additionally armed by the `voice_risk_carry` from Rerun 1.

| | ORIGINAL Phase 8.5 (Test 3) | REVISED Phase 8.5 (this rerun) |
|---|---|---|
| Report | `coherence-b01c05-shipped-validation.md` | `coherence-b01c05-shipped-revised-rerun.md` |
| Weave / Followability | 0 / 0 | 0 / 0 |
| @14 sexual-assault risk | PASS (closed) | PASS (closed) |
| **central-event-muffle sub-check** | *(does not exist — not interrogated)* | **PASS on quoted evidence** |
| Evidence basis | passed **by omission** | passed **by evidence**: locates "The third struck him." (bare SVO, own line, L31) + impact/recovery beats L33–L37; confirms the feed-muffle phrasings from the carry do **not** appear in assembled prose |
| **Verdict** | PASS | PASS |

**Same verdict, materially different rigor — and the new check has teeth.** The original Phase 8.5 reached PASS without ever interrogating how the central event renders. The revised Phase 8.5 was *forced* by the armed carry to locate the beating span, quote the carrying prose, and judge cold-reader legibility. It cleared because the stitch layer had already de-abstracted the event (the @13 "strike" recast + scene-B re-render did their job). Had the stitch left the beating in feed-vocab — the **FAIL #1 "a beating I almost missed" mechanism** — this check would have fired `COLD-READ-RISK central-event-muffled @13` at HIGH confidence → SOFT-BLOCK → stitch-revise, one phase before the Phase 9 cold-read. That is precisely the catch the chunk layer structurally cannot make (the muffle does not exist at chunk-read time) and which the original Phase 8.5 made only by luck-of-the-read.

---

## Bug surfaced by the rerun (and fixed)

The first command-body edit (826729a) put "AND Q7 lists no load-bearing confusion" as a *precondition* of the `PASS-CHUNK` trigger. That would have routed the c05 case (which has load-bearing-but-excused confusions) OUT of the PASS-CHUNK family *before* Step 2.5 / Signal A could test it — a dead branch, since "maps + strict-continue=yes + load-bearing-confusion" had nowhere to land. Fixed: the PASS-CHUNK *family* trigger is now just "maps + strict-CONTINUE=yes"; Step 2.5 resolves clean-`PASS-CHUNK` vs `PASS-CHUNK-VOICE-RISK`, and Signal A is where excused-load-bearing-confusion is tested. The rerun doing real classification work is what exposed the gap.

---

## Net

- **Phase 5.5 re-scope works as intended.** On the canonical dense-voice chapter it converts a silent false-clean-PASS into `PASS-CHUNK-VOICE-RISK` with a concrete downstream carry — without falsely blocking a sound chunk design.
- **Phase 8.5 coupling works as intended.** The armed central-event-muffle check fires the right interrogation, clears on evidence here (the shipped draft genuinely de-abstracted the beating), and would have SOFT-BLOCKED on a muffled draft — closing the FAIL #1 mechanism at the layer that can see it.
- **The two legs now compose:** chunk layer flags abstraction-risk → stitch layer verifies central-event legibility. Neither leg alone catches FAIL #1; together they do.
- **Cost:** 2 rerun dispatches (1 cold-read + 1 coherence).

**Residual note for triage:** Rerun 2 cleared because re-stitch #3 had already fixed the muffle. A maximally convincing "firing" demonstration would run the revised Phase 8.5 against a *pre-de-abstraction* draft — but no FAIL #1-era draft was preserved (only the FAIL #2 draft, which exhibits a different mechanism). The agent's quoted-evidence reasoning establishes the check *could* have fired; a future chapter that trips Signal B and ships a muffled stitch will be the live firing test.
