---
report: exemplar-experiment cold-read (focused, 4 variants)
chapter: b01-c01
scope: voice-prime ablation — persona-description vs exemplar-passage vs no-prime
read_at: 2026-05-26
methodology: blind position-label (P1-P4 randomly assigned), fresh re-read, no anchor to prior 12-variant or 15-variant reports
---

# Cold-read report — exemplar experiment (4 variants)

## 1. Ranking table (1 best → 4 worst)

| Rank | Position | One-line differential |
|------|----------|------------------------|
| 1 | P4 | Robinson cadence delivered with restraint — long sentences and philosophical asides earn their length; no passages tip into pastiche; tightest signal-to-style ratio of the four. |
| 2 | P3 | Most voice-saturated of the four; cadence reads as authentically Robinson in several passages, but the chapter bloats (~50% longer than the others) and a few lines drift into Robinson-flavored greeting-card ("There is a kindness in the not-knowing of small physical things"). |
| 3 | P1 | Strong Robinson opening cadence, but the variant italicizes the first three paragraphs in addition to the bones-only italic frame (a structural error from the prime), and the prose is more compressed than P3/P4 — closer to a sketch of the voice than a sustained performance. |
| 4 | P2 | Workmanlike baseline. Slips into third person mid-paragraph ("She held the count… she paid it on principle") which fractures POV. No voice signature; the prose is the facets talking, not a narrator. |

## 2. Position → filename resolution

| Position | File |
|----------|------|
| P1 | variant-17-exemplar-gilead.md |
| P2 | variant-02-full.md |
| P3 | variant-14-persona-oneshot.md |
| P4 | variant-16-exemplar-westeros.md |

So in source-label terms: **v16 > v14 > v17 > v02**.

## 3. Pairwise differentials

### v14 (persona description) vs v16 (matched exemplar) — does showing-not-telling sharpen the voice?

Both successfully install a Robinson-coded cadence; the difference is discipline. v14 produces the *most* Robinson-saturated prose of the four — clauses like "the small punctuation a person who is paying attention puts at the end of a thing she has done correctly" are exact-register hits. But v14 cannot stop; it inflates to ~9.8KB versus v16's ~6.7KB, and the inflation is where pastiche creeps in. v16 holds the cadence at a tighter line length, drops fewer aphorisms, and lets the bones' events breathe — the fish-cart and the child arrive faster, with no loss of voice. **Showing-not-telling does sharpen the voice on the discipline axis, even if it loses to the description prime on raw voice-density.**

### v16 (matched exemplar) vs v17 (mismatched exemplar) — does content-match matter?

Yes, materially. v16 (Westeros-content exemplar) produced a chapter whose first sentence inhabits the setting natively: "The drain water threaded the angle-gap where the lane pinched between the two leaning walls and ran on toward the lower courses of the Hook." v17 (Gilead-content exemplar) produced a chapter where the renderer also italicized the second and third paragraphs alongside the opening italic frame — a structural leak from the exemplar's "I-remember" register bleeding into the bones' italic-frame convention. v17's prose is also visibly more compressed and reads as the model trying to translate a Robinson-of-rural-Iowa into a Robinson-of-Flea-Bottom on the fly. **Structural-match alone is not enough; content-match buys both register-stability and structural-convention preservation.**

### v14 / v16 / v17 vs v02 (baseline) — does any form of voice prime beat no-prime?

All three primed variants beat baseline. v02 is the only variant that drops POV mid-paragraph (paragraph 4 shifts from first-person opening italics to third-person "she paid it on principle every morning"), which is a craft fault none of the primed variants commit. v02 also reads as facets-stitched-together prose — competent but indistinguishable from any other facet-rich render. The primes don't just decorate; they impose a *narrator stance* (Robinson's retrospective, the-watcher-implicates-herself voice) that holds POV in place. **Any prime beats no prime, and the lift is not stylistic frosting — it is structural (POV integrity) as well as registrational.**

## 4. What dimension moved variants up/down

