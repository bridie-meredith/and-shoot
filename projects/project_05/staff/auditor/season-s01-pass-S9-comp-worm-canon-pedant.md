# S9 Comprehensibility Pass — s01 bones
# Persona: worm-canon-pedant
# Date: 2026-05-11
# File-level verdict: COMPREHENSIBILITY-RISK-attention-formula-lock

---

## Sweep parameters

- Input: `active-project/theater/proto-lines/s01.bones.md`
- Reference: `active-project/staff/showrunner/season-s01-plan.md`
- Window size: ~10 bones
- Verdict per window: ENGAGED / TOLERATED / BORED
- Triggers: 2 consecutive BORED, 3 consecutive TOLERATED, ≥30% BORED-or-TOLERATED in any 100-line stretch

---

## Window verdicts

| Window | Bones (approx) | Verdict | Reason |
|--------|---------------|---------|--------|
| 1 | 1–10 | ENGAGED | Father's surveillance-pivot sequence is load-bearing; each action connects |
| 2 | 10–23 | ENGAGED | Log entries earn their slot as first appearance of the pattern |
| 3 | 25–34 | ENGAGED | Four-insect perimeter spread is information-complete; range inventory legible |
| 4 | 36–46 | ENGAGED | Three song-note bones function as a test sequence; drop and foreclosure land |
| 5 | 48–60 | ENGAGED | Labor-reordering reads as structural withdrawal; father's routing pattern clear |
| 6 | 62–77 | ENGAGED | Reeve → lord's man chain is complete; file opens legibly |
| 7 | 79–92 | ENGAGED | Elder-Taylor exchange and departure land; out-of-sequence inserts (495, 504) are contextually legible |
| 8 | 94–103 | ENGAGED | First King's Landing insect spread is geographically specific; cause-effect clean |
| 9 | 105–116 | TOLERATED | Three write-entry bones in close proximity (109, 113, 115) require inference to distinguish from mechanical repetition; first log-tripling accumulation |
| 10 | 118–126 | TOLERATED | Bone 123 writes before the log is opened; bones 124–126 then open and write again — micro-sequence logic break creates comprehensibility wobble |
| 11 | 128–143 | ENGAGED | Maester scene and Watch/dock-runner sequence are legible; "holds the feet" reads correctly as non-intervention |
| 12 | 145–155 | ENGAGED | Transactional exchange completing at bone level; cause-effect clean |
| 13 | 157–172 | TOLERATED | "The arrival" (bone 164) is an unidentified entity with no bone-level referent; the tell-exposure (bones 165–168) works but its trigger is underspecified |
| 14 | 172–190 | ENGAGED | Family departure complete; whisper-chain relay begins; cause-effect present |
| 15 | 187–207 | BORED | Severe fragmentation: multiple gap clusters; out-of-sequence bones 500, 508, 501, 502 introduce the carter and "the pass" with no preparation; reader cannot reconstruct the action chain |
| 16 | 209–230 | TOLERATED | Triple-exhale (213, 218, 221) across 8 bones with no intervening action reads as padding; range-expansion sequence formula appears for the first time at full length |
| 17 | 232–244 | ENGAGED | Eviction sequence is cause-effect complete; neighbors' non-intervention readable at bone level |
| 18 | 246–264 | ENGAGED | Partial payment and transactional formalization land; exchange structure sufficient |
| 19 | 266–278 | TOLERATED | Missing beetle spread (gap at 268) disrupts the established four-insect pattern; no explanation; range-expansion formula second appearance |
| 20 | 280–301 | TOLERATED | Beetles relaying "rhythm / phrase / rhythm" (296–298) are mechanically indistinguishable at bone level; tripling with no differentiation |
| 21 | 305–313 | ENGAGED | Named-maester recognition at bone level is legible; cataloguing moment clean |
| 22 | 315–328 | ENGAGED | Mother's solo visit with grief-state change lands; exchange structure carries the beat |
| 23 | 330–342 | ENGAGED | Hightower-apparatus clerk sequence complete; cause-effect clean |
| 24 | 344–359 | TOLERATED | Range-expansion formula third full appearance; sequence is now predictable bone-by-bone; five-insect variant is noted but does not break formula-lock |
| 25 | 361–375 | ENGAGED | Second clerk / apothecary-owner exchange complete; four-beat structure carries the naming event |
| 26 | 377–398 | ENGAGED | Dock-side task and cluster burn readable; cluster thinning and fly-retraction imply cost correctly |
| 27 | 400–422 | ENGAGED | Maester's market excursion fully bone-covered; beetles track throughout; extended pen-scratch implied at bone level |
| 28 | 424–453 | TOLERATED | Range-expansion formula fourth appearance; bone 507 (Taylor faces Red Keep) is load-bearing but placed after log close, creating disorientation; beat 23's formal-record content is bone-sparse |
| 29 | 455–475 | TOLERATED | Bones 461–462 are identical consecutive relay bones at the season's peak beat; duplicate flattens the climax moment |
| 30 | 477–494 | ENGAGED | Denouement walk is fully covered; two distinct write bones (492, 493) distinguish the dual log entries; beat lands |

