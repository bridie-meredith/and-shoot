---
report: and-facets-rejected-removal
episode: b01-c01
date: 2026-05-20
driver: user directive post-cap-burn
audit-source: active-project/staff/auditor/facets-audience-gate-r3.md
items-removed: 2 (sensory:3 @17, mem:1 @9)
files-modified: 6
---

# Fixer report — audience-gate rejected facet removal

Two facet entries failed the cycle-3 audience-gate (cap-burned). User directed removal per
minimum-change discipline. No card routing. No downstream consequence chasing beyond
citation surface cleanup.

---

## Item 1 — sensory:3 @17

**Rejection basis:** sensory-old-state-reader specialist returned a NEW HARD at cycle-3:
`street-quiet-of-mid-afternoon` old-state is unanchored to any prior loc-state or sensory
baseline. The entry was added at cycle-3 (F-015a) to satisfy modality floor; the add
introduced a new finding that would require a fourth cycle (past cap).

### File 1: `active-project/theater/facets/sensory.md`

Before:
```
1 @3 light: corner-room-dim -> overcast-yard-diffuse
# defense-anchor: ...
# [defense block, 4 lines]
# 2 @16 thermal: ...
# [sensory:2 gap-doc comment, 4 lines]

3 @17 sound: street-quiet-of-mid-afternoon -> bootfall-on-cobbles-from-the-Hook-bend
# audience-gate-cycle-3-note
# [note block describing why sensory:3 was added]
```

After:
```
1 @3 light: corner-room-dim -> overcast-yard-diffuse
# defense-anchor: ...
# [defense block, 4 lines]
# 2 @16 thermal: ...
# [sensory:2 gap-doc comment, 4 lines]

# 3 @17 sound: street-quiet-of-mid-afternoon -> bootfall-on-cobbles-from-the-Hook-bend
# sensory:3 DELETED (user directive 2026-05-20 — audience-gate cycle-3 rejection): sensory-old-state-reader
# specialist returned NEW HARD: old-state "street-quiet-of-mid-afternoon" is unanchored to any prior
# loc-state or sensory baseline. Entry was added at cycle-3 (F-015a) to satisfy modality floor; the
# fix introduced a new unanchored-old-state finding. Per user direction, removed rather than chased
# to a fourth cycle. ID gap 3 intentional (follows gap at ID 2 from F-009 cycle-2 deletion). Modality
# floor advisory reopened: sensory.md is back to 1 modality (light only, sensory:1 @3). Accepted
# tradeoff per user direction.
```

Change: live entry line + cycle-3-note annotation block deleted; replaced with F-009-style
gap-documentation comment. ID gap 3 preserved.

### File 2: `active-project/theater/proto-lines/b01-c01.md`

Before (line 26):
```
17 the boots strike the cobbles [sensory:3]
```

After (line 26):
```
17 the boots strike the cobbles
```

Change: `[sensory:3]` token stripped. Line is bare; @17 returns to bare-protolines roster.
Cite-index `## Bare protolines` section lists `@14, @17` — consistent with this state.

### File 3: `active-project/theater/facets/_inflight-r2/proto-lines-sensory.md`

Before (lines 12-13):
```
# R2 sensory judge — citation cascade
# sensory:1 @3 KEEP. sensory:2 @16 DELETED (cycle-2 F-009). sensory:3 @17 ADDED (cycle-3 F-015a).
```

After (lines 12-15):
```
# R2 sensory judge — citation cascade
# sensory:1 @3 KEEP. sensory:2 @16 DELETED (cycle-2 F-009). sensory:3 @17 ADDED (cycle-3 F-015a).
# sensory:3 @17 DELETED (user directive 2026-05-20): audience-gate cycle-3 sensory-old-state-reader
# returned NEW HARD — old-state "street-quiet-of-mid-afternoon" unanchored to any prior loc-state or
# sensory baseline. User directed removal; modality-floor advisory accepted as tradeoff.
```

And at line 32 (was line 29 before header expansion):
```
# Before: 17 the boots strike the cobbles [sensory:3]
# After:  17 the boots strike the cobbles
```

Change: deletion clause appended to cite-cascade header; `[sensory:3]` stripped from @17 line.

---

## Item 2 — mem:1 @9

**Rejection basis:** all three audience reviewers across cycles 1 and 2 rejected the
`# defense: feel-as-spine` annotation. Rubric mandates NI co-citation on every memory-flag
entry; NI is silent at @9; no carve-out exists for feel-as-spine substitution. Adding NI @9
would breach the band ceiling (7/27 = 25.9% > 25% cap). Rubric authority ruling was out of
scope. Final verdict: FAIL (cap-burn). Cycle-3 fixer deliberately skipped; user directed
removal post-cap-burn.

### File 1: `active-project/theater/facets/memory.md`

Before (lines 6-16):
```
1 @9 the feet hold and the architecture stays the shape she will not build -> monument-override-architecture-prohibition
# defense: feel-as-spine
# [multi-line defense block through "# Co-citations: [feel:1, vibes:12]."]
2 @18 the patrol's line through the bend is older than the patrol -> (westeros: flea-bottom-hook-as-coercive-geometry-monument)
```

