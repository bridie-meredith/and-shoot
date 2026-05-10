# Plan A — A4 Phase 2 migration spec (staging)

**Status:** drafted, awaiting A3 (s02 first-fire) PASS verdict before applying. A3 is the live-fire that validates the existing tens bone-gate; A4 extends the same pattern to three more facets and risks compounding any pattern flaws if landed before A3 confirms the pattern works.

**Companion:** `plan-a-a4-rubric-portability-audit.md` — verdict: all three migrated facets need per-episode-post-split routing (mirror of tens).

**Discovery:** `/and-shoot.md` does **not** exist as an active slash command (only archived under `./archive/commands/and-shoot.md`). The plan's reference to "extending /and-shoot Phase 0 rename contract" reduces to a documentation update in `schemas/facet.schema.md`'s dual-provenance notes. No active command to edit.

---

## Edits

### Edit 1 — `.claude/commands/and-season.md` Phase 4

**Add Step 1.6 (sensory authoring) immediately after Step 1.5 (tens):**

```
### Step 1.6 — Sensory authoring per proposed episode (URI-026 Phase 2, 2026-05-10) — BONE-GATE

Mirror of Step 1.5 for sensory-flags. Per the rubric portability audit
(design/shoot-v2/plan-a-a4-rubric-portability-audit.md): sensory's
file-level modality-coverage health check (≥2 modalities per file) is
calibrated per-episode and cannot be guaranteed by aggregate authoring.

**Position:** runs after Step 1.5 (tens authoring) and before Step 2 (audience review).

**Dispatch:** **studio** in fork-mode, one fork per proposed episode, in parallel with the Step 1.5 tens forks (different agent type — studio not dramatist — so no fork collision).

**Fork-discipline brief (mirror of /and-facets-r1.md:138 Layer 2b sensory):**
- **Read inputs:** the proposed-episode bone stretch (proto-line IDs `<from>`–`<to>` from the split proposal); `design/shoot-v2/rubric-sensory.md` (locked V1); `schemas/facet.schema.md` § sensory; the per-proposed-episode tens file from Step 1.5 (correlative observation only — NOT gating); the locked location-state for the episode (mandatory baseline) — **see Step 1.8 below; Step 1.6 reads its output**.
- **Forbid loading:** behavior cards, vibes, audience personas, source prose. Studio authors mechanically against the rubric.
- **Output path:** `active-project/theater/facets/sensory-<season-slug>e<NN>.md` (slug-suffixed; `<NN>` is proposed episode index).
- **Output format:** per-rubric (modality-inflection / disambiguation / magnitude / audience-side perceptibility). Same shape as `/and-facets-r1` Layer 2b sensory; only the path differs.

**Sequencing note:** Step 1.6 depends on Step 1.8 (loc-state) for old-state baseline. Order within the bone-gate: 1.5 (tens) ‖ 1.8 (loc-state) → 1.6 (sensory) ‖ 1.7 (state-updates env). Tens and loc-state are upstream-independent and run first; sensory and state-updates env both consume loc-state.

**Dispatch budget:** 1 per proposed episode (3–6 per season). Parallel within the layer.

**Failure handling:** studio refusal (rubric self-flag) ⇒ `SENSORY-AUTHORING-REFUSED-<episode>` ⇒ studio re-dispatch with refusal context. Cap: 2 retries per episode.
```

**Add Step 1.7 (state-updates env authoring):**

