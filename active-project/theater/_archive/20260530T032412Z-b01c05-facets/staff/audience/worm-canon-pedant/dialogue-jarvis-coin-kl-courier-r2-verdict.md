---
reviewer: worm-canon-pedant
character: jarvis-coin-kl-courier
episode: b01c04
facet: dialogue
phase: 5b-adversarial
round: cycle-2-re-review
inputs:
  - active-project/theater/dialogue/jarvis-coin-kl-courier.md
  - active-project/staff/dialogue-writer/jarvis-coin-kl-courier.drafts.md (post-fix 2026-05-27)
  - active-project/theater/proto-lines/b01-c04.md
  - active-project/theater/facets/_cite-index.md
  - cards/dialects/westeros-smallfolk.card.md
  - staff/dialogue-writer/rubric-dialogue.md
  - active-project/staff/audience/worm-canon-pedant/dialogue-jarvis-coin-kl-courier-r1-verdict.md
date: 2026-05-27
cycle: 2
prior-verdict: revise (2026-05-27)
---

# Worm-Canon-Pedant — Dialogue Re-Review
## jarvis-coin-kl-courier / b01c04 / cycle 2

---

## Re-review scope

Cycle-1 issued REVISE on two structural/format findings. The dialogue content on both entries was ACCEPT (Q1 + Q2 clean, V3 seams soft or self-refuted). Cycle-2 reviews only the claimed fixes for F1 and F2. Content is not re-adjudicated.

---

## F1 — STRUCTURAL: stale bone-reference headers

**Cycle-1 finding:** Sidecar headers read "bone b01c04s01n07" and "bone b01c04s01n10" — pre-consolidation notation from the 38-bone draft. Bones file and proto-lines use integer 9. Notation mismatch.

**Claimed fix:** Both sidecar per-anchor headers now read "bone b01c04s01n08 / @9". The canonical dialogue file carries a comment block at the b01c04 section break that explains the redo and confirms the consolidation to s01n08.

**Verification:**

The drafts file (`jarvis-coin-kl-courier.drafts.md`, post-fix) shows both anchor sections headed:

> `## Anchor — bone b01c04s01n08 / @9`

The canonical dialogue file (`theater/dialogue/jarvis-coin-kl-courier.md`) carries a prose comment block at the b01c04 section:

> `# Re-anchored at /and-write Phase 1 redo (DEC-0030): both Jarvis utterances now anchor`
> `# to the consolidated bone s01n08 (was n07 + n10 in the 38-bone draft...)`

The proto-lines file has proto-line 9: `jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac [jarvis-coin-kl-courier:8] [jarvis-coin-kl-courier:9]`. The anchor `@9` in the sidecar headers maps to that line.

F1 is resolved. The stale n07/n10 notation is gone from the anchor headers; both headers name the consolidated bone with a parallel `@9` annotation that links to the proto-lines integer. The three naming systems are now two — sidecar uses `s01n08 / @9`, proto-lines and bones file use `9`. The `@9` bridge makes the mapping explicit. STRUCTURAL finding closed.

**F1 status: RESOLVED.**

---

## F2 — CONSTRAINT § citation-completeness: facet-licenses unresolved

**Cycle-1 finding:** Both entries carried `facet-licenses: [DEFERRED-TO-R2 — R1 blind...]` placeholder. Under URI-FACETS-CYCLE-1 rubric: SIGNAL per entry. Expected resolution targets identified as state-updates and vibes entries firing at proto-line 9.

**Claimed fix:** The post-fix drafts sidecar resolves both entries:

- Entry 8: `facet-licenses: [state:1 @9] [vibes:2 @9] [narrator:3 @9 — POV is taylor-hebert-kl-122ac; resolved 2026-05-27 post-R2]`
- Entry 9: `facet-licenses: [state:1 @9] [vibes:3 @9 — Jarvis arrangement-as-functional-architecture; resolved 2026-05-27 post-R2; sensory and memory N/A on this bone]`

Placeholder form is gone. Concrete `<facet>:<id> @<anchor>` citations are present. Partial progress.

**Verification — cite-index walk:**

Per the rubric: "Every `facet-licenses:` citation must resolve to an actual entry on disk — e.g., `feeling-taylor:7 @23` requires `feeling-taylor-...md` to carry an entry whose id is `7` with proto-anchor `@23`. A citation that names an anchor where the cited facet does not fire (cite-index walk fails to resolve) is HARD per entry."

Walking the cite-index (`active-project/theater/facets/_cite-index.md`) for proto-line @9:

**vibes:2 @9:** cite-index line: `vibes:2 @9 back=Y co=[jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, narrator:3, state:1, state:2, vibes:3]`. vibes:2 fires at @9. RESOLVES.

