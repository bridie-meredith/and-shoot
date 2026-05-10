---
phase: E — defense or revision
date: 2026-05-10
run: and-season-tuning-r1
locked-rubric: design/shoot-v2/and-season-tuning-r1/rubric-and-season.md
input: C-seams.md
---

# Phase E — Defense or Revision

## Decision summary

- DEFEND: 4 units (U1, U2, U5, U15)
- REVISE: 12 units (U3, U4, U6, U7, U8, U9, U10, U11, U12, U13, U14, U16)
- WITHDRAW: 0 units
- DEFEND-with-carry-back: 1 unit (U17, subset of DEFEND)
- Cross-unit dependencies noted: U9/U14 linked (revising U14 to 370 partially resolves U9 by making the surveillance state the cut image rather than absent across the downstream boundary); U13 (e02→e03 at 207) cascades into e02 and e03 aggregate_range headers; U12 (e01→e02 at 131) cascades into e01 aggregate_range header.

---

## Per-unit decisions

### U1 — Season escalation curve
- decision: DEFEND
- citation: S2 — "Season-level rise-peak-fall: stretch peaks escalate cumulatively per the season escalation spine"; season-s01-plan.md §D (season drama: "four years of cost paid before a stranger in maester's robes arrives"); series-plan.md §6 cond-series-tone-constraints-84ac ("prohibits catharsis before the Dance")
- The seam argues that the post-IGNITION arc (474–912) is managed bureaucratic descent rather than escalation, but the season plan names this arc as the "long cost" structure: the descent is the season's dramaturgical intent, not a failure of the escalation curve. The S2 rubric identifies climax (419–519, peak 455–474) and denouement (520–912) as the authorized structure; the terminal cost-escalation mechanic for S1 is the surveillance apparatus tier-crossing, not a second kinetic event. The rubric's S2 "stretch peaks escalate cumulatively" applies to buildup, not to denouement; cond-series-tone-constraints-84ac explicitly prohibits a cathartic second peak. The seam mistakes the season's tone-law-mandated shape for a structural failure.
- (carry-back note: the rubric does not define what denouement share is too large; the 44% finding is real and the rubric has no answer for it; see U17 carry-back)

---

### U2 — s01e01 dramatic shape
- decision: DEFEND
- citation: Phase 4 Step 2 — OPEN-ENGAGES; S3 — entertainment window threshold; season-s01-plan.md §D early-baseline beat; Gap 1 (B-baseline)
- The OPEN-ENGAGES verdict in Phase 4 Step 2 tests whether "the open of the episode hooks; reader would read on," not whether a board-change has already occurred. The e01 open (lines 1–14: insects, floor, ecology, ledger) is the season plan's mandatory early-baseline register: the passive swarm-sense running continuously is the hook — it establishes the uncanny in the mundane, which is the series' tonal register. The S9 COMPREHENSIBILITY-RISK-attention flagged in the baseline is a pre-existing carry-forward that was not adjudicated as a blocking fault by the Phase 3 convergence call; it is not a new seam but a known residual. The episode's one board-change at episode line 99 is the intended season-plan shape for a baseline-establishing episode (season-plan §D: "what cannot remain unchanged: one thing in the household is different at beat-close from beat-open"). The OPEN-ENGAGES test is passed by the ecological uncanny, not by early board-change density.

---

### U3 — s01e02 dramatic shape
- decision: REVISE
- citation: Phase 4 Step 2 — CLOSE-EARNS-NEXT; SHAPE-COHERENT; Gap 1 (B-baseline); S2 — peak placement within episode arc
- The seam is load-bearing. Two personas converge (pulp-enthusiast STRONG, worm-canon-pedant STRONG) on the same specific candidate: the volume-handoff at aggregate 207/208 (episode line 58/59: taylor takes the volume / taylor grips the volume) is the episode's state-change beat and the strongest available close image, but the current cut at aggregate 250 (episode line 103) is 43 lines of aftermath later on column-tracing. CLOSE-EARNS-NEXT fails: the episode's payoff — Taylor now holds a pastoral-claim resource and is formally in Rowan's literacy record — is buried in the interior, not the close. The dark-fantasy-reader's alternative (basin fly at 247/episode 98) is weaker than pulp+worm's convergent pick at 207; the two-persona convergence on 207 carries more weight under the rubric's ≥2-persona threshold logic.
- What changes: move e02/e03 cut from aggregate 250 to aggregate 207. New e02 aggregate_range: 150–207 (58 lines, below the 80-line floor). New e03 aggregate_range: 208–418 (211 lines, well above the 160 ceiling).
- Who owns: dramatist (shape/split re-proposal; the new e02 at 58 lines violates Phase 4 Step 1(a) lower bound of 80 lines; dramatist must propose a compliant alternative — either move the cut to a point that produces an episode at or above 80 lines while still closing on a stronger image than 250, or propose a different e02/e03 split strategy).
- How it answers the seam: a cut at or near 207 makes the pastoral-claim board-change the close image, satisfying CLOSE-EARNS-NEXT; SHAPE-COHERENT is improved because the episode's interior rise leads to the close rather than being buried mid-episode.
- Cascade: e02 aggregate_range header changes (150–207 or adjusted near-207 value); e03 aggregate_range header changes (208–418 or adjusted value); e03's interior shape now begins on the aftermath of Rowan's literacy claim, which is a different scene-entry than the current 251 (market square). The e02→e03 continuity seam (U8) shifts accordingly — the new e03 open is the sept sequence continuation, not the market square entrance; this may resolve U8 by giving a more natural aftermath-to-next-scene bridge. Flag as boundary-rebalance subtask for dramatist.

