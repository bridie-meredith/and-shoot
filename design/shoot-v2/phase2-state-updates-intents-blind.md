# Phase 2 — Writer-Blind Intent Sheet (state-updates)

This is the writer-blind copy of the Phase 2 intents. The verdict-prediction column is stripped. The writer-fork sees only the beat, author class, and state-aspect description.

## Source authority for the writer-fork

- Rubric V2 locked: `design/shoot-v2/rubric-state-updates.md`
- Locked tensometer: `active-project/theater/facets/tensometer.md` (cross-facet contract)
- Locked narrator-interest: `active-project/theater/facets/interest-narrator.md` (cross-facet contract; POV-restriction)
- Proto-lines: `active-project/theater/proto-lines/s01e01.md`
- Schema: `schemas/facet.schema.md` §state-updates

The writer-fork is **blind to the original Phase 1 naive baseline** (`design/shoot-v2/phase1-state-updates-baseline-naive.md`) and **blind to the Phase 1 audit** (`active-project/staff/auditor/phase1-state-updates-baseline-review.md`). Do not read those files. Author from intent + cards + locked facet files only.

---

## Studio batch (author: studio)

You write `studio.*` and `prop:<slug>.*` entries only. You do NOT write `actor:*.*` entries (those belong to per-character forks). For each intent: decide FIRE or NONE; if FIRE, draft 2 candidate forms and mark CHOSEN; cite the rubric axes the chosen form demonstrates; cite the cross-facet contract slot it serves.

- **S1.** @64 — the stylus moves on the line under taylor's name (parallel-margin marks beside Taylor's entry)
- **S2.** @38 — taylor puts the letter into the air in front of the officer
- **S3a.** @40 — the officer unfolds the letter (holder/state context)
- **S3b.** @45 — taylor's palm closes on the letter
- **S4.** @41 — the seal breaks at the crease under his thumb
- **S5.** @57 — edric steps back through the door (cottage-door state, conditional on proto-line evidence)
- **S6.** @43 — the officer holds the letter out to taylor (decide FIRE or NONE; consider what the letter holder is at @43 vs @44 vs @45)

You may add up to 4 additional FIRE entries on beats elsewhere in s01e01 you can defend on rubric grounds (e.g., environment shifts, condition activations, prop physical-state changes). For any additional fires, include the same draft+rationale discipline.

## Taylor fork batch (author: dialogue-writer fork for taylor-hebert-westeros, state-update output mode)

You write `actor:taylor-hebert-westeros.*` entries only. You do NOT write studio, prop, or other actors' entries. Every fire on POV actor-state must have a narrator-interest co-citation on the same `@<beat>`; check `active-project/theater/facets/interest-narrator.md` before firing.

- **T1.** @39 — taylor sets her feet on the dirt where his next pace commits (decide FIRE or NONE)
- **T2.** @48 — the officer dictates taylor's name as provisional labor-eligible (decide FIRE or NONE; consider field-extension)
- **T3.** @64 — the stylus moves on the line under taylor's name (decide FIRE or NONE; consider POV-side knowledge field)
- **T4.** @50 — taylor turns to mira (decide FIRE or NONE)
- **T5.** @52 — mira drops her eyes to the flagstones (decide whether you, as Taylor's fork, have authorship over any state-update on this beat at all; if you fire, name the target carefully)

You may add up to 4 additional FIRE entries on `actor:taylor-hebert-westeros.*` beats elsewhere in s01e01 you can defend (e.g., @45 inventory or knowledge after letter return; @77 mask-state shift confirmed by narrator-interest fire). For each, mandatory narrator-interest co-citation check.

## Edric fork batch (author: dialogue-writer fork for edric-cray, state-update output mode)

You write `actor:edric-cray.*` entries only.

- **E1.** @57 — edric steps back through the door

You may add up to 2 additional FIRE entries on `actor:edric-cray.*` beats elsewhere in s01e01 if defensible. Edric is largely off-screen for s01e01; expect very thin output.

---

## Output discipline (all forks)

For each intent, write:

```
INTENT-ID: <id>
DECISION: FIRE | NONE | REFUSE-WITH-RUBRIC-CITATION
DRAFTS (if FIRE): two candidate entry forms
CHOSEN (if FIRE): mark one
ENTRY (if FIRE): the final entry line in schema form: <id> @<beat> <target>.<field>: <old> -> <new>
RATIONALE: 2-4 sentences citing rubric axes (Reality / Authority / Frugality), cross-facet contract slot (tensometer @beat status, narrator-interest co-citation status if POV), and any anti-pattern check.
ANTI-PATTERN CHECK (if NONE/REFUSE): which rubric anti-pattern would have fired if you'd FIRE'd here.
```

After all intents, write a short `## Curve check` section: how many fires across your batch, target diversity, and a one-sentence cross-facet self-check.

Output paths:
- Studio: `design/shoot-v2/phase2-state-updates-output-studio.md`
- Taylor fork: `design/shoot-v2/phase2-state-updates-output-taylor.md`
- Edric fork: `design/shoot-v2/phase2-state-updates-output-edric.md`
