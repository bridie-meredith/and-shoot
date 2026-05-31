# /and-facets b01c07 Phase 5b — audience-gate aggregation (cycle 1)

date: 2026-05-31
aggregation_rule: URI-AUDIENCE-AGGREGATION-RULE (3-of-3 strict; single dissent fails the facet)
reviewers:
  non-sensory + dialogue: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]
  sensory: [sensory-modality-coverage, sensory-disambiguation-pedant, sensory-old-state-reader]

## Cycle verdict: FAIL — 7 PASS / 4 FAIL → remediation cycle 2

| facet | cape-fic | dark-fantasy | worm-canon | modality | disambig | old-state | verdict |
|---|---|---|---|---|---|---|---|
| interest-narrator | REVISE | ACCEPT | ACCEPT | — | — | — | **FAIL** |
| memory | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| feeling | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| metaphor | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| vibes | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| exposition | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| location-state | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| state-updates | ACCEPT | ACCEPT | ACCEPT | — | — | — | PASS |
| sensory | — | — | — | ACCEPT | REVISE | REVISE | **FAIL** |
| dialogue-septon-halvard | REVISE | ACCEPT | ACCEPT | — | — | — | **FAIL** |
| dialogue-taylor | ACCEPT | REVISE | REVISE | — | — | — | **FAIL** |

Earth-Bet hard-fence (worm-canon, chapter-level): **CLEAN** across all facets + utterances.

## Consolidated callouts for remediation (deduped)

### A. interest-narrator — FAIL (cape-fic-reader REVISE; AP-001 cap)
- **[narrator:3] @15** — recast the sentence-final collapsed-predicate ("...that is the answer she is giving in place of the rebuttal she is holding back"). AP-001 inverted-predicate cap is ≤1/file; the file has two (narrator:3@15 + narrator:4@19). Spend the one allowed cap on **narrator:4@19** (the WATCH-1 named-death anchor — keep it). Recast **narrator:3@15** to a non-inverted-predicate form; substance-delta content survives the recast. Routing: fixer → NI-author (in-place facet edit). No anchor/citation change.

### B. sensory — FAIL (old-state-reader + disambiguation-pedant REVISE)
- **[sensory:1] @12** (FAIL both specialists) — `halvard-pastoral-account` old-state has NO loc-state sound baseline (oc-sept-corner loc-states carry zero sound fields). Fix per cycle-1 ADD pre-validation: FIRST backfill a sound field into loc-state (loc-state:3@9 or loc-state:2@7) naming Halvard's speech-register as ambient baseline, THEN re-cite; OR reframe the old-state to what loc-state can supply. If neither lands cleanly, drop.
- **[sensory:2] @17** (REVISE both) — old-state `passage-lane-packed-earth` reaches back past the governing loc-state (stone established @15) to the pre-entry lane @7; AND sustained-as-inflection (fires 5 bones after its real inflection point). Fix: correct old-state to the stone surface (loc-state:4@15 language, e.g. `sept-corner-stone-firm`), OR relocate the fire to @7 (entry). 
- **[sensory:4] @22** (FAIL disambiguation-pedant; this is a grd-002 licensed-grounding entry) — `cold-settled-through-standing-weight` is cumulative/sustained re-registration, not a discrete delta → belongs in NI, not sensory. BUT the grd-002 airless gap at @22 is REAL (Phase 4.5 confirmed) and must stay grounded. Fix: RECAST the modality to a **discrete proprioceptive or sound event** at the steadying (pedant's prescription: heel-shift / sole-scrape on cobble as she halts the departure impulse) — preserve the grd-002 grounding (cap-exempt, keep the `licensed-grounding-exception: grd-002` tag), change only the modality/content to a genuine discrete delta. Must remain distinct from sensory:2@17 (tactile cobble-grip) and sensory:3@16 (thermal breath).
- Routing: fixer → sensory-author (add mode for the loc-state backfill + recast). Re-run build_cite_index after.

### C. dialogue-septon-halvard-flea-bottom — FAIL (cape-fic-reader REVISE; 2 ACCEPT incl. a positive defense)
- **[septon-halvard:1] @12** — cape-fic: entry :1's "It grows crooked at the rate it was always going to grow" is too polished/certain for Halvard's honest-uncertainty card register (a prepared closer, not honest accounting). **CONFLICT:** dark-fantasy explicitly DEFENDED this exact form ("aphorism-form is honesty-without-omniscience, not a dodge"); worm-canon ACCEPT. Routing: Phase 5b dialogue protocol → fixer dispatches dialogue-writer in **defense-or-revise mode**. Given the split (1 attack vs 1 positive defense + 1 accept), the dialogue-writer judges: defend (must then satisfy cape-fic on re-fire) or revise toward honest-stumbling (the insight arrives as discovery, not a finished maxim). Dialogue is write-owned (Rule 15) — edit lands in `theater/dialogue/septon-halvard-flea-bottom.md`.

### D. dialogue-taylor-hebert-kl-122ac — FAIL (dark-fantasy + worm-canon REVISE; TWO-PERSONA CONVERGENCE)
- **[taylor:1] @19** — dark-fantasy AND worm-canon INDEPENDENTLY flagged the SAME closing sentence: **"She's why I'm in Flea Bottom at all"** converts Wenna Cobb's death from cost into self-justification — Taylor "wins" the exchange the chapter is built to leave undefeated (dark-fantasy: card no-self-justification-to-the-room prohibition; worm-canon: card-forbidden spoken-motive-to-interlocutor register). High-confidence (2 independent personas, same sentence). Fix: delete or rephrase the final sentence; the entry closes cleanly on "She's the first name in the count" (ledger-position, accepted). cape-fic ACCEPTED the entry overall but its Stage-2 had flagged the suasion-edge as sub-threshold — consistent. Routing: fixer → dialogue-writer revise mode; edit lands in `theater/dialogue/taylor-hebert-kl-122ac.md`.

## Passing facets (do NOT re-fire at cycle 2): memory, feeling, metaphor, vibes, exposition, location-state, state-updates.
## Re-fire at cycle 2 (after fixer): interest-narrator, sensory, dialogue-halvard, dialogue-taylor.
## Note: a sensory fix that backfills a loc-state sound field will re-touch location-state — re-fire location-state at cycle 2 IF its content changes (the backfill is an ADD, so location-state's prior PASS may need a confirm).
