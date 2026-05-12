# Round-Trip Tuning Method — Working Catalog

Living log of changes made to writers and reviewers during the dialogue-corpus round-trip experiment. Goal: distill reusable best-practice patterns for future shoot-v2 tuning.

Status: v1 reference (round 3 challenge phase issued; writer defenses pending). Operational protocol has moved to `dialogue-tuning-v2.md`, which preserves the eight v1 writer patterns + the V2/V3 reviewer stages here and re-fits the pipeline around facets-as-lenses. Read this doc for the *evidence* behind those patterns; read v2 for the *protocol* that's wired into the pipeline.

---

## Reviewer (audience) evolution

### V1 — lenient rubric *(round 1)*
- **Rule:** ACCEPT if the line does not actively violate the assigned behavior card.
- **Result on originals:** 57% accept (36/63).
- **Failure mode:** short fragments and inoffensive lines passed without demonstrating any register. The card was getting credit for not being contradicted.

### V2 — strict affirmative-demonstration rubric *(round 1.5)*
- **Rule:** ACCEPT only if the line **affirmatively demonstrates** at least one signature feature of the assigned card AND does not violate it. Inoffensive ≠ on-card.
- **Result on originals:** 40% accept (25/63), defensible floor ≈17%.
- **Audience pushback (kept):** Plumm's lines genuinely earn it — refusing to cut them keeps the rubric honest. *Defending the floor is itself a tuning signal.*
- **Result on regenerated round-2 lines (same rubric):** 94% (16/17).
- **Lift:** +54 points under identical rubric — the comparison is fair only because the rubric did not soften between rounds.

### V3 — adversarial seam-finding *(round 3, current)*
- **Rule:** for every line (accepts included), each persona produces the strongest hostile counter-argument; aggregate the single strongest as "the seam." Output is *defense scaffolding*, not new verdicts.
- **Why:** a clean accept can still be brittle under load. The seam is what a careful reader could yank on.
- **Constraint:** challenges must be persona-distinct (atmosphere / board-move / voice-precision) so the seam isn't generic craft-criticism.
- **Use:** input to writer's defense-or-revise phase.

---

## Writer evolution

