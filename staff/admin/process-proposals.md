# Admin process-change proposals

Append-only log. Schema: schemas/admin-proposal.schema.md.
Triage stamps owned by the principal. Admin does not edit `status`,
`triaged_at`, `triaged_by`, `disposition_note`, or `pr_ref` on own
initiative — only on a follow-up dispatch carrying the principal's ruling.

---

## PROP-0001

```yaml
id: PROP-0002
created_at: 2026-05-26T00:06:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md
  source_verdict: ablation:fold-density-followup (post-PROP-0001-regeneration)
target:
  type: rubric
  path: staff/exposition-author/rubric-exposition.md
  section: "Scope-specific render-as guidance / Form discipline / Audit classes"
change_type: add
rationale: |
  PROP-0001 (dialogue-adjacent fold-in fence) was accepted and applied to the exposition rubric.
  A regeneration run against the updated rubric found zero fence-fires on b01-c01 — the chapter
  has only one speech bone (bone 16) and no first-mention-* entries fall within its ±2 window
  with inline-appositive or em-dash-fold renders-as. PROP-0001 is structurally correct but does
  not explain the b01-c01 cold-read pacing failure, because the pacing cost on this chapter was
  not dialogue-adjacency.

  The regeneration agent's structural read identified the actual driver: cumulative em-dash-fold
  rhythm density at first-mention anchors @1 / @7 / @21 / @27 — four folds across 27 bones,
  with terminal-anchor folds (@21 elder reveal, @27 cost-bearer reveal) compounding the
  register-rhythm load. The reader's attention is taxed by the fold mechanism itself accumulating
  across the chapter, and the cost is highest at reveal-weight bones where the fold competes with
  the reveal's own register demand.

  The rubric currently has no per-chapter aggregate cap on em-dash-fold usage and no rule
  requiring heavier render-as at high-weight reveal anchors. The "cheapest-render-as" heuristic
  is per-anchor and does not brake on aggregate density. This is a gate absence (change_type: add),
  not a modification of an existing gate — no existing rule governs this failure mode.

  Recurrence_count = 1. Non-catastrophic (chapter shipped with Phase 9 PASS). Proposing add
  rather than waiting for recurrence because: (a) the mechanism is fully discriminated from
  PROP-0001's dialogue-adjacency case; (b) the rule can be written with precision now (density
  cap + terminal-anchor weight fence are both enumerable without ambiguity); (c) the ablation
  evidence is cold-read ranked, not a single reviewer taste-flag. Disposition calibrated
  conservatively: SIGNAL on first project-chapter fire, HARD on second.
evidence_refs:
  - "active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md — Cold-reader ranking (rank 1 leave-out-exposition vs rank 2 full); Closing observation (pacing through whitespace); Differential attribution (exposition delta −1); Bottom-of-list candidates"
  - "staff/admin/process-proposals.md — PROP-0001 (dialogue-adjacent fence: confirmed silent on b01-c01 after regeneration; distinct from present finding)"
  - "staff/exposition-author/rubric-exposition.md — Scope-specific render-as guidance §cheapest-render-as heuristic (no aggregate brake exists)"
  - "Regeneration-agent structural read (2026-05-26, inline summary): four em-dash folds across 27 bones; @21 elder reveal + @27 cost-bearer reveal are terminal-anchor folds"
recurrence_count: 1
proposed_diff: |
  In rubric-exposition.md, §Form discipline, add two sub-rules after the existing word-caps
  block:

  **Per-chapter em-dash-fold density cap.** Across all `first-mention-*` entries in a single
  chapter, the total count of `em-dash-fold` renders-as MUST NOT exceed 2. If a third or
  subsequent fold candidate arises, the author MUST step up to `post-bone-clause` or
  `parenthetical-aside` for that entry (or for earlier entries, retroactively, to stay under
  cap). Rationale: four folds across 27 bones created a register-rhythm accumulation that
  the cold reader perceived as pacing compression independent of any single fold's local
  disruption. Two is the cap because PROP-0001's dialogue-adjacency fence typically eliminates
  one potential fold per chapter; the residual budget should be tight enough to prevent
  accumulation without over-restricting.

  **Terminal-anchor fold fence.** A `first-mention-*` entry whose anchor falls in the final
  20% of bones in the chapter (i.e. anchor @N where N ≥ 0.80 × total_bones) is a
  terminal-anchor. Terminal-anchor entries MUST NOT use `em-dash-fold`. Instead:
    - Use `post-bone-clause` (if the gloss fits as a following clause), OR
    - Use `parenthetical-aside` (if the aside completes before the next scene boundary), OR
    - Defer to `episode-open-context` for the following chapter if the term is not critical
      to this chapter's close.
  Rationale: terminal-anchor folds compete with the chapter's own reveal-register demand
  (elder recognition, cost-bearer reveal, protagonist closing interiority). The fold
  mechanism at that weight class splits reader attention between the gloss and the reveal
  simultaneously. Heavier render-as keeps the gloss structurally subordinate.

  In rubric-exposition.md, §Audit classes (Phase 5 hooks), add:

  **AP-SCAN — per-chapter em-dash-fold density.** Count `em-dash-fold` renders-as across all
  `first-mention-*` entries. Total > 2 → SIGNAL (HARD on second chapter-level occurrence in
  the project). Exclusion: entries at @0 are exempt.

  **AP-SCAN — terminal-anchor fold.** For each `first-mention-*` entry, check whether the
  anchor is in the final 20% of bones. If yes AND renders-as is `em-dash-fold` → SIGNAL
  (HARD on second chapter-level occurrence in the project). Exclusion: entries at @0 are
  exempt.

  Note: the 20% threshold for terminal-anchor is a heuristic. On a 27-bone chapter that's
  bones @22–@27; on a 40-bone chapter it's @32–@40. The audit pass computes it per chapter
  from the bones file's total-bone count.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0003

```yaml
id: PROP-0003
created_at: 2026-05-26T01:00:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md
  source_verdict: ablation:voice-prime-finding (15-variant cold-read; variant-14-persona-oneshot ranked #2 of 15)
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 0 step 4 — Persona resolution"
change_type: add
rationale: |
  The 15-variant ablation cold-read found that variant-14 (Marilynne Robinson voice prime, single-shot)
  ranked #2 out of 15 — behind only the recurring leave-out-exposition champion and above the full
  no-prime baseline (#5). The cold reader attributed the gain to the variant sustaining "a meditative
  first-person register across long sentences" and producing "the single best ending in the 15."

  No current chain phase supplies a prose-register anchor to the Phase 1 renderer. The stitch-profile
  `persona:` field resolves a stitcher persona card (neutral / worm-tight / etc.) that carries
  lens-bias tables and Phase 7 aggressiveness — not a prose-voice seed. Phase 1 forks render with
  whatever register the model defaults to after reading bones + facets. The ablation shows that
  supplying a short author-voice prime at Phase 1 dispatch time produces a measurable, ranked,
  replicable gain.

  Change_type is `add` because no existing gate/phase handles voice priming. The stitcher persona
  card format is the adjacent asset (it already shapes Phase 0 → Phase 1 behavior), but it has no
  `voice-prime:` section or equivalent. This is a gate-absence, not a miscalibrated existing gate.

  Note on two-shot: variant-13 (Pass 2 self-critique-and-cut) ranked #14 of 15, and variant-15
  (persona prime + two-shot) ranked #9 — worse than the bare prime at #2. The self-critique Pass 2
  demonstrably destroys cadence and erases the voice gain. This proposal covers voice priming only;
  no proposal for self-critique-and-cut.

  Recurrence_count = 1. Non-catastrophic (chapter shipped with Phase 9 PASS; the finding is an
  ablation quality-of-output gap, not a gate failure). Proposing add at first occurrence because:
  (a) the mechanism is precisely discriminated — Phase 1 has no voice-anchor input; (b) the evidence
  is cold-read ranked across 15 variants, not a single reviewer taste flag; (c) the delta is large
  (+3 ranks over the un-primed full baseline) and replicable; (d) the proposed add is optional-by-default
  (sane fallback = neutral), so adding it to the format does not force a new required artifact on
  projects that don't want it.

  Renderer-minimal mirror: the ablation agent should accept an optional `voice_prime` input field
  (a short prose-register description or exemplar sentence block). When absent, renderer-minimal stays
  instrument-zero (current behavior). When present, the prime is included in the system context at
  render time. This preserves ablation comparability — voice priming can itself be ablated by running
  variants with and without the prime field populated.
evidence_refs:
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md — §6 NEW VARIANT FINDINGS: variant-14 ranked #2 (vs full at #5); cold reader diagnosis: meditative first-person register, strongest individual sentences and closing in the 15; also §5 What mattered most: earned voice vs. mannered voice moved Q2 up to #2"
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md — §3 Cluster notes: voice-prime cluster (Q2, Q6): Q2 commits fully and earns its length through cadence; Q6 inherits the prime but compresses back into dense architecture and loses what made the voice load-bearing — confirms prime must be allowed to run uncut"
  - ".claude/commands/and-stitch.md — Phase 0 step 4: persona resolution loads lens-bias + Phase-7-bias tables; no voice-register anchor field"
  - "staff/stitcher/personas/neutral.md + worm-tight.md — both persona cards carry lens-bias tables and cut-aggressiveness; neither carries a voice-prime or register-heuristic section"
  - "schemas/stitch-profile.schema.md — voice: block carries tense/person/pov/contractions; no prose-register or author-voice field"
  - ".claude/agents/renderer-minimal.md — Render procedure §3: renders from bones + facets; no voice-prime input in the caller payload"
recurrence_count: 1
proposed_diff: |
  PRIMARY CHANGE — .claude/commands/and-stitch.md, Phase 0 step 4 (Persona resolution):

  After loading the stitcher persona card and validating its lens-bias + Phase-7-bias tables,
  add a voice-prime resolution step:

    4a. **Voice-prime resolution (optional).** Check the loaded persona card for a
        `voice-prime:` section. If present, load it as the voice-prime context string.
        Also check `active-project/stitch-profile.md` (project default) and
        `active-project/theater/stitch-profile.md` (episode default) for a `voice-prime:` field
        that overrides the persona card's section.

        If no voice-prime is resolved (persona card has no section, profile has no override):
        voice-prime = null. Proceed with no prime — standard behavior, equivalent to current chain.

        If a voice-prime is resolved: surface it in the Phase 0.5 pre-flight summary as a
        `voice-prime: <slug or first 80 chars>` line (between the `persona:` and `voice:` lines).
        Inject the prime into Phase 1 fork dispatches as a system-context note: "Render prose in
        the following register: <voice-prime text>". Phase 1 forks receive the prime in their
        system context, not as additional facet content — it shapes *how* bones and facets are
        rendered, not *what* is rendered.

        Voice-prime text is a short prose-register description (≤150 words). It is NOT a
        character card, NOT a persona card, NOT a prose passage to paraphrase. Format: register
        heuristics + no more than 2 exemplar sentence shapes. Example shape:
          "Long, considered first-person sentences. The narrator notices physical particulars
           before emotional significance. Clause-heavy constructions that carry the observation
           across the breath rather than breaking it into fragments. The close of a paragraph is
           an arrival, not a landing. Avoid: fragmented staccato, short declarative strings,
           named emotional states."

  PERSONA CARD FORMAT CHANGE — staff/stitcher/personas/ (neutral.md, worm-tight.md, and future cards):

  Add an optional `## Voice prime` section after the `## Lens biases` section. Body is the
  voice-prime text (≤150 words). When the section is absent, voice-prime = null (current behavior
  for neutral.md and worm-tight.md — both should remain absent until a project-specific prime
  is authored).

  STITCH-PROFILE SCHEMA CHANGE — schemas/stitch-profile.schema.md (optional):

  Add an optional `voice-prime: <slug>` field under the `persona:` field in the profile schema.
  When set, this overrides the persona card's `## Voice prime` section (allows per-episode or
  per-scene voice-prime override without re-authoring the persona card).

  RENDERER-MINIMAL MIRROR — .claude/agents/renderer-minimal.md:

  Add an optional `voice_prime` field to the "Input from caller" section:
    - **`voice_prime`** — optional. Short prose-register description (≤150 words). When present,
      inject into the render step (§ "3. Render") as a system-context note identical to the
      and-stitch injection: "Render prose in the following register: <voice_prime text>". When
      absent, renderer-minimal stays instrument-zero (current behavior). The ablation caller
      (/and-ablate) may populate this field or leave it null — null preserves the existing
      comparability baseline. A future ablation dimension can test prime vs. no-prime directly.

  SCOPE / GRANULARITY NOTE:

  Voice priming is most naturally book-bound (voice is consistent across a book). The correct
  home for the book-bound prime is the book-scoped stitcher persona card. If the project uses a
  single project-scoped persona (the current pattern: `worm-tight` for taylor-westeros), the
  voice prime lives in that card's `## Voice prime` section. If future projects use per-book
  personas, the prime travels with the persona. The profile `voice-prime:` override allows
  chapter-level experimentation without re-authoring the persona card.

  NOT PROPOSED: a new `staff/voice-personas/` directory or a new lightweight voice-prime schema.
  The stitcher persona card is already the Phase 0 asset that shapes Phase 1 behavior; adding one
  optional section to it is the minimum-blast-radius path. A new format would require a new
  resolution path, new schema authority, and new `/and-project` binding step — cost L, not M.
cost_estimate: M
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0004

```yaml
id: PROP-0004
created_at: 2026-05-26T02:00:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md
  source_verdict: ablation:leave-out-exposition-rank-1 + user-override-DEC-0012
target:
  type: schema
  path: schemas/facet.schema.md
  section: "Exposition facet entries / surface field"
change_type: modify
rationale: |
  The 15-variant ablation cold-read ranked leave-out-exposition #1 across both the 12-variant
  and 15-variant runs of b01-c01. Admin previously returned OK on DEC-0012, reasoning that two
  cold reads of the same chapter constitute within-chapter replication (not across-chapter
  recurrence) and that PROP-0001/0002 should be tested first.

  The user has directly overridden DEC-0012 with a standing instruction: "move exposition to
  facet consulted by stitcher." This is a user directive, not a process-critic inference.
  Under the admin role definition, an explicit user instruction in the current session overrides
  LTM and prior OK verdicts. DEC-0012 is superseded by DEC-0014.

  The structural form of the override is clear: exposition entries gain a `surface` field
  controlling whether the entry folds into prose or is held as reference context only. Default
  `reference` means exposition is present and consulted — by the stitcher at Phase 1 for
  stake-context, by facet authors for world-grounding — but does not surface as prose inline.
  Only `surface: render` entries fold into prose at first-mention anchors; cap reduced to ≤3
  per chapter. This resolves the cold-read whitespace finding (inline fold-ins no longer appear
  by default) while preserving the world-fact context the stitcher and facet authors require.

  PROP-0001 (dialogue-adjacent fold-in fence) and PROP-0002 (per-chapter em-dash-fold density
  cap + terminal-anchor fence) remain in queue and apply unchanged to the residual `surface: render`
  subset — they are now scoped constraints within a smaller surface area, not obsoleted. Dependency
  flagged, not auto-retired.
evidence_refs:
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md — leave-out-exposition ranked #1 of 15 (and #1 of 12 in prior run); cold reader primary attribution: pacing through whitespace / structural sectioning"
  - "staff/admin/decisions.md — DEC-0012 (OK, no proposal, within-chapter replication) — superseded by user directive DEC-0014"
  - "staff/admin/process-proposals.md — PROP-0001 (dialogue-adjacent fold-in fence, status: open) — still applies to residual surface:render subset"
  - "staff/admin/process-proposals.md — PROP-0002 (per-chapter em-dash-fold density cap + terminal-anchor fence, status: open) — still applies to residual surface:render subset"
  - "schemas/facet.schema.md — current exposition entry format (no surface field)"
  - ".claude/commands/and-facets.md — exposition authoring phase + stitcher Phase 1 exposition consumption"
  - ".claude/commands/and-stitch.md — Phase 1 facet-reading behavior (context for stitcher's reference consumption)"
  - "staff/exposition-author/rubric-exposition.md — exposition authoring rubric (Phase 5 hooks; all current render-as guidance applies to surface:render residual)"
recurrence_count: 2
proposed_diff: |
  PRIMARY CHANGE — schemas/facet.schema.md, exposition entry format:

  Add an optional `surface` field to each exposition entry:

    surface: render | reference | both
    # default: reference (when field is absent, treat as reference)
    # render   — entry folds into prose as inline first-mention gloss at its declared anchor
    # reference — entry is NOT rendered inline; stitcher and facet authors may consult it for
    #             context (stake-framing, world-grounding, term disambiguation) but it produces
    #             no inline prose
    # both     — entry appears both as inline prose AND is available as reference context
    #             (reserved for critical terms the stitcher must both gloss and carry forward;
    #              counts against the ≤3 per-chapter render cap)

  Cap on surface:render entries: ≤3 per chapter (down from the existing cap on total entries).
  Entries beyond the cap MUST use surface:reference. The exposition author declares surface at
  authoring time; the auditor verifies the cap at Phase 5.

  COMMAND CHANGE — .claude/commands/and-stitch.md, Phase 1 (fork rendering):

  Phase 1 fork dispatches receive two exposition inputs:
    (a) surface:render entries — fold into prose at first-mention anchors per existing mechanics
    (b) surface:reference entries (+ surface:both) — provided as background context in the
        system prompt ("World-fact reference: [term] — [gloss]. Do not render this inline;
        use it to ground stake-framing and character interiority."). Not rendered as prose.

  Phase 1 currently reads exposition for fold-in anchors only. The reference-context block
  is new behavior; it replaces "exposition is ignored when not rendered" with "exposition is
  always consulted; only surface:render entries appear in prose."

  COMMAND CHANGE — .claude/commands/and-facets.md, exposition Phase 1 authoring:

  The exposition author's Phase 1 dispatch must declare surface for every entry. Default guidance:
    - Terms the stitcher will gloss inline at first mention → surface: render (cap ≤3; apply
      PROP-0001 dialogue-adjacency fence + PROP-0002 density cap to all render entries)
    - Terms the stitcher and facet authors need for context but should not gloss inline →
      surface: reference
    - No entries should default to render without a stated reason in the author's notes.

  RUBRIC CHANGE — staff/exposition-author/rubric-exposition.md, §Form discipline:

  Add a top-level gate before existing render-as guidance:

    **Surface-field required.** Every exposition entry MUST declare `surface:`. The field is not
    optional. Missing surface → HARD at Phase 5 auditor scan.

    **Per-chapter render cap.** Total count of `surface: render` + `surface: both` entries MUST
    NOT exceed 3. Violation → HARD. Exposition authors who exhaust the cap MUST declare
    subsequent entries `surface: reference`.

    **Reference-only is the default.** When in doubt, use `surface: reference`. The stitcher
    consumes reference entries as background context regardless of their surface setting; prose
    non-appearance is not information loss.

  All existing render-as guidance (render-as rank table, cheapest-render-as heuristic,
  PROP-0001 dialogue-adjacency fence, PROP-0002 density cap + terminal-anchor fence) applies
  exclusively to entries with surface: render or surface: both. Reference entries are not
  subject to render-as rules because they produce no prose.

  DEPENDENCY NOTE — PROP-0001 and PROP-0002:

  Both proposals remain open and unchanged in scope. They now govern a smaller surface area
  (the ≤3 per-chapter render entries rather than all exposition entries). Do not retire or
  supersede them pending triage — they are structural constraints on the residual render subset
  that the principal may still accept, reject, or defer independently of this proposal.

  SCHEMA CHANGE — schemas/facet.schema.md, if exposition entries are formally typed:

  If the facet schema has a typed block for exposition entries (versus free-form YAML), add the
  surface field with default: reference to the block definition. If exposition entries are
  currently untyped/free-form, add a schema note that any exposition section MUST include
  surface: per entry.
cost_estimate: M
status: accepted
triaged_at: 2026-05-26T02:00:00Z
triaged_by: human (direct user directive — override of DEC-0012)
disposition_note: "Pre-accepted by user directive: move exposition to facet consulted by stitcher. PROP-0001/PROP-0002 remain open and apply to residual surface:render subset."
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0003-A

```yaml
id: PROP-0003-A
created_at: 2026-05-26T03:00:00Z
created_by: admin process-critic (amendment)
trigger:
  reason: on-demand
  source_report: active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-exemplar-experiment.md
  source_verdict: ablation:exemplar-experiment (4 variants; v16 exemplar-matched ranked #1; v14 persona-description ranked #2; v17 exemplar-mismatched ranked #3; v02 no-prime ranked #4)
amends: PROP-0003
amends_rationale: |
  DEC-0013 / PROP-0003 accepted adding an optional `## Voice prime` section to the stitcher
  persona card, carrying a ≤150-word prose-register description (register heuristics + ≤2
  exemplar sentence shapes). A follow-up 4-variant experiment tested three priming formats
  against the no-prime baseline:

    v02 — no prime (baseline): last of the four.
    v14 — persona-description prime (register heuristics; Robinson description): ranked #2.
    v16 — exemplar passage prime (Robinson-voice, Westeros-adjacent content): ranked #1.
    v17 — exemplar passage prime (Robinson-voice, Gilead content — content-mismatched): ranked #3.

  Three findings with direct design implications:
  1. All three prime formats beat baseline. The Phase-0 injection point and wiring PROP-0003
     specified are confirmed correct — the problem is not the injection, it is the asset format.
  2. Matched exemplar (v16) beats persona-description (v14). v14 ran 46% longer than v16 with
     no event-coverage gain. The description format caused bloat and aphorism-creep; the
     exemplar format supplied a cadence pattern the renderer could instantiate rather than
     paraphrase.
  3. Content-mismatched exemplar (v17) leaked Gilead surface conventions (italic-as-memory)
     into the target prose. Content-match is load-bearing: exemplar content must be
     adjacent-to-but-not-from the target project.

  These three findings together supersede the asset-format specification in PROP-0003.
  The injection-point (Phase 0 step 4a), the null-default, and the renderer-minimal mirror
  field survive unchanged. Only the asset format changes: from a ≤150-word register-description
  section in the persona card to a standalone exemplar passage file (~250-350 words) with a
  surface-convention fence at the injection point.
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 0 step 4a — Voice-prime resolution (introduced by PROP-0003)"
change_type: modify
rationale: |
  PROP-0003's asset format (persona-card `## Voice prime` section, ≤150 words, register
  heuristics + ≤2 exemplar sentence shapes) was correct in mechanism but wrong in format.
  The cold-read experiment shows that a full exemplar passage — rendered in the target voice,
  content-adjacent to the project — outperforms a description of that voice. The renderer
  benefits from having prose to instantiate, not prose to interpret.

  The surface-convention leak in v17 (Gilead italics-as-memory entering target prose) is the
  critical new constraint: exemplar content must be explicitly adjacent-to-but-not-from the
  project. "Adjacent" means same register, same rough social/temporal setting, same narrator
  distance — not same characters, same events, or same surface conventions. A fence at the
  injection point (explicit prohibition: do not import exemplar surface conventions — only
  cadence and sentence-structure transfer) closes the v17 leak.

  The change from persona-card section to standalone file also improves scope: the exemplar is
  series-bound (one voice across all chapters), not persona-bound (the neutral persona card
  serves many projects). Keeping the exemplar in the persona card conflates project-specific
  voice with persona-level lens-bias. A series-level file separates these correctly.
evidence_refs:
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-exemplar-experiment.md — ranking: v16 > v14 > v17 > v02; v14 46% longer than v16 with no coverage gain (bloat + aphorism-creep); v17 leaked italic-as-memory surface convention from Gilead"
  - "staff/admin/process-proposals.md — PROP-0003 (accepted; asset format being superseded by this amendment)"
  - "staff/admin/decisions.md — DEC-0013 (original acceptance); DEC-0015 (this amendment)"
recurrence_count: 1
proposed_diff: |
  ASSET FORMAT CHANGE (supersedes PROP-0003 persona-card section spec):

  The voice-prime asset is a standalone exemplar passage file, NOT a section in the stitcher
  persona card. Default location:

    active-project/voice-exemplar.md          ← series-level (covers all chapters)
    active-project/theater/voice-exemplar-<chapter-slug>.md   ← optional per-chapter override
                                                                  for interludes or register-shift chapters

  File content:
    - ~250–350 words of prose in the target voice.
    - Content must be ADJACENT-TO-BUT-NOT-FROM the project: same register, same rough
      social/temporal setting, same narrator distance — different characters, different
      events, no surface conventions shared with the project.
    - Authored once at `/and-series` (series-level exemplar) or at `/and-substance chapter`
      (per-chapter override for interludes). The authoring step is new and must be added to
      `/and-series` Phase N as an optional step (flag: `--voice-exemplar`).
    - NOT a character card, persona card, or register description. It is a prose passage only.
      No bullet lists, no register heuristics, no meta-commentary on the voice.

  PHASE 0 STEP 4a CHANGE (.claude/commands/and-stitch.md):

  Replace the persona-card `## Voice prime` section lookup with a file lookup:

    4a. **Voice-prime resolution (optional).** Check for:
        (1) `active-project/theater/voice-exemplar-<chapter-slug>.md` (per-chapter override).
            If present, use this file's content as the voice-prime passage.
        (2) If (1) absent, check `active-project/voice-exemplar.md` (series-level default).
            If present, use this file's content as the voice-prime passage.
        (3) If both absent, voice-prime = null. Proceed with no prime — standard behavior,
            equivalent to current chain. No error, no warning.

        If a voice-prime passage is resolved:
        - Surface it in the Phase 0.5 pre-flight summary as:
            `voice-prime: <filename> (<word-count>w)`
        - Inject into Phase 1 fork dispatches as a system-context note:
            "Render prose in the cadence and sentence structure of the following passage.
             Transfer: sentence length patterns, clause construction, paragraph breath,
             arrival-not-landing paragraph closes.
             DO NOT transfer: surface conventions (italics usage, scene-break symbols,
             address forms, character names, any device specific to the exemplar's
             source material). Cadence and structure only.
             Exemplar: <passage text>"
        - The prohibition fence (DO NOT transfer surface conventions) is mandatory and must
          appear verbatim in every Phase 1 fork dispatch that carries a voice prime.
          This closes the content-mismatch leak observed in v17.

  PERSONA CARD FORMAT CHANGE (reversal of PROP-0003 card change):

  Do NOT add a `## Voice prime` section to stitcher persona cards (neutral.md, worm-tight.md,
  or future cards). PROP-0003's proposed persona-card section is superseded. The persona card
  remains limited to lens-bias tables and Phase 7 aggressiveness. Voice priming is
  project/series-scoped, not persona-scoped; the standalone file keeps these concerns separate.

  STITCH-PROFILE SCHEMA CHANGE (.schemas/stitch-profile.schema.md — replaces PROP-0003 spec):

  Replace the proposed `voice-prime: <slug>` field (which pointed to a persona-card section)
  with a `voice-exemplar-override: <path>` field (optional):
    - When set, this path overrides the standard lookup chain (series-level and chapter-level
      file paths above) with a caller-specified exemplar file path. Useful for one-off
      interlude chapters that need a wildly different register without creating a permanent
      chapter-override file.
    - When absent, standard lookup chain applies.

  RENDERER-MINIMAL MIRROR (.claude/agents/renderer-minimal.md — amends PROP-0003 spec):

  Replace the proposed `voice_prime` field (≤150-word description) with:
    - **`voice_exemplar_path`** — optional. Absolute path to a prose exemplar file
      (~250–350 words). When present, renderer-minimal reads the file and injects the
      passage into the render step (§ "3. Render") using the same injection template as
      /and-stitch Phase 0 step 4a, including the mandatory surface-convention fence.
      When absent, renderer-minimal stays instrument-zero (current behavior).
      The ablation caller (/and-ablate) may populate this field or leave it null — null
      preserves the existing comparability baseline. A future ablation dimension can
      test matched-exemplar vs. mismatched-exemplar vs. null directly.

  AUTHORING STEP — /and-series (new optional phase):

  Add an optional voice-exemplar authoring step to /and-series. Trigger: flag `--voice-exemplar`
  or user-proxy answer YES to "Author a series voice exemplar?" at /and-series Phase N.
  The screen-writer (or the stitcher persona author) authors a ~250-350 word passage:
    - Voice: the target author's register (e.g., Marilynne Robinson; Alice Munro; etc.)
    - Content: a scene adjacent to but not from the project's setting (different characters,
      different events, same rough register + narrator distance)
    - Delivery constraint: no surface conventions that would leak (italics patterns, address
      forms, etc. idiosyncratic to the exemplar author's published work must be stripped or
      neutralized)
  Output written to `active-project/voice-exemplar.md`. Included in showrunner memory as
  a one-line note (`voice_exemplar: authored at /and-series, <date>`).

  SCOPE NOTE:

  Per-chapter override (`active-project/theater/voice-exemplar-<chapter-slug>.md`) is the
  correct mechanism for interlude chapters that need a substantially different register — e.g.,
  an interlude chapter in a formal court register vs. a street-level chapter. It is NOT for
  fine-tuning voice chapter-by-chapter. The series-level exemplar covers ~90% of chapters;
  the per-chapter override is for genuine register-shift chapters only.
