# Dialogue as a Facet — V2 integration

Operational design for treating dialogue as the eleventh facet in `/and-facets`, alongside exposition. Supersedes the v1 round-trip-as-separate-pipeline shape.

V1 source: `design/shoot-v2/round-trip-method.md` (round-trip tuning on s01e01–s01e06 dialogue corpus).
V1 corpus: `design/shoot-v2/dialogue-corpus.md`.
Locked rubric: `staff/dialogue-writer/rubric-dialogue.md`.

Status: design (rubric pending lock; `/and-facets` wire-up pending).

---

## The reframe

Dialogue is a facet of a story. Same as sensory, feeling, memory, exposition. Each captures one dimension of how a bone is rendered:

- **sensory** — what the world feels like at this anchor.
- **feeling** — what the body shows at this anchor.
- **memory** — what the POV is reaching for at this anchor.
- **exposition** — what the reader needs oriented at this anchor.
- **dialogue** — what the speaker says at this anchor.

The eight v1 writer patterns and the V2/V3 reviewer protocol are not a *separate* tuning pipeline — they are the **discipline** the dialogue facet author and reviewer carry. The facet pipeline (R1 fanout → R2 fanin → Phase 5 audit → Phase 5b audience-gate) is the **machinery**. v1 already produced the tuned discipline; v2 plugs it into the machinery without re-tuning.

This mirrors the exposition retrofit: exposition was not pre-tuned in a round-trip; its discipline (union-of-audience-personas gap test) was *constructed* and dropped into the existing facet shape. Dialogue is the same move, with the difference that the discipline already exists (v1 tuned it) and the rubric authority lifts directly from `round-trip-method.md`.

---

## What v1 settled (becomes rubric authority)

The eight writer patterns and the two reviewer stages from `round-trip-method.md` are the authority. They become `staff/dialogue-writer/rubric-dialogue.md` in §-section form so any R1/R2/audit/audience-gate dispatch can cite them.

**Eight writer patterns:** per-behavior-card forks; card-stack load order; blind to originals; intent-as-state (not text); multi-draft + chosen-mark + rejection notes; affirmative card-features citation; anti-patterns explicit; calibration anchor.

**Reviewer stages:** V2 strict affirmative-demonstration rubric (ACCEPT only if affirmatively demonstrates ≥1 card signature AND does not violate); V3 adversarial seam-finding (per line, persona-distinct counter-arguments aggregated as the seam).

**Convergence:** writer defends-or-revises per seam; defended accept stays; revision means seam was load-bearing.

The full evidence trail for these patterns lives in `round-trip-method.md` and the audience-review files (`audience-review-originals.md`, `audience-review-originals-v2.md`, `audience-review-round2.md`, `audience-challenges-round3.md`, `audience-adjudication-final.md`). The rubric distills; the evidence persists.

---

## Plug-in shape — dialogue as the eleventh facet

### Phase 1 — R1 author (blind, parallel with other R1 authors)

**Author:** `dialogue-writer` fork class. Per-behavior-card fanout — one fork per distinct behavior card present in the episode's cast. A single fork authors all speakers sharing that card (preserves v1's cross-contamination prevention at generation time).

