# s01e03 State-Update Citation Mapping
# Built for flag-004 (STR-004) remediation
# Source: consolidated state-updates.md (env slice IDs 1-27 + per-character slices 28-62)
# Per the finding criteria: per-character slice entries in proto-lines use local IDs that
# collide with env-slice IDs; requires rewrite to consolidated IDs.

## Per-character Slice → Consolidated ID Mapping

### state-update-oc-broken-maester slice
# Original slice had 3 entries before culls (@74, @88 culled; @164 remained as local :3)
# state-update-oc-broken-maester:1 = CULLED @74 (never in consolidated)
# state-update-oc-broken-maester:2 = CULLED @88 (never in consolidated)
# state-update-oc-broken-maester:3 = @164 actor:oc-broken-maester.documentation_status → consolidated state:28

### state-update-oc-tanner-elder slice
# state-update-oc-tanner-elder:1 = @67 actor:oc-tanner-elder.stance-toward-taylor → consolidated state:29
# state-update-oc-tanner-elder:2 = @129 actor:oc-tanner-elder.knowledge.hightower-file-channel → consolidated state:30
# state-update-oc-tanner-elder:3 = @137 actor:oc-tanner-elder.location → consolidated state:31
# state-update-oc-tanner-elder:4 = @139 actor:oc-tanner-elder.formal-record-status → consolidated state:32

### state-update-oc-tanner-father slice
# state-update-oc-tanner-father:1 = @96 actor:oc-tanner-father.location village→junction → consolidated state:33
# state-update-oc-tanner-father:2 = @98 actor:oc-tanner-father.claim-status → consolidated state:34
# state-update-oc-tanner-father:3 = @101 actor:oc-tanner-father.location junction→returning → consolidated state:35

### state-update-taylor-hebert-flea-bottom slice
# :1  = @8  taylor.knowledge.first-clerk-record unknown→recorded → consolidated state:36
# :2  = @11 taylor.knowledge.first-clerk-record recorded→beyond-fish-gate → consolidated state:37
# :3  = @15 taylor.log_entries_episode 0→1 → consolidated state:38
# :4  = @22 taylor.stats.fauna_control_radius_m 300→400 → consolidated state:39
# :5  = @22 taylor.swarm_network_composition → consolidated state:40
# :6  = @24 taylor.log_entries_episode 1→2 → consolidated state:41
# :7  = @26 taylor.physical_condition intact→sleep-cycled-night-one → consolidated state:42
# :8  = @30 taylor.log_entries_episode 2→3 → consolidated state:43
# :9  = @40 taylor.knowledge.second-clerk-record unknown→recorded → consolidated state:44
# :10 = @42 taylor.knowledge.second-clerk-record recorded→sealed → consolidated state:45
# :11 = @47 taylor.log_entries_episode 3→4 → consolidated state:46
# :12 = @67 taylor.inventory []→[coin-from-elder] → consolidated state:47
# :13 = @70 taylor.log_entries_episode 4→5 → consolidated state:48
# :14 = @93 taylor.log_entries_episode 5→6 → consolidated state:49
# :15 = @103 taylor.knowledge.father-petitioned-elder → consolidated state:50
# :16 = @107 taylor.log_entries_episode 6→7 → consolidated state:51
# :17 = @114 taylor.stats.fauna_control_radius_m 400→500 → consolidated state:52
# :18 = @116 taylor.log_entries_episode 7→8 → consolidated state:53
# :19 = @118 taylor.physical_condition sleep-cycled-night-two → consolidated state:54
# :20 = @123 taylor.log_entries_episode 8→9 → consolidated state:55
# :21 = @125 taylor.knowledge.red-keep-beyond-ceiling → consolidated state:56
# :22 = @133 taylor.knowledge.messenger-to-elder → consolidated state:57
# :23 = @142 taylor.knowledge.formal-account-sealed → consolidated state:58
# :24 = @145 taylor.log_entries_episode 9→10 → consolidated state:59
# :25 = @155 taylor.stats.fauna_control_radius_m 500→600 → consolidated state:60
# :26 = @162 taylor.knowledge.record-discipline-state → consolidated state:61
# :27 = @164 taylor.log_entries_episode 10→11 → consolidated state:62

---

## Proto-line Citation Rewrite Table