```
### Step 1.7 — State-updates env authoring per proposed episode (URI-026 Phase 2, 2026-05-10) — BONE-GATE

Mirror of Step 1.5 for the **environment subset** of state-updates (`studio.*` and `prop:*.*` entries). Actor-state (`actor:<slug>.*`) entries are **not** migrated; `/and-facets-r1` Layer 3b retains them.

Per the rubric portability audit: state-updates env requires per-episode-post-split scope (sparsity 8–18% per-episode; tens-coupled density alignment; target-diversity ≥3 classes per episode).

**Position:** runs after Step 1.8 (loc-state) and Step 1.5 (tens), in parallel with Step 1.6 (sensory).

**Dispatch:** **studio** in fork-mode, one fork per proposed episode.

**Fork-discipline brief (mirror of /and-facets-r1.md:156 Layer 3a):**
- **Read inputs:** proposed-episode bones; `design/shoot-v2/rubric-state-updates.md` (V2 locked); `schemas/facet.schema.md` § state updates; per-proposed-episode tens from Step 1.5 (3-beats expected to co-cite); per-proposed-episode loc-state from Step 1.8 (frame context); all loc and prop cards in active warehouse.
- **Scope restriction:** environment + location + prop state changes only. `actor:<slug>.*` entries are explicitly forbidden — Layer 3b retains actor-state authoring.
- **Forbid loading:** persona cards, vibes, audience personas.
- **Output path:** `active-project/theater/facets/state-updates-env-<season-slug>e<NN>.md` (slug-suffixed; env-suffixed to distinguish from the merged file `/and-facets-r1` Layer 3b will continue to write).
- **Output format:** per-rubric. Only studio + prop entries.

**Dispatch budget:** 1 per proposed episode. Parallel.

**Failure handling:** `STATE-UPDATES-ENV-AUTHORING-REFUSED-<episode>` ⇒ studio re-dispatch with context. Cap: 2 retries.
```

**Add Step 1.8 (loc-state authoring) immediately before Step 1.6 to honor sequencing:**

```
### Step 1.8 — Location-state authoring per proposed episode (URI-026 Phase 2, 2026-05-10) — BONE-GATE

Mirror of Step 1.5 for location-state. Per the rubric portability audit: loc-state's per-entry rules are mostly portable, but per-episode-post-split routing is the safe-and-consistent choice (post-split episode-opening anchors require per-episode scope; consistency with tens, sensory, state-updates env).

**Position:** runs in parallel with Step 1.5 (tens). Both are upstream of Step 1.6 (sensory) and Step 1.7 (state-updates env).

**Dispatch:** **studio** in fork-mode, one fork per proposed episode, in parallel with Step 1.5 tens forks (different agent: studio vs dramatist — no fork collision).

**Fork-discipline brief (mirror of /and-facets-r1.md:103 Layer 1b):**
- **Read inputs:** proposed-episode bones; `design/shoot-v2/rubric-location-state.md` (V2 locked); `schemas/facet.schema.md` § location-state; all loc cards named in the per-episode `locations:` derivation (slug-grep over the proposed-episode stretch).
- **Forbid loading:** other facet rubrics, vibes (Round 1 blind precedent).
- **Output path:** `active-project/theater/facets/location-state-<season-slug>e<NN>.md` (slug-suffixed).
- **Output format:** per-rubric (necessity / interestingness / frugality).

**Dispatch budget:** 1 per proposed episode. Parallel.

**Failure handling:** `LOCSTATE-AUTHORING-REFUSED-<episode>` ⇒ studio re-dispatch. Cap: 2 retries.
```

**Step ordering summary** (replaces the linear Step 1.5 → Step 2 path):

```
Step 1.5 (tens, dramatist)        ┐
Step 1.8 (loc-state, studio)      ┘ — parallel; upstream-independent
                                  ↓
Step 1.6 (sensory, studio)        ┐
Step 1.7 (state-updates env, std) ┘ — parallel; both consume loc-state
                                  ↓
Step 2 (audience review + extended mechanic auditor)
```

### Edit 2 — `.claude/commands/and-season.md` Phase 4 Step 2 mechanic-auditor extension

**Extend the narrow-scope auditor invocation** (currently tens-only) **to consume all four bone-gate facets:**

In the §"Mechanic-arithmetic dispatch (narrow-scope auditor)" block (~line 355 of and-season.md), update the rubric class subset to include sensory / state-updates env / loc-state classes from `.claude/commands/and-facets-audit.md`. The auditor reads the per-episode tens + sensory + state-updates env + loc-state files and runs the per-rubric class subset.

