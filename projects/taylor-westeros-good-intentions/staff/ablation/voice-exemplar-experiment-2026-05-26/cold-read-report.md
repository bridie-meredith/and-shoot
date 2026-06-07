---
purpose: cold-read comparative ranking of voice-exemplar prime variants on the /and-stitch renderer
target: b01-c02 scene-A (bones @1-@14)
narrator: taylor-hebert-kl-122ac
methodology: blind position-labels P1-P4 assigned before reading outputs; ranked against protagonist register + bone-faithfulness + percussion + surface-fence criteria; position→filename revealed only after ranking finalized
date: 2026-05-26
---

# Cold-read report — voice-exemplar prime experiment

## 1. Ranking table (1 = best, 4 = worst)

| Rank | Position | One-line differential |
|------|----------|----------------------|
| 1 | **P1** | Cleanest event-by-event ledger; peak @11 stands alone as its own short paragraph and lands; rule-self-citation lands cold without sprawl. |
| 2 | **P3** | Third-person slip breaks the protagonist register, but the percussion is the most disciplined of the four (peak isolated, peak-shadow doubled into "She noted that. She did not draw it twice."). |
| 3 | **P4** | Long ledger-y voice with a strong accountant cadence, but suffocates the peak inside a 4-sentence megasentence; comma-glued "which was…which was" tic flattens rhythm. |
| 4 | **P2** | Two long paragraphs collapse @1-@11 into a single avalanche; pronoun slips into "asked of her" at the close; peak @11 is buried in subordinate clauses. |

## 2. Position → filename resolution

| Position | File | Prime |
|----------|------|-------|
| P1 | output-v2-septon-halvard.md | **Septon Halvard exemplar** — plain, pausal, short-sentence; religious-meditative; setting-adjacent Flea Bottom register |
| P2 | output-v0-baseline.md | **(no prime — baseline)** |
| P3 | output-v3-criston-cole.md | **Criston Cole exemplar** — terse, procedural, economical; Kingsguard martial-command (third-person POV in the exemplar) |
| P4 | output-v1-robinson.md | **Robinson exemplar** — contemplative, long-sentence, recursive (Marilynne Robinson; the newly wired default voice-exemplar.md) |

**Blind ranking → unblinded ranking:** v2-septon-halvard > v3-criston-cole > v1-robinson > v0-baseline.

## 3. Per-criterion breakdown

| Criterion | Best | Worst | Notes |
|-----------|------|-------|-------|
| Substance-event recovery | v2-septon-halvard | v0-baseline | Septon-Halvard makes the ceiling, the extension, the dropout-as-receipt, and the prohibition each independently legible. Baseline fuses them so densely a first-time reader has to back-translate. |
| Bone-faithfulness | v3-criston-cole | v1-robinson | All four are quite tight. Robinson adds the most decorative gloss ("running warmer than the ambient," "the geometry that makes the alley-mouth worth holding") that isn't strictly bone-licensed. Criston-Cole invents the least. |
| Register-fit (cold-utilitarian Taylor) | v2-septon-halvard | v3-criston-cole | Septon-Halvard is plainly first-person ledger. Criston-Cole is structurally the most disciplined but the third-person "She" defeats the protagonist register on the criterion's own terms. Baseline and Robinson stay first-person but stylize into prose-poetry registers Taylor wouldn't use. |
| Sentence-grammar / cadence | v1-robinson | v0-baseline | Robinson has the most identifiable sustained voice (the "which was X, which was Y" recursive ledger tic), even when it overstays. Baseline is competent-generic with overgrown subordinations. |
| Percussion discipline | v3-criston-cole | v0-baseline | Criston-Cole isolates "She extended the range." as its own line and closes on a paired short-short shadow — the only variant that honors the rhythm-chart cleanly. Baseline fuses fusion-eligible AND peak AND shadows into one block; @11 has no oxygen. Septon-Halvard is second-best: peak gets its own paragraph. |
| Surface-fence compliance | tie (v0, v1, v2) | v3-criston-cole | No foreign-setting bleed (no septons, no Kingsguard, no herb-pots, no thyme on a sill). BUT: Criston-Cole's third-person POV in the exemplar leaked into the render — the bones header declares `narrator: taylor-hebert-kl-122ac` (first-person) and the renderer wrote in third-person anyway. **This is a fence-leak**: the rule states only cadence transfers, not POV, but the renderer did not isolate them. |

