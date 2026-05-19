# /and-facets b01c01 — shared R1 brief

This file is the **common context block** every R1 facet author should read.
It carries chapter-level substance delta, scene boundaries, cast, locations,
and the canonical bones list with line numbers. Each author's per-facet
brief points here to avoid re-stating the same facts.

---

## Chapter identity

- Episode slug: `b01c01` (memory) / `b01-c01` (file paths)
- Narrator (POV): `taylor-hebert-kl-122ac`
- Goal: "the operating rule in its intact form, the ward it will fail to protect, and the child who will pay the price of its failure."
- Cast (3): `taylor-hebert-kl-122ac`, `coll-net-mender-flea-bottom`, `wren-stitch-maker-flea-bottom-ward`
- Locations: `flea-bottom` (resolves to `cards/locations/loc-flea-bottom.card.md`)
- Bones file (READ-ONLY): `active-project/theater/bones/b01-c01.md`
- Base proto-lines (your decoration target): `active-project/theater/proto-lines/b01-c01.md` (copy of bones; you copy it to your `_inflight/` path and append `[<facet>:<id>]` tokens)
- Scene-map: `active-project/theater/facets/scene-map-b01-c01.md`
- Bones in scope: 24 numbered 1-26 (gaps @10 and @19 are time-skip markers — DO NOT cite)

---

## Chapter substance_delta (from showrunner memory)

```yaml
axes_in_motion:
  - axis: capability
    direction: null
    target_delta_magnitude: 0
    notes: "dormant; passive insect-sense only; suppressed baseline at rank 3"
  - axis: knowledge
    direction: up
    target_delta_magnitude: 0.5
    notes: "Flea Bottom geography read; ward-level pattern established; 3→3.5; passive orientation; unanchored knowledge gain at baseline"
density_target: "0.6-0.9"
```

## Scene boundaries + per-scene deltas

**Scene-A (b01c01s01) @1-@9 — day-of-arrival**
- scene_conflict: protagonist establishes street-level presence without incurring debt; opposing force is Flea Bottom's vouching social physics; stakes-axis = capability
- substance_delta: capability 0 (passive insect-sense held at threshold; rank 3 unchanged), knowledge +0.2 (Hook, Coll's block, vouching physics; 3→3.2)
- density_target: 0.6-0.7

**Scene-B (b01c01s02) @11-@18 — working-day**
- scene_conflict: protagonist reads ward through insect-sense while holding the prohibition; opposing force is that capability is available and rule is the only thing holding gap open; stakes-axis = capability
- substance_delta: capability 0 (passive throughout; prohibition enacted against no external pressure), knowledge +0.2 (block density maps, movement corridors, watch patrol read passively; 3.2→3.4)
- density_target: 0.7-0.8

**Scene-C (b01c01s03) @20-@26 — third-or-fourth-day, wren arrives**
- scene_conflict: protagonist refuses to complete instrumental assessment of Wren (holds her as face, not node); opposing force is Taylor's own trained pattern-reading auto-initiating; stakes-axis = knowledge
- substance_delta: capability 0 (pattern-reading runs and is caught by rule; not deployed), knowledge +0.1 (Wren registered as face-not-node; ward social geometry one layer deeper; 3.4→3.5)
- density_target: 0.7-0.9

Time-skip markers: `@10` (next-working-day shift), `@19` (multi-day gap; Wren first appears "on the third or fourth day").

---

## Bones (canonical, READ-ONLY — append-citations-only on your `_inflight/` copy)

```
1 taylor-hebert-kl-122ac enters the corner-room
2 taylor-hebert-kl-122ac pays the-door-keeper
3 coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac
4 coll-net-mender-flea-bottom extends the needle
5 taylor-hebert-kl-122ac takes the needle
6 taylor-hebert-kl-122ac threads the needle
7 taylor-hebert-kl-122ac handles the nets
8 the insects cover the flagstones
9 coll-net-mender-flea-bottom faces the street
[time-skip @10]
11 taylor-hebert-kl-122ac threads the needle
12 the insects fill the block
13 the walls cool
14 taylor-hebert-kl-122ac handles the nets
15 the city-watch passes the hook
16 taylor-hebert-kl-122ac holds the feet
17 the needle threads the mesh
18 taylor-hebert-kl-122ac drops the nets
[time-skip @19]
20 wren-stitch-maker-flea-bottom-ward enters the street
21 wren-stitch-maker-flea-bottom-ward approaches taylor-hebert-kl-122ac
22 wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac
23 taylor-hebert-kl-122ac faces wren-stitch-maker-flea-bottom-ward
24 taylor-hebert-kl-122ac holds the eyes
25 taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward
26 wren-stitch-maker-flea-bottom-ward leaves the street
```

Speech bones (URI-DIALOGUE-COVERAGE-GATE — each MUST receive at least one dialogue citation):
- `@3` coll → taylor
- `@22` wren → taylor
- `@25` taylor → wren

---

## Output contract per author

1. Read your facet rubric in full.
2. Read this brief.
3. Read named inputs the rubric calls for.
4. Author your facet entries per rubric format. Use the facet's canonical ID convention (1-indexed, monotonic).
5. Copy `active-project/theater/proto-lines/b01-c01.md` → `active-project/theater/facets/_inflight/proto-lines-<facet-prefix>.md`. Append `[<facet-prefix>:<id>]` to each line you decorated. **Bones bodies (the SVO text) must be byte-identical** — append-only on the trailing bracket list. Existing `[<other-prefix>:<id>]` citations are preserved.
6. Time-skip lines (`10`, `19` — the bare numbered lines with no SVO) CAN be skipped entirely.
7. Per-file cull: review your own entries once before writing; delete any entry that doesn't survive rubric scrutiny.

## Hard fences (universal)

- Earth-Bet proper nouns are BANNED in narrator-prose, exposition glosses, sensory descriptions, vibes, feeling, memory, dialogue. Banned slugs (non-exhaustive): Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea. The KL world stack is at `active-project/warehouse/cond-earth-bet-noun-fence.md` and `cond-khepri-residue-122ac.md` (the latter codifies how Khepri-residue is rendered without naming).
- POV: first-person Taylor. Non-Taylor inner-life facets (feeling-coll, feeling-wren) author from those characters' inner registers without leaking into Taylor's POV narration.
- Tens is upstream-only this run (URI-SUBSTANCE-OVERHAUL); do NOT consult or cite `tens:` — substance_delta is the new pressure-signal.