### Originals — no card stack loaded
- Single voice contaminates every speaker (Taylor's em-dash + semicolon-spine chassis on noble, septon, maester, smallfolk alike).
- Modern compliance-English ("labor-eligibility," "procedural grounds") substitutes for Westerosi administrative register.
- Implicit lesson: **the dominant POV's voice tells become the project's default chassis unless something explicitly resists.**

### Round 2 writer fork — pattern that worked
1. **One fork per behavior card.** Five behaviors → five forks, parallel. Prevents register cross-contamination at generation time.
2. **Card-stack load order, fully read before drafting:**
   leaf card → parent (if present) → universal overlay (GRRM) → adjacent class/region cards referenced by the leaf → speaker persona card (+ ltm).
3. **Blind to originals.** Writer fork is forbidden to read the show files or the corpus being regenerated. Authoring is from *intent + cards only*. Eliminates paraphrase bias.
4. **Intent bullet ≠ line summary.** The intent specifies:
   - board-move (what the line does)
   - register state (e.g. for Taylor: mask ON / SLIPPING / OFF)
   - rung within the card (functionary vs. knight-administrator within noble-courtly)
   - distance / public-vs-private framing
   The writer authors *against the line's job*, not a softened version of the original sentence.
5. **Multi-draft + chosen mark.** Writer produces 2–3 drafts per intent, marks the chosen one, briefly justifies why each rejected draft is rejected. Lets reviewer test the *claim* not just the line.
6. **Affirmative card-features citation.** Writer must list, per chosen line, which card signatures are demonstrated (with §section citations). Becomes the audience's hostile target.
7. **Explicit anti-patterns.** Every fork brief lists what *not* to do (Taylor's chassis, modern HR-speak, deposition cadence, em-dash + semicolon as default spine). Negative space matters as much as positive.
8. **Calibration anchor.** Include one intent that maps to a known-strong original (Plumm/NC-4 here). Gives the writer a target and the reviewer a control point.

### Round 3 writer defense — pattern (pending execution)
- Read the seams.
- For each line: defend with card citations OR revise. Both outcomes are valid signal — a defended accept stays as is; a revision means the seam was load-bearing.
- Revisions get the same multi-draft + chosen-mark treatment.

---

## Cross-cutting principles emerging

1. **Blind input prevents anchor drift.** The regenerator never sees the original; the auditor never knows generation order. (Round 3 audience-blind comparison still pending — keep this principle.)
2. **Same rubric across rounds.** Lift numbers are only honest if the rubric doesn't soften when the writer improves. Tightening the rubric is allowed *between projects*, not *within a comparison*.
3. **Reviewer pushback is a feature, not noise.** The audience refusing to push past its defensible floor (Plumm earned it) is what makes the rubric trustworthy.
4. **Per-card forks beat a single omniscient writer.** Cross-contamination at generation time is the original failure mode; structurally preventing it costs only parallel-dispatch overhead.
5. **Intent specifies state, not text.** Mask state, rung, distance, public/private. Text-paraphrase intents collapse back to the original.
6. **Anti-patterns are first-class brief content.** "Don't do X" with the project-specific contamination named (em-dash + semicolon-spine) outperformed "follow the card."
7. **Multi-draft makes the chosen line falsifiable.** Reviewer can test *why this draft and not B, C* — the writer's own rejection notes become hypotheses the reviewer can attack.
8. **A calibration anchor in every batch.** One known-strong target prevents the whole batch from drifting upward together while feeling fine.

---

## Open methodological questions

- **The doubled-register problem.** Taylor carries two contradicting cards (Earth-Bet base / Westeros leaf). The contradiction is load-bearing but is also the primary attack surface. Round 3 audience flagged: "the slip is invisible to a reader who hasn't been told to look for it." Open: does the doubled register need a third instrument (in-prose flag, narrator context, adjacent character recognition) to land, or should the line itself carry the slip-tell? Probably both.
- **One-word lines.** "Twelve." rejected, "Twelve, septon." accepted — but the audience also flagged that the patch's recovery is simultaneous with the slip, so there's no observable slip. Open: can a card be demonstrated on a surface area below ~3 words, or is there a structural floor?
- **Cross-line dependencies.** TH-3 and S-2 depend on each other (Rowan's pastoral concern only reads as correct perception if Taylor's "twelve" was actually wrong-in-mouth). The audience now reviews lines in isolation. Open: should round-3+ have a *paired-line* review pass for cross-line load?
- **Reviewer/writer asymmetry.** Reviewer reloads cards; writer reloads cards; both cite the same rubric. This sounds tautological but the pattern works because the writer cites *which signatures the line demonstrates* and the reviewer tests whether each lands. Open: would a separate "card-mechanic auditor" (just checks the cited signatures appear, no taste) reduce reviewer load and free taste-judgment for higher-order critique?
- **Narration-as-source.** User raised: pull narration lines from the project as additional content for writers. Open: narration may be cleaner source for *speaker register testing* than authored dialogue, because narration is less contaminated by the dialogue chassis. Worth a controlled comparison.

---

## Reusable checklist *(snapshot)*

For any future register-tuning round-trip:

**Setup**
- [ ] Behavior cards exist and are read before generation.
- [ ] Active audience is defined (3 personas) with cards under active-project/audience/.
- [ ] One calibration anchor per batch.

**Reviewer**
- [ ] Strict rubric: affirmative demonstration, not non-violation.
- [ ] Persona lenses distinct.
- [ ] Audience may defend its floor — pushback is signal.
- [ ] Same rubric across all rounds being compared.

**Writer**
- [ ] One fork per behavior card.
- [ ] Blind to originals; authoring from intent + cards only.
- [ ] Intent specifies state (mask, rung, distance), not text.
- [ ] Multi-draft + chosen mark + rejection notes.
- [ ] Cited card signatures per chosen line.
- [ ] Explicit anti-patterns named.

**Adversarial round**
- [ ] All lines challenged, accepts included.
- [ ] Persona-distinct seams.
- [ ] Writer defends-or-revises per line.
- [ ] Final reviewer pass — blind to revision history if possible.
