# Season S01 — Iteration 3 Summary

```
iteration: 3 of 3 max
verdict: converged
residuals closed: RESIDUAL-1 (ch08 fauna-range)
residuals reframed: RESIDUAL-2 (ch09 fidelity) — addressed at proto-line layer; clarification below
residuals carried to facet/editor pass: RESIDUAL-3 (prop-custody housekeeping)
```

## Iter3 work

### RESIDUAL-1 resolution: ch08 restructure to Harrenhal

Per project policy "restructure to fit constraint, never weaken constraint", chose option (c): relocate Taylor's assessment from sept cottage to Harrenhal interior side chamber. SW dispatch achieved this entirely by recasting 16 existing IDs (no new IDs):

| ID | Old text | New text |
|----|----------|----------|
| 5 | crosses the yard | crosses the outer ward |
| 6 | enters the cottage | enters the side chamber |
| 26 | exits the cottage | exits the side chamber |
| 29 | exits the cottage | exits the side chamber |
| 30 | crosses the yard | reaches the passage |
| 38 | reaches the sept door | reaches the passage end |
| 46 | enters the sept | holds the passage |
| 61 | crosses the sept nave | reaches the great-hall passage |
| 62 | reaches the chancel steps | reaches the great-hall door |
| 89 | exits the sept | exits the great-hall passage |
| 90 | crosses the yard | reaches the postern gate |
| 91 | enters the cottage | exits the postern gate |
| 92 | takes the septon's seat | takes the road |
| 93 | opens the septon's ledger | pins the palms |
| 94 | closes the septon's ledger | withdraws the raven |
| 95 | pins the palms | withdraws the fly |
| 96 | a raven strikes the bell tower beam | a raven lifts from the recorder's beam |

Iter3 verification audit (`season-s01-pass-iter3-ch08-verify.md`) confirmed PASS on all four dimensions: range compliance at every fauna deployment, continuity flow ch07→ch08→ch09 + ch08-interlude, mechanic cleanliness of recasts, structural shape preserved (buildup/climax/denouement intact; great-hall-door position dramatically equivalent to prior chancel position).

Showrunner state files refreshed: maester's location now `loc-harrenhal-interior` (side chamber); Taylor's location-log corrected through the ch07/ch08/ch09 boundary (no sept return between ch07 and ch09 roadside-rise descent).

**RESIDUAL-1 CLOSED.**

### RESIDUAL-2 reframe: ch09 fidelity at 400-500m

Iter3 auditor flagged this as still open. On review of ch09 proto-lines: the dialogue lines all use the schema-licensed `<speaker> speaks to <listener>` form — speech acts are named but content is NOT transcribed. Document interactions are physical-observation only (`unfolds a document`, `lifts the page`, `closes the document`, `taps the document`) — all within fauna visual capability at 400-500m.

The "argument-level knowledge" concern is not present at the proto-line layer. It is a prose-pass / facet inference question: how much semantic content the prose may interpolate from the bare physical/dialogue beats. That is governed by facet authoring rules and editor pass, not proto-line discipline.

At proto-line layer, ch09 honors `cond-fauna-control-rules` (Taylor at 400-500m, well within 600m ceiling) and stays at physical-observation form. **RESIDUAL-2 closed at proto-line layer; carried as a prose-pass advisory note for facet/editor pass.**

### RESIDUAL-3: housekeeping deferred

- ch07 line 93 spatial collision (Plumm taking document while Taylor on outer ward)
- Plumm's three documents (rolled-inspection-page / intercession-record-book / wardship-claim-document) tracked in state notes but unslugged in proto-line files
- ch10 prop-census-file no upstream proto-line establishment
- Taylor's ch07 folio fate unresolved through ch10
- maester's side chamber → great hall → road-east transit not in his movement log (would only matter if ch08-interlude formalizes into his POV)

All deferred to editor wrap pass. Not load-bearing for shoot.

## Cumulative state at end of iter3

**All season-scope passes converged:**

| Pass | Final verdict |
|---|---|
| S1 mechanic constraint | PASS |
| S2 shape | PASS (all 5 revised chapters CLEAN; both prior NO-CLIMAX failures resolved) |
| S3 trim | ACCEPT (all 3 personas) |
| S3.5 ruleset | PASS (rolled into iter2 mechanic) |
| S4 continuity | PASS at proto-line layer (3 housekeeping items deferred to facet/editor) |
| S5 voice | PASS |
| S6 vibe | ACCEPT (all 3 personas, from iter1) |
| S7 facet readiness | PASS |
| S8 plausibility | PASS (all 3 faults closed via Plumm patch + ch06 SW + ch09 SW; ch08 restructure additionally closed the deepest case) |
| S9 comprehensibility | ACCEPT |

## Next steps

- Per-chapter Pass 4 (audience ×3) ×10 chapters = 30 dispatches. (ch08-interlude, ch07-interlude, ch03-interlude separately if treating as full chapters; otherwise rolled in.)
- Per-chapter Pass 5 (continuity, auditor #2 fresh fork) ×10.
- Then proto-line set is ready for facet authoring at all 10 facet types.
- Held / queued: promote v2 commands to live names (`/and-protolines-v2` → `/and-protolines`); implement `.claude/commands/and-season.md` Phase 3 as actual orchestrator dispatch logic (currently still prose spec).