---

### U4 — s01e03 dramatic shape
- decision: REVISE
- citation: Phase 4 Step 2 — CLOSE-EARNS-NEXT; S2 — forward-flag honor; Gap 3 (B-baseline)
- The seam is load-bearing and convergent (dark-fantasy STRONG, pulp MODERATE/STRONG, worm STRONG all identify Rymer's surveillance as the wrong internal position). The current close at 417–418 (oc-lords-steward mounts, taylor holds the feet) disperses tension through 48 lines of fishwife dispute and literacy folio exchange after the episode's most dangerous moment (Rymer holding/facing Taylor at 369–370/412). The season plan's census-paperwork-pull beat names "Rymer files Taylor watching" as the beat's key state-change, and the rubric's S2 forward-flag honor requires this commitment to be visible as closing pressure. However, the preferred cut point depends on U14's placement decision (see below; they are linked).
- What changes: revise close of e03 to end at or near the Rymer surveillance moment (aggregate 370 or 412). Pending U14's precise recommendation from dramatist, the provisional target is aggregate 370 (rymer-hedge faces taylor-hebert-jaehaerys). New e03 aggregate_range: 251–370 (120 lines, mid-band). New e04 aggregate_range: 371–563 (193 lines, over 160 ceiling — requires boundary-rebalance subtask, see U14).
- Who owns: dramatist (shape/split re-proposal; 193-line e04 exceeds band; dramatist must determine whether to push e04 end-point forward or pull e03 end-point back to produce a compliant e04, while preserving the surveillance-close image).
- How it answers the seam: closing on rymer-hedge faces taylor-hebert-jaehaerys (aggregate 370) makes the surveillance-vector the episode's final image, satisfying CLOSE-EARNS-NEXT and honoring S2 forward-flag for the census beat.
- Cascade: e03 aggregate_range header changes; e04 aggregate_range header changes; e04 is now over-band — escalate as boundary-rebalance subtask to dramatist; U9 (e03→e04 continuity) is linked — see cross-unit dependency note.

---

### U5 — s01e04 dramatic shape
- decision: DEFEND
- citation: Phase 4 Step 2 — CLOSE-EARNS-NEXT; S8a — character-action plausibility; cond-fauna-control-rules; season-s01-plan.md §H
- The seam has two components. On the cost-timing issue (worm): the aggregate at episode line 73 (aggregate line 491: taylor presses the temple) fires after the swarm contracts at line 56 (aggregate 474). Reading the episode bones directly: the swarm contracts at episode line 56, oc-craftsman-father draws Taylor away at 58–59, the swarm releases at episode line 60. Taylor presses the temple at episode line 73. The season plan §H states "the child-body ceiling applies throughout S1 — ten minutes active control → headache; twenty → nosebleed; thirty → blackout." The IGNITION event is involuntary (Taylor did not activate it deliberately); the cost is a headache after the swarm releases, not concurrent with involuntary discharge. Cond-fauna-control-rules' concurrent-cost clause applies to deliberate active control; involuntary swarm-discharge does not have a concurrent-cost requirement under the condition card. The retrospective temple-press is consistent with the involuntary nature of the event. On the CLOSE-EARNS-NEXT issue (pulp): "taylor follows mira" (episode line 148, aggregate 563) is a hard forward-momentum hook. The rubric's Phase 4 Step 2 CLOSE-EARNS-NEXT criterion is "the close lands on a beat that earns the next episode's open" — taylor follows mira earns e05's Mira-POV open directly. The 89-bone post-IGNITION section is the mandatory aftermath of the season's most expensive beat; compressing it would violate the "long cost" structure the season plan names. The seam misidentifies aftermath as flatline.

---

### U6 — s01e06 dramatic shape
- decision: REVISE
- citation: S8a — IMPLAUSIBLE-CHARACTER-oc-craftsman-mother carry-forward (B-baseline); Phase 4 Step 2 — OPEN-ENGAGES; S6 — VIBE-DRIFT-procedural-recurrence (carry-forward); season-s01-plan.md §E+H (interlude rendering constraint)
- The seam is load-bearing. Two personas converge (dark-fantasy STRONG, worm STRONG) on the same bone-level absence: the Elara interlude fails its season-plan rendering constraint ("render failure-mode cost in what Elara does not understand, not what she resolves") because the bones (reeve visit sequence, lines 740–747/41–48 in episode) give only a competent action sequence with no signal of epistemic limit. This is also the S8a IMPLAUSIBLE-CHARACTER-oc-craftsman-mother carry-forward from the B-baseline, which was never resolved. The 100-bone Elara open before the maester (episode 3–102) contributes to OPEN-ENGAGES failure for the reader who expects the season-close episode to begin its institutional reckoning.
- What changes: revise Elara interlude bones in the aggregate range 702–801 / episode lines 3–102 to register epistemic-limit cost rather than only competent action — specifically, at least one bone in the reeve-visit and/or Rowan-visit sequence should distinguish "Elara does not understand what she is asking for" from "Elara acts effectively." This is not a structural cut revision; it is a bone-level prose register fix in existing bones.
- Who owns: screen-writer (SVO-level prose work on existing Elara interlude bones, specifically lines 702–750 aggregate / episode lines 3–48; regenerate 3–6 bones at the Rowan-conversation close and reeve-visit to carry cost-register rather than only action-register).
- How it answers the seam: satisfies S8a IMPLAUSIBLE-CHARACTER-oc-craftsman-mother by making the rendering constraint visible at bone level; partially addresses S6 VIBE-DRIFT-procedural-recurrence by differentiating this sequence from a generic parent-takes-action sequence.
- Cascade: no cut-point changes; aggregate_range headers unchanged. The S8a carry-forward is resolved if the revised bones pass a re-check.

---

### U7 — e01→e02 continuity
- decision: REVISE
- citation: Gap 2 (B-baseline) — no cross-episode continuity check; S4 — state continuity
- The seam is load-bearing. Two personas converge (worm MODERATE, dark-fantasy MODERATE) on the same absent bridge: the apprentice mark (e01's only hard board-change) creates a formal documentary record of Taylor but e02 opens with no bone signaling that this exposure-variable is active in Taylor's operational posture. Gap 2 explicitly names this failure mode: "a reader experiencing the split as one-episode-then-pause-then-next-episode meets a different surface." The cross-episode continuity is not covered by S4 (which covers within-aggregate continuity) — this is a Gap 2 exposure.
- What changes: add 1–2 bones at the e02 open (aggregate region 150–155, episode lines 1–4 region) signaling that Taylor's sept entrance registers the new ledger-record as an active exposure variable — the apprentice mark exists and is now a fact outside the workshop. The bones should be in Taylor's observational/physical register (holds, stills, faces) consistent with the harsh-SVO discipline, not internal monologue.
- Who owns: screen-writer (SVO-level bone addition at e02 open, 1–2 bones).
- How it answers the seam: makes the apprentice-mark state-change propagate visibly across the cut, satisfying the Gap 2 cross-episode continuity standard without requiring a rubric revision.
- Cascade: e02 aggregate_range header start shifts if bones are added before current aggregate 151; more likely these bones replace/supplement existing blank lines (aggregate 150 is blank) — no header cascade if inserted into existing gap IDs.

---

### U8 — e02→e03 continuity
- decision: REVISE
- citation: Gap 2 (B-baseline); S4 — state continuity; S6 — vibe continuity
- Two personas converge (worm MODERATE, pulp MODERATE) on the same missing state-bridge: Rowan's pastoral claim from e02 is not visible as an active constraint at the e03 open. Note: this decision is partially dependent on U3 (REVISE) — if the e02/e03 cut moves to ~207, the e03 open will be the sept aftermath sequence (aggregate ~208 onward), which naturally carries the pastoral-claim state forward in the same scene. If the cut moves to ~207, U8's seam may be resolved structurally without additional bones. The U3 REVISE is the primary fix; U8 routing is conditional.
- What changes: conditional on U3's dramatist resolution. (a) If the e02/e03 cut moves to ~207 (sept scene): U8 is resolved by structural placement — the e03 open inherits the sept context. (b) If the dramatist cannot achieve a compliant cut near 207 and the cut remains near 250: add 1 bone at the e03 open (aggregate 252 region) signaling that Rowan's pastoral claim is an active variable as Taylor enters the market square — the volume in her possession, the awareness of the new relationship.
- Who owns: dramatist (as part of U3 boundary-rebalance subtask — confirm whether the new cut resolves U8; if not, route 1-bone addition to screen-writer).
- How it answers the seam: the pastoral-claim state propagates across the cut; S4 state-continuity and S6 tonal-arc continuity are both addressed.
- Cascade: see U3.

---

### U9 — e03→e04 continuity
- decision: REVISE
- citation: Gap 2 (B-baseline); S4 — state continuity; S2 — forward-flag honor; three-persona convergence (all three STRONG — highest defense burden)
- The seam has three-persona convergence — the highest available defense burden under the rubric's convergence-weighting clause. No rubric clause overrides all three personas here: S4 state continuity is clear that "state: every prop and actor across the season — props introduced are consumed/released or persist coherently" applies, and the two documentary state-changes (Rymer files watching at 369–370; literacy folio handed to Pryor at 405–411) are unambiguously state-changing events with no visible propagation at e04's open. S2 forward-flag honor names the census-to-IGNITION progression as a structural commitment. Cross-unit dependency: U14 REVISE (move e03 close to ~370) simultaneously addresses U9's most critical absence — if e03 closes on Rymer facing Taylor (aggregate 370), the surveillance-state becomes the e03 close image and the e04 open (now beginning at 371) carries the surveillance state in adjacent proximity. The U14 structural fix is the primary resolution for U9; however, the literacy-folio state-change (lines 405–411, now inside e04's range if the cut moves to 370) also needs a carry signal.
- What changes: (a) U14's placement revision (e03 closes at ~370) resolves the Rymer surveillance-state gap by making it the close image. (b) For the literacy folio handed to Pryor (now in e04's new range 371+): add 1 bone at e04 open region (aggregate 419–425, episode lines 1–7 region) signaling that the census established a documentary record of Taylor — either through Taylor's own posture or a brief environmental signal. This bone should be in the physical-observation register, not exposition.
- Who owns: screen-writer (1 bone at e04 open after U14 placement is resolved by dramatist); dramatist handles U14 structural fix.
- How it answers the seam: the surveillance-state is visible at the close of e03 (structural fix via U14); the documentary-exposure state propagates into e04's open (bone addition); the IGNITION beat fires with both e03 state-changes in reader working memory.
- Cascade: linked to U14. If U14 cut moves to 370, e04 range becomes 371–563 (or adjusted end-point); U9 bone addition is placed in the new e04 open region.

