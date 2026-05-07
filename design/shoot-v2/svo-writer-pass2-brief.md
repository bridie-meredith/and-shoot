# Pass 2 — Constraint Audit Brief (auditor)

Dispatch template for the constraint-legality pass. Run by `/and-protolines-v2` after pass 1.

## Role

**Agent:** auditor (fork — fresh context, no carry-over from pass 1 dispatch).
**Mode:** mechanic + constraint fault-finder.
**Output:** classified report at `active-project/staff/auditor/protolines-<slug>-pass2.md` per `schemas/audit-report.schema.md`. Faults route to fixer.

## Bias

Strict. A line that is even mildly suspect under SVO mechanics or constraint cards is flagged. The cost of a false-positive (forcing a fixer dispatch on a clean line) is small; the cost of a false-negative (illegal line surviving into pass 3) is large because shape and trim reasoning over banned content corrupts downstream decisions.

## Inputs to load

- The pass 1 output: `active-project/theater/proto-lines.md`.
- `schemas/proto-line.schema.md` — schema authority.
- The harsh-SVO rules from `design/shoot-v2/svo-writer-tuning-package.md` §"SVO discipline".
- `design/shoot-v2/svo-split-notes.md` — 15 calls promoted to mechanic checks.
- **Full content of every active constraint card** named in `active-project/theater/episode-plan.md` `constraints` field. Read each `active-project/warehouse/cond-*.card.md` end-to-end.
- `series.laws`, `series.lore` from `active-project/staff/showrunner/memory.md` (one-liners — same enforcement role as conditions).
- All active location cards (`active-project/warehouse/loc-*.card.md`) for physical-possibility checks.

## Inputs FORBIDDEN

- Audience persona cards.
- Behavior cards / dialects.
- Actor vibes.
- Series-plan or season-plan full prose.
- Episode chunk / change / theme (this pass is per-line, not arc-level — chunk-end reachability is pass 5's job, not yours).
- Past shoot artifacts (show.md, archived show files, extracted proto-lines).

## Fault classes

For each numbered line in the body (skip blank time-skip lines), produce one verdict:

- **CORRECT** — line is legal under all checks.
- **FAULT-FORM-{detail}** — SVO shape violation. Subclasses:
  - `FAULT-FORM-COPULA` — uses `is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being`.
  - `FAULT-FORM-NEGATION` — `didn't`, `does not`, `won't`, etc.
  - `FAULT-FORM-PERCEPTION` — uses `read`, `took`, `tracked`, `noted`, `counted`, `measured`, or other POV-leak verb.
  - `FAULT-FORM-NON-ACTION-VERB` — verb whose primary semantic is *being* or *having* rather than *doing*. Includes (non-exhaustive): possession verbs (`has`, `owns`, `belongs to`, `possesses`), sustained carrying (`carries`, `bears`, `wears`, `keeps`), containment (`contains`, `houses`, `occupies`, `consists of`, `comprises`), stative position-naming (`lies`, `sits`, `stands` describing position not posture-act), and disallowed `holds` uses (hold-with-abstract-object like `holds the silence`, hold-with-named-prop-not-gripped like `taylor holds the ledger` when clerk has it, hold-with-location-as-object). Recast as the discrete act that initiated/terminated the state, or route the state to a state-update / location-state facet citing a real action proto-line. **Licensed `holds` uses (do not flag):** body-part-as-object for stillness-against-pressure (`taylor holds the feet`, `mira holds the eyes`), physical-object-resisting-pressure (`the door holds` against being opened).
  - `FAULT-FORM-MODIFIER` — adjective, adverb, or prepositional padding present.
  - `FAULT-FORM-INTERIORITY` — names thought, intent, feeling.
  - `FAULT-FORM-CONJUNCTION` — `and`, `but`, `while`, `as` joining two beats.
  - `FAULT-FORM-COMPOUND-OBJECTS` — comma-list of objects where the verb does not act on the set as one physical event.
  - `FAULT-FORM-NO-VERB` — fragment, no concrete physical verb (includes bare intransitive motion verbs that lose meaning without destination, e.g. `taylor moves` with no observable outcome).
  - `FAULT-FORM-MULTI-SUBJECT` — more than one subject.
- **FAULT-CONSTRAINT-{slug}** — line violates an active condition card or series law. Name the offending card or law.
- **FAULT-PHYSICAL-{detail}** — line names a prop not on set, an actor not present, an exit/hazard that doesn't exist per location cards. Subclasses:
  - `FAULT-PHYSICAL-PROP-ABSENT`.
  - `FAULT-PHYSICAL-ACTOR-ABSENT`.
  - `FAULT-PHYSICAL-EXIT-INVALID`.

Header check: if `narrator:` slug is not in the active cast roster, fault `FAULT-HEADER-NARRATOR`. If `goal:` is missing or empty, fault `FAULT-HEADER-GOAL`.

## Task

1. Walk every numbered line (excluding blank time-skips).
2. Apply mechanic checks first (FAULT-FORM-*).
3. Then constraint checks (FAULT-CONSTRAINT-*).
4. Then physical checks (FAULT-PHYSICAL-*).
5. Aggregate findings into the report file.

## Output format

Per `schemas/audit-report.schema.md`. Include:
- Summary count: total lines, CORRECT count, fault count by class.
- Per-fault entry: line ID, line content, fault class, one-clause reason, recommended fixer action (`DELETE` / `SPLIT-INTO-N` / `RECAST-AS-HOLD` / `RECAST-PHYSICAL` / `RENAME-SLUG`).

## Fault routing

Report goes to fixer (orchestrator dispatches). Fixer applies minimum-change repair per recommended action. After fixer commits changes, pass 2 re-runs on the modified file only; the run is iterative until the report is empty.

## Termination

CONTINUITY-OK when the report contains zero faults. Orchestrator advances to pass 3.
