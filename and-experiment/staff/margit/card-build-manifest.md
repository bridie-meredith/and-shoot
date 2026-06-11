# Card Build Manifest — and-experiment gap cards
# Session: 2026-06-05
# Authority: schemas/card.schema.md
# Margit-authored per instruction (principal directive, 2026-06-05)

---

## Cards created

| # | slug | class | subclass | quality | tier | scope | project copy | library copy |
|---|------|-------|----------|---------|------|-------|--------------|--------------|
| 1 | saerys-targaryen | persona | — | full | lead | both | `and-experiment/warehouse/saerys-targaryen.card.md` | `cards/personas/saerys-targaryen.card.md` |
| 2 | saerys-targaryen-behavior | behavior | per-character-behavior | full | — | both | `and-experiment/warehouse/saerys-targaryen-behavior.card.md` | `cards/dialects/saerys-targaryen-behavior.card.md` |
| 3 | saerys-targaryen (exemplar) | persona-exemplar | — | — | project-bound | `and-experiment/persona-exemplars/saerys-targaryen.md` | not promoted |
| 4 | viserys-i-targaryen (and-experiment variant) | persona | — | full | supporting | project | `and-experiment/warehouse/viserys-i-targaryen.card.md` | not separately stored (library card remains scant) |
| 5 | helaena-targaryen-122ac | persona | — | full | supporting | both | `and-experiment/warehouse/helaena-targaryen-122ac.card.md` | `cards/personas/helaena-targaryen-122ac.card.md` |
| 6 | daenys-velaryon | persona | — | full | supporting | both | `and-experiment/warehouse/daenys-velaryon.card.md` | `cards/personas/daenys-velaryon.card.md` |
| 7 | ser-harwin-the-patient | persona | — | full | supporting | both | `and-experiment/warehouse/ser-harwin-the-patient.card.md` | `cards/personas/ser-harwin-the-patient.card.md` |
| 8 | nymeria-summer-isles | persona | — | full | supporting | both | `and-experiment/warehouse/nymeria-summer-isles.card.md` | `cards/personas/nymeria-summer-isles.card.md` |
| 9 | saerys-septa | persona | — | full | minor | project-only | `and-experiment/warehouse/saerys-septa.card.md` | not stored (no reuse value outside and-experiment) |
| 10 | comedy-register | behavior | shared-behavior | full | — | both | `and-experiment/warehouse/comedy-register.card.md` | `cards/dialects/comedy-register.card.md` |
| 11 | loc-red-keep-interior | location | — | full | — | both | `and-experiment/warehouse/loc-red-keep-interior.card.md` | `cards/locations/loc-red-keep-interior.card.md` |

**Total: 11 items (10 card files + 1 persona-exemplar)**

---

## Reused without modification (per REUSE MAP)

Per `and-experiment/design/run-01/constraints.md §4`:

| slug | class | reuse action | source |
|------|-------|--------------|--------|
| alicent-hightower-122ac | persona | reuse as-is | `cards/personas/alicent-hightower-122ac.card.md` |
| otto-hightower | persona | reuse as-is | `cards/personas/otto-hightower.card.md` |
| aemond-targaryen-122ac | persona | reuse as-is | `cards/personas/aemond-targaryen-122ac.card.md` |
| rhaenyra-targaryen-122ac | persona | reuse as-is | `cards/personas/rhaenyra-targaryen-122ac.card.md` |
| loc-dragonpit-interior | location | reuse as-is | `cards/locations/loc-dragonpit-interior.card.md` |
| loc-dragonpit-exterior | location | reuse as-is | `cards/locations/loc-dragonpit-exterior.card.md` |
| cond-kl-court-state-122ac | condition | reuse as-is | `cards/conditions/cond-kl-court-state-122ac.card.md` |
| cond-kl-geography-122ac | condition | reuse as-is | `cards/conditions/cond-kl-geography-122ac.card.md` |
| cond-dragon-bonding-claiming-rules | condition | reuse as-is | `cards/conditions/cond-dragon-bonding-claiming-rules.card.md` |
| westeros-noble-courtly | behavior | reuse as-is (inherited by new cards) | `cards/dialects/westeros-noble-courtly.card.md` |
| westeros-grrm-mannerisms | behavior | reuse as-is (referenced by new cards) | `cards/dialects/westeros-grrm-mannerisms.card.md` |

