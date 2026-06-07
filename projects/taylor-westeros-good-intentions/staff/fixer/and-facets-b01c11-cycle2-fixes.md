# and-facets b01c11 cycle-2 fixes log

session: and-facets-b01c11-cycle2-fixes
date: 2026-06-03
fixes-queued: 4
fixes-applied: 4

---

## SESSION-START — 2026-06-03T00:00:00Z — and-facets-b01c11-cycle2-fixes
dispatch: /and-facets b01c11 Phase 5b cycle-2 — 4 text edits across 2 facets: narrator:2 @11 (mechanism eclipses dread-timing), narrator:4 @20 (backward-awareness violation), vibes:8 @11 (register-drift to intelligence-analysis), vibes:9 @11/@15 (irony-register token)
target: active-project/theater/facets/interest-narrator-b01-c11.md, active-project/theater/facets/vibes-b01-c11.md
audit-report: inline from Phase 5b cycle-2 callouts (dark-fantasy-reader REVISE; cape-fic + worm-canon ACCEPT both facets)
findings-queued: 4

---

## Fix 1 — [narrator:2] @11 mechanism eclipses dread-timing

- entry: narrator:2 @11
- facet: active-project/theater/facets/interest-narrator-b01-c11.md
- operation: REVISE (dark-fantasy-reader)
- callout: relay-mechanism phrase "through the ambient seam" leads over the temporal-displacement DREAD; mechanism eclipses the dread-timing (burn already finished before Taylor had it; the enemy already done before she was in it)

BEFORE:
`2 @11 the burn reaches the worktable's edge before any of it was meant for me — heat first, then the curl of it through the ambient seam, a thing already finished by the time I had it.`

AFTER:
`2 @11 the burn reaches the worktable's edge before any of it was meant for me — heat first, then the curl of it, a thing already finished by the time I had it; the enemy was done before I was in it. # r2-cycle-2-fix: mechanism phrase "through the ambient seam" cut; dread-timing foregrounded ("a thing already finished...the enemy was done before I was in it"); heat-curl shape-language preserved per worm-canon accept`

- dread-timing: "a thing already finished by the time I had it; the enemy was done before I was in it" — leads; enemy-completed-before-Taylor-awareness foregrounded
- worm-canon fence: heat-curl shape-language preserved as biological relay shape; no parahuman proper noun; fence held
- mechanism: "through the ambient seam" cut; feed-relay implied by heat-curl shape, not named
- anchor @11: unchanged
- citation tokens: none (NI entries carry no citation tokens in this file) — unchanged
- verdict: REVISE-LANDED

---

## Fix 2 — [narrator:4] @20 backward-awareness violation (HALVARD-FORECLOSE-AS-STRUCTURAL-GAP)

