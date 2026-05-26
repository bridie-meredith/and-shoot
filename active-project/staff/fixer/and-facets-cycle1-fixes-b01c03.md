## SESSION-START — 2026-05-26T11:00:00Z — and-facets-phase5-fixes-b01c03
dispatch: Phase 5 fixer pass for /and-facets b01-c03 — 3 HARD findings; fault-001 DELETE exposition:5 @13 (fire-rule clause-b); fault-002 rewrite >=2 NI predicate-nominative entries (50% saturation); fault-003 ADD NI entries at @10, @22, @31 (cross-facet contract gap)
target: active-project/theater/facets/exposition-b01-c03.md + active-project/theater/facets/interest-narrator-b01-c03.md + active-project/theater/facets/_inflight/proto-lines-exposition.md + active-project/theater/facets/_inflight/proto-lines-narrator.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 3

## fault-001 — RESOLVED (PRE-APPLIED VERIFIED) — 2026-05-26T11:10:00Z
fault: exposition:5 @13 scene-open-orient fires when loc-state:2 @13 already covers scene-B orientation — fire-rule clause-b violated
scope: line
change: verified pre-applied: exposition-b01-c03.md line 24 carries deletion marker "# DELETED exposition:5 - @13 - scene-open-orient (Phase 5 fault-001 fire-rule clause-b: loc-state:2 covers the scene-B orientation)"; fire-audit block (lines 36-38) updated with REFUSED rationale and fixer attribution; proto-lines-exposition.md @13 carries only [exposition:4] with no [exposition:5] token; annotation block in proto-lines-exposition.md header notes deletion; no further edit required
criteria met: yes — exposition:5 absent from file; deletion marker in place; fire-audit documents refusal; per-episode counts now 7 entries (0 scene-open-orient); all caps satisfied

## fault-002 — RESOLVED — 2026-05-26T11:15:00Z
fault: 4/8 NI entries predicate-nominative ("X was/is Y") — 50% saturation above 40% threshold
scope: line
change: NI:1 @4 rewritten from "stillness in a market is the cost-tell" to "the cost-tell — stillness against market grain" (paratactic em-dash appositive; no copula); NI:5 @19 rewritten from "the overlap was the price-tag he had not yet read aloud" to "the coverage she already held ran through the wards he had named — the price-tag sat in that overlap unspoken" (two independent clauses; no predicate-nominative); NI:3 @8 and NI:7 @29 retained per audit criteria (scene-A and scene-C peak-bone retention candidates); post-rewrite predicate-nominative count: 2/11 = 18%, below 40% threshold
criteria met: yes — 2 entries rewritten to distinct syntactic constructions; semantic content (cost-tell, price-tag) preserved; no named-feeling vocabulary introduced; no NI anti-patterns introduced

## fault-003 — RESOLVED — 2026-05-26T11:20:00Z
fault: state-updates cross-facet contract gap — NI absent at @10, @22, @31 (three structurally load-bearing anchors)
scope: line
change: NI:9 @10 added ("court layer added: the rescue she had run was already read — Jarvis naming the alley confirmed the tether closed." — 22 words; co-cites state:29 tether-prot-rise-ledger; no pred-nom; paratactic with colon); NI:10 @22 added ("the wards he had named were already in the feed; she was being asked to sell coverage she was running." — 20 words; co-cites state:32 feed-mode→mapping-against-coverage; two independent clauses; no pred-nom); NI:11 @31 added ("same place, first bell — the courier's confirm read as the close; she had engaged before the utterance finished." — 19 words; co-cites state:35 position-with-patron→engaged-interlocutor; paratactic em-dash; no pred-nom); proto-lines-narrator.md updated: [interest-narrator:9] at @10, [interest-narrator:10] at @22, [interest-narrator:11] at @31; density header updated 8/36 (22%) → 11/36 (31%) with NOTE: exceedance over 25% ceiling is a Phase 5b SIGNAL — cross-facet-contract HARD requires the adds; density ceiling does not supersede structural contract gap
criteria met: yes — NI coverage added at all 3 structurally load-bearing anchors; Taylor's cold-utilitarian register; Westerosi-witness vocabulary; no Earth-Bet; all entries ≤25 words; syntax varied (colon-appositive, semicolon-pair, em-dash-paratactic)

## cite-index rebuild — DEFERRED — 2026-05-26T11:20:00Z
note: build_cite_index.py at active-project/staff/cite-index/build_cite_index.py requires Python execution environment; cannot run from fixer file-edit context; rebuild deferred to /and-facets Phase 2 operator invocation; inflight proto-lines files carry correct [interest-narrator:9/10/11] tokens at @10/@22/@31 ready for builder input

## SESSION-END — 2026-05-26T11:20:00Z — and-facets-phase5-fixes-b01c03
findings-applied: 3 (fault-001 verified pre-applied; fault-002 2 NI rewrites; fault-003 3 NI adds + proto-lines citations)
findings-skipped: 0
exit: CLEAN
