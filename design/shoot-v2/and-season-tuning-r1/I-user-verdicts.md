---
phase: I — user verdicts on human escalations
date: 2026-05-10
run: and-season-tuning-r1
input: H-carry-back.md (URI-009, URI-010 escalations)
status: closed
---

# Phase I — User Verdicts on the Two Human Escalations

The two human-escalation items from Phase H are resolved. This file records the verdicts.

---

## URI-009 — Narrator-field rule for interlude episodes — RESOLVED

**User verdict:** "designate narrator before generating lines for a chunk. consistent within chunk."

**Translation to rubric language (V2 candidate):**

> The `narrator:` field on a chunk (episode, season-stretch, or any unit a chunk-author works against) is **designated at planning time, before line generation**, and held consistent across the chunk. The /and-season Phase 4 Step 3 spec language ("the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch") is replaced with: **the `narrator:` is the plan-designated narrator for the chunk.** When `season-plan.md` POV rulings designate an interlude narrator for a content beat, that designation is authoritative — it is not overridden by raw line-count dominance after authoring.
>
> Process implication: `narrator:` is set at plan time and does not change post-hoc. Line generation honors the designation. The Phase 4 Step 3 mechanical computation rule is removed.

**Effect on s01:**

- s01e05 `narrator: mira-stonefield-jaehaerys` — already plan-designated as the witness-inquiry interlude narrator per `season-s01-plan.md` §E. Compliant.
- s01e06 `narrator: oc-craftsman-mother` — already plan-designated as the parents-act-in-concert interlude narrator per `season-s01-plan.md` §E. Compliant.
- **fault-005 (auditor HARD finding) is RESOLVED.** The e06 narrator field is correct as authored. No file edit required to s01e06.md or memory.md. The dominant-line-count reading was a misinterpretation of the V1 spec under the new rule.
- **B-baseline Gap 8 closes.** Both e05 (compliant per signal-006) and e06 (compliant per user verdict) honor the designate-at-plan-time rule.
- **URI-009 carry-back stays open** as a V2 rubric edit candidate — the language change to /and-season Phase 4 Step 3 still needs to land formally. The s01 corpus is no longer blocked by the ambiguity; future runs benefit from the explicit rule.

---

## URI-010 — Aggregate non-monotonic IDs schema clarification — RESOLVED

**User verdict:** "do not care either way about numbering, pick what is easiest for you."

**Decision:** Option A — stable-overrides-monotonic (legal-survivors path).

**Rationale for Option A:**

- Smaller blast radius. Schema clarification is a clause edit; the s01 corpus does not require any renumbering pass.
- Honors authoring history. The 21 900-range IDs are reorder artifacts from the s01 pass-2/pass-3 SVO + dramatist reshuffles; under "stable / re-ordering preserves IDs" they are legal survivors.
- The fixer formula in /and-season Phase 4 Step 3 (`aggregate_id = aggregate_range_start + episode_id - 1`) is documented as **position-aware** rather than monotonic-arithmetic. For routing, fixers map by file-line-position within the aggregate, not by ID arithmetic.
- Option B (renumber-on-reorder) would require updating every cited ID in audit reports, design docs, and commit messages — a much larger touch surface for no functional gain.

**Translation to schema language (V2 candidate):**

> Aggregate files MAY contain non-monotonic IDs as legal artifacts of pass-level reordering. The schema's "stable IDs / re-ordering preserves IDs" rule overrides the "monotonic positive integer, file-scoped" position interpretation. IDs are stable at the assignment level (no reuse, no reassignment); they are not required to appear in sorted order within the file body.
>
> Fixer routing MUST use position-aware mapping (file-line position within the aggregate) rather than the `aggregate_range_start + episode_id - 1` shortcut. The shortcut formula is valid only when the per-episode file contains a contiguous monotonic-ID range. For aggregates with non-monotonic IDs, the fixer must walk the aggregate to compute the mapping.

**Effect on s01:**

- **fault-001 (auditor HARD finding) is RESOLVED.** The 21 non-monotonic 900-range IDs in the e01 region are schema-compliant legal survivors. No corpus mutation required. The aggregate stays as-authored.
- **Downstream consumers** (any future fixer routing for s01e01 bones in the non-monotonic region) must use position-aware mapping. /and-season Phase 4 Step 3 documentation should be updated to note this — that's a V2 carry-back, not a R1 corpus fix.
- **URI-010 carry-back stays open** as a V2 schema/command edit candidate.

---

## Updated run status

Both human-escalation blockers cleared.

| Status | Pre-verdict | Post-verdict |
|---|---|---|
| Phase F file-level | SHIPPABLE-WITH-RE-PASS | (unchanged; closed by E-r2) |
| Phase G file-level | FAIL-HARD-FINDINGS (5) | **PASS-WITH-CARRY-BACKS** (3 HARD resolved by verdicts; 2 routed: fault-002 covered by U12 execution, fault-AP-1 covered by U17 REVISE; 0 remaining open) |
| Run-level | SHIPPABLE-PENDING-EXECUTION + 2 human escalations | **SHIPPABLE-PENDING-EXECUTION + 0 human escalations** |

Auditor HARD findings, post-verdict:

- ~~fault-001~~ — RESOLVED by URI-010 verdict (Option A; legal survivors).
- ~~fault-002~~ — covered by U12 showrunner-self execution (1-149 → 1-148 header + memory).
- ~~fault-004~~ — routed via U16 amendment (dramatist verifies POV-stretch boundaries).
- ~~fault-005~~ — RESOLVED by URI-009 verdict (plan-designated narrator wins; e06 field is correct).
- ~~fault-AP-1~~ — covered by U17 REVISE (targeted 20-instance contextual-differentiator pass).

All five auditor HARD findings closed at decision level.

## Carry-back queue, post-verdict

Eight V2 candidates remain open in the queue:

| URI | Item | Status |
|---|---|---|
| URI-007 | Idiom depletion as named fault class | OPEN — V2 candidate |
| URI-008 | Denouement-share quantification | OPEN — V2 candidate |
| URI-009 | Narrator-field rule (designate-before-generation) | OPEN — V2 candidate; user verdict received; rubric language drafted above |
| URI-010 | Aggregate non-monotonic IDs schema | OPEN — V2 candidate; user verdict received; schema language drafted above |
| URI-011 | Episode-shape mechanics (Phase 4 Step 2) | OPEN — V2 candidate |
| URI-012 | Post-split continuity pass S4.5 | OPEN — V2 candidate |
| URI-013 | S3 vs S9 entertainment-density reconciliation | OPEN — V2 candidate |
| URI-014 | Season-scope adversarial criteria per persona | OPEN — V2 candidate |
| URI-015 | S6 vibe-drift resolution path | OPEN — V2 candidate |
| URI-016 | S8a/S8b split-verdict adjudication | OPEN — V2 candidate |

URI-009 and URI-010 are no longer "blocking" — they are **V2 candidates with verdicts attached**. The verdicts are immediately applicable to s01 (no corpus changes required); the rubric/schema language change is queued for the V2 session.

---

## Phase I complete

The two human-escalation items are resolved. Run R1 is **SHIPPABLE-PENDING-EXECUTION** with no remaining human-blocker items. Downstream execution (screen-writer / dramatist / showrunner-self) proceeds per E-r2 routing.