After:
```
# 1 @9 the feet hold and the architecture stays the shape she will not build -> monument-override-architecture-prohibition
# mem:1 DELETED (user directive 2026-05-20 — audience-gate cycles 1+2 uniform rejection): all three
# audience reviewers across cycles 1 and 2 rejected the feel-as-spine defense. Rubric mandates NI
# co-citation on every memory-flag entry; NI is silent at @9; no carve-out exists for feel-as-spine
# substitution. Rubric authority ruling was out of scope; adding NI @9 would breach band ceiling
# (7/27 = 25.9% > 25% cap). User directed removal per cap-burn final verdict. ID gap 1 intentional;
# mem:2 ID is preserved at 2. File now has 1 live entry (mem:2 @18). The Khepri-residue
# substance-hinge at @9 is no longer carried by a memory-monument fire — accepted tradeoff per user
# direction. Co-citations [feel:1, vibes:12] remain live on those facet entries; feel:1 and vibes:12
# are not modified by this deletion.
2 @18 the patrol's line through the bend is older than the patrol -> (westeros: flea-bottom-hook-as-coercive-geometry-monument)
```

Change: live entry line + entire `# defense: feel-as-spine` block (formerly lines 7-27)
deleted; replaced with F-009-style gap-documentation comment. ID gap 1 preserved. mem:2
@18 untouched.

### File 2: `active-project/theater/proto-lines/b01-c01.md`

Before (line 19):
```
9 taylor-hebert-kl-122ac holds the feet [feel:1] [mem:1] [vibes:12]
```

After (line 19):
```
9 taylor-hebert-kl-122ac holds the feet [feel:1] [vibes:12]
```

Change: `[mem:1]` token stripped. `[feel:1]` and `[vibes:12]` untouched.

### File 3: `active-project/theater/facets/_inflight-r2/proto-lines-mem.md`

Before (line 3):
```
# R2 mutations: 0 KEEP-all (mem:1 @9, mem:2 @18 both confirmed against locked graph)
```

After (lines 3-6):
```
# R2 mutations: 0 KEEP-all (mem:1 @9, mem:2 @18 both confirmed against locked graph).
# POST-R2: mem:1 @9 DELETED (user directive 2026-05-20): audience-gate cycles 1+2 uniformly rejected
# the feel-as-spine defense (rubric requires NI co-citation; NI silent at @9; no carve-out). Removed
# per cap-burn final verdict; ID gap 1 preserved; mem:2 ID unchanged.
```

And at line 17 (was line 14 before header expansion):
```
# Before: 9 taylor-hebert-kl-122ac holds the feet [feel:1] [mem:1] [vibes:12]
# After:  9 taylor-hebert-kl-122ac holds the feet [feel:1] [vibes:12]
```

Change: deletion clause appended to R2-mutations header; `[mem:1]` stripped from @9 line.

### File 4: `active-project/theater/facets/_cite-index.md`

Four targeted edits:

**(a) Header count — line 66:**

Before: `### mem (2 entries)`
After: `### mem (1 entry)`

**(b) mem:1 entry deleted — formerly line 67:**

Before: `  mem:1 @9 back=Y co=[feel:1, vibes:12]`
After: _(line deleted)_

**(c) feel:1 co-citations — line 70 (now line 69 after deletion):**

Before: `  feel:1 @9 back=Y co=[mem:1, vibes:12]`
After: `  feel:1 @9 back=Y co=[vibes:12]`

**(d) vibes:12 co-citations — line 89 (now line 88 after deletion):**

Before: `  vibes:12 @9 back=Y co=[feel:1, mem:1] lic-out=[proto:9]`
After: `  vibes:12 @9 back=Y co=[feel:1] lic-out=[proto:9]`

Totals header (line 5) not modified — annotated as approximate; other stale citation gaps
(sensory:2, loc-state:3) already exist; regeneration deferred to Phase 6.

---

## Downstream consequences (accepted tradeoffs per user direction)

**(a) sensory.md — modality floor advisory reopened.**
sensory.md is back to 1 modality: light only (sensory:1 @3). The rubric's 2-modality floor
(sound + one other) is unmet. This was the original cycle-1 callout from sensory-modality-coverage;
cycle-3 tried and failed to resolve it within the unanchored-old-state constraint. Advisory
is open; no action is taken. The stitcher will render without a sound-entry in the sensory
facet. Downstream: if /and-stitch consults sensory.md for modality coverage it will find
light-only. If the stitcher enforces modality balance in rendering the "boots strike cobbles"
moment at @17, it will have no sensory-facet license for that beat.

**(b) memory.md — Khepri-residue substance-hinge at @9 uncarried.**
memory.md is now single-register: mem:2 @18 (Westerosi-only, coercive-geometry monument at
the Watch passage). The Khepri-residue interior-feeling-of-rule-catching at @9 — the chapter's
declared substance-hinge — is no longer carried by any memory-flag entry. feel:1 @9 and
vibes:12 @9 remain live and continue to cover the emotional and ambient registers at @9; the
memory-monument arc (architecture-she-will-not-build → monument-override-architecture-prohibition)
is absent. The SHAPE-FAIL risk named in the cap-burn report is accepted as a known tradeoff.
Downstream: if the stitcher uses memory.md to source monument-texture in the @9 passage, it
will find no memory fire at that anchor. The substance at @9 rests entirely on feel:1 + vibes:12.

Both consequences were explicitly named in the cap-burn rationale
(active-project/staff/auditor/facets-audience-gate-r3.md § Cap-burn rationale) and are
accepted per user direction.
