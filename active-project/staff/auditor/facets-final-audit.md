audit: facets-final-r1
episode: s01e03
date: 2026-05-12
mode: flag-only
status: FINDINGS-PRESENT
totals: 19 findings across 7 facets

---

# Phase 5 Facets Audit — s01e03 — r1

## Preamble

Audit runs against: proto-lines/s01e03.md (155 active proto-lines), nine facet files at active-project/theater/facets/ (post-R2), _cite-index.md (335 entries; 54.2% density), .r2-decisions.md (f-r2-counts all-zero), and series-law constraint files per showrunner memory. Rubric authority: schemas/facet.schema.md, design/shoot-v2/rubric-tensometer.md, and the task-dispatch FREQUENCY-BAND bands for all facet types.

Pre-read note on URI-CONSOLIDATION-CITE-DRIFT (documented pre-existing pipeline bug): the consolidation of per-character slices into single state-updates.md and feeling.md files renumbers local slice IDs to global IDs, but proto-line citation tokens were authored using local slice IDs. This mismatch is known and was documented in s01e02 audit as exceeding episode-scope remediation. Where it manifests as a concrete wrong-anchor citation, it is recorded as a HARD STRUCTURAL finding; where it creates cite-index anomalies with no wrong-anchor resolution impact, it is recorded as SIGNAL.

---

## Class 1 — STRUCTURAL

### Finding STR-001
- **id:** flag-001
- **type:** fault
- **class:** STRUCTURAL — HARD
- **what:** feeling.md cite-index cross-anchor citation mismatch — proto-lines @6, @15, @53, @98, @131, @145 all cite `[feel:N]` tokens that use per-character-slice local IDs. In the consolidated feeling.md, these tokens resolve to wrong anchors.
  - Proto-line @6 cites `[feel:1] [feel:2]`. In consolidated feeling.md, feel:1 = oc-broken-maester @90 and feel:2 = oc-tanner-elder @6. The `[feel:1]` citation at @6 therefore points to the maester's tell at @90, not the elder's tell at @6. The elder's tell at @6 is correctly cited by `[feel:2]`.
  - Proto-line @15 cites `[feel:1]`. Taylor's per-slice local feel:1 (@15) is consolidated feel:5. The citation `[feel:1]` at @15 resolves to the maester's @90 entry.
  - Proto-line @53 cites `[feel:2]`. Taylor's per-slice local feel:2 (@53) is consolidated feel:6. The citation `[feel:2]` at @53 resolves to the elder's @6 entry.
  - Proto-line @98 cites `[feel:1] [feel:4]`. Father's per-slice local feel:1 (@98) is consolidated feel:4 — but the `[feel:1]` token also appears here, pointing again to the maester's @90 entry. The `[feel:4]` is correct.
  - Proto-line @131 cites `[feel:2] [feel:3]`. Elder's per-slice local feel:2 (@131) is consolidated feel:3. The citation `[feel:2]` at @131 resolves to the elder's @6 entry (wrong); `[feel:3]` is the consolidated ID for the elder's @131 entry (correct).
  - Proto-line @145 cites `[feel:3]`. Taylor's per-slice local feel:3 (@145) is consolidated feel:7. The citation `[feel:3]` at @145 resolves to the elder's @131 entry.
  - Confirmed by cite-index: feel:5 @15 back=N (no proto-line cites feel:5); feel:6 @53 back=N; feel:7 @145 back=N. All three Taylor feeling entries are uncited by the proto-lines they should anchor to.
- **why:** The stitcher resolves `[feel:N]` tokens to the consolidated feeling.md. Stale tokens mean: the elder's @6 tell (feel:2) is cited correctly but also has a spurious feel:1 co-citation pointing to the maester's @90 entry; Taylor's three feeling entries (feel:5, feel:6, feel:7) are uncited by their anchor proto-lines; the maester's feel:1 is cited at @6, @15, @98 in addition to its correct @90. The cross-facet consistency graph is broken for all feeling entries except the maester's.
- **criteria:** Proto-line citation tokens for feeling entries must resolve to the consolidated feeling.md entry at the same anchor. Specifically: proto-line @6 must cite `[feel:2]` only (not `[feel:1] [feel:2]`); proto-line @15 must cite `[feel:5]`; proto-line @53 must cite `[feel:6]`; proto-line @98 must cite `[feel:4]` only (remove `[feel:1]`); proto-line @131 must cite `[feel:3]` only (remove `[feel:2]`); proto-line @145 must cite `[feel:7]`. The cite-index must be rebuilt after correction.
- **routing:** fixer (proto-lines file token correction) + cite-index rebuild

---