cost_estimate: M
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: PROP-0003 (asset-format specification only; Phase 0 step 4a injection point + null-default + renderer-minimal mirror field survive, amended in format)
```

---

## PROP-0005

```yaml
id: PROP-0005
created_at: 2026-05-26T04:00:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/ablation/impersonator-experiment-2026-05-26/cold-read-report.md
  source_verdict: user-directive-persona-exemplar-architecture (two converging experiments: renderer v16>v14>v02 + impersonator v03>v01>v02)
target:
  type: schema
  path: schemas/persona-exemplar.schema.md
  section: null
change_type: add
rationale: |
  Two experiments this session converged on the same finding: exemplar passages beat persona-description
  as agent voice primes. Renderer experiment (PROP-0003-A / DEC-0015): v16 matched-exemplar ranked #1,
  v14 persona-description ranked #2, v02 no-prime ranked last. Impersonator experiment (just-completed):
  v03 exemplar ranked #1, v01 baseline ranked #2, v02 persona-description ranked #3. Across two
  independent agent types, at two different layers of the chain (stitch-time rendering and
  character-impersonation dispatch), exemplar passages outperform description-of-voice as a prime.

  PROP-0003-A (DEC-0015) addressed this finding narrowly — a standalone voice-exemplar file at
  `active-project/voice-exemplar.md` for the stitcher's Phase 0 step 4a injection. That proposal's
  scope is the series-level prose register. The impersonator experiment generalizes the same pattern
  to persona-level voice priming: when dispatching an impersonator, audience-persona, or
  orchestrator-critic agent, supplying a concrete exemplar of that agent's expected output shape
  outperforms supplying a description of how the agent should sound.

  The user has directed a full architectural response: a new directory (`cards/persona-exemplars/`)
  holding per-persona exemplar passages; existing `cards/personas/<slug>.card.md` re-scoped to
  biography (identity, role, values, fences, taste); agents that consume personas receive both
  the biography card AND the exemplar at dispatch time; the exemplar is the live voice/output-shape
  channel. Strong named candidates: the 22 audience personas + orchestrator-critic + impersonator.

  This is change_type: add because no existing schema, directory, or dispatch convention handles
  persona-level exemplars. PROP-0003-A handles series-level voice priming (a different concern —
  series register, stitcher-only). This proposal generalizes the same architectural pattern to
  persona-level agents chain-wide. The two are complementary, not duplicative. PROP-0003-A is
  explicitly NOT superseded; its renderer-specific mechanics remain the correct implementation for
  that narrower scope. PROP-0005 is the broader architectural container of which PROP-0003-A is
  an instance.

  Recurrence_count = 2 (two independent agent experiments within the same session). Proposing at
  first cross-agent occurrence because: (a) evidence is cold-read ranked across both experiments;
  (b) the finding is architecturally convergent, not noise; (c) the user has explicitly directed
  the architectural response; (d) the add is optional-by-default — agents without an exemplar fall
  back to biography-only (current behavior); (e) the new schema + directory are low-blast additions
  that do not force changes to any existing file until exemplars are authored.
evidence_refs:
  - "active-project/staff/ablation/impersonator-experiment-2026-05-26/cold-read-report.md — impersonator experiment: v03 exemplar > v01 baseline > v02 persona-description; exemplar ranked #1"
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-exemplar-experiment.md — renderer experiment: v16 matched-exemplar > v14 persona-description > v17 mismatched-exemplar > v02 baseline; v14 46% longer than v16 with no coverage gain"
  - "staff/admin/process-proposals.md — PROP-0003-A (renderer voice-exemplar; accepted in format by DEC-0015; narrower scope: series-level register, stitcher only; NOT superseded by this proposal)"
  - "staff/admin/decisions.md — DEC-0015 (PROP-0003-A authored; exemplar > description finding at renderer layer)"
  - "cards/persona-exemplars/ — directory created by user this session (library-bound location confirmed)"