---

### U10 — e04→e05 continuity
- decision: REVISE
- citation: Gap 2 (B-baseline); S4 — reference (every slug/event resolves); S9 — comprehensibility (cause-effect chain fragile); two-persona convergence (pulp STRONG, worm MODERATE)
- The post-rider's letter (aggregate 542–548, episode lines 127–133) is an information-event that Taylor witnesses but the bones give no signal of whether she registered it as tactically relevant, and the e05 open (POV switch to Mira) drops this unresolved information-event with no bridge. S4's reference sweep requires "every slug resolves"; the post-rider's letter introduction and receipt establishes a fact whose content is never resolved across the cut. S9 comprehensibility names "cause-effect chain to the next beat fragile" as a risk when off-stage knowledge is required — the letter's board-change requires the reader to hold an open question with no close-signal.
- What changes: revise 1–2 bones in the e04 close region (aggregate 550–562, episode lines 135–147) to signal that Taylor registered the letter's arrival and its information-asymmetry consequence — not the letter's content (which can remain off-page), but Taylor's registration that a letter arrived and changed the reeve's behavior. This is a precision register fix: the current bones (post-rider exits square, Mira enters alley, taylor follows mira) give camera-cut, not continuity signal.
- Who owns: screen-writer (1–2 bone revisions in aggregate 550–562).
- How it answers the seam: the letter-event receives a close-signal before the cut; S4 reference sweep is satisfied; S9 cause-effect chain is legible.
- Cascade: no structural changes; aggregate_range headers unchanged.

