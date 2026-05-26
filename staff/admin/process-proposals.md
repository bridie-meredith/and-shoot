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