# Format: proto-line @X  cited [state:K]  was per-slice <slug>:K_local  → consolidated state:N

proto-line @96   cited [state:1]    was oc-tanner-father:1 (location village→junction @96)    → consolidated state:33
proto-line @125  cited [state:21]   was taylor:21 (knowledge.red-keep-beyond-ceiling @125)     → consolidated state:56
  NOTE: @125 also cites [state:20] = consolidated state:20 = env @125 studio.fauna_sense_status.operational_radius — THIS IS CORRECT (env-slice ID 20 stays 20)
proto-line @164  cited [state:1]    was env:1 (wrong anchor — @164 anchor is maester+taylor entries)  → consolidated state:28
proto-line @164  cited [state:27]   was env:27 (wrong anchor — env @165 oc-taylor-log open→closed)     → consolidated state:62

## Summary of edits to proto-lines/s01e03.md (COMPLETE — all per-character slice citations)

# Already applied (audit examples):
@96   [state:1]  → [state:33]   (father local:1 = father.location village→junction)
@125  [state:21] → [state:56]   (taylor local:21 = knowledge.red-keep)
@164  [state:1]  → [state:28]   (maester local:3 = documentation_status)
@164  [state:27] → [state:62]   (taylor local:27 = log_entries_episode 10→11)

# Additional per-character-slice citations requiring rewrite:
@8    [state:1]  → [state:36]   (taylor local:1 = knowledge.first-clerk-record unknown→recorded)
@11   [state:2]  → [state:37]   (taylor local:2 = knowledge.first-clerk-record recorded→beyond)
@15   [state:3]  → [state:38]   (taylor local:3 = log_entries_episode 0→1)
@22   [state:4]  → [state:39]   (taylor local:4 = stats.fauna 300→400)
@22   [state:5]  → [state:40]   (taylor local:5 = swarm_network_composition)
@24   [state:6]  → [state:41]   (taylor local:6 = log_entries_episode 1→2)
@26   [state:7]  → [state:42]   (taylor local:7 = physical_condition night-one)
@30   [state:8]  → [state:43]   (taylor local:8 = log_entries_episode 2→3)
@40   [state:9]  → [state:44]   (taylor local:9 = knowledge.second-clerk-record unknown→recorded)
@42   [state:10] → [state:45]   (taylor local:10 = knowledge.second-clerk-record recorded→sealed)
@47   [state:11] → [state:46]   (taylor local:11 = log_entries_episode 3→4)
@67   [state:1]  → [state:29]   (elder local:1 = stance-toward-taylor)
@67   [state:12] → [state:47]   (taylor local:12 = inventory []→[coin])
@70   [state:13] → [state:48]   (taylor local:13 = log_entries_episode 4→5)
@93   [state:14] → [state:49]   (taylor local:14 = log_entries_episode 5→6)
@98   [state:2]  → [state:34]   (father local:2 = claim-status)
@101  [state:3]  → [state:35]   (father local:3 = location junction→returning)
@103  [state:15] → [state:50]   (taylor local:15 = knowledge.father-petitioned-elder)
@107  [state:16] → [state:51]   (taylor local:16 = log_entries_episode 6→7)
@114  [state:17] → [state:52]   (taylor local:17 = stats.fauna 400→500)
@116  [state:18] → [state:53]   (taylor local:18 = log_entries_episode 7→8)
@118  [state:19] → [state:54]   (taylor local:19 = physical_condition night-two)
@123  [state:20] → [state:55]   (taylor local:20 = log_entries_episode 8→9)
@129  [state:2]  → [state:30]   (elder local:2 = knowledge.hightower-file-channel)
@133  [state:22] → [state:57]   (taylor local:22 = knowledge.messenger-to-elder)
@137  [state:3]  → [state:31]   (elder local:3 = location market-side-junction→writing-room)
@139  [state:4]  → [state:32]   (elder local:4 = formal-record-status)
@142  [state:23] → [state:58]   (taylor local:23 = knowledge.formal-account-sealed)
@145  [state:24] → [state:59]   (taylor local:24 = log_entries_episode 9→10)
@155  [state:25] → [state:60]   (taylor local:25 = stats.fauna 500→600)
@162  [state:26] → [state:61]   (taylor local:26 = knowledge.record-discipline-state)