---

### U11 — e05→e06 continuity
- decision: REVISE
- citation: Gap 2 (B-baseline); Phase 4 Step 2 — CLOSE-EARNS-NEXT; S4 — state continuity (Mira-debt); two-persona convergence (pulp STRONG, dark-fantasy STRONG)
- Two personas converge STRONG on the same absent bridge: e05 closes on taylor holds the feet (699) after 24 bones of workshop ledger-routine without any bone signaling that the Mira-debt (transacted at 636–641) is an active relationship-state; e06 opens on Elara's POV without the e05 state-changes visible in anyone's household posture. The Phase 4 Step 2 CLOSE-EARNS-NEXT criterion is not met: the feet-holding at 699 does not earn e06's Mira-free Elara-POV open. S4 state continuity is violated: the Mira-debt is a new actor-relationship state that should propagate.
- Note: this decision is partially linked to U16 (e05→e06 placement). A placement revision (see U16 below) trimming the 24-bone aftermath may structurally improve the close image; however, placement alone does not inject the missing Mira-debt signal.
- What changes: (a) Placement revision per U16 to trim aftermath bones. (b) Additionally, revise or add 1 bone in the e05 close region (aggregate 695–699 / episode 132–137 region) to signal the Mira-debt as an active state before the POV switch — Taylor's posture should carry some signal that the unnamed debt exists and is in working memory. The bone should be physical-register (holds, faces, presses) without naming the debt explicitly.
- Who owns: screen-writer (1 bone revision/addition in aggregate 695–699 region, after U16 placement is resolved).
- How it answers the seam: the Mira-debt state propagates across the cut; CLOSE-EARNS-NEXT is addressed because the close now carries forward tension rather than neutral feet-holding; S4 state-continuity is satisfied.
- Cascade: linked to U16 (placement revision comes first; then bone addition).