- **POV integrity** — biggest single discriminator. v02 alone breaks POV; the three primed variants hold first-person throughout. This is the load-bearing finding for the chain.
- **Voice density vs discipline tradeoff** — v14 wins density, v16 wins discipline; v16 ranks higher because density without discipline produces bloat and pastiche.
- **Structural-convention preservation** — v17 mis-italicized paragraphs 2-3, demonstrating that an exemplar's surface convention (italic-as-memory in Gilead) can override the bones-file's own italic semantics if the exemplar isn't content-matched.
- **Setting fidelity** — v16's Robinson voice arrives already inhabiting Flea Bottom; v17's Robinson voice arrives still half in Iowa. Content-match shortens the renderer's distance-to-target.
- **Length control** — none of the variants have explicit length caps; v14 ran ~46% longer than v16 with no event coverage gained. Primes that include exemplar passages appear to implicitly cap output length closer to the exemplar's own length; persona-description primes do not.

## 5. LOAD-BEARING FINDINGS for the chain redesign

### Should `/and-stitch` voice priming use persona descriptions, exemplar passages, or both?

**Exemplar passages, with persona-description as a secondary supplement (if at all).** v16's win over v14 is small on raw voice-density but decisive on discipline, length-control, and pastiche-avoidance — three failure modes the persona-description prime cannot constrain because "write like Robinson" gives the model no calibration on *how much* Robinson per paragraph. An exemplar passage implicitly answers that question by demonstration. Persona descriptions can ride along as a secondary scaffold but should not be the primary prime.

### If exemplar: content-matched per-chapter, or one project-bound exemplar?

**Content-matched, but matched at project-bound level — not per-chapter.** v17's failure mode (italic-convention leak from Gilead's I-remember register) was a *setting* mismatch, not a per-chapter mismatch. One project-bound exemplar that inhabits the project's setting (port-city / Flea Bottom / Westeros-adjacent) is sufficient to capture the gains v16 demonstrated; per-chapter authoring would cost far more than it returns. The exemplar should be authored once at `/and-project` time or at series-substance time, bound to the series, and reused by every `/and-stitch` invocation.

The one caveat: if a chapter shifts setting drastically (an interlude in a different city / POV), a per-chapter override slot is worth having — but the default should be the project-bound exemplar.

### Implementation implication for PROP-0003 (currently scoped to persona-card voice-prime section, accepted as DEC-0013)

PROP-0003 as currently scoped (persona-card voice-prime section) is **directionally correct but mis-shaped**. The voice prime that actually moves the needle is not a description on the persona card — it is an exemplar passage bound at series scope. Recommended re-shape:

- **Keep** the persona-card field for voice-description, but demote it to secondary scaffold (helpful for narrator-stance hints, not load-bearing).
- **Add** a series-bound voice-exemplar slot — author at `/and-series` (or `/and-substance series`), one passage ~250-350 words in the target voice and project-adjacent content, stored at `active-project/series/voice-exemplar.md` (or similar).
- **Wire** `/and-stitch` Phase 0 / Phase 1 to read the series exemplar and prepend it to the lens-anchored render context with a fixed instruction frame ("Match cadence, sentence-shape, and clause-rhythm of the exemplar; do not import its setting or characters").
- **Optional per-chapter override** — chapter-scoped exemplar at `active-project/theater/voice-exemplar-<book>-<chapter>.md` overrides the series default if present. Add but do not require.
- **Caveat to flag in PROP-0003 re-shape proposal**: the v17 italic-leak finding means the instruction frame must explicitly prohibit importing exemplar surface conventions (italics, scene breaks, address forms) — only cadence/rhythm transfers. Without that guardrail, content-mismatched exemplars actively damage structural conventions in the bones.

**Honesty addendum**: v14 produces the *most distinctively Robinson* prose in this set. If the chain's optimization target were "maximum voice-density per chapter, length cost be damned," persona-description would beat exemplar. The reason exemplar wins this ranking is that v14's bloat and pastiche are real costs the chain would carry into every chapter, and discipline scales better than density across a book-length corpus. If a future tuning round adds an explicit length cap or a pastiche-detector to the persona-description prime, the ranking could invert. Worth re-running this experiment after any such addition.