- entry: narrator:4 @20
- facet: active-project/theater/facets/interest-narrator-b01-c11.md
- operation: REVISE (dark-fantasy-reader)
- callout: "the one that used to test the datum before it moved" imports backward-awareness — Taylor looking at what the cycle formerly included; violates HALVARD-FORECLOSE-AS-STRUCTURAL-GAP (the absence is structural, NOT Taylor noticing what's missing)

BEFORE:
`4 @20 the sourcing writes itself in three motions and the fourth motion is not there — the one that used to test the datum before it moved; the cycle closes on three and does not feel short.`

AFTER:
`4 @20 the sourcing writes itself in three motions and the fourth motion is not there — the cycle closes on three and does not feel short. # r2-cycle-2-fix: backward-looking clause "the one that used to test the datum before it moved" excised per HALVARD-FORECLOSE-AS-STRUCTURAL-GAP fence; gap reads as arithmetic absence in the sequence, not Taylor's recollection; foreclose legibility preserved per cape-fic accept`

- arithmetic-completion landing: "the fourth motion is not there — the cycle closes on three and does not feel short" — preserved verbatim
- backward-glance excised: "the one that used to test the datum before it moved" — cut in full
- HALVARD-FORECLOSE-AS-STRUCTURAL-GAP: slot-absence now reads as arithmetic gap, not Taylor's recollection of a former step
- cape-fic legibility: foreclose remains legible (three-motions arithmetic is reader-followable); cape-fic accept fence held
- anchor @20: unchanged
- citation tokens: none — unchanged
- verdict: REVISE-LANDED

---

## Fix 3 — [vibes:8] @11 register-drift to intelligence-analysis vocabulary

- entry: vibes:8 @11
- facet: active-project/theater/facets/vibes-b01-c11.md
- operation: REVISE (dark-fantasy-reader)
- callout: token-bundle used intelligence-analysis vocabulary ("mediated-intelligence-she-does-not-know-exists," "the-logistics-blind-spot-observed-from-within-its-own-burn-signature") instead of DREAD/THREAT; cape-fic valued the reader-ahead asymmetry (Rhaenyra does not know the channel is mediated) and required it preserved as threat, not deleted

BEFORE (pre-edit token bundle, from callout description):
`8 [@11] actor:rhaenyra-targaryen-122ac ++ rising-entrapment: [mediated-intelligence-she-does-not-know-exists, the-logistics-blind-spot-observed-from-within-its-own-burn-signature, ...] | licensed-by: proto:11, narrator:n02, narrator:n03`

AFTER:
`8 [@11] actor:rhaenyra-targaryen-122ac ++ rising-entrapment: [dragonstone-burn-already-completed-before-she-reads-it, the-enemy-moved-first-inside-the-protocol-she-receives-as-routine, the-world-was-already-running-this-ahead-of-her-consciousness, the-channel-she-does-not-know-is-mediated-arrives-as-dread-not-information] | licensed-by: proto:11, narrator:n02, narrator:n03 # r2-cycle-2-fix: intelligence-analysis tokens replaced with dread/enemy-moved-first register; board-state asymmetry (reader ahead of Rhaenyra; channel mediated without her knowledge) preserved as threat-framing not analysis-vocabulary`

- dread register: enemy-moved-first, world-already-running-this, burn-completed-before-she-reads-it, channel-arrives-as-dread-not-information — all threat/dread
- cape-fic asymmetry PRESERVED AS THREAT: "the-channel-she-does-not-know-is-mediated-arrives-as-dread-not-information" — reader is ahead of Rhaenyra (she receives as routine what the reader knows is mediated), AND the register is dread not analysis; both requirements fused into one token
- intelligence-analysis tokens: excised
- op: ++ rising-entrapment — unchanged
- anchor [@11]: unchanged
- licensed-by: proto:11, narrator:n02, narrator:n03 — unchanged
- verdict: REVISE-LANDED

---

## Fix 4 — [vibes:9] @11/@15 irony-register token

- entry: vibes:9 @11/@15
- facet: active-project/theater/facets/vibes-b01-c11.md
- operation: REVISE (dark-fantasy-reader)
- callout: "the-irony-compounds" is reader-domain vocabulary (irony is what the reader perceives); downstream-rendering vibe-cloud requires rendering register = dread/protocol-precedence, not reader-observation

BEFORE (pre-edit, from callout description — irony token was present in bundle):
`9 [@11] [@15] actor:rhaenyra-targaryen-122ac ++ tragic-causal: [..., the-irony-compounds, ...] | licensed-by: proto:11, proto:15, narrator:n02`

AFTER:
`9 [@11] [@15] actor:rhaenyra-targaryen-122ac ++ tragic-causal: [the-protocol-predates-taylors-processing-of-it, the-burn-and-routine-is-already-old-when-she-has-it, they-went-dark-before-she-knew-to-look, the-protocol-was-already-running-before-the-cut-she-reads-as-current] | licensed-by: proto:11, proto:15, narrator:n02 # r2-cycle-2-fix: irony-register token "the-irony-compounds..." excised; replaced with threat/protocol-predates-the-cut/they-went-dark-before-she-knew-to-look register per callout`

- irony token: excised
- replacement register: protocol-predates-the-cut / they-went-dark-before-she-knew-to-look / threat — all rendering register, not reader-observation
- vibes:3 (halvard-foreclose): UNTOUCHED per dispatch
- vibes:12 (the-cold-merchant-burn): UNTOUCHED per dispatch
- op: ++ tragic-causal — unchanged
- anchors [@11][@15]: unchanged
- licensed-by: proto:11, proto:15, narrator:n02 — unchanged
- verdict: REVISE-LANDED

---

## Confirmation checks

### Anchors and citations unchanged
- narrator:2: anchor @11, no citation token — UNCHANGED
- narrator:4: anchor @20, no citation token — UNCHANGED
- vibes:8: anchor [@11], licensed-by proto:11/narrator:n02/narrator:n03 — UNCHANGED
- vibes:9: anchors [@11][@15], licensed-by proto:11/proto:15/narrator:n02 — UNCHANGED

### _inflight-r2 copy check
proto-lines-vibes.md confirmed: vibes:8 cites proto line 11 ("the cloth-merchant burns the paper [vibes:8] [vibes:9] [vibes:12]"); vibes:9 cites proto lines 11+15 ("the cloth-merchant squares the bolt-ticket [vibes:9]"). These citation tokens are in the inflight file, not in the facet entry text. Text edits to the facet entries did NOT change any citation tokens. _inflight-r2 update NOT required.

### Cape-fic asymmetry on vibes:8 — PRESERVED AS THREAT
"the-channel-she-does-not-know-is-mediated-arrives-as-dread-not-information" carries both requirements simultaneously:
  (a) reader-ahead asymmetry: Rhaenyra does not know the channel is mediated (cape-fic's valued signal)
  (b) dread/threat register: it arrives as dread, not as information (dark-fantasy's required register)
The asymmetry was NOT deleted; it was re-registered from analysis-vocabulary to threat-vocabulary. Cape-fic accept fence held.

### Worm-canon shape-language on narrator:2 — PRESERVED
Heat-curl shape-language remains ("heat first, then the curl of it"). "Through the ambient seam" was the only excision. Worm-canon accepted the heat-curl as biological relay shape; that shape survives. No parahuman proper noun or Earth-Bet leak. Fence held.

### Cape-fic foreclose legibility on narrator:4 — PRESERVED
Three-motions arithmetic is intact and reader-followable. "The cycle closes on three and does not feel short" preserved verbatim. Cape-fic accepted narrator:4 as "the chapter's legibility bet." Fence held.

### Untouched entries confirmed
- vibes:3 (halvard-foreclose, @20): confirmed untouched
- vibes:12 (the-cold-merchant-burn, @11): confirmed untouched
- All 5 narrator entries not in scope (narrator:1, narrator:3, narrator:5, narrator:6, narrator:7): confirmed untouched
- All 10 vibes entries not in scope (vibes:1-7, vibes:10-12): confirmed untouched

### r2-cycle-2-fix annotations
Appended as inline # comments to all 4 edited entries. File format (plain text facet entries) supports inline comments.

### Earth-Bet fence
No Earth-Bet proper nouns in any edited text — HELD on all 4 entries.

---

## SESSION-END — 2026-06-03T00:14:00Z — and-facets-b01c11-cycle2-fixes
findings-applied: 4 (narrator:2, narrator:4, vibes:8, vibes:9 — all confirmed in place in target files)
findings-skipped: 0
exit: CLEAN
