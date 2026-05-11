# Phase 2 continuity sweep — s01 — CYCLE 2

## File-level verdict
SEASON-CONTINUITY-OK

## Cycle 2 sweep scope

Targeted re-audit of five specific items following fixer and screen-writer changes since cycle 1. Full continuity axes confirmed against the post-fix bones file at `active-project/theater/proto-lines/s01.bones.md`.

---

## Re-check items — results

### 1. ID 500 physical position (close-log gap)

**Task:** Verify ID 500 (`taylor-hebert-flea-bottom closes the log`) fits between IDs 201 (open) and 205 (open) in the file's physical order.

**Result:** CONFIRMED. Physical ordering in the file:

```
201 taylor-hebert-flea-bottom opens the log
202 taylor-hebert-flea-bottom writes the entry
203  [gap — deleted]
204  [gap — deleted]
500 taylor-hebert-flea-bottom closes the log
501 oc-tanner-elder speaks to the carter
502 the wasps relay the labor-web pass
205 taylor-hebert-flea-bottom opens the log
206 taylor-hebert-flea-bottom writes the entry
207 taylor-hebert-flea-bottom closes the log
```

ID 500 is physically between ID 202 and ID 205. The log-close at 500 appears after the first write (202) and before the second open (205). The double-open fault is resolved. Log state is coherent across the full sequence: open → write → close (500) → [elder-carter exchange observable] → open → write → close. FAULT-PROP-STATE-01 is closed.

---

### 2. Maester slug transition

**Task:** Verify `the maester` only at IDs ≤301; `oc-broken-maester` at IDs ≥303.

**Result:** CONFIRMED. All pre-beat-16 maester references use "the maester":

- ID 111: `the maester speaks to the room` — correct (beat 7)
- ID 128: `the maester crosses the room` — correct (beat 7/8)
- ID 129: `the maester speaks` — correct
- ID 285: `the visitor speaks to the maester` — correct (beat 15, pre-naming)
- ID 286: `the maester speaks to the visitor` — correct (beat 15, pre-naming)

All post-beat-16 maester bones use `oc-broken-maester`:

- IDs 303–313 (beat 16 close and beat 17 overlap): confirmed `oc-broken-maester` throughout
- IDs 400–422 (beats 22): confirmed `oc-broken-maester` throughout

No occurrence of "the maester" at ID 303 or later. FAULT-SLUG-DRIFT-01 is closed.

---

### 3. New bones IDs 495–503 — POV and observability

**Task:** Verify all nine new bones are observable from Taylor's POV / insect network.

**Result:** Eight of nine are clean. One ordering flag at ID 501.

- **ID 495** (`taylor-hebert-flea-bottom speaks to oc-tanner-elder`) — beat 6 departure scene; Taylor is on-scene; elder already present at IDs 83–84. Observable. Clean.
- **ID 496** (`taylor-hebert-flea-bottom stills`) — beat 16; Taylor at base; self-action following beetle relay at IDs 296–298. Observable. Clean.
- **ID 497** (`taylor-hebert-flea-bottom faces the wall`) — beat 19; Taylor at base; post-expansion headache sequence. Observable. Clean.
- **ID 498** (`taylor-hebert-flea-bottom faces the wall`) — beat 24; Taylor at base; same pattern. Observable. Clean.
- **ID 499** (`taylor-hebert-flea-bottom straightens the spine`) — beat 24; Taylor at base. Observable. Clean.
- **ID 500** (`taylor-hebert-flea-bottom closes the log`) — beat 10; Taylor self-action. Observable. Clean.
- **ID 501** (`oc-tanner-elder speaks to the carter`) — beat 10; junction; see FLAG-RELAY-ORDER-01 below.
- **ID 502** (`the wasps relay the labor-web pass`) — beat 10; relay bone. Establishes Taylor's access to the labor-web routing event. Clean as relay.
- **ID 503** (`taylor-hebert-flea-bottom holds the feet`) — beat 22; Taylor at base; reaction to extended beetle relay. Observable. Clean.

---

### 4. Gap IDs 157, 158, 203, 204, 282, 283 — preserved

**Task:** Verify gap-IDs are preserved (deletions leave gaps visible, no renumbering).

