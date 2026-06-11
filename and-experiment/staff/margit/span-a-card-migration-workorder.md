# Span-A card-migration work-order

**Authored 2026-06-11** (from the card-layer ground-truth audit during the spine review-walk). Authority:
`schemas/card.schema.md`. The warehouse is in a **transitional** state — span-A character cards are built, but
a 30+-card **reference web** still points at span-B slugs, and the prop/cond layer still carries span-B
content (Saerys naming, charity cover, the old casualties Harwin/Daenys). This work-order specifies the
remaining migration as a **coordinated batch** so the reference graph never breaks mid-flight.

> ⚠ **Do not do this piecemeal.** Tombstoning or renaming a card whose slug is referenced by N others breaks
> N references. Run the steps **in the order below** (refs-rewrite first, then content re-derivation, then
> tombstone), validating the reference graph after each phase.

---

## A. Current state (ground truth, 2026-06-11)

| Bucket | Cards | Status |
|---|---|---|
| **Span-A LIVE — character** | gael-targaryen · wylla-maid · jaehaerys-i-targaryen · maester-lorren · septa-aldith · otto-hightower · septon-barth · alicent-hightower · hobb · daemon-targaryen | BUILT, `supersedes:` tagged. ✅ production-ready |
| **Span-A LIVE — minor (servants)** | bessa/mella-wet-nurse · cissa/wenda-nursemaid · mistress-bryony · nona/pella/marra-chambermaid · mistress-orla-wardrobe · nesta-tiring-girl | bodies use "Gael"; `references: saerys-targaryen` (slug not yet repointed) → **Phase 1** |
| **Span-A LIVE — stage** | comedy-register · loc-red-keep-interior · loc-still-room · loc-maegors-holdfast | valid; naming/ref audit only |
| **Tombstoned (done)** | saerys-targaryen · saerys-maester · saerys-septa · **loc-sick-house** (2026-06-11) · **viserys-i-targaryen** (2026-06-11) | `scope: tombstone`. Keep as provenance. |
| **Parked for the Dance (NOT stale — keep as-is)** | ser-harwin-the-patient · daenys-velaryon (+behavior) · nymeria-summer-isles · helaena-targaryen-122ac (+behavior) | parked cast; do not retire, do not migrate |
| **NEEDS RE-DERIVATION (span-B content)** | prop-account-book · prop-harwins-list · cond-saerys-formation-map-red-keep · saerys-targaryen-behavior · the-factor · (trade-network/charity threads) | see Phase 2 |
| **NEEDS AUDIT (likely span-A-valid; naming/spot-check)** | cond-inferior-path-doctrine · cond-inferior-path-technique-hierarchy · cond-trade-network-formation · cond-transmigration-previous-life · cond-westerosi-poison-pharmacology · cond-westeros-reagent-tier-map · cond-maesters-cabinet · cond-alchemists-guild-122ac · cond-heartless-dao-scripture · cond-heavenly-dao-calibration · prop-dose-log · prop-cradle-egg · prop-bill-of-exchange · prop-still-room-kit · prop-wildfire-shard · prop-christening-spoon · prop-kings-hand-note | Phase 3 |

**Live source for re-derivation:** `intake/character-profiles.md` + `intake/character-reactions.md` (cast) ·
`intake/spine.md` (story + the funding-engine + curdle ladder) · `design/run-04/state-ledger.md` §Invariants
(ruled premises) · `design/run-04/series-outline.md` (tokenized chapters).

---

## B. The span-B → span-A mapping key (apply consistently)

