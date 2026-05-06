# Behaviors Index

All behavior cards. Maintained by margit — update on every card store, quality change, or new authoring.

(Directory is named `cards/dialects/` for legacy reasons; class is `behavior`. Directory rename pending.)

Behavior cards carry voice samples, non-verbal tics, and memory-monument register for shoot-v2 dialogue authoring and audience review. Composition along three axes: **period × region × social-class** for shared cards, plus per-character cards on top.

Schema: `schemas/card.schema.md` §behavior.

---

## by_world

### earth-bet
- [taylor-hebert](taylor-hebert.card.md) — per-character; base behavior for Taylor Hebert; first-person tactical / dirty-realist; full

### planetos
- [taylor-hebert-westeros](taylor-hebert-westeros.card.md) — per-character; Westeros 120 AC variant (eleven-year-old sept ward, doubled register); inherits taylor-hebert; references grrm-mannerisms + smallfolk + septon; full
- [westeros-grrm-mannerisms](westeros-grrm-mannerisms.card.md) — shared; universal Westerosi prose eccentricities (time-keeping, X-and-twenty numbers, Anglo-Saxon morphology, universal monuments); full
- [westeros-smallfolk](westeros-smallfolk.card.md) — shared class; baseborn commoners; full
- [westeros-noble-courtly](westeros-noble-courtly.card.md) — shared class; highborn / courtly; full
- [westeros-maester](westeros-maester.card.md) — shared class/institutional; Citadel-trained maesters; full
- [westeros-septon](westeros-septon.card.md) — shared class/institutional; Faith of the Seven septons; full
- [westeros-northern](westeros-northern.card.md) — shared region; the North; old-gods, First Men, austere; full

---

## by_character

### taylor-hebert
- [taylor-hebert](taylor-hebert.card.md) — base, library, earth-bet
- [taylor-hebert-westeros](taylor-hebert-westeros.card.md) — variant, project, planetos; inherits taylor-hebert

---

## shared / inheritable

Behavior pattern banks intended to be referenced by per-character cards via `inherits:` (single parent) and `references:` (additional composition). Not personally voiced — describe how a class, region, or period of speakers sounds, moves, and weights memory.

### Westeros (planetos)

**Universal overlay:**
- [westeros-grrm-mannerisms](westeros-grrm-mannerisms.card.md) — composes with every Westerosi card: time-keeping (moons, name-days, fortnights), X-and-twenty numbers, *a-* prefix, Saxon compounds, recurring phrases, universal monuments (Aegon's Conquest, the Dance, etc.)

**Class registers:**
- [westeros-smallfolk](westeros-smallfolk.card.md) — baseborn; *m'lord*, double-negatives, collapsed-tense, Faith-conversational
- [westeros-noble-courtly](westeros-noble-courtly.card.md) — highborn; *my lord*, *shall*-modal, subordination, periodic sentences
- [westeros-maester](westeros-maester.card.md) — Citadel; *yes, yes*, polite-brief, citation-as-interruption
- [westeros-septon](westeros-septon.card.md) — Faith; *child*, homiletic three-and-close, plain-Anglo moral closers

**Regional registers:**
- [westeros-northern](westeros-northern.card.md) — North; old-gods, *aye*-preserved-across-class, understated punchline, weirwood-touch, the cold as actor

**Pending:**
- westeros-dornish (regional; Rhoynar-influenced, soft drawl, direct register)
- westeros-ironborn (regional; What Is Dead May Never Die, salt-and-iron register)
- westeros-reach (regional; flowery, Faith-saturated, courtly-leaning)
- westeros-stormlands, westeros-westerlands, westeros-vale, westeros-crownlands, westeros-riverlands (regional)
- westeros-free-folk (regional; beyond-the-Wall; *kneeler*, *you know nothing*)
- westeros-flea-bottom (sub-class; King's Landing slum register)
- westeros-royal (intensification of noble-courtly for Targaryen kings/queens)
- westeros-septa (sister card to septon)

### Essos (planetos)

**Pending:**
- essos-free-cities (regional; Braavosi-leaning; *valar morghulis*, *a man*, courteous register)
- essos-braavosi (sub-region; water-dancer cadence)
- essos-pentoshi, essos-tyroshi, essos-myrish, essos-lyseni, essos-volantene, essos-norvoshi, essos-qohorik, essos-lorathi (sub-region)
- essos-dothraki (regional; horse-lord register; *my sun and stars*, *moon of my life*, *it is known*)
- essos-ghiscari-slavers-bay (regional; Old Ghis register, slave-trade vocabulary)
- essos-qartheen (regional; *the city of cities, the world's gate*)
- essos-asshai (regional; shadow-binder, hidden-tongue)

### Earth-Bet (none yet)

---

## Composition stack (per-character loading)

For a Westeros-set per-character card, the canonical loading stack:

1. `westeros-grrm-mannerisms` (universal overlay) — always
2. Region card (e.g. `westeros-northern`) — if applicable
3. Class card (e.g. `westeros-noble-courtly`) — always
4. Per-character card (e.g. `eddard-stark`) — the leaf

Schema's `inherits:` cap is currently 1; per-character card sets `inherits:` to the most-specific parent (typically the class or character-shaping card) and lists the rest in `references:`. The dialogue-writer fork and audience reviewer compose `inherits` + `references` together at load time.

For `taylor-hebert-westeros`, the stack is:
- `inherits:` `taylor-hebert` (carries the deepest character-shaping content)
- `references:` `[westeros-grrm-mannerisms, westeros-smallfolk, westeros-septon]` (universal overlay + class context for sept ward)

---

## Schema reconciliation status

Resolved: dialect → behavior class rename (2026-05-06). The `subclass:` enum now distinguishes `shared-behavior` (no `character:`) from `per-character-behavior` (`character:` required). Frontmatter adds `period:`, `region:`, `social-class:` for composition.

Open: `inherits:` chain cap of 1 is too shallow for full period × region × class composition. Convention is `inherits:` one parent, `references:` the rest. Margit may revisit and lift the cap.