Specifically:
- **FREQUENCY-BAND** extended: tens (60-75/20-30/5-10), sensory (3–6% sparsity), state-updates env (8–18% sparsity), loc-state (sparse-by-design — flag if no fires per scene-with-irreversible-event).
- **CURVE-SHAPE** extended: tens (rise→peak→release), sensory (modality-coverage ≥2), state-updates env (density alignment with tens 2-3× ratio non-1 vs 1-zones; target-diversity ≥3 classes), loc-state (no explicit curve — per-entry only).
- **AP-SCAN** extended: tens (AP1–AP5 per rubric), sensory (charged-word redundancy + modality-monoculture + sub-threshold + cross-modal blur), state-updates env (registration-as-state + posture-as-state + invented-field), loc-state (set-dressing sweep + mood-painting + persistence-as-state + plan-bullet residue).

**Open question (carried from rubric audit):** the auditor class library at `.claude/commands/and-facets-audit.md` may not have explicit class definitions for all of these. Pre-A4 verification: read the audit command and confirm coverage. If gaps, A4 includes a class-library extension as part of the spec edit.

### Edit 3 — Combined per-episode verdict (Phase 4 Step 2)

Extend the existing `SPLIT-ACCEPT` / `SPLIT-REVISE-bones-{line-range}` / `SPLIT-REVISE-cut-{reason}` verdict to consume mechanic verdicts from all four bone-gate files. Existing tens-only conditions are expanded to: `MECHANIC-CLEAN` requires clean across tens + sensory + state-updates env + loc-state per-episode files. Any `MECHANIC-FAIL-{class}` finding in any of the four routes per the existing REGEN-{REPLACE,ADD,BOTH} discipline.

The bone-gate per-window iteration cap (2) applies to the combined gate, not per-facet — i.e., the regen window is the same window regardless of which facet's rubric flagged it.

### Edit 4 — `.claude/commands/and-season.md` Phase 5 print summary

Extend the Phase 4 print block to enumerate per-facet authoring + mechanic verdicts for sensory / state-updates env / loc-state, mirroring the existing `Step 1.5 tens-authoring:` line.

### Edit 5 — `.claude/commands/and-facets-r1.md` deletions

**Delete entirely:**

- Layer 1a (tens authoring) — already deferred for deletion per URI-026; this is the URI-026 Phase 2 closure.
- Layer 1b (location-state authoring).
- Layer 2b (sensory authoring).
- Layer 3a (state-updates env authoring).

**Retain:**

- Layer 2a (narrator-interest)
- Layer 3b (state-updates actor side — per-character impersonators)
- Layer 3c (memory)
- Layer 4 (feeling)
- Layer 5 (metaphor)
- Layer 6 (vibes-updates)

**Update Layer numbering or keep gaps?** Recommendation: **keep the gaps** for git-history clarity (`Layer 1a — DELETED (URI-026 Phase 2)` stub line; same for 1b, 2b, 3a). The numbering preserves cross-references in design docs and tuning artifacts.

**Update Phase 6 persistence check:** confirm only the **retained** facet files exist; remove the deleted facets from the file count check. Specifically the line:

```
Confirm all nine facet files exist under active-project/theater/facets/:
  - tensometer.md, location-state.md, interest-narrator.md, sensory.md, state-updates.md, memory.md, feeling.md, metaphor.md, vibes.md.
```

becomes:

```
Confirm the retained facet files exist under active-project/theater/facets/:
  - interest-narrator.md, state-updates-actor.md, memory.md, feeling.md, metaphor.md, vibes.md.

The bone-gate facets (tensometer.md, sensory.md, state-updates-env.md, location-state.md) are
authored by /and-season Phase 4 Steps 1.5–1.8 and renamed by /and-shoot Phase 0 (when /and-shoot
exists) from their slug-suffixed bone-gate paths. /and-facets-r1 does not author them.
```

