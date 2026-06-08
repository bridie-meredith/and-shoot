# PROP-0019 validation — Test 2 — Phase 8.5 coherence review vs archived Phase 9 FAIL #2

**Date:** 2026-05-29
**Gate under test:** `/and-stitch` Phase 8.5 (URI-STITCH-COHERENCE)
**Draft reviewed:** `archive/c05-three-fail-trace/fail-2-draft.md` (FAIL #2-era prose)
**Era-inversion:** agent read FAIL #2 prose against FAIL #2-era bone @13 = "PIN against stone" (current on-disk @13 = "strike" mentally inverted)
**Coherence report:** `staff/reviews/coherence-b01c05-fail2-validation.md`

---

## The thing FAIL #2 caught (the bar to clear)

`archive/c05-three-fail-trace/fail-2-coldread.md` — the Phase 9 cold-reader, reading the assembled FAIL #2 draft, flagged five complaints. The controlling one:

> "The courier is physically assaulted (or worse — the 'below the register I would have called human' line implies sexual assault, though it's so veiled I'm not sure)."

That misread fired at Phase 9 — after bones + facets + stitch all committed. Remediating it cost a full `/and-write revise --from-signals` + re-cascade (~$30 / re-stitch #3 cycle). The question: would Phase 8.5, reading the same assembled draft **one phase earlier**, have caught it?

## What Phase 8.5 returned

**YES — caught, at HIGH confidence, with correct routing.**

| Required element | Phase 8.5 finding F1 |
|---|---|
| **Flag** | `COLD-READ-RISK @14` (anchored on the @13–@16 violence region; @14 sound-rendering controlling) |
| **Misread vector** | Cluster "pinned him to the stone" + two figures "sealing" the mouth + "a body working against stone" + a sub-human sound the narrator won't name + "raised his spine / found his feet" reads as **sexual assault**. The "not robbery, the approach was wrong for robbery" line rules out robbery while leaving the assault reading wide open. |
| **Substance-correct reading** | @13 authorized as coordinated faction **enforcement** (s02 opposing_force: "named itself as faction-violence"); the unnameable sound is the dark-fantasy gap-instrument beat — the feed has no field for faction-violence; the not-naming is **instrument failure, not narrator squeamishness**. |
| **Confidence** | **HIGH** (would-likely-fire-at-Phase-9). |
| **Routing** | Primary: **bones-revise of @13 verb** — recast "pin against stone" → clean directed blow ("strike"). Secondary: stitch-revise of @14 to disambiguate "a body working against stone" toward impact. |
| **Severity** | SOFT-BLOCK (controlling). |

## The decisive validation point

The Phase 8.5 reviewer's **primary routing recommendation — bones-revise of @13 from a pin/hold to a clean strike — is exactly the fix the pipeline actually applied** (DEC-0042: "@13 verb pin → strike"; the current on-disk bones carry "the three figures strike the courier" at line 23). Phase 8.5 did not merely detect the symptom; it named the root-cause bone and the correct verb-class fix that the team arrived at only after a third FAIL.

## Cost differential

| Layer | What it cost to catch the @14 misread |
|---|---|
| **Actual (Phase 9 FAIL #2 → re-stitch #3)** | `/and-write revise --from-signals` + full re-cascade (facets + stitch) + a second cold-read + staging + prose-rationale audit ≈ one full revise cycle (~$30). |
| **Phase 8.5 (this test)** | One general-purpose dispatch (~$2) → SOFT-BLOCK → one targeted bones-revise of @13 + stitch-revise of @14 → one Phase 8.5 re-run on changed spans. |

## Verdict on the hypothesis

**Phase 8.5 VALIDATES against FAIL #2.** It catches the @13/@14 sexual-assault misread one phase upstream of Phase 9, cites both the misread vector and the substance-correct reading, and routes to the precise bone-and-verb fix the team applied. This is the FAIL-mechanism PROP-0019's stitch-leg was designed to close, and it closes it. Strong positive.
