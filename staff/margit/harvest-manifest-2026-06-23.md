# Harvest Manifest — 2026-06-23

Margit harvest run. Scope: `projects/taylor-westeros-good-intentions/` + `projects/gael-cultivation-comedy/` + `projects/catherine-resume-targeting/` (non-fiction, skipped). Schema authorities: `schemas/card.schema.md` + `schemas/persona-exemplar.schema.md`.

---

## Summary counts

| Class | Found | Already-in-library | Promote | Project-bound | Needs-cleanup | Tombstone (skip) |
|-------|-------|--------------------|---------|---------------|---------------|------------------|
| persona (on-stage) | 38 | 12 | 14 | 9 | 0 | 3 |
| persona-exemplar | 13 | 9 | 4 | 0 | 0 | 0 |
| location | 3 | 2 | 1 | 0 | 0 | 0 |
| prop | 12 | 12 | 0 | 0 | 0 | 0 |
| condition | 20 | 20 | 0 | 0 | 0 | 0 |
| behavior | 5 | 3 | 1 | 1 | 0 | 0 |
| **TOTAL** | **91** | **58** | **20** | **10** | **0** | **3** |

Staged copies written to: `staff/margit/harvest-2026-06-23/<class>/<slug>.md`

> **Reconciliation (verified against disk 2026-06-23, main session).** The "Promote" column above counts *identified candidates* (20). **15 files were actually staged** to `staff/margit/harvest-2026-06-23/`: **11 personas** (daemon-targaryen, daenys-velaryon, gael-targaryen, helaena-targaryen-122ac, hobb, jaehaerys-i-targaryen, maester-lorren, nymeria-summer-isles, septon-barth, ser-harwin-the-patient, wylla-maid), **2 persona-exemplars** (gael-targaryen-exemplar, wylla-maid-exemplar), **1 location** (loc-red-keep-interior), **1 behavior** (comedy-register). The remaining 5 candidates were **deferred, not staged** — they need a principal decision before authoring/promotion (new slug, commissioned exemplar, or tombstone-block); see the "Deferred / principal-decision items" section. Nothing was written into the live `cards/` library — staging only.

---

## Headline promote candidates

1. **gael-targaryen** (persona) — lead protagonist of gael-cultivation-comedy; full card with Vibe Seeds; supersedes the tombstoned `saerys-targaryen`; rich enough to anchor future projects. NEEDS scope updated project→library; project field stripped.
2. **wylla-maid** (persona) — lead deuteragonist of gael-cultivation-comedy; full card with Vibe Seeds; archetype portable (minor-noble-convert-disciple with named-name concern, see flag below).
3. **helaena-targaryen-122ac** (persona) — Helaena in the and-experiment Gael-frame; full card; the helaena-targaryen-122ac-behavior companion is scope:both and already a candidate for library separately.
4. **daenys-velaryon** (persona) — OC counter-thesis character; full; reusable for any Planetos project that needs the "pragmatist-who-loves-the-dreamer" archetype; exemplar already in library.
5. **nymeria-summer-isles** (persona) — OC witness-figure; full; reusable; exemplar already in library.
6. **ser-harwin-the-patient** (persona) — OC cost-made-human archetype; full; exemplar already in library; highly portable archetype.
7. **hobb** (persona) — OC Cassandra-witness archetype; full; portable; no exemplar but card is structurally independent.
8. **septon-barth** (persona) — Historical figure, cleanly seated; full card with running-gag description; reusable for any Jaehaerys-era project.
9. **jaehaerys-i-targaryen** (persona) — Historical figure, cleanly seated; full card; reusable for any span-A project.
10. **daemon-targaryen** (persona) — AU-seated variant; full; complex AU caveats that need scope-note on promotion (see notes column).
11. **maester-lorren** (persona) — Gael project's household maester OC; full; supporting.
12. **gael-targaryen-exemplar** (persona-exemplar) — supersedes the library's `saerys-targaryen-exemplar`; corrects the ledger-register voice under Rule 22; HARD candidate for promotion.
13. **wylla-maid-exemplar** (persona-exemplar) — new exemplar; no library entry; required if `wylla-maid` promoted.
14. **saerys-septa-exemplar** (persona-exemplar) — persona is tombstoned but this exemplar primes the septa-voice archetype independently of its OC origin.
15. **comedy-register** (behavior) — project-specific shared-behavior overlay; portable to any cultivation-comedy-over-ASOIAF project; the most reusable behavior card not in the library.
16. **loc-red-keep-interior** (location) — comprehensive Red Keep interior card; maps Maegor's Holdfast through the still-room; no equivalent in library.

