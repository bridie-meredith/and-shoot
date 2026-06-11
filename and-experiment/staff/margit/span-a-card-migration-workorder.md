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

**Phase 1 — reference-graph rewrite (mechanical, do as one batch).** ✅ **DONE 2026-06-11.** Repointed
`saerys-targaryen → gael-targaryen` in the `references:` list-items of **36 cards** (anchored list-item match;
`supersedes:` inline-lists + body prose + the 5 tombstone files all preserved; verified — no live card
references `saerys-targaryen`/`saerys-maester`/`saerys-septa`/`viserys-i-targaryen` any longer). *(No live
list-item refs to saerys-maester/saerys-septa/viserys-i existed outside tombstones; the one stray
septon-barth `saerys-maester` was hand-fixed 2026-06-11.)* **Two residual graph edges deferred to Phase 2
(each needs a card re-derivation, not a bare ref-swap):** (i) `cond-trade-network-formation` → `loc-sick-house`
(remove when its charity-cover body is re-derived to soap/vice); (ii) `cond-heartless-dao-scripture` (+ the
two parked behavior cards) → `saerys-targaryen-behavior` (repoint when `gael-targaryen-behavior` is built).

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
- `the-factor` (Moro Tessavik) → ✅ **KEPT + RE-DERIVED to span-A (DONE 2026-06-11).** *(Correction: the prior
  "tombstone → Quint" assumption was WRONG.)* He is **not** the III.3 greedy-factor (Quint) — he is the
  span-A-valid **Braavosi medicine/poison supply factor,** "the founding ambiguity" of the trade empire (one
  manifest, both columns). Re-derived: Saerys→Gael, Viserys I→Jaehaerys I, the charity/sick-house cover →
  **apothecary/scholar-princess** cover. *(Quint, if ever a full card, is a separate `lothar-quint` build —
  the III.3 pit-factor-grown-greedy, distinct from Moro.)*