---

## Deferred / blocked items

| item | reason | flag |
|------|--------|------|
| Library upgrade of `viserys-i-targaryen.card.md` (scant→full) | Project variant is comedy-tolerant re-tone; library upgrade would bleed and-experiment-specific framing into cards serving other projects in other registers. Deferred pending principal triage. | FLAG: promote or keep project-scoped |
| Persona-exemplars for helaena-targaryen-122ac, daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles, saerys-septa | Not required until cast is locked at `/and-cast` Phase 5 equivalent. Five exemplars deferred. | FLAG: author before cast gate fires |
| Persona-exemplar for viserys-i-targaryen | On-stage supporting; exemplar eligible. Not authored this session (warm-cage-comedy beats well-covered by card body). | FLAG: author when cast active |
| `saerys-septa` library copy | No cross-project reuse value identified. Project-only. | FLAG: reassess on project promotion |
| Behavior card for helaena-targaryen-122ac | Her register is a shared-behavior variant (riddle-notation, associative-observational); sufficiently covered by `westeros-noble-courtly` + the persona card's Voice section for now. A per-character behavior card would add value before active shoot. | FLAG: author when shoot approaches |
| Behavior card for daenys-velaryon | Similar; covered by `westeros-noble-courtly` + persona card Voice. Per-character behavior card would sharpen the counter-thesis register. | FLAG: author when shoot approaches |

---

## Index updates completed

- `cards/personas/INDEX.md` — updated
- `cards/dialects/INDEX.md` — updated
- `cards/locations/INDEX.md` — updated
- `cards/persona-exemplars/INDEX.md` — updated
- `and-experiment/staff/margit/margit.memory.md` — updated

---

## Validation summary

All 11 items validated against `schemas/card.schema.md` before storage:
- Persona cards: frontmatter complete; all required body sections present; Hard Fences honored; Vibe Seeds populated for leads and full-quality supporting
- Behavior cards: frontmatter complete; Direct samples present (load-bearing sections); Cadence, Vocabulary, Syntax, Voice tells, Non-verbal tics, Memory monuments all present
- Location card: all seven required sections present
- Persona-exemplar: frontmatter per `schemas/persona-exemplar.schema.md`; length ~230 words (within range); fences declared; dispatch-status: active

No pre-existing cards were overwritten. All cards are net-new files. Preservation discipline honored.

---

## Batch: household-servants (2026-06-08, session-authored)

Per principal request ("what sorts of maids / nannies / wet-nurses would be around her; create cards
for multiple people of each category"). Built to the **live Gael layer** (protagonist card slug remains
`saerys-targaryen`; card bodies use "Gael"). Design + reasonable per-category profiles + maid-candidate
menu (OQ-CL2): `and-experiment/design/counterfactual-life/the-household-roster.md`. All reference
`westeros-smallfolk` + `westeros-grrm-mannerisms` + `saerys-targaryen` + `loc-maegors-holdfast`.

| # | slug | category | quality | tier | scope | maid-candidate |
|---|------|----------|---------|------|-------|----------------|
| 12 | mella-wet-nurse | wet-nurse (primary) | full | minor | project | — |
| 13 | bessa-wet-nurse | wet-nurse (second) | full | minor | project | — |
| 14 | mistress-bryony | nursemaid (head nan) | full | minor | project | — |
| 15 | cissa-nursemaid | nursemaid (under) | full | minor | project | LOW |
| 16 | wenda-the-rocker | nursemaid (rocker) | full | minor | project | — |
| 17 | nona-chambermaid | chamber-maid (steady) | full | minor | project | LOW |
| 18 | pella-chambermaid | chamber-maid (clever) | full | minor | project | **HIGH** |
| 19 | marra-chambermaid | chamber-maid (timid) | full | minor | project | MED/CAUTION |
| 20 | mistress-orla-wardrobe | tiring-woman (wardrobe mistress) | full | minor | project | — |
| 21 | nesta-tiring-girl | tiring-woman (hairdresser) | full | minor | project | — |