| Span-B | Span-A | Notes |
|---|---|---|
| Saerys | **Gael** | protagonist rename (slug saerys-targaryen → gael-targaryen) |
| Viserys I (father) | **Jaehaerys I** (cold cage) + warm-cage DNA → **Alicent** | father re-seat |
| the maid (unnamed) | **Wylla** (minor noble) | deuteragonist |
| Ser Harwin (R3 victim) | **Lothar Quint** (III.3, "the account is closed") | the greedy factor |
| the "pest" (R2 victim) | **the exploiter** (II.7, Otto's lever — first premeditated kill) | |
| Daenys (apex/parked) | the **III.6 apex** — the uncosted debt = the pursuer Wylla kills (Otto's man) | |
| the **charity-apothecary / sick-house** cover | the legit **soap-chemistry front** + the **off-books gambling/entertainment vice-network** (`VICE-NETWORK`; seed stolen from the crown, `SECT-SEED-THEFT`) | the funding pivot |
| the betrothal lord (Slate, "cheap") | **the Starks** (Warden of the North's heir; sold "high") | |
| span-B Dance finale / curdle R4 dead-dragon-field | **parked** (Dance book = R5) | this series ends at the escape (III.6 = R4 apex) |

**Verify before assuming valid:** is "**the Inferior Path**" the span-A name for her (wrong) cultivation
doctrine? It's used as an alias on the tombstoned saerys card and across the cond/prop layer. If span-A keeps
it → audit naming only; if span-A renamed the doctrine → re-derive the inferior-path conds. (Check the
cultivation-library + spine cultivation framing.) **Rule 22** applies to any prose in these cards.

---

## C. Coordinated migration — run in order

**Phase 0 — refs audit (read-only).** `grep -rln "saerys-targaryen\|saerys-maester\|saerys-septa\|viserys-i" warehouse/*.card.md`
→ enumerate every card whose `references:` (or body) points at a tombstoned slug. (Live span-A cards' own
`supersedes:`/prose mentions of the old slug are CORRECT — exclude those.)

**Phase 1 — reference-graph rewrite (mechanical, do as one batch).** Repoint every dangling reference:
`saerys-targaryen → gael-targaryen` · `saerys-maester → maester-lorren` · `saerys-septa → septa-aldith` ·
`viserys-i-targaryen → jaehaerys-i-targaryen` (or alicent-hightower where the warm-cage function is meant).
Touches the servant cards + the prop/cond layer. Validate: no live card references a tombstoned slug except
in a `supersedes:`/provenance line. *(One already fixed by hand 2026-06-11: septon-barth `saerys-maester` →
`maester-lorren`.)*

**Phase 2 — content re-derivation (the real authoring; one card at a time, references intact).**
- `saerys-targaryen-behavior` → **build `gael-targaryen-behavior`** (rename + span-A voice per
  `character-profiles.md` §Gael Voice + Rule 22), point `gael-targaryen.card.md` at it, then tombstone the
  saerys behavior card.
- `prop-account-book` → re-derive: Saerys→Gael; **charity-cover → soap-front + vice-ledger**; the "one place a
  death is entered" beat → span-A casualties (Quint "the account is closed" III.3; the II.7 exploiter; the
  III.6 apex as the uncosted debt). Keep the artifact-spirit/Inferior-Path framing iff span-A-valid.
- `prop-harwins-list` → re-derive to the span-A factor-network/Quint equivalent, or tombstone if redundant
  with the account-book.
- `cond-saerys-formation-map-red-keep` → rename Saerys→Gael (slug + body); the spatial formation map is
  otherwise span-A-valid.
- `the-factor` → tombstone (span-B); Quint is a "card on demand" minor mark (memory.md stage_elements). Build
  `lothar-quint` only if III.3 graduates to needing a full card.

**Phase 3 — audit-then-keep-or-fix (the "likely-valid" bucket).** For each cond/prop in the audit bucket:
spot-check for span-B casualty/charity/Saerys content. Most are mechanics (poison pharmacology, reagent-tier,
cradle-egg, dose-log) and span-A-valid → naming/ref fix only. Flag any that carry span-B story content for
re-derivation.

**Phase 4 — validate + index + record.** Validate every touched card against `schemas/card.schema.md`; update
`cards/*/INDEX.md` + `staff/margit/margit.memory.md`; archive nothing (tombstones stay in place as
provenance); record the batch in `staff/margit/card-build-manifest.md`.

---

## D. Notes / risks
- **Parked-Dance cards are not stale** — do not "migrate" Harwin/Daenys/Nymeria/Helaena; they belong to the
  parked installment (memory.md). Only their *references from live cards* (if any) get repointed.
- **Provenance:** tombstones (`scope: tombstone`) are kept in the warehouse, not deleted (archive-never-delete).
- **Gate:** none of this is blocked — the Otto/Daemon seating is ruled (AU court-transposition, keep names),
  so the otto/daemon cards are final. The build is unblocked.
- **Concrete fixes already applied (2026-06-11):** loc-sick-house + viserys-i-targaryen tombstoned;
  septon-barth dangling ref fixed.
