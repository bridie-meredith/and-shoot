# Stitch Render Log Schema

The render-log is the Stitcher's only cross-phase artifact. Each phase forks at its natural decision granularity; each fork reads its inputs, applies its discipline, files a log entry, returns. No inter-fork memory; the log is the contract.

Schema authority: this file.

Status: **draft (tuning)**.

---

## File path

`active-project/staff/stitcher/render-log-<episode-slug>.md`

One log per episode. Forks append; later phases never rewrite earlier entries.

---

## File structure

```
# render-log — <episode-slug>
profile: <path to active profile>
persona: <active-persona-slug>
narrator: <pov-slug>
voice: {tense: <past|present>, person: <first|third>}
phase-7-mode: <strict|standard|permissive>
generated: <ISO date>

---

## Phase 1 — lens-anchored render
author: stitcher-fork (per anchor)
input: theater/proto-lines/<slug>.md + facets/* + _cite-index.md + profile + persona
output: draft/<slug>.phase-1.draft.md

<fork-entries>

---

## Phase 2 — redundancy cull
...
```

Each phase section has a fixed header (`author`, `input`, `output`) followed by fork entries.

---

## Fork entry format

```
fork-<NNN> @<anchor> -> L<line-id-or-range>  <move-class>  | <reason>
```

Multi-line forks (Phase 1 forks rendering 3+ sentences from one anchor at a peak) span multiple lines:

```
fork-043 @43 -> L25,L26,L27  render-anchor lens=feel-leads (rule-3, persona override)
   lenses-loaded: tens=3, narrator:12, memory:6, sensory:3 (tag=drop), feel:8
   rule-1: skip (no foreknowledge in NI:12)
   rule-2: would-fire (sensory drop) -> SUPERSEDED at rule-6
   rule-3: candidate
   rule-6: FIRES (worm-tight persona override)
   structural-decision: feel-leads, then bone, then narrator
   facets-rendered: feel:8, bone, narrator:12
   facets-deferred-or-dropped: memory:6 -> P2, sensory:3 -> P4 drop-if-covered
```

Per-fork fields (only fields the fork acted on appear):

| Field | Meaning |
|---|---|
| `fork-<NNN>` | Monotonic per phase. Resets to 001 at each phase header. |
| `@<anchor>` | Source bone-id. |
| `-> L<line-id>` or `-> L<N>,<N+1>,...` | Output line(s) assigned at Phase 8. Multi-line for peaks. |
| `<move-class>` | From the taxonomy below. |
| `<reason>` | One line; fixed tags from the reason taxonomy where applicable. |
| `lenses-loaded:` | Phase 1 only — which facets fired at this anchor. |
| `rule-<N>:` | Phase 1 only — lens-decider rule firings (skip / candidate / fires / superseded). |
| `structural-decision:` | Phase 1 only — final lens hierarchy applied. |
| `facets-rendered:` | Phase 1 only — what landed in prose. |
| `facets-deferred-or-dropped:` | Phase 1 only — what was held for later phases. |

Optional second line for refusals or when a move needs explicit citation:

```
  refused: <facet-cite> | reason
  citations: <source-1>, <source-2>, ...    # RESHOW only
  original: <verbatim source text>            # REWORD, RESHOW, CUT-CLAUSE
  replacement: <verbatim output text>         # REWORD, RESHOW
```

---

## Move classes by phase

### Phase 1 — lens-anchored render (per-anchor mode)

| Move class | Meaning |
|---|---|
| `render-anchor` | Anchor rendered with lens hierarchy applied. Always followed by `lens=<leading-lens>` and the decider trace. |
| `render-cite` | Single facet rendered at the anchor (e.g. NI clause without other lenses). |
| `render-bone` | Bone-only render (no lenses firing). |
| `em-dash-fuse` | Bone + single facet fused via em-dash. |
| `skip-blank` | Time-skip blank id observed; paragraph break recorded. |

### Phase 1 — scene-window render (scene-window mode)

When `phase-1.mode: scene-window`, the Phase 1 section uses scene-fork entries instead of per-anchor fork entries. The header records the boundary source and overlap-read config:

```
## Phase 1 — scene-window render
author: stitcher-fork (per scene)
mode: scene-window
boundary-source: <tensometer-derive | scene-map-facet | hybrid>
back-look: <prior-rendered-scene | none>
forward-look: <next-scene-bones-facets | none>
input: theater/proto-lines/<slug>.md + facets/* + _cite-index.md + profile + persona
output: draft/<slug>.phase-1.draft.md

<scene-fork-entries>
```

