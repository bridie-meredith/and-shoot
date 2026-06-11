# TOMBSTONE — stale warehouse cards (2026-06-11)

**What:** 11 warehouse cards + 5 paired persona-exemplars, all artifacts of the **pre-migration
old framing** (Saerys / Viserys-I-father / 122 AC / the Dance in Book III) that the run-03 → run-04
span-A migration superseded or parked. Moved out of the live `warehouse/` and `persona-exemplars/`
so the live card set reconciles to current canon (Gael, Jaehaerys-I-father, ~84–95 AC, the Dance
**parked** for a later span-B installment).

**Why retired:** the live cast roster (`staff/showrunner/memory.md` → `cast_roster`) is span-A only.
None of these entities appears in span-A; each is either a character parked for the Dance book, an
old-framing father-function card now superseded, or a condition/prop keyed to the wrong era. **Nothing
is deleted** (retired/ convention) — these revive intact if/when the parked Dance installment is taken up.

## Retired cards (`warehouse/`)

| card | class | why retired | replaced-by / parked-for |
|------|-------|-------------|--------------------------|
| `viserys-i-targaryen` | persona | old "good-king father" framing | **superseded** → `jaehaerys-i-targaryen` (its card states it "replaces the stale viserys card's father-function for span-A") |
| `helaena-targaryen-122ac` | persona | 122 AC era + wrong sibling-order vs GUARD-4 (was Gael's *elder* sister, b.109, m. Aegon II) | **parked** (Dance / span-B) |
| `helaena-targaryen-122ac-behavior` | behavior | pairs with above | parked |
| `daenys-velaryon` | persona | Dance-era lover / wild-dragon rider / counter-thesis | **parked** (memory: "PARKED for the Dance book") |
| `daenys-velaryon-behavior` | behavior | pairs with above | parked |
| `nymeria-summer-isles` | persona | Dance-era archer-guide / conscience / deck-witness | **parked** (memory) |
| `ser-harwin-the-patient` | persona | old-framing Book-II surrogate father ("the no-eat list") | **parked** (memory) |
| `prop-harwins-list` | prop | Harwin's running-gag list — pairs with Harwin | parked with `ser-harwin-the-patient` |
| `cond-alchemists-guild-122ac` | condition | 122 AC Guild; the old I.5 "furnace-sect" guild-fever beat (run-04 I.5 = the Daemon drain, not wildfire) | parked / re-author under span-A if needed |
| `prop-wildfire-shard` | prop | the old I.5 wildfire ingestion — pairs with the Guild | parked with `cond-alchemists-guild-122ac` |
| `cond-saerys-formation-map-red-keep` | condition | Saerys-named + keyed to Viserys-I's authority as the formation's power-source + his death as the Book-III hinge | concept survives (Gael still reads rooms as a cultivator) → **re-author under span-A / Jaehaerys authority if a dedicated card is wanted** |

## Retired persona-exemplars (`persona-exemplars/`)

`viserys-i-targaryen.md` · `helaena-targaryen-122ac.md` · `daenys-velaryon.md` ·
`ser-harwin-the-patient.md` · `nymeria-summer-isles.md` — paired with the retired persona cards above.

## Live-warehouse reconciliation done in this pass

- `warehouse/loc-maegors-holdfast.card.md` — dropped its dead `cond-saerys-formation-map-red-keep`
  reference (frontmatter `references:` line + the prose cross-reference clause now points here instead).

## Residual references — NOT load-bearing for production (left in place by design)

These point at retired slugs but live in **pre-migration provenance docs or design ledgers**, not in
live production cards. Cleaning them is housekeeping for a later pass, not this one:

- `staff/margit/coverage-audit-2026-06-06.md` — **entirely pre-migration** (Saerys/Viserys/122 AC/Dance-in-Bk-III). Provenance; do not treat as live inventory.
- `design/run-03/*`, `design/run-04/family-tree.md`, `design/run-04/state-ledger.md` — design ledgers that still carry parked-cast rows.
- `design/counterfactual-life/*`, `design/cultivation-library/*`, `intake/reconciliation-worksheet.md`, `intake/character-reactions.md`, `intake/CHARACTER-LAYER-INDEX.md` — narrative/design layer.

## NOT retired — the four `saerys-*` slug-anchors (deliberate)

`saerys-targaryen` (`scope: tombstone`), `saerys-maester`, `saerys-septa`, `saerys-targaryen-behavior`
remain in `warehouse/`. They are tombstone-marked predecessors whose **slugs are load-bearing**: ~30
live cards reference `saerys-targaryen` via `references:`/`supersedes:` frontmatter, and there is no
`gael-targaryen-behavior` card — `saerys-targaryen-behavior` is still the protagonist's active behavior
layer. The migration **deliberately left the slugs un-repointed** (see the explicit naming note in
`warehouse/pella-chambermaid.card.md`). Physically retiring these would orphan the live set.

**Era-fix debt (separate task, NOT done here):** repoint live-card slug-refs `saerys-targaryen →
gael-targaryen`, `saerys-maester → maester-lorren`, `saerys-septa → septa-aldith`; author a
`gael-targaryen-behavior` card (or rename the behavior card); then these four can be retired too. Also
rewrite the residual "Saerys"/"Viserys" **prose** in live cards (e.g. `loc-maegors-holdfast`,
`cond-trade-network-formation`, `prop-bill-of-exchange`, `prop-kings-hand-note`, `the-factor`,
`prop-cradle-egg`) and the dangling `cond-kl-geography-122ac` / `cond-kl-court-state-122ac` references.