---

## Trigger analysis

**Consecutive BORED:** 0 instances. Threshold not triggered.

**Consecutive TOLERATED (3+):**
- Windows 9–10: 2 consecutive. Below threshold.
- Windows 19–20: 2 consecutive. Below threshold.
- Windows 28–29: 2 consecutive. Below threshold.
No three-consecutive-TOLERATED run. Threshold not triggered on this rule.

**30% BORED-or-TOLERATED in any 100-line stretch:**
Total windows: 30. BORED-or-TOLERATED: 10 (Windows 9, 10, 13, 15, 16, 19, 20, 24, 28, 29).
Rate: 10/30 = **33.3%**. Threshold is 30%. **TRIGGERED.**

---

## Risk findings

### COMPREHENSIBILITY-RISK-attention-fragmentation
**Location:** Window 15, bones ~187–207 (out-of-sequence cluster: 500, 508, 501, 502 inserted amid gap bones 189, 191, 193, 194, 199, 203, 204)

The bone sequence in this range is the single genuine comprehensibility failure in the file. Out-of-sequence bones introduce two unresolved referents — "the carter" (bone 501) and "the pass" (bone 502, "wasps relay the pass") — with no prior bone establishing either entity. The intervening gap bones (which appear to be episode-break or placeholder markers) compound the fragmentation: the reader cannot determine whether the gaps are scene breaks, time ellipses, or missing bones. The elder-and-carter exchange in bones 508, 501 has no cause-effect preparation in the preceding bones. The beat this window is meant to carry (beat 10: whisper-chain mapping; weather-pattern data routing) loses its spine.

This is a skeleton-level structural gap, not a prose-layer issue. The bones themselves do not hold the action chain.

### COMPREHENSIBILITY-RISK-attention-formula-lock
**Location:** Distributed — Windows 9, 10, 16, 19, 20, 24, 28 (range-expansion sequences and log-triple accumulation)

The range-expansion sequence bone pattern — spread (× 4 insect types) → perimeter walk → write entry (× 2) → exhale → headache wakes → holds eyes → [inserted bone] → log open/write/close — appears four times at substantively identical bone structure (Beats 11, 14, 19, 24; windows 16, 19, 24, 28). By the third appearance (Window 24, Beat 19), the reader can predict each bone before it arrives. The fourth appearance (Window 28, Beat 24) adds bone 507 (Taylor faces the Red Keep) as an inserted differentiation — but the inserted bone appears after log-close, which is the conventional end-of-window position, and it reads as dislocated rather than as a climax marker.

Separately, the log-open / write-entry / close-log triple has accumulated across nearly every scene boundary in the bones (approximately 20+ instances). At bone level, log entries are not differentiated from each other — every "writes the entry" is structurally identical regardless of what is being logged. Beat 26's two-entry denouement (bones 492, 493) is legible as distinct only because two consecutive write bones appear before the close; it is not bone-labeled as the dual-entry moment it is in the season plan.

The formula-lock is responsible for eight TOLERATED windows. It does not create outright incomprehensibility — cause-effect is always present, information is always accumulating — but it steadily erodes attention because no individual bone within the formula is distinguishable from its predecessors.

### COMPREHENSIBILITY-RISK-attention-peak-flatness
**Location:** Window 29, bones 461–462

At the season's peak beat (beat 25, the Hand's file completing), bones 461 and 462 are identical: both read "the flies relay the messenger." Two consecutive bones with identical text at a climax moment flatten the narrative momentum at exactly the point it should be highest. The season plan marks beat 25 as PEAK. At bone level it reads as identical to any mid-season relay sequence.

---

## Per-risk severity

| Risk | Severity | Rule triggered |
|------|----------|---------------|
| COMPREHENSIBILITY-RISK-attention-fragmentation | HARD | Window 15 = BORED; ≥30% threshold |
| COMPREHENSIBILITY-RISK-attention-formula-lock | HARD | ≥30% threshold (primary driver at 8 TOLERATED windows) |
| COMPREHENSIBILITY-RISK-attention-peak-flatness | SOFT | Noted; does not independently trigger threshold |

---

## File-level verdict

**COMPREHENSIBILITY-RISK-attention-formula-lock**

Two HARD findings. The 33.3% BORED-or-TOLERATED rate across the full season bones exceeds the 30% threshold. The primary driver is formula-lock (8 TOLERATED windows from repeated bone-identical sequences). The secondary driver is the single fragmented window (Window 15, 1 BORED) with unresolved referents at bone level.

The bones carry the season plan's cause-effect architecture correctly in 20 of 30 windows. The risk is not structural incoherence — it is sustained attention erosion from pattern repetition that a skeleton-level document cannot paper over with prose. Flesh-out will not automatically resolve formula-lock if the prose layer inherits identical structural beats without differentiation.

Flagged for screen-writer review before Phase 4 advance.