Per scene-fork:

```
fork-<NNN> scene-<label> bones=@<start>–@<end>  scene-window-render
   bones-consumed: @<start>, ..., @<end>
   back-look: <prior-scene-label | empty>
   forward-look: <next-scene-label | empty>
   variance-moves:
     - <move-description>
   refusals:
     - <refusal-description>
   bone-walk:
     - @<id> -> <rendered-line-id | FUSE-into-L<n> | CUT-BONE | RESHOW>
     - ...
   drift-risk: <none | minor | flag with bone IDs>
```

Move classes for scene-fork-level entries (the scene-fork itself records one of these as its overall verdict):

| Move class | Meaning |
|---|---|
| `scene-window-render` | Standard scene-fork render. Bones consumed, prose emitted, per-bone walk clean. |
| `scene-window-fallback-per-anchor` | Scene-fork dispatch failed (no scene-map, coverage gap, or runtime fault) and the run fell back to per-anchor for this scene. Records the trigger in `reason`. |

Per-bone-walk dispositions (each bone in the scene maps to exactly one):

| Disposition | Meaning |
|---|---|
| `-> L<N>` | Bone rendered as line N (or one of multiple lines for peak bones). |
| `FUSE-into-L<N>` | Bone fused into another bone's rendered sentence (em-dash, comma-appositive, conjunction). |
| `CUT-BONE` | Bone cut under bones-cuttable license. Cite the cut-elsewhere facet or rationale. |
| `RESHOW` | Bone rendered via a reauthored surface citing ≥2 graph sources (rare at Phase 1; usually Phase 7's territory). |

Scene-window-specific fault classes (record as fork-level entries with the fault as move-class):

| Fault | Meaning |
|---|---|
| `FAULT-BONE-FOLDED-INTO-SUMMARY` | Per-bone walk found a bone with no disposition. Wider window summarized the cluster and lost a bone. Triggers re-render of the scene. |
| `FAULT-PHASE-1-NO-SCENE-MAP` | Neither scene-map-facet nor tensometer-derive produced a usable boundary set. Triggers fallback or escalation per `phase-1.scene-window.fallback-on-no-scene-map`. |
| `FAULT-PHASE-1-SCENE-MAP-COVERAGE` | A bone falls outside every scene's range or inside multiple. Coverage gap or overlap in the scene-map. |
| `FAULT-BONE-AUDIT-MISS @<id>` | Bone carries a Q9-coined hyphen-compound in its SVO content. Stitcher cannot REWORD without violating bone-faithfulness; surfaces upstream as a `/and-protolines-v2` rubric pass. |
| `FAULT-NI-VERB-FOLD-STRETCH @<id>` | NI register-verb folded into bone-verb beyond the bone's SVO (defensible under lens-fold license; soft Q-check for auditor). Render kept; recorded in `drift-risk:`. |

### Phase 2 — redundancy cull

| Move class | Meaning |
|---|---|
| `DROP-ECHO` | Facet dropped — closing-phrase echo with another co-anchored facet. |
| `DROP-IMAGE-OVERLAP` | Facet dropped — image-set overlap with co-anchored facet. |
| `KEEP-OVER-ECHO` | Facet retained over a flagged echo (profile priority). |

### Phase 3 — compression

| Move class | Meaning |
|---|---|
| `MERGE-SAME-SUBJECT` | Bones N..M merged into one sentence (same subject, continuous action). |
| `SUBSTITUTE-PRONOUN` | Subject replaced with pronoun after first mention. |
| `COLLAPSE-TENS1-RUN` | Run of tens=1 zero-cite bones collapsed. |
| `MERGE-EXIT-TRIO` | Terminal three-bone sequence collapsed. |
| `MERGE-TIMESKIP` | Blank-id-adjacent bone fused. |
| `NO-MERGE` | Merge candidate declined (records why — usually `pattern-protected` or `facet-anchor-present`). |

### Phase 4 — voice transform

| Move class | Meaning |
|---|---|
| `TENSE-SHIFT` | Bone or facet verb shifted to target tense. |
| `PERSON-SHIFT-POV` | POV-character pronoun shifted to target person. |
| `POV-PRONOUN-RESOLVE` | "the girl's face" / "her hands" resolved against POV at anchor. |
| `PRESERVE-THIRD-PARTY` | Named third-party (e.g. Tya) preserved verbatim. |
| `SENSORY-PROSE-FIT` | Sensory arrow form rendered via prose template. |
| `SENSORY-DROP-COVERED` | Sensory delta dropped because adjacent bone verb covers the modality shift. |
| `BONE-OBJECT-IDIOM-FIT` | Bone object adjusted per profile's `bone-object-policy: idiom-fit`. |
| `CONTRACTION` | "do not" → "didn't" etc. per profile's `contractions: true`. |

### Phase 5 — local flow

| Move class | Meaning |
|---|---|
| `MIGRATE-SENSORY-FORWARD` | Sensory facet moved forward within window. |
| `MIGRATE-NI-BACKWARD` | NI clause moved backward within window. |
| `WITHIN-ANCHOR-REORDER` | Cite order within one anchor changed. |
| `EM-DASH-FUSE` | Bone + same-anchor facet fused via em-dash at Phase 5 (vs Phase 1 direct fusion). |
| `UN-MERGE` | Phase 3 merge undone to rescue a swallowed facet. |
| `REFUSE-MIGRATE` | Migration proposed and refused (records the refusal with reason). |

### Phase 6 — buildup preservation

| Move class | Meaning |
|---|---|
| `RESTORE-PATTERN` | Protected pattern restored after a prior pass flattened it. |
| `PATTERN-OK` | Protected pattern detected and confirmed intact. (Optional.) |
| `NEW-PATTERN-CANDIDATE` | A pattern that looks structural but is not in the profile's protected list. Flagged for human review; no action taken. |
| `PATTERN-ABANDONED` | A formerly-protected pattern whose licensing facet was cut at Phase 7. Bones become eligible for `CUT-BONE` if Phase 7 elects. |

### Phase 7 — editorial reflection

| Move class | Meaning |
|---|---|
| `PASS` | Line passes all nine questions. No change. |
| `CUT` | Whole sentence dropped. Q1=no, or Q2-7 yes-but-bad without partial-cut path. |
| `CUT-CLAUSE` | Clause within sentence dropped at hard-punctuation boundary. Q5 or Q8. |
| `CUT-ASININE` | Whole sentence cut on Q8 with no reshow license. |
| `CUT-HOLLOW` | Whole sentence cut on Q5 (hollow-prose pattern). |
| `CUT-BONE` | Bone dropped under the bones-cuttable license. Requires `bones-cuttable: anchor-cut-only` precondition. |
| `RESHOW` | Clause reauthored through different surface. Requires ≥2 graph sources. |
| `REWORD` | Single word/phrase substituted with common-English equivalent. ≤2 per sentence. |
| `KILL-DARLING` | Q7 fires (line liked-for-its-own-sake more than for what it does). Cuts. |
| `FLAG-ASININE` | Yes-asinine, no reshow license — emit `NEEDS_EDIT` annotation in polish file for editor. |
| `SIMPLIFY-PUNCT` | Q6 fires. Em-dash → comma, semicolon → period, etc. |

The per-sentence Q-answer line records all nine answers:

```
L<N>  Q1=<y|n> Q2=<y|n> Q3=<y|n> Q4=<y|n> Q5=<y|n> Q6=<y|n> Q7=<y|n> Q8=<y|n> Q9=<y|n>  |  <move>
```

No `borderline` value under `cut-aggressiveness: strict`. Borderline = `n` for Q1 (not load-bearing), or `y` for Q3/Q4/Q5/Q7/Q8/Q9 (would cut).

### Phase 8 — finalize

| Move class | Meaning |
|---|---|
| `ASSIGN-LINE-ID` | Stable line-IDs assigned. Records the mapping fork-id → L-id. |
| `WRITE-CLEAN` | `draft/<slug>.md` written. |
| `WRITE-ANNOTATED` | `draft/<slug>.annotated.md` written (when `output: dual`). |
| `WRITE-LOG` | Render-log finalized. |
| `STATS` | Final counts: words, sentences, paragraphs, bones rendered, bones merged, bones dropped, facets rendered, facets dropped, reshow count, reword count. |

---

## Reason taxonomy

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
| `pattern-abandoned` | Pattern's licensing facet cut at Phase 7; bones become cuttable. |
| `not-load-bearing` | Q1 counterfactual fails — audience can follow without this line. |
| `asinine-no-license` | Q8 fires, no graph sources for RESHOW; falls through to CUT-ASININE. |
| `asinine-licensed` | Q8 fires, ≥2 graph sources available; RESHOW emitted. |
| `awkward-rephrasable` | Q9 fires, clean substitution available; REWORD emitted. |
| `awkward-no-rephrase` | Q9 fires, no clean substitution; line cuts or flags. |
| `density-cap-escalate` | 3+ REWORDs needed in one sentence; escalated to RESHOW. |
| `pov-only-referent` | POV is the only matching referent at this anchor; resolution unambiguous. |
| `idiom-fit` | Bone object adjusted per profile's `bone-object-policy: idiom-fit`. |
| `verbatim-preserved` | Bone object kept verbatim per profile's `bone-object-policy: verbatim`. |
| `persona-override` | Persona's lens-bias table or Phase 7 bias fired. |
| `borderline-strict-reject` | Answer was borderline; strict policy rejected (cut). |

---

## Worked example — Scene C, Phase 7 excerpt

```
## Phase 7 — editorial reflection
author: stitcher-fork (per sentence)
phase-7-mode: strict
output: draft/s01e01.phase-7.draft.md

L18  Q1=y Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
L19  Q1=y Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
L20  Q1=n Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  CUT
   reason: not-load-bearing
   cut-text: "Her first note was a song Tya knew. The silk in the rafters caught the vibration."
   note: NI:10 head + RESHOW tail both fail Q1 under strict counterfactual;
         Taylor's silence reads as in-character without the song-Tya-knew context;
         fauna-power was established in Scene B (@26-29) so silk-RESHOW is redundant
L21  Q1=n Q2=n Q3=y Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  CUT-BONE
   reason: pattern-abandoned (P6 NEW-PATTERN-CANDIDATE; protective facet NI:12 cut at L27)
   merged-into: L19 ("She opened her mouth and sang")
   note: bones @40 + @41 (second and third notes) lose buildup-protection
         when NI:12 referencing "third note" cuts; collapse into single "sang"
L22  same as L21  |  CUT-BONE
L24  Q1=y Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
   note: bone "I held her eyes" critical (Taylor's only physical action);
         NI:11 tail was already cut at Q5 (narrator-intrusion) - see fork-042 P7 entry
L25  Q1=y Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
   note: feel:8 critical - without body anchor, song-drop is unmotivated
L26  Q1=y Q2=n Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
L27  Q1=n Q2=y Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  CUT
   reason: not-load-bearing (NI:12 - feel:8 + silence already show recognition-failure)
L28  Q1=y Q2=n Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
L29  Q1=y Q2=n Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS
   note: NI:13 tail was already cut at L29-fork-045 (Q1=n)
L30  Q1=y Q2=n Q3=n Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n  |  PASS

phase-7-summary:
   pass: 8 lines
   cut: 2 lines (L20, L27)
   cut-bone: 2 lines (L21, L22)
   reshow: 0
   reword: 0
   flag-asinine: 0
```

---

## Audit handle

The render-log is the auditor's primary input for stitch review. The auditor checks:

1. Every bone in `proto-lines/<slug>.md` has a corresponding `render-bone`, `MERGE-*`, `CUT-BONE`, or `DROP-*` entry (per-anchor mode), or appears in exactly one scene-fork's `bone-walk:` block with a non-empty disposition (scene-window mode).
2. Every facet drop has a reason that maps to the taxonomy.
3. Every `RESHOW` has ≥2 graph source citations and a `function-preserved` field.
4. Every `REWORD` has `original:` and `replacement:` fields and density ≤2 per sentence.
5. Every `CUT-BONE` cites the cut-elsewhere facet ID that abandoned the protective pattern.
6. No `MIGRATE-*` violates `cross-bone-temporal` or `cross-scene`.
7. Every `RESTORE-PATTERN` matches a `protected-patterns` entry in the active profile.
8. Phase 7 Q-answer lines: under strict-mode, no `borderline` values; every cut has a reason tag.
9. Final stats match Phase 7 + Phase 8 reconciliation.

If those check, the stitch run is auditable-clean regardless of the prose's taste qualities. Taste lives downstream in the editor.

---

## What the log is not

- Not a justification document. One-line reasons; no paragraphs.
- Not a place to log "why this profile" — that lives in the profile file's optional notes section.
- Not a substitute for the prose. Reading the log without the draft tells you what the Stitcher *did*; reading the draft tells you what the Stitcher *produced*.
