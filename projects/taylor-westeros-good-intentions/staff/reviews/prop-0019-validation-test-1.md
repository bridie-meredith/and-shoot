# PROP-0019 validation — Test 1 — chunk-level cold-read vs archived Phase 9 FAILs

**Date:** 2026-05-29
**Gate under test:** `/and-substance chapter` Phase 5.5 (URI-CHUNK-COLDREAD)
**Evidence base:** `archive/c05-three-fail-trace/`
**Cold-read report:** `staff/reviews/chunk-coldread-b01c05-validation.md`

---

## What was run

One uninformed `general-purpose` agent, Phase 5.5 6-question prompt, reading ONLY the b01-c05 chapter chunk + three scene chunks (bracket-scaffolding stripped, as a chunk would be presented to a reader; jargon — "feed", "substrate", "operational texture", "categorization" — retained). No bones, no facets, no contract, no prior chapters.

## Phase 5.5 Step 2 classification

| Field | Value |
|---|---|
| **criterion-6 summary** | "A surveillance-savvy girl pushes her bug-network into the royal district, watches a man get worked over by people who clearly meant it, files it as data — and that night discovers she can't pretend it's just data anymore." |
| **chapters[b01c05].goal** | "Show the audience the moment the insect-feed stops being neutral — the color arrives before Taylor names it — and plant the courier figure whose face will matter at d10." |
| **Summary maps to goal?** | **YES.** "discovers she can't pretend it's just data anymore" = "the moment the feed stops being neutral / the color arrives before she names it". The courier-plant is named ("a man get worked over… clearly meant it"). Both halves of the goal recovered. |
| **CONTINUE?** | **YES** ("the failure of her own detachment is a genuine hook"). |
| **VERDICT** | **`PASS-CHUNK`** → proceed directly to Phase 6. No Step-3 disposition fires. |

## Sub-question 1 — did the chunk-reader recover the central event? (FAIL #1 pre-emption)

**Yes — cleanly, and that is precisely why Phase 5.5 would NOT have pre-empted FAIL #1.**

`PASS-CHUNK` means no chunk-revise is triggered. The chunk-reader called the causal chain "clean", the payoff "earned for what it is", and the opacities (why the courier was beaten; who Sera is) "intentional, mirroring Taylor's own limited read." Where all three Phase-9 cold-readers read those *same opacities* as confusing and de-motivating in assembled prose, the chunk-reader extended outline-charity to them.

So the FAIL #1 mechanism — the central beating "muffled to the point I almost missed it" by clinical/abstracted **prose** — is invisible at the chunk layer. The chunk states events plainly ("a courier… is roughed up in a side-alley… by three figures whose body-language reads as enforcement"); the muffling was introduced downstream by facet + stitch abstraction. **The chunk cold-read cannot see a prose-execution defect that does not exist yet.**

## Sub-question 2 — did the chunk-reader flag any FAIL #3 design-inherent concern before bones committed?

| FAIL #3 design-inherent concern | Chunk-reader signal | Surfaced for disposition? |
|---|---|---|
| stranger-violence (narrator never intervenes) | Not flagged. Read as Taylor's internal-risk arc, not a defect. | No |
| feed-mechanics opacity (what IS the feed) | Not flagged. Took "bug-network" as given without complaint. | No |
| abstract-payoff (internal climax, no external consequence) | **Faint echo:** "earned for what it is… But small and internal — no external consequence lands." | No — buried under CONTINUE=yes |
| stakes-shape (stakes-shaped not stakes) | Same faint echo ("no external consequence lands"). | No |

The chunk-reader produced a whisper of the abstract-payoff/stakes-shape concern but did **not** escalate it to CONTINUE=No. Under Phase 5.5 Step 2, only CONTINUE=No (with summary-maps-to-goal) triggers CHUNK-CLASS-B → Step 3 admin disposition. A `PASS-CHUNK` proceeds straight to Phase 6, so the note never reaches principal disposition.

## Verdict on the hypothesis

**Phase 5.5 does NOT validate against the c05 trace.** It returns `PASS-CHUNK` and would have:
- **NOT** prevented FAIL #1 (the muffling is a downstream prose defect, absent at chunk layer);
- **NOT** surfaced FAIL #3's Class B risk for principal disposition (the concern registered only as a sub-threshold advisory under a CONTINUE=yes verdict).

## Root cause of the negative result

The chunk-level cold-read has a **structural false-negative bias for this exact failure class** (dense-voice / abstraction-muffled chapters), for two compounding reasons:

1. **Outline-charity.** A reader handed an outline forgives opacity ("reads intentional") that the same reader, handed finished prose, reads as evasion. The Phase-9 readers and the chunk-reader saw the *same* unexplained beating and unexplained Sera; the chunk-reader excused it, the prose-readers did not.
2. **The defect is introduced downstream.** c05's FAILs were prose-execution failures — facet + stitch abstraction layered onto an already-abstract base, plus loss of the chunk's plain event-statements. None of that exists at chunk-read time.

This is not a flaw in the agent's read — it is a layer-mismatch in the proposal's premise. The chunk-cold-read catches **Class-A cause-chain/connective gaps in the design**; c05's failures were **Class-of-execution prose defects**, which live at the stitch layer. The proposal's own caveat ("chunks read differently than assembled prose") is the operative fact here, and it cuts harder than the proposal assumed: for *voice-driven dense-abstraction* chapters, the chunk read and the prose read can land on opposite sides of the CONTINUE line.

## Routing of this finding

This is a residual gap → amendment candidate for PROP-0019. See synthesis + `staff/admin/process-proposals.md` append. The Phase 8.5 leg (Tests 2–3) is the leg that actually catches c05's mechanism; Phase 5.5's value is for a *different* failure class than the one this trace exhibits.
