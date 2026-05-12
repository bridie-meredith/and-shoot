# Stitch Render Log Schema

The render-log is the Stitcher's only cross-phase artifact. Each phase reads the prior phase's draft and the log to date; it does not retain reasoning state from earlier phases. Every decision a phase makes is filed here with a fixed move-class and a one-line reason.

Schema authority: this file.

Status: **draft (tuning)**.

---

## File path

`active-project/staff/stitcher/render-log-<episode-slug>.md`

One log per episode. Phases append; no phase rewrites earlier entries.

---

## File structure

```
# render-log — <episode-slug>
profile: <path to active profile>
narrator: <pov-slug>
generated: <ISO date>

---

## Phase 1 — baseline concat
author: stitcher-fork
input: theater/proto-lines/<slug>.md + all facets/*.md
output: polish/<slug>.draft.md (phase-1 snapshot)

<move-entries>

---

## Phase 2 — redundancy cull
...
```

Each phase section has a fixed header (`author`, `input`, `output`) followed by move-entries.

---

## Move entry format

```
<id> <move-class> @<anchor> [-> @<target-anchor>] | <one-line reason>
```

- `<id>` — monotonic per phase. Resets to 1 at each phase header.
- `<move-class>` — fixed taxonomy (below).
- `@<anchor>` — source bone-id the move applies to.
- `-> @<target-anchor>` — destination anchor, when the move migrates a facet.
- `<reason>` — one line, drawn from a fixed reason taxonomy when applicable.

Optional second line for refusals or when the move needs a context phrase:

```
  refused: <facet-cite> | reason
```

---

## Move classes by phase

### Phase 1 — baseline concat

| Move class | Meaning |
|---|---|
| `RENDER-BONE` | Bone rendered as sentence. |
| `RENDER-CITE` | Facet cite appended to current bone's output. |
| `SKIP-BLANK` | Time-skip blank id observed; paragraph break recorded. |

Phase 1 is deterministic; the log is mostly a manifest.

### Phase 2 — redundancy cull

| Move class | Meaning |
|---|---|
| `DROP-ECHO` | Facet dropped — closing-phrase echo with another co-anchored facet. |
| `DROP-IMAGE-OVERLAP` | Facet dropped — image-set overlap with co-anchored facet. |
| `KEEP-OVER-ECHO` | Facet retained over a flagged echo (profile priority). |
| `NO-ACTION` | Anchor has multi-cite but no redundancy detected. (Optional; omit for brevity.) |

### Phase 3 — compression

| Move class | Meaning |
|---|---|
| `MERGE-SAME-SUBJECT` | Bones N..M merged into one sentence (same subject, continuous action). |
| `SUBSTITUTE-PRONOUN` | Subject replaced with pronoun (records the substitution point only, not every occurrence). |
| `COLLAPSE-TENS1-RUN` | Run of tens=1 zero-cite bones collapsed. |
| `MERGE-EXIT-TRIO` | Terminal three-bone sequence collapsed. |
| `MERGE-TIMESKIP` | Blank-id-adjacent bone fused. |

Compression moves note the bone range affected (`@N..@M`) rather than a single anchor.

### Phase 4 — voice transform

| Move class | Meaning |
|---|---|
| `TENSE-SHIFT` | Bone or facet verb shifted to target tense. |
| `PERSON-SHIFT-POV` | POV-character pronoun shifted to target person. |
| `POV-PRONOUN-RESOLVE` | "the girl's face" / "her hands" resolved against POV at anchor. |
| `PRESERVE-THIRD-PARTY` | Named third-party (e.g. Tya) preserved verbatim. |
| `SENSORY-PROSE-FIT` | Sensory arrow form rendered via prose template. |
| `SENSORY-DROP-COVERED` | Sensory delta dropped because adjacent bone verb covers the modality shift. |

### Phase 5 — local flow