### Finding STR-002
- **id:** flag-002
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** interest-narrator.md has ID gaps at positions 7 and 27 (post-R2 deletions) with no in-file deletion-gap comments. The file jumps from ID 6 to ID 8, and from ID 26 to ID 28. R2 decisions document these as deliberate DELETEs (narrator:7 @22 — voice-fidelity fail, "six hundred paces" at 400m radius; narrator:27 @114 — voice-fidelity fail, "doubled" when radius was 1.25×). The schema permits gaps from deletions; no error. No in-file comment is required per schema.
- **why:** Downstream tooling that expects monotonic IDs without gaps may misparse. The R2 decisions provide the deletion record, but a reader of the NI file alone cannot distinguish deletion-gap from authoring error. Editor-call.
- **routing:** interest-narrator author (advisory)

---

### Finding STR-003
- **id:** flag-003
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** tensometer.md and tensometer-s01e03.md are confirmed identical (both files read; content matches line-for-line). URI-028 carry-forward note is present and accurate. No schema violation. The redundancy itself is structurally sound per the schema's dual-provenance rule (the flat canonical path is retained for current-episode work; the slug-suffixed copy is the archive). Noting for completeness.
- **why:** No downstream risk. Informational only.
- **routing:** n/a

---

### Finding STR-004
- **id:** flag-004
- **type:** fault
- **class:** STRUCTURAL — HARD
- **what:** state-updates.md consolidated citation token mismatch — the URI-CONSOLIDATION-CITE-DRIFT bug manifests in the state-updates layer. Proto-line @96 cites `[state:1]` which in the consolidated file is `1 @7 oc-record-book-market-junction.physical_condition: closed -> open`. The actual state change for @96 (actor:oc-tanner-father.location) is consolidated state:33. Proto-line @125 cites `[state:20] [state:21]` — Taylor's per-slice local IDs 20 (@123 log entry count) and 21 (@125 knowledge.red-keep), but consolidated state:20 = @125 (knowledge.red-keep, correct) and state:21 = @138 (elder-account.physical_condition). The @125 citation `[state:21]` in the proto-line therefore points to an @138 entry when read via consolidated IDs. Proto-line @164 cites `[state:1] [state:27]` which in consolidated IDs are env entry @7 and env entry @165 respectively — neither matches the @164 anchor. The actual @164 entries (maester documentation_status = consolidated state:28; taylor log_entries = consolidated state:62) are uncited.
  - This is the same pre-existing pipeline bug as URI-CONSOLIDATION-CITE-DRIFT (confirmed also in the feeling layer). The issue is systemic across per-character state-update slice entries.
  - Severity note: unlike the feeling mismatch, the state-updates mismatch is partially masked because the env slice's IDs 1-27 are also the consolidated IDs 1-27. Only the per-character slice entries (IDs 28-62 in consolidated) are affected. Proto-line citations to those entries use per-slice local IDs that collide with env-slice IDs.
- **why:** Stitcher resolving state-update citations from proto-lines will pull env entries instead of per-character entries (and vice versa in some cases). The state write-back at phase boundary will apply incorrect field mutations to state files.
- **criteria:** Per-character slice citation tokens in proto-lines must resolve to consolidated state-updates.md IDs. Requires systematic re-tokenization of all per-character state-update citations in proto-lines/s01e03.md to use consolidated IDs, followed by cite-index rebuild.
- **routing:** fixer (proto-lines token correction) + cite-index rebuild — same operation class as STR-001

---

## Class 2 — FREQUENCY-BAND

### Finding FB-001
- **id:** flag-005
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** tensometer.md 3s frequency at 4.5% (7/155). Standard band floor is 5%. Exemption 5 (Tone-law-licensed slow-burn) is claimed.
  - Exemption verification against rubric-tensometer.md §"Exemption 5":
  - (a) CONFIRMED: cond-series-tone-constraints-125ac is in showrunner-memory.series.behaviors. Card §"The Primary Register: Contemplative-Procedural-Horror" declares slow-burn / low-rupture-density register.
  - (b) CONFIRMED: card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" quantifies "3s: 4.5-10% season-average, 4.0-10% per-episode."
  - (c) CONFIRMED: 4.5% ≥ relaxed per-episode floor 4.0%. (c.i) Named scenes all carry peaks: Scene 330-342 (@11, tens=3), Scene 361-375 (@42, tens=3), Scene 477-494 (@162, tens=3); structural climax @139. (c.ii) Scalar inflation refused per AP4 (cycle-2 downgrades @8 and @40 documented in footer).
  - (d) Season-wide scope: s01e01 and s01e02 file matching Exemption 5 claims per showrunner memory.
  - **Exemption verdict: CONFIRMED as EXEMPT-TONE-LAW-SLOW-BURN.** Not a HARD finding.
  - Note: s01e03 per-episode 3s = 4.5% is at the relaxed season-average floor. Season average 3s across s01 (per footer): 21/464 ≈ 4.5%, also at the floor. Any further 3s attrition in subsequent episodes would breach the 4.5% season-average criterion and invalidate the exemption retroactively.
