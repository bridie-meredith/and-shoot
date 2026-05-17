# Stitch Sample — s01e01 Scene C (mother-sings)

source: active-project/theater/s01e01-archive/
bones: 36–46 (11 contiguous proto-lines; +1 time-skip blank at @35 marking the noon gap)
scene-label: Scene C (per interest-narrator.md sparsity gradient — "mother-sings 4/9 ≈ 44% peak-cluster")
peaks: tens=3 at @43 (7 cites — pile-up #2 in cite-index, after @98)
prior-scene-tail: @34 taylor closes the log (yard-map sequence complete)
next-scene-head: @48 oc-tanner-father assigns taylor-hebert-flea-bottom the yard-edge task (Scene D)

This sample is the raw materials for one scene-pass stitch experiment. Every cited facet entry
is quoted verbatim at the bone it anchors. Vibes are listed (render-forbidden by schema; bias
signal only). State entries are listed (continuity enforcement; not for prose).

---

## The bones (verbatim from proto-lines/s01e01.md)

```
36 oc-tanner-mother enters the room                              [state:26] [tens:34]
37 oc-tanner-mother sets the afternoon bowl                      [tens:35]
38 oc-tanner-mother opens the mouth                              [tens:36]
39 oc-tanner-mother sings the first note                         [narrator:10] [sensory:2] [tens:37]
40 oc-tanner-mother sings the second note                        [tens:38]
41 oc-tanner-mother sings the third note                         [tens:39]
42 taylor-hebert-flea-bottom holds the eyes                      [narrator:11] [tens:40]
43 oc-tanner-mother drops the song                               [feel:8] [mem:6] [narrator:12] [sensory:3] [tens:41] [vibes:8] [vibes:9]
44 oc-tanner-mother sets the bowl                                [tens:42]
45 oc-tanner-mother faces the wall                               [narrator:13] [tens:43]
46 oc-tanner-mother exits the room                               [state:27] [tens:44]
```

Tens curve across the scene: 1 1 1 1 1 1 2 **3** 1 1 1 — flat approach, single peak at @43, immediate flat exit.
POV: taylor-hebert-flea-bottom. Mother is non-POV.

---

## Per-anchor cards

### @36  `oc-tanner-mother enters the room`
- tens:34 = 1
- state:26  actor:oc-tanner-mother.position: elsewhere-in-cottage -> in-the-room   *(continuity only)*

### @37  `oc-tanner-mother sets the afternoon bowl`
- tens:35 = 1

### @38  `oc-tanner-mother opens the mouth`
- tens:36 = 1

### @39  `oc-tanner-mother sings the first note`
- tens:37 = 1
- narrator:10  the mother's first note is a song Tya knew; the spiders in the rafters do not know it
- sensory:2    sound: yard-work-ambient -> mother-singing  `# tag: up`

### @40  `oc-tanner-mother sings the second note`
- tens:38 = 1

### @41  `oc-tanner-mother sings the third note`
- tens:39 = 1

### @42  `taylor-hebert-flea-bottom holds the eyes`
- tens:40 = 2
- narrator:11  the eye-hold is the only honest thing she has to offer; honest by what it withholds

### @43  `oc-tanner-mother drops the song`  *— tens=3 peak; pile-up of 7 cites*
- tens:41 = 3
- narrator:12  the silence after the third note is the shape Tya should have filled
- feel:8       oc-tanner-mother: the hands still on the apron-front and the gaze holds the girl's face  |  expressed: partial
- mem:6        the song stops on the third note and what the third note was reaching for is the silence the body should have filled  ->  (earth-bet: helpless-protector / failed-recognition pattern — dying-parent-recognition-fail variant)
- sensory:3    sound: mother-singing -> silence  `# tag: drop`
- vibes:8      actor:oc-tanner-mother ++ grief-without-object: [song-as-test, probe-enacted-not-verbal, cessation-as-the-answer-received]   *(render-forbidden; bias)*
- vibes:9      actor:oc-tanner-mother ++ asking-around-the-edge: [song-as-adjacent-question-enacted, enacted-not-asked, the-non-response-as-open-question]   *(render-forbidden; bias)*

### @44  `oc-tanner-mother sets the bowl`
- tens:42 = 1

### @45  `oc-tanner-mother faces the wall`
- tens:43 = 1
- narrator:13  the wall is what the mother turns to when she has run out of daughter to look at

### @46  `oc-tanner-mother exits the room`
- tens:44 = 1
- state:27  actor:oc-tanner-mother.position: in-the-room -> elsewhere-in-cottage   *(continuity only)*

---

## Methods to try

Each method renders the same 11 bones. Compare output length, fidelity to facet content,
and the read-aloud feel.

### Method A — Pure concatenator (lowest effort, highest fidelity)
Render every bone as a sentence. For each cited facet at that bone, append the facet content
verbatim, in this order: bone → sensory → NI → feel → mem → metaphor. State and vibes never
render. No reordering, no compression, no added prose beyond punctuation and case fixes.

### Method B — Peak-anchored compression
Render the tens=3 peak (@43) as a full multi-facet paragraph. Render the tens=2 beat (@42)
as a single sentence with its co-cite. Collapse the tens=1 run of three song-notes (@39–41)
into one sentence. Keep entry/exit (@36, @46) as one-clause framers. The three "bowl" beats
(@37, @44) compress into a single repeated-bowl gesture or get cut.

### Method C — NI-as-spine
Use only the four NI clauses (@39, @42, @43, @45) as the prose spine. Reference bones inline
where the NI clause needs the physical anchor; let the rest of the bones disappear into the
NI's voice. Sensory @39 and @43 fold into the NI clauses they sit beside. Feel and mem at @43
attach to NI:12 as appositives. Most compact form; risks losing the mother's act-of-singing as
a discrete event.

### Method D — Bones-only baseline (control)
Render the 11 bones verbatim as sentences, no facet content at all. This is the floor — what
the prose looks like if no facets were ever authored. Use it to measure how much each other
method adds.

---

## Stitcher rules (from schemas/facet.schema.md "Stitch interface", line 235)

> The stitcher reads proto-lines in citation order. For each citation, it fetches the
> corresponding facet entry and uses it as guidance for *selection and arrangement*, not for
> prose generation. Per the stitcher edit budget (only "and"), facet content is either quoted
> or used as a selection signal — it is not paraphrased into the manuscript.

Operational interpretation for this experiment:
- **Quotable verbatim**: bone SVO, NI clause, feel clause, mem clause, sensory delta (the
  arrow form may be rephrased to "X gave way to Y" or similar, but the modality and direction
  are fixed).
- **Selection-only**: tens scalar (drives paragraph weight, not word content), vibes (bias),
  state (continuity).
- **Added prose budget**: punctuation, capitalization, and the connectives "and" / "then"
  per the schema. Method B and C may need slightly more (one or two transition words per
  scene); flag any addition beyond a single connective so we can compare violation rates.

---

## Quick sanity check

If a method's output for @43 does NOT contain all five renderable cites (bone, sensory:3, NI:12,
feel:8, mem:6), that's either a deliberate compression choice (Method B/C may legitimately drop
mem:6's parenthetical) or a fidelity bug. Mark which.

If a method's output for the song-note run (@39–41) is three separate sentences, that's
Method A. If it's one sentence, that's Method B/C. If the notes don't appear at all, that's
Method C with full compression — verify the mother is still recognizable as singing.
