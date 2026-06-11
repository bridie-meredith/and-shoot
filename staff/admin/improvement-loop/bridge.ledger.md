# Bridge Improvement-Loop Ledger

Cross-repo mining log. One entry per pass. Rotates through areas of `brighid-creative-writing`
to surface process/structure patterns worth porting to `and-shoot`. Principal triages each
filed PROP; bridge loop does not implement.

**Source repo:** `bridie-meredith/brighid-creative-writing`
**Target repo:** `bridie-meredith/and-shoot` (branch `claude/wizardly-brown-6sjjbk`)
**Schema:** append-only; one `---` block per pass.

**Rotation order (cycle indefinitely):**
1. ingrid plans (`rut-detection.plan.md` + `project-improvement-tracking.plan.md`)
2. critic/audience/narrator INDEX registries (`audience/INDEX.md`, `critics/INDEX.md`, `narrators/INDEX.md`)
3. director-cuts (`director-cuts/`)
4. `specs/pipeline-architecture.spec.md`

---

## Pass 1 — 2026-06-11

area_mined: ingrid plans — `staff/agents/ingrid/rut-detection.plan.md` +
  `staff/agents/ingrid/project-improvement-tracking.plan.md` + `audience/INDEX.md`
  (read as supporting evidence)

pattern_found: >
  Audience health trendline. In brighid, oskar writes a structured stink-total table at
  campaign close (`audience_persona | cumulative_stink | prior_campaign_stink | delta |
  signal_source`); ingrid reads it at project close as Axis A of the predecessor-comparison
  framework. The mechanism ensures that rising audience-persona displeasure across consecutive
  runs is visible as a *trendline*, not merely a per-chapter verdict. And-shoot has per-chapter
  audience verdict files (e.g. `active-project/audience/<slug>/*.md`) but no structured
  accumulation and no book-close health trend. The DEC-0115 failure (16 consecutive AIRLESS
  chapters shipped with no circuit breaker because each chapter PASSED in isolation) is the
  live evidence of this gap — a stink trendline would have flagged the pattern at c06.

prop_filed: PROP-0053

next_area: critic/audience/narrator INDEX registries (pass 2)
  Files: `brighid-creative-writing/audience/INDEX.md` (partially read this pass for context),
  `critics/INDEX.md`, `narrators/INDEX.md` — read for naming/quality/tier conventions and
  dispatch-composition patterns not yet mined.