| Move class | Meaning |
|---|---|
| `MIGRATE-SENSORY-FORWARD` | Sensory facet moved forward within window. |
| `MIGRATE-NI-BACKWARD` | NI clause moved backward within window. |
| `WITHIN-ANCHOR-REORDER` | Cite order within one anchor changed. |
| `EM-DASH-FUSE` | Bone + same-anchor facet fused via em-dash. |
| `UN-MERGE` | Phase 3 merge undone to rescue a swallowed facet. |
| `REFUSE-MIGRATE` | Migration proposed and refused (records the refusal). |

### Phase 6 — buildup preservation

| Move class | Meaning |
|---|---|
| `RESTORE-PATTERN` | Protected pattern restored after a prior pass flattened it. |
| `PATTERN-OK` | Protected pattern detected and confirmed intact. (Optional.) |
| `NEW-PATTERN-CANDIDATE` | A pattern that looks structural but is not in the profile's protected list. Flagged for human review; no action taken. |

### Phase 7 — finalize

| Move class | Meaning |
|---|---|
| `WRITE` | Final prose written to `polish/<slug>.md`. |
| `STATS` | Word count, sentence count, bone coverage, facet render rate. |

---

## Reason taxonomy

A small fixed set keeps the log machine-readable. Free-text reasons are allowed but should map to one of these when possible.

| Tag | Meaning |
|---|---|
| `echo` | Closing-phrase echo with another facet. |
| `overlap` | Image-set overlap with another facet. |
| `cumulative-delta` | Sensory delta that completes at a later anchor; license to defer. |
| `temporal-lock` | Clause contains a temporal-lock word; cannot migrate. |
| `cross-bone-temporal` | Move would reorder bones; forbidden. |
| `cross-scene` | Move would cross a scene boundary; forbidden. |
| `cap-reached` | Per-anchor render cap reached; lower-priority cite dropped. |
| `pattern-protected` | Move would break a protected pattern; refused. |
| `redundant-with` | Phase 3 merged because facet content of source bone is covered by target bone. |
| `pov-only-referent` | POV is the only matching referent at this anchor; resolution unambiguous. |
| `idiom-fit` | Bone object adjusted per profile's `bone-object-policy: idiom-fit`. |
| `verbatim-preserved` | Bone object kept verbatim per profile's `bone-object-policy: verbatim`. |

---

## Worked example (Scene C, Phase 5 excerpt)

```
## Phase 5 — local flow
author: stitcher-fork
input: polish/s01e01.phase-4.draft.md
output: polish/s01e01.phase-5.draft.md

1 MIGRATE-SENSORY-FORWARD @39 -> @41 | cumulative-delta
2 EM-DASH-FUSE @39 | within-anchor-order: em-dash-fusion (bone + narrator:10)
3 REFUSE-MIGRATE @39 | temporal-lock (clause contains "first")
   refused: narrator:10 -> @41 (proposed; declined)
4 UN-MERGE @44..@46 | phase-3 MERGE-EXIT-TRIO swallowed narrator:13 @45
5 PATTERN-OK three-note-buildup @39..@41 | confirmed intact pre-phase-6
```

Five moves; each one self-describing; an auditor reading only this block can reconstruct what changed and why.

---

## Audit handle

The render-log is the auditor's primary input for stitch review. The auditor checks:
1. Every bone in `proto-lines/<slug>.md` has a corresponding `RENDER-BONE`, `MERGE-*`, or `DROP-*` entry across Phase 1–3.
2. Every facet drop has a reason that maps to the taxonomy.
3. No `MIGRATE-*` violates `cross-bone-temporal` or `cross-scene`.
4. Every `RESTORE-PATTERN` matches a `protected-patterns` entry in the active profile.
5. Final word count, sentence count, and bone coverage match Phase 7 `STATS`.

If those check, the stitch run is auditable-clean regardless of the prose's taste qualities. Taste lives downstream in the editor.

---

## What the log is not

- Not a justification document. One-line reasons only; no paragraphs.
- Not a place to log "why this profile" — that lives in the profile file's optional notes section.
- Not a substitute for the prose. Reading the log without the draft tells you what the Stitcher *did*; reading the draft tells you what the Stitcher *produced*.
