# Rubric — exposition facet

Authority: `schemas/facet.schema.md` § exposition is the authoritative shape. This rubric is the working discipline the R1 + R2 exposition-author follows.

## What gets glossed (the audience-gap test)

The exposition-author's central test is the **union-of-audience-personas gap question**:

> For this term / object / place / circumstance at this anchor — would the UNION of the active audience personas know what it is on a cold read?

Load all persona cards from `active-project/audience/*/`. For each candidate gloss-anchor, ask the test. If even ONE persona has a real gap (not just "is unfamiliar with the genre" but "would actively misread or lose the scene without the gloss"), the entry is warranted.

**Convergence rule across personas:** if all three personas converge on "yes, gloss needed" with the same reasoning, high-confidence fire. If one persona objects ("this would over-explain to my audience"), the gloss MUST be light enough to not disrupt that persona's reading — i.e. fold via `em-dash-fold` or `inline-appositive`, not `parenthetical-aside` or `preamble-paragraph`.

## Always-gloss

Audience-gap is structural; no persona can be expected to know:
- Westeros institutional roles when neither dark-fantasy nor a Westeros-canon persona reads the project: `reeve`, `septon`, `maester`, `Watch`, `hand-of-the-king`, `master-of-coin`, `castellan`, `kingsguard`, `Citadel`, `lords-man`, `holdfast`.
- Series-specific objects whose presence needs orientation: `the log` (Taylor's clinical-self-erasure instrument), `the count` (insect-count from swarm-control), `the swarm` itself when not yet named in prose.
- Pre-story circumstances that would invite reader-question on first encounter: the resurrection in s01e01 (waking-in-dead-body would invite riot/canonization in any plausible world; the gloss must answer why-it-didn't).
- **Named individuals appearing in prose without prior introduction.** A character mentioned in the polish by definite description (`the carter`, `the dock-runner`, `the lord's-man`, `the maester`) or by name (`Tom`, `Ben`) needs a first-mention gloss when the reader has no prior anchor for who that person is. The cast roster is graph-resident for the audit; the **reader does not have the roster**. Walk every proto-line and ask: does this named individual appear in the polish without having been previously introduced? If yes, author a `first-mention-character` entry. The carter in s01e02 (introduced cold at @52) is the canonical miss the rule prevents. Exclusion: the POV character does not need a first-mention gloss (they're named in the preamble); named individuals who appear ONLY in dialogue (Tom referred to by the elder in his utterance) do not need a gloss unless they also appear in prose.

## Conditionally-gloss

Audience-gap depends on which personas have it:
- Westeros places that aren't in source canon (the Crownlands village, Flea Bottom proper, the Fish Gate margin): gloss IF cape-fic or worm-canon would not know.
- Worm-specific concepts (Khepri, shard, parahuman, swarm-radius): gloss IF dark-fantasy or general-reader would not know.
- Time-period markers (~125 AC, "the year before the Dance"): gloss when dating matters for stakes; skip when ambient.

## Never-gloss

Either handled by other facets or obvious from context:
- Common English nouns (door, latch, salt, bread, bowl).
- Contextually-obvious items (a "bowl on the table" is a meal-bowl; do not gloss bowl-as-meal-ritual unless the bowl-ritual is itself the load-bearing register).
- Things lens facets already establish:
  - NI establishing place-name → exposition does NOT add a place-gloss for the same name.
  - mem establishing a callback-anchor → exposition does NOT explain the callback's prior context.
  - loc-state firing at-establishment → exposition does NOT add time-of-day or location-shift.
- Plot content (what the lord's-man wrote in the record book is the bone's job, not exposition's).

## Form discipline

- **Word caps:**
  - `first-mention-*` glosses: ≤30 words.
  - `episode-open-preamble`: ≤80 words.
  - `episode-open-context`: ≤80 words per paragraph; ≤3 paragraphs total.
  - `scene-open-orient`: ≤15 words.
  - `prior-episode-bridge`: ≤120 words.
- **Plain English only.** No invented compounds. No tokens on the project `anti-jargon` list. No nominalizations-as-jargon.
- **No new plot content.** Every claim in the gloss must map to a `sources:` entry. The fact already exists in the graph; the gloss restates it in compressed orienting form.
- **No author-meta.** No "in this episode...", "later you'll learn...", "as the reader knows..." Voice is in-narrator (`pov-frame`) unless profile sets `voice: omniscient` or `voice: author` (rare; reserved for projects where the narrator-frame is incompatible with the audience-model).
- **Audience-license required.** Every entry's `licensed-by:` field names ≥1 persona-card slug + the specific gap-claim ("cape-fic-doesnt-know-westerosi-feudal-roles", "worm-canon-doesnt-know-flea-bottom-as-slum-district").
- **Embedded-noun gloss-completeness (HARD).** A gloss's `<gloss-text>` cannot contain an un-glossed proper-noun frame that the same persona-set the entry claims to orient would also lack context for. Example: a `first-mention-character` entry for `Wren` that situates her as "the Hook's ward" without `the Hook` itself being on the cross-episode glossed-terms register OR a co-anchor exposition entry — the gloss partially orients then delegates essential context to an unoriented term. **Audit pass:** for each entry's `<gloss-text>`, identify proper-noun frames (capitalized terms, definite-article + place-noun like "the Hook" / "the Watch"); each such frame must resolve via (a) cross-episode glossed-terms register entry, (b) a separate `first-mention-*` exposition entry at the same anchor or any prior anchor in scope, or (c) the project's always-known register (e.g., King's Landing for an ASOIAF project). Unresolved embedded-noun → HARD. (URI-FACETS-CYCLE-1, 2026-05-19 — promoted from audience-gate cycle-1 attack on b01c01 exposition:4 @20: cape-fic-reader requested ADD for "the Hook" embedded inside Wren's first-mention-character gloss; the mechanical first-mention-character-coverage check passed without inspecting gloss-internal proper nouns.)

### Voice (pov-frame default)

When voice is `pov-frame: first-person`, ALL exposition entries render in first-person from the POV character. Phase 2 dogfood emitted 3rd-person preamble despite the default — this is a fault. Re-check every entry's voice before write-out:
- "She had won her world..." → fault.
- "I had won my world..." → correct.

The voice constraint applies to preamble paragraphs and to scene-open-orient bridges. First-mention glosses may render in either neutral-narrative or pov-frame depending on how they fold (parenthetical-aside often reads as narrator-aside which is acceptable in first-person; inline-appositive reads as the POV's own naming which is pov-frame).

## Per-anchor caps

- **≤2 entries per anchor.** Allowed pairs:
  - episode-open-* + scene-open-orient
  - scene-open-orient + first-mention-*
  - episode-open-* + first-mention-*
- No two entries of the same scope on the same anchor.
- Special case: @0 may carry 1 episode-open-preamble + up to 3 episode-open-context entries (per the per-episode cap below), all marked as same-anchor synthetic entries.

## Per-episode caps

- `episode-open-preamble`: 1 per episode (preamble exists or it doesn't).
- `episode-open-context`: ≤3 per episode. Most episodes need ≤2.
- `prior-episode-bridge`: ≤1 per episode (mutually exclusive with `episode-open-preamble`; first episode uses preamble, subsequent episodes use bridge).
- `first-mention-*` (all subtypes combined): ≤12 per episode. If more are needed, the audience-model is wrong or the episode is overloaded.
- `scene-open-orient`: ≤1 per scene MAX (the micro-bridge). Refuses per the conditional fire-rule below.

## Sparsity

1-5% per episode. Higher than feeling/sensory because the audience-gap surface is significant in cross-genre projects (Worm-in-Westeros has gap on both sides); lower than NI because most of the prose carries via lens-facets without needing exposition.

Sparsity computation: `(total exposition entries) / (proto-line count) × 100`. If above 5%, the author is over-budgeting and likely glossing things the lens facets already carry. If below 1%, the author is under-budgeting and the polish will read fragmentary to fresh audiences.

## Scope-specific render-as guidance

| Scope | Renders-as | When |
|---|---|---|
| `episode-open-preamble` | `italic-preamble` | Cold-start (first episode) or new-season-open. Always at @0. |
| `episode-open-context` | `preamble-paragraph` | Additional context paragraphs after the preamble. Always at @0. |
| `prior-episode-bridge` | `italic-preamble` | Subsequent episodes; recap prior terminal state + delta. Always at @0. |
| `first-mention-term` | `inline-appositive` (cheapest) / `parenthetical-aside` (medium) | Institutional terms (reeve, maester, Watch). Land at first-mention anchor. |
| `first-mention-object` | `em-dash-fold` (cheapest) / `post-bone-clause` (medium) | Series-specific objects (the log, the count). Land at first-mention anchor. |
| `first-mention-place` | `inline-appositive` (cheapest) / `em-dash-fold` (medium) | Specific named locations (Flea Bottom, Fish Gate). Land at first-mention anchor. |
| `first-mention-character` | `inline-appositive` (cheapest) / `em-dash-fold` (medium) | Named individuals appearing in prose without prior introduction (the carter, the dock-runner, the lord's-man, Tom). Land at first-mention anchor. POV character excluded (covered in preamble). Dialogue-only mentions excluded (a name in an utterance is the speaker's reference, not a prose introduction). |
| `scene-open-orient` | `scene-bridge` | Micro-bridge at scene-open. ≤15 words. Renders BEFORE first bone of scene. |

**Render-cost ranking** (cheap → expensive, by reader-disruption):
1. `inline-appositive` ("the reeve — the lord's bookkeeper") — minimal interruption.
2. `em-dash-fold` ("the morning bowl — porridge and salt — on the table") — fold mid-sentence.
3. `post-bone-clause` ("He opened the book. Different rank than the reeve...") — full clause after bone.
4. `parenthetical-aside` ("(Our reeve was the lord's hand for...)") — explicit aside.
5. `scene-bridge` (separate sentence at scene-open) — full sentence cost.
6. `preamble-paragraph` (full paragraph) — high cost, reserved for episode-open.

Use the cheapest render-as that the gloss content can fit. If a term needs >30 words, escalate to `parenthetical-aside`; if it needs context that can't fit a parenthetical, the term may actually belong in an `episode-open-context` paragraph or be skipped entirely (the lens facets are over-burdened).

### Dialogue-adjacent fold-in fence (REQUIRED — PROP-0001 / DEC-0010, 2026-05-26)

**Rule.** For any `first-mention-*` entry whose anchor is within ±2 bones of a speech bone (a bone carrying a dialogue-anchor citation or a speech-act SVO), the cheapest two render-as options — `inline-appositive` and `em-dash-fold` — are **PROHIBITED**. The author MUST step up to one of:

- `post-bone-clause` (full clause AFTER the bone — clean paragraph break before the speech bone)
- `parenthetical-aside` (acceptable if the aside completes before the speech bone)
- defer the gloss past the dialogue cluster to the next non-adjacent anchor and re-evaluate at that anchor

**Why.** Em-dash inline fold-ins at dialogue-adjacent anchors pack glosses mid-sentence into the same paragraph as speech acts, denying the rescue / exchange beat the structural whitespace it needs to land. Evidence: `/and-ablate` b01-c01 cold-read ranked `leave-out-exposition` above `full` (rank 1 vs 2) on pacing-through-whitespace, with the diagnosis pointing specifically at em-dash fold-ins crowding the rescue dialogue. The information was wanted; the delivery mechanism was the cost. Report: `staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md`. Proposal: PROP-0001 / DEC-0010.

**How to apply.** At R1 author-time: for each `first-mention-*` candidate, walk ±2 bones from the anchor. If any bone in that window is a speech bone (check bones file for dialogue citations of shape `[<character-slug>:<id>]`, or speech-act SVOs like "X says/asks/calls"), the cheapest-render-as heuristic does NOT pick `inline-appositive` or `em-dash-fold` for that entry. Escalate to `post-bone-clause` or defer. Log the dialogue-adjacency decision in the entry's authoring notes.

**R2 sweep.** R2 graph-aware pass MUST re-walk every existing `first-mention-*` entry against the same ±2-bone speech-adjacency window (now using the cite-index for precise dialogue-anchor resolution). Existing `inline-appositive` / `em-dash-fold` entries adjacent to a speech bone REWORD to `post-bone-clause` or DELETE-and-defer.

**Exclusion.** Entries at @0 (preamble / context paragraphs) and `scene-open-orient` entries are exempt — they are not bone-adjacent renderings.

### Em-dash-fold density cap + terminal-anchor fence (REQUIRED — PROP-0002 / 2026-06-23)

The dialogue-adjacency fence above brakes folds *locally* (one anchor at a time). It does not brake on *aggregate* density — four em-dash folds spread across a chapter created a register-rhythm accumulation a cold reader perceived as pacing compression independent of any single fold's local disruption. Evidence: `/and-ablate` b01-c01 fold-density follow-up; report `staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md`. These two sub-rules add the aggregate brake.

**Per-chapter em-dash-fold density cap.** Across all `first-mention-*` entries in a single chapter, the total count of `em-dash-fold` renders-as MUST NOT exceed **2**. If a third or subsequent fold candidate arises, the author MUST step up to `post-bone-clause` or `parenthetical-aside` for that entry (or, retroactively, for an earlier entry, to stay under cap). Two is the cap because the dialogue-adjacency fence typically eliminates one potential fold per chapter; the residual budget is kept tight to prevent accumulation without over-restricting.

**Terminal-anchor fold fence.** A `first-mention-*` entry whose anchor falls in the final 20% of bones (anchor @N where N ≥ 0.80 × total_bones) is a *terminal-anchor*. Terminal-anchor entries MUST NOT use `em-dash-fold`. Instead:
- `post-bone-clause` (if the gloss fits as a following clause), OR
- `parenthetical-aside` (if the aside completes before the next scene boundary), OR
- defer to `episode-open-context` for the following chapter if the term is not critical to this chapter's close.

**Why.** Terminal-anchor folds compete with the chapter's own reveal-register demand (elder recognition, cost-bearer reveal, protagonist closing interiority). The fold mechanism at that weight class splits reader attention between the gloss and the reveal simultaneously; heavier render-as keeps the gloss structurally subordinate.

**Exclusion.** Entries at @0 are exempt from both sub-rules.

## Scene-open-orient conditional fire-rule (REQUIRED)

A `scene-open-orient` entry fires for a scene boundary if AND ONLY IF:

- **(a)** the proto-line has a time-skip blank immediately preceding the scene-open anchor (i.e. the scene is genuinely discontinuous from the prior scene, not a paragraph break within a continuous time-frame), AND
- **(b)** `location-state` does NOT fire at the scene-open anchor (loc-state at-establishment carries the time/place; if it fires, the scene-orient is wallpaper), AND
- **(c)** no `interest-narrator` entry in the first 2 anchors of the new scene carries time-of-day or place-shift content.

The author MUST audit each scene-boundary against these three conditions and refuse to fire when (b) or (c) holds. Lens facets carry → exposition stays out.

The audit-trail per scene-boundary is logged in a `# Fire-audit` comment block at the top of the scene-orient section of the facet file (see the s01e01 reference facet for the format).

## Cross-episode register

`active-project/staff/exposition-author/glossed-terms.md` tracks every term/object/place glossed in the project. Entries:

```
- reeve | glossed-in: s01e01 | gloss-id: 5 | first-mention-anchor: @63
- maester | glossed-in: s01e01 | gloss-id: 8 | first-mention-anchor: @114
- the-Watch | glossed-in: s01e01 | gloss-id: 9 | first-mention-anchor: @139
- log | glossed-in: s01e01 | gloss-id: 4 | first-mention-anchor: @22
- flea-bottom | glossed-in: s01e01 | gloss-id: 7 | first-mention-anchor: @98
```

A term in the register cannot be re-glossed in future episodes. If a future episode's exposition-author considers `reeve` for glossing, the register entry blocks it. (Exception: if the term reappears in a markedly different context — e.g. "the King's reeve" vs "the village reeve" — a new entry with a `qualifier:` field is permitted.)

The R1 author writes a `# Cross-episode register write-back` comment block at the end of the facet file. The Phase 4 cite-index rebuild will read this and update `glossed-terms.md` at canonical merge time.

## R1 vs R2 differences

**R1 (blind):** the exposition-author reads only its rubric + non-facet upstreams (audience persona cards + series-plan + world-build cards + condition cards + character cards) + base proto-lines + the upstream `tensometer.md` (correlative gate for which anchors are peak/transitional). Does NOT read other R1 facet outputs. The gap-identification is audience-pure.

**R2 (graph-aware):** the exposition-author re-runs with all 9 R1 facet files + the cite-index in hand. Decisions per existing entry:
- KEEP (gap still real after lens-facets reviewed; no other facet covers it; sources still resolve).
- DELETE (lens facet covers — typical: NI established the term in body, exposition was redundant; or mem carries the callback exposition was about to gloss; or loc-state covered the scene-orient).
- REWORD (the gap is real but the surface chose a heavy render-as where a lighter one would do; or anti-jargon list grew in R1 cull and a term needs re-rendering).

Adds at R2: rare. The audience-gap is largely identifiable at R1; new candidates at R2 are typically when an R1 lens-facet author chose NOT to cover a register the exposition can pick up cleanly. Add-cap 3.

R2 also resolves any `provisional-anchor` notes from R1 (e.g. R1 says "@first-mention-of-record-book"; R2 binds to the actual proto-line ID by walking the cite-index).

## Audit classes (Phase 5 hooks)

- **CONSTRAINT — source-traceability.** Every claim in `<gloss-text>` must trace to a source in `<sources>`. The auditor's CONSTRAINT scan extracts each substantive claim and checks at least one source resolves to actual graph content matching the claim. Unresolvable claim → HARD.
- **CONSTRAINT — license-completeness.** Every entry's `<licensed-by>` field must name ≥1 persona-card slug + a specific gap-claim. Missing/malformed → SIGNAL.
- **FREQUENCY-BAND — per-episode caps.** Episode-open ≤4 entries; first-mention ≤12; scene-open-orient ≤scene count; sparsity 1-5%. Out-of-band → SIGNAL.
- **AP-SCAN — anti-jargon.** Scan every `<gloss-text>` against the project `anti-jargon` list (case-insensitive substring). Hit → HARD (the gloss is inventing or echoing jargon).
- **AP-SCAN — hollow-prose.** Scan against the project `hollow-prose-patterns` list. Hit → SIGNAL (gloss surface is hollow; needs REWORD before stitch).
- **AP-SCAN — asinine-pattern.** Scan against `asinine-patterns` list. Hit → SIGNAL.
- **AP-SCAN — new-plot-content.** For each `<gloss-text>`, check that no substantive claim is absent from `<sources>` lookups. Hit (claim not in sources) → HARD (exposition is inventing plot).
- **AP-SCAN — author-meta.** Scan for "in this episode", "the reader", "we'll see", "as you'll learn", "stay tuned" — any TV-narrator framing. Hit → HARD when voice is pov-frame; SIGNAL when voice is author/omniscient.
- **AP-SCAN — re-gloss-check.** Cross-reference each `<key>` against the cross-episode register. Hit (re-glossing) → HARD.
- **AP-SCAN — voice-fault.** When profile sets `pov-frame`, scan for 3rd-person pronouns in `episode-open-*` and `scene-open-orient` entries. Hit → SIGNAL (Phase 2 dogfood emitted 3rd-person; this fault must surface at audit).
- **AP-SCAN — scene-orient-fire-rule.** For each `scene-open-orient` entry, verify (a) time-skip-blank + (b) loc-state silent at anchor + (c) NI silent on time/place in first 2 anchors. Any violation → HARD (entry fires when lens should carry).
- **AP-SCAN — dialogue-adjacent-fold-in (PROP-0001 / DEC-0010).** For each `first-mention-*` entry, walk ±2 bones from the anchor against the bones file + dialogue cite-index. If any bone in that window is a speech bone (carries a `[<character-slug>:<id>]` citation or a speech-act SVO: says / asks / calls / replies / answers / shouts / whispers / murmurs / mutters / declares / instructs) AND the entry's `renders-as` is `inline-appositive` or `em-dash-fold` → HARD (cheap fold prohibited at dialogue-adjacent anchor). Exclusion: entries at @0 and `scene-open-orient` are exempt.
- **AP-SCAN — em-dash-fold density (PROP-0002).** Count `em-dash-fold` renders-as across all `first-mention-*` entries in the chapter. Total > 2 → SIGNAL (HARD on second chapter-level occurrence in the project). Exclusion: entries at @0 are exempt.
- **AP-SCAN — terminal-anchor fold (PROP-0002).** Compute the terminal-anchor band per chapter from the bones file's total-bone count (final 20%: anchor @N where N ≥ 0.80 × total_bones). For each `first-mention-*` entry whose anchor is in that band AND whose `renders-as` is `em-dash-fold` → SIGNAL (HARD on second chapter-level occurrence in the project). Exclusion: entries at @0 are exempt. (On a 27-bone chapter the band is @22–@27; on a 40-bone chapter, @32–@40.)

## Audience-gate (Phase 5b) hooks

Exposition is the only facet authored AS audience-modeled-by-construction. The audience-gate adversarial reviewers therefore have a unique relationship to it:

- **Each audience persona reviewer ATTACKS the gloss from their persona's reading-experience.** Cape-fic-reader reviewing the s01e01 maester entry asks: "did this gloss successfully orient me to maester-as-institution, or did it leave me still confused?" If unsatisfied: REVISE. If clearly off-target (gloss is wrong, or wrong scope): REJECT.
- **All three persona reviewers must ACCEPT (3-of-3) for exposition to pass the gate.** Single dissent blocks (same rule as other facets).
- **Reviewers may also propose ADDS:** "I'm a cape-fic-reader; I needed the gloss for `kingsguard` at @<N> and there isn't one." This is the audience-side surfacing a gap the R1 author missed.
- **The author has the final call on the ADD's gloss content** but cannot refuse an audience-flagged ADD without escalating to the auditor's TASTE-FLAG → AP-SCAN promotion path.

This is the cleanest audience-gate test the pipeline has — exposition is the facet most directly designed against audience-modeling, so the audience-gate is the canonical reviewer.

## Cull pass (R1 author-time)

After R1 authoring, the exposition-author runs a single-pass cull on its own facet file:
- DROP entries where the union-gap test is borderline (any reviewer would say "I'd want less" rather than "I'd want more").
- DROP entries that duplicate content already established in series-plan-resident background (the audience presumably read the series-pitch; exposition is about per-episode reader-state, not series-state).
- DROP entries glossing terms that appear only once and aren't structurally load-bearing (single-mention non-load-bearing terms can survive without gloss; the reader infers from context).

Cull pass is single-attempt. If the cull doesn't converge in one pass, the authoring stage failed; re-author from scratch.

## What this rubric does not cover

- The schema definition (that's `schemas/facet.schema.md` § exposition).
- The agent card (that's `staff/exposition-author/card.md`).
- The cross-episode register file format (defined inline in this rubric's § Cross-episode register).
- The stitcher-side fold-in mechanics (that's the stitcher card's Phase 1 and the and-stitch command's Phase 0.6).
