audit:
  scope: chapter
  target: b01c07
  gate: /and-facets b01-c07 Phase 4 mechanical audit (URI-FACETS-SLIM — sole mechanical gate; no R2 round; no Phase 5b audience-gate behind this)
  timestamp: 2026-06-08
  headline: FINDINGS-PRESENT — HARD: 4 / SIGNAL: 5
  earth_bet_fence: CLEAN
  curve_shape: SHAPE-OK
  gate: BLOCKED — 4 HARD findings route to fixer

  findings:

  # =========================================================
  # CLASS 1 — STRUCTURAL
  # =========================================================

    - id: fault-001
      type: fault
      class: STRUCTURAL
      severity: HARD
      what: >
        exposition-b01-c07.md: entries appear in non-monotonic id order. The entry with
        id=2 (anchor @0, prior-episode-bridge) is written before the entry with id=1
        (anchor @5, first-mention). Per facet.schema.md § Uniform line shape, ids must
        be monotonically increasing positive integers scoped per facet file. Current order
        in file: 2 @0 ... then 1 @5.
      why: >
        Cite-index build and stitcher Phase 1 consume exposition entries in id order.
        A non-monotonic file will cause the stitcher to fold the prior-episode-bridge
        preamble after the first-mention inline, reversing the render-position relative
        to the declared renders-as directives (italic-preamble before the body for @0;
        inline-appositive at @5 within the body). The result at stitch is a malformed
        chapter open.
      criteria: >
        exposition-b01-c07.md must renumber entries so id=1 is the prior-episode-bridge
        (@0) and id=2 is the first-mention (@5), matching file-order. Both entries must
        otherwise be preserved unchanged (gloss text, scope, renders-as, sources,
        licensed-by all intact).

    - id: fault-002
      type: fault
      class: STRUCTURAL
      severity: HARD
      what: >
        Feeling facet files are entirely absent. The dispatch brief declares feeling-taylor
        (1 entry) and feeling-halvard (3 entries). No feeling file exists on disk under any
        checked path:
          active-project/theater/facets/feeling-taylor-b01-c07.md          (not found)
          active-project/theater/facets/feeling-halvard-b01-c07.md         (not found)
          active-project/theater/facets/feeling-b01-c07.md                 (not found)
          active-project/theater/facets/feeling-taylor-hebert-b01-c07.md   (not found)
          active-project/theater/facets/feeling-septon-halvard-b01-c07.md  (not found)
        The grounding-ledger grd-001 notes that sensory:3@17 is the "minimum acceptable
        fallback" and that a Taylor feeling entry at @16/@17 was the preferred resolution.
        That preferred entry was never authored.
      why: >
        The feeling facet is a mandatory graph layer for any chapter with named characters
        performing somatic-tells. Its absence (a) leaves the frequency-band floor for feeling
        at 0% for both taylor (floor 2%) and halvard (floor 2%), both below the required
        2-5% per character; (b) leaves the rubric-fidelity multi-justification check
        unverifiable for any feeling entries; (c) leaves the grounding-ledger grd-001
        preferred resolution unmet — the bones-review forward note explicitly warned that
        the soc-tether +0.5 Δ displaced onto NI at @17/@24 must render as socially legible
        (Halvard reads Taylor's stance / Taylor reads herself setting it), and the preferred
        vehicle for that legibility is a feeling entry, not only a proprioceptive sensory
        entry. Without the feeling layer, the stitcher has no somatic-tell material
        for either character at the scene B/C peak bones.
      criteria: >
        Feeling files must be authored and persisted to disk for both taylor-hebert-kl-122ac
        and septon-halvard-flea-bottom at the declared entry counts (taylor: 1; halvard: 3)
        or at whatever counts the authoring rubric justifies. Requirements: per-character
        per-scene cap ≤1/scene hard; multi-justification ≥3 of 5; Earth-Bet fence clean;
        body-register only (no named-feeling vocabulary). The grounding-ledger grd-001
        requirement (a person-anchored ground at @16/@17 making the foot-planting socially
        legible, distinct from the @15 arithmetic-stillness and the @24 departure-steadying)
        must be addressed — preferred via a Taylor feeling entry at @16 or @17 that satisfies
        the "Halvard reads it / Taylor reads herself in it" legibility criterion.

    - id: fault-003
      type: fault
      class: STRUCTURAL
      severity: HARD
      what: >
        Actor state-update files are absent. The dispatch brief declares state-updates-taylor
        (3 entries) and state-updates-halvard (5 entries). Neither file exists on disk:
          active-project/theater/facets/state-updates-taylor-b01-c07.md    (not found)
          active-project/theater/facets/state-updates-halvard-b01-c07.md   (not found)
          active-project/theater/facets/state-updates-b01-c07.md           (not found)
        Only state-updates-env-b01-c07.md exists (4 entries covering studio and prop fields).
      why: >
        The state-updates layer is the canonical source for batched actor-state memory
        write-back at the chapter-close boundary. Without actor state-updates for taylor
        and halvard, showrunner cannot apply the chapter's substance_delta to actor state
        files. The chapter's declared axes in motion (political_register-prot +0.5,
        social_tether-prot-rise +1.0) have no actor-state-file carrier. The
        social_tether relational Δ at @17/@24 — which the bones-review forward note
        identified as partially displaced onto NI and requiring social legibility — also
        has no formal state-record. Halvard's new status as a genuine interlocutor
        (handoff_out: "Halvard: counter-argument genuinely engaged; not resolved; will
        return") similarly has no state-update record.
      criteria: >
        state-updates-taylor-b01-c07.md and state-updates-halvard-b01-c07.md must be
        authored and written to disk. Taylor's file must include field updates for
        political_register-prot and social_tether-prot-rise reflecting the chapter's
        declared Δ. Halvard's file must include at minimum a field update for his
        engagement status / awareness of Taylor as interlocutor consistent with handoff_out.
        All entries must use the state-updates schema shape:
          <id> @<anchor> <target>.<field>: <old> -> <new>

    - id: fault-004
      type: fault
      class: CONSTRAINT
      severity: HARD
      what: >
        vibes-b01-c07.md entry vibes:1 @2 carries a non-resolvable licensed-by source:
        "peak-bone:scene-A-2". The scene-map-b01-c07.md declares scene A with
        `peak-bones: none` — scene A has no peak-bones at all. "scene-A-2" cannot
        be resolved to any flat-id in any peak-bones array in the scene-map. The vibes
        schema requires licensed-by to be machine-resolvable (≥1 required source).
        A peak-bone citation pointing to a scene that declares no peak-bones is a
        dangling reference. This finding differs from the non-standard format issue
        in signal-004: those entries (vibes:2/3/5/6) use a non-standard format but
        DO resolve to real peak-bones; vibes:1's citation does NOT resolve.
      why: >
        A non-resolvable licensed-by source means vibes:1's peak-bone license cannot
        be validated. Any downstream tooling that enforces licensed-by resolution
        against the scene-map will hard-fail this entry. The other two cited sources
        (proto:2, proto:3) are valid and sufficient — the peak-bone token is both
        erroneous and redundant.
      criteria: >
        vibes:1 @2 must remove "peak-bone:scene-A-2" from its licensed-by list.
        The remaining sources proto:2 and proto:3 are sufficient to license the vibe.
        No other change to the entry is required.

  # =========================================================
  # CLASS 2 — FREQUENCY-BAND
  # =========================================================

    - id: signal-001
      type: flag
      class: FREQUENCY-BAND
      severity: SIGNAL
      what: >
        interest-narrator-b01-c07.md: 7 entries over 25 bones = 28%. The NI band is
        15-25% (ceiling 25%). Breach: 3 percentage points over ceiling. The author
        claim documented in showrunner memory is "load-bearing-interiority-carrier
        carve-out — 7 interior readings transferred to NI on a low-dialogue hinge
        chapter" (bones-review forward_note: "7 interior readings transferred to NI —
        treat all 7 as explicit deliverables (PASS-CHUNK-VOICE-RISK)"). However, no
        rubric carve-out preamble exists in interest-narrator-b01-c07.md. The file
        has only a standard header; the carve-out is documented in memory but not
        in the file itself. facet.schema.md § Rubric carve-out preamble V3 requires
        file-local preamble documentation for any exception to a cross-facet rubric.
      why: >
        The breach is denominator-driven (7 vs theoretical 6.25 ceiling on 25 bones)
        and the design justification is legitimate and documented in memory. However
        without a file-level carve-out preamble, the exception is not formally
        sanctioned and cannot be verified by downstream agents reading only the facet
        file. Classified SIGNAL not HARD because: (a) the 0.75-entry excess is
        marginal; (b) all 7 NI entries pass the three-axis test; (c) AP-scan is CLEAN
        (0 AP-001 hits in 7 entries); (d) the design rationale is well-documented
        upstream. A carve-out preamble in the file would clear this signal.
      criteria: null

    - id: signal-002
      type: flag
      class: FREQUENCY-BAND
      severity: SIGNAL
      what: >
        sensory-b01-c07.md: excluding grd-001-exempt sensory:3@17, there are 2 non-exempt
        entries (sensory:1@9 smell, sensory:2@19 tactile) over 25 bones = 8%. The sensory
        band ceiling is 6% (= 1.5 entries on 25 bones). Two entries exceeds the fractional
        ceiling by 0.5 entries. No grounding-ledger license exists for the non-exempt
        entries (grd-001 licenses only sensory:3).
      why: >
        The breach is marginal and denominator-driven. Both non-exempt entries carry
        substantive scene-grounding work: sensory:1@9 is the smell-transition at arrival
        (tallow-and-wax, grounding the entry into the sept corner); sensory:2@19 is the
        first-touch tactile (cold stone through soles, grounding the prolonged standing).
        Neither is decorative. Classified SIGNAL not HARD: a 25-bone chapter requires
        at minimum one smell and one tactile to meet modality-coverage ≥2 per episode,
        and those are the two entries in question. Forcing a deletion would violate
        modality-coverage. The stitcher should note sensory density is at the high end.
      criteria: null

  # =========================================================
  # CLASS 3 — METADATA-INCONSISTENCY
  # =========================================================

  # state-updates-env-b01-c07.md carries frontmatter `facet: state-updates` while the
  # filename uses the env sub-suffix. The schema defines a single `state-updates` type;
  # the env/taylor/halvard file-split is an organizational convention, not a schema
  # requirement. The frontmatter value is schema-conformant. Not faulted.
  # All other files carry correct schema-conformant frontmatter facet types. PASS.

  # =========================================================
  # CLASS 4 — CURVE-SHAPE
  # =========================================================

  # Dramatic_shape: hinge (from showrunner memory b01c07 block).
  # Scene-map rhythm-shapes:
  #   scene A @1-10: rising, peak-bones: none
  #   scene B @11-19: rising-to-peak, peak-bones: @14
  #   scene C @20-25: peak-and-release, peak-bones: @20, @21, @23
  #
  # A hinge shape requires: rising approach → recognition/argument peak → release/departure
  # without downward resolution (the argument is not resolved; the moment is planted for
  # later foreclosure at d09).
  #
  # Facet graph alignment:
  # - NI distribution: 3 in scene A (rising decoration @2/@3/@8), 2 in scene B
  #   (recognition approach @13/@15), 2 in scene C (peak @20 + release @24). Appropriate
  #   distribution across the hinge arc.
  # - Peak decoration: @14 (dialogue halvard:1), @20 (NI:6 + memory:2), @21 (dialogue
  #   taylor:1), @23 (dialogue halvard:2). All four peak-bones carry substantive facet
  #   content.
  # - Release: NI:7@24 explicitly encodes "nothing has resolved / the argument she is
  #   leaving standing, the one she half-believes and is walking away from anyway." This
  #   is the hinge's required unresolved-carry. PASS.
  # - No downward-resolution content anywhere in the graph. PASS.
  #
  # CURVE-SHAPE: SHAPE-OK

  # =========================================================
  # CLASS 5 — CONTRADICTION
  # =========================================================

  # State-updates-env continuity: hook-ward-lane → oc-sept-corner (@9) → hook-ward-lane
  # (@25). This is a clean open-close arc matching bones (bone 9: enters sept-corner;
  # bone 25: leaves sept-corner), memory handoff_in (Taylor on ward-coverage circuit),
  # and loc-state sequence. PASS.
  #
  # Vibes op coherence: all ++ ops on pre-loaded keywords confirmed in the vibes preamble
  # comment block (rising-entrapment / contempt-without-refusal / tragic-causal on taylor;
  # the-counter-argument-still-present / tragic-causal on halvard; all listed as
  # pre-loaded). All + ops create genuinely new keywords. No = op used. Token bundles
  # are non-sentence noun-phrase compressions per schema. PASS.
  #
  # NI vs memory at shared anchors: NI:4@13 / memory:1@13 are distinct (NI reads the
  # in-present-moment recognition; memory carries the callback to the series structure
  # of atonement-as-repetition). NI:6@20 / memory:2@20 are distinct (NI reads the
  # naming-as-prior-ownership; memory carries the callback to correct-calculation-wrong-
  # frame). No duplication. PASS.
  #
  # No contradictions found in any verifiable facet file. PASS.

  # =========================================================
  # CLASS 6 — DEDUP
  # =========================================================

  # No within-facet or cross-facet duplicate entries found among existing files.
  # Dialogue vs NI: no NI entries at @14, @21, @23 (the three dialogue anchors). No dedup.
  # Dialogue vs memory: memory fires at @13 and @20; no dialogue at those anchors. No dedup.
  # Cannot verify dialogue vs feeling dedup at shared anchors because feeling files are
  # absent (fault-002). PASS on verifiable scope.

  # =========================================================
  # CLASS 7 — SUPERFLUOUS
  # =========================================================

  # NI: all 7 entries pass three-axis test (audience-meaningful + functional-register ≥2 +
  # scene-eligible). NI:3@8 (fly-read on Halvard: "no angle on the man, only the child") is
  # the strongest SUPERFLUOUS candidate but passes on social-commentary + characterization
  # registers (it characterizes Halvard as read-resistant to tactical extraction and
  # establishes the chapter's central dynamic). PASS.
  # Memory: both entries link to declared series monuments
  # (monument-atonement-that-is-the-repetition / monument-correct-calculation-wrong-frame).
  # Neither is decorative. PASS.
  # Sensory: all three entries carry substantive grounding. PASS.
  # Vibes: 9 entries carry operator-bias work on load-bearing entities across all scene zones.
  # No superfluous vibes detected. PASS.
  # Exposition: prior-episode-bridge + first-mention-character both warranted. PASS.
  # Feeling files absent — cannot evaluate. Noted under fault-002.

  # =========================================================
  # CLASS 8 — CONSTRAINT
  # =========================================================

  # Memory NI-spine co-citation:
  #   memory:1@13 → NI:4@13 present. PASS.
  #   memory:2@20 → NI:6@20 present. PASS.
  #
  # Metaphor licensed-by: no metaphor entries. N/A.
  #
  # Feeling duplicating POV NI: cannot verify (feeling files absent — fault-002).
  #
  # Vibes licensed-by resolution:
  #   vibes:1: "peak-bone:scene-A-2" does not resolve. FAULT — see fault-004.
  #   vibes:2/3/5/6: non-standard format but resolve to real peak-bones. See signal-004.
  #   vibes:4/7/8/9: use proto: and canon: / world-build: sources — all resolvable. PASS.
  #
  # Exposition source-traceability:
  #   exposition @0 (prior-episode-bridge): gloss text traces to showrunner-memory
  #   handoff_in + chunk + prior-chapter glossed-terms. All claims derivable. PASS.
  #   exposition @5 (first-mention): gloss text traces to oc-sept-corner.card.md
  #   (chandler's storehouse / pastoral function confirmed), showrunner-memory cast,
  #   glossed-terms. All claims derivable. PASS.
  #
  # Exposition fire-rule (scene-open-orient): no scene-open-orient entries. N/A.
  #
  # Exposition re-gloss: the prior-episode-bridge @0 does not re-gloss any first-mention
  # terms from prior chapters; it is a reader-state refresh only. PASS.
  #
  # First-mention character coverage: Halvard is the chapter's only new named character;
  # exposition:1@5 provides his first-mention gloss. PASS.
  #
  # Dialogue behavior-card compliance:
  #   taylor:1@21 — compliant with taylor-hebert.card.md: short declaratives, numeric
  #   specificity (six years old / three days), cost-language (slow road / costs), no
  #   feeling vocabulary, clinical-of-the-horrible register for the named death, plain
  #   two-sentence close. Earth-Bet fence CLEAN. PASS.
  #   halvard:1@14 — compliant with westeros-septon.card.md: plain Anglo-Saxon register,
  #   body-matter vocabulary (bread/rot/hand), compound-interest homily pattern, plain
  #   closer ("It is the only one that costs less at the end"). No overpromising on Faith.
  #   Earth-Bet fence CLEAN. PASS.
  #   halvard:2@23 — compliant: cost-acknowledgment without doctrinal retraction, correct
  #   Faith vocabulary ("the Mother / she did not spare her" — appropriately refuses
  #   empirical promise), plain Anglo closer ("I will not invent one"). PASS.
  #
  # Earth-Bet fence (all text fields, all files, all dialogue utterances):
  #   NI entries: "feed prices" = Taylor's operational vocabulary; not Earth-Bet jargon.
  #   No parahuman terms, cape-register vocabulary, or Earth-Bet proper nouns in any
  #   NI, memory, sensory, loc-state, state-updates, vibes, or exposition entry.
  #   Dialogue (both characters): CLEAN.
  #   EARTH-BET FENCE: CLEAN.
  #
  # Per-scene sensory cap (≤3):
  #   scene A @1-10: sensory:1@9 = 1. PASS.
  #   scene B @11-19: sensory:2@19 + sensory:3@17 = 2. PASS.
  #   scene C @20-25: 0. PASS.
  #
  # Scene-map coverage: 25/25 bones in exactly 3 scenes, no gaps, no overlaps (per
  # scene-map file footer). PASS.
  #
  # Loc-state continuity-license: five entries cover approach (@1), corners-changed (@3),
  # passage-blocked (@4), sept-corner-entry (@9), exit (@25). Complete arc. PASS.
  #
  # Sensory old-state lineage:
  #   sensory:1@9 smell (hook-lane-ambient): first-touch on smell modality; old-state
  #   traces to loc-card oc-sept-corner.md § Sensory Vocabulary ("hook-lane-ambient"
  #   prior to tallow transition). PASS.
  #   sensory:2@19 tactile (lane-packed-earth-underfoot): first-touch on tactile modality;
  #   old-state traces to loc-card § Texture ("packed earth over old cobble" in passage)
  #   and loc-state:1@1 (lane-ambient-active). New-state (cold-stone-through-soles) traces
  #   to loc-card § Texture ("cold-holding stone") and loc-state:4@9. PASS.
  #   sensory:3@17 proprioceptive (weight-unanchored -> weight-settled-and-braced):
  #   first-touch on proprioceptive; grd-001 exempt per grounding-ledger. PASS.

    - id: signal-003
      type: flag
      class: CONSTRAINT
      severity: SIGNAL
      what: >
        exposition-b01-c07.md entry id=1 (after renumbering per fault-001) carries a dual
        scope tag: "scope: first-mention-term, first-mention-character". The exposition
        schema defines scope as a single scope-kind per entry. Two scope-kinds on one
        entry is non-conforming to the schema's field definition.
      why: >
        The intent is legitimate and space-efficient — the septon's role-term and the
        character's first appearance are coextensive (the term and the man enter together
        at @5). A single entry covering both scope-kinds is pragmatically reasonable but
        syntactically off-schema. If a stitcher or cite-index consumer expects a single
        scope token, "first-mention-term, first-mention-character" will fail to match
        either valid scope-kind individually.
      criteria: null

  # =========================================================
  # CLASS 9 — AP-SCAN
  # =========================================================

  # NI AP-001 check (feeling vocabulary in NI entries):
  #   NI:1@2: "the feed prices" — operational register. CLEAN.
  #   NI:2@3: "patrol-weight / settled-weight / mapped which faces" — operational. CLEAN.
  #   NI:3@8: "brings back nothing she can use / no angle on the man, only the child" —
  #   tactical register. CLEAN.
  #   NI:4@13: "registers, before he finishes the turn / the argument has her address" —
  #   recognition phrasing in cost register. CLEAN.
  #   NI:5@15: "the words land where she runs the arrangement / no exit she had not already
  #   counted" — cost-language, arrangement register. CLEAN.
  #   NI:6@20: "the name is hers to set down / the child the slow refusal would have left
  #   to die" — possessive-accounting register. CLEAN.
  #   NI:7@24: "the argument she is leaving standing / the one she half-believes and is
  #   walking away from anyway" — architectural-inventory register. CLEAN.
  #   AP-001 hits: 0 / 7 entries. Saturation rate: 0%. AP-SCAN CLEAN on NI.
  #
  # Vibes token-bundle sentence-parsability scan:
  #   All token bundles are hyphenated noun-phrase compressions; none parse as complete
  #   sentences (subject + finite-verb + object). CLEAN.

    - id: signal-004
      type: flag
      class: AP-SCAN
      severity: SIGNAL
      what: >
        vibes-b01-c07.md entries vibes:2@14, vibes:3@20, vibes:5@23, and vibes:6@14
        use the licensed-by format "peak-bone:scene-X-N" (e.g. "peak-bone:scene-C-20",
        "peak-bone:scene-B-14") rather than the schema-specified format "peak-bone:<flat-id>"
        (e.g. "peak-bone:20", "peak-bone:14"). These four citations DO resolve (scene-C-20
        → @20 is in scene C's peak-bones array; scene-B-14 → @14 is in scene B's peak-bones;
        scene-C-23 → @23 is in scene C's peak-bones). This distinguishes them from
        vibes:1's "peak-bone:scene-A-2" which does NOT resolve (fault-004).
      why: >
        Non-standard licensed-by format is a maintenance risk. If tooling enforces the
        schema's "peak-bone:<flat-id>" pattern, these four entries will require reformatting.
        Classified SIGNAL (not HARD) because they semantically resolve; the issue is
        syntactic non-conformance only.
      criteria: null

  # =========================================================
  # CLASS 10 — TASTE-FLAG
  # =========================================================

    - id: signal-005
      type: flag
      class: TASTE-FLAG
      severity: SIGNAL
      what: >
        Bone @16 ("taylor-hebert-kl-122ac faces septon-halvard-flea-bottom") is entirely
        undecorated — no facet entry of any kind fires at this anchor. It is the physical-
        blocking pivot between NI:5@15 (arithmetic-already-run recognition) and sensory:3@17
        (weight-settled-and-braced) with sensory:2@19 (cold-stone) downstream. The
        grounding-ledger grd-001 required a ground at @16/@17; its resolution note reads:
        "preferred: a Taylor feeling/NI tell that makes the foot-planting socially legible
        (the stance Halvard can read as 'she is not leaving / she is going to answer')."
        sensory:3@17 provides the minimum-acceptable fallback; the preferred feeling entry
        at @16/@17 was never authored (feeling files absent per fault-002).
      why: >
        @16 is the moment Taylor turns to face Halvard before setting her feet. The bones-
        review forward note warned: "the soc-tether +0.5 Δ is partially DISPLACED onto the
        NI facet — the body-rooting witnesses physical bracing; NI must render it as socially
        LEGIBLE (Halvard reads it; Taylor reads herself in it) or the relational Δ goes
        unearned at stitch." With @16 bare and the feeling layer absent, the stitcher arrives
        at this hinge with NI content from @15 (interior stillness/arithmetic), a proprioceptive
        sensory entry at @17 (body weight), and nothing anchoring the social legibility of
        the turn itself. The relational-Δ risk identified in the bones-review remains open.
        This SIGNAL is advisory for fixer and stitcher; it is a consequence of fault-002
        (the preferred resolution is a feeling entry).
      criteria: null

  # =========================================================
  # CLASS 11 — PILE-UP REVIEW
  # =========================================================

  # Maximum co-located facets per bone:
  #   @14: dialogue halvard:1 / vibes:2 / vibes:4 / vibes:6 = 4 entries.
  #   @20: NI:6 / memory:2 / vibes:3 = 3 entries.
  #   @9: sensory:1 / loc-state:4 / state-updates-env:3 = 3 entries.
  #   @25: loc-state:5 / state-updates-env:4 / vibes:9 = 3 entries.
  # Threshold is >4. No bone exceeds 4. PILE-UP: CLEAN.
  # @14's count of exactly 4 is warranted: the scene B peak-bone carries dialogue (load-
  # bearing), two taylor-vibes firing on the argument-landing, and one halvard-vibe. Each
  # entry serves a distinct facet-type function. Not over-decoration.

  # =========================================================
  # CLASS 12 — RUBRIC-FIDELITY
  # =========================================================

  # Sensory first-touch rubric: both first-touch entries (sensory:1 smell, sensory:2 tactile)
  # carry loc-card lineage per oc-sept-corner.md. Per-scene cap compliance verified (CLASS 8).
  # Disambiguation gate: sensory:1@9 (tallow-and-wax) — the bone says "taylor enters the
  # sept-corner"; the loc-card establishes tallow-and-wax as the corner's characteristic
  # ambient; without the sensory flag, the prose word "sept-corner" does not self-carry the
  # smell. Flag is warranted (proto-line word is bare). PASS. sensory:2@19 — bone is "the
  # cold stone presses... soles" which is already charged (the stone presses is self-carrying
  # cold-tactile to some degree). This is a borderline call on the disambiguation gate; the
  # sensory entry maps the transition from lane-packed-earth (the old-state) to cold-stone,
  # which the single bone does not self-carry as a modality-transition. PASS with note.
  #
  # NI carve-out preamble: 28% NI count (above 15-25% band) lacks a file-level carve-out
  # preamble per facet.schema.md § Rubric carve-out preamble V3. See signal-001.
  #
  # Vibes rubric: op coherence PASS. Token bundles PASS. licensed-by: fault-004 (vibes:1)
  # and signal-004 (vibes:2/3/5/6 format). All other entries: PASS.
  #
  # Metaphor rubric: zero-fires within 0-3% band. Refuse-log is comprehensive (AP7 on all
  # peak-zone candidates; no confirmed upstream anchors for shadow candidates;
  # Halvard's in-dialogue "crooked bread / straight road" cross-figure fence documented).
  # PASS.
  #
  # Exposition rubric: id-order fault (fault-001); dual-scope signal (signal-003). Content
  # and source-traceability PASS. Per-anchor cap (2 entries across 2 different anchors,
  # different scope categories) PASS.
  #
  # State-updates rubric: env file carve-out preamble for oc-handcart is correctly formatted
  # and annotated per facet.schema.md § Rubric carve-out preamble V3. Env entries cover
  # prop and studio fields. Actor files absent (fault-003).
  #
  # Feeling rubric: UNVERIFIABLE — files absent (fault-002). Cannot confirm per-character
  # per-scene cap, multi-justification ≥3 of 5, or any feeling-rubric element.
  #
  # Dialogue coverage (upstream-leak sanity): bones-review verdict CLEARS_FACETS on this
  # session's re-review. All three dialogue citations in bones (@14, @21, @23) resolve to
  # existing dialogue entries. All dialogue entries reverse-resolve to existing bones.
  # No orphan entries in either direction. PASS.

  # =========================================================
  # AUDIT SUMMARY
  # =========================================================

summary:
  status: FINDINGS-PRESENT
  hard_count: 4
  signal_count: 5
  earth_bet_fence: CLEAN
  curve_shape: SHAPE-OK
  gate: BLOCKED

  hard_findings_by_class:
    STRUCTURAL: 3
      # fault-001: exposition id non-monotonic (id=2 before id=1)
      # fault-002: feeling facet files entirely absent (taylor:1 / halvard:3 declared)
      # fault-003: state-updates-taylor and state-updates-halvard files absent
    CONSTRAINT: 1
      # fault-004: vibes:1 licensed-by "peak-bone:scene-A-2" does not resolve (scene A has no peak-bones)

  signal_findings_by_class:
    FREQ-BAND: 2
      # signal-001: NI 28% over 15-25% cap; no file-level carve-out preamble (design-warranted but undocumented)
      # signal-002: sensory excl. grd-001 exempt at 8% over 3-6% cap; marginal denominator-driven
    CONSTRAINT: 1
      # signal-003: exposition:1 carries dual scope tags (first-mention-term, first-mention-character)
    AP-SCAN: 1
      # signal-004: vibes:2/3/5/6 use non-standard "peak-bone:scene-X-N" format vs schema "peak-bone:<flat-id>"
    TASTE-FLAG: 1
      # signal-005: bone @16 entirely undecorated; physical-blocking pivot at scene B peak approach; relational-Δ legibility risk

  ni_band_adjudication: >
    The NI 28% breach classified SIGNAL not HARD. Rationale: (1) breach is 0.75 entries
    over the fractional ceiling on a 25-bone chapter; (2) the design justification is
    documented in showrunner memory as an explicit /and-write authoring decision (7 interior
    readings transferred to NI to pass the bones-gate on an argument chapter); (3) all 7
    entries pass three-axis test and AP-001 scan is 0/7. The SIGNAL is the absence of a
    file-level carve-out preamble, not the count itself. HARD would require decorative or
    AP-violating entries — none found.

  sensory_band_adjudication: >
    The sensory 8% breach classified SIGNAL not HARD. Rationale: 2 non-exempt entries on
    a 25-bone chapter is the minimum meaningful count to meet modality-coverage ≥2 per
    episode (smell + tactile). Forcing a deletion would violate modality-coverage. The
    breach is 0.5 entries over the fractional ceiling. Denominator-driven.

  routing: >
    BLOCKED. 4 HARD findings route to fixer. Suggested priority order:
    1. fault-002 (feeling files — most substantive gap; affects band floor, rubric-fidelity,
       stitcher somatic-tell content, and the grounding-ledger grd-001 preferred resolution).
    2. fault-003 (actor state-updates files — required for chapter-close write-back; 
       fast authoring based on declared Δ in memory).
    3. fault-001 (exposition id reorder — single renumber, no content change).
    4. fault-004 (vibes:1 licensed-by — single token removal; proto:2 + proto:3 are
       sufficient; no other change required).
    signal-005 should be reviewed alongside fault-002: the preferred resolution for the
    @16 decoration gap is a Taylor feeling entry at @16 or @17, which fault-002's fix
    must address. fixer resolving fault-002 should specifically address the @16/@17
    social-legibility requirement from grounding-ledger grd-001 as part of the feeling
    authoring.

---

## FIXER RESOLUTION + CORRECTION (orchestrator, Phase 4 remediation pass 1 — 2026-06-08)

**Two of the four reported HARDs were FALSE POSITIVES (auditor filename-resolution error), verified against disk per CLAUDE.md Rule 19:**

- **fault-002 (feeling files "absent") — RETRACTED.** `feeling-taylor-hebert-kl-122ac-b01-c07.md` (1 entry) and `feeling-septon-halvard-flea-bottom-b01-c07.md` (3 entries) BOTH exist on disk. The auditor searched for the abbreviated slug (`feeling-taylor-b01-c07.md`) instead of the full actor slug. Not a graph defect.
- **fault-003 (actor state-update files "absent") — RETRACTED.** `state-updates-taylor-hebert-kl-122ac-b01-c07.md` (3 entries) and `state-updates-septon-halvard-flea-bottom-b01-c07.md` (5 entries) BOTH exist. Same abbreviated-slug resolution error.
- Root cause: this test run skipped the Phase 2 cite-index merge (a stitcher convenience), which in the full pipeline consolidates per-character slices into `feeling.md` / `state-updates.md` with a known manifest the auditor reads. A harness artifact, not a pipeline defect. (Process note: the real `/and-facets` run does the merge, so this false-positive class does not arise in production.)

**Two genuine HARDs — RESOLVED by fixer (this pass):**

- **fault-001 (STRUCTURAL, exposition id monotonicity) — FIXED.** Renumbered so file order is `1 @0` (prior-episode-bridge / preamble) then `2 @5` (septon first-mention). Content unchanged.
- **fault-004 (CONSTRAINT, vibes:1 non-resolvable licensed-by) — FIXED.** Removed the `peak-bone:scene-A-2` token (scene A has `peak-bones: none`); the remaining `proto:2, proto:3` sources are valid and sufficient.

**SIGNAL findings (5) — carried, non-blocking** (NI 28% denominator-driven carve-out; sensory 8% denominator-driven; exposition dual-scope tag; vibes peak-bone format off-schema but resolvable; @16 undecorated → routed to /and-stitch as VOICE-FIXABLE per Phase 2.5). These match the OLD c07 run's SIGNAL dispositions (NI carve-out + denominator-driven band notes).

**FINAL GATE: PASS — 0 HARD** after 1 fixer pass. CURVE-SHAPE SHAPE-OK. Earth-Bet fence CLEAN. The facet layer clears to persist WITHOUT any R2 round or audience-gate.