### Edit 6 — `schemas/facet.schema.md` dual-provenance extension

The existing tens dual-provenance note (lines 48–58) becomes a template for sensory / state-updates env / loc-state. **Add equivalent §"Dual provenance" notes to:**

- `### sensory flags` (after the existing modality enumeration, before the deprecated-loudness note).
- `### state updates` (split into env + actor subsections, with dual-provenance only on env).
- `### location-state` (after the existing description).

Each new dual-provenance note follows the tens template:

1. Primary (bone-gate): `/and-season` Phase 4 Step 1.x — per-proposed-episode studio fork. Output path slug-suffixed.
2. Legacy: `/and-facets-r1` Layer N — DELETED at URI-026 Phase 2 (2026-05-10). Path retained as documentation; no active authoring path.

**Note difference from tens:** for sensory / state-updates env / loc-state, the legacy path is **deleted**, not "retained operationally." Tens kept its legacy path during a transition window; the Phase 2 migrations skip the transition (URI-026 already validated the bone-gate pattern with tens at Phase 1).

### Edit 7 — `design/shoot-v2/upstream-tuning-queue.md`

A4's spec edits land URI-026 Phase 2. Mark in the queue:

```
URI-026 — Phase 1 LANDED 2026-05-10; Phase 2 LANDED <A4-date> (Plan A A4)
- Phase 1: tens migration to /and-season Phase 4 Step 1.5 + bone-gate F7
- Phase 2: sensory + state-updates env + loc-state migrations + /and-facets-r1 layer deletions
```

(A5 closes URI-026 entirely after A1 + A3 + A4 all land.)

---

## Validation re-fire (per plan A4)

After Edits 1–7 land, re-fire `/and-season s02` with all four bone-gates active. Per plan: ~6 added dispatches per facet × 3 facets = ~18 added dispatches. Total Phase 4 bone-gate dispatch budget worst-case ~48 (~12 authoring forks + ~24 mechanic auditor invocations + ~12 inner regen iterations); **breaches the orchestrator-critic R1 hard cap of 60 per `/and-season` run**.

**Mitigation paths (pick one before A4 lands):**

1. Raise R1 to 80 in the orchestrator-critic card (preferred — bone-gate is structurally heavier than the pre-bone-gate baseline; cap was calibrated before any bone-gate existed).
2. Tighten per-facet inner-iteration cap from 2 to 1 (drops ~8 dispatches; risks more residual HARDs).
3. Serialize the bone-gate authoring (1.5 → 1.8 → 1.6 → 1.7) instead of paralleling within layer (drops nothing dispatch-wise, but reduces concurrency burden).

**Recommendation:** option 1 (raise R1 to 80). The 60 cap was calibrated empirically on pre-bone-gate runs; the bone-gate pattern is now load-bearing infrastructure and the cap should reflect its presence.

---

## Verification (post-apply)

1. `grep -n "Step 1\.[5-8]" .claude/commands/and-season.md` → 4 hits (1.5 tens, 1.6 sensory, 1.7 state-env, 1.8 loc-state).
2. `grep -n "Layer 1a — DELETED\|Layer 1b — DELETED\|Layer 2b — DELETED\|Layer 3a — DELETED" .claude/commands/and-facets-r1.md` → 4 hits.
3. `grep -c "Dual provenance" schemas/facet.schema.md` → 4 (tens + sensory + state-updates env + loc-state).
4. `grep "URI-026.*Phase 2.*LANDED" design/shoot-v2/upstream-tuning-queue.md` → 1 hit.
5. `/and-season s02` re-fire produces per-episode `tensometer-*.md`, `sensory-*.md`, `state-updates-env-*.md`, `location-state-*.md` files. Phase 6 verdict prints expanded mechanic-arithmetic verdict line. R1 dispatch count remains within recalibrated cap.