- **why:** Carry-forward advisory: the season-average is at the relaxed floor exactly. No margin for future attrition.
- **routing:** dramatist (advisory)

---

### Finding FB-002
- **id:** flag-006
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** tensometer.md 2s frequency at 30.3% (approximately 47/155). Standard band ceiling is 30%. The exemption claim (Exemption 5) covers only the 3s rung breach; the 2s band is explicitly within standard range per the exemption footer ("Note: 2s and 1s are within the standard band"). The footer describes 2s as "at upper edge of standard band" — but 30.3% is above the 30% ceiling.
  - The rubric uses "roughly" language ("expect roughly 60-75% 1s, 20-30% 2s, 5-10% 3s"), which admits 0.3% rounding. Auditor treats this as a boundary SIGNAL rather than a HARD breach given the explicit "roughly" qualifier and the 0.3% margin.
- **why:** 2s above ceiling can indicate ambient-escalation inflation. At 0.3% over ceiling with "roughly" qualifier, this is advisory only.
- **routing:** dramatist (advisory at wrap)

---

### Finding FB-003
- **id:** flag-007
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** memory.md fire rate at 6/155 = 3.9%. The task-dispatch FREQUENCY-BAND class specifies memory band as 5-12%. The memory R2 shard states the fire rate is "within 1-5% rubric band" — contradicting the task-dispatch. The actual rate (3.9%) is below the 5% floor stated in the task-dispatch.
  - Note: the internal contradiction between task-dispatch band (5-12%) and the memory rubric's internally claimed band (1-5%) is unresolved. If the authoritative band is 5-12%, this is a below-floor breach. If the authoritative band is 1-5%, this is clean. The task-dispatch numbers take precedence for this audit class.
- **why:** If memory fires below 5% band floor, the licensing layer is under-contributing at anchors where the stitcher could use displacement weight. Also surfaces an inconsistency between the memory rubric and the task-dispatch that should be resolved upstream.
- **routing:** memory author + rubric maintainer (clarify authoritative band for memory facet)

---

### Finding FB-004
- **id:** flag-008
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** interest-narrator.md fire rate at 39/155 = 25.2% (after R2 deletions of IDs 7 and 27; 39 active entries). Task-dispatch NI band ceiling is 25%. At 25.2% the file is 0.2% over the ceiling — at the boundary. This matches the s01e01 NI density reading (25.2% also noted there as editor-call) and was deferred as a designed pattern.
- **why:** NI at or above the 25% ceiling is an advisory signal for momentum risk; the file may register too densely and slow the stitched prose. Not a protocol violation at 0.2% margin.
- **routing:** interest-narrator author (editor advisory)

---

### Finding FB-005
- **id:** flag-009
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** feeling.md: Taylor's per-character fire rate is 3/155 = 1.9%, nominally below the 2% per-character floor specified in the task-dispatch (2-5%/char). The shortfall is 0.1% (one entry at a 155-proto-line denominator). The same pattern was flagged in s01e01 audit as an editor-call on non-POV feeling sparsity.
- **why:** At 0.1% below floor with a 155-line denominator the shortfall is within rounding. Editor-advisory.
- **routing:** feeling author — taylor slice (advisory)

---

## Class 3 — METADATA-INCONSISTENCY

### Finding META-001
- **id:** flag-010
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** tensometer.md URI-028 carry-forward note states "Total active tens entries post-prune: ~153" but the frequency-band footer counts "Total entries: ~155" and the cite-index records 155 tens entries. The "~153" figure predates the final prune count. Minor discrepancy in internal documentation; the cite-index figure (155) is authoritative as the post-build count.
- **why:** Documentation inconsistency could cause confusion during future reprocessing. The "~153" note in the carry-forward section should read "155."
- **routing:** tensometer author (documentation fix)

---

### Finding META-002
- **id:** flag-011
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** state-updates.md consolidated file header contains a second raw YAML frontmatter block mid-file (the oc-broken-maester source section begins with `facet: state-updates / episode: s01e03 / target-scope: ...` as a YAML block without `---` delimiters as its start, producing a second frontmatter-style block after the canonical top-of-file frontmatter). Per URI-040 convention (plain-comment slice headers; consolidator owns the canonical frontmatter), this secondary YAML block is non-compliant — it should be a plain-comment header `# source: oc-broken-maester` only. Same issue appears in the oc-tanner-elder and oc-tanner-father source sections.
- **why:** YAML parsers encountering multiple frontmatter-style blocks may fail or misparse. The URI-040 fix was applied to s01e01/02 but the s01e03 per-character state-update slices still contain YAML headers in their source sections.
- **routing:** state-updates author / consolidator

