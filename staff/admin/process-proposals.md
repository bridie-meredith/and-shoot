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
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED. Persona-exemplar architecture live: schemas/persona-exemplar.schema.md + cards/persona-exemplars/ populated; CLAUDE.md Rule 16 (URI-PERSONA-EXEMPLAR); Tier-1 auto-resolve at dispatch. Reconciled 2026-06-23."
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
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED. Tier-1/2/3 exemplar split codified in CLAUDE.md Rule 16 (Tier-2 exclusion recorded). Reconciled 2026-06-23."
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
recurrence_count: 4
# recurrence_count bumped 3->4 by admin process-critic DEC-0084 (2026-06-04):
# b01c14 Phase 6 bone-gate — 11 HARD, root cause: every fractional scene-target (0.25/0.5)
# enacted by a 1.0-floor moving bone, producing chapter bone-sum 2-6x the contract AND
# axis-ties at 1.0 in S03/S04 (3 STAKES-AXIS-NOT-DOMINANT HARDs). Remediated in-cycle
# via mover-to-held conversions + S04 lenient-tie disposition. S04 convergence-climax
# (4 arcs closing simultaneously) is the most consequential sub-case of fractional-floor
# collision: strict single-dominance is structurally impossible when N arcs complete at
# the 1.0 floor simultaneously. PROP-0010's proposed_diff consolidation language already
# covers the mechanism but should be read as especially binding for multi-arc convergence
# chapters. Note: the co-dominant-tie clause for simultaneous N-arc completion is proposed
# separately as PROP-0039 (Phase 6 gate spec amendment).
recurrence_refs:
  - "active-project/staff/auditor/write-b01c06-bone-gate.md — signal-001 + signal-002: moral_legibility_to_self scene-aggregate target +0.5 (fractional residual after scene distribution); bone-floor 1.0 forced over-delivery to +1.0; accepted-with-rationale; stakes-axis tie (moral_framework=moral_legibility at 1.0 each) is a direct consequence of the same fractional-target-floor collision. Second chapter exhibiting this exact structural pattern (b01c04 was first). No HARD fired; accepted path worked. Confirms recurrence is predictable on any chapter with fractional scene residuals."
  - "active-project/staff/auditor/write-b01c06-bone-gate-revise.md — signal-001 + signal-002 (identical signals, depth-pass revise run): moral_legibility +0.5->+1.0 bone-floor artifact + stakes-tie mf=mls at 1.0. Third chapter run exhibiting the fractional-target-floor collision. Merged by DEC-0057."
  - "active-project/staff/auditor/write-b01c14-bone-gate.md — 11 HARD (all remediated in-cycle); root cause: every fractional scene-target (0.25/0.5 for antag/position/moral_leg in multi-arc convergence chapter) enacted by a 1.0-floor moving bone. Chapter bone-sum (relational +2.0, antag +3.0, position +3.0, moral_leg +2.0) overshot contract (+1.0/+1.5/+1.0/+0.5) 2-6x. 3 STAKES-AXIS-NOT-DOMINANT HARDs in S03/S04 from axis-ties at 1.0. Remediated via mover-to-held conversions (S02/S03 to strict single-mover dominance; S04 convergence-climax via lenient co-dominant-tie disposition). Fourth occurrence. The multi-arc simultaneous-completion case is the most structurally forced sub-case of this collision: strict single-dominance is impossible when N arcs complete at the 1.0 floor per the substance contract. PROP-0010's consolidation guidance must be understood as mandatory for such chapters. Merged by DEC-0084."
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
recurrence_count: 4
# recurrence_count bumped 2→3 by admin process-critic DEC-0069 (2026-06-02):
# b01c10 Phase 6 bone-gate returned 4 HARD HELD-AXIS-NOT-WITNESSED covering 9 scene-contract
# held axes (s01 ×2, s02 ×3, s03 ×1, s04 ×3). Root cause: screen-writer attributed
# held-axis coverage via rollup ("implicit n03 grounding") rather than placing each held axis
# into the target bone's bone-level axes_held[]. All 9 resolved cycle-1 by fixer. Same failure
# class as c04 (5 axes, additive-bone cycle) and c06 (1 axis, assign-to-existing). Third
# chapter-level occurrence confirms the Phase 1 brief gap is persistent.
# recurrence_count bumped 3→4 by admin process-critic DEC-0077 (2026-06-03):
# b01c12 Phase 6 bone-gate returned 3 HARD (fault-001/003/004) — single structural gap:
# s04 contract declared political_register-prot + social_tether-antag held; zero bones in s04
# carried either axis in bone-level axes_held[]. Resolved in-cycle by fixer attaching axes_held
# to two existing s04 bones (n40 + n41 in the final bones file) without adding new bones.
# Root cause identical to prior occurrences: Phase 1 brief does not present held-axis witnessing
# as an explicit numbered completion gate, so the screen-writer omits the axes_held[] population
# step when focusing on moving/chatter bone authoring. Fourth chapter-level occurrence.
recurrence_refs:
  - "active-project/staff/auditor/write-b01c12-bone-gate.md — 3 HARD HELD-AXIS-NOT-WITNESSED; 2 axes (political_register-prot, social_tether-antag) in s04; resolved in-cycle (fixer attached axes_held to existing bones n40/n41; no new bones added). Fourth occurrence of the Phase 1 brief gap."
  - "active-project/staff/auditor/write-b01-c10-bone-gate.md — 4 HARD HELD-AXIS-NOT-WITNESSED; 9 axes across s01/s02/s03/s04; resolved cycle-1 (fixer added 9 axes_held[] entries to s01n03/n05, s02n03/n04/n07, s03n07, s04n01/n03/n05). Process note: 'screen-writer attributed held axes via rollup rather than bone-level axes_held[]' — the exact authoring gap PROP-0011 proposes to close."
  - "active-project/staff/auditor/write-b01c04-bone-gate-redo.md — first occurrence: 5 HARD across 3 scenes; additive bone cycle."
  - "active-project/staff/auditor/write-b01c06-bone-gate.md — second occurrence: 1 HARD fault-001; trivial fix."
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

    Note: rollup-level attribution ("this axis is implicitly witnessed by n03's grounding")
    does NOT satisfy this check. The target bone must have the axis explicitly listed in
    its bone-level axes_held[]. Implicit attribution is not detectable by the Phase 6
    gate and will return HELD-AXIS-NOT-WITNESSED even when a suitable bone exists.

    Holding discipline for the held bone: the SVO must enact stillness-against-pressure
    for axis A (see step 2 held-bone description). The rationale must name the discipline.
    The bone is a normal held bone — it may serve double duty (also a grounding bone or
    a chatter bone) if its SVO is concretely physical and the axes_held entry is present.

  The existing held-bone description in step 2 is unchanged — this step 4a is the
  completion checkpoint that operationalizes the requirement stated there. The information
  is not new; its placement as a named completion gate is the change. The note on
  implicit/rollup attribution (added at third recurrence) closes the specific gap that
  produced 9 missed witnesses at b01c10: the screen-writer knew the axes were held but
  expressed coverage at the scene-rollup level rather than the bone level.
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
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED. Cherry-pick default-on live in .claude/commands/and-stitch.md. Reconciled 2026-06-23."
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
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED. Chunk-cold-read upstream gate wired in and-substance.md Phase 5.5 + and-stitch.md Phase 8.5 (CLAUDE.md Rule 17); exercised live through b01c20; superseded as sole readability backstop by DEC-0115 no-ledger layer. Reconciled 2026-06-23."
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
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED (reshaped). Aliveness axis (FOLLOWABLE x ALIVE) live at /and-facets Phase 2.5; the apparatus-register-as-axis framing was superseded by DEC-0115 (apparatus register prohibited as prose mode, not scored). Reconciled 2026-06-23."
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

---

## PROP-0025