**Total: 10 persona cards (net-new; warehouse-only, project-scoped).** No persona-exemplars authored
(minor tier; defer until/if a card is promoted toward the maid role at cast-equivalent). No library
copies (project-only, no cross-project reuse value — same call as `saerys-septa`). All validated
against `schemas/card.schema.md`: frontmatter complete; required persona sections present
(Description/Voice/Taste/Pet Peeves + Stats/Relationships); Fiction-role overlay present
(Thematic Purpose/Look/Hard Fences/Default Stance/Off-Screen Cadence). No pre-existing cards
overwritten.

**Open flags:**
- **OQ-CL2 (the Book II maid):** built as a *menu* — Pella (HIGH), Marra (MED/cautionary), Nona (LOW).
  Not committed; principal chooses. If chosen, promote that card to `tier: supporting` + author an
  exemplar.
- **OQ-CL3 (names):** all servant names overridable.
- **Next batch (not built):** the maester, the masters of accomplishments, the companion girls/ladies.

---

## Batch: span-A card migration (2026-06-11, session-authored)

The full warehouse migration from span-B ("Saerys" / Viserys-father / charity-cover / span-B Dance casualties)
to **span-A** (Gael / Jaehaerys-father + Alicent-warm-cage / soap-apothecary+vice cover / escape-ending,
Dance parked). Coordinated per `staff/margit/span-a-card-migration-workorder.md` (now marked COMPLETE).

**What was done:**
- **Reference graph:** `saerys-targaryen → gael-targaryen` across 36 cards' `references:` (mechanical batch).
- **Naming:** `Saerys → Gael` warehouse-wide (verified; provenance/parked/tombstone cards excluded).
- **Content re-derivation (~20 cards):** Viserys→Jaehaerys (cold king) or Alicent (warm reactions/grants);
  charity/sick-house cover → legit soap-apothecary front + off-books vice; "the Dance"/national-scale →
  parked R5; Daenys → Wylla + the III.6 apex (the "blank line" register-silence); Harwin → Quint;
  Harwin's-list → the bestiary; the curdle-ladder R-table → span-A. Includes the 3 **license cards**
  (`prop-kings-hand-note`, `prop-bill-of-exchange`, `cond-trade-network-formation`): the span-B
  orphaned-license/Dance-heist mechanic **dropped** (King lives, escape = off-books dice-coin per spine
  III.1); the supply-chain cover re-derived to **Alicent's patronage**. *(Reversible judgment-default —
  the spine doesn't pin the legal-cover mechanic.)*
- **New card built:** `gael-targaryen-behavior` (per-character voice card; `character: gael-targaryen`,
  `period: jaehaerys-reign`; supersedes `saerys-targaryen-behavior`). Schema-validated: required
  `Direct samples` + all recommended sections present.
- **Slug rename:** `cond-saerys-formation-map-red-keep → cond-gael-formation-map-red-keep` (git mv + name
  field + referrer).
- **Tombstoned** (`scope: tombstone` + `superseded_by`, schema-clean): `saerys-targaryen`→gael-targaryen ·
  `saerys-maester`→maester-lorren · `saerys-septa`→septa-aldith · `saerys-targaryen-behavior`→
  gael-targaryen-behavior · `viserys-i-targaryen`→jaehaerys-i-targaryen · `loc-sick-house`→loc-still-room.
- **Parked** (`scope: project`, held for the Dance, not used span-A): `ser-harwin-the-patient` +
  `prop-harwins-list`, `daenys-velaryon` (+behavior), `nymeria-summer-isles`, `helaena-targaryen-122ac`
  (+behavior).
- **Kept-and-re-derived (not retired):** `the-factor` (Moro Tessavik — the Braavosi supply factor, NOT the
  III.3 greedy-factor Quint; the work-order's initial "tombstone" assumption was corrected).
- **No-change (false positives checked):** `marra-chambermaid` ("pious" = her character, not the cover);
  the live character cards' `supersedes:`/provenance "Saerys"/"Viserys" mentions (correct, preserved).

**QA verified:** warehouse-wide sweep — no stale span-B in any live card; no live card references a tombstoned
slug; no non-schema frontmatter fields (`retired_reason` removed; tombstones use the proven convention);
`prop-kings-hand-note` re-derivation restored to schema-complete (all 6 prop sections); check-threads PASS.

**Open (cosmetic, recommended-leave):** the `cond-*-122ac` library slug suffixes (in-world era already
corrected in the bodies; `cond-kl-court-state-122ac` / `cond-kl-geography-122ac` are shared-library reuse
cards that should keep their library names).
