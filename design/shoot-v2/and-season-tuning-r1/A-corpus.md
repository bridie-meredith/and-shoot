---
phase: A — corpus prep
date: 2026-05-10
run: and-season-tuning-r1
locked-rubric: design/shoot-v2/and-season-tuning-r1/rubric-and-season.md
---

# Phase A — Corpus Prep

## Files in scope

| Artifact | Path | Size |
|---|---|---:|
| Season aggregate (canonical, pre-split) | `active-project/theater/proto-lines/s01.aggregate.md` | 900 numbered lines + 5 inline `# pov:` markers |
| Episode 1 split | `active-project/theater/proto-lines/s01e01.md` | aggregate range 1–149 |
| Episode 2 split | `active-project/theater/proto-lines/s01e02.md` | aggregate range 150–250 |
| Episode 3 split | `active-project/theater/proto-lines/s01e03.md` | aggregate range 251–418 |
| Episode 4 split | `active-project/theater/proto-lines/s01e04.md` | aggregate range 419–563 |
| Episode 5 split | `active-project/theater/proto-lines/s01e05.md` | aggregate range 564–699 |
| Episode 6 split | `active-project/theater/proto-lines/s01e06.md` | aggregate range 700–912 |
| Season plan | `active-project/staff/showrunner/season-s01-plan.md` | content beats + cast/stage matrices |
| Series plan | `active-project/staff/showrunner/series-plan.md` | series chunks + condition cards |
| Showrunner memory | `active-project/staff/showrunner/memory.md` | season status / split metadata |

## Season metadata (lifted)

- **Time-window:** ~84–88 AC (Taylor age 7–11 in body); ~4-year span.
- **Season drama:** invisible operational baseline → market-square involuntary swarm → four years of cost paid before a stranger in maester's robes arrives at Fairstead with someone else's letter.
- **Season question:** what does Taylor build between arriving unknown and becoming named — and what does she give up, without choosing to, to the people she was supposed to be a daughter and neighbor to, before the institutional clock crosses its first tier?
- **Season-spine pivot (IGNITION):** the swarm event in the market square; first institutional record of Taylor as a named anomaly. Located by content beats at "anchor: ~86 AC, Taylor age ~9".

## Eight content beats (continuous content guidance — not episode boundaries)

1. **Early baseline** (~84 AC, age 7) — household + fauna baseline; child-register cost.
2. **Sept access** (~85 AC, age ~8) — Rowan's first pastoral claim.
3. **Child-witness slip** (~85 AC, age ~8) — Clem Ferris noticing.
4. **Census paperwork pull** (~85–86 AC, age ~8–9) — Pryor at the dock; Rymer files Taylor watching.
5. **IGNITION** (~86 AC, age ~9) — involuntary swarm; season pivot; first incident-log entry.
6. **Witness inquiry [INTERLUDE]** (~86–87 AC, age ~9–10) — narrator: mira-stonefield-jaehaerys.
7. **Parents act in concert [INTERLUDE]** (~87 AC, age ~10) — narrator: oc-craftsman-mother (Elara).
8. **Networked surveillance** (~87–88 AC, age ~10–11) — season-close; lord's traveling maester arrives.

## POV transitions in the aggregate (verified by grep)

| Aggregate line | POV slug |
|---:|---|
| 1 (header preamble) | `taylor-hebert-jaehaerys` |
| 671 | `mira-stonefield-jaehaerys` |
| 765 | `taylor-hebert-jaehaerys` |
| 834 | `oc-craftsman-mother` |
| 945 (file end region) | `taylor-hebert-jaehaerys` |

Five inline POV markers. Two interlude stretches:
- 671–764 = Mira witness-inquiry interlude.
- 834–944 = Elara parents-act-in-concert interlude.

## Phase 4 split snapshot (post-split)

Six episodes. Within target band 80–160, except:
- **s01e03** (251–418) = 168 proto-lines — slightly above the 160 ceiling.
- **s01e06** (700–912) = 213 proto-lines — well above the 160 ceiling. *(This is the season-close + Elara interlude stretch; the split chose to keep the interlude wholly inside e06 rather than break it at the POV boundary.)*

The aggregate ID range 1–912 carries some legal numbering gaps (skipped IDs from deletions) — counted lines = 900. `s01e01` first numbered line is 1; the file body re-numbers from 1 per the schema (verified).