recurrence_count: 2
proposed_diff: |
  ITEM 1 — NEW SCHEMA: schemas/persona-exemplar.schema.md

  Author a new schema file defining the persona-exemplar format. Required fields:

    persona_slug: <slug>          # must match a card in cards/personas/<slug>.card.md
    purpose: voice | output-shape | both
      # voice       — exemplar demonstrates register, sentence rhythm, word-choice
      # output-shape — exemplar demonstrates structural format of the agent's output
      # both         — the common case for audience and critic agents (voice + output structure together)
    content_match_notes: <one sentence>
      # required. States what makes this exemplar content-adjacent-but-not-from the project.
      # For audience/critic exemplars: confirm the passage does not import surface conventions
      # from a specific source text that the agent would then leak into target prose.
    authored_by: <agent or session>
    authored_at: <ISO date>

  Body: the exemplar passage itself. Length range:
    - Voice exemplar (purpose: voice): ~250–350 words of prose. Same constraint as PROP-0003-A:
      content adjacent-to-but-not-from the project; no surface conventions that would leak.
    - Output-shape exemplar (purpose: output-shape): a representative output sample — typically
      one full review paragraph or a comparable block showing the agent's characteristic structure,
      stance, and notation conventions. Length as needed to demonstrate the shape (not a minimum).
    - Both: whichever is longer governs the length target.

  Surface-convention fence (mandatory for voice purpose): exemplar content must be
  adjacent-to-but-not-from the target project. Dispatching agents must include the prohibition:
  "Transfer: cadence, sentence length patterns, clause construction, output structure.
   DO NOT transfer: surface conventions (italics usage, notation systems, address forms,
   any device specific to the exemplar's source)."

  This fence generalizes PROP-0003-A's surface-convention fence from the renderer to all
  exemplar-consuming dispatch points.

  ITEM 2 — CARD SCHEMA NOTE: schemas/card.schema.md

  Add a note to the biography/persona card schema that the `cards/personas/<slug>.card.md`
  files are now explicitly biography-scoped: identity, role, values, fences, taste, threshold
  discipline. Voice and output-shape demonstration live in `cards/persona-exemplars/<slug>.md`.
  The biography card is not deprecated or restructured — it is re-labeled as the DESCRIPTION
  layer. The exemplar is the DEMONSTRATION layer. Both are valid inputs to agent dispatch;
  the exemplar is the preferred live channel when one exists.

  ITEM 3 — MARGIT RESPONSIBILITY: staff/margit/card.md (or equivalent margit definition)

  Extend margit's responsibility to cover persona-exemplars:
    - Validate new persona-exemplar files against schemas/persona-exemplar.schema.md at authoring time.
    - Index exemplars in the cards catalog alongside biography cards (or in a parallel
      `persona-exemplars` section of the catalog index).
    - Promotion path: exemplar is authored alongside or after the biography card. Margit does not
      block biography card provisioning on the absence of an exemplar — exemplars are incremental.
    - When an exemplar exists for a persona, margit notes it in the catalog index entry for that slug.

  ITEM 4 — AGENT DEFINITION UPDATES

  Agents that consume persona cards should gain an optional input field for exemplar path:

    - **Impersonator** (`.claude/agents/impersonator.md` or equivalent): add optional
      `voice_exemplar_path` field. When present, exemplar is injected into character dispatch
      as a system-context note using the same surface-convention fence as PROP-0003-A.
      When absent, behavior is current biography-card-only (no regression).

    - **Audience agent** (invoked at `/and-facets` Phase 5b and `/and-write` bone-gate):
      The 3 active audience persona cards are in `active-project/audience/`. Each persona's
      dispatch should accept an optional `exemplar_path` pointing to the matching
      `cards/persona-exemplars/<slug>.md`. When present, exemplar is injected alongside the
      biography card. When absent, biography-only (current behavior).

    - **Orchestrator-critic** (`staff/orchestrator-critic/card.md`): add optional
      `exemplar_path` field. The orchestrator-critic's output-shape is well-defined
      (verdict + per-criterion drill-down + ranking); an output-shape exemplar demonstrating
      that structure would be the most natural exemplar type (purpose: output-shape or both).
      Per user's note: "critic might also profit if the exemplars are written to the taste
      of the persona" — meaning the exemplar passage should reflect the critic's characteristic
      severity and criterion prioritization, not just structural format.

    - **Renderer-minimal** (`.claude/agents/renderer-minimal.md`): PROP-0003-A already
      specified `voice_exemplar_path` for series-level voice. No change needed here for
      PROP-0005; the renderer-minimal field covers the stitcher/render layer.

  ITEM 5 — DISPATCH CONVENTION: command bodies that fire the above agents

  In each command body that dispatches impersonator, audience, or orchestrator-critic, add a
  standard exemplar-resolution step after persona-slug resolution:

    After resolving the persona slug, check for a matching exemplar at
    `cards/persona-exemplars/<slug>.md`. If present, include `exemplar_path: <path>` in the
    agent dispatch payload alongside `persona_path`. If absent, omit the field (agent falls back
    to biography-only). This resolution step is passive — it does not block on absence.

  Command bodies affected: `.claude/commands/and-facets.md` (Phase 5b audience dispatch),
  `.claude/commands/and-write.md` (bone-gate audience dispatch), and any command that fires
  the orchestrator-critic (e.g. `/and-review verdict`).

  ITEM 6 — MIGRATION PLAN

  Existing 22 audience persona cards in `staff/audience/` do NOT require exemplars to ship the
  architecture. The schema, directory, margit extension, and agent-definition optional fields can
  land without any exemplar being authored. Initial cohort for exemplar authoring (named by user):

    - 3 active-project audience personas (currently bound to the active project)
    - orchestrator-critic (output-shape + taste exemplar)
    - Taylor (impersonator exemplar — voice already implied by series-level voice-exemplar at
      `active-project/voice-exemplar.md`; a character-specific exemplar would go further,
      demonstrating Taylor's interior-monologue style specifically)

  Exemplars are authored on-demand, not required at project activation or cast time.

  ITEM 7 — OPEN QUESTIONS (for principal triage)

  a. Project-bound vs. library-bound exemplars: `cards/persona-exemplars/` is library-bound
     (created this session). Should project-specific exemplar overrides also be supported at
     `active-project/persona-exemplars/<slug>.md`? Resolution path would mirror PROP-0003-A's
     per-chapter override: check project-bound first, fall back to library. Not required for
     initial architecture — flag for principal decision.

  b. Multi-exemplar slots per persona: a single canonical exemplar per persona (one file per slug)
     or multiple typed slots (e.g. `<slug>-dialogue.md`, `<slug>-interior.md`,
     `<slug>-decision.md`)? Single file is lower infrastructure; multi-slot is more precise for
     agents with distinct output modes (impersonator does dialogue, interior, decision separately).
     Current proposal: single file, purpose field declares the dominant type. Principal may expand.

  c. Versioning: when a persona biography card is revised mid-project, do exemplars version
     independently or are they considered stale on card revision? Current proposal: no automatic
     staleness cascade — exemplars are stable unless the author explicitly revises them. If a
     card revision materially changes the persona's voice or output shape, the exemplar should
     be re-authored manually. No automated enforcement of this (cost: S to add a note to
     margit's validation; not required at launch).

  DEPENDENCY NOTE — PROP-0003-A:

  PROP-0003-A specifies the renderer / stitcher instance of the exemplar pattern: a series-level
  prose-register file at `active-project/voice-exemplar.md`, injected at `/and-stitch` Phase 0
  step 4a and mirrored to renderer-minimal's `voice_exemplar_path` field. That proposal's
  specific mechanics (file location, injection template, surface-convention fence wording,
  optional per-chapter override) are the correct implementation for that layer and are NOT
  superseded by PROP-0005. PROP-0005 generalizes the same pattern to persona-level agents.
  The two proposals are complementary: PROP-0003-A is the renderer instance;
  PROP-0005 is the persona-agent generalization. Accept / reject / defer each independently.
cost_estimate: L
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0005-A

```yaml
id: PROP-0005-A
created_at: 2026-05-26T05:00:00Z
created_by: admin process-critic (amendment)
trigger:
  reason: critic-experiment-refutes-universal-scope
  source_reports:
    - active-project/staff/ablation/audience-experiment-2026-05-26/judgment.md
    - active-project/staff/ablation/critic-experiment-2026-05-26/judgment.md
  source_verdict: "audience-experiment: exemplar LIFT (medium, 4/5 criteria); critic-experiment: exemplar LOSS (4/6 criteria) — same architecture produces opposite outcomes by consumer type"
amends: PROP-0005
amends_rationale: |
  PROP-0005 (DEC-0016) proposed exemplar priming across all persona-consuming agents:
  impersonator, audience, and orchestrator-critic. The generalization was supported by two
  converging experiments (renderer + impersonator) and directed by the user.

  Two follow-up experiments now discriminate the pattern by consumer type:

  AUDIENCE EXPERIMENT — exemplar-primed cape-fic-reader won 4/5 criteria over the
  biography-only baseline. Lift: medium. Three new failure modes observed (cadence over-fit,
  performative theatricality, prescription atrophy) but net positive. Exemplar priming
  helps judgment/voice-driven consumers.

  CRITIC EXPERIMENT — exemplar-primed orchestrator-critic LOST to baseline on 4/6 criteria.
  The exemplar's prose-shape dominated the card's enumerated A/B/C/R template: the schema
  check was dropped, the F7-r2 lookup was skipped, and the critic fabricated an EFFICIENT
  runtime judgment without evidence — a direct honesty-discipline violation. The exemplar
  did not enhance the critic's output quality; it corrupted its structural reliability.

  The discriminating criterion is not "loads a persona" but "is the output voice-shape-driven
  or template-shape-driven." Voice/judgment-driven consumers gain from exemplar priming.
  Template/structure-driven consumers are harmed by it because the exemplar's prose-shape
  competes with (and can displace) the consumer's prescribed structural schema.

  PROP-0005 core architecture (directory, schema, biography/exemplar split, dispatch
  convention) is NOT retired. The amendment narrows scope: orchestrator-critic is explicitly
  excluded from the current PROP-0005 rollout. Dramatist, auditor, and editor are also
  deferred under the same discriminator (all are template/schema-driven consumers). A future
  sub-class of exemplar that conforms to the prescribed template format — rather than leading
  with prose voice — may be appropriate for Tier 2 consumers and would require its own
  experiment and proposal.
target:
  type: schema
  path: schemas/persona-exemplar.schema.md
  section: "purpose field + consumer-tier classification"
change_type: modify
rationale: |
  The audience experiment confirms: exemplar priming works for voice/judgment-driven consumers.
  The critic experiment refutes: exemplar priming does not work for template/schema-driven
  consumers. The criterion is mechanistically precise and discriminated by experiment, not
  inferred. PROP-0005 must be scoped to Tier 1 consumers; auto-extension to Tier 2 consumers
  is explicitly blocked pending a different exemplar sub-class.

  The principal's directive states the refinement: leave the orchestrator-critic exemplar file
  on disk (useful design artifact) but mark it as excluded from active dispatch. No agent
  dispatch pipeline should include the orchestrator-critic exemplar until a Tier 2 approach
  is validated.
evidence_refs:
  - "active-project/staff/ablation/audience-experiment-2026-05-26/judgment.md — exemplar-primed cape-fic-reader won 4/5 criteria; new failure modes: cadence over-fit, performative theatricality, prescription atrophy; net positive"
  - "active-project/staff/ablation/critic-experiment-2026-05-26/judgment.md — exemplar-primed orchestrator-critic lost 4/6 criteria; schema-check dropped; F7-r2 lookup skipped; EFFICIENT fabricated without evidence; honesty-discipline violation"
  - "staff/admin/process-proposals.md — PROP-0005 (accepted scope being narrowed by this amendment)"
  - "staff/admin/decisions.md — DEC-0016 (PROP-0005 authored; broad scope: impersonator + audience + orchestrator-critic)"
recurrence_count: 1
proposed_diff: |
  ITEM 1 — SCOPE AMENDMENT: schemas/persona-exemplar.schema.md

  Add a `consumer_tier` field to the schema:

    consumer_tier: 1 | 2 | 3
    # Tier 1 — voice/judgment-driven consumers (apply exemplar treatment; confirmed gain)
    #   Confirmed members: renderer (PROP-0003-A), impersonator (impersonator experiment),
    #   audience (audience experiment).
    # Tier 2 — template/structure-driven consumers (defer; exemplar treatment as currently
    #   specified causes structural regression)
    #   Members: orchestrator-critic, dramatist, auditor, editor.
    #   May be revisited with a template-conforming exemplar sub-class. A Tier 2 exemplar
    #   would demonstrate the agent's prescribed schema/template being executed well, rather
    #   than leading with prose voice. Requires its own experiment before dispatch.
    # Tier 3 — no persona/voice channel (out of scope)
    #   Members: showrunner, margit, fixer.

  When consumer_tier is 2 or 3, dispatch convention (PROP-0005 Item 5) MUST NOT inject
  the exemplar into agent dispatch. The exemplar file may exist in cards/persona-exemplars/
  as a design artifact, but it is excluded from active dispatch until a Tier 2 approach is
  validated.

  ITEM 2 — DISPATCH EXCLUSION: orchestrator-critic

  In command bodies that fire the orchestrator-critic (e.g. .claude/commands/and-review.md,
  verdict subcommand), do NOT add the exemplar_path resolution step that PROP-0005 Item 5
  specifies for Tier 1 agents. The orchestrator-critic dispatches biography-card-only until
  a Tier 2 exemplar sub-class is validated.

  ITEM 3 — EXEMPLAR FILE METADATA: cards/persona-exemplars/orchestrator-critic.md

  Add to the file's frontmatter:

    dispatch-status: excluded
    excluded-by: DEC-0017
    excluded-reason: |
      Critic experiment (2026-05-26) found exemplar priming caused structural regression
      in the orchestrator-critic: schema checks dropped, F7-r2 lookup skipped, EFFICIENT
      fabricated without evidence. Orchestrator-critic is a Tier 2 (template/structure-driven)
      consumer. Exemplar priming as currently specified does not apply to Tier 2 consumers.
      File retained as design artifact. Do not inject into orchestrator-critic dispatch.

  ITEM 4 — TIER 2 FUTURE PATH (not a current proposal)

  A Tier 2 exemplar sub-class would differ from Tier 1 in its governing principle:
    - Tier 1 exemplar: demonstrate voice/judgment in prose
    - Tier 2 exemplar: demonstrate the agent's prescribed structural schema being executed
      correctly (i.e., show a well-formed A/B/C/R block, not prose that approximates it)
  A Tier 2 experiment would prime the orchestrator-critic with a model-verdict that exactly
  follows its card's enumerated template, then test whether the structural compliance improves
  without displacing the schema. This is a separate experiment, not an extension of the
  current exemplar architecture. Flag for future triage only — not a current proposal item.

  ITEM 5 — PROP-0005 ITEMS 1-7: unchanged

  PROP-0005's schema (Item 1), card schema note (Item 2), margit responsibility (Item 3),
  and agent definition updates (Item 4) for Tier 1 agents (impersonator + audience) are
  unchanged. The orchestrator-critic sub-item in PROP-0005 Item 4 is superseded by this
  amendment's exclusion. PROP-0005 Items 5-7 (dispatch convention, migration plan, open
  questions) apply only to Tier 1 agents.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0006

```yaml
id: PROP-0006
created_at: 2026-05-26T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-final-audit.md + active-project/staff/audience/worm-canon-pedant/vibes-r1-verdict.md
  source_verdict: "Phase 5b cycle 1 REVISE (vibes) — auditor Phase 5 CONSTRAINT Earth-Bet hard-fence scan returned CLEAN but worm-canon-pedant independently found Earth-Bet fence hits inside vibes keyword token arrays (gold-morning-refusal in vibes:2; khepri-rhyme in vibes:13); resolved by fixer keyword-replacement in cycle 1 before /and-stitch"
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 5 — AUDIT: single auditor dispatch / Audit classes / CONSTRAINT / Earth-Bet hard-fence proper-noun scan"
change_type: modify
rationale: |
  The auditor's Phase 5 CONSTRAINT Earth-Bet hard-fence proper-noun scan is described as a
  "case-insensitive substring scan against the Earth-Bet proper-noun list across every text field
  of every facet entry." The scan explicitly states: "Names to scan ... Any hit is HARD; emit
  [<facet>:<id>] @<proto> — earth-bet-hard-fence — <name> at <field>: <surrounding-text>."

  In b01c02, the auditor's scan passed the vibes facet as CLEAN. It listed the entry-level
  keyword handles in its scan trace ("Keyword arrays: cost-signature-range-bound,
  atonement-as-repetition, ...") but did not walk the individual token strings inside each
  entry's bracket-enclosed token array. Two fence violations were present inside token arrays:

    vibes:2 ("atonement-as-repetition") — token "line-drawn-at-twelve-in-same-hand-as-gold-morning-refusal"
      contains substring "gold morning" (fence list entry: "Gold Morning")
    vibes:13 ("surveillance-architecture-legible") — token "accounting-structure-readable-as-khepri-rhyme-by-audience-not-taylor"
      contains substring "khepri" (fence list entry: "Khepri")

  The worm-canon-pedant independently identified both at Phase 5b and escalated them as
  independent REVISE bases. Fixer resolved both via keyword replacement in cycle 1.

  The structural gap: the auditor's scan treats the vibes facet entry as having two levels
  of text fields — the entry-level keyword handle and the bracket-enclosed token array — but
  only scanned the first level. The scan spec says "every text field" and the command body
  CONSTRAINT section notes "Slug components matter: a margit-referral slug embedding
  `khepri-` or `gold-morning-` is a hard-fence violation even when no full English phrase is
  rendered." Token array strings are text fields by any reading, and the scan's stated
  scope must include them. This is a scope-description gap that caused two HARD-class
  findings to be caught only at Phase 5b (audience) rather than Phase 5 (auditor CONSTRAINT),
  which is the authoritative gate for this class. The failures were non-catastrophic (fixer
  resolved in cycle 1), but the CONSTRAINT class is the mechanical backstop for fence
  violations; relying on audience adversarial review to catch HARD CONSTRAINT items is
  a gate-gap, not just a taste call.
evidence_refs:
  - "active-project/staff/audience/worm-canon-pedant/vibes-r1-verdict.md — vibes:2 'gold-morning-refusal' finding (lines 25-43); vibes:13 'khepri-rhyme' finding (lines 61-67)"
  - "active-project/staff/auditor/facets-final-audit.md — CONSTRAINT section, Earth-Bet hard-fence scan: CLEAN declaration + auditor keyword-array scan trace (lines 111-118) — shows auditor listed keyword handles, not sub-tokens"
  - ".claude/commands/and-facets.md — Phase 5 CONSTRAINT § Earth-Bet hard-fence proper-noun scan clause: 'case-insensitive substring scan ... across every text field of every facet entry'; also: 'Slug components matter: a margit-referral slug embedding khepri- or gold-morning- is a hard-fence violation'"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, the CONSTRAINT section's Earth-Bet hard-fence proper-noun
  scan clause, add explicit enumeration of vibes token array scope.

  Current text (from "Earth-Bet hard-fence proper-noun scan" through the vibes entry in the
  example scan-target list):
    "vibes entity-target-primary fields"

  Proposed addition — after "vibes entity-target-primary fields", add:
    "vibes token arrays (for every vibes entry, scan EACH individual token string inside the
    bracket-enclosed [ ] bundle separately; the scan must walk token-by-token, not stop at
    the entry-level keyword handle; a token containing a fence-list substring is a hit
    regardless of how the token is hyphenated or whether the surrounding context qualifies
    the name — the fence is a substring scan, not a semantic check)"

  Additionally, the scan trace the auditor writes to the audit report should be required to
  confirm per-token coverage explicitly. Add a one-line audit note requirement:
    "For the vibes facet, the auditor must confirm: 'Vibes token arrays scanned token-by-token:
    <n> entries × ~<avg-token-count> tokens each.' A scan trace that lists only keyword handles
    does not satisfy the per-token requirement."

  This is a single-paragraph clarification of existing scope. It adds no new fence targets and
  does not change the HARD disposition of any hit. Cost: S (one clause addition to one section
  of one command body, plus a one-line scan-confirmation note in the same section).
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0007

```yaml
id: PROP-0007
created_at: 2026-05-26T00:00:00Z
created_by: admin process-critic
trigger:
  reason: postop
  source_report: active-project/staff/reviews/pleasure-read-b01-c02-2026-05-26-postop.md + active-project/staff/reviews/audience-worm-canon-pedant-b01-c02-2026-05-26-postop.md
  source_verdict: postop-convergence:divergent (Fork A substance DELIVERED clean; Forks B+C converge on compound-noun saturation prose-surface tic)
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition step 5 (SVO discipline) + Phase 6 HARD/SIGNAL classification table"
change_type: modify
rationale: |
  Two independent postop reports (Fork B naive cold-read + Fork C worm-canon-pedant) converge
  on compound-noun saturation as a prose-surface tic in b01c02. Fork B: "compound-hyphenated
  nouns ('ward-junction,' 'fever-cluster,' 'threshold-count,' 'junction-signature') at five per
  paragraph numb the ear." Fork C: "'threshold-stones' appearing four times in the first half
  threatens to become a term-of-art rather than a description." This is confirmed recurrence:

    Occurrence 1 — pl-2026-05-25-013 (b01c01 /and-stitch Phase 9 cold-read): "prose dense with
    hyphen-compound nouns (angle-wall, lane-mouth, chin-lift)... I had to reread the middle
    three times to confirm an event was happening." Filed as SOFT parking-lot item at first
    occurrence.

    Occurrence 2 — b01c02 postop Forks B + C (this dispatch): independent convergence from two
    readers across a chapter revised specifically to add substance-grounding. The depth-pass
    succeeded at substance delivery (Fork A: all 12 dimensions DELIVERED) but introduced
    compound-noun saturation as a new prose-surface tic. The bones authored at /and-write
    revise --from-signals contain many compound-noun tokens by design; the stitcher renders them
    faithfully under the bone-faithfulness fence and Q9 cannot touch them. From and-stitch.md
    Phase 7/Phase 1 scene-window Q9 anti-jargon rule: "Q9 hits in bones themselves are upstream
    faults: emit FAULT-BONE-AUDIT-MISS and render the bone as-is — Phase 7 cannot REWORD a
    bone-content compound without violating bone-faithfulness."

  The root cause is upstream: the screen-writer at Phase 1 has no guidance about compound-noun
  economy in SVO authoring, and Phase 6 has no AP-SCAN check for compound-noun density per
  bone-cluster. Every compound noun the bone-author introduces in a bone's SVO subject/object
  appears verbatim in the rendered draft; there is no downstream gate capable of thinning them
  without violating bone-faithfulness.

  This is a process gap at /and-write Phase 1 (authoring guidance absent) + Phase 6 (AP-SCAN
  absent). Options (a) Phase 7 Q9 tightening and (b) /and-stitch Phase 1 variance discipline
  are both structurally unable to fix bone-authored compound nouns and are not proposed.

  Note on content-architecture tension: compound nouns are not categorically bad for this
  project's surveillance-architecture vocabulary — `ward-junction`, `fever-cluster`,
  `junction-lane` are load-bearing terms that enact the feed-geography the substance contract
  requires. The problem is aggregate density: the same 3-4 roots (`junction`, `fever`,
  `threshold`) recycled across 47 bones saturate the paragraph-level register. The proposed
  check targets recycling density, not raw compound-noun count.
evidence_refs:
  - "active-project/staff/reviews/pleasure-read-b01-c02-2026-05-26-postop.md — §4 Voice: 'Compound-hyphenated nouns at five per paragraph numb the ear'; §2 attention drift: 60 lines of compound-noun tic-recycling"
  - "active-project/staff/reviews/audience-worm-canon-pedant-b01-c02-2026-05-26-postop.md — §4 Disliked: 'threshold-stones appearing four times in the first half threatens to become a term-of-art'"
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-05-25-013 (b01c01 /and-stitch Phase 9 cold-read: 'prose dense with hyphen-compound nouns'; filed SOFT at first occurrence, status: open)"
  - ".claude/commands/and-stitch.md — Phase 7 / scene-window §Q9 anti-jargon: 'Q9 hits in bones themselves are upstream faults: emit FAULT-BONE-AUDIT-MISS; render as-is — Phase 7 cannot REWORD without violating bone-faithfulness'"
  - ".claude/commands/and-write.md — Phase 6 HARD/SIGNAL table: 'register-as-mannerism (verb-object pair ≥3 occurrences)' — existing analog this change extends"
recurrence_count: 2
proposed_diff: |
  CHANGE 1 — .claude/commands/and-write.md, Phase 1 step 5 (SVO discipline):

  After the existing bullet "Author with full SVO discipline. Speech bones use `speaks to` form."
  add:

    **Compound-noun economy.** Hyphenated compound nouns in SVO subjects and objects
    (e.g. `ward-junction`, `fever-cluster`, `junction-lane`) appear verbatim in rendered
    prose under the bone-faithfulness fence — the stitcher cannot thin them. Ration compound
    nouns to the 2-3 per scene that are most load-bearing for the architecture or substance
    contract. For remaining spatial/object references, prefer simple English nouns or
    definite-article forms where unambiguous in context (`the junction`, `the corner`,
    `the lane`). A paragraph-cluster of 4+ distinct hyphenated compound nouns signals
    over-nomination; the screen-writer should prefer the load-bearing 1-2 and simplify
    the rest.

  CHANGE 2 — .claude/commands/and-write.md, Phase 6 HARD/SIGNAL classification table:

  Add one new SIGNAL entry (after `register-as-mannerism`) in the SIGNAL row:

    | compound-noun-density-per-cluster: count of distinct hyphenated compound
    nouns appearing across any 5-consecutive-bone window in the scene exceeds 3
    (i.e. ≥4 distinct compound nouns in a rolling 5-bone window) | SIGNAL |

  Disposition: SIGNAL (records, passes). The auditor reports: "compound-noun density SIGNAL:
  bones @<A>–@<B> contain <N> distinct hyphenated compound nouns in a 5-bone window
  (<list them>). Consider simplifying 1-2 to natural English." The bone-author may accept
  (SIGNAL graduates to HARD on second chapter-level occurrence across the project) or
  remediate in revise mode.

  SCOPE NOTE:

  This check applies only to compound nouns in bone SVO subjects and objects — the `subject`
  and `object` fields of the bones file. It does not apply to cost_ledger_anchor slugs, axis
  names, or actor slugs. The intent is compound-noun density as perceived by a reader of
  rendered prose, not metadata density.

  "Distinct" means unique hyphenated-noun tokens, not unique roots. `ward-junction` and
  `junction-lane` are two distinct tokens even though they share the `junction` root; but
  `ward-junction` appearing five times across 5 bones counts as 1 distinct token. Recycling
  of the same token is a separate concern addressed by the existing `register-as-mannerism`
  SIGNAL for verb-object pair recurrence — the two checks are complementary, not redundant.

  THRESHOLD CALIBRATION NOTE:

  The 5-bone window / ≥4 distinct tokens threshold is calibrated against b01c02's evidence:
  Fork B named "five per paragraph" as the point of ear-numbing. A 5-bone window approximates
  a rendered paragraph in scene-window mode. ≥4 (not ≥5) gives one bone of headroom for a
  chapter with unusually high architectural vocabulary load. If the threshold produces false
  positives on c03+ chapters that are not prose-surface concerns, adjust to ≥5 before
  graduating the SIGNAL to HARD.

  PARKING-LOT CROSS-REFERENCE:

  pl-2026-05-25-013 points its resolution_suggestion at "future spec edit on stitcher persona /
  Phase 7 Q9 rubric" — that target is the wrong layer. If this proposal is accepted,
  pl-2026-05-25-013's resolution_suggestion should be re-stamped to point at /and-write Phase 1
  + Phase 6 instead, and the item stamped resolved_by this proposal's implementation. The
  parking-lot item remains open pending implementation.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0008

```yaml
id: PROP-0008
created_at: 2026-05-27T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/auditor-b01c04-substance-2026-05-27.md
  source_verdict: "FAIL — fault-001 HARD (POV violation, literal-reading of cond-taylor-pov-behavior auditor-use clause)"
target:
  type: agent-card
  path: cards/conditions/cond-taylor-pov-behavior.card.md
  section: "POV Scope — First Person Only + Interaction Notes / For auditor use"
change_type: modify
rationale: |
  The auditor at /and-substance chapter b01c04 Phase 5 fired fault-001 HARD on POV
  violation: all three c04 scene chunks are third-limited (named-subject SVO: "Taylor
  walks," "She does not review") in direct violation of the card's text: "Every chapter
  defaults to first-person Taylor" and "Flag any chapter not marked interlude that is
  not in Taylor's first-person."

  Investigation confirmed the finding is a false positive. c01/c02/c03 scene chunks in
  showrunner memory.md are ALL third-limited; rendered prose at draft/b01-c01.md through
  b01-c03.md is first-person throughout. The first-person transformation is the
  responsibility of /and-write (which uses third-person-named-subject SVO for mechanical
  clarity at the bone layer) and /and-stitch (which renders to first-person prose). The
  chain's consistent operating convention for three prior chapters, confirmed by three
  prior Phase 5 auditor passes that did not flag this, is that "first-person" governs
  rendered prose, not planning-layer chunks or bones.

  The card's "For auditor use" clause does not qualify which production layer the
  first-person requirement applies to. A literal reading of "Flag any chapter not marked
  interlude that is not in Taylor's first-person" catches scene chunks and bones files
  as well as rendered prose — which is not the chain's intent and not the interpretation
  that would produce correct results. The card also does not mention that planning chunks
  and bones use third-person-named-subject SVO by pipeline convention.

  This is not a first-occurrence taste flag requiring recurrence before proposal. It is
  a card-text specification gap that produces a false-positive HARD on every correctly-
  authored scene-chunk pass in the project. Future chapters c05+ will trip this same
  HARD on identically-authored chunks unless the card is clarified. The recurrence is
  not probabilistic — it is certain on every future invocation of /and-substance chapter
  Phase 5. The fix is S-cost (two qualifying sentences added to one card). The cost of
  not fixing is a standing false-positive HARD block on all future substance-chapter
  passes, requiring an explicit override and admin process-critic dispatch each time.
evidence_refs:
  - "active-project/staff/reviews/auditor-b01c04-substance-2026-05-27.md — fault-001: auditor cites cond-taylor-pov-behavior 'Every chapter defaults to first-person Taylor' against third-limited chunk prose (lines 22-50)"
  - "cards/conditions/cond-taylor-pov-behavior.card.md — §POV Scope — First Person Only: 'Every chapter defaults to first-person Taylor'; §Interaction Notes: 'Flag any chapter not marked interlude that is not in Taylor's first-person' — neither clause names which production layer"
  - "active-project/staff/showrunner/memory.md — c01/c02/c03 scene chunks all third-limited in memory (confirmed by DEC-0028 context); rendered draft/b01-c01.md through b01-c03.md all first-person throughout"
  - "staff/admin/decisions.md — DEC-0028: 'OVERRIDE fault-001 (convention established; prior audits accepted; card text ambiguous) ... the card's language does not exclude the planning layer. This is a card-text failure, not a chain failure. Flagging for process-critic card-text clarification closes the audit gap for future chapters.'"
recurrence_count: 1
proposed_diff: |
  In cards/conditions/cond-taylor-pov-behavior.card.md, §POV Scope — First Person Only,
  after the paragraph "Every chapter defaults to first-person Taylor.":

  Add a new paragraph:

    **Layer scope.** "First-person throughout" applies to **rendered prose** — the
    chapter draft delivered by `/and-stitch`. Planning chunks (scene chunks authored by
    `/and-substance chapter`) are conventionally written in third-limited named-subject
    form ("Taylor walks," "She does not review") for screen-writer clarity; this is
    pipeline convention, not a POV violation. Bones (authored by `/and-write`) use
    third-person-named-subject SVO form by mechanical design. The first-person
    transformation is the responsibility of `/and-write` Phase 1 (which works in named-
    subject SVO) and `/and-stitch` render phases (which produce the final first-person
    prose). Chunk-layer and bones-layer third-limited form is NOT a POV violation.

  In cards/conditions/cond-taylor-pov-behavior.card.md, §Interaction Notes,
  in the "For auditor use" paragraph, qualify the first-person flag:

  Replace:
    "Flag any chapter not marked interlude that is not in Taylor's first-person."
  With:
    "Flag any chapter not marked interlude whose **rendered draft** (the `/and-stitch`
    output at `draft/<book>-<chapter>.md`) is not in Taylor's first-person. Do NOT flag
    scene chunks or bones files for being in third-person named-subject form — this is
    pipeline convention at the planning and bone-authoring layers; the first-person
    transformation happens at `/and-stitch`. The auditor's POV check applies to the
    rendered draft layer only."

cost_estimate: S
status: applied
triaged_at: 2026-05-27T00:00:00Z
triaged_by: user (principal)
disposition_note: |
  Accepted in full. Both edits applied to
  cards/conditions/cond-taylor-pov-behavior.card.md AND its
  active-project override at active-project/warehouse/
  cond-taylor-pov-behavior.md. Future /and-substance chapter
  Phase 5 auditor passes should no longer fire fault-001 on
  third-limited scene chunks; the rule now explicitly applies
  to the rendered-draft layer only.
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0009

```yaml
id: PROP-0009
created_at: 2026-05-27T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c04-bone-gate-redo.md
  source_verdict: "PASS — 0 HARD, 3 SIGNAL (all ACCEPTED): prior cycle produced 45 HARDs from c03 cascade-budget contamination; Phase 1 redo with corrective brief (c02-reference) cleared to 0 FAULT-FORM"
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition (screen-writer dispatch brief)"
change_type: modify
rationale: |
  At b01c04 Phase 2, the auditor returned 45 HARD findings (33 FAULT-FORM-MODIFIER + 12
  FAULT-BONE-DELTA-MALFORMED) on 38 bones. Root cause: the screen-writer used c03 bones as a
  cadence model. c03 ran under cascade-budget with Phase 2 form-auditing skipped, leaving c03
  in a state where PP-heavy SVOs and 0.5-magnitude pair-splits were never corrected. c03 taught
  the wrong pattern. DEC-0030 identified c02 (post-revise, fully Phase-2-audited) as the only
  correct canonical reference in the project.

  The corrective brief for Phase 1 redo explicitly named c02 as the reference and warned
  against c03. The redo produced 0 FAULT-FORM (confirmed by the re-audit that became the
  triggering bone-gate report). The fix worked — but it required a user-proxy dispatch (DEC-0030)
  and a full Phase 1 redo cycle because the Phase 1 dispatch brief had no standing guidance on
  which prior chapter's bones to use as a cadence reference.

  The structural gap: Phase 1's screen-writer dispatch currently receives prior-chapter bones
  as context for cadence modeling, with no instruction constraining which chapters are safe to
  reference. Cascade-budget chapters (those that skipped Phase 2 auditing) are unreliable SVO-form
  exemplars and will recur — any future cascade run will produce a chapter whose Phase 2 audit
  was skipped. Without a standing instruction to prefer the last fully-audited chapter over
  any cascade-budget chapter, the screen-writer will pick whatever is most recent or provided
  and risk repeating the contamination.

  DEC-0030 explicitly deferred a formal proposal "until outcome TBD" (Phase 1 redo outcome).
  The outcome is now confirmed: the corrective brief prevented recurrence. The deferred
  proposal is now ready to author. This is a process modification, not a content failure —
  a stricter version of the existing Phase 1 brief (with explicit cadence-reference guidance)
  would have prevented the 45-HARD cycle.
evidence_refs:
  - "active-project/staff/auditor/write-b01c04-bone-gate-redo.md — PASS verdict after redo; 0 FAULT-FORM on 39 bones; confirms corrective brief (c02-reference, no-c03) fixed the contamination"
  - "staff/admin/decisions.md — DEC-0030: root cause identified as c03 cascade-budget contamination; Phase 1 redo with c02-reference authorized; proposal deferred pending outcome"
  - ".claude/commands/and-write.md — Phase 1 screen-writer dispatch (no cadence-reference guidance currently; forbid-loading block names other chapters' bones files as forbidden from Phase 1 loading, but does not distinguish audited from unaudited references when prior chapters are legitimately provided as context)"
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-05-27-001 (c03 contamination watch-item; filed at c04 start)"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-write.md, Phase 1 screen-writer dispatch brief section, add a
  cadence-reference guidance note after the existing forbid-loading block (or as a new
  sub-bullet in step 5 "Author with full SVO discipline"):

    **Cadence-reference rule.** When providing prior-chapter bones as a cadence / SVO-form
    model for the screen-writer, the dispatcher MUST prefer the most recently fully-audited
    chapter — specifically, the last chapter whose Phase 2 constraint audit returned clean
    (0 FAULT-FORM, 0 FAULT-BONE-DELTA-MALFORMED). Chapters that ran under cascade-budget and
    had Phase 2 auditing skipped are NOT valid cadence references for SVO-form or
    delta-magnitude discipline, regardless of their recency. If no prior chapter is fully
    audited (first-chapter case), fall back to `schemas/bones.schema.md` examples only.

    **Cascade-budget chapter identification.** A chapter whose `chapters[].cascade_budget:
    true` flag is set (or whose memory notes indicate Phase 2 was skipped) is a
    cascade-budget chapter. Do not load its bones file as a cadence reference.

    **Practical note for the corrective-brief pattern.** When a Phase 1 redo is triggered by
    systematic FAULT-FORM (≥10 form faults), the redo brief must name the canonical reference
    chapter explicitly rather than leaving the screen-writer to infer from recency. The
    DEC-0030 corrective brief (explicitly: "reference c02 revised bones, NOT c03") is the
    model for this pattern.

  Additionally, in showrunner memory schema (schemas/showrunner-memory.schema.md) or in the
  Phase 7 emit block, add a `phase2_clean` boolean field to each chapter's record — set true
  when Phase 2 returns 0 FAULT-FORM and 0 FAULT-BONE-DELTA-MALFORMED; set false or absent for
  cascade-budget chapters. This makes the "is this chapter a safe cadence reference?" question
  answerable mechanically from memory rather than requiring the dispatcher to grep notes text.
  (The memory field is the lower-cost implementation path; a command-body comment naming
  the reference chapter is acceptable as a lower-overhead alternative if the memory-schema
  change is deferred.)
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0010

```yaml
id: PROP-0010
created_at: 2026-05-27T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c04-bone-gate-redo.md
  source_verdict: "PASS — underlying cycle: chapter-contract capability +1.5 target with 1.0 magnitude floor forced 0.5+0.5 pair-splits, triggering 11 FAULT-BONE-DELTA-MALFORMED; resolved by bumping chapter target to +2.0 in DEC-0030"
target:
  type: command
  path: .claude/commands/and-substance.md
  section: "Chapter-level Phase 4/5 — per-scene substance contract validation"
change_type: add
rationale: |
  At b01c04, the chapter contract declared capability target +1.5 split across two scenes
  (s01 and s03). The bone magnitude floor is 1.0 per `chunk_targets.bone.delta_per_axis`.
  A +1.5 chapter target split into 2 scenes mathematically requires either a 1.0+0.5 split
  (with the 0.5 violating the floor) or a 1.0+1.0 split (rounding up to 2.0, deviating from
  contract). The screen-writer chose 0.5+0.5 per scene — which is both below floor and wrong
  as a sum. Resolution in DEC-0030: bump the chapter contract to +2.0 (1.0 per scene), which
  is structurally valid and consistent with the bone floor.

  The root cause is a design-time mismatch: `/and-substance chapter` authors per-axis targets
  at fractional granularity without checking those targets against the bone magnitude floor.
  When `target_delta_magnitude / scene_count < delta_per_axis_floor`, the screen-writer is
  placed in a structurally impossible position: any split satisfying the floor violates the
  contract, and any split satisfying the contract violates the floor. The substance chapter
  authoring phase has no gate that catches this before the screen-writer is dispatched at
  `/and-write`.

  This is a gate absence at the authoring layer: no existing phase in `/and-substance chapter`
  validates per-scene granularity against the bone floor. A pre-flight check at Phase 4 or
  Phase 5 of `/and-substance chapter` would catch this before `/and-write` is invoked, allowing
  the chapter contract author to adjust targets rather than forcing DEC-0030-style mid-redo
  corrections.

  Recurrence is foreseeable: any chapter with an odd total target split across an even scene
  count, or any fractional target derived from book-level deltas, can produce the same
  tension. This is not a tail-case — book-level fractional targets (e.g. capability +2.5 split
  across 3 chapters) naturally produce per-chapter fractions.
evidence_refs:
  - "staff/admin/decisions.md — DEC-0030: 11 FAULT-BONE-DELTA-MALFORMED traced to 0.5-magnitude pair-splits below the 1.0 floor; resolution was bumping chapter contract from +1.5 to +2.0; root cause named as 'chapter-contract author at /and-substance must pre-flight against the magnitude floor'"
  - "active-project/staff/auditor/write-b01c04-bone-gate-redo.md — PASS verdict after redo; additive cycle confirms the 2.0 target with 1.0-per-scene split is structurally valid"
  - ".claude/commands/and-write.md — Phase 2: FAULT-BONE-DELTA-MALFORMED classification: magnitude outside chunk_targets.bone.delta_per_axis is a HARD fault"
  - "schemas/showrunner-memory.schema.md — chunk_targets.bone.delta_per_axis field (the floor the chapter contract must pre-flight against)"
recurrence_count: 2
recurrence_refs:
  - "active-project/staff/auditor/write-b01c06-bone-gate.md — signal-001 + signal-002: moral_legibility_to_self scene-aggregate target +0.5 (fractional residual after scene distribution); bone-floor 1.0 forced over-delivery to +1.0; accepted-with-rationale; stakes-axis tie (moral_framework=moral_legibility at 1.0 each) is a direct consequence of the same fractional-target-floor collision. Second chapter exhibiting this exact structural pattern (b01c04 was first). No HARD fired; accepted path worked. Confirms recurrence is predictable on any chapter with fractional scene residuals."
proposed_diff: |
  In .claude/commands/and-substance.md, in the chapter-level authoring phase (Phase 4 or
  Phase 5 — whichever phase persists the per-scene substance contract to memory), add a
  pre-flight check:

    **Magnitude-floor pre-flight (new check, fires before persisting scene contracts).** For
    every axis in `axes_in_motion[]` across all scenes, verify:

      (scene's target_delta_magnitude) >= chunk_targets.bone.delta_per_axis.floor

    If any scene's per-axis target falls below the bone floor, the chapter contract cannot
    be satisfied without a floor violation at /and-write. Surface the conflict immediately:

      SUBSTANCE-CONTRACT-FLOOR-CONFLICT: axis <axis> in scene <slug>
        target_delta_magnitude: <X>
        bone.delta_per_axis floor: <floor>
        required adjustment: raise target to ≥<floor>, OR consolidate scenes so the
          full target is delivered in fewer scenes each with ≥<floor> per-axis target.

    This is a WARNING (not a HARD abort): the chapter author may legitimately choose to
    consolidate scenes or round up. But the conflict must be surfaced at contract-authoring
    time, not at /and-write Phase 2 after bones have been authored against the broken contract.

    The check also applies to the aggregate: if `sum(axes_in_motion[].target_delta_magnitude
    across all scenes for <axis>)` is not achievable by any integer ≥floor combination
    summing to ≤total, flag it.

  Cost estimate: S (one new validation block in one command phase; no schema change required;
  chunk_targets.bone.delta_per_axis is already readable from memory).

  NOTE: this check should also be applied at /and-substance book when per-chapter targets
  are first allocated (if the book-level screen-writer allocates fractional chapter targets
  from a book total), but the chapter-level check is the minimum-blast-radius addition since
  chapter-level is where per-scene allocation happens. Book-level pre-flight can be added
  separately if recurrence at the book phase is observed.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0011

```yaml
id: PROP-0011
created_at: 2026-05-27T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c04-bone-gate-redo.md
  source_verdict: "PASS — prior cycle: 5 HARD HELD-AXIS-NOT-WITNESSED (s01 capability, s02 political_register-prot, s03 moral_framework, s03 political_register-prot, s03 position-prot-rise); resolved by additive cycle adding 5 dedicated held bones"
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition, step 2 (held-bone shape description)"
change_type: modify
rationale: |
  At b01c04 Phase 6, the auditor returned 5 HARD HELD-AXIS-NOT-WITNESSED findings — one per
  held axis declared in the scene contracts (capability, political_register-prot ×2,
  moral_framework, position-prot-rise). The screen-writer authored moving and chatter bones
  cleanly but did not author dedicated held bones for any of the chapter-contract-declared
  held axes. The fix was an additive cycle (5 bones added; existing bones unchanged;
  chapter substance unchanged).

  The Phase 1 spec already states the requirement: "Held axes contribute zero by definition
  and must each have at least one bone in the scene with that axis in its bone-level
  axes_held[]." This rule is embedded in the description of the held-bone shape, as part
  of the explanation of the three bone shapes. It is not presented as a numbered authoring
  step or a checklist item the screen-writer must verify before declaring Phase 1 complete.

  The screen-writer correctly read and applied the moving-bone and chatter-bone rules (no
  FAULT-FORM-MODIFIER on those shapes). The held-bone requirement was missed — not because
  the rule doesn't exist, but because it's buried in a shape-description paragraph rather
  than presented as an explicit authoring obligation with a completion criterion. Adding a
  numbered checklist step ("Before Phase 1 is complete, verify that for every axis in
  scenes[].substance_delta.axes_held[], at least one bone in that scene carries that axis in
  its bone-level axes_held[]") makes the requirement a completion gate, not a background fact.

  Recurrence_count = 1 (first time HELD-AXIS-NOT-WITNESSED fired systematically across
  multiple held axes in a chapter). Non-catastrophic (additive cycle resolved without
  modifying existing bones). Proposing modify at first occurrence because: (a) the
  requirement exists but is structurally under-specified in the task list; (b) the fix is
  a single sentence addition to Phase 1; (c) the failure mode is deterministic — any chapter
  with held axes whose screen-writer focuses on moving/chatter bones first will hit this
  unless the requirement is an explicit completion-gate.
evidence_refs:
  - "active-project/staff/auditor/write-b01c04-bone-gate-redo.md — PASS after additive cycle; 5 held bones added to satisfy HELD-AXIS-NOT-WITNESSED on 5 axes across 3 scenes; no existing bones modified"
  - ".claude/commands/and-write.md — Phase 1 step 2 held-bone shape description: 'Held axes contribute zero by definition and must each have at least one bone in the scene with that axis in its bone-level axes_held[]' — requirement exists but is embedded in shape description, not in numbered authoring steps"
  - ".claude/commands/and-write.md — Phase 6 HELD-AXIS-NOT-WITNESSED: 'for each entry in scenes[].substance_delta.axes_held[], at least one bone in the scene must have that axis in its bone-level axes_held[]' — the gate exists and fires correctly; the gap is at the authoring brief, not the gate"
  - "active-project/staff/auditor/write-b01c06-bone-gate.md — fault-001 HELD-AXIS-NOT-WITNESSED: political_register-prot s01; resolved by assigning axis to existing bone s01n02 (no new bone required); same failure class at lower severity than c04 (1 axis vs 5; trivial fix vs additive cycle). Confirms the pattern is recurrent across chapters with held axes in the contract."
recurrence_count: 2
proposed_diff: |
  In .claude/commands/and-write.md, Phase 1, after step 4 (scene_conflict / opposing-force
  rule), add a new numbered step 4a (or append to step 4 as a sub-bullet):

    **4a. Held-axis coverage verification (completion gate, before declaring Phase 1 done
    for a scene).** For every axis listed in `scenes[<slug>].substance_delta.axes_held[]`,
    verify that at least one bone in the scene's bone set carries that axis in its
    bone-level `axes_held[]`. This is NOT optional — every declared held axis must have
    a witnessing bone, or the Phase 6 bone-gate will return HARD `HELD-AXIS-NOT-WITNESSED`.
    Complete this check before moving to Phase 2; additive cycles at Phase 6 (after the
    full five-pass SVO pipeline) are costly. The check is mechanical:

      For each axis A in scenes[slug].substance_delta.axes_held[]:
        assert count(bones[slug] where axes_held[].axis == A) >= 1
      If any axis A has count == 0: author a held bone for A before exiting Phase 1.

    Holding discipline for the held bone: the SVO must enact stillness-against-pressure
    for axis A (see step 2 held-bone description). The rationale must name the discipline.
    The bone is a normal held bone — it may serve double duty (also a grounding bone or
    a chatter bone) if its SVO is concretely physical and the axes_held entry is present.

  The existing held-bone description in step 2 is unchanged — this step 4a is the
  completion checkpoint that operationalizes the requirement stated there. The information
  is not new; its placement as a named completion gate is the change.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0012

```yaml
id: PROP-0012
created_at: 2026-05-27T12:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-audience-gate-r3.md
  source_verdict: PASS-WITH-TASTE-FLAG-RESIDUE (Phase 5c dispatch; Pattern A — multi-token bracket spec/tool drift)
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 2 — FANIN: merge + cite-index / cite-index build step"
change_type: modify
rationale: |
  At /and-facets b01c04 Phase 2, build_cite_index.py failed to parse multi-token dialogue citation
  brackets emitted by /and-write Phase 7. /and-write emits `[X:1, X:2]` (comma-separated multi-token
  form) when a bone carries multiple dialogue citations; the cite-index builder's trailing-cite regex
  only handles single-token `[X:1] [X:2]` (space-separated sequential brackets). The mismatch caused
  inflight proto-lines to carry malformed or unresolved citation tokens until an inline fix
  (/tmp/fix_brackets.py) was applied to normalize the format before the build ran.

  This is a spec/implementation gap: /and-write's Phase 7 emit specification and build_cite_index.py's
  parser operate on different bracket conventions. The fix was applied inline for this chapter, but
  the gap will recur on any chapter where /and-write emits multi-dialogue-anchor bones (which is the
  expected case for action-dense scenes with overlapping dialogue). There is no standing normalization
  step between Phase 7 emit and Phase 2 cite-index build.

  Two candidate fixes: (a) constrain /and-write Phase 7 to always emit single-token sequential brackets
  (`[X:1] [X:2]`) rather than comma-separated multi-token form; (b) update build_cite_index.py to
  accept both forms. Either eliminates the gap; (a) is a spec change to /and-write; (b) is a parser
  change to the tool. The command body's Phase 2 cite-index step should also document the expected
  bracket format explicitly so the two sides of this interface share a declared contract.

  This is the same drift class as PROP-0008 (spec-vs-tool ambiguity, where the auditor's operational
  instruction and the tool's behavior diverged). Pattern repeating confirms the value of an explicit
  shared-format contract.
evidence_refs:
  - "active-project/staff/auditor/facets-audience-gate-r3.md — Pattern A trigger: multi-token bracket
    emit [X:1, X:2] vs. single-token parser expectation; inline fix via /tmp/fix_brackets.py at Phase 2"
  - ".claude/commands/and-facets.md — Phase 2 §cite-index build: `python3 active-project/staff/cite-index/build_cite_index.py <episode-slug>` — no bracket-format contract documented"
  - ".claude/commands/and-write.md — Phase 7 emit: dialogue-anchor bones carry [<character-slug>:<id>] citation tokens — multi-anchor emit format unspecified"
  - "staff/admin/process-proposals.md — PROP-0008 (spec vs tool ambiguity class: auditor CONSTRAINT scan scope not matching tool behavior — same class of drift)"
recurrence_count: 1
proposed_diff: |
  OPTION A (preferred for minimal downstream blast radius) — constrain /and-write Phase 7 emit format:

  In .claude/commands/and-write.md, Phase 7 emit section, add a bracket-format note:

    **Citation token format.** When a bone carries multiple dialogue citations, emit sequential
    single-token brackets: `[X:1] [X:2]` (space-separated, one bracket per token). Do NOT emit
    comma-separated multi-token form `[X:1, X:2]`. The cite-index builder's trailing-cite regex
    is single-token-only; multi-token form is not parsed. Every dialogue-anchor token must appear
    in its own `[ ]` bracket with no comma inside.

  OPTION B (alternative) — update build_cite_index.py to accept both forms:

  In active-project/staff/cite-index/build_cite_index.py, update the trailing-cite regex to match
  both `[X:1]` and `[X:1, X:2]` forms. If comma-separated, split on `,\s*` and register each token
  separately. This makes the parser tolerant of both emit formats and eliminates the dependency on
  /and-write maintaining the single-token-only convention.

  SHARED ADDITION (both options) — add a bracket-format contract note to .claude/commands/and-facets.md
  Phase 2 cite-index step:

    **Bracket format contract.** The cite-index builder expects citation tokens in the form `[X:N]`
    (one token per bracket). Before running build_cite_index.py, verify the proto-lines file does not
    contain comma-separated multi-token brackets `[X:1, X:2]`. If found, normalize to sequential form
    before the build. (This should not occur if /and-write Phase 7 follows Option A above; this check
    is a defensive backstop.)

  Admin recommendation: Option A (spec-side constraint) is preferred because it makes /and-write's
  emit format self-documenting and removes the parser's need to handle multiple forms. Option B is
  acceptable if the principal prefers parser tolerance over emit-format strictness.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0013

```yaml
id: PROP-0013
created_at: 2026-05-27T12:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-audience-gate-r3.md
  source_verdict: PASS-WITH-TASTE-FLAG-RESIDUE (Phase 5c dispatch; Pattern B — R2 judge output-format discipline)
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 3 — R2 fanout dispatch brief / R2 judge output-format requirement"
change_type: modify
rationale: |
  At /and-facets b01c04 Phase 3, 5 of 7 R2 judges wrote decision-log prose into their inflight
  proto-lines files instead of the canonical citation-only format (citation tokens + KEEP/DELETE/ADD
  dispositions). The Phase 4 FANIN merge + cite-index rebuild reads inflight files expecting a clean
  citation-format structure; prose decision logs embedded in those files caused parse failures or
  ambiguous merge results. The main session had to reconstruct 5 inflight copies (memory, metaphor,
  exposition, dialogue-taylor, dialogue-jarvis) manually before the Phase 4 merge could proceed.

  The R2 dispatch brief tells judges to mutate their `_inflight-r2/` copy using citation-cascade logic
  (strip `[<own>:<id>]` tokens from proto-lines on DELETE). It does not state explicitly that the
  inflight proto-lines file must remain citation-format throughout — no prose commentary, no
  decision-log entries, no rationale text. Five of seven judges conflated "record my decision" with
  "write rationale into the file." The decision-log section belongs in the R2 decision shard
  (`staff/<facet>/r2-decision-shard.md`), not in the inflight proto-lines copy.

  This is a dispatch brief gap: the inflight file format constraint is implicit (it follows from the
  cite-index build's parse requirements) rather than explicit (a stated prohibition). Adding a one-line
  prohibition to the R2 dispatch brief prevents the 5-of-7 failure rate from recurring.
evidence_refs:
  - "active-project/staff/auditor/facets-audience-gate-r3.md — Pattern B: 5/7 R2 judges wrote prose
    into inflight files; 5 inflight copies reconstructed inline before Phase 4 merge"
  - ".claude/commands/and-facets.md — Phase 3 R2 dispatch brief: 'Citation cascade on the author's
    proto-lines copy. When the judge deletes <own>:<id>, it strips [<own>:<id>] from every proto-line
    in its _inflight-r2/ copy' — no prohibition on prose commentary in the file"
  - ".claude/commands/and-facets.md — Phase 4 §FANIN: merge + cite-index rebuild: parses inflight
    proto-lines by citation token; prose content causes ambiguous merge"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 3 R2 fanout section, in the dispatch brief for R2 judges,
  add after the "Citation cascade" instruction:

    **Inflight file format discipline.** The `_inflight-r2/` proto-lines copy is a structured
    citation-token file, not a decision log. The R2 judge MUST NOT write prose commentary, rationale
    text, or decision summaries into the inflight proto-lines file. Prose decision notes belong
    EXCLUSIVELY in the R2 decision shard at `staff/<facet>/r2-decision-shard.md`. The inflight
    proto-lines file must remain parseable by build_cite_index.py after all edits — which means
    only citation tokens, proto-line text, and the deletions / additions prescribed by the judge's
    KEEP/DELETE/ADD verdicts. A judge that writes prose into the inflight file will cause Phase 4
    merge failures that require manual reconstruction. Format discipline is the judge's responsibility,
    not the FANIN operator's.

  Additionally, consider adding a Phase 4 pre-merge validation step:

    Before running Phase 4 merge + cite-index rebuild, scan each inflight proto-lines file for
    prose-pattern indicators (multi-sentence blocks with no citation tokens on lines that should
    be proto-line entries). If found, abort and surface: "R2 inflight file for <facet> contains
    prose commentary at lines <N>–<M>. Strip prose before merge." This is a validation backstop
    that catches the format failure at the merge boundary rather than forcing manual reconstruction.
    Estimated cost: S (one validation scan added to Phase 4 pre-merge).

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0014

```yaml
id: PROP-0014
created_at: 2026-05-27T12:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-audience-gate-r3.md
  source_verdict: PASS-WITH-TASTE-FLAG-RESIDUE (Phase 5c dispatch; Pattern C — sidecar stale-ref + DEFERRED-TO-R2 placeholder)
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 3 — R2 fanout / R2 dialogue-judge dispatch brief"
change_type: modify
rationale: |
  At /and-facets b01c04 Phase 3, two related sidecar failures caused 4 audience reviewers to flag
  SIGNAL/HARD at Phase 5b across multiple cycles:

  (1) Stale bone-references in dialogue sidecars: after /and-write redo consolidated bones and
  renumbered @n07/n10 to @9, the dialogue drafts sidecars at `active-project/staff/dialogue-writer/
  <character-slug>.drafts.md` still carried old bone-reference numbers. The R2 dialogue-judge's
  dispatch brief specifies mutating the dialogue facet file (KEEP/DELETE/REWRITE per facet graph)
  but does not include sidecar update as a task. The R2 judge worked correctly on the dialogue file
  and left the sidecar unchanged — which is the correct interpretation of the current brief, but
  produces stale-ref artifacts that downstream audience reviewers treat as HARD constraint violations.

  (2) DEFERRED-TO-R2 placeholders in sidecars: dialogue drafts sidecars contained DEFERRED-TO-R2
  placeholder stubs (notes deferring authoring decisions to the R2 judge pass). These stubs were
  created at the dialogue-writing stage (Phase 1.5) and were intended to be resolved when R2 ran.
  The R2 dialogue-judge did not resolve them because the brief does not name sidecar placeholder
  resolution as a task. The stubs survived into Phase 5b as phantom content, confusing reviewers
  about whether entries were authored or pending.

  Both failures share the same root: the R2 dialogue-judge brief omits sidecar update from its
  task list. The judge correctly performs its primary task (KEEP/DELETE/REWRITE against the dialogue
  facet file using the facet graph as context) but the sidecar — which is a supporting artifact the
  judge has access to — is left in its pre-R2 state. A one-line task addition to the R2 dialogue-judge
  brief closes both gaps.
evidence_refs:
  - "active-project/staff/auditor/facets-audience-gate-r3.md — Pattern C: dialogue sidecars carrying
    n07/n10 stale refs after /and-write redo to @9; DEFERRED-TO-R2 placeholders surviving past R2;
    4 audience reviewers flagged as SIGNAL/HARD across cycles"
  - ".claude/commands/and-facets.md — Phase 3 R2 dialogue-judge dispatch brief: 'Full nine-facet
    graph + per-character dialogue files + cite-index in every dispatch payload... dialogue judges
    additionally receive the drafts sidecars for their characters' — sidecar UPDATE not listed as a task"
  - "staff/dialogue-writer/rubric-dialogue.md — sidecar format requirements (drafts sidecar carries
    card-signature + facet-license citations on chosen drafts)"
  - ".claude/commands/and-write.md — Phase 1.5 dialogue-writer dispatch: dialogue sidecars authored
    here; DEFERRED-TO-R2 placeholder pattern originated here as an authorized deferral mechanism"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 3 R2 fanout section, in the R2 dialogue-judge dispatch
  brief, add after the existing task list (KEEP / DELETE / REWRITE instructions):

    **Sidecar update (mandatory, same pass as dialogue file edits).** After completing all
    KEEP/DELETE/REWRITE verdicts on the dialogue facet file, the R2 dialogue-judge MUST also
    update the matching drafts sidecar at `active-project/staff/dialogue-writer/<character-slug>.drafts.md`:

      (a) **Stale bone-reference correction.** If the upstream /and-write run produced a redo or
          additive cycle that renumbered bones (detectable by checking the bones file's current bone
          IDs against any `@n<old>` references in the sidecar), update all sidecar bone-reference
          numbers to match the current bones file. The bones file is authoritative; any `@nNN` in
          the sidecar that does not match a current bone ID is stale and must be corrected.

      (b) **DEFERRED-TO-R2 placeholder resolution.** Scan the sidecar for any entries or fields
          containing `DEFERRED-TO-R2` or equivalent placeholder text. Resolve each placeholder:
          either fill in the deferred content using the facet graph context now available to R2,
          OR mark the entry as `NOT-APPLICABLE` with a one-line rationale. No DEFERRED-TO-R2
          placeholder may survive the R2 pass. Unresolved placeholders at Phase 5b are phantom
          content that confuses audience reviewers and produces false HARD findings.

    If the sidecar does not exist (first-run case where Phase 1.5 didn't produce one), skip this
    step with a note: "No sidecar found for <character-slug> — skipping sidecar update."

  SECONDARY CHANGE — staff/dialogue-writer/rubric-dialogue.md:

  Add a note in the sidecar format section:

    **DEFERRED-TO-R2 placeholder contract.** Placeholders marked DEFERRED-TO-R2 are authorized
    at Phase 1.5 (the dialogue-writing stage) only when the facet graph context needed to resolve
    the decision is not yet available. R2 is the mandatory resolution point. Any placeholder that
    survived R2 without resolution is a sidecar integrity fault. The R2 dialogue-judge is responsible
    for resolution; if the placeholder represents a decision that R2 cannot resolve (e.g., a dependency
    on a facet that was deleted in R2), the judge replaces it with NOT-APPLICABLE + rationale.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0015

```yaml
id: PROP-0015
created_at: 2026-05-27T12:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-audience-gate-r3.md
  source_verdict: PASS-WITH-TASTE-FLAG-RESIDUE (Phase 5c dispatch; Pattern D — cite-index regen wiping audit-fixes)
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 5 — AUDIT: single auditor dispatch / post-Phase-5 fixer protocol / cite-index rebuild after fixer"
change_type: add
rationale: |
  At /and-facets b01c04 Phase 5, the auditor found forward-cite faults (fault-002: [state:2]@9 and
  fault-003: [state:5]@22 in proto-lines, referencing state entries that appear later in the sequence).
  The fixer correctly stripped these citation tokens from the proto-lines file. However, a subsequent
  cite-index rebuild (triggered by the state-updates fixer as part of its mechanical-fix pass in
  cycle 3) re-added both [state:2]@9 and [state:5]@22. The cite-index builder reads upstream
  co-cite sources (loc-state, state-updates facet files) and propagates co-citations back into the
  proto-lines, overwriting any manual strips that preceded the rebuild.

  This is a deletion-marker permanence gap: when the auditor instructs the fixer to strip a citation
  token from proto-lines (as a HARD fault fix), that strip has no permanent record that prevents the
  cite-index builder from re-adding the token on next rebuild. The strip is ephemeral; the builder's
  co-propagation logic is authoritative. The two conflict silently, requiring re-detection and re-stripping
  at cycle-3 close.

  The consequence: any citation token stripped at Phase 5 as an audit fault (forward-cite, constraint
  violation, etc.) is vulnerable to re-addition by any subsequent cite-index rebuild in the same
  /and-facets run. The fixer's Phase 5 strip cannot survive a rebuild unless the deletion is recorded
  somewhere the builder checks.

  A deletion-marker mechanism — a lightweight manifest of citation tokens that the auditor has
  permanently invalidated — would allow build_cite_index.py to honor deletions and skip re-propagation
  of blacklisted tokens. This is a new mechanism (change_type: add); no existing gate handles it.
evidence_refs:
  - "active-project/staff/auditor/facets-audience-gate-r3.md — Pattern D: state-updates fixer cite-index
    regen re-added [state:2]@9 and [state:5]@22 after auditor fault-002/003 strip; required re-stripping
    inline at cycle-3 close"
  - ".claude/commands/and-facets.md — Phase 2 / Phase 4 cite-index rebuild: build_cite_index.py reads
    upstream facet sources and propagates co-cites to proto-lines — no deletion-marker input mechanism"
  - ".claude/commands/and-facets.md — Phase 5 §cap-burn handling: 'The cite-index builder reads this
    marker, auto-strips stale [<prefix>:<id>] tokens from proto-lines' — cap-burn already uses a
    deletion-marker mechanism (DELETED ENTRIES section); audit-fault strips do not use the same mechanism"
recurrence_count: 1
proposed_diff: |
  PRIMARY CHANGE — .claude/commands/and-facets.md, Phase 5 fixer protocol:

  After the auditor's Phase 5 strip of HARD citation tokens, the fixer (or the orchestrating phase)
  must record each stripped token in a deletions manifest. Add a step to the Phase 5 fixer protocol:

    **Deletion-manifest update.** When stripping a citation token from proto-lines as a Phase 5
    HARD fault fix, the fixer MUST also append the stripped token to the deletions manifest at
    `active-project/theater/facets/_cite-deletions-<book>-<chapter>.md`. Format per entry:

      - token: [<facet-prefix>:<id>]
        fault_id: fault-<NNN>
        stripped_at_phase: 5
        reason: <one-line rationale>

    This file is the authoritative list of citation tokens that have been permanently invalidated
    by audit fault findings. The cite-index builder reads this manifest before propagating any
    co-citation and MUST skip propagation of any token listed here.

  SECONDARY CHANGE — build_cite_index.py:

  Add a deletion-manifest check step at the start of the propagation pass:

    1. Check for `_cite-deletions-<book>-<chapter>.md` in the theater/facets/ directory.
    2. If present, load all `token:` entries as a no-propagate blacklist.
    3. During co-cite propagation: if a candidate citation token matches any entry in the blacklist,
       skip propagation silently (do not add the token to proto-lines). Log the skip to the
       cite-index build summary: "Skipped blacklisted token [<prefix>:<id>] at @<proto> (fault <NNN>)."

  SCOPE NOTE — relationship to existing cap-burn deletion mechanism:

  The Phase 5b cap-burn DELETE path already uses a similar mechanism: `DELETED ENTRIES` section
  in `_cite-index.md` marks cap-burned entries so the builder strips them. The proposed audit-fault
  deletion manifest is the Phase 5 analog: audit HARDs that require citation strip also need a
  permanent record the builder respects. The two mechanisms are complementary; consider unifying them
  into a single `_cite-deletions-*` format that both Phase 5 auditor and Phase 5b cap-burn write to.
  This unification is optional (cost M if unified vs. cost S if separate files) — the principal may
  implement as two separate mechanisms for simplicity.

cost_estimate: M
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0016

```yaml
id: PROP-0016
created_at: 2026-05-27T12:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/facets-audience-gate-r3.md
  source_verdict: PASS-WITH-TASTE-FLAG-RESIDUE (Phase 5c dispatch; Pattern E — cross-location-carry interpretation gap in rubric-sensory.md)
target:
  type: rubric
  path: design/shoot-v2/rubric-sensory.md
  section: "Per-location anchoring rule / old-state sourcing from prior locations"
change_type: modify
rationale: |
  At /and-facets b01c04 Phase 5b, sensory-disambiguation-pedant and sensory-old-state-reader
  gave opposite verdicts on sensory:2 @13 (TASTE-FLAG-001). After sensory:1 @1 was deleted in
  cycle 3, sensory:2 became the first sensory entry for its scene, with its old_state field
  sourcing from loc-state:1 (a different location from sensory:2's anchor location). The two
  specialist reviewers interpreted the rubric's per-location anchoring rule differently:

    sensory-old-state-reader: cross-location carry from loc-state:1 to loc-state:3 is standard
    pattern — when the character moves between locations, the old_state for a new sensory entry
    legitimately references the previous location's state. ACCEPTed.

    sensory-disambiguation-pedant: strict per-location rule — old_state must source from the
    same location as the sensory entry's anchor location. Using a prior location's loc-state as
    old_state is a per-location anchoring violation. REVISEd.

  The rubric's per-location text is genuinely ambiguous: it does not state whether "per-location"
  means (a) the old_state must source from the same loc-state entry as the sensory entry's anchor,
  or (b) old_state may source from any prior loc-state in temporal sequence (including a previous
  location, as long as it is the most recent prior state before the anchor). The two interpretations
  produce opposite verdicts on a chapter-opening sensory entry after location transition.

  This ambiguity will recur on any chapter where a character moves between locations and the first
  sensory entry in the new location needs to reference what the sensory environment was in the
  previous location. This is a structurally common scenario (character transitions are a standard
  chapter-opening pattern in this project). Clarifying the rubric eliminates the disambiguation
  burden from both specialist reviewers and prevents future TASTE-FLAG accumulation on a mechanical
  question that has a correct answer.
evidence_refs:
  - "active-project/staff/auditor/facets-audience-gate-r3.md — TASTE-FLAG-001: sensory-disambiguation-pedant
    REVISEd sensory:2 @13 (cross-location old-state from loc-state:1); sensory-old-state-reader ACCEPTed
    citing cross-location carry as standard pattern; rubric interpretation gap named explicitly"
  - "design/shoot-v2/rubric-sensory.md — per-location anchoring rule: states that sensory entries must
    be anchored per-location but does not specify old_state sourcing across location transitions"
  - ".claude/commands/and-facets.md — Phase 5b sensory specialist dispatch: sensory-disambiguation-pedant
    + sensory-old-state-reader both receive the rubric; divergent interpretation of same text"
recurrence_count: 1
proposed_diff: |
  In design/shoot-v2/rubric-sensory.md, §per-location anchoring rule (or the section governing
  old_state field requirements), add a location-transition clause:

    **old_state sourcing across location transitions.** When a sensory entry's anchor is the first
    sensory anchor in a new location (i.e., the character or POV has moved since the previous sensory
    entry), the old_state field MAY source from the most recent prior loc-state entry in temporal
    sequence — including a prior location's loc-state — if no loc-state entry exists yet for the
    current location. This is the "cross-location carry" pattern; it is permitted, not a per-location
    violation. Rationale: the old_state field represents "what the sensory environment was before this
    anchor" — which, at a location transition, is necessarily the previous location's state. Requiring
    old_state to source only from the current location's loc-state entry would force either (a) a
    vacuous old_state declaration ("no prior state at this location"), or (b) prohibition of sensory
    entries at location-transition anchors — both of which are worse than cross-location carry.

    **Per-location anchoring applies to: anchor location, modal categories, spatial specifics.** The
    per-location rule governs which location's sensory palette governs modal category selection and
    spatial anchoring text. It does NOT govern old_state sourcing, which follows temporal sequence
    rather than location-match. Reviewers applying the per-location rule to old_state field sourcing
    are misapplying it; the two concerns (location-specificity of the sensory reading vs. temporal
    continuity of the state reference) are orthogonal.

  This is a clarification, not a rule change. The sensory-old-state-reader's interpretation is
  being codified as the correct reading. The sensory-disambiguation-pedant's interpretation
  (strict same-location-only old_state sourcing) is being explicitly excluded. The clarification
  should be short enough to embed as a parenthetical in the existing old_state field description.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0001
created_at: 2026-05-26T00:05:43Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md
  source_verdict: ablation:1-low-rank-facet
target:
  type: rubric
  path: staff/exposition-author/rubric-exposition.md
  section: "Scope-specific render-as guidance / Form discipline"
change_type: modify
rationale: |
  The b01-c01 ablation cold-read ranked leave-out-exposition #1, beating full (#2), on one
  specific dimension: pacing through whitespace. The cold reader's closing observation
  identifies the cost mechanism — exposition's inline fold-in technique (em-dash-fold and
  inline-appositive render-as directives at first-mention anchors) packs glosses mid-sentence
  inside paragraphs that also carry crowd-compression, insect propagation, and world-fact
  setup. The result is a 200-word block where rescue dialogue cannot breathe. This is not
  evidence that exposition information is unwanted — full (#2) still beat nine other variants,
  and the preamble/prologue structure was praised as "the most complete" by the cold reader.
  The evidence points at the fold-in delivery mechanism at dialogue-adjacent or
  dialogue-containing anchors specifically, not at exposition in general.

  The rubric's "Scope-specific render-as guidance" section already ranks em-dash-fold as
  render-cost rank 2 (cheap) and states "use the cheapest render-as that the gloss content
  can fit." This heuristic steers exposition authors toward em-dash fold-ins as the default
  even when the anchor is immediately adjacent to a dialogue bone — exactly the case the cold
  read flagged. The rubric has no fence against em-dash fold-ins at dialogue-adjacent anchors.
  A modified gate that requires exposition authors to step up to parenthetical-aside or
  post-bone-clause (heavier render-as, more structural air) when the anchor is within ±2 bones
  of a speech bone, or alternatively defer the gloss to the next non-dialogue anchor, would
  have prevented the pacing collapse the cold reader observed.

  First occurrence; non-catastrophic; chapter passed Phase 9. Proposing modify (not delete)
  and waiting for recurrence before escalating to delete-class evidence.
evidence_refs:
  - "active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md — Closing observation (pacing through whitespace); Differential attribution (exposition delta −1); Bottom-of-list candidates"
  - "staff/exposition-author/rubric-exposition.md — Scope-specific render-as guidance table; Form discipline §cheapest-render-as heuristic"
  - ".claude/commands/and-stitch.md — Exposition fold-in mechanics (em-dash-fold / inline-appositive defined)"
recurrence_count: 1
proposed_diff: |
  In rubric-exposition.md, section "Scope-specific render-as guidance":

  Add a sub-rule under the render-as table (or as a named fence in "Form discipline"):

  **Dialogue-adjacent fold-in fence.** When a first-mention-* exposition entry's anchor is
  within ±2 bones of a speech bone (a bone whose SVO verb is "speaks" / "says" / "asks" or
  equivalent — visible in the bones file's dialogue-anchor notation), the author MUST NOT
  use `em-dash-fold` or `inline-appositive`. Instead:
    - Step up to `parenthetical-aside` (if the gloss fits ≤30 words as an aside), OR
    - Step up to `post-bone-clause` (if the gloss needs a full clause), OR
    - Defer the entry to the nearest non-dialogue anchor downstream (with a note:
      `deferred-from: @<original-anchor>`) — allowed only if the deferred anchor is within
      the same scene and the gap risk is not materially higher at the deferred point.

  Rationale to embed in the rubric: "Em-dash fold-ins at dialogue-adjacent anchors collapse
  the paragraph air that rescue / high-stakes dialogue depends on for pacing. Heavier render-as
  or deferral preserves the structural whitespace the stitcher needs to isolate speech acts."

  Audit class to add to "Audit classes (Phase 5 hooks)":
    **AP-SCAN — dialogue-adjacent fold-in.** For each `first-mention-*` entry with
    render-as `em-dash-fold` or `inline-appositive`, verify the anchor is not within ±2 bones
    of a speech bone. Violation → SIGNAL (HARD on second occurrence per chapter after
    recurrence is confirmed at project level).
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0017

```yaml
id: PROP-0017
created_at: 2026-05-28T00:00:00Z
created_by: admin process-critic
trigger:
  reason: audit-finding (codification anti-pattern)
  source_report: active-project/staff/ablation/multi-arm-vs-single-arm-b01-c04-audit-2026-05-27/README.md
  source_verdict: REVERT (URI-STITCH-CHERRY-PICK-DEFAULT-ON + URI-STITCH-MULTI-ARM-DEFAULT-ON both reverted)
  gate_path: .claude/commands/and-stitch.md#cherry-pick-default-off-audit-note
target:
  type: rule
  path: CLAUDE.md
  section: "Rules §13 — Admin process-critic mode / trigger enumeration"
change_type: add
rationale: |
  The process-critic trigger surface (Rule 13 tail-step hooks: /and-write Phase 6.5,
  /and-facets Phase 5c, /and-stitch Phase 9.5, /and-postop Phase 3.5, /and-review
  Common-Phase 4.5) covers chain-command non-PASS verdicts only. A session-authored
  URI spec-edit commit that cites an experiment conclusion falls entirely outside this
  trigger surface. No existing gate fires between "experiment surfaces tuning candidates"
  and "codification commit."

  Incident: experiment commit `2d525d2` (2026-05-27 02:57) concluded: "CONTINUE=no (same
  as multi-arm)... cherry-pick fires same walkout-severity peeves as pure-winner because
  cost-legibility lives in bones SVO authoring, not stitch paragraph composition" and surfaced
  A-E process-tuning candidates as "not yet codified." Twelve minutes later, commit `be7de51`
  (03:09) selected option D ("make cherry-pick a default arm") and codified it as default-on
  with the framing "strictly-better default" — directly inverting the experiment's stated
  conclusion. The codification also omitted the experiment's CONTINUE=no cold-read verdict
  from its evidence framing.

  The failure mode is structurally compound:
  (1) The tuning-candidates-list shape (A-E options, "not yet codified") provides a ready-made
      selection menu for the session that just ran the experiment. Sessions in that context have
      structural incentive to pick the option that confirms the work they just ran — confirmation
      bias is a predictable property of same-session codification, not a character flaw.
  (2) A 12-minute gap is normal in-session pacing — not an anomalous rush. The same pattern
      will recur on any future experiment that surfaces a candidates list in the same session.
  (3) The process-critic trigger surface fires on output failures (chain-command non-PASS
      verdicts), not on the meta-production activity of codifying those outputs into spec
      defaults. These are distinct: a chain-command FAIL tests whether the chapter was authored
      well; a URI default-change spec edit tests whether the pipeline itself is being authored
      faithfully to its evidence base. The latter requires independent-review discipline that the
      former's trigger surface does not supply.

  The proposed gate is minimum-blast-radius: one new trigger clause in CLAUDE.md Rule 13.
  No changes to command bodies, rubrics, or schemas. Expected trigger frequency: 0-2 per
  project-month given the observed pace of URI spec changes.

  Remediation confirmed: both URIs reverted; multi-judge verification (3/3 high-confidence)
  confirmed the experiment's actual finding; b01-c04 canonical draft restored to single-arm.
  Non-trivial spend wasted: multi-arm production run + tournament + cherry-pick + verification
  audit + principal-surfacing effort. Non-catastrophic in outcome but the trigger surface gap
  is structural and will recur.
evidence_refs:
  - "active-project/staff/ablation/multi-arm-vs-single-arm-b01-c04-audit-2026-05-27/README.md — audit finding; commit timestamps 2d525d2 (02:57) vs. be7de51 (03:09); misrepresentation traced; remediation confirmed; 3/3 multi-judge verification"
  - "Experiment commit 2d525d2 verbatim conclusion: 'CONTINUE=no (same as multi-arm)... cost-legibility lives in bones SVO authoring, not stitch paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate.' Candidates A-E: not yet codified."
  - "Codification commit be7de51 framing (verbatim from README audit trace): 'The 2026-05-27 b01-c02 cherry-pick experiment confirmed the cherry-pick path captures paragraph-level lift the pure-winner cannot... making paragraph the strictly-better default.' Omits CONTINUE=no. Inverts 'not predictive of continue-rate' as positive evidence."
  - "CLAUDE.md Rules §13 — current process-critic trigger surface: chain-command non-PASS verdicts + /and-postop convergence only; no trigger for URI default-change spec edits"
  - "staff/admin/decisions.md — DEC-0024 (multi-arm FAIL, OK) + DEC-0021 (Phase 9 cold-read FAIL b01c02, OK): prior process-critic dispatches on chain-command verdicts; cherry-pick experiment NOT dispatched (correct at the time; trigger gap identified here)"
recurrence_count: 1
proposed_diff: |
  In CLAUDE.md Rules §13, in the process-critic mode description, after the existing trigger
  enumeration (non-PASS verdicts from chain commands + every /and-postop convergence write),
  add a third trigger class:

    **URI default-change trigger.** When a session authors a URI-labeled spec edit that satisfies
    BOTH of the following conditions, the session MUST dispatch process-critic (mode: process-critic,
    trigger.reason: uri-default-change) before committing the edit:

      (a) **Default-change condition.** The spec edit changes a flag default from off to on,
          from opt-in to default-active, or enables a new pipeline feature as the default behavior.
          Spec edits that add opt-in flags, add documentation only, or clarify existing behavior
          without changing defaults are NOT subject to this trigger.

      (b) **Experiment-citation condition.** The spec edit's justification text (in the spec body,
          the commit message, or the URI rationale note) directly cites a specific prior experiment's
          conclusion as the primary basis for the default-on change.

    When both conditions hold: the session dispatches admin with mode: process-critic and additionally
    passes:
      - `experiment_conclusion_verbatim`: the experiment's stated conclusion, verbatim, not
        paraphrased by the session authoring the spec edit
      - `proposed_spec_text`: the draft spec edit text (the section being added or changed)
      - `gate_path`: the file and section being edited

    Process-critic reads the experiment conclusion and the proposed spec text. If the spec text
    accurately represents the conclusion (including any CONTINUE=no or negative-result language)
    and the proposed default-on is supported by the experiment's stated finding: returns OK (or
    PROCESS-CHANGE-PROPOSED if the change itself warrants a standalone proposal). If the spec text
    selectively cites only supporting fragments while omitting or inverting the experiment's stated
    conclusion: returns REVISE with the specific divergence identified. The session may not commit
    a default-on URI spec edit that has received REVISE until a revised spec text re-dispatches and
    returns OK or PROCESS-CHANGE-PROPOSED.

    **Derivative-default note.** When a second URI change is built on a first URI change as a
    dependency (e.g. "URI-B enables X because URI-A already enabled Y"), both URIs are subject to
    this trigger independently if both satisfy conditions (a) and (b). The parent URI's accuracy
    is not inherited by the derivative; the derivative must be dispatched on its own evidence.
    (This closes the URI-STITCH-MULTI-ARM-DEFAULT-ON class: the auto-alt-authoring URI was built
    on the misrepresented cherry-pick URI without its own independent experiment justification.)

    **Scope note.** This trigger does not cover: spec edits that add optional flags only; spec
    edits directed by explicit principal user-statements rather than session-inferred experiment
    conclusions; non-URI housekeeping edits. The discriminating question: "Does this edit change
    what happens by default, AND is a session-run experiment cited as the primary justification?"
    Both must be yes for the trigger to fire.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0018

```yaml
id: PROP-0018
created_at: 2026-05-29T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md
  source_verdict: FAIL (CONTINUE=NO; third consecutive cold-read FAIL on b01-c05)
  gate_path: .claude/commands/and-stitch.md#phase-9
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 9 Step 2 — Diff against intent (harness) / routing rules"
change_type: modify
rationale: |
  Phase 9's disposition rule is a binary: PASS → chapter terminal; FAIL → /and-write revise.
  This binary cannot discriminate between two structurally distinct FAIL sub-classes:

    CLASS A — Structural-incompleteness FAIL. The cold-reader cannot recover the chapter's
    central event or goal (criterion 6 summary does not map to chapters[slug].goal). The
    chapter has failed to deliver its own design. Bones-revise is the correct routing.

    CLASS B — Recovered-event design-inherent FAIL. The cold-reader CAN recover the chapter's
    central event and goal (criterion 6 summary maps to chapters[slug].goal). CONTINUE=no
    fires because the chapter's design properties — register, POV strategy, protagonist role,
    payoff shape — are inherently challenging for a first-time cold reader. Bones-revise cannot
    fix these properties because they ARE the substance contract. Routing to bones-revise
    produces a revise cycle that correctly addresses tractable complaints while leaving the
    dominant CONTINUE=no causes intact, then re-fails on those same causes.

  The b01-c05 triple-FAIL establishes this discrimination with precision:

    FAIL #1 (pre-revise): CLASS A — criterion 6 did not map to goal (cold-reader could not
    recover central event). /and-write revise --from-signals correct. Four bones added.

    FAIL #2 (post-revise --from-signals): central event recovered. CONTINUE=no fired on five
    complaints. DEC-0041 analyzed: one complaint tractable (sexual-assault read, complaint 4),
    four design-inherent. Principal chose to run third revise cycle (DEC-0042) targeting the
    tractable complaint.

    FAIL #3 (this dispatch): sexual-assault read REMEDIATED (the fix worked). Criterion 6
    summary correctly maps to the chapter goal: "surveillance-capable narrator watches a courier
    she's been tracking get beaten... her system won't stop flagging the route she set up —
    because she's the reason it happened." This is the goal. Yet CONTINUE=no fires again on:
      (1) stakes "stakes-shaped not stakes" — protagonist watches; design property of the
          chapter's substance contract (Taylor observes and files; not-deciding IS the irony)
      (2) "feed" mechanics unexplained — intentional per series register; c01-c04 also do not
          gloss it; a bones-revise glossing the feed would violate cross-episode contracts
      (3) causality "loose" — partially inherent to an interior/observational chapter
      (4) payoff "abstract, no decision" — the explicit substance (moral_legibility_to_self
          held; "filing-as-texture" protagonist_force; the not-deciding IS the substance)
      (5) dense prose / no named cast / central event happens to stranger / no clear want/fear
          — accumulation of design properties, not structural gaps

    Three revise cycles on b01-c05 have now confirmed the prediction DEC-0041 made at FAIL #2:
    a bones-revise cannot address the dominant CONTINUE=no class because that class IS the
    chapter's substance contract. The gate's detection is correct — it accurately identifies
    a chapter that is challenging for a cold reader. The gap is in the disposition rule, not
    the detection.

  The minimum-blast-radius fix is: add a Class B routing branch to Phase 9 Step 2. The
  discriminator between Class A and Class B is mechanical: compare the cold-reader's criterion
  6 one-line summary against chapters[slug].goal. If the summary maps to the goal (Class B),
  the harness flags "recovered-event FAIL" and routes to a disposition decision rather than
  mandatory bones-revise. The disposition decision routes to the principal (or admin user-proxy),
  not auto-mandated by the spec.

  This is change_type: modify on the disposition rules of an existing gate, not a new gate.
  The Phase 9 cold-read is not proposed for removal or loosening of its detection criteria.
  FAIL remains a FAIL. The change is to what the disposition does after classifying the FAIL.

  Prior precedent: DEC-0024 established a first-occurrence marker for "chapters FAIL Phase 9
  cold-read despite sound bones" — that candidate deferred to cross-chapter recurrence. DEC-0041
  explicitly named the recovered-event FAIL class and escalated without proposing. Now at third
  consecutive FAIL on the same chapter — with the design-inherent class isolated as the sole
  remaining residual after the tractable complaint was fixed — the class is precisely discriminated
  and a proposal is warranted.

  Recurrence_count: within-chapter this is occurrence 3; cross-chapter the class has appeared at
  b01c02 (DEC-0021 / DEC-0024, OK at first-occurrence) and b01c05 (three consecutive FAILs).
  Total class-level cross-chapter recurrence = 2 (two distinct chapters). The b01c05 data is
  the stronger case: three revise cycles confirmed the revise-loop cannot close the design-inherent
  class; the tractable complaint was isolated and fixed, leaving the class cleanly discriminated.
evidence_refs:
  - "active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md — FAIL #3: criterion 6
    summary maps to goal; CONTINUE=no on stakes-shaped-not-stakes / feed unexplained / causality
    loose / payoff abstract / dense prose accumulation — all design properties of substance contract"
  - "staff/admin/decisions.md — DEC-0041 (second-FAIL ESCALATE; identified Class A vs Class B
    discrimination; candidate process change surfaced for principal awareness; not proposed without
    authorization; principal responded with third revise cycle)"
  - "staff/admin/decisions.md — DEC-0042 (third revise scope: @13-@14 recast to close sexual-assault
    read; FAIL #3 confirms fix worked; design-inherent class is sole remaining residual)"
  - "staff/admin/decisions.md — DEC-0024 (b01c02 third Phase 9 FAIL, OK; cross-chapter marker;
    b01c05 is second cross-chapter occurrence of recovered-event design-inherent FAIL)"
  - ".claude/commands/and-stitch.md Phase 9 Step 2 — current routing: PASS terminal; FAIL /and-write
    revise; no recovered-event class check or Class B disposition branch"
recurrence_count: 3
proposed_diff: |
  In .claude/commands/and-stitch.md, Phase 9 Step 2 (Diff against intent — harness), modify
  the routing block at the end of Step 2:

  CURRENT routing:
    PASS → proceed to Step 3, then Step 4 (verdict: PASS).
    FAIL → route to /and-write revise.

  PROPOSED routing (replaces the FAIL arm only):

    **FAIL class discriminator.** Before routing, compare the cold-reader's criterion 6
    one-line summary against chapters[slug].goal (showrunner memory). Comparison is semantic:
      - Summary does NOT map to goal → FAIL Class A (Structural-incompleteness).
        Route to /and-write revise. Unchanged from current behavior.
      - Summary DOES map to goal → FAIL Class B (Recovered-event).
        Proceed to Class B disposition.

    **Class B disposition:**

      B1. Categorize each CONTINUE=no complaint:
          (i) Tractable — addressable by targeted bones-revise or stitch-layer fix without
              modifying the substance contract (register, POV, protagonist role, payoff shape).
          (ii) Design-inherent — a direct property of the substance contract.

      B2. If tractable complaints remain: route to targeted bones-revise scoped ONLY to (i)
          items. The revise brief MUST name design-inherent complaints and exclude them from
          scope. After revise + re-stitch, re-run Phase 9. If new FAIL is Class B with zero
          tractable complaints, proceed to B3.

      B3. If zero tractable complaints: dispatch to admin (user-proxy mode) with:
          - criterion 6 summary (confirmed maps to goal)
          - complaint list with design-inherent classification
          - Three options for principal:
              (S) Ship as PASS-DESIGN-INHERENT: substance contract properties that challenge
                  a cold first-timer are not defects for the series reader. Record verdict.
              (R) Revise substance contract: escalate to /and-substance chapter. High cost.
              (I) Iterate: authorize bones-revise knowing it rewrites design properties.
          - Admin default (goals + LTM): Option (S), given substance contract was approved
            upstream and design-property CONTINUE=no is not evidence the contract is wrong.

    **Memory additions (Step 4):**
      cold_read.fail_class: A | B
      cold_read.tractable_complaints: [...] (Class B only)
      cold_read.design_inherent_complaints: [...] (Class B only)

  SCOPE NOTE: Detection is unchanged. CONTINUE=no remains a FAIL. Class A routing (bones-revise)
  is unchanged. Only the Class B disposition changes: bounded classification + principal call
  replaces open-ended revise loop that cannot address design-inherent causes.

cost_estimate: M
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

## PROP-0019

```yaml
id: PROP-0019
created_at: 2026-05-29T00:00:00Z
created_by: principal (via main session, RCA conversation)
trigger:
  reason: rca-followup
  source_report: active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md
  source_verdict: SHIPPED-WITH-CAVEATS (b01-c05 three-FAIL trace; PROP-0018 already proposed)
  gate_path: .claude/commands/and-stitch.md#phase-9
target:
  type: command
  path: [.claude/commands/and-substance.md, .claude/commands/and-stitch.md]
  section: "and-substance Phase 5.5 (new); and-stitch Phase 8.5 (new)"
change_type: add
rationale: |
  Root-cause analysis of the b01-c05 three-FAIL trace identified two structural gaps that PROP-0018
  (Class A/B disposition discriminator) does not address:

    GAP-1: No upstream cold-read proxy. The Phase 9 cold-read is the cheapest discriminator of
    cold-reader-fit and the MOST EXPENSIVE place to fire it — after bones + facets + stitch have
    all committed. A chunk-level cold-read at /and-substance chapter would catch Class A
    (cause-chain gaps; missing connectives) and surface Class B (design-inherent risk) at the
    cheapest possible layer (~1 dispatch vs ~50 to remediate post-stitch). The chunk-level read
    cannot substitute Phase 9 — chunks read different than assembled prose — but it can drain
    most of what Phase 9 currently catches into a cheaper upstream layer.

    GAP-2: No assembled-prose review prior to Phase 9. Every reviewer prior to Phase 9 sees one
    of: (a) chunks + bones + facets (audience, dramatist, auditor, /and-review bones), or
    (b) per-scene fork-window prose (stitcher forks, Phase 7 sweep). NONE read the assembled
    preamble + body + facet-fold cohesion. The cold-reader at Phase 9 is the first and only
    fork that reads the assembled draft end-to-end. The FAIL #2 sexual-assault mechanism
    ("below the register I would have called human" at @14) was a stitch-layer rendering
    invention licensed by a generic-object bone + sensory-facet at the same anchor; no upstream
    fork saw the assembled prose with substance context to flag it. An informed reviewer reading
    draft + bones + facets + chunks would have flagged the COLD-READ-RISK before Phase 9 fired.

  The c05 three-FAIL trace specifically:
    - FAIL #1 (chunk-level cold-read would have caught): cause-chain gaps in scene-B + scene-C
      (Jarvis-routing destination, courier-recurrence-as-apparatus, recognition cause-chain).
      All bone-realizable; a cold-read on the chunk would have surfaced confusion. Catches at
      $1 not $50.
    - FAIL #2 (assembled-prose coherence would have caught): "below the register I would have
      called human" phrasing. The substance-aware informed reviewer reading the assembled draft
      would flag "this @14 rendering could read as sexual assault to a cold reader despite
      chunk authorizing enforcement." Stitch-revise fix (~2 dispatches) vs full revise cycle (~30).
    - FAIL #3 (chunk-level cold-read would have surfaced): design-inherent risk on substance
      contract approval. Principal disposition before bones commit instead of three revise cycles.
      Bundles with PROP-0018's Class B branch — chunk-level Class B disposition is the same logic
      applied upstream.

  This proposal is complementary to PROP-0018, not substitutive:
    - PROP-0018 adds Class A/B discrimination at Phase 9 (terminal-gate disposition rules).
    - PROP-0019 adds upstream gates that drain most of what reaches Phase 9. PROP-0018 still
      governs the residual Phase 9 FAILs that survive upstream catches.

evidence_refs:
  - "active-project/staff/reviews/coldread-b01-c05-2026-05-28.md — FAIL #1 (Class A)"
  - "active-project/staff/reviews/coldread-b01-c05-2026-05-28-revise.md — FAIL #2 (mixed; sexual-assault mechanism)"
  - "active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md — FAIL #3 (Class B design-inherent)"
  - "staff/admin/decisions.md — DEC-0041/0042/0043/0044 (three-revise-cycle disposition trail)"
  - ".claude/commands/and-substance.md Phase 5 — current chunk-quality review (substance-aware reviewers only; no cold-read proxy)"
  - ".claude/commands/and-stitch.md Phase 9 — current terminal gate (only assembled-prose read in chain)"
  - "RCA conversation (this session) — gap identification: audience reviewers see chunks/bones/facets; cold-reader sees assembled prose; no fork bridges the artifacts"

recurrence_count: 1  # first proposal of this gate-architecture class
status: open
proposed_diff: |
  TWO additive changes:

  ---

  ### Change 1: .claude/commands/and-substance.md — insert Phase 5.5 (chapter level only)

  After Phase 5 (Chunk-quality review), before Phase 6 (Persist), insert:

  ### Phase 5.5 — Chunk cold-read gate (chapter level only)

  Fires only at `chapter b<NN>c<MM>` invocation level. Skipped at series + book levels (which
  do not produce reader-facing chunks). Skipped if `chapters[<slug>].chapter_class: frame-coda`
  (Phase 6 substance bone-gate exemption is symmetric here).

  **Step 1 — Cold read (one general-purpose agent, uninformed).**

  Dispatch one general-purpose agent with the same 6-question cold-read prompt as
  /and-stitch Phase 9 Step 1, modified to read the chunk:

    > You are a first-time reader. You have been handed one chapter outline of a novel...
    > Read ONLY this file: active-project/staff/showrunner/b<NN>c<MM>-draft.md.
    > Answer the 6 questions...

  The agent reads ONLY the chapter chunk + scene chunks. NOT bones (no bones yet); NOT facets
  (no facets yet); NOT prior chapter chunks; NOT the substance contract.

  Persist agent output to `staff/reviews/chunk-coldread-<slug>-<timestamp>.md`.

  **Step 2 — Diff against intent + classify.**

  Compare cold-reader's criterion 6 summary against the chunk-author-declared `chapters[<slug>].goal`.

  - Summary maps to goal AND CONTINUE=yes → PASS-CHUNK. Proceed to Phase 6.
  - Summary maps to goal AND CONTINUE=no → CHUNK-CLASS-B (design-inherent risk surfaced at
    cheapest layer). Route to Step 3 admin user-proxy disposition.
  - Summary does NOT map to goal → CHUNK-CLASS-A (chunk has cause-chain / connective gaps).
    Route to Step 3 with revise-recommendation default.

  **Step 3 — Admin user-proxy disposition (non-PASS only).**

  Dispatch admin in user-proxy mode (per CLAUDE.md Rule 13) with:
    - Chunk text + scene chunks
    - Cold-reader's 6 answers
    - Classification (Class A / Class B)
    - Three options:
        (R) Revise chunk → /and-substance chapter <slug> revise. Cheapest fix at this layer.
        (P) Proceed with eyes open → record disposition; advance to Phase 6 with cold-read risk
            documented on chapters[<slug>].chunk_cold_read.
        (S) Substance-contract revision → /and-substance chapter <slug> redo with refined contract.

  Admin returns disposition; pipeline applies it. Class A admin default: (R). Class B admin
  default: (P) given substance contract was approved at /and-substance series.

  **Step 4 — Persist + memory.**

  Write to `chapters[<slug>].chunk_cold_read`:
    verdict: PASS-CHUNK | CHUNK-CLASS-A | CHUNK-CLASS-B | SHIPPED-WITH-RISK-RECORDED
    classification: A | B | n/a
    recovered_summary: <criterion 6>
    intended_goal: <chapters[<slug>].goal>
    report_path: staff/reviews/chunk-coldread-<slug>-<timestamp>.md
    disposition: <R | P | S>
    dispositioned_at: <iso>
    dispositioned_by: admin | principal

  Phase 9 (downstream /and-stitch) reads chapters[<slug>].chunk_cold_read.verdict at its
  Step 4 routing — a chunk-level CHUNK-CLASS-B that was dispositioned (P) carries forward to
  Phase 9 as "design-inherent already approved"; a recurring Phase 9 FAIL Class B on such a
  chapter ships terminal without re-asking principal (the chunk-level disposition already
  authorized the cold-read risk).

  ---

  ### Change 2: .claude/commands/and-stitch.md — insert Phase 8.5

  After Phase 8 (Finalize), before Phase 9 (Cold-read terminal gate), insert:

  ## Phase 8.5 — Assembled-prose coherence review (URI-STITCH-COHERENCE; advisory + routing-bearing)

  Fires after Phase 8 has written `draft/<book>-<chapter>.md` and BEFORE Phase 9 cold-read.
  Single dispatch. Substance-aware reviewer with full graph context, reading the assembled
  prose end-to-end. Catches what no upstream reviewer can: facet-fold cohesion and prose-layer
  cold-read-risk at the cheapest pre-terminal-gate layer.

  **Why this exists.** Every reviewer prior to this phase saw chunks + bones + facets (substance
  reviewers) or per-scene fork-window prose (stitch forks). None read the assembled preamble +
  body + facet-fold cohesion. The Phase 9 cold-reader is the FIRST AND ONLY fork to read the
  assembled draft, and at the most expensive recovery point. Phase 8.5 inserts a substance-aware
  reading of the same artifact one phase earlier.

  **Dispatch:** one general-purpose agent. Inputs (READ-ONLY):
    - `active-project/draft/<book>-<chapter>.md` (assembled)
    - `active-project/theater/bones/<book>-<chapter>.md`
    - `active-project/theater/facets/*-<book>-<chapter>.md` (all facets)
    - `chapters[<slug>].{goal, dramatic_shape, scenes[].chunk, scenes[].substance_delta, scenes[].scene_conflict}`
    - `chapters[<slug>].chunk_cold_read` (from PROP-0019 Change 1 if present)
    - Exposition entries with their `renders-as` directives

  **Mandate (three checks, in order):**

    1. **Weave check.** For each scene-window of the assembled prose, do the facet-folds tie
       together as one fabric? Or are exposition + bone-rendering + sensory + NI + memory
       arriving as discrete add-ons? Flag `WEAVE-GAP @<bone>` for visible seams.

    2. **Followability check.** Assuming a reader has read prior chapters in the series, can
       they follow this chapter's narrative arc? Where does a causal hand-off between facets
       fail (preamble names X; body never reconnects to X)? Flag `FOLLOWABILITY-BREAK @<bone>`.

    3. **Cold-read-risk surface.** Reading the assembled prose with substance context, flag
       any span that would PLAUSIBLY misread to a first-time cold-reader despite being
       substance-correct. The reviewer cites the misread vector + the substance-correct reading
       + the routing recommendation. Flag `COLD-READ-RISK @<bone>`.

  **Output:** classified findings to `staff/reviews/coherence-<slug>-<timestamp>.md` + summary
  to render-log under `## Phase 8.5 — coherence review`.

  **Routing:**
    - 0 findings → PASS. Proceed to Phase 9.
    - WEAVE-GAP / FOLLOWABILITY-BREAK findings → SOFT-BLOCK. Route per finding:
        * stitch-layer (per-scene re-render): re-dispatch the offending scene's Phase 1 fork
          with the finding cited; re-run Phases 2-8 on the changed scene only.
        * exposition-layer (gloss missing or stale): re-dispatch exposition-author at /and-facets
          for the named entry; re-run Phase 0.6 preamble assembly.
        * bones-layer (rationale-named element missing from prose): route to /and-write revise
          on the named bone.
    - COLD-READ-RISK findings → ADVISORY by default; SOFT-BLOCK if the finding cites a
      high-misread-confidence vector (reviewer signals "would-likely-fire-at-Phase-9"). On
      SOFT-BLOCK: route to the same per-layer routing above before Phase 9.

  **Memory writes:**
    chapters[<slug>].coherence_review:
      reviewed_at: <iso>
      verdict: PASS | SOFT-BLOCK-RESOLVED | SOFT-BLOCK-UNRESOLVED-PROCEED-ANYWAY
      findings: [...]
      report_path: staff/reviews/coherence-<slug>-<timestamp>.md

  **Cap:** Phase 8.5 may trigger at most ONE round of stitch/exposition/bones revise before
  Phase 9 fires regardless. The gate's purpose is to drain pre-Phase-9 catches; it is not a
  loop. Unresolved findings carry forward to Phase 9 + render-log; admin process-critic fires
  on Phase 9.5 with the coherence-review report as additional context.

  ---

cost_estimate: M
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

### PROP-0019 — VALIDATION ADDENDUM (2026-05-29)

```yaml
addendum_to: PROP-0019
kind: validation-findings
validated_at: 2026-05-29T00:00:00Z
validated_by: main session (claude/intelligent-gauss-qacpV)
protocol: archive/c05-three-fail-trace/NEXT-SESSION-PROMPT.md
method: ran both new gates against the c05 three-FAIL evidence archive (1 chunk-cold-read + 2 coherence reviews, 3 dispatches)
reports:
  synthesis: active-project/staff/reviews/prop-0019-validation-synthesis.md
  test_1_chunk_coldread: active-project/staff/reviews/prop-0019-validation-test-1.md
  test_2_coherence_fail2: active-project/staff/reviews/prop-0019-validation-test-2.md
  test_3_coherence_shipped: active-project/staff/reviews/prop-0019-validation-test-3.md
  raw_agent_outputs:
    - active-project/staff/reviews/chunk-coldread-b01c05-validation.md
    - active-project/staff/reviews/coherence-b01c05-fail2-validation.md
    - active-project/staff/reviews/coherence-b01c05-shipped-validation.md

verdict_phase_8_5: VALIDATED   # the /and-stitch Phase 8.5 leg
verdict_phase_5_5: NOT-VALIDATED-AGAINST-THIS-TRACE   # the /and-substance Phase 5.5 leg

findings:
  - id: VF-1
    leg: Phase 8.5 (assembled-prose coherence)
    result: STRONG-POSITIVE
    detail: |
      On the FAIL #2 draft, Phase 8.5 flagged COLD-READ-RISK @14 at HIGH confidence, cited both the
      misread vector (sexual assault) and the substance-correct reading (chunk-authorized enforcement;
      not-naming = feed instrument-failure), and routed PRIMARY to bones-revise of @13 (pin -> strike) —
      the exact fix DEC-0042 applied — plus secondary stitch-revise of @14. Catch one phase upstream of
      Phase 9 at ~$2 vs the ~$30 revise cycle actually spent. On the SHIPPED draft it returned PASS:
      confirmed @14 risk closed AND correctly classified all four FAIL #3 design-inherent concerns as
      ADVISORY (not WEAVE-GAPs), firing zero spurious revises. Gate neither under- nor over-fires.
  - id: VF-2
    leg: Phase 5.5 (chunk cold-read)
    result: NEGATIVE-AGAINST-THIS-TRACE
    detail: |
      The chunk-reader RECOVERED the central event, mapped it to chapters[b01c05].goal, called causality
      "clean", and returned CONTINUE=yes -> PASS-CHUNK. A PASS fires no chunk-revise and no Step-3
      disposition. Therefore Phase 5.5 would have (a) NOT pre-empted FAIL #1 and (b) NOT surfaced FAIL #3's
      Class B risk for early principal disposition. This contradicts PROP-0019's GAP-1 rationale lines
      2337-2348, which credit the chunk-cold-read with catching FAIL #1 and surfacing FAIL #3.
    root_cause: |
      Two compounding structural biases make the chunk-cold-read a false-negative for c05's failure class:
      (1) OUTLINE-CHARITY — readers forgive opacity in an outline ("reads intentional") that they read as
          evasion in finished prose. The chunk-reader and the Phase-9 readers saw the SAME unexplained
          beating and unexplained Sera; the chunk-reader excused them, the prose-readers did not.
      (2) DOWNSTREAM-DEFECT — c05's FAILs were prose-execution failures (facet + stitch abstraction muffling
          a plainly-stated chunk event). That defect does not exist at chunk-read time, so the chunk read
          cannot see it. The proposal's own caveat ("chunks read different than assembled prose") cuts
          harder than assumed: for voice-driven dense-abstraction chapters, chunk-read and prose-read can
          land on OPPOSITE sides of the CONTINUE line.
    not_a_kill: |
      Phase 5.5 may still earn its keep on a DIFFERENT failure class — chunks with a genuine cause-chain
      hole or a CONTINUE=No-on-premise design. c05 is not that class (sound chunk, over-abstracted prose).
      This validation shows c05 was the WRONG evidence base to prove the chunk leg, not that the chunk leg
      is worthless.

recommendation:
  phase_8_5: KEEP — validated; closes the FAIL #2-class mechanism; net-cost-positive.
  phase_5_5: KEEP-BUT-RE-SCOPE — author PROP-0019-A to (a) correct the GAP-1 claim (FAIL #1/#3 are NOT
    chunk-catchable for this trace), (b) document the outline-charity + downstream-defect limitation, and
    (c) re-scope Phase 5.5 explicitly to chunk-design-hole / CONTINUE-on-premise detection, OR pin a fresh
    evidence base (a chapter that failed at the chunk-design level, not the prose-execution level) to validate it.
  triage_note: |
    PROP-0019 should NOT be triaged as a single accept/reject. Split: accept Phase 8.5 leg on this evidence;
    hold Phase 5.5 leg pending PROP-0019-A re-scope or fresh evidence. Both gates are already WIRED into the
    command bodies (commit 003f830); this addendum bears on whether to KEEP-AS-WIRED, re-scope the Phase 5.5
    classification logic, or gate Phase 5.5 behind a chapter_class / voice-density predicate so it does not
    bank a false PASS on dense-voice chapters.
status: open-pending-principal-triage
```

---

## PROP-0023

```yaml
id: PROP-0023   # renumbered from PROP-0020 by orchestrator (2026-05-30): PROP-0020 is the existing completeness/context-weave proposal (20 refs repo-wide); admin process-critic mislabeled this new apparatus-airless proposal. Content unchanged; ID corrected to next-free (PROP-0021 gap, 0022 taken).
created_at: 2026-05-30T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c06-2026-05-30.md
  source_verdict: PASS-WITH-DEPTH-PASS-REQUIRED
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 4.6 — Conditional R3 + fixer / Step 2 grounding-ledger re-review ALIVE verdict criteria"
change_type: modify
rationale: |
  b01-c06 is the first live chapter under the 2026-05-29 readability+completeness overhaul.
  The readability track fired correctly at every upstream checkpoint:
    - /and-review bones flagged BONES-AIRLESS-RISK on the accounting middle
    - Phase 2.5 opened 3 grounding-ledger lines
    - Phase 4.5 separated-scoring returned AIRLESS-HOLE
    - Phase 4.6 authored 3 cap-exempt grounding sensory adds
    - Phase 4.6 Step-2 re-review returned ALIVE
    - /and-stitch Phase 4 applied voice-embodiment discipline (4 VOICE-FIXABLE anchors person-first)
  The terminal cold-read (Phase 9) still returned AIRLESS.

  Root cause (per DEC-0048 + DEC-0049): ~18/25 bones have record-substrate verbs —
  apparatus-dominant by contract. The overhaul's interventions (3 grounding adds + 4 person-first
  renders) were exactly the 2 spots the cold-reader named as "the only breathing spots" — they
  worked, but they covered ~7 of ~18 apparatus-dominant bones. The grounding-ledger mechanism
  (add sensory anchors around apparatus prose) is PALLIATIVE on bone-layer abstraction — it
  cannot de-abstract the underlying apparatus SVOs; it only surrounds them with sensory adds.

  Critical structural distinction this overhaul was not designed/tested against:
    - c05's airlessness: render-layer (concrete bones, apparatus-rendered at stitch) →
      cured by person-first voice discipline. The overhaul was designed against this class.
    - c06's airlessness: bone-layer (apparatus-dominant SVO by contract) →
      palliative grounding adds and person-first renders cannot close the gap without
      content invention. This class was not in the overhaul's evidence base.

  The Phase 4.6 Step-2 re-review returned ALIVE after the 3 grounding adds, clearing the
  chapter for stitch. This was a false-ALIVE: an informed context-aware reviewer called ALIVE
  where a context-blind cold-reader called AIRLESS. The mechanism: context-aware reviewers
  compensate for apparatus prose by using their knowledge of the surveillance-operative POV
  and the chapter's substance contract. Cold-readers cannot access that compensation. For
  apparatus-dominant chapters, the "does it breathe after grounding adds?" question has
  systematically different answers from informed vs. uninformed perspectives.

  The false-ALIVE at Phase 4.6 deferred the depth pass one full stitch + cold-read cycle
  later than necessary. If Phase 4.6 had output AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER instead
  of ALIVE, the chapter would have routed to /and-write revise --from-signals BEFORE stitch,
  saving the stitch + Phase 9 round-trip (10-15 dispatches).

  The fix is a modifier to the Phase 4.6 Step-2 ALIVE verdict criteria: on an
  apparatus-dominant chapter (both BONES-AIRLESS-RISK in bones_review AND ABSTRACTION-DOMINANT
  SIGNAL in Phase 6 gate record), ALIVE requires explicit evidence that at least one bone per
  scene was de-abstracted (apparatus verb replaced by concrete actor-verb-object) — not just
  evidence that grounding adds are present around apparatus prose. If grounding adds are the
  only change and the bone-set remains apparatus-dominant, the verdict is
  AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER rather than ALIVE.

  This is change_type: modify on existing Phase 4.6 verdict criteria, not a new gate.
  The detection mechanism (BONES-AIRLESS-RISK + AIRLESS-HOLE) is unchanged and correct.
  The modification is to what ALIVE means for the re-review step when both upstream
  apparatus-dominance signals are in the chapter record.

  Recurrence count: 1 (first live apparatus-dominant chapter under the overhaul).
  Non-catastrophic (depth-pass loop fired correctly at Phase 9). Proposing at first
  occurrence because:
  (a) The mechanism is precisely discriminated from c05's render-layer class — two structurally
      distinct failure modes of "airlessness" that the grounding-ledger handles differently.
  (b) The false-ALIVE is a concrete gate gap (threshold miss on an existing gate step), not
      a taste call — it has a mechanical detection predicate (BONES-AIRLESS-RISK +
      ABSTRACTION-DOMINANT both in record) and a mechanical correction (require bone-level
      de-abstraction evidence before ALIVE).
  (c) The overhaul's own honest-limitations section (report 2026-05-29 §4) stated: "nothing
      is live-proven; b01-c06 is the first live test" — this is exactly the class of gap live
      testing was expected to surface, making a first-occurrence proposal appropriate.
  (d) The fix is S-cost and modify-only; no new gate, no new command phase, no schema change.

evidence_refs:
  - "active-project/staff/reviews/coldread-b01c06-2026-05-30.md — AIRLESS verdict; two breathing
    spots (stylus grounding add @17 + child's spoken line); accounting section (27-35) worst
    offender: 'abstract bookkeeping metaphor stacked on abstract metaphor'; withheld name 'reads
    as a tidy diagram of a feeling'"
  - "staff/admin/decisions.md — DEC-0048: root cause 'apparatus-dominant bone-set (~18/25
    record-substrate verbs) — a bone-layer authoring defect, not a stitch-layer voice problem';
    Phase 4.6 ALIVE false-positive traced; PASS-WITH-DEPTH-PASS-REQUIRED disposition"
  - "staff/admin/readability-completeness-overhaul-report-2026-05-29.md — §4 Honest limitations:
    'Nothing is live-proven. Every verification ran retroactively on already-shipped c05...
    b01-c06 is the first live test'; §3 PROP-0022 aliveness axis rerun on c05 found
    'AIRLESS (8 VOICE-FIXABLE + 5 GROUNDING-REQUIRED)' — 13 findings on c05 vs 3 on c06
    (c06 is a harder apparatus-dominance class; the reviewer found fewer because the whole
    bone-set is apparatus-dominant, not isolated patches)"
  - ".claude/commands/and-facets.md — Phase 4.6 Step-2 re-review (grounding-ledger); Phase 4.5
    AIRLESS-HOLE trigger; Phase 2.5 aliveness axis"
  - ".claude/commands/and-review.md — BONES-AIRLESS-RISK advisory note: 'If the bone set is
    wholly apparatus/process with no embodied or sensory-grounded beats, note BONES-AIRLESS-RISK
    in the record: it forewarns /and-facets Phase 2.5 to scrutinize the aliveness axis and likely
    open grounding-ledger lines'"
  - ".claude/commands/and-write.md — Phase 6 ABSTRACTION-DOMINANT SIGNAL: 'grounding bones < 25%
    of non-chatter' — the upstream apparatus-dominance detector whose firing (in conjunction with
    BONES-AIRLESS-RISK) is the proposed predicate for the stricter Phase 4.6 ALIVE bar"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 4.6 conditional R3 section, in the Step-2 grounding-
  ledger re-review instructions, add an apparatus-dominance qualifier to the ALIVE verdict:

  CURRENT (implied):
    Phase 4.6 Step-2 re-review: if grounding adds are present and the aliveness reviewer reports
    the airless zones now breathe → verdict ALIVE → proceed to Phase 5.

  PROPOSED — add a qualifier block before the ALIVE verdict:

    **Apparatus-dominance qualifier (fires when both conditions hold):**

    Condition A: `chapters[<slug>].bones_review.aliveness_note` contains `BONES-AIRLESS-RISK`
    (the bones reviewer flagged the whole chapter as apparatus/process-dominant at /and-review bones).

    Condition B: `chapters[<slug>].phase6_gate_signals` contains `ABSTRACTION-DOMINANT`
    (Phase 6 bone-gate SIGNAL: grounding bones < 25% of non-chatter — confirms the apparatus-
    dominance is bone-level, not a localized patch).

    If BOTH conditions hold, the Phase 4.6 Step-2 ALIVE verdict requires:

      **Evidence of bone-level de-abstraction (per scene).** For each scene in the chapter,
      the re-reviewer must identify ≥1 bone where the apparatus verb in the original SVO was
      replaced by a concrete actor-verb-object (e.g., "the count updates" → "Taylor marks one
      adult male, records, closes the notebook"). If the only changes are grounding sensory adds
      AROUND existing apparatus-dominant bones (the standard grounding-ledger add pattern),
      without any bone-level de-abstraction, the re-reviewer MUST return:

        AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER: apparatus-dominant bone-set. Grounding adds
        address isolated airless patches but cannot de-abstract the spine. Route to
        /and-write revise --from-signals before stitch. The ABSTRACTION-DOMINANT SIGNAL list
        from Phase 6 is the signal set.

      The re-reviewer may still return ALIVE if they can point to ≥1 concrete actor-verb-object
      bone per scene that was not present before Phase 4.6 (or confirm that a grounding-add
      bone itself carries concrete person-first SVO that de-abstracts the dominant verb pattern).
      VOICE-FIXABLE classifications (apparatus verb that can be person-first'd without content
      invention) do NOT count toward this requirement — they are stitch-layer, not bone-layer.

    The re-reviewer's verdict note must explicitly state whether the apparatus-dominance qualifier
    applies and which condition triggered it (A-only, B-only, or both). If neither condition holds,
    the qualifier does not fire and the standard ALIVE/AIRLESS verdict applies.

  **Routing when AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER fires:**
    Route to /and-write revise --from-signals with the following signal set passed to the
    brief:
      - All GROUNDING-REQUIRED entries from the grounding-ledger (these are the bones the
        facets layer targeted; the /and-write revise brief should de-abstract these bones
        specifically rather than just surrounding them with grounding adds)
      - ABSTRACTION-DOMINANT SIGNAL list from Phase 6 (the full apparatus-dominant bone set)
      - The Phase 4.6 re-reviewer's note on which scenes lack bone-level de-abstraction

    Memory write: chapters[<slug>].context_followability.readability_verdict =
    AIRLESS-UNRESOLVABLE-AT-FACETS-LAYER (not AIRLESS-HOLE; distinct outcome that routes
    upstream rather than to stitch).

  **Why this qualifier does not over-fire:**
  The two-condition predicate (BONES-AIRLESS-RISK + ABSTRACTION-DOMINANT) requires both:
  - The bones reviewer must have flagged whole-chapter apparatus-dominance (not just noted
    occasional instrument-register bones, which are common in surveillance chapters)
  - Phase 6 must have fired ABSTRACTION-DOMINANT (grounding bones < 25%) — a structural
    threshold, not a taste call

  A chapter with isolated apparatus patches (normal surveillance register) will not have
  ABSTRACTION-DOMINANT in its Phase 6 record and the qualifier will not fire. The qualifier
  is scoped to chapters that are apparatus-dominant by the bone-set's own structural
  composition, not chapters that merely use apparatus language in context.

  **Note on the grounding-ledger mechanism:**
  The grounding-ledger is still the correct intervention for chapters where apparatus-dominance
  is localized (isolated patches). The qualifier does not retire the grounding-ledger or prevent
  grounding adds — it only changes the ALIVE verdict threshold when the bone-set is structurally
  apparatus-dominant. Chapters where apparatus-dominance is localized (< both condition thresholds)
  continue through the existing grounding-ledger path unchanged.

  MEMORY SCHEMA NOTE (optional, deferred):
  The two-condition check requires reading two fields:
  - `chapters[<slug>].bones_review.aliveness_note` — current; written by /and-review bones
  - `chapters[<slug>].phase6_gate_signals` — may need a new memory field if ABSTRACTION-DOMINANT
    is not currently persisted to showrunner memory (it fires at Phase 6 but may only live in the
    bone-gate audit report). If not currently in memory, the Phase 4.6 step should read the
    bone-gate report directly to check. Adding a `phase6_signals: [<signal-name>]` field to
    `schemas/showrunner-memory.schema.md` would make this mechanical; cost S.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0024

```yaml
id: PROP-0024
created_at: 2026-05-30T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c07-bonegate.md
  source_verdict: "FAIL (6 HARD — EVENT-NOT-CONCRETE + SUBSTANCE-FLAT on 4 argument-middle bones: s02n06, s02n07, s03n04, s03n09)"
  gate_path: .claude/commands/and-write.md#phase-6
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition, step 2 (bone-shape + SVO discipline)"
change_type: modify
rationale: |
  b01c07 is a HINGE chapter whose central content is a discursive argument (Septon Halvard's
  principled-slower thesis, genuinely engaged + unresolved). /and-substance chapter Phase 5.5
  chunk-cold-read returned PASS-CHUNK-VOICE-RISK with an explicit "seminar-risk" flag. The
  /and-write Phase 1 decomposition brief carried that risk flag + WATCH-1 (named-death concrete)
  + front-load-concreteness instruction. The screen-writer honored WATCH-1 (Wenna Cobb is
  concrete in dialogue). But the four spine bones carrying the argument's progression — the
  thesis landing (s02n06), Taylor turning the thesis (s02n07 + its +0.3 axis-move), the named
  death landing (s03n04), and the argument completing (s03n09 + its +0.5 axis-move) — were
  authored as abstract arrival/landing/turning/completing interiority-form SVOs. Phase 6
  EVENT-NOT-CONCRETE correctly fired HARD on all four, plus SUBSTANCE-FLAT on the two that
  carried axis-moves.

  The gate is working as intended. The revise cycle routes correctly. The process question is:
  should the Phase 1 brief have prevented this at authoring time, given it explicitly carried
  the PASS-CHUNK-VOICE-RISK / seminar-risk flag?

  The answer is yes, and the gap is precise: Phase 1 step 2 instructs the screen-writer on
  SVO discipline and the event-coverage map but has no explicit guidance on how to author
  spine bones for argument-class chapters where the central event IS a discursive argument
  progression. The seminar-risk flag from Phase 5.5 enters the brief as risk context, but
  the brief does not translate it into a bone-authoring constraint on the argument-spine bones.
  The current discipline covers the schema-level interiority prohibition (no perception verbs,
  no cognitive objects) but does not name the specific failure mode for argument chapters: the
  "X lands / X turns / X completes" abstract-arrival form that is not a schema violation on its
  face (the verb "turns" is physical; "the thesis" as object is what makes it interiority) but IS
  the canonical failure mode for argument-middle spine bones.

  This is a Phase 1 brief-discipline gap for argument-class / PASS-CHUNK-VOICE-RISK chapters,
  not a gate miss. The gate detected correctly. The addition is a proactive authoring constraint
  that the screen-writer receives at decomposition time — the same substance the Phase 6 criteria
  require, surfaced one phase earlier, so the revise cycle is the exception rather than the rule
  on argument chapters.

  Distinct from PROP-0023: PROP-0023 targets apparatus-dominant whole-chapter airlessness
  (Phase 4.6 false-ALIVE threshold). That pattern is ~18/25 apparatus-dominant bones by contract,
  ABSTRACTION-DOMINANT SIGNAL chapter-wide. The c07 pattern is argument-middle interiority at
  4 specific spine bones despite a concrete bone-set everywhere else (91/57/69% ratios; the
  abstraction is concentrated at the 4-bone argument spine). Different failure class (bone-authoring
  discipline gap vs. ALIVE-verdict threshold), different target (Phase 1 brief vs. Phase 4.6
  verdict criteria), different command phase.

  Recurrence count: 1. First argument-chapter spine-bone interiority failure. Non-catastrophic
  (4-bone revise cycle, clear criteria, chapter otherwise clean). Proposing at first occurrence
  rather than waiting because: (a) the mechanism is precisely discriminated from all prior
  failure classes; (b) the gap is in the Phase 1 brief (a concrete spec omission, not a taste
  call); (c) the fix can be written with precision now — the three forms to prohibit (abstract
  subject + arrival/completion verb; cognitive object + any verb; abstract-progress framing on
  spine bones) are enumerable; (d) the minimum-repair path (argument-spine bone-authoring
  constraint in Phase 1 step 2) is S-cost; (e) PASS-CHUNK-VOICE-RISK is already the detection
  predicate (the flag is in the brief; the constraint only needs to name what the flag implies
  for bone-authoring).

  Note on question 3 (over-fire risk): the bone-gate report's criteria fields show that concrete
  witnessing of relational/interior axis-moves is achievable without physical-prop invention —
  enacted physical postures, speech bones with concrete objectives, departure gestures, stillness-
  against-pressure forms all satisfy EVENT-NOT-CONCRETE for relational argument events. The
  gate is not misfiring on legitimate interior-chapter content; the constraint directs the
  screen-writer toward the available concrete-witnessing vocabulary for this chapter class.
evidence_refs:
  - "active-project/staff/auditor/write-b01c07-bonegate.md — fault-001/002/003/004 (FAULT-FORM-INTERIORITY on s02n06/s02n07/s03n04/s03n09); fault-011/012 (SUBSTANCE-FLAT-political_register-prot + SUBSTANCE-FLAT-social_tether-prot-rise on same bones); fix_scope block: spine bones must record observable physical acts from which the cognitive/relational quality can be inferred at the facet layer; event_not_concrete_summary: 4 FAIL of 7 tested"
  - "active-project/staff/auditor/write-b01c07-bonegate.md — abstraction_dominance: s01=91%, s02=57%, s03=69%; ABSTRACTION-DOMINANT SIGNAL on s02 n06-n09 block only (not chapter-wide); chapter is NOT apparatus-dominant overall — c07 and c06 are structurally distinct failure classes"
  - "staff/admin/process-proposals.md — PROP-0023 (Phase 4.6 apparatus-dominant false-ALIVE; target phase and failure class both distinct from this proposal: PROP-0023 is whole-chapter apparatus-dominance by contract; PROP-0024 is argument-spine interiority at 4 specific spine bones on a chapter that is otherwise concrete)"
  - ".claude/commands/and-write.md Phase 1 step 2 — SVO discipline; PASS-CHUNK-VOICE-RISK risk context is received but no explicit bone-authoring constraint for argument-spine positions on flagged chapters is stated"
  - "active-project/staff/auditor/write-b01c07-bonegate.md — fault-002 criteria: 'the bone must be recast as a concrete physical act by taylor-hebert-kl-122ac that an observer would see or hear — a physical gesture, a posture change, a verbal act, a return gaze, any concrete enacted response to the argument'; fault-004 criteria: 'concrete physically-observable act by a named actor — a leave-taking gesture, moment of mutual stillness, Taylor's physical departure, Halvard's response'"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-write.md, Phase 1 step 2, after the three bone shapes (moving /
  held / chatter) block and before the event-coverage map instruction, add a subsection:

  **Argument-chapter spine-bone constraint.** Fires when ANY of these predicates hold:
    (a) `chapters[<slug>].chunk_cold_read.verdict = PASS-CHUNK-VOICE-RISK`
    (b) Phase 0 brief names seminar-risk / argument-dominant / discursive-argument in WATCH items
    (c) `chapters[<slug>].dramatic_shape` resolves to persuasion / deliberation / argument class

  On chapters where the predicate fires, spine bones — bones whose `event_map[]` entries cover
  the argument's progression (thesis delivery, thesis reception, evaluative turn, argument
  completion, resolution) AND bones carrying axis-moves on relationship-class axes
  (social_tether, relational_anchor, political_register, reputation, trust, community) where
  those moves depend on the argument's progress — are subject to an additional bone-authoring
  constraint:

    **Prohibited forms on argument-spine bones:**

    1. **Abstract-arrival form.** SVO whose subject is the argument, thesis, claim, evidence,
       or named event itself, driving a metaphorical-arrival verb (lands, settles, strikes, hits,
       completes, closes, resolves). Examples: "the thesis lands," "the named death lands,"
       "the argument completes." These map an interior-reception event to an abstract-subject
       pseudo-action. The schema already bans interiority verbs; this names the canonical
       argument-chapter evasion that the schema's abstraction-as-subject rule catches but that
       the screen-writer may not recognise as an interiority form without explicit naming.
       Both FAULT-FORM-INTERIORITY (Phase 2) and EVENT-NOT-CONCRETE (Phase 6) are HARD.

    2. **Cognitive-object form.** SVO whose named actor is concrete but whose object is the
       thesis, argument, claim, or any abstraction of it: "taylor turns the thesis," "taylor
       reads the argument," "taylor weighs the claim." The schema rule is abstraction-as-object
       = INTERIORITY. The canonical failure: a physical verb ("turns") with an abstract object
       ("the thesis"). Test: replace the object with a concrete physical referent — if the bone
       no longer makes sense, the object is an abstraction and the bone is non-concrete.

    **Prescribed alternatives.** For argument-spine positions, author a concrete physical act by
    a named actor that an observer could witness, from which the argument-progression can be
    inferred at the narrator-interest facet layer:

    - Thesis reception: not "the thesis lands" — author the observable physical response that
      signals engagement (actor goes still, actor moves toward the speaker, actor does not reach
      for the counter, any enacted physical posture an observer reads as reception). The cognitive
      event is narrator-interest material; the bone records the observable correlate.

    - Evaluative turn: not "taylor turns the thesis" — author the physical act that enacts the
      turn (a concrete speech bone where the actor delivers a counter, a posture shift, naming a
      specific object or person, any physically-enacted response). The inner evaluation is
      narrator-interest; the bone records what an observer sees or hears.

    - Relational axis-moves in argument chapters: the moving bone must physically enact the
      relational shift. For social_tether, political_register, community, trust axis-moves,
      record the physical act from which the relational shift can be inferred — enacted presence,
      a leave-taking, a named acknowledgment, a sustained or broken gaze, a physical departure
      — not the shift itself as an abstract event.

    - Argument completion: not "the argument completes" — author the physical act that is the
      completion (a leave-taking beat, a moment of mutual stillness, the actor's physical
      departure, the other actor's response) from which completion-not-closure can be inferred
      at the facet layer.

    These alternatives do not restrict what content the chapter carries — the evaluative,
    interior, and relational dimension belongs in narrator-interest facets citing the bone's
    concrete SVO as their physical anchor. The constraint governs what the bone itself records.

  **Phase 0 integration note.** When Phase 0 reads
  `chapters[<slug>].chunk_cold_read.verdict = PASS-CHUNK-VOICE-RISK`, the Phase 0 brief
  surfacing block MUST include: "Argument-spine constraint active: spine bones carrying
  thesis-progression and relational axis-moves must be concrete actor-verb-object (not
  abstract-arrival or cognitive-object form) — see Phase 1 step 2 argument-chapter constraint."
  This connects the PASS-CHUNK-VOICE-RISK detection to the Phase 1 authoring discipline so
  the screen-writer receives the constraint at dispatch time, not at Phase 6 gate-time.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```