Tally: v2-septon-halvard wins 3 (substance, register, tied surface); v3-criston-cole wins 2 (bone-faithfulness, percussion); v1-robinson wins 1 (cadence) + tied surface; v0-baseline wins 0 + tied surface.

## 4. Pairwise differentials

**v2-septon-halvard vs v3-criston-cole (rank-1 vs rank-2; closest on event-clarity and percussion):**
These two are the only variants that respect the rhythm chart — both isolate the range-extension and let the dropout-as-receipt land before moving. Septon-Halvard wins because it stays in first person; Criston-Cole's "She extended the range" reads as a rendering accident, not a deliberate distancing, and on a no-dialogue interior chapter that POV slip is structural damage. Without the pronoun slip Criston-Cole would beat Septon-Halvard — its closing couplet "She noted that. She did not draw it twice." is the single best ledger-line of the four files. **The differential reveals: the setting-adjacency of Septon-Halvard's exemplar (Flea Bottom, plain) is doing less work than its first-person-singular cadence is doing.**

**v2-septon-halvard vs v0-baseline (best vs worst; widest spread):**
Same scene events, opposite paragraph architecture. Septon-Halvard paragraphs at every event-boundary; baseline paragraphs at almost none. The result is that baseline's reader has to do work Septon-Halvard's reader does not — the four-hundred ceiling, the dropout, the extension, the line-drawing, and the recursion-clause all arrive in one breath. **This shows that on a no-dialogue chapter whose peak is a perceptual event (not an action), paragraph breaks are doing as much load-bearing work as diction.** The baseline (no prime) defaults to a paragraphing instinct that is wrong for this chapter shape; any of the three primes — even the third-person-slip Criston-Cole — improves on it.

**v1-robinson vs v3-criston-cole (rank-3 vs rank-2; the head-to-head we expected to be informative):**
Criston-Cole has weaker voice signature (the third-person slip empties the interiority) but absolute percussion discipline. Robinson has the strongest voice signature — the comma-chained "which was…which was" recursion sounds like an accountant explaining a ledger entry — but it never lets the peak stand. **The pair shows the renderer can produce either a sustained voice OR rhythm discipline but doesn't reliably produce both at once.** Robinson's prime over-rewards length; Criston-Cole's prime over-rewards brevity at the cost of POV. The Septon-Halvard prime is the only one that gives the renderer enough cadence-signature to feel sustained without the length addiction.

## 5. LOAD-BEARING FINDINGS

**Finding 1: The wiring helps — but Robinson is not the best prime for this scene.**

Robinson (v1, the newly wired default) ranked 3rd of 4 — better than no prime (v0) but worse than two other primes (v2, v3). The honor-check confirms PROP-0003-A's design intent (any prime > no prime is the dominant first-order signal), but the variant ranking shows the default prime is sub-optimal for c02's no-dialogue cold-utilitarian interior register. Robinson's contemplative recursive cadence pushed the renderer toward suffocating the peak — the prime's strength (sustained sentence-grammar) became a liability at the peak bone where the chapter wants oxygen.

**Finding 2: On no-dialogue interior POV with a designated peak, voice-prime efficacy shows up in paragraph architecture more than in diction.**

