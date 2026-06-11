# Improvement-Loop / Assets Ledger

Owned by oskar (studio/foreman). One entry per pass; append-only.

---

## Pass 1 — 2026-06-11

**Asset:** `staff/dialogue-writer/rubric-dialogue.md`

**Change:** Removed the impossible-to-satisfy `facet-licenses:` HARD gate from `CONSTRAINT § citation-completeness` in the Audit classes section. The two-axis (card-signatures + facet-licenses) requirement was authored for the R1+R2 pipeline; R2 is retired under DEC-0116. The R1-blind dialogue-writer cannot populate `facet-licenses:` (no locked facets exist at `/and-write` authoring time), so this gate fired as a guaranteed HARD finding on every production chapter — the Phase 4 RUBRIC-FIDELITY class reads this exact section. Fixed to: card-signatures §-cite required (HARD on absent); `facet-licenses:` explicitly deferred with an auditor no-fire note. Added DEC-0116 retirement notice to the file header and to the V2 facet-citation extension section's HARD claim (lines 61-63). Updated Files section to remove the retired R2 decision shard and `_inflight-r2/` path.

**Why top-ranked:** Active-pipeline HARD. Every production chapter run through Phase 4 RUBRIC-FIDELITY would receive a HARD `CONSTRAINT § citation-completeness` finding on every dialogue entry (since `facet-licenses:` is never populated). A guaranteed HARD blocks persist under the Phase 4 gate (0 HARD required). Cost: four surgical edits to one file.

**Persona voice touched:** None. Rubric is structural/operational content, not persona voice.

**For-Brighid log:**
- `staff/audience/literary-snob/` has a biography card but no library exemplar at `cards/persona-exemplars/literary-snob.md`. This is a Tier-1 gap per Rule 16 (`/and-project` Phase 1c blocks on missing audience exemplars). Persona voice content — needs Brighid to author.

**Next candidate:** Survey `rubric-dialogue.md` § R2-specific sections (Contamination disciplines, R1 vs R2 differences, V2 reviewer protocol) for any further live-pipeline contradictions. Lower priority now that the HARD gate is fixed; those sections are marked retired and the auditor no longer reads them for gate decisions.