---

## Class 4 — CURVE-SHAPE

### Finding CURVE-001
- **id:** flag-012
- **type:** flag
- **class:** CURVE-SHAPE — SIGNAL
- **what:** Two 1→3 direct jumps without a bridging 2 at the immediately-preceding beat.
  - @10(r=1) → @11(r=3): "taylor-hebert-flea-bottom writes the entry" / "the clerk crosses the Fish Gate." The 2-ramp is at @7/@8 (two beats before the 3, with @9/@10 falling back to 1). The rubric says "beats leading into a 3 should ramp through 2s" — the ramp is present 2-3 beats earlier but the two immediately preceding beats are 1s.
  - @161(r=1) → @162(r=3): "taylor-hebert-flea-bottom enters loc-flea-bottom-base" / "taylor-hebert-flea-bottom faces the wall." The preceding walk sequence runs @159=2, @160=1, @161=1, @162=3. The single 2 at @159 is 3 beats before the 3. The entry-beat @161 and the walk-beat @160 are both 1s immediately before the denouement peak.
  - Both cases have axis justifications in the tensometer (Fish Gate: stakes-visibility + reversal-proximity; wall-facing: reversal-proximity + body-charge), and both were added in cycle-3 F7-bone rescue as explicit rupture additions. The sudden-turn read is structurally defensible but per rubric they are flagged.
- **why:** 1→3 direct jumps without a 2 bridge are either misratings or true sudden turns; both require documentation and may cause stitcher misread (no escalation signal before the rupture). Not a hard fail given the documented axis justifications, but the scene structure may read as jarring in stitch.
- **routing:** dramatist (advisory — consider whether a bridging 2 is warranted at @10 or @161 if the scene reads flat before rupture)

---

## Class 5 — CONTRADICTION

No cross-facet contradictions found. State-update chains are internally consistent within each source. The log open/close sequence for oc-taylor-log is: closed→open (@14), open→closed (@16), closed→open (@29), open→closed (@31), closed→open (@69), open→closed (@71), closed→open (@92), open→closed (@94), closed→open (@163), open→closed (@165). Each close follows an open; no double-open or double-close. Maester pen: writing→set (@90); no subsequent reset. Elder account: blank→written (@138), unsealed→sealed (@139), elder→middleman (@140). Clean cascade.

One note: state-update env entry 19 fires at @90 (`oc-maester-pen.physical_condition: writing -> set`) but the source `<old>` value ("writing") assumes the pen was already in "writing" state at episode open. No prior episode state file was checked for the maester-pen's initial condition (this is a newly introduced OC prop). The field-extension protocol documents this as a first-touch this episode; the initial-state assumption is auditor-untestable without a prior-episode write-back record for this prop. No finding; noted.

---

## Class 6 — DEDUP

No within-facet same-anchor duplicates found. The double-3 at @67/@68 in tensometer is the intentional double-tap device (two parties committing the same turn), documented with explicit axis justifications. The two loc-state entries at @10 and @12 are for different proto-line anchors (consecutive but distinct). No dedup violations found.

---

## Class 7 — SUPERFLUOUS

### Finding SUP-001
- **id:** flag-013
- **type:** flag
- **class:** SUPERFLUOUS — SIGNAL
- **what:** vibes:2 @15 anchors at a tens=1 beat ("taylor-hebert-flea-bottom writes the entry") with no proto-line co-citation in the cite-index (the cite-index shows vibes:2 back=Y but no co-citations in the proto-line's bracket; vibes:2 is cited in proto-line @15 per the proto-lines file `[vibes:2]`). Per convention, tens=1 vibes are never superfluous. However, vibes:2 fires at @15 (the episode's first log entry, one beat after the @11 3-peak where the clerk exits Fish Gate). The licensed-by tokens reference `state-update-taylor-hebert-flea-bottom:2` (per-slice local ID 2 = @11 knowledge.first-clerk-record → file-crossed-fish-gate-beyond-range) and `state-update-taylor-hebert-flea-bottom:1` (per-slice local ID 1 = @8 knowledge.first-clerk-record → recorded-at-elder) — both @11 and @8 entries, not the @15 anchor. The vibes entry fires one beat after its licensed-by state events. This is a forward-anchor fire (the vibe is licensed by events at @8/@11 but placed at @15). Per schema, vibes `licensed-by:` must be machine-resolvable and the source is `state-update:<id>` — these per-slice IDs are the CONSOLIDATION-CITE-DRIFT issue again. The vibe placement itself is defensible (one log entry after the event), but the cross-anchor licensed-by is a schema concern.
- **why:** The forward-anchor vibe placement is borderline per rubric (vibes licensed by on-screen beats require the optional `@<proto-line-id>` anchor; vibes:2 does carry `@15` as its anchor, which is post-event). The schema allows `[@proto-line-id]` to be omitted for off-screen context. At @15 this vibe fires on a beat where the licensed-by state events happened at @8/@11 — the event is on-screen (earlier in same episode), so the anchor should ideally be at the event beat. Advisory, not hard.
- **routing:** vibes author (advisory)