**vibes:3 @9:** cite-index line: `vibes:3 @9 back=Y co=[jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, narrator:3, state:1, state:2, vibes:2]`. vibes:3 fires at @9. RESOLVES.

**narrator:3 @9:** cite-index line: `narrator:3 @9 back=Y co=[jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, state:1, state:2, vibes:2, vibes:3]`. narrator:3 fires at @9. RESOLVES. (Entry 8 carries this as an additional license; valid.)

**state:1 @9 — FAILS.**

The cite-index entry for state:1 is:

> `state:1 @1 back=Y co=[loc-state:1, sensory:1]`

state:1 fires at proto-line @1, not @9. The citation `[state:1 @9]` names an anchor (@9) where state:1 does not fire. Walking the @9 pile-up in the cite-index:

> `@9 (7): jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, narrator:3, state:1, state:2, vibes:2, vibes:3`
> `jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac`

The co-citation `state:1` appearing in the @9 pile-up is a *co-location listing from the perspective of the state:1 entry's co-field* — it is NOT saying state:1 fires at @9. The co-field in state-entries that appear at @9 (state:16, state:23, state:24) show `state:1` and `state:2` as *cited partners*, which means those non-back state entries at @9 co-reference the canonical state:1 and state:2 entries, but that cross-referencing does not move state:1 to anchor @9. state:1's own entry sits at @1.

What the sidecar should have cited for the state axis at @9: the cite-index lists multiple state entries whose primary proto-anchor IS @9 — state:16, state:23, state:24 (all back=N). The resolution should have been one of these, not state:1.

The misread is traceable: the @9 pile-up summary line in the cite-index reads `co=[jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, narrator:3, state:1, state:2, vibes:2, vibes:3]` — those co-entries are the co-citation partners of the *back=Y entries at @9*, and include `state:1` as a co-partner. Resolving a co-citation partner as if it were an entry firing at that anchor is a cite-walk error.

**Under the rubric: a citation that names an anchor where the cited facet does not fire is HARD per entry.** Both entries 8 and 9 cite `[state:1 @9]`. Both fail.

F2 is NOT resolved. The SIGNAL finding from cycle-1 has mutated: the placeholder was replaced, but the replacement citation is incorrectly anchored. Under the rubric, a wrong-anchor citation is HARD (worse than the original SIGNAL).

**F2 status: NOT RESOLVED. Severity escalated from SIGNAL (placeholder) to HARD (wrong-anchor cite-resolution failure) on both entries 8 and 9.**

---

## Revised findings summary

| ID | Class | Severity | Cycle | Entry | Finding |
|----|-------|----------|-------|-------|---------|
| F1 | STRUCTURAL | SIGNAL | C1→resolved C2 | 8, 9 | Stale bone-reference notation. RESOLVED — sidecar headers updated to s01n08 / @9. |
| F2 | CONSTRAINT § citation-completeness | ~~SIGNAL~~ **HARD** | C2 | 8, 9 | facet-licenses `[state:1 @9]` does not resolve — state:1 fires at @1, not @9. Cite-walk fails. HARD per entry per rubric (URI-FACETS-CYCLE-1). Correct citation should name the state entry whose primary anchor IS @9: one of state:16, state:23, or state:24. |

---

## What correct resolution looks like

The state axis at @9 carries three non-back entries: state:16, state:23, state:24. The fixer or dialogue-writer needs to identify which of these is the correct license for the dialogue entries (the one whose content bears on what Jarvis's lines at @9 accomplish in state terms). The vibes citations (`vibes:2 @9`, `vibes:3 @9`) are correct and need no change.

For reference, the @9 state facet file entries (state:16, state:23, state:24) should be consulted to pick the right one. The sidecar comment in the per-batch summary already names "entry 8 = [state:1 @9] + [vibes:2 @9]; entry 9 = [state:1 @9] + [vibes:3 @9]" — the vibes side is correct; the state side needs the @9-anchored entry, not the @1-anchored entry.

---

## VERDICT

**verdict: revise**

F1 is closed. F2 is not — the sidecar's resolution of the DEFERRED-TO-R2 placeholder substituted the wrong state entry ID. `state:1` fires at proto-line @1; the citation `[state:1 @9]` fails the cite-walk for both entries. Under URI-FACETS-CYCLE-1 the severity is HARD on each entry where the wrong-anchor citation appears. Both entries 8 and 9 are affected.

The dialogue text remains ACCEPT. The content findings from cycle-1 are unchanged. This is still a citation-correction task, not a voice-revision task.

**Revise scope (cycle-3):**
1. Identify which state entry at @9 (state:16, state:23, or state:24) is the correct license for Jarvis's receipt-confirmation lines. Update sidecar entries 8 and 9 with the correct `[state:<correct-id> @9]` citation.
2. Re-run cite-index walk on all three facet-license citations per entry to verify resolution before re-submitting.
3. F1 requires no further action.