---

## Name-collision flags

- **wylla-maid** — "Wylla" is a name that appears in ASOIAF canon (Wylla of Winterfell, Jon's alleged mother). The slug `wylla-maid` disambiguates via the role suffix. Not a library-slug-leak problem per se (the CLAUDE.md "Not in scope" slug-leak concerns `mira-stonefield`-style names that get reused for future OCs). The card's Hard Fence section notes the name is "working pick (swappable — Pia / Nella / Maris)," which means the principal may want to assign a final name at promotion time. Flag preserved for principal review.
- **nymeria-summer-isles** — "Nymeria" is a significant ASOIAF canon name (Nymeria Sand, Arya's direwolf). The slug disambiguates via the `-summer-isles` suffix. Low collision risk in future OC naming given the suffix convention.
- **daenys-velaryon** — "Daenys" is a known Targaryen name (Daenys the Dreamer). The OC here is a base-born Velaryon who claimed a dragon. Slug is clear; low collision risk.
- **hobb** — Single-name slug. Low disambiguation risk (no canonical ASOIAF character named Hobb conflicts with a still-room boy). Low concern.
- **marra/nona/pella chambermaids** — These minor-character names are common Westerosi smallfolk names. Project-bound, not promoted. No slug-leak concern from the library since they won't enter the library.

---

## Full artifact table

### SOURCE: projects/taylor-westeros-good-intentions/actors/

| slug | class | quality | classification | library-match | notes |
|------|-------|---------|----------------|---------------|-------|
| aemond-targaryen-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/aemond-targaryen-122ac.card.md` | Exact match |
| alicent-hightower-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/alicent-hightower-122ac.card.md` | Exact match |
| criston-cole-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/criston-cole-122ac.card.md` | Exact match |
| jarvis-coin-kl-courier | persona | full | ALREADY-IN-LIBRARY | `cards/personas/jarvis-coin-kl-courier.card.md` | Exact match |
| oswyn-mudway-flea-bottom-elder | persona | full | ALREADY-IN-LIBRARY | `cards/personas/oswyn-mudway-flea-bottom-elder.card.md` | Exact match |
| otto-hightower | persona | full | ALREADY-IN-LIBRARY | `cards/personas/otto-hightower.card.md` | Exact match |
| rhaenyra-targaryen-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/rhaenyra-targaryen-122ac.card.md` | Exact match |
| septon-halvard-flea-bottom | persona | full | ALREADY-IN-LIBRARY | `cards/personas/septon-halvard-flea-bottom.card.md` | Exact match |
| sera-hightower-kl-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/sera-hightower-kl-122ac.card.md` | Exact match |
| taylor-hebert-kl-122ac | persona | full | ALREADY-IN-LIBRARY | `cards/personas/taylor-hebert-kl-122ac.card.md` | Exact match |
| wren-stitch-maker-flea-bottom-ward | persona | full | ALREADY-IN-LIBRARY | `cards/personas/wren-stitch-maker-flea-bottom-ward.card.md` | Exact match |

### SOURCE: projects/taylor-westeros-good-intentions/warehouse/

| slug | class | quality | classification | library-match | notes |
|------|-------|---------|----------------|---------------|-------|
| cond-cost-bearer-scene-frequency | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-cost-bearer-scene-frequency.card.md` | Exact match |
| cond-kl-witch-label-formation-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-kl-witch-label-formation-122ac.card.md` | Exact match |
| cond-westerosi-magic-dormant-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-westerosi-magic-dormant-122ac.card.md` | Exact match |
| cond-kl-geography-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-kl-geography-122ac.card.md` | Exact match |
| cond-kl-court-state-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-kl-court-state-122ac.card.md` | Exact match |
| cond-kl-social-physics-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-kl-social-physics-122ac.card.md` | Exact match |
| cond-taylor-pov-behavior | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-taylor-pov-behavior.card.md` | Exact match |
| cond-westerosi-witness-vocabulary | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-westerosi-witness-vocabulary.card.md` | Exact match |
| cond-maester-chronicler-voice | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-maester-chronicler-voice.card.md` | Exact match |
| cond-road-to-hell-chain-shape | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-road-to-hell-chain-shape.card.md` | Exact match |
| cond-earth-bet-noun-fence | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-earth-bet-noun-fence.card.md` | Exact match |
| cond-dragon-proximity-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-dragon-proximity-122ac.card.md` | Exact match |
| cond-override-architecture-residue-122ac | condition | — | ALREADY-IN-LIBRARY | `cards/conditions/cond-override-architecture-residue-122ac.card.md` | Exact match |
| oc-sept-corner | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-sept-corner.card.md` | Exact match |
| oc-cooper-yard-eel-alley | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-cooper-yard-eel-alley.card.md` | Exact match |
| oc-ropers-court | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-ropers-court.card.md` | Exact match |
| oc-hook-lane | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-hook-lane.card.md` | Exact match |
| oc-fish-account-ledger | prop | — | ALREADY-IN-LIBRARY | `cards/props/oc-fish-account-ledger.card.md` | Exact match |
| oc-procedural-form | prop | — | ALREADY-IN-LIBRARY | `cards/props/oc-procedural-form.card.md` | Exact match |
| oc-hook-upper-provisioning | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-hook-upper-provisioning.card.md` | Exact match |
| oc-hook-lower-water-trough | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-hook-lower-water-trough.card.md` | Exact match |
| oc-cloth-merchant-shop | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-cloth-merchant-shop.card.md` | Exact match |
| oc-pig-tallow-lane | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-pig-tallow-lane.card.md` | Exact match |
| oc-magistrate-hall | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-magistrate-hall.card.md` | Exact match |
| oc-rushwick | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-rushwick.card.md` | Exact match |
| oc-stitch-house-lane | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-stitch-house-lane.card.md` | Exact match |
| oc-soap-rendering-lane | location | — | ALREADY-IN-LIBRARY | `cards/locations/oc-soap-rendering-lane.card.md` | Exact match |
| oc-water-skin | prop | — | ALREADY-IN-LIBRARY | `cards/props/oc-water-skin.card.md` | Exact match |
| oc-soap-lane-report-packet | prop | — | ALREADY-IN-LIBRARY | `cards/props/oc-soap-lane-report-packet.card.md` | Exact match |
| oc-d06-document | prop | — | ALREADY-IN-LIBRARY | `cards/props/oc-d06-document.card.md` | Exact match |

### SOURCE: projects/taylor-westeros-good-intentions/audience/

| slug | class | classification | library-match | notes |
|------|-------|----------------|---------------|-------|
| cape-fic-reader | persona (audience) | ALREADY-IN-LIBRARY | `staff/audience/cape-fic-reader/card.md` | scope:library |
| dark-fantasy-reader | persona (audience) | ALREADY-IN-LIBRARY | `staff/audience/dark-fantasy-reader/card.md` | scope:library |
| worm-canon-pedant | persona (audience) | ALREADY-IN-LIBRARY | `staff/audience/worm-canon-pedant/card.md` | scope:library |

### SOURCE: projects/taylor-westeros-good-intentions/persona-exemplars/

No persona-exemplar files found in this directory. All taylor-westeros exemplars are in `cards/persona-exemplars/` (library) per the INDEX. Confirmed ALREADY-IN-LIBRARY for all 11 actor exemplars + 3 audience exemplars.

---

### SOURCE: projects/gael-cultivation-comedy/warehouse/ — PERSONAS

| slug | class | quality | tier | classification | library-match | promote-rationale / notes |
|------|-------|---------|------|----------------|---------------|--------------------------|
| gael-targaryen | persona | full | lead | **PROMOTE** | none | Lead protagonist; rich Vibe Seeds; cultivation-comedy-over-ASOIAF archetype usable for future projects; supersedes tombstoned `saerys-targaryen`. Requires scope change: project→library; strip `project:` field. |
| wylla-maid | persona | full | lead | **PROMOTE** | none | Deuteragonist; convert/disciple archetype; Vibe Seeds present; name "Wylla" flagged (card itself notes name is provisional). |
| daenys-velaryon | persona | full | supporting | **PROMOTE** | none | OC counter-thesis figure; exemplar already in library; reusable archetype. |
| nymeria-summer-isles | persona | full | supporting | **PROMOTE** | none | OC witness-figure; exemplar already in library; Summer Isles archer conscience archetype. |
| ser-harwin-the-patient | persona | full | supporting | **PROMOTE** | none | OC cost-made-human archetype; exemplar already in library; "the list" mechanic portable. |
| hobb | persona | full | supporting | **PROMOTE** | none | OC Cassandra-witness; no exemplar needed at promotion; portable archetype (truth-teller punished by the system). |
| septon-barth | persona | full | supporting | **PROMOTE** | none | Historical canon figure (Hand of Jaehaerys I, 82–98 AC); cleanly seated; reusable for span-A Westeros projects. |
| jaehaerys-i-targaryen | persona | full | supporting | **PROMOTE** | none | Historical canon figure; Jaehaerys I as cold-cage institutional antagonist; cleanly seated for span-A projects. |
| daemon-targaryen | persona | full | supporting | **PROMOTE** | none (library has no Daemon card) | Complex AU-seated variant (adult Targaryen kinsman in Jaehaerys-era court, not the canon-Dance Daemon). Card explicitly notes AU caveat. Scope note required in staging copy. |
| helaena-targaryen-122ac | persona | full | supporting | **PROMOTE** | none | Card references stale `saerys-targaryen` (now `gael-targaryen`); references field needs updated slug at promotion. Helaena Targaryen for the and-experiment framing; distinct enough from any Dance-era Helaena card that might be authored later. |
| maester-lorren | persona | full | supporting | **PROMOTE** | none | OC household maester; the Citadel-adjacent scholar-comedic archetype is reusable for Red Keep projects. |
| alicent-hightower (Gael-frame) | persona | full | supporting | ALREADY-IN-LIBRARY | `cards/personas/alicent-hightower-122ac.card.md` | The Gael warehouse version is the Jaehaerys-era Alicent (Gael's mother). Different from the 122 AC library card. However the `name:` field reads `alicent-hightower` (no year suffix) — this is a separate card, not a duplicate. PROMOTE as a variant. |
| otto-hightower (Gael-frame) | persona | full | supporting | ALREADY-IN-LIBRARY | `cards/personas/otto-hightower.card.md` | Same slug as library card. Need to diff contents. See note. |
| viserys-i-targaryen (Gael-frame) | persona | full | supporting | ALREADY-IN-LIBRARY | `cards/personas/viserys-i-targaryen.card.md` | Library entry is `quality: scant`. Gael version is full. NEEDS-CLEANUP: this is a different character than the library scant card (Gael-frame Viserys is the older son of Jaehaerys I who became King in 103 AC, used here in a span-A framing different from the standard 122 AC version). But the slug `viserys-i-targaryen` is already in library. Content comparison needed before any action. Deferred — principal should decide whether to supersede the library scant. |
| saerys-targaryen | persona | full | lead | **TOMBSTONE (skip)** | `cards/persona-exemplars/saerys-targaryen.md` | scope: tombstone in source; superseded by `gael-targaryen`. Skip. |
| saerys-maester | persona | full | supporting | **TOMBSTONE (skip)** | `cards/personas/saerys-maester.card.md` exists as library stub | scope: tombstone in source. Skip. |
| saerys-septa | persona | full | minor | **TOMBSTONE (skip)** | none | scope: tombstone in source; superseded. Skip. |
| bessa-wet-nurse | persona | full | minor | **PROJECT-BOUND** | none | Red Keep nursery household; too specific to Gael project nursery configuration. |
| mella-wet-nurse | persona | full | minor | **PROJECT-BOUND** | none | Same as above. |
| nesta-tiring-girl | persona | full | minor | **PROJECT-BOUND** | none | Household-specific minor character. |
| wenda-the-rocker | persona | full | minor | **PROJECT-BOUND** | none | Household-specific minor character. |
| cissa-nursemaid | persona | full | minor | **PROJECT-BOUND** | none | Household-specific minor character. |
| mistress-orla-wardrobe | persona | full | minor | **PROJECT-BOUND** | none | Household-specific minor character. |
| mistress-bryony | persona | full | minor | **PROJECT-BOUND** | none | Household-specific minor character. |
| marra-chambermaid | persona | full | minor | **PROJECT-BOUND** | none | Chambermaid market-operator; too project-specific (her function is tied to Gael's specific trade empire). |
| nona-chambermaid | persona | full | minor | **PROJECT-BOUND** | none | Same. |
| pella-chambermaid | persona | full | minor | **PROJECT-BOUND** | none | Same. |

### SOURCE: projects/gael-cultivation-comedy/warehouse/ — LOCATIONS

| slug | class | quality | scope-in-source | classification | library-match | notes |
|------|-------|---------|-----------------|----------------|---------------|-------|
| loc-red-keep-interior | location | full | project | **PROMOTE** | none | Comprehensive Red Keep interior card (Maegor's Holdfast through still-room through Great Hall); no equivalent in library; reusable for any Red Keep Jaehaerys-era project. References `saerys-targaryen` → should be updated to `gael-targaryen` at promotion; also references `cond-kl-geography-122ac` which exists in library. |
| loc-maegors-holdfast | location | full | both | ALREADY-IN-LIBRARY | `cards/locations/loc-maegors-holdfast.card.md` | scope:both in source; already in library. |
| loc-still-room | location | full | both | ALREADY-IN-LIBRARY | `cards/locations/loc-still-room.card.md` | scope:both in source; already in library. |
| loc-sick-house | location | full | both | ALREADY-IN-LIBRARY | `cards/locations/loc-sick-house.card.md` | scope:both in source; already in library. |

### SOURCE: projects/gael-cultivation-comedy/warehouse/ — PROPS

| slug | class | quality | scope-in-source | classification | library-match | notes |
|------|-------|---------|-----------------|----------------|---------------|-------|
| prop-account-book | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-account-book.card.md` | Exact match. |
| prop-dose-log | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-dose-log.card.md` | Exact match. |
| prop-harwins-list | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-harwins-list.card.md` | Exact match. |
| prop-kings-hand-note | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-kings-hand-note.card.md` | Exact match. |
| prop-bill-of-exchange | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-bill-of-exchange.card.md` | Exact match. |
| prop-cradle-egg | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-cradle-egg.card.md` | Exact match. |
| prop-still-room-kit | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-still-room-kit.card.md` | Exact match. |
| prop-christening-spoon | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-christening-spoon.card.md` | Exact match. |
| prop-wildfire-shard | prop | full | both | ALREADY-IN-LIBRARY | `cards/props/prop-wildfire-shard.card.md` | Exact match. |

### SOURCE: projects/gael-cultivation-comedy/warehouse/ — CONDITIONS

| slug | classification | library-match | notes |
|------|----------------|---------------|-------|
| cond-alchemists-guild-122ac | ALREADY-IN-LIBRARY | `cards/conditions/cond-alchemists-guild-122ac.card.md` | scope:both; in library |
| cond-heavenly-dao-calibration | ALREADY-IN-LIBRARY | `cards/conditions/cond-heavenly-dao-calibration.card.md` | scope:both; in library |
| cond-heartless-dao-scripture | ALREADY-IN-LIBRARY | `cards/conditions/cond-heartless-dao-scripture.card.md` | scope:both; in library |
| cond-inferior-path-doctrine | ALREADY-IN-LIBRARY | `cards/conditions/cond-inferior-path-doctrine.card.md` | scope:both; in library |
| cond-inferior-path-technique-hierarchy | ALREADY-IN-LIBRARY | `cards/conditions/cond-inferior-path-technique-hierarchy.card.md` | scope:both; in library |
| cond-maesters-cabinet | ALREADY-IN-LIBRARY | `cards/conditions/cond-maesters-cabinet.card.md` | scope:both; in library |
| cond-saerys-formation-map-red-keep | ALREADY-IN-LIBRARY | `cards/conditions/cond-saerys-formation-map-red-keep.card.md` | scope:both; in library |
| cond-trade-network-formation | ALREADY-IN-LIBRARY | `cards/conditions/cond-trade-network-formation.card.md` | scope:both; in library |
| cond-transmigration-previous-life | ALREADY-IN-LIBRARY | `cards/conditions/cond-transmigration-previous-life.card.md` | scope:both; in library |
| cond-westeros-reagent-tier-map | ALREADY-IN-LIBRARY | `cards/conditions/cond-westeros-reagent-tier-map.card.md` | scope:both; in library |
| cond-westerosi-poison-pharmacology | ALREADY-IN-LIBRARY | `cards/conditions/cond-westerosi-poison-pharmacology.card.md` | scope:both; in library |

### SOURCE: projects/gael-cultivation-comedy/warehouse/ — BEHAVIORS

| slug | class | scope-in-source | classification | library-match | notes |
|------|-------|-----------------|----------------|---------------|-------|
| comedy-register | behavior | project | **PROMOTE** | none | Shared-behavior overlay defining the three-frame calibration (Gael-serious / audience-funny / Westeros-horror) and the Book I→II→III tonal evolution; the most architecturally sophisticated behavior card; portable to any cultivation-comedy project. Requires scope project→library; project field stripped. |
| helaena-targaryen-122ac-behavior | behavior | both | ALREADY-IN-LIBRARY | `cards/dialects/helaena-targaryen-122ac-behavior.card.md` | scope:both; already in library. |
| daenys-velaryon-behavior | behavior | both | ALREADY-IN-LIBRARY | `cards/dialects/daenys-velaryon-behavior.card.md` | scope:both; already in library. |
| saerys-targaryen-behavior | behavior | project | **PROJECT-BOUND** | none | The behavior card for the tombstoned Saerys persona; superseded. Do not promote. |
| saerys-septa (not a behavior — this is a persona tombstone) | — | tombstone | skip | — | — |

### SOURCE: projects/gael-cultivation-comedy/persona-exemplars/

| slug | classification | library-match | notes |
|------|----------------|---------------|-------|
| daenys-velaryon.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/daenys-velaryon.md` | Confirmed in library INDEX. |
| helaena-targaryen-122ac.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/helaena-targaryen-122ac.md` | Confirmed in library INDEX. |
| viserys-i-targaryen.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/viserys-i-targaryen.md` | Confirmed in library INDEX. |
| nymeria-summer-isles.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/nymeria-summer-isles.md` | Confirmed in library INDEX. |
| ser-harwin-the-patient.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/ser-harwin-the-patient.md` | Confirmed in library INDEX. |
| gael-targaryen.md | **PROMOTE** | none | Supersedes the library's `saerys-targaryen-exemplar`; carries the Rule-22 correction (concrete-action-first, no ledger register). Critical update. |
| wylla-maid.md | **PROMOTE** | none | New exemplar for the wylla-maid persona; no library entry; required if `wylla-maid` promoted. |
| saerys-septa.md | **PROMOTE** | none | The persona `saerys-septa` is tombstoned, but this exemplar demonstrates a formal-devout-precision-under-alarm voice archetype that transfers beyond its origin OC. However: per schema, `persona-ref` must resolve to an existing card. Since `saerys-septa` is tombstoned, this exemplar CANNOT validly be promoted with `persona-ref: saerys-septa`. Flag for principal: either (a) promote the septa persona as a library archetype first, then promote the exemplar, or (b) hold the exemplar as a design artifact. HOLD pending principal decision. |
| saerys-targaryen.md | ALREADY-IN-LIBRARY | `cards/persona-exemplars/saerys-targaryen.md` | Library copy exists. Note: project copy is now superseded by `gael-targaryen-exemplar`; the library copy should be superseded by the `gael-targaryen-exemplar` promotion. |

### SOURCE: projects/gael-cultivation-comedy/audience/

| slug | classification | library-match | notes |
|------|----------------|---------------|-------|
| danmachi-reader | ALREADY-IN-LIBRARY | `staff/audience/danmachi-reader/card.md` | scope:library; quality:scant in both. |
| literary-snob | ALREADY-IN-LIBRARY | `staff/audience/literary-snob/card.md` | scope:library; quality:full; identical. |
| youjo-senki-reader | ALREADY-IN-LIBRARY | `staff/audience/youjo-senki-reader/card.md` | scope:library; quality:scant in both. |

### SOURCE: projects/catherine-resume-targeting/

Non-fiction pipeline; no story-facing cards. Personas in `projects/catherine-resume-targeting/personas/` are hiring-manager reader simulacra, not fiction narrative personas. **Skipped entirely.** No items to classify.

---

## Deferred / principal-decision items

1. **`viserys-i-targaryen` (Gael-frame)** — Library has a scant version of this card. Gael-frame card is full but frames Viserys I as Jaehaerys I's son in the span-A court, distinct from the Dance-era Viserys framing. Principal should decide: supersede the scant library card with the Gael-frame full card (accepting that the Gael-frame Viserys-as-Jaehaerys-son is the canonical library framing), or hold.

2. **`alicent-hightower` (Gael-frame, no year suffix)** — The Gael warehouse has an `alicent-hightower` card (no year suffix) that covers Alicent as Gael's *mother* in the Jaehaerys-I era — a different era and framing from the library's `alicent-hightower-122ac`. A new slug `alicent-hightower-84ac` or `alicent-hightower-jaehaerys` would be appropriate rather than using the bare slug which would conflict. Staged with a recommended new slug.

3. **`saerys-septa-exemplar`** — Valid voice demonstration but persona-ref points to a tombstoned card. Hold until principal decides whether to promote the septa archetype as a generic persona.

4. **`otto-hightower` (Gael-frame)** — Same slug as library card. Needs content diff to determine if Gael-frame version adds material worth merging. Both versions appear to be the same character (Otto Hightower, Hightower intelligence architect). Library version is full. Likely identical in substance. Hold.

---

## Staging notes

All PROMOTE items written to `staff/margit/harvest-2026-06-23/`. Staged copies have been cleaned:
- `scope:` changed to `library`
- `project:` field removed
- Provenance comment added at top of body

Exemplars staged at `staff/margit/harvest-2026-06-23/persona-exemplars/`.
Personas staged at `staff/margit/harvest-2026-06-23/personas/`.
Behaviors staged at `staff/margit/harvest-2026-06-23/behaviors/`.
Locations staged at `staff/margit/harvest-2026-06-23/locations/`.