**Result:** CONFIRMED. All six deletion gaps are physically present in the file as bare ID lines with no bone text:

- IDs 157, 158: confirmed blank — appear as standalone `157` and `158` lines at the beat-9 start
- IDs 203, 204: confirmed blank — appear as standalone `203` and `204` lines in the beat-10 transmission sequence
- IDs 282, 283: confirmed blank — appear as standalone `282` and `283` lines in the beat-15 stairwell sequence

No renumbering. Gap structure intact per schema.

---

### 5. New transmission bones at beat 10 — network-physics consistency

**Task:** Verify IDs 500/501/502 are consistent with season-plan network-physics (Taylor routes through Flea Bottom labor web without identifying herself).

**Result:** PASS with one ordering flag.

The beat-10 plan commits: Taylor routes weather-pattern data and Watch-movement timing through the whisper chain anonymously; chain accepts and transmits; she reads as "odd but functional."

ID 500 closes the log after the first write (weather-pattern data). ID 501 shows the elder relaying to the carter (chain operation). ID 502 shows wasps relaying the labor-web pass (Taylor's observational coverage of the routing). ID 205-207 is the second log sequence (Watch-movement timing write).

Network-physics: the elder as relay node between Taylor and the labor web is consistent with beat 6 and beat 8 establishing the elder as her Flea Bottom interface. The carters as downstream recipients of weather-pattern data is consistent with beat 10 plan prose. Taylor's anonymity is preserved — the elder speaks to the carter (501), not Taylor. No identifying contact between Taylor and the carter.

**Ordering concern (see FLAG-RELAY-ORDER-01):** ID 501 (elder speaks to carter, observed event) precedes ID 502 (wasps relay labor-web pass, relay bone). The relay logically enables the observation; ordering it after the observed event is structurally reversed. Junction fly coverage is pre-established from IDs 95–96 and active through prior beats, which partially mitigates the reversal, but this mirrors the class of issue that was escalated to FAULT-POV-LEAK-03 in cycle 1.

---

## Continuity axes — cycle 2 confirmation

### 1. Cross-season state

No changes to actor entries or exits introduced by the new bones. ID 495 (Taylor speaks to elder at departure) — the elder is present in that scene per existing IDs 83–84. ID 501 introduces "the carter" as an interaction partner for the elder at the junction. The elder at the junction is established. The carter is a functional-role entity (no location inconsistency; junction is within Taylor's established 300m range throughout beat 10). All existing cross-season state findings from cycle 1 remain valid: tanner-family visits coherent, clerk/messenger/middleman entries and exits clean, range expansion consistent.

### 2. Prop chains

- **The log:** FAULT-PROP-STATE-01 closed. Sequence at IDs 201–207 is now coherent with ID 500 closing between the two open-write-close cycles. All other log open/close sequences (21–23, 32–34, 58–60, 79–81, 101–103, 114–116, 124–126, 132–134, 153–155, 183–185, 196–198, 228–230, 242–244, 262–264, 276–278, 292–294, 299–301, 311–313, 326–328, 340–342, 357–359, 373–375, 396–398, 420–422, 434–436, 451–453, 473–475, 491–494) remain unchanged and coherent.
- **Dock-side cluster:** Unchanged. Burn-down at IDs 389–390 coherent; beat 24 expansion correctly absent from dock-side; denouement at ID 494 logs "dock-side insect cluster still thin" — consistent.
- **Sealed account (beat 25):** Unchanged. Coherent per cycle 1.
- **Purse (beat 13):** FLAG-PROP-CLOSE-01 from cycle 1 unresolved — no close-purse bone added. Still flag only; not load-bearing.

### 3. POV transitions

The three cycle-1 faults are resolved:

- **FAULT-POV-LEAK-01 (IDs 157–158):** Gap confirmed. Beat 9 opens cleanly at ID 159 with the tanner-family already at the junction — no south-gate observation claimed.
- **FAULT-POV-LEAK-02 (IDs 282–283):** Gap confirmed. Stairwell sequence now: `visitor enters stairwell` (281) → [gaps 282, 283] → `visitor enters upper room` (284). The remaining ID 281 (`the visitor enters the stairwell`) claims only positional presence in the stairwell, which is within the mouse-run's "positional data" capability per the apothecary location card. Clean.
- **FAULT-POV-LEAK-03 (IDs 203–204):** Gap confirmed. Recipient-state assertions removed. Beat 10 transmission bones (200, 501, 502) replace these without asserting what third parties received — the elder-to-carter exchange at 501 is an observed speech-act, not a recipient-state assertion.

No new POV leaks introduced by IDs 495–503. Maester-speaks bones at IDs 285–286 remain "the maester" (pre-naming, correct). Self-action bones (496, 497, 498, 499, 503) are Taylor's own body; no POV issue.

FLAG-INTERIOR-REGISTER-01 from cycle 1 (the `marks` vocabulary) is unaffected — those bones were at IDs 14, 17, 166, 170, 171; IDs 170 and 171 were fixed to `stills` per Group 4 fixer work; IDs 14 and 17 retain `stills` form as confirmed by fixer log. Flag condition resolved.

### 4. Reachability

No change to the start → end state path. Season open (tanner-village, 300m, IDs 1–82) to season close (Flea Bottom base, 600m, two external records, IDs 477–494) remains coherent. New bones introduce no new location traversals, no new range claims, no new record events. Beat 10 transmission bones (500–502) operate within the established 300m radius and do not imply range beyond what is established at that beat.

---

## Findings

### Fault

None new. All five cycle-1 faults are closed.

---

### Flags

- **flag-NNN (carry-forward):** FLAG-PROP-CLOSE-01 — purse opened at ID 254, no close-purse bone added in fix round. Still inert and non-load-bearing. No change.

- **FLAG-RELAY-ORDER-01**
  - `id`: FLAG-RELAY-ORDER-01
  - `type`: flag
  - `what`: ID 501 (`oc-tanner-elder speaks to the carter`) precedes ID 502 (`the wasps relay the labor-web pass`). The observed social exchange at the junction (501) is stated before the relay bone establishing Taylor's access to the labor-web routing event (502).
  - `why`: The relay-then-observation ordering rule grounds observed events in Taylor's insect coverage before asserting them as fact. The reversal here (observation before relay) mirrors the structure of FAULT-POV-LEAK-03 — which was classified as a fault in cycle 1 for the same reason (transmission vs. confirmed receipt; relay at 200 did not cover the receipt, and bones 203–204 asserted recipient state without a covering relay). Here the junction fly coverage is pre-established from IDs 95–96 and beat 7–8 relay activity, which reduces the severity — the junction is a covered surface, not an uncovered location. However, the labor-web pass relay (502) is specifically what grants Taylor access to the routing signal; 501 asserts the elder's speech as observed before that specific relay fires. Not escalated to fault given the pre-established junction coverage, but flagged for screen-writer awareness: at screen-write, the ordering should render as Taylor observing the elder's speech through established junction insects, with the labor-web routing becoming explicit afterward — not as two equally-grounded simultaneous observations.

---

## Cycle 2 verdict

**SEASON-CONTINUITY-OK**

All five cycle-1 faults are closed:
- FAULT-POV-LEAK-01: closed (IDs 157–158 deleted, gap preserved)
- FAULT-POV-LEAK-02: closed (IDs 282–283 deleted, gap preserved, stairwell entry ID 281 within mouse-run positional data capability)
- FAULT-POV-LEAK-03: closed (IDs 203–204 deleted, gap preserved, new bones 501–502 replace without recipient-state assertion)
- FAULT-SLUG-DRIFT-01: closed (oc-broken-maester confirmed at IDs 303+ throughout)
- FAULT-PROP-STATE-01: closed (ID 500 close-log confirmed between IDs 202 and 205 in physical order)

Carry-forward flags: FLAG-PROP-CLOSE-01 (purse, inert), FLAG-RELAY-ORDER-01 (new, non-blocking, screen-writer awareness item).

No escalation warranted.

---

---

# [ARCHIVED] Phase 2 continuity sweep — s01 — CYCLE 1

## File-level verdict
SEASON-CONTINUITY-FAIL

## Sweep results

### 1. Cross-season state

- **Taylor's location at season open:** Tanner-village (tanner-family bed, IDs 1–82). Transition to Flea Bottom at IDs 83–99. Location state is tracked coherently throughout. Taylor never appears in two locations simultaneously.
- **oc-tanner-family visits:** Beat 9 (IDs 157–181) — parents enter at south gate (IDs 157–158), cross to market-side junction (IDs 159–160). Beat 13 (IDs 246–264) — both parents at junction, wage-claim partial payment. Beat 17 (IDs 315–328) — mother alone at loc-flea-bottom-base. Beat 23 (IDs 424–436) — father alone at junction, relays to elder who relays to Taylor. All entries/exits coherent.
- **oc-tanner-elder:** Introduced at tanner-village (IDs 83–92), routes Taylor's placement. Present at Flea Bottom market-side junction throughout. Consistent.
- **oc-dock-runner:** Enters at Fish Gate margin (IDs 138–143), observed by flies. Approaches junction via elder (IDs 146–152). Exits cleanly at ID 152. No further appearance. Coherent.
- **The clerk / second clerk:** Beat 18 (IDs 330–342) — "the clerk" enters junction, speaks to tanner-elder, exits. Beat 20 (IDs 361–375) — "the second clerk" enters apothecary ground floor, speaks to apothecary owner, exits. Both enter and exit cleanly. No dangling actor.
- **The messenger / middleman:** Beat 25 (IDs 455–475) — messenger enters junction (ID 455), exits (ID 460). Elder goes to writing room, writes and seals account (IDs 465–468). Middleman receives sealed account (ID 469), exits writing room (ID 470). Taylor observes departure via flies (ID 471). Both exit cleanly. No dangling actor.
- **Range expansion state:** Tracked across five expansion events — beat 2 (300m, IDs 25–34 in tanner-village), beat 11 (~330m, IDs 209–230), beat 14 (400m, IDs 266–278), beat 19 (500m, IDs 344–359), beat 24 (600m, IDs 438–453). Each expansion followed by perimeter walk, grid notation, and headache. Physiological cost is present at all five events. Consistent with plan commitments.

### 2. Prop chains

- **The log:** First appears at ID 21 (beat 1, tanner-village). Used continuously and coherently through IDs 21–81 in tanner-village. Taylor lifts travel pack at ID 87 (log implicitly carried — the pack contains it; confirmed by log reappearing at IDs 101–103 immediately upon arrival at Flea Bottom base). Log continues throughout season to IDs 491–494 (beat 26, two log entries at season close). **Coherent.** However: **log-state fault at IDs 201–207** — log opens at ID 201, writes at ID 202, then IDs 203–204 interject (carter/dock-worker receipt statements), then log opens AGAIN at ID 205 with no intervening close. Two consecutive `opens the log` bones without a `closes the log` between. Log-state is corrupted at this sequence. See FAULT-PROP-STATE-01.

- **The salt:** Introduced at ID 8 (Taylor extends arm toward salt), drawn at ID 10 (Taylor draws the salt). Used implicitly during the meal scene. Never explicitly set down or exited. This is a tanner-village meal prop with no load-bearing forward consequence; the prop is inert after ID 10 and does not appear in subsequent scenes. No orphan problem — it is a scene-local prop that lives on the tanner-family table and is not carried forward.

- **The travel pack:** Appears at ID 87 (Taylor lifts the travel pack). Arrives at Flea Bottom base at ID 100 (Taylor sets the travel pack). Explicit set-down confirms delivery. Clean prop chain.

- **The dock-side insect cluster:** Active at IDs 210, 267 (wasps spread dock-side alleys). Beat 21 burn-down at IDs 383–390: cluster explicitly thins at IDs 389–390 (`the dock-side cluster thins`, `the flies thin the dock-side relay`). Post-burn: beat 24 range expansion (IDs 438–453) does NOT include `the wasps spread the dock-side alleys` (present in beat 19 at ID 345, absent in beat 24). The dock-side is correctly absent from the beat 24 operation, consistent with the cluster remaining thin. **Coherent.** No post-burn bones imply the dock-side cluster is functioning normally.

- **The sealed account (beat 25):** Appears at ID 468 (oc-tanner-elder seals the account). Received by the middleman at ID 469. Middleman exits at ID 470. Taylor observes departure via flies (ID 471) but per plan cannot observe what is written or where it goes. Account exits the scene with the middleman and is not further tracked. **Clean. No orphan.**

- **The record book (clerk):** Clerk opens record book at ID 334, writes at ID 335, closes at ID 336. Second clerk opens at ID 367, writes at ID 368, closes at ID 369. Both prop-open/close sequences are complete. Clean.

- **The purse / coins (beat 13):** Taylor opens the purse at ID 254, extends coins at ID 255, oc-tanner-father receives coins at ID 256. Purse is not explicitly closed or re-stowed. Minor sequence incompleteness — no close-purse bone. Not load-bearing; the purse does not reappear. Flag only.

### 3. POV transitions

- **POV:** Monolithic Taylor (taylor-hebert-flea-bottom). No `# pov:` markers present in the file. Expected per plan ("One POV: Taylor"). Correct.

- **POV leak at IDs 157–158:** `oc-tanner-father enters King's Landing via the south gate` / `oc-tanner-mother enters King's Landing via the south gate`. At this point in beat 9, Taylor is at or near the market-side junction in Flea Bottom (she approaches the junction at ID 163). The south gate of King's Landing is outside Taylor's established 300m radius from her Flea Bottom base. No insect relay bone precedes or accompanies IDs 157–158. These two bones state the parents' entry at the south gate as direct observed fact without a relay establishing Taylor's observational access. The junction (IDs 159–160) is within range; the south gate is not. **FAULT-POV-LEAK-01.** See fault entry.

- **POV concern at IDs 281–284 (visitor stairwell, beat 15):** `the visitor enters the stairwell` / `the visitor pauses in the stairwell` (twice) / `the visitor enters the upper room`. The beetle relay confirming Taylor's access to the upper-room register does not appear until ID 287. The stairwell pauses (IDs 282–283) are stated as direct fact with no relay bone. The loc-eastern-quarter-apothecary card establishes Taylor's insect presence in: south-wall beetle colony gap, south-window fly population, wall-cavity mouse-run (positional data), and ceiling-corner spiders. The mouse-run "positional data" may cover stairwell footfall, but this is not explicit. The two stairwell-pause bones (IDs 282–283) claim fine-grained behavioral information (the visitor pauses twice, distinct from simply ascending) that exceeds what positional data from a mouse-run would deliver. **FAULT-POV-LEAK-02.** See fault entry. Borderline — flagged as fault given bias-toward-flag instruction and the specificity of the pause beats.

- **POV concern at IDs 203–204:** `the carters receive the weather-pattern data` / `the dock workers receive the Watch-movement timing`. These are recipient-state statements. Taylor has no insect relay bone confirming observation of the carters or dock workers receiving data; the fly relay at ID 200 covers the weather-pattern data being transmitted, not the receipt. These bones state what third parties received as a matter of fact, not as Taylor-observed outcome. This is a narrator-intrusion POV leak. **FAULT-POV-LEAK-03.** See fault entry.

- **Interior register check — oc-tanner-father "marks" bones:** IDs 14, 17, 166, 170, 171. `oc-tanner-father marks the stillness`, `marks the pivot angle`, `marks the half-second`, `marks the scan pattern`; `oc-tanner-mother marks the scan pattern`. These are interior cognitive-register bones attributed to the tanner characters. From Taylor's POV (insect network plus direct observation), she can read body-language and behavioral tells, but `marks` implies internal cognition she cannot directly access. However, the series uses `marks` as a behavioral-tell vocabulary (observable external behavior that Taylor reads as the father registering something), consistent with the clinical register. Borderline. Not escalated to fault — the `marks` bones are ambiguous between interior cognition (leak) and behavioral observation (legal). **Flag only.**

### 4. Reachability

- **Tanner-village → Flea Bottom transition:** IDs 83–99. Coherent. Tanner-elder routes placement (ID 86), Taylor lifts travel pack (ID 87), tanner-family farewell (IDs 88–89), Taylor exits yard gate (ID 90), walks road (IDs 91–92), blank ID 93 (time-skip covering day's walk), enters loc-flea-bottom (ID 94), enters loc-flea-bottom-base (ID 99). Transition is fully traversed, no teleport, road journey accounted for by the time-skip at ID 93. **Coherent.**

- **Range progression:** 300m (story open, tanner-village, IDs 25–34) → ~330m (overnight expansion, IDs 209–230) → 400m (autumn expansion, IDs 266–278) → 500m (winter-onset expansion, IDs 344–359) → 600m (late-winter expansion, IDs 438–453). Five discrete expansion events with perimeter walk, grid notation, and headache cost at each. No bone in any stretch implies a range Taylor does not yet have — the insect spread bones stay within the established range for each stretch. **Coherent.**

- **Season start → season close delta:** Start state: Taylor in tanner-village at 300m range. End state required: Flea Bottom base, 600m range, two records existing (one lord's-man record per beat 23, one Hand's file per beat 25). Bones deliver: Flea Bottom base (confirmed throughout from ID 99), 600m range (ID 438–453), lord's-man record (tanner-father states it to elder, IDs 424–428, relayed to Taylor ID 431), Hand's file completing under wrong framework (messenger/middleman sequence, IDs 455–475). Both records exist at season close. Beat 26 denouement (IDs 477–494): Taylor walks full perimeter, returns to base, writes two log entries side by side (IDs 492–493). The double write at 492–493 matches the plan's "two log entries side-by-side" at beat 26. **Reachability coherent.**

- **Maester naming transition (beat 16):** Season plan commits: before beat 16, "the maester" (lowercase, non-named); after beat 16 (`oc-broken-maester` slug). Beat 16 is IDs 296–313. Examination of all maester bones: IDs 111, 128, 129, 155 (not present — confirmed), 303, 304, 305, 306, 308, 309, 310, 400, 401, 403, 404, 406, 407, 408, 409, 410, 411, 413, 414, 415 — all use "the maester." The slug `oc-broken-maester` does not appear anywhere in the 494-bone file. After beat 16, all maester references remain "the maester" through IDs 303–422. **FAULT-SLUG-DRIFT-01.** See fault entry.

- **Hightower apparatus naming:** Beats 18 (IDs 330–342), 20 (IDs 361–375), 25 (IDs 455–475). All use: `the clerk` (IDs 330–337), `the second clerk` (IDs 361–370), `the messenger` (IDs 455–462), `the middleman` (IDs 469–471). No Hightower slug, no `oc-otto-hightower`, no `oc-hightower-clerk`. **Coherent. Correct.**

- **Time-skip markers:** 39 blank IDs confirmed (24, 35, 47, 61, 70, 78, 82, 93, 104, 117, 127, 135, 144, 156, 182, 186, 194, 199, 208, 231, 245, 261, 265, 279, 295, 302, 314, 325, 329, 343, 360, 376, 382, 399, 423, 437, 454, 464, 476). All correspond to plausible elapsed-time gaps between distinct beats or sub-beats. The road journey (tanner-village to King's Landing, day's walk) is covered by the blank at ID 93. No scene shift detected without a blank. **Coherent.**

---

## Faults (cycle 1)

- **FAULT-POV-LEAK-01:** IDs 157–158 — `oc-tanner-father enters King's Landing via the south gate` / `oc-tanner-mother enters King's Landing via the south gate`. Taylor is at or near the market-side junction in Flea Bottom. The south gate of King's Landing is outside her established 300m radius. No insect relay bone precedes these lines. These are offstage movements at an unobservable location narrated as fact without a relay establishing Taylor's access. Downstream consequence: at screen-write, these bones will produce narration that implies Taylor's POV extends to the south gate, which violates single-POV and the range ceiling. Route: **fixer** (line-level — insert relay bone or reframe from junction-arrival perspective, dropping south-gate entry bones and starting with the characters crossing the junction at IDs 159–160).

- **FAULT-POV-LEAK-02:** IDs 282–283 — `the visitor pauses in the stairwell` (twice). Taylor's established insect coverage of the apothecary does not explicitly include the stairwell interior. The mouse-run in the wall cavity provides "positional data" per the location card, but the two stairwell-pause bones claim distinct behavioral beats (two separate pauses) that exceed positional data granularity. No relay bone covers the stairwell between IDs 280 and 287. Downstream consequence: screen-write will render the visitor's stairwell hesitation as Taylor-observed fact, implying coverage she doesn't have. Route: **fixer** (line-level — add a relay bone attributing the stairwell detection to the wall-cavity mouse-run, or collapse the two pause bones into a single footfall-delay entry mediated by the mouse-run's positional data register).

- **FAULT-POV-LEAK-03:** IDs 203–204 — `the carters receive the weather-pattern data` / `the dock workers receive the Watch-movement timing`. No relay bone establishes Taylor's insect coverage of the carters or dock workers receiving these data. The fly relay at ID 200 covers transmission, not confirmed receipt. These bones state third-party internal-state (what the recipients received) as a matter of record, not as relayed observation. Downstream consequence: screen-write will produce narration asserting what the carters and dock workers received, which is outside Taylor's POV. Route: **fixer** (line-level — reframe as Taylor observes the data passing through the network; drop the recipient-state assertion, or replace with relay bones showing Taylor's flies at the handoff points).

- **FAULT-SLUG-DRIFT-01:** IDs 303–422 (post-beat-16) — "the maester" slug used throughout all post-named-entry bones. Season plan commits: after beat 16 (IDs 296–313), Taylor has logged the maester as a named presence and the bones should use `oc-broken-maester`. Every post-beat-16 maester bone — IDs 303, 304, 305, 306, 307, 308, 309, 310, 400, 401, 403, 404, 405, 406, 407, 408, 409, 410, 411, 413, 414, 415, 416, 417, 418, 419 — uses "the maester" not `oc-broken-maester`. Downstream consequence: the naming transition that marks Taylor's epistemic shift (pre-named / post-named) is erased from the bones. Screen-writer and Phase 7 episode-write both consume these bones; the slug distinction is a structural continuity signal. Also creates inconsistency with the cast-roster (which defines `oc-broken-maester` as the character's identifier). Route: **fixer** (systematic line-level — replace "the maester" with `oc-broken-maester` in all bones at ID 303 and later; IDs 111–301 retain "the maester" which is correct for the pre-named period).

- **FAULT-PROP-STATE-01:** IDs 201–207 — log-state corruption. `taylor-hebert-flea-bottom opens the log` (ID 201) → `taylor-hebert-flea-bottom writes the entry` (ID 202) → [IDs 203–204: carters/dock-workers receipt interject] → `taylor-hebert-flea-bottom opens the log` (ID 205) → `taylor-hebert-flea-bottom writes the entry` (ID 206) → `taylor-hebert-flea-bottom closes the log` (ID 207). The log is opened at ID 201, never closed, then opened again at ID 205. The log-state is `open` when the second `opens the log` fires. Downstream consequence: screen-write treats the log as a bounded prop state; the double-open implies either a continuity error or a missing close-log bone between IDs 202 and 205. Route: **fixer** (line-level — insert `taylor-hebert-flea-bottom closes the log` between IDs 202 and 203, or restructure the stretch so the carters/dock-workers interject lines appear within a single open/write/close sequence using a second write bone rather than a second open).

---

## Flags (non-fault, cycle 1)

- **FLAG-INTERIOR-REGISTER-01:** IDs 14, 17, 166, 170, 171 — `marks the stillness` / `marks the pivot angle` / `marks the half-second` / `marks the scan pattern` (twice, father and mother). The verb `marks` carries interior-cognition weight (implies a character noticing and registering something internally). From Taylor's POV, she can read behavioral tells but not internal registration. The bones may be using `marks` as shorthand for "exhibits a readable behavioral tell that Taylor interprets as the character registering X" — this is consistent with the clinical register and does not unambiguously require access to the tanner characters' interior. Not classified as fault. Flagged for screen-writer awareness: `marks` bones should render as Taylor reading visible behavioral indicators, not as direct access to another character's cognition.

- **FLAG-PROP-CLOSE-01:** ID 254–256 — purse opened, coins extended and received; no close-purse bone. Inert after ID 256. Not load-bearing. Flagged for fixer to add a close-purse bone if prop-state bookkeeping is enforced at the shoot level.