POV honor across cuts:
- e01–e04 narrator: `taylor-hebert-jaehaerys`.
- e05 narrator: `mira-stonefield-jaehaerys` (interlude wholly contained in e05; aggregate-range 564–699 covers the Mira-POV stretch 671–764 partially — **anomaly to flag for Phase B**).
- e06 narrator: `oc-craftsman-mother` (interlude wholly contained in e06; aggregate-range 700–912 covers the Elara-POV stretch 834–944 partially — **anomaly to flag for Phase B**).

**Anomaly:** the per-episode `narrator:` field for e05 and e06 names the *interlude* narrator, not the *dominant* POV across the episode's full aggregate range. The /and-season Step 3 spec says `narrator:` is "the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch." In s01e05 (564–699) the dominant POV is Taylor (564–670 = 107 lines) vs Mira (671–699 = 29 lines); Taylor dominates. In s01e06 (700–912) the dominant POV is Taylor (700–833 = 134 lines) vs Elara (834–944 ∩ 700–912 = 834–912 = 79 lines); Taylor dominates again. **The split appears to have honored the *interlude* characterization from the season plan rather than the *dominant* POV from the aggregate.** This is one to bring to Phase B and likely to Phase G's METADATA-INCONSISTENCY class.

## Group by review axis (units the audience attacks)

Following the packet's four named targets, the units of audience attack are:

### Axis 1 — Season escalation curve (1 unit)

The arc 1 → 912 read as one rise-peak-fall. The dramatic-shape question for the audience: does the season escalate honestly across all 8 content beats? Does the curve land its peak where the season-spine names it (IGNITION ~86 AC, expected to fall mid-aggregate per "back half of the aggregate" rubric)?

**Approximate peak placement:** content beat 5 (IGNITION) maps to aggregate region ~419–563 (s01e04 = the swarm event episode per `e04.goal`). 419–563 falls at 46–62% of the aggregate — front-half of the back-half, borderline-acceptable per the "back half" rule but worth pressing.

### Axis 2 — Per-episode dramatic shape (6 units)

One unit per episode (e01–e06). Each unit gets attacked under the Phase 4 Step 2 verdicts: OPEN-ENGAGES, CLOSE-EARNS-NEXT, SHAPE-COHERENT.

This is the single largest seam-source area — 6 units × 3 personas = up to 18 per-episode seams, plus the 6 close→open joins.

### Axis 3 — Cross-episode continuity (5 units)

One unit per episode boundary (e01→e02, e02→e03, e03→e04, e04→e05, e05→e06). Continuity attack: does state carry coherently across the cut? Cast presence, prop chain, monument callback, off-page time-jump signaling.

### Axis 4 — Episode boundary placement (5 units, same boundaries as Axis 3 but different attack vector)

Same 5 boundary lines, but attacked for *placement quality* rather than continuity. Does the cut land at a natural breath, or interrupt momentum? Could a cut a few lines earlier or later carry a stronger close?

The aggregate IDs at each cut:
- e01/e02 boundary: 149 → 150
- e02/e03 boundary: 250 → 251
- e03/e04 boundary: 418 → 419
- e04/e05 boundary: 563 → 564
- e05/e06 boundary: 699 → 700

### Axis 5 — Season aggregate as a whole (1 unit)

The aggregate read end-to-end as a season-shape verdict. Captures the S2 STRICT structural identification (buildup range, climax range, denouement range) plus the S6 vibe-arc continuity.

### Total seam units

1 (Axis 1) + 6 (Axis 2) + 5 (Axis 3) + 5 (Axis 4) + 1 (Axis 5) = **18 units** for adversarial attack.

Per-persona seams = 18 × 3 = 54 attacks generated, then aggregated to one strongest seam per unit = 18 aggregated seams for Phase E.

## Locked rubric reference

Phase C dispatches read `design/shoot-v2/and-season-tuning-r1/rubric-and-season.md` as the locked V1 rubric. The rubric does NOT move during this run.

## Carry-forward signals from prior season-scope reviews (informational)

The existing nine-pass review under `active-project/staff/auditor/season-s01-pass-*.md` produced two carry-forward notes (per `escalation-s6-vibe-drift-carry-forward.md` and the earlier `season-s01-pass-S6-vibe-*` reports):
- **S6 vibe drift (worm-canon-pedant):** shard-load suppressed across late-stretch beats — carry-forward to impersonation, but a season-scope concern.
- **S6 vibe drift (dark-fantasy-reader):** procedural recurrence (ledger-sequence fatigue).

These are pre-existing audience signal and may resurface as seams in Phase C. Not contraband — the audience can re-press them under V1 rubric, and the defense in Phase E will know the priors.

## Phase A complete

Phase B will read this corpus and produce the baseline gap analysis.