**Reads:**
- Behavior card stack (margit-composed: leaf → `inherits:` parent → universal overlay → `references:` adjacent cards).
- Speaker persona + ltm + stm + state for every speaker the fork covers.
- Base proto-lines (the speaking-beat anchors are the proto-lines where this card's speakers appear as subject of a `speaks` SVO).
- Upstream `tensometer.md` (correlative — peak anchors warrant register-state pressure).
- `rubric-dialogue.md` (v1-distilled discipline).

**Forbidden:** other R1 facet outputs (R1 stays blind), show files / source prose, other behavior cards not in this fork's domain.

**Writes:** per-character dialogue files under `active-project/theater/dialogue/<character-slug>.md` per `schemas/dialogue.schema.md` (existing schema preserved). The fork's multi-draft + chosen-mark + cited-signatures sidecar lands under `active-project/staff/dialogue-writer/<character-slug>.drafts.md`. Annotated proto-lines copy under `_inflight/proto-lines-dialogue-<card>.md` with `[<character-slug>:<id>]` citations on the speaking anchors.

**Per-file cull:** delete-only pass — same one-pass discipline as other facets.

### Phase 2 — fanin (existing machinery)

`build_cite_index.py` merges the dialogue authors' `_inflight/` copies into canonical proto-lines along with all other R1 facet citations. Slice consolidation: per-card dialogue authors produce per-character files; no merge needed (the files are already per-character per the schema). Stale-cite check covers `<character-slug>:<id>` citations.

### Phase 3 — R2 judge (graph-aware, parallel with other R2 judges)

**Judge:** `dialogue-writer` fork class, judge mode. Per-character fanout (one judge per dialogue file) — R2 is the graph-aware re-anchoring pass.

**Reads:**
- The dialogue file under judgment + its drafts sidecar.
- All nine other R1 facet files + cite-index.
- Behavior card stack (re-loaded).
- Speaker persona + ltm + stm + state.
- `rubric-dialogue.md`.

**Per-entry verdict:** KEEP / DELETE-<reason> / REWRITE (delete + new ID per schema).

**KEEP criteria:**
- Card signature affirmatively demonstrated (v1 V2 rubric).
- Anchor's locked facet decoration *licenses* the line — if the chosen draft claimed `feeling-<speaker>:<id>` as register license, that entry must still exist post-R1-merge and the somatic tell must support the claimed mask state.
- No hard-fence violation (Earth-Bet proper-noun scan across utterance text).
- Behavior monument rules respected (speaker does not name monuments they cannot have; does weight monuments they would carry).

**DELETE criteria:**
- Card signature missing (inoffensive ≠ on-card).
- Forbidden vocabulary present (v1 anti-patterns).
- Facet-license citation does not resolve in the locked graph.
- Hard-fence proper-noun hit.
- Other facets render the same content (DEDUP — e.g. interior the line says aloud that NI already carries).

**REWRITE criteria (delete + new ID):**
- Seam from V3-shape adversarial pass exists *internally* (the judge does a mini-V3 pass per entry as part of its KEEP/DELETE deliberation) AND the seam is closable with a different draft.

**Add-cap:** ≤3 per character per run. Adds are exceptional — R1 dialogue covers the speaking beats; R2 adds only if a beat is genuinely silent that the card + graph license a line for.

**Writes:** mutated dialogue file + `_inflight-r2/proto-lines-dialogue-<character>.md` + decision-shard `staff/dialogue-writer/r2-decision-shard-<character>.md`.

### Phase 4 — fanin (existing machinery)

`build_cite_index.py` rerun. Decision shards fold into `.r2-decisions.md` under `## dialogue` heading. Arbiter glue (T1/T4) applies same as other R2 judges.

### Phase 5 — audit (mechanical, existing machinery + dialogue-specific classes)

Existing eleven audit classes carry forward. Dialogue-specific additions land in CONSTRAINT, AP-SCAN, and STRUCTURAL:

- **STRUCTURAL** — every dialogue entry's `@<proto-line-id>` resolves; every cited `<character-slug>:<id>` in proto-lines resolves to an existing entry; entry-ID monotonicity per-character.
- **CONSTRAINT** — behavior-card-compliance (does the entry respect the card's hard fences and monument rules); citation-completeness (every chosen-mark entry has both card-signature citation AND facet-license citation in the drafts sidecar); Earth-Bet hard-fence proper-noun scan across utterance text.
- **AP-SCAN** — v1 anti-patterns (em-dash + semicolon chassis on non-Taylor speakers; modern HR-speak in Westeros register; deposition cadence; nominalizations substituting for plain English when the card's register is colloquial).
- **FREQUENCY-BAND** — sparsity unconstrained (dialogue is content, not flag; sparsity is downstream of what the proto-lines call for). But per-anchor cap ≤3 utterances; multi-utterance exchanges at one anchor should split across anchors when natural.

### Phase 5b — audience-gate (adversarial, existing machinery)

Dialogue runs through Phase 5b like every other facet. **Reviewer set:**
- If specialist dialogue personas exist (`staff/audience/<slug>/card.md` with `target-facet: dialogue` frontmatter), they fire as the reviewer set.
- Otherwise the active-project audience (3 personas) fires in graph-aware adversarial mode under the v1-distilled V2 + V3 protocol.

**Reviewer protocol per persona per character:**
- **V2 pass:** every entry receives ACCEPT (affirmatively demonstrates ≥1 card signature, no violation) / REVISE / FAIL verdict.
- **V3 pass:** every line including accepts gets the strongest hostile counter-argument from this persona's lens. Persona-distinct: atmosphere / board-move / voice-precision (or facet-equivalents). Facet evidence is fair attack surface — "the chosen draft cites `feeling-taylor:7` as license, but that entry is a held-breath tell that doesn't carry register-slip in stitch."

**Aggregation:** strict 3-of-3 per `/and-facets` audience-gate convention (URI-AUDIENCE-AGGREGATION-RULE). Single dissent fails the character.

**Convergence:** failed characters route callouts to fixer; fixer dispatches `dialogue-writer` in defense-or-revise mode (v1 R3 protocol) — defended accepts stay, revisions get multi-draft + chosen-mark treatment. Cycle cap: 3.

### Phase 6 — persist (existing machinery)

Dialogue files at `theater/dialogue/<character-slug>.md` are canonical. Drafts sidecars + decision shards persist under `staff/dialogue-writer/` for forensic review.

---

## What changes elsewhere

### `schemas/facet.schema.md`

No change needed — dialogue's schema is `schemas/dialogue.schema.md`, independent. The facet pipeline tolerates this the way it already tolerates exposition's distinct entry shape. Cite-index treats `<character-slug>:<id>` citations the same as `<facet-prefix>:<id>` citations; the build_cite_index.py prefix table just adds the per-cast slugs.

### `.claude/commands/and-facets.md`

Adds dialogue as R1 author #11, R2 judge #6. Phase 5 audit picks up dialogue-specific classes. Phase 5b audience-gate enumerates dialogue alongside the other ten facets. Phase 6 persist + master summary mention dialogue.

### `cards/dialects/` (pending rename to `cards/behaviors/`)

No change to card content. The behavior-card composition stack is the load mechanism for the R1 + R2 dispatches.

### Stitcher contract

Unchanged. Dialogue entries are rendered verbatim under their `@<proto-line-id>` anchor per `schemas/dialogue.schema.md` § "Stitch interface." Edit budget remains "and" only. The new R2 + Phase 5 + Phase 5b gates upstream of the stitcher mean the stitcher receives a graph-validated dialogue layer instead of a raw one.

---

## What stays from the v1 round-trip work

All of it, as rubric authority. The two-pass shape (R1 author + R2 judge with audience-gate V2 + V3 attached) maps cleanly onto v1's "writer fork + adversarial audience" + "writer defends-or-revises" loop. The difference is just where it lives — folded into the facet pipeline's existing R1/R2/Phase-5/Phase-5b shape instead of as a separate command or phase.

The audience-review files (`audience-review-originals.md` through `audience-adjudication-final.md`) are preserved as the evidence trail behind the locked rubric. They are not part of the operational pipeline — they are the *citation* the rubric can point at when a v2 reviewer asks "why is this the rubric."

---

## Open questions

1. **R1 fanout granularity — per behavior card or per character?** v1's anti-cross-contamination argument was at the card level. But the existing facet pipeline fans out feeling and state-updates *per character* in the R1 parallel block, and the per-character impersonator fork already loads the per-character card stack. Either: (a) per-behavior-card forks, each writing multiple per-character files (mirrors v1 exactly) or (b) per-character forks, each loading its own card stack (mirrors existing pipeline shape). Lean: (a) for the s01 dogfood — keep v1 protocol intact for the A/B — then evaluate whether (b) is safe at scale.
2. **Per-character vs per-card R2 judge.** R2 graph-aware judging probably wants per-character — the graph context (this character's feeling slice, this character's state slice) is per-character. Per-card judge would re-load multiple characters' graph slices in one fork. Lean: per-character R2 even if R1 is per-card.
3. **Calibration anchor selection at scale.** v1 hand-picked Plumm/NC-4. For automated runs, the rubric needs a programmatic rule. Probably: highest-tens anchor with all four lens facets fired AND a known-strong v1 line on the same card.
4. **Audience specialist personas for dialogue.** Worth authoring `staff/audience/voice-precision-pedant/card.md`, `staff/audience/register-distinctness-reader/card.md`, `staff/audience/board-move-pedant/card.md` as specialist Phase-5b reviewers — they encode the V3 seam-finding lenses v1 used. Alternative: keep fallback-to-active-audience as default and only author specialists if Phase 5b under-flags.
5. **Per-anchor utterance cap.** ≤3 is a guess. Audit data from the first dogfood should calibrate.

---

## Migration

- **First dogfood:** /and-facets re-run on s01e01 with dialogue as facet #11. A/B against v1 round-trip output. Audience pass blind to which is which.
- **Metric:** v3 seam-defensibility rate (% of accepts that survive seam-finding without revision). v1 baseline ≈ open (the round-trip stalled at challenge phase). v2 target: ≥75%.
- **Anti-regression:** must not regress v1's affirmative-demonstration rate on round-2 lines (94% on regenerated). If facet citations end up *substituting* for card-signature citations rather than supplementing, the rubric's CONSTRAINT § citation-completeness should catch it.