- ✅ **CORRECTION (2026-06-11): "the Inferior Path" is span-A-VALID — NOT a span-B coinage; do NOT defer
  these cards as cosmology-blocked.** It's absent from the *narrative* docs (spine/character-profiles) only
  because those use plain language; the **cultivation-library defines it** as her self-conceived path-name /
  operational philosophy (`cultivation-cosmology-dao-law-and-dark-paths.md`: *"the Inferior Path does not
  require Heavenly Dao approval… is a precise statement of her actual operational philosophy"*). The cosmology
  (Inferior Path · Heavenly Demon self-label · Cauldron-Belly · human-cauldron) is unchanged span-A→span-B.
  So `prop-account-book` + `cond-inferior-path-*` **keep the Inferior-Path framing** and just need the
  **standard fixes**: Saerys→Gael; the span-B **casualties** (Harwin → Quint III.3 / the II.7 exploiter;
  Daenys → the III.6 apex uncosted debt); charity-cover → soap/vice; and **Dance-scale content** (national
  battlefield / harvester) → reframed as *parked future* (span-A ends at the escape, R4 III.6; the
  national-scale curdle is the parked Dance, R5). *(The cultivation-library docs themselves are still
  Saerys-named + carry Dance-scale content — a parallel lower-priority migration, not card-layer.)*

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
  septon-barth dangling ref fixed; Phase-1 ref-rewrite (36 cards); the-factor re-derived; 5 naming-only cards
  migrated (see §E).

---

## E. Full triage (2026-06-11 — every remaining card classified)

> **Traps (do NOT blind-sed):** (1) the **live replacement cards** (gael-targaryen, maester-lorren,
> septa-aldith, jaehaerys-i-targaryen, alicent-hightower) carry *correct* "Saerys"/"Viserys" mentions in
> `supersedes:` + provenance prose — **preserve them.** (2) **Parked-Dance cards** (daenys-velaryon +behavior,
> nymeria-summer-isles, helaena-targaryen-122ac +behavior, ser-harwin-the-patient) are Saerys/Daenys/Harwin-
> heavy but **SKIP** — they're the parked installment, not span-A-live. (3) lowercase **"slate"** = the
> writing-material, NOT Errold Slate — never sed `slate→Stark` blind. (4) **"Viserys"** maps to *Jaehaerys*
> (cold father/king) OR *Alicent* (warm-cage) depending on context — read before swapping.

**DONE:** Phase-1 refs (36 cards) · the-factor (re-derived) · **5 naming-only:** cond-maesters-cabinet ·
loc-red-keep-interior · loc-still-room · prop-christening-spoon · prop-dose-log · **tombstoned:** loc-sick-house ·
viserys-i-targaryen (+ pre-existing saerys-targaryen/maester/septa).

**ALREADY CLEAN (no action):** the span-A character cards + the servant minors (bessa/mella/cissa/wenda/
mistress-bryony/nona/pella/marra*/mistress-orla/nesta — bodies already "Gael", refs fixed). *(marra has one
"pious" → check it's not a stale charity/piety-cover line.)*

**✅ Saerys→Gael NAMING LAYER COMPLETE (2026-06-11):** the 15 content cards below have had `Saerys→Gael`
applied in one verified batch (every diff line a clean swap; "Saerys" now remains only in provenance/parked/
tombstone/the slug-rename card). **What remains per card is the OTHER span-B content listed below** (Viserys,
charity/sick-house, Dance-scale, Harwin/Daenys casualties) — that part is contextual, NOT blind-sed.

**CONTENT-FIX bucket — REMAINING span-B content (Saerys→Gael already done; these need per-card work):**
| Card | Span-B content to fix |
|---|---|
| comedy-register | Saerys + Daenys/Harwin **examples** → Gael/Quint; **battlefield** (Dance-scale) → parked-future framing |
| cond-alchemists-guild-122ac | Saerys + Viserys + **sick-house** + Dance |
| cond-heartless-dao-scripture | Saerys + Daenys; ref `saerys-targaryen-behavior` (Phase-2 behavior build) |
| cond-heavenly-dao-calibration | Saerys + Daenys + **charity/sick-house** + Dance |
| cond-inferior-path-doctrine | Saerys + Daenys + Dance — **keep Inferior-Path framing** |
| cond-inferior-path-technique-hierarchy | Saerys + national-scale (Dance) — keep framing |
| cond-trade-network-formation | Saerys + Viserys + **charity/sick-house** (+ the loc-sick-house dangling ref) + Dance → soap/vice cover |
| cond-transmigration-previous-life | Saerys + Daenys |
| cond-westeros-reagent-tier-map | Saerys + **charity/sick-house** + Dance |
| cond-westerosi-poison-pharmacology | Saerys + Dance (note: "slate" here is the material — leave) |
| loc-maegors-holdfast | Saerys + Viserys; ref to cond-saerys-formation-map (slug rename pending) |
| prop-account-book | **charity/charitable** → soap/vice; **Harwin/Daenys** death-entries → span-A casualties; keep Inferior-Path artifact framing |
| prop-bill-of-exchange | Saerys + Viserys + **charity/sick-house** |
| prop-cradle-egg | Saerys + Harwin + Viserys + national-scale |
| prop-harwins-list | **assess: is this a span-A factor-list (→ rename) or Harwin-specific span-B (→ tombstone)?** |
| prop-kings-hand-note | Saerys + Viserys + **charity** + Dance |
| prop-still-room-kit | **sick-house** + "slate" (material — leave) |
| prop-wildfire-shard | Viserys |
| marra-chambermaid | "pious" (check) |

**SLUG-RENAME (filename + referrers):** cond-saerys-formation-map-red-keep → cond-gael-formation-map-red-keep
(referrers: itself + loc-maegors-holdfast — only 1 external). Body is span-A-stable (Red-Keep surveillance map);
mostly Saerys→Gael + the rename.

**BEHAVIOR-CARD BUILD:** saerys-targaryen-behavior → build **gael-targaryen-behavior** (span-A voice per
character-profiles §Gael Voice + Rule 22), point gael-targaryen + cond-heartless-dao-scripture + the parked
behavior cards at it, then tombstone the saerys behavior card.

---

## F. Content-fix progress + the established span-A mappings (2026-06-11)

**✅ CONTENT-FIXED (11 cards):** prop-wildfire-shard · loc-maegors-holdfast (Viserys→Jaehaerys) · prop-cradle-egg
(christening→Alicent; curdle-ladder R-table→span-A; dead-dragon-field = parked R5) · prop-account-book
(charity→soap/apothecary+vice; death-entries Harwin→Quint / Daenys-blank-line→III.6 apex) · cond-transmigration
(blank-line→apex; body slug ref→gael) · cond-westerosi-poison-pharmacology (Dance→cage/betrothal) ·
cond-westeros-reagent-tier-map (charity→apothecary; dragon-bone→parked) · prop-still-room-kit (sick-house clause
removed) · cond-inferior-path-doctrine + cond-heartless-dao-scripture (Daenys→Wylla / the apex). **Tombstoned:**
prop-harwins-list (parks with Ser Harwin). **No-change:** marra-chambermaid ("pious" = her character, not the cover).

**The established mappings (use for the remaining cards):** Daenys (the central unresolved attachment) → **Wylla** ·
Daenys's death / the blank line (Bk III) → **the III.6 apex** (the register-silence; *what she does to Wylla* — makes
her a killer; she doesn't die) · Harwin (warm guardian / R3) → **Quint** (III.3 "the account is closed") · Harwin's-list
(the comedy instrument) → **the bestiary** (gag ③) · charity/sick-house cover → **soap + apothecary** front (+ off-books
vice) · "the Dance" / national-battlefield → **parked R5 (later installment)** · Viserys → **Jaehaerys** (cold king/
authority) or **Alicent** (warm reaction/indulgence) by context.

**⏳ DOABLE-NEXT (mappings above; ~3 cards):** cond-heavenly-dao-calibration (Daenys-row→apex; "Operating the
sick-house"→household apothecary; the-Dance rows→parked; "her father intervened"→"the legal document held") ·
cond-alchemists-guild-122ac (the Dance-wildfire-at-scale content → parked-Dance framing; sick-house→apothecary) ·
comedy-register (Daenys-blank-line→apex; Harwin's-list→bestiary; "battlefield of dead dragons"→the apex).

**⛔ DESIGN-FLAG — needs a principal steer before re-derivation (a span-B *plot mechanic*, not naming):**
`prop-kings-hand-note` · `prop-bill-of-exchange` · `cond-trade-network-formation` are built on the **charitable-works
royal license → orphaned at the King's death (Bk III) → cashed in the Dance-chaos (Lock III heist)** mechanic. This is
**incompatible with span-A**: Jaehaerys **lives** through the escape (d. 103 AC, after the ~95 AC escape — he's the living
cage she flees), the **Dance is parked**, and the spine's actual escape runs on **off-books dice-coin + three layers of
paper** (III.1), not an orphaned royal license. Also the warm "fond father granted it" register is Viserys's — in span-A
the cold King wouldn't, so the grant would route through **Alicent's** influence or be reframed as the Queen's patronage.
**Open question:** in span-A, what is the legal-cover mechanic for (a) the Books I–II supply chain and (b) the Lock-III
escape — re-derive these cards to the off-books-coin approach, keep a modified Books-I–II license (granted via Alicent)
and drop the orphan/Dance heist, or tombstone? The spine doesn't pin it. **Do not guess.**