---

## Class 8 — CONSTRAINT

### Finding CON-001
- **id:** flag-014
- **type:** fault
- **class:** CONSTRAINT — HARD — vibes licensed-by non-canonical token forms
- **what:** Multiple vibes entries use `licensed-by:` source tokens in non-canonical form:
  - `state-update-oc-tanner-elder:1` (should be `state-update:<consolidated-id>` per schema)
  - `state-update-taylor-hebert-flea-bottom:N` (per-slice local IDs; should be consolidated IDs)
  - `feeling-oc-tanner-elder:1` (vibes:12; should be `feeling:<consolidated-id>` — which is `feeling:2` for the elder's @6 entry)
  - The schema §"vibes updates" specifies `<source>` as one of: `state-update:<id>` | `memory:<id>` | `feeling:<id>` | `proto:<id>` | `tens:<reading>` | `canon:<gloss>` | `world-build:<gloss>`. None of these forms include per-slice-prefixed variants. The token `state-update-oc-tanner-elder:1` is not a valid schema source token because it uses a per-slice prefix ("state-update-oc-tanner-elder") rather than the canonical `state-update` prefix. Similarly `feeling-oc-tanner-elder:1` uses a per-source prefix that is not in the schema-defined source token vocabulary.
  - This is a systemic issue across all vibes entries that reference state-update or feeling sources. Specific entries affected: vibes:1, vibes:2, vibes:3, vibes:4, vibes:5, vibes:6, vibes:7, vibes:8, vibes:9, vibes:10, vibes:11, vibes:12, vibes:13, vibes:14, vibes:15, vibes:16, vibes:17, vibes:18, vibes:19, vibes:20, vibes:21, vibes:22, vibes:23, vibes:24, vibes:25, vibes:26, vibes:27, vibes:28, vibes:29, vibes:30, vibes:31, vibes:32, vibes:33, vibes:34.
  - The cite-index records vibes `lic-out:` in the same non-canonical form, confirming the token pattern was used throughout.
- **why:** Schema requires `licensed-by:` to be machine-resolvable. Non-canonical token forms break the machine-resolution path for any tooling that resolves `state-update:<N>` by looking up consolidated ID N. The cite-index builder is likely treating these as opaque strings rather than resolvable IDs, meaning the DAG validation cannot verify that the cited sources exist.
- **criteria:** All vibes `licensed-by:` source tokens that use `state-update-<slug>:N` or `feeling-<slug>:N` forms must be rewritten to canonical consolidated-ID forms (`state-update:<consolidated-N>`, `feeling:<consolidated-N>`). The mapping from per-slice local IDs to consolidated IDs is derivable from state-updates.md and feeling.md in order.
- **routing:** vibes author

---

### Finding CON-002
- **id:** flag-015
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — memory monument-type calibration
- **what:** All six memory entries (mem:4, mem:7, mem:8, mem:10, mem:11, mem:12) pass the monument-type calibration check (URI-AUDITOR-MONUMENT-TYPE-CALIBRATION):
  - mem:4 → "the previous-life classification-architecture / register-of-act-without-content" — free-text mechanism gloss. OK.
  - mem:7 → "s01e02:64" — prior proto-line callback. OK.
  - mem:8 → "the Westerosi-monument clamp on the seat-as-future-stage / the keep older than this country's name for what is coming to it" — free-text Westerosi gloss. OK.
  - mem:10 → "the previous-life classification-architecture / file-departing-upstream-from-its-witness" — free-text mechanism gloss. OK.
  - mem:11 → "the previous-life dying-tutor / helpless-protector pattern / tutor-figure whose session terminates" — free-text mechanism gloss. OK.
  - mem:12 → "the previous-life refusal-to-look / enclosed-space-with-the-decision-the-record-will-not-name" — free-text mechanism gloss. OK.
  - No cond-* slugs in target-references. Clean.
- **why:** All pass. Noting for completeness as this was a newly-calibrated class from s01e02 cycle-3 finding.
- **routing:** n/a (clean)

---

### Finding CON-003
- **id:** flag-016
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — Earth-Bet hard-fence scan (URI-AUDITOR-CONSTRAINT-CALIBRATION)
- **what:** Case-insensitive substring scan across all text fields of all facet entries — NI free-text rationale, memory target-reference glosses (parenthetical and slug components), metaphor licensed-by notes and figure text, vibes entity-target-primary fields and token-bundles, feeling somatic-tell text, state-updates field names and old/new values, sensory disambiguation notes, loc-state composite-state and observable-affordance fields. Scanned for: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea.
  - Result: ZERO HITS across all facet entry content fields. All nine facets clean.
  - Note: R2 decision internal prose uses the term "Earth-Bet" and "base card §Memory monuments / Earth-Bet" as category labels. These appear in the .r2-decisions.md decision commentary, not in facet entry text fields. The scan does not cover R2 decision prose (which is process record, not facet content). No violation.
- **why:** Clean. Noting for completeness per the calibration URIs that established this as a per-episode required scan.
- **routing:** n/a (clean)

---

## Class 9 — AP-SCAN

### Finding AP-001
- **id:** flag-017
- **type:** flag
- **class:** AP-SCAN — SIGNAL — vibes AP8 sentence-parsability
- **what:** Two vibes token-bundle items parse as complete sentences with subject + finite verb + object, violating the vibes AP8 sentence-parsability test.
  - vibes:1 @11, actor:taylor-hebert-flea-bottom, token: `the-file-carries-the-name-out-the-gate` — "the file carries the name out the gate" = subject (the file) + finite verb (carries) + direct object (the name) + directional phrase. Complete sentence.
  - vibes:8 @162, series, token: `she-does-not-know-what-file-she-is-in` — "she does not know what file she is in" = clear embedded-clause complete sentence. Subject (she) + finite verb (does not know) + object clause (what file she is in).
  - Other tokens reviewed: `debt-acquiring-administrative-mobility`, `record-written-and-departed`, `no-retrieval-window`, `first-external-claim-on-the-body-now-ambulatory`, `multi-species-sweep-established-at-400m`, `the-front-arrived-at-its-structural-wall` — this last one ("the front arrived at its structural wall") also parses as a sentence: subject (the front) + finite verb (arrived) + prepositional phrase. AP8 concern on vibes:7 @125 token `the-front-arrived-at-its-structural-wall`.
- **why:** Sentence-form tokens are forbidden per the vibes schema ("a token is forbidden if it parses as a complete sentence with subject + finite verb + object"). Tokens that parse as sentences risk being read as prose by downstream operators rather than as word-algebra.
- **routing:** vibes author

---

### Finding AP-002
- **id:** flag-018
- **type:** flag
- **class:** AP-SCAN — SIGNAL — tensometer AP1 advisory (ambient escalation check)
- **what:** Two tensometer entries rated 2 on speech-beats warrant scrutiny under AP2 (speech-beat default):
  - tens:48 @51 r=2 (`oc-tanner-elder speaks to taylor-hebert-flea-bottom`). The proto-line is a bare speech act with no stated content modifier. Per AP2, speaking-to is by default 1 unless something else lights. At @51 the elder is approaching Taylor; the surrounding cluster runs @50=2, @51=2, @52=1, @53=1, @54=2 — the approaching-and-speaking sequence with @50=2 (approach) and @51=2 (speech). The 2 on the speech beat may be climax-bleed from the @50 approach. The axis justification for @51 would need to name what's charged on the speech beat face.
  - tens:97 @103 r=2 (`oc-tanner-elder speaks to taylor-hebert-flea-bottom`). Same pattern — bare speech beat rated 2. The cluster @96=1, @97=2, @98=2, @99=1, @100=2, @101=2, @102=2, @103=2 — a dense 2-run following the father-petition scene. The @103 speech is the elder relaying the father's petition to Taylor. The NI at @103 fires ("the formal register repeats and what it carries has changed"). Rated 2 — defensible on stakes-visibility (Taylor now knows the father-petition result through formal-register delivery), but the beat is a speech-relay and the load is more contextual than face-evident.
  - These are SIGNAL-level concerns; the rubric's "roughly" qualifier means small deviations from ideal are advisory. Both are bracketed by other 2-rated beats in their clusters and are not isolated.
- **why:** AP2 speech-beat over-rating could inflate the 2s band; already noted at 30.3% (above ceiling).
- **routing:** dramatist (advisory)

---

## Class 10 — TASTE-FLAG

### Finding TF-001
- **id:** flag-019
- **type:** flag
- **class:** TASTE-FLAG — SIGNAL — over-decoration candidate at @162
- **what:** Proto-line @162 ("taylor-hebert-flea-bottom faces the wall") carries 9 facet co-citations including six vibes entries (vibes:8, vibes:29, vibes:30, vibes:31, vibes:32, vibes:33). The season-close structural justification for density is documented (this is the denouement registration beat, tens=3, the committed season-close). However, six vibes entries at one anchor is the highest vibe-density in the episode and may read as over-engineered at the stitched layer. Vibes are not rendered in prose, so the stitcher won't produce purple prose from them — but the operator bias accumulation at one beat (six distinct keyword injections) may produce an over-saturated register signal for whatever operator generates prose at this anchor.
  - The six vibes are: vibes:8 (series scope, apparatus-blindness), vibes:29 (actor:taylor, body-not-mine), vibes:30 (loc:loc-flea-bottom-base, denouement-commitment-registered), vibes:31 (season scope, season-closed-on-asymmetry), vibes:32 (actor:taylor, clinical-self-erasure deepens), vibes:33 (actor:taylor, faustian-pressure-first-entry). The fan-out across five distinct targets (actor:taylor ×3, loc ×1, season ×1, series ×1) is structurally intentional. Still the highest single-anchor vibe density in the episode.
- **why:** At the audience adversarial gate, audience may flag this anchor as over-decorated even if each vibe is individually justified. Pre-flagging for reviewer awareness.
- **routing:** vibes author + audience adversarial gate

---

## Class 11 — PILE-UP REVIEW

### Pile-up verdicts

Eight pile-ups identified in cite-index (>4 co-located facets):

| anchor | proto-line | count | verdict |
|--------|-----------|-------|---------|
| @162 | taylor faces the wall | 9 | warranted — season-close structural climax, denouement registration, tens=3; all 9 serve distinct structural purposes (memory/NI/state cover interior/log/decision; 6 vibes cover distinct entity-scope vibe-injections); vibe-density flagged as TF-001 |
| @11 | clerk crosses Fish Gate | 7 | warranted — Scene 1 rupture peak; 7 distinct facets (loc, memory, NI, sensory, 2 states, vibes); all serve the record-departure registration |
| @90 | maester sets pen | 7 | warranted — Scene 5 peak; feeling/memory/NI/sensory/state/2×vibes serve distinct interior vs. external-observation vs. actor-state vs. register-shift functions |
| @125 | Taylor faces Red Keep | 7 | warranted — season-ceiling registration; memory/NI carry foreknowledge; 2 states serve knowledge+radius; 3 vibes cover actor/season/ceiling. Note: the state:21 citation anomaly (pointing to wrong consolidated entry per STR-004) may cause a false co-citation |
| @67 | elder places coin | 6 | warranted — coin-transfer peak (tens=3); all 6 cover distinct ground (NI/sensory/2 states/vibes; no duplication) |
| @98 | father speaks to elder | 6 | warranted — village-claim formalization peak; feel:1 citation is erroneous per STR-001 (should not appear here — the father's tell is feel:4, which is also present); the spurious feel:1 citation inflates this pile-up count by 1 |
| @139 | elder seals account | 6 | warranted — structural climax (tens=3 three-axis); NI/sensory/2 states/2 vibes all cover distinct structural surfaces |
| @42 | second clerk releases book | 5 | warranted — Scene 3 rupture peak; NI/state/2×vibes serve distinct functions |

---

## Audit Summary

Total findings: 19 across 7 facets.

**HARD (5):**
- flag-001 (STR-001): feeling citation token mismatch — proto-line citations for feeling entries use per-slice local IDs that resolve to wrong consolidated entries. All but the maester's feel:1 are affected.
- flag-004 (STR-004): state-updates citation token mismatch — per-character state-update slice entries cited with local IDs that collide with env-slice IDs in consolidated file. Known manifestation of URI-CONSOLIDATION-CITE-DRIFT.
- flag-014 (CON-001): vibes `licensed-by:` non-canonical token forms — all 34 vibes entries use per-slice-prefixed `state-update-<slug>:N` and `feeling-<slug>:N` tokens instead of the schema-canonical `state-update:<consolidated-N>` and `feeling:<consolidated-N>` forms.
- (STR-001 and STR-004 together constitute the primary blocking structural issue; both are downstream manifestations of URI-CONSOLIDATION-CITE-DRIFT.)

**SIGNAL (14):**
- flag-002 (STR-002): NI deletion gaps without in-file comments (advisory)
- flag-003 (STR-003): tensometer dual-file identity confirmed (informational)
- flag-005 (FB-001): tens 3s at 4.5% — EXEMPT-TONE-LAW-SLOW-BURN confirmed; season-average at floor, no attrition margin
- flag-006 (FB-002): tens 2s at 30.3%, 0.3% above 30% ceiling (within "roughly" qualifier)
- flag-007 (FB-003): memory fire rate 3.9% vs. task-dispatch 5% floor; rubric band inconsistency also surfaced
- flag-008 (FB-004): NI density at 25.2%, at ceiling (editor advisory)
- flag-009 (FB-005): Taylor feeling fire rate 1.9%, 0.1% below 2% floor (rounding margin; editor advisory)
- flag-010 (META-001): tensometer carry-forward note says ~153 entries vs. actual 155
- flag-011 (META-002): state-updates consolidated file has secondary YAML frontmatter blocks in per-character source sections (should be plain-comment headers per URI-040)
- flag-012 (CURVE-001): two 1→3 direct jumps at @10→@11 and @161→@162 without immediately-preceding 2
- flag-013 (SUP-001): vibes:2 @15 forward-anchor fire licensed by state events at @8/@11 (advisory)
- flag-015 (CON-002): memory monument-type calibration — all six entries PASS (clean note)
- flag-016 (CON-003): Earth-Bet hard-fence scan — ZERO HITS (clean note)
- flag-017 (AP-001): vibes AP8 sentence-parsability — three tokens violate (vibes:1 token `the-file-carries-the-name-out-the-gate`; vibes:7 token `the-front-arrived-at-its-structural-wall`; vibes:8 token `she-does-not-know-what-file-she-is-in`)
- flag-018 (AP-002): tensometer AP2 speech-beat default concerns at @51 and @103
- flag-019 (TF-001): @162 six-vibe pile-up — over-decoration candidate for audience gate

---

## Routing Block

| finding | type | routing |
|---------|------|---------|
| flag-001 (STR-001) | HARD | fixer → proto-lines/s01e03.md feeling citation token correction + cite-index rebuild |
| flag-002 (STR-002) | SIGNAL | interest-narrator author (advisory) |
| flag-003 (STR-003) | SIGNAL | n/a |
| flag-004 (STR-004) | HARD | fixer → proto-lines/s01e03.md state-update citation token correction + cite-index rebuild |
| flag-005 (FB-001) | SIGNAL | dramatist (advisory — season-avg at exemption floor) |
| flag-006 (FB-002) | SIGNAL | dramatist (advisory at wrap) |
| flag-007 (FB-003) | SIGNAL | memory author + rubric maintainer (band clarification) |
| flag-008 (FB-004) | SIGNAL | interest-narrator author (editor advisory) |
| flag-009 (FB-005) | SIGNAL | feeling author — taylor slice (advisory) |
| flag-010 (META-001) | SIGNAL | tensometer author (documentation fix) |
| flag-011 (META-002) | SIGNAL | state-updates consolidator (YAML→comment headers) |
| flag-012 (CURVE-001) | SIGNAL | dramatist (advisory — consider bridging 2 at @10 or @161) |
| flag-013 (SUP-001) | SIGNAL | vibes author (advisory) |
| flag-014 (CON-001) | HARD | vibes author → rewrite all licensed-by state-update + feeling source tokens to canonical consolidated IDs |
| flag-015 (CON-002) | SIGNAL | n/a (clean) |
| flag-016 (CON-003) | SIGNAL | n/a (clean) |
| flag-017 (AP-001) | SIGNAL | vibes author |
| flag-018 (AP-002) | SIGNAL | dramatist (advisory) |
| flag-019 (TF-001) | SIGNAL | vibes author + audience adversarial gate |

---

## Process notes for next session

1. The HARD findings flag-001, flag-004, and flag-014 share a common root cause: the consolidation of per-character slice files into the canonical feeling.md, state-updates.md, and vibes.md produces global IDs, but proto-line citation tokens and vibes licensed-by tokens were authored using per-slice local IDs. This is the URI-CONSOLIDATION-CITE-DRIFT bug (documented in s01e02 process_gaps as a pre-existing structural pipeline bug). The three findings here are the specific episode-scope manifestation that the fixer can address with token rewrites; the upstream pipeline fix (ensuring citation tokens are written using consolidated IDs at authoring time) is a separate URI-level remediation.

2. flag-001 and flag-004 together mean the cite-index as built is partially incorrect for feeling and per-character state-update entries. The cite-index should be rebuilt after any fixer token corrections land.

3. The exemption claim for frequency-band (flag-005, Exemption 5) is confirmed as valid against all four rubric criteria. No reaudit needed on this point unless season-average 3s drops below 4.5%.

4. Clean classes: CONTRADICTION (5), DEDUP (6), Earth-Bet hard-fence (CON-003), monument-type calibration (CON-002). No findings in those classes require fixer dispatch.