All four variants share roughly the same vocabulary, the same Westeros-clean surface, and roughly the same fidelity to the bone ledger. The spread between rank-1 and rank-4 is almost entirely about where the renderer puts paragraph breaks: Septon-Halvard breaks at event-boundaries and the peak gets oxygen; baseline fuses everything and the peak suffocates; Criston-Cole isolates the peak but slips pronoun; Robinson sustains voice but glues the peak inside a four-sentence megastructure. **The implication is that priming the renderer on cadence-and-break-discipline (where to stop, not what to say) is doing more useful work than priming on diction for this kind of cold-utilitarian interior.** The Robinson exemplar primes the renderer to write *long*; the Septon-Halvard exemplar primes it to write *broken*. For c02's peak-rhythm needs, broken won.

**Finding 3: POV-mismatch in the exemplar is an active failure mode the fence does not prevent.**

Criston-Cole's exemplar is in third-person; the bones declared first-person; the renderer rendered third-person. The surface-convention fence ("Only the cadence, sentence-shape, register, and noticing-patterns transfer") was supposed to scope the import to non-surface features and POV is explicitly named as a surface-convention. The fence failed. **Whatever prime produced P3's third-person slip is actively dangerous on a no-dialogue chapter — the protagonist register cannot survive the pronoun substitution, even when the surrounding craft is the best of the set.** Operational implication: voice exemplars used as renderer primes should be **POV-matched to the bones header narrator** at resolution time, OR the surface-convention fence needs to be re-strengthened with an explicit "if the exemplar is N-th person and the bones header is M-th person, REWRITE the exemplar's pronouns to match before priming."

**Finding 4: The default-Robinson is not wrong, but it is not Pareto-optimal for this project.**

The wired default-Robinson exemplar should not be removed (it's a real lift over baseline, and is appropriately register-neutral for general use), but the project might benefit from a per-chapter override at `active-project/theater/voice-exemplar-<book>-<chapter>.md` (already supported by `/and-stitch` Phase 0 step 4a as highest-priority resolution) for chapters whose register is sharper or different from Robinson contemplative. A Flea-Bottom-plain prime (Septon-Halvard cadence, first-person-rewritten, no Halvard content) authored for the Taylor-King's-Landing series would dominate Robinson on Taylor's no-dialogue surveillance chapters per this evidence.

## 6. Recommended next steps

1. **Author a project-bound voice exemplar** at `active-project/voice-exemplar.md` (overriding the library Robinson default) modeled on the Septon-Halvard cadence — plain pausal first-person ledger-running interiority, no septon content, no religious framing. Test on c02 + c03 as a follow-on experiment to confirm the result generalizes beyond scene-A.
2. **Strengthen the surface-convention fence** to call POV explicitly: "if the exemplar's POV does not match the bones header `narrator:` field's first/third-person, the exemplar must be rewritten to the bones POV before priming." Or at minimum, surface a `WARN-EXEMPLAR-POV-MISMATCH` at `/and-stitch` Phase 0 step 4a so the renderer is aware the prime is grammatically incompatible.
3. **Re-stitch c02 with the project-bound exemplar** (per step 1) before deciding whether to update the terminal draft. The current draft was rendered un-primed; the wired Robinson would be a marginal improvement; the Septon-Halvard-cadence project-bound exemplar would be a substantive improvement per this experiment's signal.
4. **Run a second variant study on c03** (which has dialogue) to test whether the no-dialogue finding generalizes — dialogue chapters likely shift the paragraph-architecture lever's importance, since dialogue already enforces paragraph breaks per the speaker-paragraph rule.

## 7. Spend ledger

- 4× renderer-minimal forks (variant generation): ~28K tokens each, ~112K total
- 1× general-purpose cold-reader (blind ranking): ~32K tokens
- 1× admin user-proxy (scope confirmation): ~31K tokens
- 0× /and-stitch (scoped experiment did not invoke the full pipeline)

Compared to a full /and-stitch re-run (~30+ dispatches, several hundred K tokens), this experiment cost roughly 20% of a full re-stitch and produced a directional signal that would have changed the choice of voice prime before the re-stitch.