---

### U12 — e01→e02 placement
- decision: REVISE
- citation: Gap 3 (B-baseline); Phase 4 Step 1(b) — dramatic-shape close criterion; two-persona convergence (dark-fantasy MODERATE, pulp MODERATE)
- Two personas converge (dark-fantasy's preferred close: candle catches at episode line 130/aggregate 148; pulp's preferred close: candle catches at aggregate 131 in the e01 episode file) on the same 1-line improvement: the current cut at episode line 131 / aggregate 149 (oc-craftsman-father marks the ledger entry) is one line past the stronger close image (episode line 130: the candle catches). Reading the e01 file directly: line 130 = "the candle catches"; line 131 = "oc-craftsman-father marks the ledger entry." The ledger-entry close is an administrative act; the candle-catches close is the ignition image — atmospherically stronger and available one line earlier. Both personas identify this specific line.
- What changes: move e01/e02 cut from aggregate line 149 to aggregate line 148 (the candle catches). New e01 aggregate_range: 1–148 (no material change in episode size; the ledger-mark line moves to e02's open). New e02 aggregate_range: 149–250 (or 149–207 if U3 revision is applied).
- Who owns: showrunner-self (aggregate_range header field update: s01e01 aggregate_range 1–148; s01e02 aggregate_range 149–207 or 149–250 depending on U3 outcome). No bone generation needed — the cut moves by 1 line.
- How it answers the seam: e01 closes on an ignition image rather than an administrative record; Phase 4 Step 1(b) close criterion satisfied.
- Cascade: e01 aggregate_range header changes (1–148); e02 aggregate_range start changes (149 onward); the ledger-mark bone (aggregate 149) becomes e02's first numbered line, which is a plausible scene-entry (ledger record already made, Taylor enters the sept). If U3 revises the e02/e03 cut, the e02 range becomes 149–207 or nearby compliant value.

---

### U13 — e02→e03 placement
- decision: REVISE
- citation: Gap 3 (B-baseline); Phase 4 Step 1(b) — CLOSE-EARNS-NEXT; S2 — peak placement within episode arc; two-persona convergence (pulp STRONG, worm STRONG)
- This is the strongest convergence of any placement unit: pulp-enthusiast STRONG and worm-canon-pedant STRONG both name aggregate 207/208 (episode 58/59: taylor takes the volume / taylor grips the volume) as the correct close candidate. Dark-fantasy-reader's alternative (basin fly at 247/episode 98, aggregate 247) is weaker and is a minority position. The two-persona convergence on 207 is decisive: the volume-handoff is the episode's state-change beat and the strongest available close image. The current cut at 250 buries the payoff 43 lines later on column-tracing aftermath. This decision is already incorporated in U3 as the primary driver of that REVISE; they are the same placement call.
- What changes: move e02/e03 cut from aggregate 250 to aggregate 207 (taylor takes the volume) or 208 (taylor grips the volume). Preferred: 207 (takes = the decisive action); grips (208) is also acceptable as a stronger physical-register close. New e02 aggregate_range: 149–207 (59 lines, below 80-line floor — requires dramatist boundary-rebalance).
- Who owns: dramatist (boundary-rebalance subtask — e02 at 59 lines is below Phase 4 Step 1(a) lower bound; dramatist proposes compliant alternative: either push cut to produce 80+ line e02 while still closing on a meaningful beat, or restructure with a different 6-episode split that honors the volume-handoff as a close).
- How it answers the seam: closes e02 on the pastoral-claim state-change rather than 43 bones of aftermath; satisfies CLOSE-EARNS-NEXT and Phase 4 Step 1(b) close criterion.
- Cascade: e02 aggregate_range becomes 149–207 or dramatist's compliant value; e03 aggregate_range becomes 208–418 or adjusted value (e03 now begins in the sept aftermath, which is a different scene-entry and changes e03's interior shape — flagged as boundary-rebalance subtask); U8 cross-episode continuity may resolve structurally as noted there.