```yaml
id: PROP-0025
created_at: 2026-05-30T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/bones-b01c07-2026-05-30.md
  source_verdict: "/and-review bones b01c07 = FAIL; HARD 3 (SVO-form: flat15/22/16); all three passed /and-write Phase 6 bone-gate on rev2"
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 6 — Substance bone-gate / Per-bone verification (auditor)"
change_type: modify
rationale: |
  At /and-write b01c07 rev2 (attempt 3 under DEC-0052's one-attempt cap), the Phase 6 bone-gate
  accepted three bones that carry PP-modifier or abstraction-as-object violations banned by
  bones.schema.md:

    flat15 "taylor-hebert-kl-122ac stays in the argument" [MOVING soc-tether +0.5] —
      "in the argument" is a PP modifier (locative-abstract), banned by line 57. The rev2
      draft marked it "unchanged PASS" (from attempt 1). The Phase 6 auditor accepted the
      author's annotation without re-deriving the form.

    flat22 "taylor-hebert-kl-122ac stays at the sept-corner" [MOVING soc-tether +0.5] —
      "at the sept-corner" is a textbook PP-of-place, banned by line 57. The rev2 draft
      cited "the exact form that passed at attempt 1." Prior-pass status is not schema
      authorization. The Phase 6 auditor accepted the citation.

    flat16 "septon-halvard-flea-bottom holds the silence" [HELD] — abstraction-as-object
      ("the silence"), banned by line 60. A held bone; does not destabilize Δ arithmetic.
      Form fault is real and the gate missed it.

  The bones-review re-fire at /and-review caught all three. Phase 6 did not.

  The structural gap: the Phase 6 auditor brief says "classify each bone as CORRECT or
  FAULT-{class}" using bones.schema.md + harsh-SVO rules. It does not instruct the auditor
  to re-derive form from the raw SVO text independently of author form annotations. Without
  that instruction, a revise context — where the author has already labeled bones with form
  verdicts ("unchanged PASS", "passed at attempt 1", "whitelist-licensed") — creates pressure
  for the auditor to defer to the label rather than re-derive. The author's annotation acts as
  a surrogate gate-pass, and the auditor's independent classification collapses into
  annotation-acceptance.

  This is not a gate-existence gap. The gate has the right checks (FAULT-FORM per
  bones.schema.md line 57/60). The brief gap is the absence of an explicit re-derivation
  instruction: the auditor must re-derive from raw text, not from the author's prior verdict.
  One sentence in the Phase 6 brief closes the gap.

  Note on context pressure: the DEC-0052 one-attempt cap amplified the pressure to accept
  near-miss forms on the final permitted attempt. The cap was correct (DEC-0052). The brief
  gap is independent of the cap and exists on any revise cycle where the author annotates
  unchanged bones with prior verdicts.

  Recurrence count: 1 (first cross-chapter instance of auditor accepting author self-assessment
  on MOVING bones with PP/abstraction violations). Non-catastrophic — caught by /and-review
  bones at cost of one revise cycle. Proposing at first occurrence rather than waiting because:
  (a) the spec omission is precisely discriminated — one instruction absent from the Phase 6
  brief; (b) not a taste call but a re-derivation procedure gap; (c) every revise cycle on any
  chapter carries the same bypass risk when the author annotates unchanged bones; (d) S-cost.

  Distinct from PROP-0024: PROP-0024 targets Phase 1 argument-spine bone-authoring (what the
  screen-writer authors). This proposal targets Phase 6 auditor re-derivation discipline (how
  the auditor classifies bones the author has already annotated). Different phase, different
  agent, different gap class. Both are open and independent.
evidence_refs:
  - "active-project/staff/reviews/bones-b01c07-2026-05-30.md — fault-001 (flat15 PP 'in the argument': rev2 marked 'unchanged PASS'; Phase 6 did not re-audit); fault-002 (flat22 PP 'at the sept-corner': rev2 cited 'exact form that passed at attempt 1'; Phase 6 accepted); fault-003 (flat16 'holds the silence': abstraction-as-object)"
  - ".claude/commands/and-write.md — Phase 6 §Per-bone verification (auditor): 'classify each bone as CORRECT or FAULT-{class}' per bones.schema.md + harsh-SVO rules — no re-derivation instruction; no prohibition on accepting author form annotations"
  - "schemas/bones.schema.md — line 57 (no PP modifiers of place/direction/time/instrument/accompaniment on bone SVOs) + line 60 (concrete object requirement: no abstraction-as-object)"
  - "staff/admin/decisions.md — DEC-0052 (one-attempt cap context; cap was correct call; brief gap is independent)"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-write.md, Phase 6 §Per-bone verification (auditor), before the
  "Moving bones", "Held bones", "Chatter bones" sub-sections, add:

    **Re-derivation rule (mandatory in revise mode and redo mode).** For every bone in scope —
    including bones the author or screen-writer has annotated with a prior verdict ("unchanged
    PASS", "whitelist-licensed", "form passed at attempt N", "prior-pass status") — the auditor
    MUST re-derive SVO form from the raw bone text against bones.schema.md. Author form
    annotations are NOT accepted as a substitute for independent re-derivation.

    Specifically check: (1) does the SVO core (subject–verb–object) contain a prepositional
    phrase modifier appended to it (PP of place/direction/time/instrument/accompaniment —
    banned by line 57)? (2) Is the object an abstract noun rather than a concrete referent
    (banned by line 60 — "the argument," "the silence," "the weight," "the truth" are canonical
    examples; replace-with-concrete-noun test: if the SVO stops making sense as a physical
    event when you replace the object with a concrete noun, the object is an abstraction)?
    (3) Is the verb a perception, interiority, or cognition verb (banned generally)?

    A MOVING or HELD bone that fails any of these checks is FAULT-FORM regardless of prior
    annotation. The rev2 bypass case (b01c07: "stays in the argument" marked "unchanged PASS"
    — PP modifier; "stays at the sept-corner" marked "prior-pass" — PP-of-place; "holds the
    silence" — abstraction-as-object) is the canonical evidence that author annotations cannot
    substitute for this check. All three were caught by /and-review bones after Phase 6 passed
    them.

  Additionally, recommend (but defer to principal) adding a mechanical pre-screen before the
  auditor's semantic classification step: regex-scan every MOVING bone's raw SVO text for
  preposition strings (in / at / on / with / to / across / through / around / from / into +
  following noun phrase) and any object match against a short abstraction-noun list (argument /
  silence / tension / weight / uncertainty / void / truth / meaning). Any regex match on a
  MOVING bone → flagged for mandatory re-derivation regardless of author annotation. This
  mechanical pre-check makes the re-derivation rule self-enforcing under any context pressure.
  Principal's call whether to add this as a formal Phase 6 sub-step or as an auditor-dispatch
  note.

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

## PROP-0026

```yaml
id: PROP-0026
created_at: 2026-05-31T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/audience/facets-audience-gate-r1.md
  source_verdict: "/and-facets b01c07 Phase 5b cycle-1 FAIL (7 PASS / 4 FAIL); dialogue-taylor FAIL on no-winner-invariant violation"
  gate_path: .claude/commands/and-facets.md#phase-5b
  secondary_gate_paths: [.claude/commands/and-write.md#phase-1.5, .claude/commands/and-facets.md#phase-3]
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 3 — R2 fanout / R2 dialogue-judge dispatch brief"
change_type: modify
rationale: |
  b01c07 is a HINGE/ARGUMENT chapter with PASS-CHUNK-VOICE-RISK. The substance contract for
  argument chapters carries a no-winner invariant: neither party prevails; the chapter ends
  unresolved. The dialogue-taylor entry [taylor:1] @19 closed with "She's why I'm in Flea Bottom
  at all" — a spoken motive that converts Wenna Cobb's death from cost into self-justification,
  making Taylor the winner of an exchange the chapter is built to leave undefeated.

  Two independent reviewers at Phase 5b (dark-fantasy-reader + worm-canon-pedant) independently
  flagged the SAME sentence as the fault. The dialogue-writer at Phase 1.5 passed it — the
  Phase 1.5 dispatch is blind to facets and chapter-substance invariants are not in the
  dialogue-writer brief beyond behavior-card fences. The R2 dialogue-judge at Phase 3 passed it
  — the rubric's Q2 is limited to behavior-card hard-fences (forbidden vocabulary, Earth-Bet,
  monument naming), and the R2 dispatch brief does not carry chapter-class substance invariants.
  The Phase 5 mechanical auditor passed it — no card-fence violation; the no-winner invariant
  is not in the CONSTRAINT class. Only Phase 5b audience adversarial review caught it.

  The structural gap: the R2 dialogue-judge brief does not thread chapter-level substance
  contracts (specifically: argument-chapter invariants like no-winner, cost-vs-justification
  prohibition, and unresolved-outcome requirements) into the Q2 check. These invariants are
  not behavior-card properties — they are properties of the chapter's substance contract
  (`chapters[<slug>].dramatic_shape` + `chapters[<slug>].goal` + the substance_delta's
  invariant block if present). The dialogue content must not violate them even when it is
  card-affirmative and card-fence-clean.

  This is distinct from PROP-0024 (argument-spine bone-authoring at /and-write Phase 1 step 2).
  That proposal targets what the bones record (observable physical acts vs. abstract arrivals).
  This proposal targets what dialogue says relative to chapter-substance invariants (a completed
  ARGUMENT chapter's no-winner invariant vs. dialogue that declares a winner). Different gate
  (Phase 3 R2 dialogue-judge brief vs. Phase 1 screen-writer brief), different agent, different
  constraint source. Both can fire on the same chapter; they are complementary, not overlapping.

  The fix is to add a chapter-class substance constraint block to the Phase 3 R2 dialogue-judge
  dispatch brief, gated on the same predicate as PROP-0024's Phase 1 constraint:
    (a) `chapters[<slug>].chunk_cold_read.verdict = PASS-CHUNK-VOICE-RISK`, OR
    (b) `chapters[<slug>].dramatic_shape` resolves to argument / persuasion / deliberation class.

  On argument chapters, the R2 judge's Q2 check must additionally verify each utterance against
  the chapter's substance contract invariants — specifically, the no-winner / cost-vs-justification
  class: any utterance that would make one interlocutor the victor of an unresolved argument, or
  converts a cost-paid event into a self-justifying motive, is a Q2 violation even when
  card-fence-clean.

  This is change_type: modify on the existing Phase 3 R2 dispatch brief, not a new gate.
  The R2 dialogue-judge is already dispatched; the substance-contract coupling is the only
  addition. The rubric's two-question gate (Q1 + Q2) already exists; the proposal extends Q2's
  scope on argument chapters.

  Recurrence count: 1 (first argument chapter in the project). Non-catastrophic (caught at
  Phase 5b, resolved cycle-2). Proposing at first occurrence because:
  (a) The gap is a precise spec omission — argument-chapter substance invariants are not in
      the R2 brief's Q2. Not a taste call.
  (b) Deterministic recurrence: every argument chapter's dialogue will be reviewed by an R2 judge
      that does not check chapter-substance invariants unless this proposal is implemented.
  (c) S-cost: one constraint block in the Phase 3 dispatch brief section for dialogue judges,
      gated on the same predicate as PROP-0024.
  (d) PROP-0024's predicate infrastructure is already proposed — this proposal piggybacks the
      same activation gate.

evidence_refs:
  - "active-project/staff/audience/facets-audience-gate-r1.md — §D dialogue-taylor FAIL: 'She's why
    I'm in Flea Bottom at all' — dark-fantasy: card no-self-justification-to-the-room prohibition;
    worm-canon: card-forbidden spoken-motive-to-interlocutor register; two-persona convergence,
    same sentence; high-confidence FAIL."
  - ".claude/commands/and-facets.md — Phase 3 R2 dialogue-judge dispatch brief: rubric-dialogue.md
    Q2 'card not violated' — scoped to behavior-card hard fences only; no chapter-substance contract
    check."
  - "staff/dialogue-writer/rubric-dialogue.md — §Hard fences: Earth-Bet proper-noun scan +
    monument naming + forbidden vocabulary from behavior card. No chapter-class substance invariants."
  - ".claude/commands/and-write.md — Phase 1.5 dispatch: 'blind to other facets; forbidden inputs:
    facet rubrics (no facets exist yet)' — chapter-substance contracts are explicitly excluded from
    Phase 1.5 dispatch at authoring time."
  - "staff/admin/process-proposals.md — PROP-0024 (argument-spine bone-authoring constraint at Phase 1
    step 2; activation predicate PASS-CHUNK-VOICE-RISK or argument dramatic_shape — same predicate
    proposed here for R2 dialogue-judge; distinct target and failure class)."
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 3 R2 fanout section, in the R2 dialogue-judge dispatch
  brief (the section that covers the judge's decision mandate: KEEP / DELETE / REWRITE), add a
  new Q2-extension block after the existing Q2 ("card not violated") description:

    **Q2 extension: chapter-class substance invariant check (fires on argument/deliberation chapters).**

    Activation predicate (check either condition):
      (a) `chapters[<slug>].chunk_cold_read.verdict = PASS-CHUNK-VOICE-RISK`
      (b) `chapters[<slug>].dramatic_shape` resolves to argument / persuasion / deliberation /
          negotiation class

    If the predicate fires, the R2 dialogue-judge must additionally verify every utterance — KEEP
    candidates included — against the chapter's substance contract invariants. Read:
      - `chapters[<slug>].goal` (the chapter's declared outcome/intent)
      - `chapters[<slug>].dramatic_shape` (the structural shape; unresolved-argument, cost-landing, etc.)
      - The scene's `substance_delta.scene_conflict` for the scene the dialogue anchor belongs to

    Substance invariant violations that are NOT card-fence violations but ARE chapter-contract violations:

    1. **No-winner violation.** On a chapter whose dramatic_shape is argument / deliberation /
       unresolved, any utterance that would make one interlocutor the definitive winner of the
       exchange is a Q2 violation. Markers: the speaker explicitly states they have prevailed,
       declares a victor position, or converts a shared cost into personal justification for their
       position. Example: on a chapter built around the no-winner invariant (b01c07: Wenna Cobb's
       death as unresolved cost, not a justification for any position), an utterance that frames
       the death as "why I'm in this place" converts cost into self-justification — the speaker
       names the cost as evidence that their position is right, which is the no-winner invariant's
       exact prohibition.

    2. **Cost-vs-justification violation.** A cost-paid event (a death, a sacrifice, a loss) that
       the chapter tracks as substance-axis movement (moral_legibility, position, community axis)
       must not be rendered in dialogue as a justification for the speaker's position or presence.
       The cost is a cost; dialogue that converts it into "the reason I do X" re-frames it as
       benefit. This is the spoken-motive-to-interlocutor prohibition — making the cost serve the
       speaker's argument is a substance fault regardless of card-register.

    On detecting a substance invariant violation:
    - Classification: DELETE (if the violation is the core function of the entry) or REWRITE
      (if the violation is a closing sentence / final clause while the entry body is clean — as in
      b01c07 where the entry closed cleanly on "She's the first name in the count" with the
      invariant violation only in the final sentence "She's why I'm in Flea Bottom at all").
    - The judge must name the violated invariant in the decision-shard: "SUBSTANCE-INVARIANT:
      [no-winner | cost-vs-justification] — entry [id] at @[anchor] violates [goal/dramatic_shape]
      because [one-line reason]."
    - A REWRITE disposition follows the existing multi-draft + chosen-mark protocol; the judge
      must note which draft avoids the invariant violation.

    This Q2 extension does NOT override the standard card-fence Q2. Both checks are AND-gated:
    an entry must pass both card-fence Q2 AND chapter-substance-invariant Q2 to receive KEEP.

  Additionally, the R2 dialogue-judge's required inputs (Phase 3 dispatch payload) should include:
    - `chapters[<slug>].goal` (already accessible from showrunner memory)
    - `chapters[<slug>].dramatic_shape`
    - `chapters[<slug>].scenes[].scene_conflict` (for the scenes whose dialogue the judge reviews)

  These are already in showrunner memory and do not require new artifacts. The dispatch payload
  block in Phase 3 should name them explicitly for dialogue judges on argument chapters.

  SCOPE NOTE:
  The Q2 extension fires only on argument/deliberation chapters (per the activation predicate).
  On non-argument chapters (action, revelation, grief, threshold, etc.), the standard Q1 + Q2
  behavior-card discipline applies unchanged. The predicate ensures the extension doesn't
  over-fire on chapter classes where the no-winner / cost-vs-justification distinction is
  not load-bearing.

  PHASE 0 INTEGRATION NOTE:
  Phase 0 already reads `chapters[<slug>].chunk_cold_read.verdict` (per PROP-0019/0024 wiring).
  If PASS-CHUNK-VOICE-RISK is present, the Phase 0 brief surfacing block should include:
  "Argument-substance constraint active at Phase 3 R2 dialogue-judge: Q2 extended to include
  no-winner / cost-vs-justification chapter invariant check."

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

## PROP-0027

```yaml
id: PROP-0027
created_at: 2026-05-31T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/audience/facets-audience-gate-r1.md
  source_verdict: "/and-facets b01c07 Phase 5b cycle-1 FAIL — fixer recast sensory:4@22 to modality `proprioceptive`; grounding-ledger grd-002 satisfied_by became stale"
  gate_path: .claude/commands/and-facets.md#phase-5b
  secondary_gate_paths: [.claude/commands/and-facets.md#phase-4.6]
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 5b — remediation cycle / fixer dispatch protocol"
change_type: modify
rationale: |
  The grounding-ledger mechanism was introduced by PROP-0022 (URI-READABILITY-TWIN, 2026-05-29).
  b01c07 is the first live chapter to use it. The grounding-ledger at
  `active-project/staff/showrunner/grounding-ledger-b01-c07.md` carried grd-002, a
  GROUNDING-REQUIRED entry with:
    satisfied_by: sensory:4  (once Phase 4.6 added the grounding entry)
    status: satisfied

  At Phase 5b cycle-1, the audience-gate callouts included a fix to sensory:4@22: the entry was
  a discrete-modality problem (cumulative re-registration, not a discrete delta) as well as a
  grounding-ledger grd-002 licensed-grounding entry. The cycle-1 fixer recast the entry's
  modality and content to a discrete proprioceptive event (which separately introduced the
  schema-invalid modality `proprioceptive` — Pattern 2 from DEC-0055). This recast made the
  grounding-ledger's satisfied_by field stale: grd-002.satisfied_by pointed to sensory:4, but
  sensory:4's content was now different from what satisfied the grounding requirement.

  The structural gap: the Phase 5b remediation cycle's fixer dispatch brief does not include a
  coupled-record-update step for the grounding-ledger. The fixer is dispatched with: consolidated
  audience-gate callouts + facet rubrics + Phase 5 audit report. The grounding-ledger is present
  in the auditor's inputs (Phase 5 reads it) but is not in the fixer's briefing as a coupled
  artifact whose `satisfied_by` references may need update when the fixer touches a sensory entry.

  The fix is a single instruction in the Phase 5b fixer dispatch protocol: when the fixer makes
  changes to any sensory entry (RECAST, REWRITE, DELETE), it must check whether any open or
  satisfied grounding-ledger entry has `satisfied_by` pointing to the modified entry. If so:
    - RECAST (same entry id, new content): update the grounding-ledger `satisfied_by` to confirm
      the recast still satisfies the grounding requirement, or downgrade to `status: open` if the
      recast no longer serves the GROUNDING-REQUIRED purpose.
    - DELETE: check whether the deleted entry was the grd-NNN-satisfying entry; if so, the ledger
      entry reverts to `status: open` and must be re-satisfied before Phase 4.6 / Phase 5 pass.

  This is the same coupled-record-update discipline that /and-write Phase 6 applies when modifying
  bones that carry dialogue citations: the citation tokens must be updated when the bone changes.
  The grounding-ledger's `satisfied_by` is the ledger analog of those citation tokens.

  Recurrence count: 1 (first live chapter with a grounding-ledger under fixer operations). The
  grounding-ledger mechanism is new (PROP-0022, 2026-05-29); no prior chapter was in a state
  where the fixer touched a ledger-referenced sensory entry. Proposing at first occurrence because:
  (a) Deterministic recurrence: every future fixer recast of a grounding-ledger satisfied_by
      target will produce stale `satisfied_by`. This is not a probabilistic coincidence — it is
      a direct consequence of the fixer not knowing the ledger coupling exists.
  (b) The ledger mechanism is brand new — this is the first live test; a first-occurrence proposal
      is appropriate to close the design gap before it accumulates across chapters.
  (c) S-cost: one coupled-record-update instruction added to the Phase 5b fixer dispatch brief.
      The fixer already receives facet files + auditor report; adding the grounding-ledger to the
      fixer's payload + a one-paragraph update-check instruction is the minimum fix.

  Note on the auditor's Phase 5 STRUCTURAL class: the grounding-ledger's satisfied_by staleness
  is not currently in scope for the STRUCTURAL scan (which checks schema/format/integrity of
  facet entries, not ledger-facet coupling). Adding a STRUCTURAL check for stale satisfied_by
  references is a possible secondary fix, but the primary gap is the fixer brief — if the fixer
  updates the ledger correctly, there is nothing for the STRUCTURAL scan to find. The fixer-brief
  fix is the minimum-blast-radius closure.

evidence_refs:
  - "active-project/staff/audience/facets-audience-gate-r1.md — §B sensory FAIL: sensory:4@22 is a
    grd-002 licensed-grounding entry; fix: 'recast the modality to a discrete proprioceptive or
    sound event... preserve the grd-002 grounding (cap-exempt, keep the licensed-grounding-exception:
    grd-002 tag)' — the callout preserves the grounding requirement, but the fixer's recast must
    update the satisfied_by pointer"
  - ".claude/commands/and-facets.md — Phase 4.6 Step 1: 'Re-run build_cite_index.py. Stamp each
    satisfied ledger entry satisfied + satisfied_by.' — shows satisfied_by is set at Phase 4.6;
    Phase 5b fixer dispatch has no corresponding update-check instruction"
  - ".claude/commands/and-facets.md — Phase 5b remediation cycle §fixer dispatch: 'Dispatch fixer
    with the consolidated callouts + the facet rubrics. Fixer routes per-entry' — grounding-ledger
    not listed as a fixer input artifact; no coupled-record-update instruction"
  - ".claude/commands/and-facets.md — Phase 5 auditor inputs: 'Grounding-ledger: active-project/
    staff/showrunner/grounding-ledger-<book>-<chapter>.md if present' — ledger is in auditor payload
    but not explicitly in the fixer payload"
  - "staff/admin/decisions.md — DEC-0055 (pattern 3 analysis: deterministic recurrence; first-occurrence
    override justified by new mechanism + deterministic gap)"
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 5b remediation cycle section, in the fixer dispatch
  block (the paragraph that reads "Dispatch fixer with the consolidated callouts + the facet
  rubrics..."), add the grounding-ledger to the fixer's required payload and add a coupled-record
  update instruction:

  CHANGE 1 — Add grounding-ledger to the fixer dispatch payload:

    Current fixer payload (inferred from command body):
      - consolidated audience-gate callouts (deduped per §Consolidated callouts structure)
      - facet rubrics for the affected facets
      - Phase 5 audit report (final cycle)

    Proposed addition to payload:
      - **Grounding-ledger (if present):** `active-project/staff/showrunner/grounding-ledger-<book>-<chapter>.md`
        Include on every fixer dispatch, not just when a sensory callout is present. The fixer
        cannot know whether a callout touches a ledger-referenced entry without reading the ledger.

  CHANGE 2 — Add a coupled-record update instruction to the fixer's remediation scope:

  After the existing per-entry routing instructions ("small revisions to the facet file directly;
  cross-facet conflicts to the responsible author via Agent"), add:

    **Grounding-ledger coupling check (mandatory when any sensory entry is modified).**

    When the fixer RECASTS, REWRITES, or DELETEs any sensory entry, it MUST:

    (1) Read the grounding-ledger for the chapter.
    (2) Check every grounding-ledger entry's `satisfied_by` field. If `satisfied_by` names the
        entry being modified (match by entry ID, e.g. `satisfied_by: sensory:4`):

        Case RECAST (same entry ID, new modality/content):
          Re-evaluate whether the recast entry still satisfies the grounding requirement the
          ledger line was opened for (the `item` + `licensed_at` fields describe the GROUNDING-REQUIRED
          finding; the satisfied entry must still provide discrete concrete grounding at the
          named anchor). If yes: update no fields other than optionally a `satisfied_by_recast: true`
          annotation. If no (the recast changes the nature of the grounding): stamp
          `status: open` + `satisfied_by: null` + add a note:
          "re-opened by Phase 5b fixer recast at [timestamp]; original satisfy source removed".
          A re-opened ledger entry is a new open GROUNDING-REQUIRED: if cycle-budget remains,
          re-dispatch the sensory author to author a replacement grounding entry; if at cap-burn,
          the entry cannot be satisfied and the chapter ships with GROUNDING-UNRESOLVED noted
          in the grounding-ledger (non-blocking — carried to /and-stitch Phase 4 as a voice-
          embodiment advisory).

        Case DELETE:
          The deleted entry can no longer satisfy the ledger requirement. Stamp
          `status: open` + `satisfied_by: null` + note: "re-opened by Phase 5b fixer DELETE at [timestamp]".
          Same routing as RECAST-no above.

    (3) If no grounding-ledger entry has `satisfied_by` matching the modified entry, no update needed.

  AUDITOR SECONDARY NOTE (optional; may be deferred to principal triage):
    Consider adding a cross-check to the Phase 5 auditor's STRUCTURAL class: for each entry in the
    grounding-ledger with `status: satisfied` and a `satisfied_by: sensory:<id>`, verify that the
    sensory facet file contains an entry with that ID and that the entry's `licensed-grounding-exception`
    tag references the correct ledger entry ID. A mismatch (entry deleted; entry ID changed; tag
    missing) is STRUCTURAL-GROUNDING-LEDGER-STALE — HARD. This makes the stale-satisfied_by
    condition self-detecting at the next Phase 5 scan, independent of whether the fixer explicitly
    updated the ledger. If accepted: adds one STRUCTURAL sub-check to the auditor scan spec with no
    other command-body changes.
    Cost if added: S. Can be accepted or deferred independently of the fixer-brief primary fix.

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

## PROP-0028

```yaml
id: PROP-0028
created_at: 2026-05-31T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c06-bone-gate-revise.md
  source_verdict: "Phase 6 revise bone-gate PASS — 1 HARD FAULT-FORM-NON-ACTION-VERB on @20 'holds the stylus' (narrow-holds-license misread; resolved in-invocation to 'stills the hand')"
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition, step 2 (verb-form SVO discipline)"
change_type: modify
rationale: |
  The narrow `holds` license in schemas/bones.schema.md permits `holds` only when (1) the
  object is a body part of the subject and the action is stillness-against-pressure, or (2) the
  object is a physical object resisting external pressure. The schema supplies one deny-list
  example: "taylor holds the ledger" (non-body-part physical object, not pressure-resisting).

  Three chapters have now produced holds-license violations, each a different sub-type:

  Occurrence 1 — b01c04: "the cooper's-yard workers hold the smallfolk-hours murmur"
    Sub-type: group subject + abstract acoustic-register object.
    Disposition: advisory flag (auditor accepted with annotation; not HARD-blocked).
    Source: bones-b01c04-2026-05-27.md (prior re-audit new-flag-002).

  Occurrence 2 — b01c07: "septon-halvard-flea-bottom holds the silence"
    Sub-type: abstraction-as-object ("the silence" is the schema's own deny-list pattern
    from the abstraction-as-object rule, but the author reached for `holds` instead of a
    schema-clean form). HARD, caught at /and-review bones.
    Source: bones-b01c07-fidelity-2026-05-30.md fault-003.

  Occurrence 3 — b01c06 revise: "taylor-hebert-kl-122ac holds the stylus"
    Sub-type: non-body-part physical object (parallel to the schema deny-list example
    "taylor holds the ledger" — a stylus is the same class as a ledger). HARD, caught at
    Phase 6, resolved in-invocation via auditor-specified recast ("stills the hand").
    Source: active-project/staff/auditor/write-b01c06-bone-gate-revise.md fault-001.

  Pattern: the screen-writer consistently over-extends the holds license beyond its two
  licensed conditions. The schema provides the rule and one deny-list example. The Phase 1
  SVO discipline brief does not supply authoring guidance on holds-license scope — the
  screen-writer must derive the license from the schema at authoring time, and the derivation
  is failing at recurrence-3.

  The gate (Phase 6 for co-bonded bones; /and-review bones for the fidelity review) catches
  correctly in all three cases. The gap is at the authoring brief: a Phase 1 note enumerating
  both conditions explicitly and providing negative examples parallel to the schema deny-list
  would prevent mis-derivation before the gate fires.

  change_type: modify (not add — the SVO discipline section already exists; this adds a
  named subsection to it); cost: S.
evidence_refs:
  - "active-project/staff/auditor/write-b01c06-bone-gate-revise.md — fault-001: FAULT-FORM-NON-ACTION-VERB on 'holds the stylus'; auditor named the two licensed conditions and the deny-list parallel; resolved in-invocation by recast to 'stills the hand'"
  - "active-project/staff/reviews/bones-b01c07-fidelity-2026-05-30.md — fault-003 (line 96-109): 'septon-halvard-flea-bottom holds the silence' HARD; auditor cited the narrow holds license and the deny-list example 'the yard holds the silence'"
  - "active-project/staff/reviews/bones-b01c04-2026-05-27.md — flag-001 (lines 819-826): 'workers hold the smallfolk-hours murmur' — extended holds license to group-subject + acoustic-register; prior auditor accepted as advisory (not HARD); /and-review critic flagged the extension as beyond the narrow body-part DO precedent"
  - "schemas/bones.schema.md line 105 — narrow holds license definition and deny-list examples: 'taylor holds the ledger', 'the yard holds the silence', 'the wards hold their positions'"
  - "staff/admin/decisions.md — DEC-0057 (process-critic dispatch; holds-license pattern confirmed at recurrence-3)"
recurrence_count: 3
proposed_diff: |
  In .claude/commands/and-write.md, Phase 1, step 2 (SVO verb-form discipline), in the section
  that describes the FAULT-FORM-NON-ACTION-VERB classification and recast guidance, add a
  named subsection after the existing stative-verb coverage:

  ---

  **`holds` — narrow license, high-failure verb.**

  `holds` is licensed only under two exhaustive conditions (from schemas/bones.schema.md):

    Condition 1: The object is a body part OF the subject AND the action is
      stillness-against-pressure. Licensed: `taylor holds the feet` (feet are Taylor's body
      part; stillness against the pull to run). `mira holds the eyes` (eyes are Mira's body
      part; stillness-against-closing).

    Condition 2: The object is a physical object resisting external pressure. Licensed:
      `the door holds` (door resisting force applied to it).

  The license is exhaustive — there is no third condition.

  Negative examples (verify your SVO before authoring — if it matches any form below, recast):
    `taylor holds the ledger` — non-body-part physical object, not resisting pressure. FAULTS.
    `taylor holds the stylus` — parallel to ledger (writing implement, same class). FAULTS.
    `the yard holds the silence` — abstraction-as-object. FAULTS.
    `the workers hold the murmur` — group subject + abstract object. FAULTS.
    `taylor holds the position` — stative holding, not physical stillness-against-pressure. FAULTS.

  Recast path when `holds` fails the license:
    - Subject's own physical stillness → bare intransitive or body-part form:
        `taylor stills`, `taylor stills the hand`, `taylor freezes`.
    - Instrument laid down / at rest → transitive resting form:
        `taylor rests the stylus`.
    - Sustained grip as action-setup → use the action verb directly
        (the bone should be the action, not the holding):
        `taylor reads the ledger` not `taylor holds the ledger`.
    - Sustained grip as load-bearing beat → use a transitive action verb:
        `grips`, `clasps`, `clutches` (all pass FAULT-FORM without the holds license).

  This guidance lives at Phase 1 because the recast must happen at bone-authoring time.
  Phase 6 will catch any slip (FAULT-FORM-NON-ACTION-VERB), but authoring against a broken
  SVO costs at minimum one fixer cycle. Author-time discrimination is cheaper.

  ---

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

## PROP-0029

```yaml
id: PROP-0029
created_at: 2026-05-31T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c06-2026-05-31.md
  source_verdict: "PASS-TERMINAL-DEPTH-RESOLVED — completeness PASS / readability AIRLESS-ABSTRACT-BY-CONTRACT. First depth-pass loop completion returning AIRLESS again; 0-mute prose-rationale-mute audit; DEC-0058 ruled Option C (abstract-by-contract, terminal)."
  gate_path: .claude/commands/and-stitch.md#phase-9
  secondary_gate_paths: [.claude/commands/and-write.md#phase-6]
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 9 — Cold-read terminal gate / Separated scoring readability axis / depth-pass disposition"
change_type: modify
rationale: |
  b01c06 is the first chapter where the depth-pass loop (URI-STITCH-COLD-READ-FEEDBACK-LOOP,
  wired by DEC-0048) ran to completion and returned AIRLESS a second time. The DEC-0048
  escalation clause — "if the next cold-read is still AIRLESS on the central event →
  FAIL/re-decompose" — was written under the premise that a second AIRLESS result would
  mean the depth pass failed to de-abstract the bones. The b01c06 run exposed a case the
  clause did not model: de-abstraction was EXHAUSTED (0-mute audit across 20 bones; every
  rationale-named concrete element staged in prose), and the persisting airlessness is
  contract-origin (offstage victims, no-choice framing, cold-utilitarian ledger register
  from cond-taylor-pov-behavior — all project-spine commitments, not rendering defects).

  Without a short-circuit for this case, the Phase 9 readability axis + DEC-0048 escalation
  clause would mechanically order a re-decompose (~40 dispatches) that hits the same contract
  wall. DEC-0007 anti-literalism + DEC-0058 blocked it this run, but the block was an
  ad-hoc admin ruling, not a mechanical gate outcome. Any future apparatus-dominant chapter
  that ships PASS-WITH-DEPTH-PASS-REQUIRED and runs its depth pass to completion against a
  contract-register bone-set will hit this exact branch — and will require a fresh admin
  ruling to avoid the same wasted cycle.

  The 0-mute audit (Step 3.5 of Phase 9) is already a Phase 9 sub-step whose result is on
  disk. Its result is mechanically determinable. The proposed short-circuit adds one
  disposition branch to the Phase 9 readability-axis composition block:

  When the Phase 9 PASS-WITH-DEPTH-PASS-REQUIRED depth-pass re-stitch cold-read returns
  AIRLESS AND the Step 3.5 prose-rationale-mute audit for the depth-pass run shows mute
  count = 0 (all rationale-named concrete elements staged in prose) AND the completeness
  axis PASSES, the Phase 9 orchestrator MUST:
    (1) Classify the result as AIRLESS-ABSTRACT-BY-CONTRACT — de-abstraction is exhausted;
        the persisting airlessness is contract-origin.
    (2) Stamp chapters[<slug>].cold_read.depth_pass_resolved = true and
        chapters[<slug>].cold_read.readability_axis.verdict = AIRLESS-ABSTRACT-BY-CONTRACT.
    (3) Return PASS-TERMINAL-DEPTH-RESOLVED (terminal verdict). The chapter ships. Do NOT
        route to /and-write revise. Do NOT re-decompose.
    (4) Surface a one-line note in the exit summary: "AIRLESS-ABSTRACT-BY-CONTRACT: all
        rationale-named elements staged (0 mutes); persisting airlessness is contract-register.
        Chapter ships. Principal may override with /and-substance contract revision."

  The re-decompose route survives for non-zero mute counts: when the mute audit finds N > 0
  muted concrete elements (rationale names X but prose does not stage X), de-abstraction is
  genuinely incomplete and the DEC-0048 escalation clause applies. The short-circuit fires
  only when mute count = 0 — de-abstraction is confirmed exhausted, not failed.

  This is change_type: modify on the existing Phase 9 readability-axis composition block.
  The detection mechanism (0-mute audit), the completeness pass, and the AIRLESS result are
  all already Phase 9 gate outputs. The modification adds one disposition branch using those
  existing outputs. No new gate, no new step, no new schema field beyond the
  AIRLESS-ABSTRACT-BY-CONTRACT verdict value added to the readability-axis classification.

  Relationship to PROP-0023: PROP-0023 targets Phase 4.6 (pre-stitch, apparatus-dominance
  qualifier on the ALIVE verdict — prevents apparatus-dominant chapters from reaching stitch
  without bone-level de-abstraction). PROP-0023 addresses the upstream case; this proposal
  addresses the depth-pass completion case. They are complementary: PROP-0023 may prevent
  some chapters from needing the depth-pass loop; this proposal handles the case where a
  chapter arrives at depth-pass completion and hits the contract wall anyway. Both can be
  accepted independently.

  Recurrence: first occurrence at depth-pass-loop completion. Proposing at first occurrence
  rather than waiting because:
  (a) The gap is deterministic. Every apparatus-dominant chapter whose contract-register
      bones cannot be de-abstracted further will hit this exact branch when the depth-pass
      loop completes. The "0 mutes but AIRLESS" state is the unambiguous mechanical indicator.
  (b) The fix uses only Phase 9 gate outputs already on disk (mute count, completeness,
      AIRLESS). No new detection mechanism required.
  (c) Without the short-circuit, the only protection against the wasted re-decompose cycle
      is an admin ruling (DEC-0007 anti-literalism applied to DEC-0048's escalation clause).
      A gate whose literal application wastes ~40 dispatches is a gate with a missing
      disposition branch.
  (d) S-cost: one conditional branch in the Phase 9 readability-axis disposition block.
  (e) The "abstract-by-contract" case is the exact exception DEC-0048's trade-off note
      anticipated ("The accounting section may be abstract-by-contract") without giving it
      a mechanical gate outcome. This proposal closes that acknowledged gap.
evidence_refs:
  - "active-project/staff/reviews/coldread-b01c06-2026-05-31.md — AIRLESS verdict on depth-pass re-stitch; 'there IS a person now… the crowd breathes' (improved); 'the moment the form arrives, the prose becomes a man describing his own bookkeeping in abstract nouns… I never feel the four names as men'; completeness PASS; CONTINUE marginal-yes."
  - "staff/admin/decisions.md — DEC-0058: 0-mute audit across 20 bones; cold-reader complaints (offstage victims / no-choice framing / ledger register) all map to project-spine commitments; Option C (accept terminal, abstract-by-contract) selected; DEC-0007 anti-literalism applied to DEC-0048 clause."
  - "staff/admin/decisions.md — DEC-0048: escalation clause 'if next cold-read still AIRLESS on central event → FAIL/re-decompose'; trade-off note anticipates 'abstract-by-contract' case but gives it no mechanical gate outcome."
  - ".claude/commands/and-stitch.md — Phase 9 Step 3.5 (prose-rationale-mute audit): already fires; already produces mute count on disk. Phase 9 readability-axis composition rule: 'AIRLESS with completeness-pass → at least PASS-WITH-DEPTH-PASS-REQUIRED' — no disposition branch for depth-pass re-stitch 0-mute result."
  - "staff/admin/process-proposals.md — PROP-0023 (Phase 4.6 apparatus-dominance qualifier; complementary upstream proposal; different target, different phase; open/untriaged)."
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-stitch.md, Phase 9, in the separated-scoring readability-axis
  composition block (the paragraph reading "AIRLESS with completeness-pass → at least
  PASS-WITH-DEPTH-PASS-REQUIRED"), add a depth-pass re-stitch sub-clause:

  CURRENT (simplified):
    AIRLESS + completeness-pass → PASS-WITH-DEPTH-PASS-REQUIRED
    AIRLESS on central event → FAIL → /and-write revise

  PROPOSED — add after the PASS-WITH-DEPTH-PASS-REQUIRED sentence:

    **Depth-pass re-stitch AIRLESS sub-clause.** Fires only in depth-pass mode
    (this /and-stitch invocation is the depth-pass re-stitch following a prior
    PASS-WITH-DEPTH-PASS-REQUIRED; detectable from
    chapters[<slug>].cold_read.depth_pass: in-progress or equivalent flag):

    When AIRLESS AND completeness PASS AND depth-pass mode is active:

    Sub-check: read the Step 3.5 prose-rationale-mute audit result for this run.

    Case A — mute count = 0 (all rationale-named concrete elements staged in prose):
      De-abstraction is exhausted. The persisting airlessness is contract-origin.
      Classify: AIRLESS-ABSTRACT-BY-CONTRACT.
      Actions:
        1. Stamp chapters[<slug>].cold_read.depth_pass_resolved = true.
        2. Stamp chapters[<slug>].cold_read.readability_axis.verdict =
           AIRLESS-ABSTRACT-BY-CONTRACT.
        3. Return PASS-TERMINAL-DEPTH-RESOLVED. Chapter is terminal. Do NOT route to
           /and-write revise. Do NOT re-decompose.
        4. Exit summary line (mandatory):
           "AIRLESS-ABSTRACT-BY-CONTRACT: 0-mute audit confirms de-abstraction exhausted.
            Persisting airlessness is contract-register. Chapter ships terminal. Principal
            may override with /and-substance contract revision."

    Case B — mute count > 0 (N rationale-named concrete elements not staged in prose):
      De-abstraction is genuinely incomplete. Apply DEC-0048 escalation clause:
      FAIL → /and-write revise --from-signals.
      Surface the muted elements list from Step 3.5 in the FAIL exit block as the
      signal targets for the revise brief.

    Case C — Step 3.5 not run for this invocation (mute audit absent):
      Run Step 3.5 before deciding. Do not assume mute count. The sub-clause requires
      the mute-audit result to be present before it can fire.

  VERDICT ENUMERATION ADDITIONS:
    - Add AIRLESS-ABSTRACT-BY-CONTRACT to the readability-axis verdict enumeration
      alongside READABLE and AIRLESS.
    - Add PASS-TERMINAL-DEPTH-RESOLVED to the Phase 9 outcome enumeration alongside
      PASS, PASS-WITH-DEPTH-PASS-REQUIRED, and FAIL.
    Both new values fire only in depth-pass mode.

  MEMORY SCHEMA NOTE (optional, deferred to principal):
    If chapters[<slug>].cold_read.readability_axis.verdict is formally typed in
    schemas/showrunner-memory.schema.md, add AIRLESS-ABSTRACT-BY-CONTRACT to the enum.
    If chapters[<slug>].cold_read.depth_pass_resolved is a new field, add it as an
    optional boolean to the cold_read block. Cost S; can be accepted independently.

  INTERACTION WITH PROP-0023:
    If PROP-0023 is implemented, Phase 4.6 catches apparatus-dominant chapters before stitch
    and routes them upstream. Chapters that PROP-0023 catches do not invoke the depth-pass
    loop and do not trigger this sub-clause. If PROP-0023 is not implemented (open/untriaged),
    this sub-clause is the only mechanical protection against the wasted re-decompose cycle
    at depth-pass completion. The proposals are complementary; accept/defer each independently.

---

## PROP-0035

> **2026-06-01 ID-renumbering note:** allocated PROP-0030 on main 2026-05-31 (stitch-spine-staging body-act-companion proposal). Collided with session-branch PROP-0030 (cohere primitive) when session/audit-and-stitch-2026-05-31 merged 2026-06-01. Renumbered to PROP-0035 to preserve cohere PROP-0030's downstream references (PROP-0031, /and-review cohere subcommand, /and-cohere skill registration). DEC-0061 references updated accordingly.

```yaml
id: PROP-0035
created_at: 2026-05-31T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/staging-b01-c08-20260531T210000Z.md
  source_verdict: FAIL (finding-002 STAGE on @6 — s01 central-event / axis-move capability +0.5 — BLOCKING under URI-STITCH-SPINE-STAGING)
  gate_path: .claude/commands/and-stitch.md#phase-9
secondary_gate_paths:
  - .claude/commands/and-write.md#phase-6
  - .claude/commands/and-substance.md#phase-5.5
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 1 — Scene-decomposition, step 4a (held-axis coverage verification / completion gate) + Step 2 (bone-shape discipline for central-event bones)"
change_type: modify
rationale: |
  b01-c08 Phase 9 staging-review found finding-002 BLOCKING: STAGE on @6, the sole axis-move
  central-event bone (capability +0.5). The staging gap: "Taylor traces the watcher-sightlines"
  is a concrete SVO; the bone's cognitive sequence (traced → resolved → slotted) is faithfully
  rendered at stitch. What is absent: the physical act of Taylor's body during the trace. The
  rendered prose gives a cognitive sequence without any physical correlate — no locomotion, no
  stillness, no physical arrest that marks the moment the overlay slots. The staging reviewer
  correctly diagnosed: "the integration should have a physical correlate on Taylor's side."

  Crucially: the voice-embodiment discipline (URI-STITCH-VOICE-EMBODIMENT, PROP-0022 /and-stitch
  Phase 4) was applied. The stitcher rendered "I traced" (person-first) with the cognitive sequence
  intact. Voice-embodiment cannot supply what the bones file did not contain. The gap is at the
  bone-decomposition layer: the central-event bone carries the cognitive/mechanism SVO but has no
  companion physical-body-act bone for the character during that mechanism. The stitcher is
  bone-faithful; no downstream phase can retroactively add a physical correlate without a bone.

  This is a distinct failure class from PROP-0024 (argument-spine interiority: abstract arrivals
  where a concrete physical act exists but the bone records the cognitive arrival instead).
  In PROP-0024, the fix is recasting the central-event bone itself to a concrete physical act.
  In this failure class, the central-event bone IS a concrete SVO (the mechanism is correctly
  stated) — what is missing is a separate body-position / body-act bone for the character DURING
  the mechanism event. "Taylor traces the watcher-sightlines" is a valid concrete SVO for an
  axis-move; the gap is that Taylor-as-body has no physical correlate at the moment of tracing.

  Recurrence across 3 chapters:

    b01c01: staging findings on central-event bones flagged body-act absence at peak moments
    (per PROP-0007 / PROP-0018 era evidence; the pattern that drove URI-STITCH-SPINE-STAGING).
    Those findings pre-dated the current proposal infrastructure; they are the founding evidence
    that URI-STITCH-SPINE-STAGING was needed at all.

    b01c05: the three-FAIL trace included staging gaps on central-event bones (Forks B+C postop;
    PROP-0019 / c05 three-FAIL evidence base). The c05 primary FAIL class was voice-abstraction,
    but the postop confirmed body-act absence at peak moments as a co-occurring pattern.

    b01c08: finding-002 STAGE on @6 (axis-move central-event; sole Δ-bone in chapter).
    finding-004 GROUND on @13 (central-event held-register foreshadow; body thin at logging moment).
    finding-006 GROUND on @20 (central-event courier-delivery; courier body absent at approach).
    3 of 4 spine-promotion findings are on central-event bones where the physical body-act at
    the peak moment is absent or thin — not because the SVO is wrong but because no bone authored
    a physical body-act companion for Taylor at the mechanism/peak moment.

  Process discrimination:

    Could a stricter URI-WRITE-EVENT-CONCRETENESS (Phase 6 HARD gate) have caught this?
    No — EVENT-NOT-CONCRETE fires when the central-event bone is NOT a concrete SVO. @6 IS
    concrete ("taylor traces the watcher-sightlines"). The gate correctly passed @6. The gap
    is not in the bone's own concreteness but in the absence of a companion body-act bone.
    EVENT-NOT-CONCRETE is a necessary but not sufficient condition for staging adequacy on
    axis-move bones.

    Could the staging-reviewer have been prompted upstream? The staging review fires at Phase 9
    (post-stitch). The only upstream gate that touches bone-completeness for central-event bones
    is Phase 6 URI-WRITE-EVENT-CONCRETENESS. Adding a companion check here — "for the
    central-event bone (BONE-CLASS: axis-move), is there at least one bone in the scene that
    records Taylor's physical body-act or body-position during the central event?" — would catch
    the gap at Phase 6, before stitch, at $2 instead of $50+.

  The fix is a Phase 1 authoring obligation and a Phase 6 verification check:

    Phase 1: when authoring the central-event bone for an axis-move scene, the screen-writer
    must ensure at least one companion bone in the scene records a physical body-act by the POV
    character during or immediately adjacent to the mechanism event. The companion bone may be
    the central-event bone itself (if the SVO is a physical act, not a cognitive-mechanism act)
    or a separate grounding bone at the same peak zone. This obligation is separate from PROP-0011
    (held-axis completion gate) — it applies to the axis-MOVE central-event bone, not held bones.

    Phase 6: add a SIGNAL check: for each bone classified as central-event in the scene-map
    (axis-move class), verify that at least one bone in the scene's peak zone carries a physical
    body-act by the named POV character. If the central-event bone's SVO is a cognitive/mechanism
    act (not a physical act) AND no companion physical-body-act bone exists in the scene's peak
    zone → BODY-ACT-ABSENT-AT-PEAK SIGNAL (HARD on second chapter-level occurrence).

  Disposition for b01c08 finding-002 + this proposal's recurrence evidence:
  This is a third-chapter recurrence of the same mechanism. The first-occurrence hold
  (non-catastrophic, wait for recurrence) does not apply at recurrence_count = 3.
  Proposing at this count is correct per the process-critic decision procedure.

  Relationship to PROP-0019 + PROP-0022:
    PROP-0019 (Phase 8.5 coherence + Phase 5.5 chunk cold-read): the coherence review (Phase 8.5)
    PASSED b01c08 correctly — it is a substance-aware reviewer who correctly identified the chapter
    as followable for a c01-c07 reader. It is not designed to catch body-staging gaps; those require
    the staging reviewer. No PROP-0019 gate failure here.
    PROP-0022 (voice-embodiment discipline at stitch): applied correctly at /and-stitch Phase 4.
    The discipline produced AIRLESS anyway because the physical correlate was not in the bones.
    PROP-0022 is correct and operating; the gap it cannot close is the one this proposal addresses.

  Question 1 resolution (Class B SHIPPED-WITH-CAVEATS vs. staging FAIL):
  The cold-read AIRLESS complaint and the staging STAGE finding on @6 are correlated but
  diagnostically distinct. The cold-reader did not say "I can't feel Taylor's body at the
  integration moment" — they said "no decision, cost, reversal, or confrontation," which is the
  design-inherent Class B staging-chapter complaint. The PROP-0018 Class B / matching-complaint
  rule correctly routes the cold-read leg to SHIPPED-WITH-CAVEATS.
  But URI-STITCH-SPINE-STAGING governs the staging-review leg independently. Finding-002 (STAGE
  on the one axis-move bone) is a separately diagnosable, addressable defect — not a
  design-inherent constraint. A staging chapter CAN have a staged body-act at its axis-move peak;
  that is not a genre requirement violation. The staging-review override of the cold-read
  SHIPPED-WITH-CAVEATS route is correct: the chapter has a diagnosable fixable gap at the
  central-event bone, not merely a design-inherent cold-reader challenge.

evidence_refs:
  - "active-project/staff/reviews/staging-b01-c08-20260531T210000Z.md — finding-002: STAGE on @6
    (s01 central-event axis-move capability +0.5); rationale: 'prose gives a cognitive sequence
    (traced → resolved → slotted) but Taylor-as-body is absent for the duration'; spine-promotion:
    YES; severity: BLOCKING."
  - "active-project/draft/b01-c08.md — @6 prose: 'I traced the sightlines through the feed...
    The sightlines resolved as a coverage already in place; my own overlay slotted in above it,
    geometric not contested.' Taylor body absent; no physical correlate for the tracing act."
  - "active-project/staff/reviews/coherence-b01-c08-20260531T210000Z.md — Phase 8.5 PASS:
    coherence reviewer confirmed WEAVE clean and FOLLOWABILITY holds; did not flag body-staging
    gap (correctly — coherence review is not a staging audit)."
  - "active-project/staff/reviews/coldread-b01-c08-20260531T210000Z.md — Phase 9 cold-read FAIL:
    CONTINUE=no; AIRLESS; complaint matches chunk_cold_read.cold_read_risk_carry VERBATIM
    ('no decision, cost, reversal, or confrontation'). Class B matching-complaint rule fires."
  - "active-project/staff/showrunner/memory.md — chapters[b01c08].chunk_cold_read.cold_read_risk_carry:
    'Cold reader (uninformed) read this as two names logged + a wider coverage map. No decision,
    cost, reversal, or confrontation'; disposition P (DEC-0060 same shape as DEC-0044)."
  - ".claude/commands/and-write.md — Phase 6 URI-WRITE-EVENT-CONCRETENESS: EVENT-NOT-CONCRETE HARD
    (central-event bone must be concrete SVO). @6 passed this gate correctly ('taylor traces the
    watcher-sightlines' is a concrete SVO). The gap is not EVENT-NOT-CONCRETE; it is absence of
    a physical body-act companion for Taylor during the mechanism event."
  - ".claude/commands/and-stitch.md — URI-STITCH-VOICE-EMBODIMENT (PROP-0022, Phase 4): applied
    at stitch; 'I traced' renders person-first correctly. Voice-embodiment cannot supply a body-act
    that the bones file did not contain."
  - "staff/admin/process-proposals.md — PROP-0024 (argument-spine interiority: abstract arrivals
    on spine bones; Phase 1 step 2 + Phase 6 HARD). Distinct from this proposal: PROP-0024 fixes
    bones where the SVO records an abstract cognitive arrival instead of a concrete physical act;
    this proposal adds a companion body-act bone requirement for bones where the SVO IS concrete
    but the physical body-during-the-mechanism is unaddressed in the decomposition."
  - "staff/admin/process-proposals.md — PROP-0011 (held-axis completion gate; Phase 1 step 4a).
    This proposal extends the completion-gate pattern to central-event axis-move bones; a
    companion body-act bone for the axis-move peak is a separate requirement from held-axis
    witnessing."
recurrence_count: 4
recurrence_refs:
  - "b01c01 era: staging findings on central-event bones (body-act absent at peak) pre-dated
    proposal infrastructure; founding evidence for URI-STITCH-SPINE-STAGING. Not a formal
    report reference — see PROP-0018 era discussion."
  - "b01c05 three-FAIL trace (PROP-0019): Forks B+C postop converged on body-act absence at
    peak moments as a co-occurring pattern alongside voice-abstraction primary class. Second
    chapter-level occurrence."
  - "active-project/staff/reviews/staging-b01-c08-20260531T210000Z.md — finding-002 (@6 axis-move
    central-event), finding-004 (@13 central-event foreshadow), finding-006 (@20 central-event
    courier-delivery): 3/4 spine-promotion findings on central-event bones with absent/thin
    physical body-act at peak moment. Third chapter-level occurrence."
  - "active-project/staff/auditor/write-b01c09-bone-gate.md — signal-001 (CORROBORATING, NOT a
    new failure): s02 central-precursor bone n09 'the insect-feed returns corwick' is an
    instrument/perception-class SVO (feed-interaction verb 'returns' = cognitive/mechanism per
    this proposal's detection heuristic). The bone-gate ACCEPTED it with a /and-stitch Phase 4
    render-physical advisory, explicitly on the basis that companion bones n04 ('corwick faces
    the second man') and n05 ('corwick squares the shoulders') carry concrete physical body-acts
    in the ±2 peak zone — i.e. the SW-3 split satisfies exactly the body-act-companion condition
    this proposal codifies. This case is EVIDENCE THAT THE PROP-0035 MECHANISM IS CORRECT, not a
    gap it misses: under PROP-0035 the Phase 6 BODY-ACT-ABSENT-AT-PEAK SIGNAL would have fired on
    n09 and then cleared on companion-presence, converting the current ad-hoc 'FLAG accepted with
    rationale' into a mechanical 'SIGNAL evaluated, cleared by n04/n05.' The caller's framing
    question ('should the bone-gate require the central-precursor bone ITSELF to be concrete
    rather than lean on neighbors?') is answered NO by this proposal's accepted design: the
    SW-3 feed-surface→physical-signature split intentionally places the concrete act on the
    companion bones. Fourth chapter-level occurrence of the central-event cognitive/mechanism SVO
    + companion-dependency pattern; no new proposal authored (admin process-critic, 2026-06-01,
    /and-write b01c09 Phase 6.5)."
proposed_diff: |
  CHANGE 1 — .claude/commands/and-write.md, Phase 1, Step 2 (bone-shape discipline):

  In the description of the axis-move / central-event bone shape, after the existing instruction
  to author the central-event bone as a concrete SVO (URI-WRITE-EVENT-CONCRETENESS), add:

    **Central-event body-act companion obligation (applies when axis-move SVO is a
    cognitive/mechanism act).** When the central-event bone's SVO is a cognitive or mechanism
    act (e.g., "taylor traces the sightlines," "taylor logs the name," "taylor attaches the
    courier-name," "the feed resolves the coverage"), the screen-writer MUST ensure at least one
    companion bone in the scene's peak zone records a physical body-act by the POV character
    during or immediately adjacent to the mechanism event.

    The companion bone is NOT required if the central-event bone's SVO is already a
    physical act (e.g., "taylor strikes the courier," "taylor closes the register"). In
    that case, the SVO itself carries the body-act and no companion is needed.

    The companion bone MAY be:
      - A dedicated grounding bone immediately preceding or following the central-event bone,
        whose SVO records Taylor's physical position, movement, or sensory engagement during
        the mechanism (e.g., "taylor stills at the junction corner," "taylor's step slows
        at the integration close").
      - An existing bone in the peak zone that carries a physical body-act at the same
        temporal position (an overlap is acceptable; the companion does not have to be
        authored de novo if an adjacent grounding bone already fills the slot).

    Body-act companions must be authored at Phase 1; they cannot be added retroactively by
    the stitcher (voice-embodiment at Phase 4 cannot supply a body-act that the bones file
    does not contain). If the scene's peak zone currently has no physical body-act bone for
    Taylor at the mechanism moment, add one before exiting Phase 1.

    This is separate from PROP-0011 (held-axis completion gate): held-axis witnessing
    covers axes in axes_held[]. This obligation covers the axis-move's central-event bone
    and applies to the moving bone's physical body-act, not held-axis witnessing.

  CHANGE 2 — .claude/commands/and-write.md, Phase 1, Step 4a (completion gate):

  In the held-axis coverage verification block (step 4a), add a parallel check:

    **Central-event body-act companion check (new, fires alongside held-axis check).** For
    each scene, identify the central-event bone (scene-map classification: axis-move). If the
    central-event bone's SVO is a cognitive or mechanism act (not a physical act), verify:

      count(bones[scene_peak_zone] where SVO is a physical-body-act by POV character) >= 1

    If count == 0: author a companion grounding bone at the axis-move peak before
    exiting Phase 1 (per the body-act companion obligation in Step 2 above).

    If no central-event bone exists in the scene (held-discipline scene with no axis-move):
    this check does not fire. Skip with a note: "scene <slug> has no axis-move; body-act
    companion check skipped."

  CHANGE 3 — .claude/commands/and-write.md, Phase 6 HARD/SIGNAL classification table:

  Add one new SIGNAL entry (after EVENT-NOT-CONCRETE):

    | BODY-ACT-ABSENT-AT-PEAK: the central-event bone's SVO is a cognitive or mechanism act
    AND no companion physical-body-act bone exists for the POV character in the scene's
    peak zone (±2 bones of the central-event bone). This check fires only on the central-
    event bone(s) identified in the scene-map. | SIGNAL (HARD on second chapter-level
    occurrence in the project) |

  Detection logic:
    1. Read the scene-map for the current scene. Identify bones classified as central-event
       (axis-move class).
    2. For each such bone B: check whether the SVO is a physical act or a cognitive/mechanism
       act. Heuristic: if the verb is an act of perception, processing, logging, tracing, or
       feed-interaction (e.g., traces, logs, reads, marks, attaches, resolves, notes), it is
       cognitive/mechanism. If the verb is locomotion, physical contact, physical arrest, or
       sensory engagement (e.g., strikes, stills, steps, sets, fixes, turns, positions), it
       is physical.
    3. If cognitive/mechanism: scan bones within ±2 positions of B for a physical body-act
       SVO by the POV character. If none found → BODY-ACT-ABSENT-AT-PEAK SIGNAL.

  Disposition: SIGNAL on first chapter-level fire (records, passes). Auditor reports:
    "BODY-ACT-ABSENT-AT-PEAK: @<N> (central-event, axis-move, <axis>) has cognitive/mechanism
    SVO '<verb>' with no physical body-act companion in ±2 bones. The stitcher cannot supply
    a body-act that the bones file does not contain; a body-act companion is needed for the
    staging reviewer to find physical grounding at this peak. Consider adding a grounding bone
    at @<N-1> or @<N+1>."
  HARD disposition activates on the second chapter-level BODY-ACT-ABSENT-AT-PEAK occurrence
  in the project (same graduation logic as PROP-0007 compound-noun-density).

  SCOPE NOTE:
  This check applies only to central-event bones in axis-move scenes. It does NOT apply to
  held-axis central-event bones (bones marked as central-event in held-discipline scenes with
  no Δ). For held-discipline central-event bones, the finding-004 and finding-006 GROUND class
  (finding specific to @13/@20 in b01c08) is a staging-reviewer call, not a Phase 6 gate —
  held-discipline bones have fence constraints that limit how much body-grounding can be added,
  and those fences are scene-map mediated, not Phase 6 detectable without reading the full
  scene-map contract. The Phase 6 check targets the unconstrained case: the axis-move central-
  event bone where the mechanism SVO is cognitive and no physical body-act bone is present.

  PRECEDENCE NOTE re URI-STITCH-SPINE-STAGING vs. Class B / PROP-0018 matching-complaint rule:
  The Class B + matching-complaint → SHIPPED-WITH-CAVEATS rule governs the cold-read leg of
  Phase 9 (Step 1). The URI-STITCH-SPINE-STAGING rule governs the staging-review leg (Step 3).
  These are independent diagnostic legs. A STAGE finding on the axis-move central-event bone
  is not "the cold-read complaint repeating itself" — it is a separately diagnosable structural
  gap. The staging FAIL correctly overrides the cold-read SHIPPED-WITH-CAVEATS routing because
  the chapter has a fixable bone-level gap (body-act absent at @6), not merely a design-inherent
  cold-reader challenge. The Class B matching-complaint rule was designed for DESIGN-INHERENT
  failures (c05: register fatigue, genre-seam). This failure class (absent body-act companion at
  axis-move peak) is NOT design-inherent — it is diagnosable and addressable at bones-revise.
  No change to PROP-0018's Class B rule or the matching-complaint disposition is proposed.

cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```

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

## PROP-0030

```yaml
id: PROP-0030
created_at: 2026-05-31T22:00:00Z
created_by: principal-directed session cold-read of combined b01 c01-c07 sub-section
trigger:
  reason: on-demand (session audit; not a chain-verdict trigger)
  source_report: active-project/draft/_combined-b01-c01-c07-audit.md
  source_verdict: session:cross-chapter-apparatus-register-accumulation
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 4.5 — completeness + aliveness scoring; Phase 9 — cold-read terminal gate"
change_type: modify
rationale: |
  PROP-0022 (aliveness twin) is wired across /and-stitch Phase 4 voice-embodiment +
  Phase 4.5 separated-axis scoring + Phase 9 cold-read terminal gate. Live-test results:
    - c05 (retroactive) — ALIVE verdict, the chapter shipped clean.
    - c06 (first live) — false-ALIVE; PROP-0023 opened to catch apparatus-dominant
      whole-chapter at bone-level before stitch.
    - c07 (second live) — PASS-WITH-CAVEATS / AIRLESS-at-the-edge; depth-pass
      recommended at parking-lot pl-2026-05-31-001.
  Session 2026-05-31 cold-read of c01-c07 as a continuous sub-section identifies a
  failure class neither PROP-0022 nor PROP-0023 surfaces: apparatus-register
  ACCUMULATES across chapters even when each individual chapter scores ALIVE in
  isolation. The cold reader notices c02-c05 read as a stretch of operating-instruction
  prose only when held against c01 prologue prose + c07 ledger-stylus prose — the
  contrast surfaces what chapter-isolated reading does not.

  Current Phase 4.5 + Phase 9 scoring run per chapter. A chapter that holds up under
  isolated cold-read can still degrade a multi-chapter run. The failure shape is
  cumulative load on a register that any single chapter sustains without protest.

  PROP-0023 catches apparatus-dominant whole-chapter at bone level (de-abstraction
  required before ALIVE verdict can fire). PROP-0030 is the orthogonal axis: even
  chapters that PASS PROP-0023 can accumulate cross-chapter aliveness debt. The two
  proposals are complementary; PROP-0023 protects single-chapter readability,
  PROP-0030 protects sub-section readability.

  First-occurrence proposing rationale: (a) the mechanism is precisely discriminated
  (per-chapter scoring blind to cross-chapter accumulation); (b) the evidence is a
  cold-read of seven shipped chapters held against each other, not a single reviewer
  taste-flag; (c) the cost shape is M (new optional /and-review pipeline + cohere
  subcommand machinery — design overlap with the PROP-0031 sub-section coherence
  process queued same session); (d) the failure is silent in the existing gates by
  construction.
evidence_refs:
  - "active-project/draft/_combined-b01-c01-c07-audit.md — §Where the prose fails item 1 (apparatus-register dominates the middle); cross-references items 2 (sensory grounding named but not embedded) + 10 (dialogue sparse compounds apparatus problem)"
  - "active-project/draft/b01-c01.md through b01-c07.md — seven shipped chapter drafts; c02-c05 are the load-bearing evidence stretch"
  - "staff/admin/process-proposals.md — PROP-0022 (aliveness twin, wired); PROP-0023 (false-ALIVE bone-level, open-pending-principal-triage)"
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-05-31-009 (cross-chapter aliveness scoring question surfaced to /and-review pipeline)"
  - "active-project/staff/reviews/coldread-b01c09-20260601T163000Z.md — fourth consecutive chapter (c06/c07/c08/c09) drawing a tentative-or-worse uninformed cold-read (NO-CONTINUE) and shipping via Class-B risk-recorded path (DEC-0058/0060/0062/0066). Per-chapter gates all clean; cold-read NO-CONTINUE is the cross-chapter accumulation signal. This is the recurrence that makes the triage of PROP-0030 urgent: the mechanism is now confirmed across four chapters, not merely an artifact of the c01-c07 session audit."
  - "active-project/staff/reviews/coldread-b01-c10-2026-06-02.md — fifth consecutive chapter (c06/c07/c08/c09/c10) drawing an apparatus-airless cold-read ('dense and repetitive, arm's-length throughout; barely yes'). c10 chunk_cold_read was PASS-CHUNK-VOICE-RISK with airlessness flagged design-inherent for the climax; per-chapter Phase 9 verdict PASS-WITH-DEPTH-PASS-REQUIRED. DEC-0070 merged this as third cross-chapter recurrence (DEC-0067 N=4; now N=5; threshold for new accumulation-warning proposal per DEC-0067 is N=6). Per-chapter gates remain clean; the accumulation failure class is invisible to chapter-isolated scoring by construction."
  - "active-project/staff/auditor/write-b01c11-bone-gate.md (report not on disk — sourced from dispatch context) — sixth recurrence point: b01c11 (silent/observational rising chapter, 27 bones, no dialogue) fired ABSTRACTION-DOMINANT on s02 (insect-feed relay + timestamp sequence; architecture-licensed-abstract) and s03 (5-bone routing-decision beat; central event is behavioral ABSENCE). Both dispositioned ACCEPTED-with-rationale, carry to /and-stitch Phase 4 physical-materiality. Audience 3/3 SUBSTANCE-FELT all scenes. Chapter PASS. Second consecutive abstract chapter (c10+c11). DEC-0073 merged as fourth cross-chapter recurrence (N=6; now at the threshold DEC-0067 named for a potential new accumulation-warning proposal). Per-chapter gates functioning correctly; accumulation is invisible to chapter-isolated scoring by construction."
recurrence_count: 4
proposed_diff: |
  PRIMARY CHANGE — new /and-review subcommand: `cohere`

  Add a `cohere` subcommand to /and-review (per /and-review router pattern). Invocation:

    /and-review cohere <book> [<from-chapter>-<to-chapter>]

  When called without a range: defaults to all shipped chapters of the named book.
  When called with a range: cold-reads the named chapter window as a sub-section.

  Phases:
    Phase 0: validate (chapters in range are shipped to draft/); parking-lot scan;
             concatenate draft/<book>-c<XX>.md files into a working combined file at
             active-project/staff/reviews/cohere-<book>-<range>-<ts>.combined.md.
    Phase 1: dispatch a single naive cold-reader against the combined file (one
             impersonator load of the naive-reader persona — same persona as the
             routine /and-postop fork). Prompts target cross-chapter axes specifically:
               - Q1 voice/register consistency across the stretch
               - Q2 setup→payoff: which beats land, which drop
               - Q3 calendar/time legibility
               - Q4 character-presence accumulation (who arrives cold; who is felt as
                 carried)
               - Q5 sensory texture distribution (where the prose embeds vs lists)
               - Q6 apparatus-register cumulative load (the load-bearing question)
               - Q7 "does this feel like a sub-section of a book or seven shipped
                 chapters with prologue glue"
             Verdict shape per question: PASS / CAUTION / FAIL with one-paragraph
             evidence excerpt + line reference.
    Phase 2: dramatist axis — same combined file, structural-shape review across the
             window (arc legibility; promise/payoff inventory; antagonist pressure
             curve sustained or fragmented).
    Phase 3: audience fork — one of the three project audience personas (rotating;
             tracked in active-project/audience/<slug>/cohere-history.md to round-
             robin); reviews the stretch with the persona's substance-felt axes
             extended to multi-chapter (cross-chapter substance accumulation).
    Phase 4: aggregate. Verdict shape:
               - PASS-COHERE — all three forks PASS; no chapter revises required.
               - CAUTION-COHERE — at least one CAUTION; advisory parking-lot entries
                 written but no blocking action; sub-section ships.
               - FAIL-COHERE — at least one FAIL on a load-bearing axis (Q2 setup→
                 payoff drop on a structural beat; Q6 apparatus-register exceeds
                 sustainable density). Routes to the new PROP-0031 cohere-iterate
                 process (drafted same session): chapter-revise queue authored as
                 parking-lot HARD items targeting /and-write revise on the named
                 chapters; on revise + re-cascade completion, /and-review cohere
                 re-runs.
    Phase 5: persist. Writes
               - active-project/staff/reviews/cohere-<book>-<range>-<ts>.md (verdict +
                 evidence)
               - chapters[<slug>].cohere_review for each chapter in the range
                 (audit trail per chapter)
               - parking-lot entries for any FAIL-COHERE chapter-revises required
    Phase 5.5: admin process-critic (always-fires; same pattern as /and-postop 3.5).
    Phase 6: summary.

  Gates:
    - FAIL-COHERE HARD-routes to chapter-revise queue; the cohere verdict is NOT a
      ship-gate on the individual chapters (they already shipped). It IS a gate on
      shipping the sub-section as a sub-section of the book.
    - CAUTION-COHERE never blocks; it surfaces.

  Pattern: cohere is to the sub-section what /and-postop is to a single chapter —
  depth-of-quality check, not the primary ship gate. The primary ship gate stays at
  /and-stitch Phase 9 cold-read terminal gate (PROP-0022). PROP-0030 adds a layer
  above it for multi-chapter accumulation.

  RENDERER-MINIMAL MIRROR: none. cohere is review-only, no rendering.

  MEMORY SCHEMA NOTE (optional, deferred to principal):
    Add `cohere_review` block to chapters[<slug>] schema in
    schemas/showrunner-memory.schema.md (verdict, report_path, ts). Cost S.

  INTERACTION WITH PROP-0022 / PROP-0023:
    - PROP-0022 (chapter-isolated aliveness scoring) — unchanged; remains the primary
      per-chapter readability gate at /and-stitch.
    - PROP-0023 (bone-level apparatus-dominant catch) — unchanged; remains the
      pre-stitch upstream cure.
    - PROP-0030 — cross-chapter accumulation cure; runs after N chapters ship.
    All three are complementary. None of them subsumes another.

  INTERACTION WITH PROP-0031 (cohere-iterate process, drafted same session):
    PROP-0031 is the iteration-to-positive loop. PROP-0030 is the cold-read primitive
    that surfaces holes. The cohere subcommand of /and-review is the surfacing
    machinery; the cohere-iterate process is the convergence loop. Accept PROP-0030
    independently; PROP-0031 is opt-in on top of it.

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

## PROP-0031

```yaml
id: PROP-0031
created_at: 2026-05-31T22:00:00Z
created_by: principal-directed session (sub-section coherence process design)
trigger:
  reason: principal directive — "Draft process that will stitch chapters together, identify and plug holes in narrative, and then ensure readability is high. Cold reads must pass with positive content. If not, iterate in fixing the material until all reviews are positive."
  source_report: active-project/staff/showrunner/subsection-coherence-process-plan-2026-05-31.md
  source_verdict: principal-directive
target:
  type: command
  path: .claude/commands/and-cohere.md  # new command
  section: full command body
change_type: add
rationale: |
  PROP-0030 adds /and-review cohere as a single-pass cold-read primitive. PROP-0031
  wraps it in an iteration-to-convergence loop: /and-cohere <book> [range] runs the
  cold-read, dispatches the chapter-revise queue, re-cascades the affected chapters
  through /and-write revise → /and-facets → /and-stitch, and re-runs /and-review
  cohere until either PASS-COHERE or the cap (default 3 iterations) is hit.

  Justifies as a separate command (not a subcommand of /and-review) because:
    - /and-review is read-only by design; cohere-iterate is read-then-mutate.
    - The iteration loop spans multiple cascade re-runs and needs its own state file
      (iteration counter, per-iteration verdict log, convergence trace).
    - Convergence cap + escalation belongs in command-body orchestration, which
      /and-review explicitly does not own.

  First-occurrence proposing rationale: (a) the mechanism is precisely the principal
  directive shape — stitch → identify holes → plug → iterate until positive; (b) the
  cost is M-L (command body + state file + cap logic + interaction with /and-write
  revise machinery, but most of the consuming machinery already exists); (c) the
  failure-on-no-PROP path is "no convergence loop exists, sub-section ships with
  whatever holes /and-review cohere surfaced once" — which is acceptable as a
  graceful degradation but loses the iteration leverage the principal asked for.
evidence_refs:
  - "active-project/staff/showrunner/subsection-coherence-process-plan-2026-05-31.md — process design draft (this session)"
  - "staff/admin/process-proposals.md — PROP-0030 (cohere primitive, paired)"
  - "active-project/draft/_combined-b01-c01-c07-audit.md — surfaced holes the iteration loop would plug"
  - "active-project/staff/reviews/coldread-b01c09-20260601T163000Z.md — fourth consecutive chapter (c06/c07/c08/c09) shipping via Class-B risk-recorded path. The accumulation of depth-pass-pending flags (4 chapters simultaneously) is exactly the sub-section-coherence debt the /and-cohere iteration loop exists to converge. This is the second cross-chapter recurrence (c01-c07 audit + c06-c09 pattern) strengthening the case for triaging PROP-0031."
  - "active-project/staff/reviews/coldread-b01-c10-2026-06-02.md — fifth consecutive chapter (c06-c10) in the apparatus-register accumulation sequence; cold-read 'dense and repetitive, arm's-length throughout; barely yes.' Depth-pass-pending flags now at N=5. DEC-0070 merged as third cross-chapter recurrence. The /and-cohere iteration loop is the designed convergence path for depth-pass-pending debt of this scale; triage urgency increases at N=5 (threshold for new accumulation-warning proposal is N=6)."
  - "active-project/staff/auditor/write-b01c11-bone-gate.md (dispatch context) — sixth chapter in apparatus-register accumulation sequence (c06-c11). b01c11 ABSTRACTION-DOMINANT on s02 + s03, both accepted-with-rationale, audience 3/3 SUBSTANCE-FELT. Second consecutive abstract chapter (c10+c11). Depth-pass-pending flags at N=6 (the DEC-0067 threshold for a new accumulation-warning proposal, but DEC-0073 judges the existing accept-with-rationale + stitch-carry path is functioning correctly and the cohere iteration loop is the designed convergence path). DEC-0073 merged as fourth cross-chapter recurrence."
recurrence_count: 4
proposed_diff: |
  PRIMARY CHANGE — new command body at .claude/commands/and-cohere.md.

  Phases (sketch — full body to be authored at acceptance):

    Phase 0: validate. Args: <book> [<from-chapter>-<to-chapter>]; default range =
             all shipped chapters of the named book. Read showrunner memory,
             parking-lot, iteration state. If a prior /and-cohere iteration is
             open on the same range, resume from its checkpoint.

    Phase 1: dispatch /and-review cohere <book> [range] (PROP-0030).

    Phase 2: gate on verdict.
               - PASS-COHERE — write convergence record; exit success.
               - CAUTION-COHERE — write advisory record; exit success unless
                 --strict (strict treats CAUTION as iterate).
               - FAIL-COHERE — proceed to Phase 3.

    Phase 3: triage. Read /and-review cohere's chapter-revise queue from the
             parking-lot HARD items it just authored. For each item:
               - Group by chapter (one item may cite multiple chapters; one chapter
                 may receive multiple items).
               - Order by dependency (e.g. plant Wren in c03 BEFORE revising c06's
                 cost-bearer reception).
               - Reject items the principal has previously dismissed (read
                 staff/admin/decisions.md for prior cohere dispositions on this
                 book).

    Phase 4: execute. For each chapter in the queue:
               (a) /and-write <chapter> revise --from-signals (or --cohere-driven
                   if a cohere-revise mode is added — phase-internal flag).
               (b) /and-review bones (mandatory gate; per existing chain).
               (c) /and-facets <chapter> (re-cascade).
               (d) /and-stitch <chapter> (re-cascade; terminal gate).
             Failures at any sub-phase bubble up; the cohere iteration enters a
             held state and surfaces the failing chapter for principal triage
             (auto-escalation, no infinite loop).

    Phase 5: re-run /and-review cohere. Compare verdict to prior iteration.
               - If improved (FAIL → CAUTION, CAUTION → PASS, etc.) — continue
                 the loop.
               - If unchanged or regressed — admin process-critic fires
                 (mandatory; reason: cohere-iteration-not-converging); proposal
                 likely generated for the principal.

    Phase 6: convergence cap. Default 3 iterations. On cap-hit without PASS:
               - Write final verdict CAP-HIT (advisory).
               - Surface the unresolved chapter-revise queue.
               - admin process-critic fires.
               - Exit to principal triage. Do NOT auto-revise indefinitely.

    Phase 7: persist. Write
               - active-project/staff/cohere/<book>-<range>-<ts>/iteration-log.md
               - chapters[<slug>].cohere_iterations for each touched chapter
               - parking-lot resolutions for items the iteration plugged

    Phase 7.5: admin process-critic (always-fires).

    Phase 8: summary.

  Flags:
    --strict — treat CAUTION-COHERE as iterate (default: PASS on CAUTION).
    --max-iter N — convergence cap override (default 3; max 5).
    --range <from-c>-<to-c> — restrict cohere range (default = all shipped chapters).
    --dry-run — Phase 1 only; do not enter revise loop.

  STATE FILE: active-project/staff/cohere/<book>-<range>-state.md tracking
  iteration counter, last verdict, queued revises, convergence trace.

  INTERACTION WITH /and-substance --cascade:
    /and-cohere is downstream of /and-substance. A book-level cascade runs
    /and-substance chapter → /and-write → /and-facets → /and-stitch per chapter;
    /and-cohere runs after N chapters have shipped and explicitly does not
    interleave with single-chapter cascades.

  INTERACTION WITH /and-postop:
    /and-postop is per-chapter depth-of-quality (already shipped chapter).
    /and-cohere is per-sub-section depth-of-coherence (already shipped chapters
    held as a stretch). Both are optional / on-demand; both are post-ship.
    Run /and-postop per chapter for chapter-level depth; run /and-cohere per
    sub-section for sub-section-level coherence. They do not block each other.

  AMENDMENT 2026-05-31 (forward-feed channel; replaces back-prop):
    Closes the upstream/draft divergence the b01-c01-c07 session surfaced
    (session-synthesis-report-2026-05-31.md §5d) by replacing back-propagation
    with a forward-feed channel. Adds two phases to /and-cohere and one Phase 0
    contract on /and-substance chapter.

    Phase 4.5 — REVISION CLASSIFICATION (new; fires after each Phase 4 chapter
    revise, before Phase 5 re-review):
      For each chapter revised in this iteration, diff the post-revise draft
      against the pre-revise draft and classify each hunk:
        - cosmetic — sentence-rhythm, paragraph joins, redundancy cuts. No
          substance change, no reader-facing new content.
        - presentation-reinforcement — character callbacks, sensory anchors,
          calendar anchors, plant-establishing prose. Reader-facing but no
          new substance axis-movement, no new declared events.
        - substantive — new events, new axis-movement, new opposing-force
          resolution, new character introduction, declared-fact reframe.
      Classification is a small fork (haiku-class). Output appended to the
      iteration log as a per-hunk table. Substantive hunks are surfaced in
      Phase 8 summary and gate Phase 6.5 (below).

    Phase 6.5 — AGGREGATE EMIT (new; fires at PASS-COHERE, before Phase 7
    persist):
      Walks the converged stretch end-to-end and writes/updates the rolling
      forward-feed file at:
        active-project/staff/showrunner/aggregate-state.md
      Schema (sketch — full schema authored at acceptance under
      schemas/aggregate-state.schema.md):
        ---
        book: b01
        through_chapter: c07
        last_updated: <ts>
        last_cohere_run: <range>-<ts>
        ---
        # Axis state at close of c07
        - moral_framework: rank 5 (from start 2; delta +3 across stretch)
        - political_register: rank 4.5 (peaked c05 evening replay)
        - ... (one line per axis)

        # Open forward-hooks (promises not yet paid)
        - hook-<id>: <description> (origin c<MM>; expected payoff c<NN>±range)

        # Characters introduced through c07
        - <slug>: reader-legibility = <high|partial|cipher>; last appearance c<MM>

        # Terrain / calendar / prop state
        - <name>: <state> as of c07 close

        # Revision layer (substantive hunks promoted from Phase 4.5)
        - <chapter>:<hunk-id>: <description> | acknowledged: <bool>
        - ...

      Fork shape: read prior aggregate (if any) + the converged stretch +
      Phase 4.5 classifications → emit next aggregate. ~1 dispatch.

    CONTRACT ON /and-substance chapter Phase 0:
      Phase 0 reads active-project/staff/showrunner/aggregate-state.md if
      present, in addition to handoff_in from the book chunk.
        - On conflict: aggregate value wins, conflict logged in chapter chunk
          metadata. Book-chunk handoff_in stays as historical prediction.
        - On unacknowledged substantive revision-layer entries: HARD-abort
          until principal acknowledges (stamps acknowledged: true on the
          relevant entries).
        - If aggregate-state.md does not exist (cohere never fired): fall
          back to today's handoff_in-only behavior. Purely additive.

    NON-GOALS (deliberate):
      - No back-propagation to bones / facets / per-chapter chunks. The
        aggregate IS the forward-truth; upstream artifacts remain frozen at
        original ship state.
      - No automatic propagation across already-shipped chapters downstream
        of the cohere stretch. If chapters c08-c10 were already shipped
        when /and-cohere is run on c01-c07, the aggregate update fires; the
        already-shipped chapters are not retroactively re-cohered. Re-cohere
        is a separate principal-invoked run.

    INTERACTION WITH PROP-0030:
      Cohere is the *check* (PROP-0030's cold-read primitive); aggregate is
      the *feed* (this amendment). They remain complementary and
      non-overlapping. Aggregate emit fires only at PASS-COHERE — the
      converged state is the trustworthy emit point.

    COST OF AMENDMENT: small. Phase 4.5 ≈ 1 fork per chapter touched per
    iter; Phase 6.5 ≈ 1 fork per /and-cohere run; Phase 0 contract on
    /and-substance chapter ≈ a read + a conflict-log line. Schema authoring
    at acceptance. Total: still L (no commands added).

  AMENDMENT 2026-05-31 (2) — per-chapter forward-thread at /and-stitch Phase 10:
    The stretch-level amendment above closes the c01-c07-style retroactive gap.
    Per-chapter forward-threading closes the per-chapter forward gap: each
    chapter, as it ships, should already be reconciled against accumulated
    past material rather than waiting for a periodic cohere run to surface
    the misses. Adds a new terminal phase to /and-stitch.

    Phase 10 — FORWARD-THREAD (new; fires only on Phase 9 PASS or
    PASS-WITH-DEPTH-PASS-REQUIRED; on Phase 9 FAIL, skipped — failing
    chapter routes to /and-write revise per existing flow):

      Step 1 — Read accumulated past.
        Inputs (in priority order):
          (a) active-project/staff/showrunner/aggregate-state.md if present.
          (b) If absent: drafts of all prior shipped chapters in this book
              (draft/<book>-c<01..MM-1>.md). First chapter (c01) skips
              Step 1 — Phase 10 is a no-op on first chapter except for
              Step 4 (emit aggregate).

      Step 2 — Threading-review fork.
        Single dispatch (medium model). Brief:
          - Read accumulated past (Step 1 inputs).
          - Read the just-finalized current chapter draft.
          - Identify threading needs in three classes:
              * UNPAID-HOOK — forward-hook from prior chapter unaddressed
                here despite the current chapter being a natural payoff
                landing.
              * MISSED-CALLBACK — character/place/object established prior
                appears in current chapter but without callback that would
                cost-free reinforce reader-legibility.
              * STATE-DRIFT — current chapter implicitly assumes an axis
                state that the aggregate says is different (e.g., prior
                close had political_register at 4.5; current chapter
                opens treating it as 3.0).
          - For each, propose a minimal threading edit (sentence-level
            preferred; paragraph-level only when truly required).
          - Hard fence: edits must be bone-faithful. No new events. No new
            axis-movement. No new declared facts. Reinforcement and
            connective tissue only.
        Output: ranked list of proposed threading edits (max 5 per chapter
        by default).

      Step 3 — Classify-and-apply.
        For each proposed edit:
          (a) Classify per the same scheme as Phase 4.5 of /and-cohere:
              cosmetic / presentation-reinforcement / substantive.
          (b) cosmetic + presentation-reinforcement edits: apply to
              draft/<book>-<chapter>.md inline. Log to render-log.
          (c) substantive edits: DO NOT APPLY at this layer. Surface as
              parking-lot HARD items targeting either /and-substance chapter
              <slug> revise or /and-write <slug> revise (whichever the
              threading-review fork identifies as the appropriate seam).
              Substantive needs at Phase 10 indicate upstream chunk
              authoring missed the constraint; back-prop via upstream re-run,
              not at draft layer.
          (d) Edits the threading-review fork itself flagged as
              uncertain-classification: held for principal acknowledge,
              not applied.

      Step 4 — Emit/update aggregate-state.md.
        Same shape as /and-cohere Phase 6.5 emit, but scoped to "through
        current chapter":
          - Read prior aggregate (if any).
          - Compose this chapter's close-state (axis ranks at chapter close,
            new hooks introduced, characters introduced + their
            reader-legibility, terrain/calendar/prop state).
          - Append revision-layer entries from Step 3's
            presentation-reinforcement edits.
          - Write to active-project/staff/showrunner/aggregate-state.md
            with last_updated, through_chapter = current.
        First-chapter case (c01): emits the initial aggregate; no prior
        to read.

      Step 5 — Phase 10 verdict.
        - PASS-THREAD (no substantive needs surfaced; cosmetic/presentation
          edits applied) → chapter is shipped + threaded; continue cascade
          to optional postop or exit.
        - HOLD-THREAD (substantive needs surfaced; parking-lot HARD items
          written) → chapter is shipped per Phase 9 verdict but flagged
          as having unresolved upstream threading needs. /and-substance
          chapter b<NN>c<MM+1> Phase 0 reads these as part of the
          aggregate-state contract (existing in Amendment 1) and HARD-aborts
          on unacknowledged entries.

    CASCADE INTERACTION:
      Cascade includes Phase 10 automatically (it's a phase of /and-stitch).
      Under --unattended (per the cascade-unattended discipline pending
      separately): substantive surfacings at Phase 10 do not halt the
      cascade for this chapter (chapter is already shipped); they enter
      the end-of-run summary as ESCALATE items for principal review before
      next-chapter Phase 0 fires.

    INTERACTION WITH /and-cohere:
      /and-stitch Phase 10 is the per-chapter forward-feed; /and-cohere is
      the periodic stretch-level reconciliation. Both write aggregate-state.md.
      /and-cohere may overwrite or revise entries Phase 10 emitted —
      cohere has the cold-read advantage of seeing a stretch as a stretch.
      Both producers tag their entries with last_updated_by:
      {and-stitch-phase-10 | and-cohere} so the source is traceable.

    INTERACTION WITH /and-postop:
      /and-postop is post-ship depth-of-quality and is optional. Phase 10
      is in-chain and fires automatically on every PASS / PASS-WITH-DEPTH
      stitch. They do not overlap.

    NON-GOALS:
      - Phase 10 does not re-render the chapter, does not run a cold-read,
        does not re-fire Phase 9. It is a final reconciliation pass against
        accumulated past, with a hard fence at the bone-faithfulness boundary.
      - Phase 10 does not back-propagate to bones/facets. Substantive needs
        surface as parking-lot items for principal-triaged upstream re-run.

    COST: Phase 10 ≈ 2-3 dispatches per chapter (threading-review fork +
    classify-and-apply fork + aggregate-emit fork; latter two can collapse).
    Adds ~5-10% to per-chapter cost. Schema authoring for
    aggregate-state.md is shared with Amendment 1.

cost_estimate: L
status: implemented
triaged_at: 2026-06-23
triaged_by: principal (backlog reconciliation 2026-06-23)
disposition_note: "IMPLEMENTED. /and-cohere shipped (.claude/commands/and-cohere.md); PROP-0031 directive satisfied. Reconciled 2026-06-23."
pr_ref: null
defer_until: null
supersedes: null
```

## PROP-0032

```yaml
id: PROP-0032
created_at: 2026-05-31T22:30:00Z
created_by: principal-directed session (chapter-production runbook)
trigger:
  reason: principal directive — "I would like to say, do chapter xx, and then walk away while you churn through all the steps and iterations in order to craft chapter xx." Then narrowed: "you should have a single runbook that engages to produce a chapter, including the cohere and revision that happens after stitch."
  source_report: RUNBOOK.md (post-amendment); CLAUDE.md Rule 18
  source_verdict: principal-directive
target:
  type: runbook+rule
  path: RUNBOOK.md § "Producing a chapter — end-to-end protocol" + CLAUDE.md Rule 18
  section: full section + rule
change_type: add
rationale: |
  The session observed repeated mid-run halts during cascade execution caused by
  the operator (Claude) calling AskUserQuestion on prompts that should have
  routed to admin user-proxy per Rule 13, narrating gate transitions, and
  bailing on FAIL verdicts before exhausting documented cap-bounded retries.

  Principal initially asked for a --unattended flag scattered across command
  bodies plus an operator contract doc. Re-scoped on principal correction:
  "you should have a single runbook." Implementation is the runbook itself,
  not a flag — chapter production is a single canonical operation with the
  runbook owning the discipline (R1–R5) and the chain steps owning the work.

  This collapses three concerns into one document:
    (a) the "walk-away" cascade discipline (no AskUserQuestion, drive through
        gate FAILs, single end-of-run summary, silent mid-run);
    (b) the per-chapter forward-thread (Phase 10 of /and-stitch from PROP-0031
        Amendment 2) is now part of the canonical chapter-production motion;
    (c) the aggregate-state forward-feed (PROP-0031 Amendment 1) is checked
        at pre-flight and Phase 0 of /and-substance chapter.

  Tradeoff: chapter production loses opt-in semantics — every chapter-production
  invocation runs under R1–R5 discipline. This is the principal's stated
  preference: they want to say "do chapter X" and walk away, not say "do
  chapter X --unattended" and walk away.
evidence_refs:
  - "RUNBOOK.md § Producing a chapter — end-to-end protocol (newly authored this session)"
  - "CLAUDE.md Rule 18 (newly added this session)"
  - "active-project/staff/reviews/session-synthesis-report-2026-05-31.md — observed mid-run-halt failure modes"
  - "staff/admin/process-proposals.md — PROP-0031 (per-chapter forward-thread; integrated into the chain step list)"
recurrence_count: 1
proposed_diff: |
  PRIMARY CHANGE — already landed (this session):

    1. RUNBOOK.md gained a full section "Producing a chapter — end-to-end
       protocol" defining R1–R5, the pre-flight block, the chain sequence
       (with Phase 10 of /and-stitch), and the end-of-run summary format.
       Trigger map updated to point all "produce chapter X" / "do c<MM>" /
       "walk away" phrasings at this protocol.

    2. CLAUDE.md gained Rule 18 making the runbook protocol binding for
       chapter-production runs. Rule 18 supersedes any command-body behavior
       that would prompt the principal mid-run.

  NON-CHANGES (deliberate):
    - No --unattended flag on /and-substance --cascade. Cascade itself is
      unchanged; chapter production is the runbook protocol, which uses
      cascade as its backbone.
    - No per-command-body modifications. The runbook owns the discipline;
      command bodies remain authoritative on chain work.
    - No new schema. cascade-checkpoint.md continues to exist as-is.

  INTEGRATION:
    - PROP-0031 Amendment 1 (aggregate-state at /and-substance chapter Phase 0)
      is the pre-flight aggregate-state check + chain Phase 0 abort condition.
    - PROP-0031 Amendment 2 (/and-stitch Phase 10) is step 6 in the chain.
    - URI-ADMIN-PROCESS-CRITIC tail-step dispatches continue to fire as
      documented; their outputs log silently and surface in the end-of-run
      summary's process-critic line.

cost_estimate: S
status: implemented
triaged_at: 2026-05-31T22:30:00Z
triaged_by: principal-directed
disposition_note: |
  Implemented inline this session (RUNBOOK.md + CLAUDE.md Rule 18). No
  separate command-body modifications required — the runbook is the
  authoritative spec; command bodies follow on Rule 18 binding. Logged as
  status: implemented (not open) because the diff landed at proposal time
  per principal directive.
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0033

```yaml
id: PROP-0033
created_at: 2026-06-01T05:00:00Z
created_by: admin process-critic
trigger:
  reason: cohere-converged-caution
  source_report: active-project/staff/reviews/cohere-b01-c01-c07-2026-06-01T04-20-31Z.md
  source_verdict: CAUTION-COHERE (load_bearing_fails=0; all load-bearing axes PASS)
target:
  type: command
  path: .claude/commands/and-cohere.md
  section: "Phase 6.5 — Aggregate emit; Phase 2 — Gate"
change_type: modify
rationale: |
  Phase 6.5 fires only at PASS-COHERE per spec. On this first live /and-cohere
  run, the run converged to CAUTION-COHERE with load_bearing_fails == 0 — a
  stretch that is ship-clean on every load-bearing axis. The five CAUTIONs are
  all non-load-bearing advisories consistent with deliberate project structural
  choices (interior-pressure narrative shape; observation-as-control POV). The
  state file itself identifies this as a design gap worth triage.

  The consequence of the strict condition: aggregate-state.md was NOT bootstrapped
  from this converged stretch. /and-stitch Phase 10 on c08 will fall back to
  reading all seven prior chapter drafts directly (Step 1b fallback). That path
  works but is higher-cost, loses the curated synthesis the Phase 6.5 aggregate
  provides, and accumulates across every subsequent CAUTION-COHERE run.

  The strict condition was reasonable as a first-cut design (emit only when
  converged with certainty). The live evidence is that a CAUTION-COHERE run with
  zero load-bearing fails IS a converged-with-sufficient-certainty state — the
  CAUTIONs are advisory observations, not evidence that the stretch is
  unreliable as a forward-feed source.

  No existing gate was missed: Phase 6.5's condition is working as written. The
  written condition is too conservative. This is change_type: modify on the
  trigger condition in Phase 6.5 + the Phase 2 exit path.

  First-occurrence proposing rationale: (a) the gap is deterministic — every
  future CAUTION-COHERE run with zero load-bearing fails will silently skip
  aggregate-state.md emit; (b) the state file itself diagnosed the gap at ship
  time; (c) the fix is small (one-line condition change in Phase 6.5 + one-line
  change in Phase 2 exit); (d) the cost of the gap compounds across every cohere
  run that converges to CAUTION rather than PASS.

  Note: --strict mode already routes CAUTION-COHERE to Phase 3 rather than
  converging. This proposal does NOT change --strict behavior. Under --strict,
  CAUTION-COHERE is not convergence, so Phase 6.5 does not fire. The proposed
  change only affects the default non-strict path where CAUTION-COHERE == success.
evidence_refs:
  - "active-project/staff/reviews/cohere-b01-c01-c07-2026-06-01T04-20-31Z.md — verdict: CAUTION-COHERE; load_bearing_fails: 0; all load-bearing axes PASS; CAUTIONs are advisory non-load-bearing"
  - "active-project/staff/cohere/b01-c01-c07-state.md — aggregate_emit_at: null; aggregate_emit_skipped_reason identifies the strict-condition gap; design note explicitly flags this for principal triage at Phase 7.5"
  - ".claude/commands/and-cohere.md — Phase 6.5 trigger condition: 'Fires only at PASS-COHERE. Specifically: verdict_trace[-1].verdict == PASS-COHERE AND status: converged. Skipped on CAUTION-COHERE...'"
  - ".claude/commands/and-cohere.md — Phase 2 gate: CAUTION-COHERE + strict == false exits to Phase 7 (skipping Phase 6.5)"
recurrence_count: 1
proposed_diff: |
  PRIMARY CHANGE — .claude/commands/and-cohere.md, Phase 6.5 trigger condition:

  Change the fire condition from:

    Fires only at PASS-COHERE. Specifically: verdict_trace[-1].verdict == PASS-COHERE
    AND status: converged. Skipped on CAUTION-COHERE (even under --strict...),
    FAIL-COHERE, CAP-HIT, HELD.

  To:

    Fires on PASS-COHERE OR (CAUTION-COHERE with load_bearing_fails == 0).
    Specifically:
      - verdict_trace[-1].verdict == PASS-COHERE AND status: converged, OR
      - verdict_trace[-1].verdict == CAUTION-COHERE AND verdict_trace[-1].load_bearing_fails == 0
        AND flags.strict == false AND status: converged
    Skipped on:
      - CAUTION-COHERE with flags.strict == true (strict routes CAUTION to Phase 3;
        convergence not declared)
      - CAUTION-COHERE with load_bearing_fails > 0 (load-bearing axis failed; stretch
        not reliable as forward-feed source)
      - FAIL-COHERE (any load-bearing fail)
      - CAP-HIT
      - HELD

  SECONDARY CHANGE — .claude/commands/and-cohere.md, Phase 2 exit path:

  The Phase 2 CAUTION-COHERE + strict==false branch currently skips directly to
  "Phase 7 + 7.5 + 8." Split this branch on load_bearing_fails:

    - CAUTION-COHERE + flags.strict == false + load_bearing_fails == 0:
        Surface CAUTION-axes + advisory parking-lot SOFT items.
        Set status: converged, final_verdict: CAUTION-COHERE, closed_at.
        Proceed to Phase 6.5 → Phase 7 → Phase 7.5 → Phase 8. Exit success.
    - CAUTION-COHERE + flags.strict == false + load_bearing_fails > 0:
        Surface CAUTION-axes + advisory parking-lot SOFT items.
        Set status: converged, final_verdict: CAUTION-COHERE, closed_at.
        Skip Phase 6.5. Proceed to Phase 7 → Phase 7.5 → Phase 8. Exit success.
        (Aggregate emit skipped: a load-bearing axis failed; stretch not reliable
        as forward-feed source.)

  PHASE 6.5 SELF-TAG CHANGE:

  Tag the aggregate-state.md emit entry with:
    last_updated_by: and-cohere-pass  (for PASS-COHERE)
    last_updated_by: and-cohere-caution  (for CAUTION-COHERE + load_bearing_fails == 0)
  This preserves traceability for downstream consumers (/and-stitch Phase 10,
  /and-substance chapter Phase 0) to see whether the aggregate was emitted from
  a clean PASS or a converged-but-cautioned run.

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

## PROP-0034

```yaml
id: PROP-0034
created_at: 2026-06-01T05:00:00Z
created_by: admin process-critic
trigger:
  reason: cohere-converged-caution
  source_report: active-project/staff/reviews/cohere-b01-c01-c07-2026-06-01T04-20-31Z.md
  source_verdict: CAUTION-COHERE (dramatist-axis3-antagonist-pressure-curve + dramatist-axis4-scene-shape-distribution — both describe declared project design choices)
target:
  type: command
  path: .claude/commands/and-review.md
  section: "cohere subcommand — Phase 2 dramatist fork verdict rubric; Phase 4 aggregate"
change_type: modify
rationale: |
  The dramatist fork fired CAUTION on axis3 (antagonist pressure fragmented across
  chapters) and axis4 (scene-shape distribution narrow: interior+transaction dominant,
  argument scenes sparse before c07). Both findings accurately describe the project's
  structure. Both describe deliberate design choices declared at the series-level:
  interior-pressure rather than adversary-pressure narrative; observation-as-control
  POV architecture. The findings are accurate but not actionable — fixing them would
  require rearchitecting the series.

  The consequence: these CAUTIONs will recur on every future /and-review cohere run
  across every sub-section of this project. They degrade the signal/noise ratio of
  the cohere advisory record. Recurring inactionable CAUTIONs generate parking-lot
  SOFT items that cannot be resolved, and over time cause the principal to discount
  the cohere CAUTION signal generally — a signal-value erosion that is worse than
  having no caution tier.

  The discriminating criterion is: does the finding describe a structural feature
  that is explicitly licensed by the project's declared series structure? If yes,
  CAUTION is the wrong tier — CAUTION implies actionability. The correct tier is
  ADVISORY: accurate structural description, inactionable, recorded for reference,
  does not color the aggregate verdict.

  First-occurrence proposing rationale: (a) the failure mode is deterministic —
  it will fire on every future cohere run for this project's structural shape;
  (b) the discriminating criterion is mechanistically precise (licensed-by-declared-
  structure vs. departure); (c) the fix is modest and additive (a new verdict tier
  + an optional exemption mechanism); (d) recurring inactionable CAUTIONs produce
  signal-value erosion that is hard to reverse once established.

  Note: this proposal does NOT suppress CAUTIONs that represent genuine quality
  concerns. A finding that departs from the declared structure (e.g., Otto sustains
  a multi-chapter adversary arc but it resolves without cost — a broken promise, not
  a design-consistent observation) is not exempt. The exemption applies only when
  the finding is "the project is executing its declared structural shape."
evidence_refs:
  - "active-project/staff/reviews/cohere-b01-c01-c07-2026-06-01T04-20-31Z.md — axis3: 'b01 reads as interior-pressure rather than adversary-pressure narrative'; axis4: 'heavily interior+transaction; ~1 action beat, ~5 interior, ~4 transaction, ~1 argument'"
  - "active-project/staff/reviews/cohere-dramatist-b01-c01-c07-2026-06-01T04-20-31Z.md — axis3 CAUTION + axis4 CAUTION; load-bearing fail: false"
  - "active-project/staff/showrunner/memory.md — series structural choices: interior-pressure + observation-as-control POV architecture, established at /and-cast series audit"
  - "active-project/staff/reviews/cohere-b01-c01-c07-2026-06-01T04-20-31Z.md — comparison to 2026-05-31 manual convergence: 'all consistent with the project's known structural shape (interior-pressure rather than adversary-pressure narrative)'"
recurrence_count: 1
proposed_diff: |
  PRIMARY CHANGE — /and-review cohere, dramatist fork verdict rubric:

  Add an ADVISORY verdict tier to the dramatist fork. Full verdict ladder for the
  dramatist fork:

    ACCEPT   — structural feature present and functioning as designed. No concern.
    ADVISORY — structural feature accurately described; is a declared design choice
               for this project (licensed by the series structural declaration).
               Inactionable as a quality signal. Does NOT roll into the cohere
               aggregate verdict. Does NOT generate parking-lot items. Surfaced in
               the report under a dedicated `advisory_notes:` section.
    CAUTION  — structural concern that is actionable (addressable via chapter revise
               or upstream chunk revision). Rolls into aggregate → CAUTION-COHERE.
    FAIL     — structural failure on a load-bearing axis. Rolls into aggregate →
               FAIL-COHERE. Generates revise queue.

  SECONDARY CHANGE — /and-review cohere, Phase 4 aggregate aggregation rule:

  Update Phase 4 to read dramatist fork verdicts as:
    ACCEPT + ADVISORY → PASS contribution (same as ACCEPT; ADVISORY does not raise
                         the aggregate verdict)
    CAUTION            → contributes to CAUTION-COHERE
    FAIL               → contributes to FAIL-COHERE

  ADVISORY entries are collected and surfaced in the combined report under an
  `advisory_notes:` section at the bottom, separate from `caution_axes`. They do
  not appear in the `caution_axes:` frontmatter field and do not feed parking-lot
  item authoring.

  TERTIARY CHANGE — optional project-level structural exemption mechanism:

  Add an optional `cohere_structural_exemptions` block to showrunner memory (or to a
  per-project cohere rubric file at `active-project/staff/cohere/rubric.md` —
  principal's choice of home):

    cohere_structural_exemptions:
      - axis: dramatist-axis3-antagonist-pressure-curve
        licensed_by: |
          Series structure: interior-pressure narrative; observation-as-control POV.
          Adversary-pressure arc is not the project spine. Otto and other antagonists
          are episodic by design. Established at /and-cast series audit.
        verdict_floor: ADVISORY
      - axis: dramatist-axis4-scene-shape-distribution
        licensed_by: |
          Series structure: interior+transaction dominant; argument scenes sparse.
          POV narrator observes and negotiates rather than confronts. Established
          at /and-cast series audit.
        verdict_floor: ADVISORY

  When the dramatist fork's dispatch brief includes this block, it applies the
  exemption check per finding:
    - Finding maps to an exempt axis AND is consistent with the licensed_by
      description → emit as ADVISORY.
    - Finding maps to an exempt axis BUT departs from the licensed_by description
      (e.g., an adversary arc that started and then fragmented without resolution,
      creating an unresolved promise) → exemption does not apply; classify as
      CAUTION or FAIL per standard criteria.
    - Finding does not map to an exempt axis → standard criteria.

  The dramatist fork is responsible for applying the exemption check. It cannot
  be pre-computed because the finding's content (consistent vs. departure) is
  what determines eligibility.

  RUBRIC CHANGE — /and-review cohere dramatist dispatch brief:

  Add the following paragraph to the dramatist fork's dispatch brief (the instructions
  the dramatist fork receives when invoked by /and-review cohere):

    "Before writing CAUTION on any axis: check whether the finding accurately
     describes a structural feature explicitly licensed in this project's declared
     series structure (from the cohere_structural_exemptions block if present in
     showrunner memory, or from the substance signature's declared structural choices).
     If the finding is an accurate description of a licensed structural feature —
     and NOT a departure from it — classify as ADVISORY rather than CAUTION. ADVISORY
     findings are accurate observations; they are recorded for reference but do not
     indicate a quality concern. A finding that describes a departure from a licensed
     feature is not exempt and must be classified CAUTION or FAIL as warranted."

  OPEN QUESTION FOR PRINCIPAL:

  Should `cohere_structural_exemptions` live in showrunner memory or in a dedicated
  `active-project/staff/cohere/rubric.md`? Showrunner memory is already read at Phase 0
  of every cohere-adjacent command. A dedicated rubric file is more explicitly scoped
  and would age well if per-book structural choices differ (e.g., a later book shifts to
  adversary-pressure shape — the exemption would not apply and must be per-book). If
  the series structural choices are constant across all books, showrunner memory is the
  lower-infrastructure home.

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

## PROP-0036

```yaml
id: PROP-0036
created_at: 2026-06-02T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01-c10-bone-gate.md
  source_verdict: PASS (after cycle-1 fix). Process note — two full audience-trio dispatch deaths (socket-close + timeout ~41min/49 tool-uses) before split single-persona remediation succeeded.
  gate_path: .claude/commands/and-write.md#phase-6
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 4 + Phase 6 — audience review dispatches (bone-gate substance-felt trio)"
change_type: modify
rationale: |
  At /and-write b01c09 and again at b01c10, the audience-trio Phase 6 bone-gate dispatch
  (all three personas in a single agent invocation) failed catastrophically before the
  bone-gate could complete: at c09 a socket-close killed the trio mid-run; at c10 a first
  retry also failed (socket-close), then a second retry timed out at ~41 minutes / ~49
  tool-uses. Both chapters ultimately used a split single-persona remediation — 3 separate
  light dispatches, ~75-97 seconds each — that succeeded on the first attempt.

  This is the same failure mode at two consecutive chapters. The trio-in-one-agent dispatch
  is structurally unreliable for the bone-gate review: the dispatch is long-running (multi-
  scene, multi-persona, per-scene SUBSTANCE-FELT verdict across 3 reviewers), which crosses
  the socket-close + timeout threshold that isolated lightweight single-persona dispatches
  do not reach.

  The split-dispatch remediation has proven itself at both c09 and c10 with no quality loss:
  each persona reads the same bones file and produces the same SUBSTANCE-FELT per-scene
  verdicts the trio would produce; the bone-gate aggregation rule (3-of-3 ACCEPT required)
  is unchanged. The only structural difference is invocation topology: 3 x ~90sec instead
  of 1 x ~40min dispatch that may die before returning.

  The command body has no documented fallback for dispatch death, and no indication that
  the split-dispatch is the tested-and-working alternative. The fix is to retire the
  trio-in-one-agent dispatch as default in favor of per-persona dispatches at the bone-gate
  audience review phases. This does not change what is reviewed or how verdicts are
  aggregated — only that each persona is dispatched as a separate lightweight agent.

  Recurrence_count = 2 (c09 + c10 consecutive). Two consecutive chapters is sufficient to
  rule out one-off infrastructure noise. The trio-in-one-agent pattern is deterministically
  unreliable at the bone-gate scale.
evidence_refs:
  - "active-project/staff/auditor/write-b01-c10-bone-gate.md — Process notes: 'Two audience-trio dispatch deaths (socket-close + timeout) before the split single-persona remediation succeeded (c09-precedent; ~75-97s each). Recurrence of the dispatch-death failure mode (cf. pl-2026-06-01-003, c09 INCIDENT).'"
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-06-01-003: '/and-facets b01c09 — auditor + orchestrator silent-write incident' (same session as the c09 audience-trio dispatch death; confirms the dispatch-death family is recurring at c09)."
  - "active-project/staff/auditor/write-b01-c10-bone-gate.md — Audience section: all three personas returned full per-scene SUBSTANCE-FELT verdicts, coverage discipline satisfied. Split dispatch produced complete verdicts with no quality degradation vs. the trio format."
  - ".claude/commands/and-write.md — Phase 4 + Phase 6: audience review dispatches that invoke all three personas in a single agent call."
recurrence_count: 2
proposed_diff: |
  In .claude/commands/and-write.md, at each phase that invokes the audience trio in a
  single agent dispatch (Phase 4 substance-felt pre-screen and Phase 6 bone-gate trio):

  CHANGE — Default invocation topology:

  Replace the trio-in-one-agent dispatch with per-persona dispatches:

    Old: dispatch one agent with instructions to speak for all three audience personas
    and return a combined verdict block.

    New: dispatch three agents, one per persona (parallel preferred; sequential if
    parallel unavailable). Each agent receives:
      - The persona's card + persona-exemplar (resolution: project-bound -> library -> absent).
      - The bones file and scene-map facet.
      - A single-persona verdict template: per-scene SUBSTANCE-FELT or NOT-FELT with
        rationale, scene-count coverage confirmation, W1/W2/fences check, ACCEPT/FAIL.

  Aggregation is unchanged: 3-of-3 ACCEPT required for the phase to PASS. The orchestrating
  command body reads the three returned verdicts and aggregates as before.

  This change applies wherever /and-write currently dispatches a single agent to produce
  verdicts for all three audience personas simultaneously. The same topology risk applies
  to /and-facets Phase 5b and /and-substance Phase 5 audience dispatches; the principal
  may choose to extend this change to those command bodies at triage.

  NOTE: the split dispatch is not a fallback for failure — it is the new default. The
  trio-in-one format's apparent benefit (fewer dispatches) is outweighed by two
  demonstrated catastrophic failures. Three ~90-second dispatches is always cheaper than
  one 40-minute dispatch that dies before returning.
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

## PROP-0037

```yaml
id: PROP-0037
created_at: 2026-06-03T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c12-2026-06-03.md
  source_verdict: SHIPPED-WITH-CAVEATS (DEC-0078) — 3rd consecutive SHIPPED-WITH-CAVEATS
    on apparatus-register density / cold-context / design-inherent low-jeopardy (c10
    DEC-0072, c11 DEC-0074, c12 DEC-0078); N=7 consecutive-abstract chapters (c06-c12).
target:
  type: command
  path: .claude/commands/and-substance.md
  section: "Phase 0 — Validate + mode select (chapter b<NN>c<MM> invocation only)"
change_type: modify
rationale: |
  The per-chapter pipeline correctly applied the coupling rule at c10, c11, and c12,
  shipping each chapter as SHIPPED-WITH-CAVEATS with /and-cohere flagged HIGH for the
  apparatus-register accumulation concern. The per-chapter gates are working correctly.
  The process failure is structural: no gate prevents the principal from starting the
  next chapter production run without first running /and-cohere. The /and-cohere
  recommendation has been bypassed twice (c10 to c11, c11 to c12) because the process
  only surfaces it as an end-of-run suggestion rather than a blocking precondition.

  At N=3 consecutive SHIPPED-WITH-CAVEATS on the same cross-chapter pattern, the
  recommendation class needs to become a HARD-abort class. The minimum-viable enforcement
  surface is a Phase 0 check in /and-substance chapter: before authoring the next chapter,
  read the showrunner memory's consecutive_shipped_with_caveats counter; if >= 3 and
  no cohere acknowledgment stamp is present, abort with instructions to run /and-cohere
  (or acknowledge the bypass explicitly).

  This proposal is discriminated from the DEC-0075 deferred mechanism (wiring a counter
  inside the not-yet-implemented /and-cohere command body — PROP-0030/0031 dependency).
  PROP-0037 targets the next chapter production command, not the cohere command body;
  it does not require /and-cohere to be implemented. It is the "obligation-surfaces-at-
  the-right-moment" gate. PROP-0030/0031 are the "obligation-execution" machinery.
  They are orthogonal: accept PROP-0037 independently of PROP-0030/0031 triage.

  Evidence chain: DEC-0072 (c10 ship) → DEC-0073 (N=6, PROP-0030/0031 recurrence_count
  3→4, /and-cohere before c13 flagged) → DEC-0074 (c11 ship) → DEC-0075 (2nd consecutive,
  DEC-0075 deferred cap mechanism pending PROP-0030/0031 triage) → DEC-0076 (c12 chunk
  proceed) → DEC-0077 (N=7, PROP-0030/0031 recurrence_count 4→4, urgency HIGH) → DEC-0078
  (c12 ship) → DEC-0079 (this dispatch, PROP-0037 authored).
evidence_refs:
  - "active-project/staff/reviews/coldread-b01c12-2026-06-03.md — cold-read CONTINUE=No:
    apparatus-register density, design-inherent low jeopardy, cold-context proper-noun
    opacity; all three categories pre-authorized by DEC-0076; identical pattern to c10/c11."
  - "staff/admin/decisions.md — DEC-0075: deferred consecutive-cap mechanism pending
    PROP-0030/0031 triage; 2nd consecutive at that decision point."
  - "staff/admin/decisions.md — DEC-0078: 3rd consecutive SHIPPED-WITH-CAVEATS; /and-cohere
    before c13 urgency HIGH; this dispatch is the 3rd-consecutive trigger."
  - "staff/admin/process-proposals.md — PROP-0030 (status: open, recurrence_count: 4) +
    PROP-0031 (status: open, recurrence_count: 4): the cohere execution machinery.
    PROP-0037 is complementary, not overlapping."
  - ".claude/commands/and-substance.md — Phase 0 chapter invocation: existing HARD-abort
    pattern (aggregate-state unacknowledged substantive entries) is the structural analog;
    same enforcement shape."
  - "active-project/staff/reviews/coldread-b01-c16-2026-06-04.md + DEC-0093 (2026-06-04) —
    second independent N=3 run: c14/c15/c16 all SHIPPED-WITH-CAVEATS on quiet-falling-chapter
    pattern post-cohere-clearance. Consecutive count = 3 (matching c10/c11/c12 first run).
    DEC-0093 confirms N=3 threshold correctly calibrated; no argument for N=2 or N=4 change."
  - "active-project/staff/reviews/coldread-b01-c17-2026-06-05.md + DEC-0095 (2026-06-05) —
    fourth consecutive in the c14-c17 run (N=4 post-cohere-clearance); fifth data point overall
    across both independent runs (c10/c11/c12 + c14/c15/c16/c17). Cold-reader complaints: event-
    poverty / interior-accounting-density / withheld-prior-chapter-motive / jargon-opacity — all
    pre-authorized at DEC-0094. Central event recovered; moral turn maps to goal. Mechanism
    functioning correctly; no argument for changing N=3 threshold."
  - "active-project/staff/reviews/coldread-b01-c18-2026-06-05.md + DEC-0098 (2026-06-05) —
    fifth consecutive in the c14-c18 run (N=5 post-cohere-clearance; 6th data point overall
    across both independent runs: c10/c11/c12 + c14/c15/c16/c17/c18). Cold-reader complaints:
    event-poverty / no-dialogue / no-on-page-resistance / anti-climax-by-design — all
    pre-authorized at DEC-0096. Central event recovered; climax shape affirmed by dramatist.
    NEW signal vs. prior recurrences: c18 is the CLIMAX chapter; the 5th consecutive auto-ship
    arriving at the climax intensifies the question of whether the /and-cohere b01 c13-c18 step
    is correctly positioned as optional-before-book-close vs. a precondition. DEC-0098 (process-
    critic) ruled: /and-cohere is correctly positioned — it is the accumulation handler, not a
    per-chapter gate; the per-chapter coupling is functioning correctly; the depth-pass obligations
    (c14+c18 mandatory, c15/c16/c17 Case 1 no mandatory pass) are the per-chapter layer. The
    book-close enforcement surface belongs to /and-review verdict (the orchestrator-critic pass),
    not a new HARD-abort. No threshold change warranted; N=3 remains correctly calibrated."
  - "active-project/staff/reviews/coldread-b01c19-2026-06-05.md + DEC-0101 (2026-06-05) —
    sixth consecutive in the c14-c19 run (N=6 post-cohere-clearance; 7th data point overall
    across both independent runs: c10/c11/c12 + c14/c15/c16/c17/c18/c19). Cold-reader
    complaints: interior-sameness (one filing action narrated five times) + abstraction-density
    (relentless abstraction) — both pre-authorized at DEC-0099 as design-inherent thesis
    (continuation-unchanged = the horror) + interior-collapse penultimate design. s04 Daven-
    severance LANDED (shown not told) — the one non-auto-dispositioned category did NOT fire.
    Phase 8.5 coherence confirmed central-event-muffle NOT-MATERIALIZED (both spine events
    register as events). Chapter is genuinely well-executed within the Class-B interior-collapse
    design. c19 is the PENULTIMATE chapter. DEC-0101 ruled: 6th consecutive Class-B is the
    expected shape of the c14-c20 falling-collapse stretch; c20 is the catastrophe-climax that
    breaks the interior-sameness; no new signal class beyond DEC-0098 (climax chapter); no
    argument for threshold change or new proposal. PROP-0037 is the correct mechanical gate;
    triage urgency remains HIGH before /and-review verdict b01."
  - "active-project/staff/reviews/coldread-b01c20-2026-06-06.md + DEC-0104 (2026-06-06) —
    seventh consecutive in the c14-c20 run (N=7 post-cohere-clearance; 8th data point overall
    across both independent runs: c10/c11/c12 + c14/c15/c16/c17/c18/c19/c20). Cold-reader
    complaints: abstraction-density / does-not-land-emotionally / airless / tired-turning-page
    — all pre-authorized at DEC-0102 as design-inherent (Class-B cohort extension; series-
    terminal chapter). Central event RECOVERED (Wren's feed-blank). Completeness PASS.
    Readability AIRLESS-leaning but pre-authorized. Prose-rationale-mute=1 (below soft-block).
    2 non-spine NEEDS-BEAT signals (non-blocking). c20 is the SERIES-TERMINAL chapter — the
    c14-c20 depth-pass cohort is NOW COMPLETE and DUE at book-close per PROP-0037 intent.
    DEC-0104 ruled: 7th consecutive Class-B closes the cohort; no new signal class; PROP-0037
    is the outstanding gate that enforces book-close depth-pass obligation. Triage urgency:
    CRITICAL — book-close (/and-review verdict b01) is the next natural step."
  - "active-project/staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md + DEC-0106
    (2026-06-06) — /and-review verdict b01 PASS-WITH-NOTES (series-terminal). Book-close
    confirmation: orchestrator-critic B2 finding explicitly names PROP-0037 as the correct
    gate ('Process signal: the 7-consecutive Class-B chain is the empirical case PROP-0037
    wants hard-gated'). The c14-c20 cohort's per-chapter DEC-acknowledgments (DEC-0085 through
    DEC-0104) are exactly the manual bypass PROP-0037's proposed_diff licenses (path b:
    one-chapter-at-a-time acknowledgment, counter does not reset). b01 is now closed.
    Triage urgency shifts from CRITICAL (pre-verdict) to GENERAL-PIPELINE-RULE (applies
    to b02+ and to any future project with a falling-arc back third). No new proposal
    class: the book's behavior is confirmatory, not novel. DEC-0106 ruled: OK-MERGED."
recurrence_count: 8
proposed_diff: |
  In .claude/commands/and-substance.md, Phase 0 — Validate + mode select, at the
  chapter b<NN>c<MM> invocation level, add a new numbered step after step 6 (Aggregate-
  state read) or after the parking-lot scan, whichever comes last:

  NEW STEP — Consecutive SHIPPED-WITH-CAVEATS gate:

    a. Read showrunner memory field:
       books[<book>].consecutive_shipped_with_caveats (integer; default 0 if absent).
       Also check books[<book>].cohere_acknowledgment (see step d below).

    b. If consecutive_shipped_with_caveats < 3 OR cohere_acknowledgment is present
       and its timestamp post-dates the last SHIPPED-WITH-CAVEATS entry: proceed.

    c. If consecutive_shipped_with_caveats >= 3 AND no valid cohere_acknowledgment:
       HARD-ABORT with message:

       /and-substance chapter <slug> Phase 0 abort: consecutive SHIPPED-WITH-CAVEATS
       = <N> (>= 3 threshold). Cross-chapter apparatus-register accumulation requires
       resolution before the next chapter production run. Resolve by one of:
         (a) Run /and-cohere <book> [range covering the SHIPPED-WITH-CAVEATS chapters]
             and allow it to complete or reach its convergence cap. On completion,
             /and-cohere stamps cohere_acknowledgment in showrunner memory; this
             gate clears automatically.
         (b) If /and-cohere is not yet implemented or the run is not feasible before
             this chapter, stamp a manual acknowledgment in showrunner memory:
             books[<book>].cohere_acknowledgment:
               acknowledged_at: <ISO timestamp>
               acknowledged_by: <principal>
               reason: <one line explaining why /and-cohere is deferred>
             This allows the chapter to proceed; it does NOT clear the counter.
             The gate will re-fire at the NEXT chapter unless /and-cohere runs.

    d. cohere_acknowledgment validity: a stamp qualifies as valid for ONE chapter
       production run only. After the chapter ships, the gate re-evaluates
       consecutive_shipped_with_caveats against the current count (which may or
       may not have increased). A prior acknowledgment does not carry forward.

  COUNTER MAINTENANCE: The showrunner (or the command that emits SHIPPED-WITH-CAVEATS,
  i.e. /and-stitch Phase 9) is responsible for incrementing
  books[<book>].consecutive_shipped_with_caveats on each SHIPPED-WITH-CAVEATS verdict
  and resetting it to 0 on a clean PASS verdict. Proposed: add a single line to
  /and-stitch Phase 9's verdict-persist block for each case. (S-cost addition to
  /and-stitch as a companion change — can be a note here or a separate micro-proposal;
  principal's choice.)

  SCHEMA: Add books[<book>].consecutive_shipped_with_caveats (integer, default 0) and
  books[<book>].cohere_acknowledgment (object: acknowledged_at, acknowledged_by, reason;
  nullable) to schemas/showrunner-memory.schema.md. (S-cost companion change.)

  INTERACTION WITH PROP-0030/0031:
    - If PROP-0031 is accepted and /and-cohere is implemented: path (a) in step c is
      the canonical resolution; /and-cohere writes the acknowledgment stamp.
    - If PROP-0030/0031 are not yet implemented: path (b) is the fallback; the gate
      still enforces the obligation and requires an explicit principal decision to
      proceed.
    - On PROP-0030/0031 implementation, the acknowledgment-stamp write can be added
      to /and-cohere's Phase 7 (persist) as a natural extension of that command body.
      PROP-0037 does not need to wait for that.

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

## PROP-0038

```yaml
id: PROP-0038
created_at: 2026-06-03T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c13-bone-gate.md
  source_verdict: |
    /and-write b01c13 Phase 6 bone-gate FAIL(1-HARD) → remediated to PASS.
    Phase 2 auditor flagged 3 s04 speech bones FAULT-BONE-DELTA-MALFORMED because
    they are held (axis_moves: []) in an all-held foreclosure scene; bones.schema.md
    §Dialogue-anchor bones requires canonical speech bones to move >=1 communication-
    class axis. Orchestrator ruled held-discipline speech (speech that deliberately
    holds a communication-class axis with foreclosure/discipline rationale) is licit.
    This is the second adjudication ruling on speech-bone schema interpretation
    (first: pl-2026-05-30-003, custom-signature axis taxonomy, b01c06).
  gate_path: .claude/commands/and-write.md#phase-6
target:
  type: schema
  path: schemas/bones.schema.md
  section: "Dialogue-anchor bones (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25)"
change_type: modify
rationale: |
  bones.schema.md §Dialogue-anchor bones, rule 1 (canonical speech form) states:
  "Required substance_delta: >=1 communication-class axis (community / knowledge /
  reputation / trust)." This is read by the Phase 2 auditor as requiring axis_moves[]
  to be non-empty — i.e. the speech must MOVE a communication-class axis, not merely
  hold one.

  b01c13 s04 is an all-held foreclosure scene: every bone holds flat; no axis moves.
  The three speech bones (s04n03 Halvard / s04n04 Taylor / s04n06 Halvard) are held-
  discipline bones — the speech IS the holding of the relational/communication-class
  axis (social_tether-antag, relational_anchor_status) flat, with foreclosure rationale.
  This is structurally valid: a character speaking while disciplining a communication-
  class axis to hold is a meaningful bone shape. The schema's silence on this case
  caused FAULT-BONE-DELTA-MALFORMED false positives that required an orchestrator
  adjudication ruling to resolve.

  This is the SECOND time the speech-bone rule required an interpretation ruling:
  - First (pl-2026-05-30-003, b01c06): the universal questionnaire axis slugs
    (community / knowledge / reputation / trust) do not match this project's custom
    signature; ruling: relational_anchor_status + social_tether-* are the project's
    communication/relational-class axes. Fix: generalize the axis-class language.
  - Second (b01c13): a speech bone that holds a communication-class axis in an all-
    held scene fires FAULT-BONE-DELTA-MALFORMED because axis_moves: []. Ruling:
    held-discipline speech is licit when axes_held[] declares a communication-class
    axis with a foreclosure/discipline rationale.

  The pl-2026-05-30-003 generalization (custom-signature axis class language) and the
  held-discipline license are SEPARATE schema additions — pl-2026-05-30-003 fixes the
  axis-slug mismatch; this proposal licenses the held-discipline form. Both are needed.
  pl-2026-05-30-003 is an open parking-lot item awaiting a pipeline tri-walk or schema-
  edit pass; this proposal can be applied in the same pass.

  The fix is precision-writable. The held-discipline license has a narrow predicate:
  (a) axes_in_motion: [] for the scene (all-held scene), AND (b) axes_held[] on the
  speech bone declares a communication-class axis, AND (c) the held rationale names the
  discipline (foreclosure / withholding / held-flat-intentional). This does not relax
  the general movement requirement — speech bones in non-all-held scenes must still
  move >=1 communication-class axis.

  Recurrence_count: 2 (pl-2026-05-30-003 adjudication + b01c13 adjudication). Two
  orchestrator adjudication rulings on the same schema section within 7 chapters is
  sufficient to treat the gap as deterministic rather than waiting for a third instance.
  The predicate is narrow, enumerable, and non-ambiguous; the false-positive blast
  (FAULT-BONE-DELTA-MALFORMED on licit held speech in all-held foreclosure scenes) will
  recur on every future all-held dialogue scene without this amendment.
evidence_refs:
  - "active-project/staff/auditor/write-b01c13-bone-gate.md — pass-bone-s04n03/n04/n06:
    all three speech bones pass on adjudication; auditor note cites held-discipline speech
    licit when axes_held[] declares a communication-class axis with foreclosure/discipline
    rationale; explicitly names this as the second speech-bone interpretation ruling."
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-05-30-003: SCHEMA AMBIGUITY
    (ruled, needs formalization): custom-signature axis-taxonomy ruling at b01c06; proposes
    (a) bones.schema.md generalization of axis-class language. The held-discipline license
    is a SEPARATE addition to the same schema section — this proposal can be co-applied."
  - "schemas/bones.schema.md — Dialogue-anchor bones rule 1: 'Required substance_delta:
    >=1 communication-class axis (community / knowledge / reputation / trust)' — axis slugs
    are universal-questionnaire only; no held-discipline license; bottom paragraph: 'speech
    bones must move at least one communication-class axis' — implies non-empty axis_moves[]."
  - ".claude/commands/and-write.md — Phase 1 step 5 speech-bone form; Phase 2
    FAULT-BONE-DELTA-MALFORMED definition (magnitude 0 or null is malformed, implying
    axis_moves: [] on a speech bone is malformed when the movement requirement is enforced)."
recurrence_count: 2
proposed_diff: |
  In schemas/bones.schema.md, §Dialogue-anchor bones, rule 1 (canonical speech form),
  amend as follows:

  CURRENT TEXT (rule 1):
    1. **Canonical speech form** — `<speaker-slug> speaks to <listener-slug>`.
       Required substance_delta: ≥1 communication-class axis (community / knowledge /
       reputation / trust).

  AMENDED TEXT (rule 1):
    1. **Canonical speech form** — `<speaker-slug> speaks to <listener-slug>`.
       Required substance_delta: one of:
         (a) **Movement form.** axis_moves[] declares ≥1 communication/relational-class
             axis (universal questionnaire: community / knowledge / reputation / trust;
             custom signature: the axis/axes the signature designates relational or
             communicative — e.g. relational_anchor_status, social_tether-*). The axis
             is moved (non-zero magnitude).
         (b) **Held-discipline form.** axes_held[] declares ≥1 communication/relational-
             class axis AND axis_moves: [] AND the scene's axes_in_motion: [] (all-held
             scene). The held rationale MUST name the discipline: foreclosure /
             withholding / held-flat-intentional / any equivalent. This licenses speech
             that enacts the deliberate non-movement of a relational/communicative axis
             — e.g. a character speaking while foreclosing a patron-channel, refusing a
             relational proposition, or withholding the response the other character
             invited.

  Also in §Dialogue-anchor bones, at the bottom paragraph ("Speech bones must move at
  least one communication-class axis..."), amend:

  CURRENT:
    Speech bones must move at least one communication-class axis (community / knowledge /
    reputation / trust) per the substance bone-gate; speech bones whose substance_delta
    lists only physical-action axes are malformed.

  AMENDED:
    Speech bones must satisfy rule 1(a) or rule 1(b) above. Speech bones in axis-move
    scenes (axes_in_motion non-empty) must use form (a): move ≥1 communication/relational-
    class axis. Speech bones in all-held scenes (axes_in_motion: []) may use form (b):
    hold ≥1 communication/relational-class axis with discipline rationale. Speech bones
    whose substance_delta declares only physical-action axes without any communication/
    relational-class entry in either axis_moves[] OR axes_held[] are malformed.

  NOTE: This amendment incorporates pl-2026-05-30-003 proposed generalization (a) —
  axis-class language is generalized to cover custom-signature axis slugs. If
  pl-2026-05-30-003 is resolved at the same schema-edit pass, both changes should be
  applied together. The parking-lot item can be stamped resolved at that point.

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

## PROP-0039

```yaml
id: PROP-0039
created_at: 2026-06-04T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/auditor/write-b01c14-bone-gate.md
  source_verdict: |
    /and-write b01c14 Phase 6 bone-gate: 3 HARD STAKES-AXIS-NOT-DOMINANT on S03/S04
    from axis-ties at 1.0 in a multi-arc convergence climax. Remediated in-cycle:
    S02/S03 reconciled to strict single-mover dominance via mover-to-held conversions;
    S04 convergence-climax (4 arcs x +1.0) accepted via lenient co-dominant-tie reading
    (no non-stakes axis delivers strictly more than the stakes axis; ties accepted as
    co-dominant). Queued for admin ratification and process-critic judgment.
  gate_path: .claude/commands/and-write.md#phase-6
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 6 — Per-scene verification, stakes-axis-dominant check (URI-WRITE-STAKES-AWARE)"
change_type: modify
rationale: |
  The Phase 6 gate spec (stakes-axis-dominant check) reads: "that axis's delivered aggregate
  magnitude MUST be the largest delivered delta in the scene. If a non-stakes axis delivers a
  larger aggregate than the declared stakes axis, the scene is mis-shaped — STAKES-AXIS-NOT-
  DOMINANT (HARD)."

  This formulation has no carve-out for simultaneous N-arc completion scenes. In a convergence-
  climax scene where 3+ cost-arcs complete simultaneously, every completing axis delivers at the
  1.0 bone floor — the minimum deliverable magnitude. In that configuration, strict single-axis
  dominance is structurally impossible: the bone floor prevents any axis from delivering LESS
  than 1.0 in the scene where it completes, so all completing axes tie at 1.0.

  b01c14 S04 is the first live convergence-climax scene in the project: cl-antag-d10 +
  cl-d07a + cl04 + relational arc all close at S04, each with a 1.0-floor completing bone.
  The auditor correctly reasoned that "no non-stakes axis delivers strictly more than the
  stakes axis" and accepted the tie. But that reasoning is not supported by the spec text,
  which reads "MUST be the largest" — a future auditor following the spec literally would
  HARD on any tie, including the co-dominant convergence-climax case.

  The gate's intent is to prevent stakes-axis under-delivery: a chapter whose declared
  capability stakes axis delivers +0.5 while a knowledge axis delivers +3.0 is mis-shaped.
  Co-dominant ties at the 1.0 floor are not mis-shaped — the stakes axis delivered its
  contractual increment, and other arcs completed alongside it. The gate's purpose is fully
  satisfied when the stakes axis is not outscored; it is over-applied when it HARDs on ties.

  This is the first occurrence of the convergence-climax co-dominant tie. First-occurrence
  hold is overridden because: (a) the failure is deterministic — every future convergence
  climax in a multi-arc project will hit this structural condition; (b) the fix is narrow
  and precise; (c) the orchestrator adjudication ruling (lenient tie accepted) confirms the
  correct outcome is clear even without a spec change; (d) leaving the spec inconsistent
  creates a reproducible false-positive HARD on every future convergence-climax scene.
evidence_refs:
  - "active-project/staff/auditor/write-b01c14-bone-gate.md — S04 stakes-dominance section:
    'four movers tied at +1.0. LENIENT PASS: no non-stakes axis delivers strictly more than
    the stakes axis (relational). The convergence-climax completes three cost-arcs + closes
    cl04 simultaneously; strict single-dominance is structurally impossible when N arcs
    complete at the 1.0 floor. Disposition: co-dominant tie accepted; queued for admin
    user-proxy ratification.' Audience 3/3 SUBSTANCE-FELT on S04."
  - ".claude/commands/and-write.md — Phase 6 per-scene verification, stakes-axis-dominant
    check: 'that axis's delivered aggregate magnitude MUST be the largest delivered delta
    in the scene. If a non-stakes axis delivers a larger aggregate than the declared stakes
    axis, the scene is mis-shaped — STAKES-AXIS-NOT-DOMINANT (HARD).' No co-dominant-tie
    exception exists in the current spec."
  - "staff/admin/decisions.md — DEC-0084: user-proxy ratification of lenient-tie; accepted
    on goal:1 (gate purpose satisfied) + goal:2 (3/3 SUBSTANCE-FELT; revise would burn caps
    on a chapter that delivered by every informed-critic measure) + methodology:3a grounds."
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-write.md, Phase 6 — Per-scene verification, stakes-axis-dominant
  check (URI-WRITE-STAKES-AWARE — HARD), amend the check criterion as follows:

  CURRENT TEXT:
    When scene_conflict.stakes_axis resolves to an axes_in_motion[] axis, that axis's
    delivered aggregate magnitude MUST be the largest delivered delta in the scene. If a
    non-stakes axis delivers a larger aggregate than the declared stakes axis, the scene
    is mis-shaped — STAKES-AXIS-NOT-DOMINANT (HARD). (A scene of *watching* delivering
    a knowledge overrun while its declared capability stakes axis under-delivers is the
    canonical failure this catches.) When stakes_axis resolves to an axes_held[] axis,
    this check is N/A (held axes deliver zero by design).

  AMENDED TEXT:
    When scene_conflict.stakes_axis resolves to an axes_in_motion[] axis, that axis's
    delivered aggregate magnitude MUST NOT be outscored by any other axis. Two cases:

      (a) Strict dominance (normal scenes): the stakes axis delivers strictly the largest
          aggregate delta in the scene. Any non-stakes axis delivering a larger aggregate
          is STAKES-AXIS-NOT-DOMINANT (HARD). (A scene of *watching* delivering a
          knowledge overrun while its declared capability stakes axis under-delivers is
          the canonical failure this catches.)

      (b) Co-dominant tie (convergence-climax exception): when >=2 axes complete
          simultaneously at the bone delta floor (chunk_targets.bone.delta_per_axis.floor)
          in a single scene, co-dominant ties are ACCEPTED — the gate fires HARD only when
          a non-stakes axis delivers STRICTLY GREATER magnitude than the stakes axis.

          Conditions for the co-dominant-tie exception:
            1. The scene is a convergence scene: >=2 cost_ledger entries whose anchor
               resolves at-or-under this scene each have a completing bone in this scene.
            2. The tied axes are all at the bone delta floor value (not above it).
            3. The stakes axis is INCLUDED in the tie (i.e., it is not outscored; it
               ties for highest or shares the highest delivered magnitude).

          If all three conditions are met, report as LENIENT-PASS-CO-DOMINANT (not HARD;
          not a blocking finding). Log the tie explicitly in the bone-gate report with
          the convergence rationale. Admin process-critic dispatch (Phase 6.5) receives
          the LENIENT-PASS log for user-proxy ratification.

          If any condition is NOT met (non-stakes axis ties above the bone floor, or
          the stakes axis is genuinely outscored, or there is no convergence trigger),
          apply the standard strict-dominance check.

      When stakes_axis resolves to an axes_held[] axis, this check is N/A (held axes
      deliver zero by design).

  HARD / SIGNAL classification table: update the STAKES-AXIS-NOT-DOMINANT row to clarify
  it applies only under strict-dominance case (a); LENIENT-PASS-CO-DOMINANT is not a
  SIGNAL — it is a passing log entry that routes to Phase 6.5 admin ratification.

  NOTE: This change does not relax the gate for any scenario where a non-stakes axis
  genuinely outscores the stakes axis. The co-dominant exception is structurally narrow:
  it requires simultaneous cost-arc completion at the bone floor — a condition that arises
  only in designed convergence-climax scenes. A chapter where the stakes axis under-delivers
  (e.g., delivers 0.5 while others deliver 1.0) is still STAKES-AXIS-NOT-DOMINANT (HARD)
  because 0.5 < 1.0 is strict outscoring, not a tie.

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

## PROP-0040

```yaml
id: PROP-0040
created_at: 2026-06-04T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/reviews/coldread-b01c14-2026-06-04.md
  source_verdict: |
    SHIPPED-WITH-CAVEATS (Phase 9 Class-B cold-read FAIL CONTINUE=no; central event recovered;
    cause = design-inherent accounting-abstraction register + cold-context name-opacity;
    DEC-0085 coupling-rule dispatch). Fourth application of the coupling rule across
    c10/c11/c12/c14 (DEC-0072/0074/0078/0085). All four deterministic on identical pattern.
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 9 — Step 2 Diff against intent (harness) / Step 4 Verdict + memory"
change_type: modify
rationale: |
  PROBLEM: The Phase 9 coupling-rule (Class-B FAIL + matching-complaint → SHIPPED-WITH-CAVEATS)
  has now been applied four times across c10/c11/c12/c14. Each application was deterministic —
  in DEC-0074 and DEC-0078 and DEC-0085 the admin user-proxy answered identically, with zero
  ambiguity, citing the prior DEC entries as the basis. The coupling rule is stable. Two
  sub-cases have emerged across the four applications:

  Case 1 — Zero tractable complaints (c11/c12 shape): CONTINUE=no causes are 100%
  design-inherent (design-inherent abstract register by contract) and/or cold-context noise
  (serial mid-point proper-noun load). No complaint is addressable by any revise without
  violating the endorsed substance contract. Admin round-trip adds no information. DEC-0074
  and DEC-0078 are both pure Case 1 — both answered "SHIPPED-WITH-CAVEATS, no depth pass" in
  one sentence citing prior decisions.

  Case 2 — Tractable complaints remain alongside design-inherent causes (c14 shape): the
  CONTINUE=no causes include at least one addressable texture gap (courier-as-person
  concreteness, Sera-stake staging) that is NOT design-inherent and CAN be addressed via
  /and-write revise --from-signals without violating the substance contract. Admin round-trip
  adds value here: it identifies the tractable items, names the depth-pass targets, and
  stamps `depth_pass_mandatory: yes` with a specific target brief. DEC-0085 is a pure Case 2
  — the tractable items are what distinguished c14's disposition from c11/c12's.

  The current Phase 9 spec does not encode this distinction. The Phase 9 Step 2 harness fires
  a FAIL and routes to admin user-proxy in both cases. In Case 1, the admin round-trip is pure
  overhead — a deterministic call with the answer already encoded in DEC-0072/0074/0078. In
  Case 2, it is load-bearing (the tractable-item identification is the admin value-add).

  PROPOSED CHANGE: Add a Case 1 auto-ship path to Phase 9 Step 2 (the diff harness). When
  the Class-B routing fires AND the chunk_cold_read.cold_read_risk_carry categories account
  for ALL CONTINUE=no complaint categories (zero tractable complaints remain), the harness
  resolves directly to SHIPPED-WITH-CAVEATS WITHOUT an admin user-proxy dispatch. The
  per-chapter caveat string is assembled mechanically from the carried risk items. When any
  CONTINUE=no complaint is NOT covered by the carried risk categories (Case 2), the existing
  admin user-proxy dispatch fires as before.

  This does not change the gate's detection (CONTINUE=no still fires Class-B), routing
  (Class-B still goes to SHIPPED-WITH-CAVEATS on matching-complaint), or the caveat record
  (the caveat string is still written to showrunner memory). It eliminates one admin
  dispatch per Case 1 chapter — a small efficiency gain per chapter that adds up at book scale
  (c10+c11+c12 would each have saved one admin round-trip under this rule; across a 14-chapter
  book that is real budget). The residual admin dispatch (Phase 9.5 process-critic) still fires.

  DISCRIMINATION — what counts as Case 1 (zero tractable) vs. Case 2 (tractable remains):
  The Phase 9 harness performs this classification by matching each CONTINUE=no complaint
  from the cold-read against the chapter's `chunk_cold_read.cold_read_risk_carry` list:
    - If every complaint maps to a carried risk item (exact or paraphrase match), Case 1.
    - If ANY complaint has no carried risk match, Case 2.
  Hard fence: the harness applies conservative matching — "no match" wins over "marginal
  match." When in doubt, fire the admin dispatch (Case 2 path). The auto-ship path is not a
  cost-cutting bypass; it is the mechanical expression of a ruling the principal has made
  four times on identical evidence. Case 2 complaints are not about cost; they are about
  specificity of the depth-pass brief.

  INTERACTION WITH PROP-0018 (Class A/B discriminator): PROP-0018 added the Class A/B branch
  at Phase 9 Step 2 and specified "admin returns disposition; pipeline applies it. Class B
  admin default: (P) given substance contract was approved." This proposal amends the Case 1
  half of that admin default to mechanical harness execution (admin default = SHIP, no dispatch
  needed). The Case 2 half (admin dispatch for tractable items) is unchanged — PROP-0018's
  pipeline-applies-it contract continues to govern Case 2. PROP-0018 does not need to be
  reopened; this is a refinement of its routing.

  DEPTH-PASS STATUS CLARIFICATION (candidate b in trigger): the trigger's concern about
  "4 chapters with depth-pass debt" is inaccurate. Actual pending depth passes as of
  this dispatch: c10 (PASS-WITH-DEPTH-PASS-REQUIRED, bone-level staging targets) and
  c14 (mandatory per DEC-0085, texture-level targets). c11 and c12 are SHIPPED-WITH-CAVEATS
  without depth-pass obligations (c11: readability READABLE, no mandatory depth pass;
  c12: DEC-0078 explicitly resolved apparatus-density to /and-cohere, not a per-chapter
  depth pass). The SHIPPED-WITH-CAVEATS / PASS-WITH-DEPTH-PASS-REQUIRED distinction is
  working correctly. No process change warranted on depth-pass accumulation.

  UPSTREAM GROUNDING DEFAULTS (candidate c in trigger): c14's tractable gaps
  (courier-as-person, Sera-stake) are first-occurrence at this exact class (tractable texture
  gap in an interior-accounting chapter shipping SHIPPED-WITH-CAVEATS). Not catastrophic.
  Standard first-occurrence hold applies per process-critic Rule step 4.
evidence_refs:
  - "active-project/staff/reviews/coldread-b01c14-2026-06-04.md — Class-B, CONTINUE=no,
    causes = aggregate abstraction-density + names-unfamiliar; Phase 8.5 PASS; tractable
    items (courier-as-person, Sera-stake) identified; DEC-0085 coupling-rule dispatch."
  - "staff/admin/decisions.md — DEC-0074 (c11 Phase 9, Case 1: all complaints covered by
    carried risk; one-sentence answer; no depth pass); DEC-0078 (c12 Phase 9, Case 1:
    identical); DEC-0085 (c14 Phase 9, Case 2: tractable items identified; depth-pass
    mandatory before book-close). DEC-0072 (c10 chunk-level precedent)."
  - ".claude/commands/and-stitch.md — Phase 9 Step 2 (current harness: FAIL routes to admin
    user-proxy unconditionally; no Case 1/2 discrimination in the spec). Phase 9 Step 4
    (SHIPPED-WITH-CAVEATS not listed as a first-class verdict alongside PASS / PASS-WITH-
    DEPTH-PASS-REQUIRED / FAIL)."
  - "staff/admin/process-proposals.md — PROP-0018 (Class A/B discriminator; status: check
    triage stamp before implementing; this amendment is a refinement of PROP-0018's Class B
    admin-default, not a rewrite of it)."
recurrence_count: 4
proposed_diff: |
  In .claude/commands/and-stitch.md, Phase 9 Step 2 — Diff against intent (harness),
  immediately after the Class-B classification check (summary maps to goal), add:

  **Complaint-coverage check (Case 1 vs. Case 2):**

    After Class-B is established, classify each CONTINUE=no complaint from the cold
    reader's answers against `chapters[<slug>].chunk_cold_read.cold_read_risk_carry` items:
      - COVERED = a carried risk item accounts for this complaint class. Examples of
        covered mappings: "relentlessly abstract ledger-metaphor" → carried risk
        "design-inherent abstract register"; "Otto/Sera faction unexplained" → carried risk
        "cold-context proper-noun load (serial mid-point)."
      - UNCOVERED = no carried risk match, OR the complaint names a tractable texture gap
        (e.g., "courier never felt as a person", "stakes not staged on-page", "no concrete
        scene") even if partially overlapping with a carried item.
      Conservative fence: classify UNCOVERED when in doubt.

    **Case 1 — all complaints COVERED:**
      Skip the admin user-proxy dispatch. Resolve directly:
        cold_read.verdict: SHIPPED-WITH-CAVEATS
        cold_read.case: 1
        cold_read.caveat: <assembled from cold_read_risk_carry items verbatim>
        depth_pass_pending: false
      Continue to Step 3, Step 3.5, Step 4 (write memory), Phase 9.5 (process-critic).

    **Case 2 — ≥1 complaint UNCOVERED:**
      Dispatch admin user-proxy as currently specified (PROP-0018 path, unchanged).
        cold_read.case: 2
      Admin identifies tractable items, authors depth-pass brief if warranted, returns
      disposition. Pipeline applies it.

    If `chunk_cold_read.cold_read_risk_carry` is absent (chapter had PASS-CHUNK, not
    PASS-CHUNK-VOICE-RISK), treat as Case 2 unconditionally (no carried risk → all
    complaints are uncovered).

  In .claude/commands/and-stitch.md, Phase 9 Step 4 Verdict + memory block,
  add SHIPPED-WITH-CAVEATS as a first-class verdict bullet:

    "**SHIPPED-WITH-CAVEATS** — Class-B FAIL; all CONTINUE=no complaints covered by
    carried risk (Case 1) OR admin-dispositioned (Case 2). Terminal. No retry.
    Depth-pass obligation: none for Case 1; per admin brief for Case 2.
    Write: `cold_read = {verdict: SHIPPED-WITH-CAVEATS, case: 1|2, caveat: <string>, ...}`.
    Phase 9.5 (process-critic) fires as normal."

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

## PROP-0041

```yaml
id: PROP-0041
created_at: 2026-06-04T00:00:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: active-project/staff/audience/ (b01c16 Phase 5 HARD state-updates moral_legibility Drift-old)
  source_verdict: |
    Phase 5 HARD: state-updates @19 moral_legibility recorded 4->4.5 (series-baseline
    start_rank) instead of 6.0->6.5 (chapter-entry value from aggregate-state); fixed.
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 1 — R1 author 5: state-updates actor (per-character impersonators)"
change_type: modify
rationale: |
  The per-actor state-updates impersonator (Phase 1 item 5) produced a Drift-old HARD
  violation: moral_legibility recorded as "4 -> 4.5" (series-baseline start_rank = 4)
  instead of "6.0 -> 6.5" (chapter-entry value = 6.0 from the character's aggregate-state
  after 15 prior chapters of axis movement). The state-updates rubric requires <old> to
  match the most-recent prior cited canonical value (Drift-old REJECT: "<old> doesn't
  match the prior cited canonical value").

  The Phase 1 state-updates-actor dispatch payload currently names: character stack
  (card + behavior cards + LTM + STM + state) + base proto-lines + per-chapter
  substance_delta from showrunner memory + rubric-state-updates.md § actor-state.
  The per-chapter substance_delta gives the delta targets for this chapter (how much
  each axis moves) but NOT the current chapter-entry value (where the axis stands
  entering the chapter). For a project in its first chapter these are the same
  (chapter-entry = series-baseline start_rank). After N chapters of cumulative movement
  they can differ materially -- here by 2.0 units (4 vs 6.0).

  The character stack includes the character's state file; however the state file's
  primary content is the character's narrative/behavioral state, and the most visible
  per-axis rank value in a dispatch context is the axis definition's start_rank
  (series-baseline). Without an explicit call to read the current per-axis value from
  the state file (or aggregate-state), the impersonator will default to the most
  accessible rank value -- the series-baseline -- producing systematic Drift-old at
  any axis that has moved significantly from baseline. This is a deterministic payload
  spec gap, not an authoring error.

  The fix is a single instruction added to the Phase 1 state-updates-actor dispatch
  brief: explicitly require the impersonator to read the character's current per-axis
  values from the actor state file before authoring any state-update entry, and use
  those as the <old> anchor rather than the axis definition's start_rank. S-cost.

  Proposing at N=1 because the gap is deterministic (same error class will recur on
  any chapter where a substance axis has moved significantly from series-baseline) and
  the fix is precisely targeted (analogous to PROP-0027: first live test of a mechanism
  with a deterministic omission in the dispatch payload).
evidence_refs:
  - "active-project/staff/audience/ b01c16 Phase 5 audit -- HARD: state-updates @19
    moral_legibility 4->4.5 (series-baseline) vs. correct 6.0->6.5 (chapter-entry);
    fixed before Phase 5b."
  - ".claude/commands/and-facets.md Phase 1 item 5 -- state-updates-actor dispatch
    payload: 'Character stack + base proto-lines + per-chapter substance_delta from
    showrunner memory + rubric-state-updates.md § actor-state.' Current per-axis
    entry values from actor state file are NOT named as an explicit required input."
  - "design/shoot-v2/rubric-state-updates.md § V2 rubric axes -- Drift-old REJECT:
    '<old> doesn't match the prior cited canonical value.' ACCEPT: '<old> matches
    the most-recent prior cited value on the same field (or the project-setup baseline
    if first-touch).'"
  - "staff/admin/process-proposals.md -- PROP-0027 (grounding-ledger first-live-test
    dispatch omission; proposed at N=1 on same deterministic-gap rationale)."
  - "staff/admin/decisions.md -- DEC-0092 (this dispatch; Q2 judgment)."
recurrence_count: 1
proposed_diff: |
  In .claude/commands/and-facets.md, Phase 1 item 5 (state-updates actor), in the
  dispatch payload description, add a required pre-authoring read step:

  Current payload (paraphrase):
    "Character stack + base proto-lines + per-chapter substance_delta from showrunner
    memory + rubric-state-updates.md § actor-state."

  Add to the dispatch payload list:
    "character's CURRENT per-axis values -- read the actor state file at
    active-project/actors/<slug>/state.md (or the aggregate-state section of
    active-project/staff/showrunner/memory.md chapters[<slug>]) and extract the
    current rank/value for each tracked substance axis."

  Add to the dispatch brief sent to the impersonator (before the first authoring step):
    "REQUIRED PRE-AUTHORING STEP: Read <character>'s actor state file and record the
    CURRENT value of each tracked substance axis (moral_legibility, social_position,
    community_belonging, [etc. per series signature]). Use these values as the <old>
    anchor for every state-update entry on actor:<slug> fields. Do NOT use the axis
    definition's start_rank (series-baseline). The series-baseline is the value at
    story-start; the chapter-entry value is the current value after N chapters of
    accumulated movement, and they diverge as the series progresses. A state-update
    entry whose <old> uses the series-baseline instead of the chapter-entry value is
    a Drift-old HARD finding per the state-updates rubric."

  Scope: state-updates-actor per-character impersonator dispatches only (Phase 1 item 5).
  State-updates-env (item 4) uses environmental fields sourced from loc-state / studio
  state, not substance-axis tracking; this change does not apply to item 4.

  The character stack already contains the actor state file; this change makes the
  read-and-extract step explicit rather than implicit, eliminating the impersonator's
  fallback to the axis-definition start_rank.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```


# NOTE: ported from claude/chapters-audit-hLABe; renumbered PROP-0041 -> PROP-0042 (main independently used PROP-0041). Source: c01-c15 chapters audit + c13-c15 cohere.
## PROP-0042

```yaml
id: PROP-0042
created_at: 2026-06-04T00:00:00Z
created_by: admin process-critic
trigger:
  reason: cohere-converged-caution
  source_report: active-project/staff/reviews/cohere-b01-c13-c15-20260604T151735Z.md
  source_verdict: CAUTION-COHERE (load_bearing_fails 0, iteration_count 1)
target:
  type: command
  path: .claude/commands/and-substance.md
  section: "Phase 5 — Chunk-quality review (book level)"
change_type: add
rationale: |
  The protect-target (sera-hightower) has had no planned on-page appearance across 10
  consecutive shipped chapters (c06-c15). This structural absence was flagged by TWO
  consecutive /and-cohere runs — c06-c12 (pl-2026-06-03-006) and c13-c15 (confirms
  existing) — both times as "not chapter-fixable" and routed to /and-review verdict b01.
  By /and-review verdict b01 the fix is maximally expensive: the book is fully authored
  and a protect-target on-page appearance requires retrofitting an existing chapter or
  adding a new one.

  The gap has no owning gate upstream of /and-cohere. The /and-substance book Phase 5
  dramatist review checks cross-chapter handoff consistency but has no check for book-
  level structural completeness of story promises — specifically, whether the declared
  protect-target (the person the entire arrangement is owed against) appears on-page
  before the climax that fires the protection guarantee.

  This is a deterministic gap: every future book whose substance signature declares a
  protect-target (or equivalent "person the stakes are owed to") faces the same risk —
  the person can be planned absent for the entire book without any gate firing until
  /and-review verdict catches it retrospectively. The Sera case is the first evidence;
  the structure of the gap is project-independent.

  The minimum-viable fix is a SOFT flag at /and-substance book Phase 5 (dramatist
  review): when the book chapter plan is reviewed, the dramatist checks whether any
  chapter in the plan provides the protect-target on-page. If no chapter does, the
  dramatist flags it — not as a HARD block (because "never on-page" can be a deliberate
  hollow-by-design irony choice) but as a surfacing that forces the authorial decision
  at planning time rather than book-close time.
evidence_refs:
  - "active-project/staff/reviews/cohere-b01-c13-c15-20260604T151735Z.md — Group 3
    structural holes: 'Sera never appears on-page (c06-c15). The entire arrangement is
    owed against protecting her; the guarantee fires correctly as a structural node at
    the c14 stylus-decision, but fires hollow — the protection object is a name in a
    prologue, never a felt person. Requires a book-level authorial decision (hollow-by-
    design irony vs. a prior/epilogue appearance). → /and-review verdict b01.'
    Confirms existing: pl-2026-06-03-006."
  - "active-project/staff/showrunner/parking-lot.md — pl-2026-06-03-006: Sera-never-
    on-page + Otto-off-page structural holes confirmed by BOTH the c06-c12 cohere and
    the c13-c15 cohere; routed to /and-review verdict b01 both times."
  - ".claude/commands/and-substance.md — Phase 5 book-level dramatist check: cross-
    chapter handoff consistency is the only structural completeness check; no protect-
    target / story-promise on-page-presence check exists."
  - "active-project/staff/showrunner/memory.md — series.substance.signature.cost_ledger:
    protect-target declared as the structural anchor of the trades (the person the
    arrangement is owed against keeping alive)."
recurrence_count: 4
recurrence_refs:
  - "active-project/staff/reviews/cohere-b01-all-20260606T215813Z.md — DEC-0109 (2026-06-06)
    whole-book /and-cohere (b01 all, c01-c20) dramatist-promise-payoff finding: Sera Hightower
    payoff-weight drop. Sera introduced c03 as the cost-justification of the Otto arrangement;
    never appears as a person across all 20 chapters; threat never staged; c20 decommission does
    not confirm protection. Reader never feels her weight — the moral engine's human face is a
    ledger entry. Third independent /and-review cohere run to flag the same root: protect-target
    absent-as-felt-person across the full book. Confirms gap is structural and persisted to
    book-close despite three sub-section coheres routing it 'not chapter-fixable → /and-review
    verdict b01.' Full-book scope is the terminal confirmation of the gap PROP-0042 targets at
    planning time."
proposed_diff: |
  In .claude/commands/and-substance.md, Phase 5 — Chunk-quality review, book level,
  in the dramatist reviewer row, add a new check alongside the existing cross-chapter
  handoff check:

  CURRENT dramatist review description (book level, partial):
    "Book level additionally checks cross-chapter handoff: for every adjacent chapter
    pair (N, N+1) under the book, chapters[N].handoff_out is consistent with
    chapters[N+1].handoff_in. Mismatches HARD-fail and force revise on the offending
    chapter chunks."

  ADD after the handoff-consistency paragraph:

    **Book-structural promise completeness (book level only — SOFT flag).** For each
    declared protect-target or cost-bearer in
    series.substance.signature.cost_ledger[] (any entry where the ledger trade names
    a living character as the object of the structural guarantee), check whether at
    least one chapter in the current book's chapter plan provides that entity on-page.
    "On-page" = the chapter's substance_delta or dramatic_shape explicitly places the
    entity in a scene as a participant, not merely referenced in interior accounting.

    If no chapter in the plan provides the entity on-page:
      Flag as PROTECT-TARGET-ABSENT-FROM-BOOK-PLAN (SOFT — does NOT block persist,
      does NOT force a revise cycle). Output in the dramatist report:
        "PROTECT-TARGET-ABSENT: <entity-slug> has no planned on-page appearance
        in this book. The cost-ledger's structural guarantee fires on this entity
        without the reader ever meeting them. Authorial options: (A) plan a chapter
        that places <entity-slug> on-page before the climax, or (B) acknowledge
        hollow-by-design as the intended irony (stamp
        books[<slug>].protect_target_absent_acknowledged in showrunner memory)."

    At Phase 7 (Persist): if the SOFT flag fired, write to showrunner memory:
      books[<slug>].protect_target_absent_flag:
        entity: <entity-slug>
        flagged_at: <ISO>
        acknowledged: false   # principal stamps true via option B
    The flag surfaces in the Phase 7 print block and at /and-review verdict b01.
    It does NOT trigger a revise loop in the Phase 5 accept/revise cycle.

    Principal may acknowledge via one of:
      (A) Revising the chapter plan to include the entity on-page (sets acknowledged
          automatically when the entity appears in a chapter's substance_delta).
      (B) Manually stamping books[<slug>].protect_target_absent_flag.acknowledged:
          true with acknowledged_at + acknowledged_by + reason (e.g. 'hollow-by-
          design irony: the unfelt protection object is the point').

  SCHEMA COMPANION (S-cost, same implementation pass):
    Add to schemas/showrunner-memory.schema.md, books[<slug>] block:
      protect_target_absent_flag: null | {entity, flagged_at, acknowledged, [acknowledged_at,
      acknowledged_by, reason]}
    Field is optional; absent = not flagged or check not yet run.

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

## PROP-0043

```yaml
id: PROP-0043
created_at: 2026-06-07T00:00:00Z
created_by: admin process-critic
trigger:
  reason: principal-initiated-retro
  source_report: active-project/staff/auditor/cohere-b01-all-aggregate-audit.md
  source_verdict: retro (session retrospective on the /and-cohere b01 all cycle, 2026-06-06; no gate verdict)
target:
  type: agent-card
  path: CLAUDE.md
  section: "Rules — dispatch-discipline (new rule, candidate Rule 19)"
change_type: add
rationale: |
  During the /and-cohere b01 all session (2026-06-06), the auditor was dispatched to
  produce and persist `active-project/staff/auditor/cohere-b01-all-aggregate-audit.md`.
  The auditor returned its full classified findings report in its final message but never
  wrote the file. The dispatcher (the main session) consumed the in-message result without
  noticing the artifact was absent. The gap was caught ONLY by a post-session `git log
  -- <path>` + `ls` check; the report was one step from permanent loss. The principal had
  to reconstruct and persist it from the agent's return text.

  This is a structural dispatch-discipline gap, not a one-off execution error: any
  Write-capable agent contracted to emit a file can return its complete result in-message
  and never touch the filesystem, and no existing rule or convention requires the dispatcher
  to check. The check is trivially cheap (single stat/ls call), but it is not currently
  mandated anywhere in the pipeline. The failure class is silent — there is no error, no
  FAIL verdict, no gate that fires. The dispatcher treats in-message content as delivered;
  the filesystem does not.

  There is no existing gate, command phase, or CLAUDE.md rule that covers this class.
  First occurrence, but: (a) the mechanism is structurally generic — applies to every
  Write-capable agent across every command; (b) the consequence is permanent data loss on
  the next context window boundary; (c) the fix is S-cost (one mandated existence check
  per contracted emit path); (d) the check is a single stat/ls — no false positives, no
  blast radius. The first-occurrence hold does not apply when the failure mode is silent
  data loss and the fix is trivially cheap. Proposing at first occurrence.

  change_type: add — no existing rule covers this; the check is a new dispatch-discipline
  requirement, not a modification of an existing one.
evidence_refs:
  - "active-project/staff/auditor/cohere-b01-all-aggregate-audit.md — full audit classified
    and filed (by principal reconstruction) 2026-06-06; the original agent dispatch returned
    findings in-message only; the file did not exist until the principal manually persisted
    from the return text; confirmed by git log -- active-project/staff/auditor/cohere-b01-
    all-aggregate-audit.md showing no auditor-authored commit"
  - "CLAUDE.md §Agent routing table — auditor row: declares that auditor emits to
    active-project/staff/auditor/ but specifies no dispatcher existence-check obligation"
  - "CLAUDE.md §Rules — no existing rule requires dispatchers to verify file persistence
    after a Write-capable agent returns; Rule 4 ('Nothing moves without being recorded')
    is the closest existing principle but applies to story-state, not dispatch artifacts"
recurrence_count: 1
proposed_diff: |
  In CLAUDE.md, §Rules, add a new dispatch-discipline rule (next available number after
  Rule 18; candidate Rule 19):

  **Rule 19. Subagent output-persistence check (TRUST-WITHOUT-VERIFY gate).** Any
  command body or main-session dispatch that sends work to a Write-capable agent contracted
  to emit one or more specific artifacts MUST existence-check each declared output path on
  disk BEFORE consuming the in-message result or building on it in subsequent phases.

  Enforcement:
    1. After the agent returns, stat or ls each declared output path.
    2. If the file exists on disk: proceed normally.
    3. If the file does NOT exist on disk (in-message-only result):
       (a) Treat the artifact as NOT DELIVERED.
       (b) Persist the artifact from the in-message return text to the declared path, OR
           re-dispatch the agent with an explicit write instruction.
       (c) Confirm existence before proceeding.

  Application scope: any agent dispatched with a contracted emit path. The contracted
  emit path is determinable from:
    - The agent routing table (e.g., auditor → active-project/staff/auditor/<scope>-audit.md;
      screen-writer, studio, margit, renderer, editor, fixer similarly).
    - Explicit path declarations in the command phase brief sent to the agent.

  This check is always cheap (one stat/ls). It is never optional.

  OPTIONAL COMPANION (same implementation pass, cost S):
    In command bodies that fan out to Write-capable emitters (/and-write, /and-facets,
    /and-review, /and-stitch, /and-cohere Phase 2-3), add a per-phase existence-check
    note in the phase's closing step:

      "**Emit verify:** before reading this phase's output for downstream use, confirm
      the emitter's declared artifact is on disk at the expected path. If absent, persist
      from in-message return or re-dispatch."

    This companion is low-value if Rule 19 is implemented in CLAUDE.md (both enforce the
    same discipline); include only if the principal wants belt-and-suspenders per command body.

cost_estimate: S
status: implemented
triaged_at: 2026-06-07
triaged_by: principal (session)
disposition_note: "ACCEPTED + IMPLEMENTED as CLAUDE.md Rule 19 (2026-06-07). Optional per-command companion NOT added — Rule 19 enforces the discipline globally."
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0044

```yaml
id: PROP-0044
created_at: 2026-06-07T00:00:00Z
created_by: admin process-critic
trigger:
  reason: principal-initiated-retro
  source_report: active-project/staff/auditor/cohere-b01-all-aggregate-audit.md
  source_verdict: retro (session retrospective on the /and-cohere b01 all cycle, 2026-06-06; no gate verdict)
target:
  type: agent-card
  path: CLAUDE.md
  section: "Rules — dispatch-discipline (new rule, candidate Rule 20)"
change_type: add
rationale: |
  During the /and-cohere b01 all session (2026-06-06), an admin user-proxy dispatch
  (DEC-0108) was given Edit/Write access to `active-project/staff/cohere/b01-all-state.md`
  and mutated that file after the main session's own write. The admin edit introduced a
  duplicate YAML `result:` key (a `result: null` initial value coexisting with a
  `result: SKIPPED` stamp in the same mapping node — schema-invalid per audit fault-002).
  The main session committed on top of the mutated file without reading the diff;
  the defect was caught only by the subsequent auditor pass. This is the class of failure
  where an async agent with Edit/Write access modifies shared state, and the dispatcher
  treats the state as settled based on its own prior version rather than the mutated result.

  The gap is distinct from PROP-0043 (output-persistence): PROP-0043 targets agents that
  FAIL to write a file; this proposal targets agents that SUCCESSFULLY mutate a shared file
  in ways the dispatcher does not review before committing. The failure mode is: dispatcher
  writes state → dispatches async agent with Edit/Write to same state → agent mutates state
  → dispatcher commits without reading the resulting diff → defect ships.

  The affected shared state surfaces are: cohere-state files; parking-lot.md; showrunner
  memory.md; decisions.md; process-proposals.md; and any other file written by BOTH the
  main session and an async agent in the same invocation. The fix is a single read-back
  of the mutated file (or equivalent diff) after the async agent returns, before the
  dispatcher treats the state as settled. This is cheap, targeted, and structurally prevents
  the entire class.

  First occurrence at the explicit-defect-introduction level. Proposing at first occurrence
  because: (a) any async agent with Edit/Write dispatched to a shared state file can
  introduce schema-invalid edits, and the failure is silent (no gate fires on a committed
  defect until a downstream auditor reads the file); (b) the check is trivially cheap;
  (c) the affected surfaces include `decisions.md` and `process-proposals.md` — the admin
  agent's own shared-state output — making the gap self-referential and worth closing early.

  change_type: add — no existing CLAUDE.md rule or dispatch-discipline convention
  requires a post-agent-mutation read-back before committing shared state. Rule 4
  ("Nothing moves without being recorded") governs story-state authorship; it does not
  govern dispatch-state review. PROP-0043's output-persistence check is orthogonal
  (existence vs. content integrity). A separate rule is warranted.
evidence_refs:
  - "active-project/staff/auditor/cohere-b01-all-aggregate-audit.md — fault-002: state file
    b01-all-state.md revise_queue[0] — duplicate result key (result: null AND result: SKIPPED);
    'Introduced by the admin DEC-0108 edit'; resolution: RESOLVED (fixer pass)"
  - "staff/admin/decisions.md — DEC-0108 (the admin user-proxy dispatch that held Edit/Write
    to active-project/staff/cohere/b01-all-state.md; the duplicate key was introduced in that
    dispatch's edit)"
  - "CLAUDE.md §Rules — no existing rule requires the dispatcher to read-back shared state
    files after an async agent with Edit/Write returns, before committing or building on
    those files"
  - ".claude/commands/and-cohere.md — Phase 3 triage step + admin dispatch protocol:
    admin is dispatched with Edit/Write to cohere-state; no post-dispatch diff-check step"
recurrence_count: 1
proposed_diff: |
  In CLAUDE.md, §Rules, add a new dispatch-discipline rule (next available number after
  Rule 19 / PROP-0043; candidate Rule 20):

  **Rule 20. Post-async-agent shared-state read-back.** When an async agent is dispatched
  with Edit or Write access to a SHARED state file — any file the main session has also
  written or will write in the same invocation — the session MUST read the resulting state
  of the touched paths BEFORE treating that state as settled or committing on top of it.

  The check applies to: cohere-state files; parking-lot.md; showrunner memory.md;
  decisions.md; process-proposals.md; and any other path the dispatcher names in the agent
  brief as a target for agent mutation.

  Procedure:
    1. Agent dispatch returns.
    2. Before proceeding: read the current state of every shared path the agent was
       authorized to touch (read the file or run git diff HEAD -- <path>).
    3. If the result is as expected: proceed.
    4. If the result introduces schema violations, duplicate keys, unexpected field
       mutations, or content the dispatcher did not authorize: correct before committing.
       Do NOT commit on top of an unreviewed agent mutation.

  Application scope: admin user-proxy + admin process-critic dispatches (both write to
  decisions.md and process-proposals.md), showrunner dispatches (write to memory.md and
  parking-lot.md), margit dispatches, fixer dispatches (write to cohere-state and facet
  files), and any other async dispatch with Edit/Write to shared state.

  DISTINCTION FROM PROP-0043 (Rule 19):
    Rule 19 addresses the case where an agent FAILS to write a contracted file (missing
    artifact). Rule 20 addresses the case where an agent SUCCESSFULLY mutates a shared file
    in an unreviewed way (defective content). Both rules apply independently; neither
    subsumes the other.

cost_estimate: S
status: implemented
triaged_at: 2026-06-07
triaged_by: principal (session)
disposition_note: "ACCEPTED + IMPLEMENTED as CLAUDE.md Rule 20 (2026-06-07)."
pr_ref: null
defer_until: null
supersedes: null
```

---

## PROP-0045

```yaml
id: PROP-0045
created_at: 2026-06-07T00:00:00Z
created_by: admin process-critic
trigger:
  reason: principal-initiated-retro
  source_report: active-project/staff/auditor/cohere-b01-all-aggregate-audit.md
  source_verdict: retro (session retrospective on the /and-cohere b01 all cycle, 2026-06-06; no gate verdict)
target:
  type: command
  path: .claude/commands/and-cohere.md
  section: "Phase 3 — Triage / Phase 4 — aggregate authoring (pre-commit RECONCILE sub-step)"
change_type: add
rationale: |
  During the /and-cohere b01 all session (2026-06-06), the principal hand-authored the
  cohere aggregate (rolled-up verdict + Phase 3 triage + parking-lot item + state write).
  The subsequent auditor pass found three independently-authored defects that a brief
  structured self-check at authoring time would have caught:

  (1) fault-001 — citation error: the aggregate's triage note cited DEC-0105 as the
  authority for treating naive-q6 as design-accepted at whole-book cohere scope. DEC-0105's
  actual subject was the depth-pass deferral (skip the depth-pass revise loop before
  /and-review verdict b01); it says nothing about the cohere-axis naive-q6 acceptance.
  The real authority was the per-chapter DEC chain (DEC-0060/0062/0066/0072/0074/0085/
  0087/0090/0096/0099/0104) plus DEC-0109 (the process-critic dispatch authored by the
  same run). The citation was imprecise/circular and visible in the output at authoring time.

  (2) fault-004 — self-contradiction: the aggregate's parking-lot item text described a
  TWO-point fix (c03 establish + c20 confirm), but target.scope named only b01c03 — the
  c20 confirm-leg was untracked. The item's own description named both points; the
  target.scope omitted one. This contradiction was visible in the output at authoring time.

  (3) fault-003 — schema-id format drift: the cohere parking-lot items used the convention
  `pl-<YYYY-MM-DD>-cohere-<NNN>` (cohere- infix). The parking-lot schema at authoring
  time specified `pl-<YYYY-MM-DD>-<NNN>` (no infix). SYSTEMATIC deviation across ~6 items
  (pl-2026-06-01-cohere-001..005 + the b01-all item). Root-fixed by amending the schema
  this session (the established convention was legitimate; the schema was wrong). A
  citation-format check at authoring time would have detected the drift.

  All three are visible-at-authoring-time defects on hand-authored rollup artifacts — the
  exact class a structured pre-commit self-check catches. The class generalizes: any
  /and-cohere aggregate or /and-review verdict rollup hand-authored by the orchestrating
  session faces citation-accuracy, report-to-state field-equality, and self-contradiction
  risks that no downstream gate is specifically designed to catch at the authoring layer
  (the auditor catches them post-hoc, not pre-commit).

  This is an add (change_type: add) — no pre-commit self-check sub-step exists in
  /and-cohere Phase 3/4 or in /and-review (verdict/cohere subcommands). The closest
  existing mechanism is the post-hoc auditor pass (not always invoked; separate dispatch;
  costs model tokens to find defects that are free to catch at authoring time).

  Proposing at first explicit-fault-instance. Rationale for first-occurrence proposal:
  (a) fault-001 and fault-004 are simultaneously present in the same artifact — a
  structural pattern, not a one-off; (b) fault-003 is a systematic drift across multiple
  items; (c) the check is mechanizable at near-zero cost; (d) the target command body is
  the natural home — the check belongs at the phase that authors the aggregate, not at a
  separate auditor dispatch; (e) /and-review verdict rollups face the same citation-accuracy
  risk and benefit from the same sub-step.

  Distinct from PROP-0043 (output-persistence) and PROP-0044 (async-agent shared-state
  read-back): those proposals target dispatch execution; this proposal targets the authoring
  discipline of the hand-authored aggregates those dispatches produce.
evidence_refs:
  - "active-project/staff/auditor/cohere-b01-all-aggregate-audit.md — fault-001: triage
    cites DEC-0105 as naive-q6 cohere-scope authority; DEC-0105's actual scope is depth-pass
    deferral; correct authority is per-chapter DEC chain (DEC-0060/0062/0066/0072/0074/0085/
    0087/0090/0096/0099/0104) + DEC-0109"
  - "active-project/staff/auditor/cohere-b01-all-aggregate-audit.md — fault-004:
    pl-2026-06-06-cohere-001 item text names two resolution points (c03 establish + c20
    confirm); target.scope filed as b01c03 only; c20 confirm-leg untracked; criteria:
    'file a second item targeting b01c20'"
  - "active-project/staff/auditor/cohere-b01-all-aggregate-audit.md — fault-003:
    pl-<YYYY-MM-DD>-cohere-<NNN> id format violates schemas/parking-lot.schema.md
    pl-<YYYY-MM-DD>-<NNN> spec at authoring time; ~6 items; root-fixed by schema amendment
    this session to permit optional [-<label>] infix"
  - "schemas/parking-lot.schema.md — id format specification (post-session-fix: now permits
    optional [-<label>] infix per the established convention; fault-003 drove the schema
    amendment)"
  - ".claude/commands/and-cohere.md — Phase 3 (triage) and Phase 4 (aggregate authoring):
    no pre-commit self-check sub-step; post-hoc process-critic dispatch at Phase 4.5 fires
    after commit, not before"
  - ".claude/commands/and-review.md — verdict subcommand aggregate authoring: no citation-
    resolution or report-to-state field-equality check step; same risk class"
recurrence_count: 1
proposed_diff: |
  PRIMARY TARGET — .claude/commands/and-cohere.md, Phase 3 (triage) and Phase 4
  (aggregate authoring), add a pre-commit RECONCILE sub-step immediately before the
  phase's output is written to disk:

  **Pre-commit self-check (RECONCILE).** Before committing the cohere aggregate (triage
  note, state write, parking-lot items), run the following three checks in order:

    CHECK 1 — CITATION RESOLUTION.
    For every DEC-<NNNN>, PROP-<NNNN>, or pl-<date>-<NNN> id cited in the aggregate:
      (a) Confirm the id exists in its owning file (decisions.md, process-proposals.md,
          parking-lot.md). If absent, mark as MISSING-CITATION.
      (b) Confirm the claim the aggregate makes about that id matches what the id actually
          says. Specifically: if a DEC is cited as "the authority for X," read the DEC's
          decision/rationale and confirm it adjudicates X. If it does not, replace the
          citation with the correct id(s) or correct the claim.
    Also confirm that any generated parking-lot item id matches schemas/parking-lot.schema.md
    id pattern (pl-<YYYY-MM-DD>[-<label>]-<NNN>).
    Blocking: any MISSING-CITATION, citation-mismatch, or id-format violation blocks commit.

    CHECK 2 — REPORT-TO-STATE FIELD-EQUALITY.
    Compare the aggregate's front-matter axes/queue against the state file's corresponding
    fields. Specifically:
      (a) load_bearing_fails count in the report = load_bearing_fails count in the state.
      (b) failed_axes list in the report matches failed_axes list in the state.
      (c) caution_axes, revise_queue[*].chapter, and revise_queue[*].result in the state
          match the aggregate's triage disposition.
    Blocking: any mismatch blocks commit.

    CHECK 3 — SELF-CONTRADICTION SCAN (judgement check; not fully mechanizable).
    For each parking-lot item in the aggregate:
      (a) Count the number of atomic resolution points named in the item's text
          (e.g., "c03 establish AND c20 confirm" = two points).
      (b) Confirm that the number of filed items for this finding equals the number of
          atomic resolution points. If the text describes N points but only 1 item is filed,
          flag as RESOLUTION-COUNT-MISMATCH and split the item before committing.
    Blocking: RESOLUTION-COUNT-MISMATCH blocks commit.

  Output of the RECONCILE sub-step: a three-line check summary inline before the commit
  block (CHECK 1: PASS/N-issues, CHECK 2: PASS/N-mismatches, CHECK 3: PASS/N-splits).
  All three PASS → proceed to commit. Any FAIL → correct before committing.

  SECONDARY TARGET — .claude/commands/and-review.md, verdict subcommand aggregate
  authoring: add the same CHECK 1 (citation resolution + id-format validation) and
  CHECK 2 (verdict report front-matter vs. state field-equality). CHECK 3 adapted to:
  "each finding bullet matched to a DEC-id that exists and adjudicates that finding."
  Same blocking semantics.

cost_estimate: M
status: implemented
triaged_at: 2026-06-07
triaged_by: principal (session)
disposition_note: "ACCEPTED + IMPLEMENTED as CLAUDE.md Rule 21 + RECONCILE sub-steps in and-cohere.md Phase 7 and and-review.md (cohere Phase 4 + verdict persist), 2026-06-07."
pr_ref: null
defer_until: null
supersedes: null
```


## PROP-0046

```yaml
id: PROP-0046
created_at: 2026-06-08T14:05:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: PASS-WITH-NOTES (principal-rejected on read; DEC-0115)
target:
  type: schema
  path: schemas/bones.schema.md + schemas/facet.schema.md + .claude/commands/and-stitch.md + .claude/commands/and-write.md + audience persona cards (Threshold Discipline)
  section: "prose register fence (cross-surface)"
change_type: add
rationale: |
  Book 1 narrated nearly every event as bookkeeping ("the count let him go," "the gap propagated,"
  "I closed the entry," "I held the feet"), replacing literal action with its accounting-trace until a
  reader could not reconstruct the scene. The abstraction originates at the bones layer (b01-c01 bones:
  "the insects propagate / the nearest dozen bodies yield / the gap propagates") and is faithfully
  carried through stitch. No surface in the chain prohibits register-as-narration; the project's
  "signature" actively licensed it. Per DEC-0115 the ledger/accounting/apparatus register is retired as a
  prose mode. This requires a fence that exists at every authoring surface, not a single gate.
evidence_refs:
  - completed-works/taylor-westeros-good-intentions/book-one.md (whole, esp. c10-c19)
  - projects/taylor-westeros-good-intentions/theater/bones/b01-c01.md (abstract bones origin)
  - .claude/commands/and-stitch.md Phase 4 (PROP-0022 person-first lever; insufficient — fence not ban)
  - projects/taylor-westeros-good-intentions/voice-exemplar.md (the breathing target the prose ignored)
recurrence_count: 1
proposed_diff: |
  NO-LEDGER FENCE (cross-surface). The apparatus a narrator perceives through (feed/count/ledger/
  column/network/sense-power) may be a LENS but may NOT be the grammatical subject of narration nor the
  unit by which events are reported. Events render as concrete physical/human action first.
  - bones.schema.md: SVO bones must name a concrete actor + concrete action; "the gap propagates" /
    "the count closes" class subjects (abstraction-as-subject) are REJECT.
  - and-write Phase 6: ABSTRACTION-AS-SUBJECT becomes a HARD bone-gate finding (see PROP-0049).
  - and-stitch Phase 4: ledger/accounting/apparatus register is PROHIBITED, not merely de-preferred
    (see PROP-0047). LEDGER-REGISTER findings re-render concretely or route upstream.
  - audience cards: add a Threshold-Discipline clause that a reviewer may NOT excuse opacity as
    "signature/intended register"; followability is judged against a naive reader.
  Authoritative home: CLAUDE.md Rule 22.
cost_estimate: M
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session)
disposition_note: "ACCEPTED per DEC-0115 ('no ledger at all'). CLAUDE.md Rule 22 + stitch/write edits this session; schema + card edits staged. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/optimistic-newton-YCnTC
defer_until: null
supersedes: null
```

## PROP-0047

```yaml
id: PROP-0047
created_at: 2026-06-08T14:06:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: PASS-WITH-NOTES (principal-rejected on read)
target:
  type: command
  path: .claude/commands/and-stitch.md
  section: "Phase 9 — cold-read terminal gate; Phase 4 — voice transform"
change_type: modify
rationale: |
  The Phase-4 voice-embodiment lever (PROP-0022) only *preferred* person-first where both renderings were
  bone-faithful, and fell back to apparatus-register (logging EMBODIMENT-BLOCKED) whenever the bones were
  abstract — which, in this book, was nearly everywhere. The Phase-9 cold-read ran per-chapter and was
  calibrated to the chapter's own signature, so it normalized the register instead of failing it. Neither
  gate ever asked the only question that matters: "can a naive reader say what physically happens here?"
evidence_refs:
  - .claude/commands/and-stitch.md Phase 4 (URI-STITCH-VOICE-EMBODIMENT) + Phase 9
  - staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md (B1: "abstraction-muffle ... events stayed legible" — false-negative)
recurrence_count: 1
proposed_diff: |
  (1) Phase 4: upgrade the person-first preference to a PROHIBITION on ledger/accounting/apparatus
      register (VOICE-APPARATUS-DEFAULT -> LEDGER-REGISTER, HARD within-stitch; re-render concrete or
      route to /and-write revise as EMBODIMENT-BLOCKED).
  (2) Phase 9: add a NAIVE-FOLLOW sub-gate. A fork holding NO signature/contract context renders a
      one-paragraph plain-English "what physically happens" summary per scene. If it cannot, FOLLOW-FAIL
      (blocking; routes to /and-write revise). This fork may not be told the register is intentional.
cost_estimate: S
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session)
disposition_note: "ACCEPTED per DEC-0115. Implemented this session. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/optimistic-newton-YCnTC
defer_until: null
supersedes: null
```

## PROP-0048

```yaml
id: PROP-0048
created_at: 2026-06-08T14:07:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: PASS-WITH-NOTES (Class-B cohort accepted as design-inherent)
target:
  type: command
  path: .claude/commands/and-review.md + .claude/commands/and-stitch.md
  section: "verdict disposition rules / per-chapter caveat-ship disposition"
change_type: modify
rationale: |
  The dominant disposition problem (schema anti-pattern: "the gate caught it but the author shipped
  anyway"). The recurring AIRLESS finding was classified DESIGN-INHERENT ~16 consecutive times
  (DEC-0060..0104) and 7 consecutive chapters shipped SHIPPED-WITH-CAVEATS with no circuit breaker.
  A defect class that recurs is, at some count, no longer "design-inherent" — it is an unaddressed
  systemic defect wearing that label.
evidence_refs:
  - staff/admin/decisions.md DEC-0060/0062/0066/0072/0074/0078/0085/0087/0090/0094/0096/0098/0100/0101/0102/0104/0105
  - staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md (A2 Class-B cohort: 7 consecutive)
recurrence_count: 16
proposed_diff: |
  Add a CONSECUTIVE-CAVEAT CIRCUIT BREAKER: the same defect class may be dispositioned
  "design-inherent / accepted-caveat" at most N consecutive chapters (default N=2). The (N+1)th
  occurrence auto-promotes the finding from NOTE to BLOCKING and forces a depth-pass or an explicit
  principal escalation BEFORE further ships — it may no longer be auto-accepted under the standing
  disposition. Wire the counter into aggregate-state and check it at /and-stitch Phase 9.5 and
  /and-review verdict.
cost_estimate: M
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session)
disposition_note: "ACCEPTED per DEC-0115. Command-body wiring staged; recorded as binding policy now. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/optimistic-newton-YCnTC
defer_until: null
supersedes: null
```

## PROP-0049

```yaml
id: PROP-0049
created_at: 2026-06-08T14:08:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: PASS-WITH-NOTES (event-poverty)
target:
  type: command
  path: .claude/commands/and-write.md
  section: "Phase 6 — substance bone-gate"
change_type: modify
rationale: |
  The unreadability begins in the bones: events were authored as abstract nominalizations
  ("the gap propagates," "the count closes") rather than concrete actor+action. The existing
  EVENT-NOT-CONCRETE gate fires only on the single central-event bone, so a scene built almost entirely
  of abstract bones passes. The stitcher cannot un-abstract what the bones never made concrete.
evidence_refs:
  - projects/taylor-westeros-good-intentions/theater/bones/b01-c01.md (bones 12-14, 18-27)
  - .claude/commands/and-write.md Phase 6 (EVENT-NOT-CONCRETE / ABSTRACTION-DOMINANT)
recurrence_count: 1
proposed_diff: |
  (1) ABSTRACTION-AS-SUBJECT: a bone whose grammatical subject is the apparatus/an abstraction rather
      than a concrete actor is a HARD bone-gate finding (was: SIGNAL ABSTRACTION-DOMINANT).
  (2) CONCRETENESS FLOOR: each scene must hold a minimum ratio of concrete-SVO bones to
      accounting/abstract bones (default >= 0.6 concrete). Below floor -> SCENE-ABSTRACT-DOMINANT HARD.
  (3) Promote EMBODIMENT-BLOCKED: when /and-stitch returns >=K EMBODIMENT-BLOCKED on a chapter, it
      routes to /and-write revise (the fix is content bones must supply), not a silent ship.
cost_estimate: M
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session)
disposition_note: "ACCEPTED per DEC-0115. Phase 6 edit this session. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/optimistic-newton-YCnTC
defer_until: null
supersedes: null
```

## PROP-0050

```yaml
id: PROP-0050
created_at: 2026-06-08T14:09:00Z
created_by: admin process-critic
trigger:
  reason: failure
  source_report: staff/reviews/verdict-b01-2026-06-06T04-08-37Z.md
  source_verdict: PASS-WITH-NOTES (interior-sameness across c10-c19)
target:
  type: command
  path: RUNBOOK.md + .claude/commands/and-substance.md
  section: "Producing a chapter protocol (mandatory cohere cadence) / series signature authoring"
change_type: add
rationale: |
  The interior-sameness/repetition cluster (c10-c19: same scene shape every chapter) is invisible to
  every per-chapter gate by construction, and /and-cohere — the one cross-chapter gate that catches it —
  was opt-in and its standing queue items were principal-deferred. Separately, the root enabler was a
  single-axis "signature" with no readability counterweight, allowing register to be optimized to
  unreadability.
evidence_refs:
  - completed-works/taylor-westeros-good-intentions/book-one.md c10-c19
  - RUNBOOK.md ("/and-cohere is ... NOT in this chain ... opt-in")
  - staff/showrunner/memory.md substance.state_axes (single-axis register-as-signature)
recurrence_count: 1
proposed_diff: |
  (1) Make /and-cohere MANDATORY at book-thirds (~1/3 and 2/3 of planned chapters) in the
      chapter-production protocol, not opt-in. A FAIL-COHERE on interior-sameness blocks further ships
      until addressed.
  (2) /and-substance series: a substance signature may NOT be satisfiable by a prose register, and must
      declare a readability/concreteness floor as a non-negotiable constraint the register coexists with
      (prevents register-as-substance single-axis optimization).
cost_estimate: M
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session)
disposition_note: "ACCEPTED per DEC-0115. Wiring staged; binding policy recorded now. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/optimistic-newton-YCnTC
defer_until: null
supersedes: null
```

---

## PROP-0051

```yaml
id: PROP-0051
created_at: 2026-06-08T00:00:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md
  source_verdict: principal-directive (DEC-0116) — "consider if and-facets is adding value; find the cheapest way to simplify yet improve"
target:
  type: command
  path: .claude/commands/and-facets.md
  section: "Phase 3 (R2 fanout) + Phase 4 (R2 fanin) + Phase 4.5 + Phase 4.6 + Phase 5b (audience-gate)"
change_type: delete
rationale: |
  /and-facets was the single most expensive step in chapter production (~60-100 dispatches typical, up
  to ~180), dominated by two review layers whose value the evidence does not justify: (1) the R2 facet-
  judging round (5-6 parallel judges re-culling R1) and (2) the Phase 5b per-facet 3-of-3 adversarial
  audience-gate (up to (9+speakers)x3 dispatches/cycle x 3 cycles + cap-burn). The b01-c01 ablation
  studies prove the facet STACK adds aggregate value (bones-only ranked last; full ranked #2/#5) but it
  concentrates in 3 facets (memory, location-state, state-updates); the biggest quality mover across all
  variants was pacing/whitespace/voice (a /and-stitch concern); and removing density facets sometimes
  IMPROVED rank ("room to breathe"). R2 optimizes for exactly the density the ablation shows hurts.
  DEC-0115 is dispositive on Phase 5b: the audience-gate reviewed an intermediate artifact the reader
  never sees and blessed ~16 consecutive AIRLESS chapters "by signature" while the reader found the book
  unreadable — the worst outcome from the most expensive gate. DEC-0033's "skipping facets costs more
  downstream" rationale was premised on bones-quality being the risk; since then /and-write Phase 6 bone-
  gate + five-pass SVO + /and-review bones + the DEC-0115 no-ledger fence at write/stitch cover that
  surface upstream and downstream of facets. The live proof: the no-ledger re-cascade bypassed the full
  chain and produced the now-shipped drafts, which read better than the originals that went through it.
evidence_refs:
  - "active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md — bones-only ranked 12/12 and 15/15; full ranked #2/#5; value concentrated in memory/location-state/state-updates; pacing/whitespace outranked sensory/metaphor/interior"
  - "active-project/staff/ablation/b01-c01-2026-05-26T000543Z/cold-read-report-15variant.md — whitespace/cadence outranked sensory richness, metaphor variation, interior depth"
  - "staff/admin/decisions.md DEC-0115 — Phase 5b (and every facet gate) instructed to bless the unreadable signature; 16 AIRLESS dispositions with no circuit breaker"
  - "staff/admin/decisions.md DEC-0033 — full-process rationale was bones-quality risk, now covered upstream by /and-write Phase 6 + /and-review bones"
  - "staff/admin/decisions.md DEC-0116 — GO Option A (slim) with the R2 dialogue judge left to implementer"
  - ".claude/commands/and-facets.md — Phase 3/4/4.5/4.6 (R2 round) + Phase 5b (audience-gate) + cap-burn semantics"
recurrence_count: 2
proposed_diff: |
  Rewrite .claude/commands/and-facets.md to the slim flow: Phase 0 validate -> Phase 1 single R1
  authoring round (the facets; exposition surface:reference by default per PROP-0004) -> Phase 2 fanin
  (cite-index) -> Phase 2.5 context/aliveness review (writes context + grounding ledgers) -> Phase 3
  CONDITIONAL spine-hole remediation (slimmed descendant of the old 4.6, fired off 2.5; 0 dispatches
  common case) -> Phase 4 single mechanical auditor (12 classes; THE facet-layer gate; absorbs scene-map
  coverage + dialogue dedup/coverage sanity + the per-facet caps R2 enforced) -> Phase 4.5 admin process-
  critic (renamed from 5c) -> Phase 5 persist + orchestrator-critic verdict. DROP the R2 round
  (Phase 3/4/4.5/4.6 in old numbering) including the R2 dialogue judge (its dedup concern -> Phase 4
  auditor DEDUP class), and DROP Phase 5b + its cap-burn cycle. The adversarial prose read moves to the
  existing /and-stitch Phase 9 cold-read + naive-follow (DEC-0115-hardened). Net ~60-100 -> ~10-12
  dispatches. Coupled doc updates: CLAUDE.md Rules 11/13/15/17/18 + commands table + routing table +
  primary pattern; RUNBOOK pre-flight cap + R2 table + chain step 4; schemas/showrunner-memory.schema.md
  status table (faceted-r2 retired); staff/audience/and-facets-orchestrator-critic/card.md acceptance
  criteria + hot_buttons (criterion 4 audience-gate -> Phase 2.5/auditor).
cost_estimate: M
status: implemented
triaged_at: 2026-06-08
triaged_by: principal (session, via admin user-proxy DEC-0116)
disposition_note: "ACCEPTED + IMPLEMENTED this session per DEC-0116 (Option A). R2 dialogue judge dropped (implementer call); its dedup concern folded into Phase 4 auditor DEDUP. | RECONCILED accepted->implemented 2026-06-23: no-ledger fences verified live in command bodies (ABSTRACTION-AS-SUBJECT/SCENE-ABSTRACT-DOMINANT in and-write; LEDGER-REGISTER/EMBODIMENT-BLOCKED in and-stitch; naive-follow/FOLLOW-FAIL in and-stitch+and-facets; CLAUDE.md Rule 22)."
pr_ref: claude/ecstatic-volta-14ixm1
defer_until: null
supersedes: null
```

---

## PROP-0052

```yaml
id: PROP-0052
created_at: 2026-06-08T00:00:00Z
created_by: admin process-critic
trigger:
  reason: on-demand
  source_report: active-project/staff/reviews/sameness-scan-b01-c08-c20.md
  source_verdict: SAMENESS-HIGH (8 of 10 mid-book chapters run one scene template; longest unbroken run fails the >=4 threshold at c17-c19)
target:
  type: command
  path: .claude/commands/and-review.md
  section: "cohere subcommand (add a cheap structural-sameness pre-scan) OR a new cross-chapter check"
change_type: add
rationale: |
  The cohesion machinery has a real gap (confirmed this session): NOTHING detects cross-chapter
  STRUCTURAL SAMENESS — N consecutive chapters running the same scene-move template. Per-chapter
  Phase 9 cold-read cannot see it (each chapter reads fine alone); /and-cohere is opt-in, post-ship,
  and oriented to setup/payoff + register, not scene-shape repetition. The b01 mid-book (c10-c19) was
  diagnosed with this exact problem; the no-ledger rebuild fixed the register but left the structure,
  making the sameness MORE legible. A prototype detector (run this session on the rebuilt drafts)
  mechanically confirmed it: 8/10 mid-book chapters run TEMPLATE-T (packet-arrives -> transcribe ->
  withhold-the-protected-name -> lift-stylus -> hand-off-surface), with an unbroken run at c17-c19.
  The detector is CHEAP because it reads STRUCTURE (bones / scene-maps / dramatic_shape), not prose —
  ~1 dispatch over a chapter range, no re-render. It is the structural-layer analogue of CLAUDE.md
  Rule 22's "N=2 consecutive" circuit-breaker.
evidence_refs:
  - "active-project/staff/reviews/sameness-scan-b01-c08-c20.md — SAMENESS-HIGH; Template-T cluster c08-c19; 8/10 mid-book; breaks at c13/c16; threshold rule proposed"
  - "staff/admin/decisions.md DEC-0115 — no-ledger overhaul fixed register but preserved structure (rebuild rendered faithful-to-existing-structure)"
  - ".claude/commands/and-cohere.md + .claude/commands/and-review.md (cohere subcommand) — opt-in, post-ship; no scene-shape-repetition lens"
recurrence_count: 2
proposed_diff: |
  Add a cheap structural-sameness pre-scan as a sub-step of /and-review cohere (or a standing flag at
  /and-stitch Phase 10 forward-thread, which already reads accumulated past): over a chapter range,
  compute a per-chapter scene-shape signature (dramatic_shape + central scene-move template, derived
  from bones/scene-map — no prose read) and flag when >= 4 consecutive chapters share a signature OR
  >= 2 consecutive are interchangeable instances (the invariant beat does not change meaning). Emit a
  SOFT parking-lot flag suggesting a light /and-cohere structural pass; do NOT block. Threshold:
  accretion is licensed if longest unbroken run <= 3 AND the repeated beat changes meaning each time.
  ~1 dispatch per range; off the per-chapter critical path.
cost_estimate: S
status: open
triaged_at: null
triaged_by: null
disposition_note: null
pr_ref: null
defer_until: null
supersedes: null
```