---

### U14 — e03→e04 placement
- decision: REVISE
- citation: Gap 3 (B-baseline); Phase 4 Step 1(b) — CLOSE-EARNS-NEXT; three-persona convergence (dark-fantasy MODERATE, pulp STRONG, worm STRONG)
- Three personas converge on the same candidate: rymer-hedge faces taylor-hebert-jaehaerys (aggregate line 370 / episode line 122) is the episode's most dangerous close candidate. The current cut at 418 is 48 lines later after fishwife dispute and literacy folio exchange. Per the convergence-weighting instruction, only a hard rubric clause can override three-persona convergence; no such clause exists here. S2 forward-flag honor (census beat: "Rymer files Taylor watching") requires this state-change to register as closing pressure; the current cut at 418 disperses it.
- What changes: move e03/e04 cut from aggregate 418 to aggregate 370 (rymer-hedge faces taylor-hebert-jaehaerys). New e03 aggregate_range: 251–370 (120 lines, mid-band, compliant). New e04 aggregate_range: 371–563 (193 lines, over the 160 ceiling — escalate as boundary-rebalance subtask to dramatist).
- Who owns: dramatist (boundary-rebalance subtask — e04 at 193 lines is 33 lines over the 160 ceiling; dramatist proposes: either extend e04 close end-point to distribute bones into e05 per the multiple-of-3 constraint, or accept e04 as a permitted over-band episode if the season's density supports it, noting Phase 4 Step 1(a)'s exact language is "default target band" and the 160 ceiling is not a hard maximum — but the rationale must be stated).
- How it answers the seam: closes e03 on the surveillance-vector image; satisfies CLOSE-EARNS-NEXT for all three personas; S2 forward-flag honor for the census beat.
- Cascade: e03 aggregate_range header changes (251–370); e04 aggregate_range header changes (371–563 or adjusted); linked to U9 (see U9 — the Rymer surveillance close also partially resolves U9's cross-episode continuity seam by making the surveillance state visible at the cut); e04's new opening (aggregate 371) begins immediately after Rymer faces Taylor, which is the fishwife-dispute sequence — this is a materially different episode-open than the current aggregate 419 (garrison man), so e04's goal statement may need minor adjustment.

---

### U15 — e04→e05 placement
- decision: DEFEND
- citation: Gap 3 (B-baseline); Phase 4 Step 1(b) — no viable alternative identified
- All three personas rate this THIN. The aggregate seam itself states "the ±20 window offers no stronger candidate." The current cut at 563 (taylor follows mira) is the tightest available forward-momentum close in its neighborhood; the 562/563 debate (mira retreats vs. taylor follows) is the only viable margin and both placements are defensible. Under Phase 4 Step 1(b), the cut closes on a beat that earns its own next-open: "taylor follows mira" directly earns the e05 Mira-POV alley entry. The bones stay as authored.

---

### U16 — e05→e06 placement
- decision: REVISE
- citation: Gap 3 (B-baseline); Phase 4 Step 1(b) — "close on a beat that earns its own next-open"; two-persona convergence (pulp MODERATE, dark-fantasy MODERATE)
- Two personas converge (pulp MODERATE, dark-fantasy MODERATE) on the same finding: the last 24 bones of e05 (aggregate 676–699 / episode 113–137) are workshop ledger-routine with no board-change, placing the cut 60 bones after the episode's last meaningful board-change (Mira-debt transacted at 636–641). The worm-canon-pedant's preferred close (aggregate 919-range / episode line 128: taylor releases the page) is available inside this range and is the most specific: it is a cost-register image (accepting the ledger's record) with more resonance than passive feet-holding at 699. The worm position is precise; pulp and dark-fantasy confirm the general diagnosis.
- What changes: move e05/e06 cut from aggregate 699 to approximately aggregate 919-range (episode line 128 per the worm seam: "taylor releases the page"). This requires identifying the exact aggregate ID for the "taylor releases the page" bone — per the e05 episode file, this is episode line 128. Per the aggregate file, s01e05 aggregate_range is 564–699, and episode line 128 maps to aggregate ~692 (564 + 128 = 692; adjusted for blank lines and gaps, this is in the 685–695 band). Provisional target: aggregate ~692 (taylor releases the page). New e05 aggregate_range: 564–692 (approx 129 lines, within band). New e06 aggregate_range: 693–912 (approx 220 lines, well over ceiling — escalate as boundary-rebalance subtask to dramatist).
- Who owns: dramatist (boundary-rebalance subtask — e06 over-band; must confirm whether the Elara-interlude POV constraint permits a cut before aggregate 700 without bisecting a POV-coherent stretch; the pov: oc-craftsman-mother marker is at e06 line 1 / aggregate 700 region — cutting before 700 would require the pov marker to land inside the new e06 open, which is possible if the pov marker precedes the first Elara-POV bone).
- How it answers the seam: closes e05 on a specific cost-register image (taylor releases the page) rather than neutral feet-holding; Phase 4 Step 1(b) satisfied; the close earns e06's Elara-POV open as a contrast image.
- Cascade: e05 aggregate_range header changes (~564–692); e06 aggregate_range header changes (~693–912); linked to U11 (continuity bone addition at e05 close; placement and continuity fix should be coordinated).

---

### U17 — Season aggregate shape (idiom depletion)
- decision: DEFEND-with-carry-back
- citation: S6 — VIBE-DRIFT-shard-load-suppressed / organism-texture-underweight (carry-forward, both named in B-baseline); S3.5 — drift-pattern report (holds-the-feet appearing 5+ times as borderline state-verb idiom); S2 — season-level rise-peak-fall; Gap 7 (B-baseline); rubric explicit gap — "no quantified definition of 'buildup' and 'denouement' share"
- The seam is real and the corpus confirms it: the holds-the-feet / holds-the-eyes / holds-the-chin group appears 20+ times in the instance list the seam provides, and the worm and dark-fantasy personas both converge STRONG on idiom depletion as shard-cost suppression. However, the rubric does not currently give a mechanic for adjudicating this at the bone level: S3.5's drift-pattern report flags "a verb appearing 5+ times across the season as a borderline state-verb," but "holds the feet" is a physical action verb (holds = physical grip/plant), not a state-verb on the deny-list — it falls in the rubric's gap between "state-verb deny-list" and "voice-register coherence drift." S5 voice-register coherence addresses drift from first-stretch to last-stretch, but the idiom in question is consistent voice-register (Taylor always uses physical-stasis); the fault is depletion through overuse, not inconsistency, which is a category the V1 rubric does not formalize.
- The blast radius of a REVISE here is 60–80 bones regenerated across the full aggregate by screen-writer — the largest single revision in this run. At V1, the rubric gives no stable criterion for what "differentiated enough" looks like: any regeneration would be measured against the same underspecified S6 vibe standard that allowed the carry-forward to ship in the first place.
- Defense at V1: the bones stay as authored. The shard-cost differentiation problem is real, but it cannot be corrected reliably against V1 rubric language — any fix risks introducing new failures in the same rubric's other passes (S3.5 is particularly constrained by the SVO discipline). This is a V2 rubric problem, not a V1 corpus problem.
- Carry-back queue entry: "V2 rubric addition needed: formalize 'idiom depletion' as a named fault class distinct from state-verb deny-list violation; define a differentiated-cost idiom standard for physical-stasis verbs appearing 5+ times across the aggregate with distinct shard-cost and non-shard-cost instances; provide a mechanic for distinguishing depletion from consistent register. Draft candidate: for any physical-stasis idiom appearing 10+ times in the aggregate, at minimum 25% of instances must carry a contextual differentiator (preceding scene density, following board-change, or direct proximity to a named shard-load beat) that allows a reader to distinguish cost-register from patience-register. Screen-writer owns regeneration of flagged instances under this criterion in a future pass."

---

## Routed subtasks (for main-session pickup)

### screen-writer
- U6: revise Elara interlude bones, aggregate 702–750 / e06 episode lines 3–48 — regenerate 3–6 bones to carry epistemic-limit cost register (failure-mode in what Elara does not understand) rather than only action register. S8a IMPLAUSIBLE-CHARACTER-oc-craftsman-mother carry-forward must be addressed.
- U7: add 1–2 bones at e02 open (aggregate 150–155 region) signaling apprentice-mark exposure as active operational variable. Harsh-SVO discipline applies; physical-register only.
- U9: add 1 bone at new e04 open region (aggregate 419–425 or post-U14-cut region ~371–380 open) signaling census documentary-record as active exposure variable before IGNITION fires. Physical-register only.
- U10: revise 1–2 bones in aggregate 550–562 / e04 episode lines 135–147 to signal Taylor's registration of the letter-arrival event before e05 POV switch.
- U11: add/revise 1 bone in aggregate 695–699 / e05 episode lines 132–137 region to signal Mira-debt as active relationship-state at e05 close. Coordinate with U16 placement revision.
- U3/U13 additional: if dramatist's boundary-rebalance for e02/e03 requires additional bones at the new e03 open (now beginning mid-sept-sequence), screen-writer generates them.

### dramatist
- U3/U13: boundary-rebalance subtask — e02 at ~58 lines (cut near 207) is below Phase 4 Step 1(a) 80-line floor; propose compliant alternative cut-point that (a) closes e02 on a stronger beat than column-tracing at 250, (b) produces e02 ≥ 80 lines, (c) produces e03 ≤ 160 lines or provides rationale for over-band. Candidate range to examine: does any cut between aggregate 220 and 240 (still in sept-aftermath, before market square) produce a better-than-250 close at ≥ 80-line episode size?
- U4/U14: boundary-rebalance subtask — e03 closes at aggregate 370 (120 lines, compliant); e04 now runs 371–563 = 193 lines, over 160 ceiling; dramatist proposes: either (a) push e04 end-point forward to distribute lines into e05 (requires e05 aggregate_range to shift accordingly, cascading into e06 start — check POV marker placement), or (b) accept e04 as permitted over-band given "default target band" language in Phase 4 Step 1(a), stating explicit rationale.
- U16: boundary-rebalance subtask — e05 closes at ~692 (129 lines, within band); e06 runs ~693–912 = ~220 lines, over 160 ceiling; dramatist must (a) confirm that cutting before aggregate 700 does not bisect the Elara POV stretch (the pov: oc-craftsman-mother marker is at e06 file line 1 / aggregate 700 region — cutting at 692 means the pov marker must be at or before 692 in the aggregate, or e06 must open before the marker; examine the actual marker placement), and (b) propose whether e06 over-band is acceptable (keeping the Elara-interlude wholly inside e06 was the original split rationale; 220 lines is now the justified over-band for interlude coherence).

### fixer
- (none in this phase — all revisions are bone additions or structural cuts, not error corrections)

### showrunner-self
- U12: update e01 aggregate_range header from 1–149 to 1–148 in memory.md and s01e01.md. Update e02 aggregate_range start from 150 to 149 (or to dramatist's U3/U13 compliant value once resolved).
- After dramatist resolves U3/U13 and U14 boundary-rebalance subtasks: update e02, e03, e04 aggregate_range headers in memory.md and respective per-episode files.
- After U16 is resolved: update e05, e06 aggregate_range headers in memory.md and respective per-episode files.
- After all header updates: verify contiguous, non-overlapping union of all six episode ranges equals the full aggregate 1..912 (accounting for legal ID-deletion gaps).
- Add tuning_r1_status field to memory.md (see below).

### carry-back queue (V2 rubric edit candidates)
- U17 carry-back: formalize "idiom depletion" as a named fault class. Draft mechanic provided in U17 decision above. Target: rubric V1.1 or V2; Phase H to draft.
- U1 carry-back: rubric should quantify acceptable denouement share of the aggregate (the 44% finding from U17/U1 is a legitimate rubric gap — S2 names "back half" constraint on climax placement but nothing names maximum denouement share). Candidate: "denouement must not exceed N% of aggregate; if denouement share exceeds 40%, a LATE-WEIGHT flag is issued for human review." Target: Phase H.
- Gap 8 (B-baseline — narrator field anomaly on e05/e06): rubric should clarify whether narrator: is the dominant POV or the interlude POV when an interlude is present. The shipped state (interlude POV as narrator) is a named anomaly. Resolution: either (a) add a rubric clause "when an episode contains a designated interlude as its primary dramatic arc, the interlude narrator is the named narrator," or (b) require narrator: to reflect dominant line-count POV. Target: Phase H.

---

## Phase E complete

No corpus files (aggregate, per-episode proto-line files, season-plan, series-plan) were modified in this phase. Phase E produces decisions and routing only.

Changes produced in this phase:
- The E-defense.md file (this document) is written.
- Memory.md will receive a tuning_r1_status field update (showrunner-self task, executed after this file is written).

What is queued for downstream phases:
- Phase F (final adjudication): receives this decision set for confirmation or override.
- Post-Phase-F execution: screen-writer bone additions/revisions (U6, U7, U9, U10, U11, U3/U13 open); dramatist boundary-rebalance subtasks (U3/U13, U14, U16); showrunner-self header updates (U12, plus all boundary-rebalance outcomes); per-episode file header rewrites.
- Phase H (carry-back): U17 idiom-depletion rubric formalization; U1 denouement-share quantification; Gap 8 narrator-field anomaly resolution.

The bones of U1, U2, U5, U15, and U17 are unchanged. The twelve REVISE decisions require downstream execution; none of the revisions delete existing content — all are additions (continuity bones), close-point shifts (placement decisions), or bone-level register fixes (U6 Elara rendering constraint).
