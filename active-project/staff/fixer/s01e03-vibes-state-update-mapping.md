# s01e03 Vibes — State-Update licensed-by Token Mapping
# Built for flag-014 (CON-001) remediation
# Maps per-slice-prefixed state-update-<slug>:N → canonical state-update:<consolidated-N>

## Mapping table

state-update-taylor-hebert-flea-bottom:1  → state-update:36
state-update-taylor-hebert-flea-bottom:2  → state-update:37
state-update-taylor-hebert-flea-bottom:3  → state-update:38
state-update-taylor-hebert-flea-bottom:4  → state-update:39
state-update-taylor-hebert-flea-bottom:5  → state-update:40
state-update-taylor-hebert-flea-bottom:6  → state-update:41
state-update-taylor-hebert-flea-bottom:7  → state-update:42
state-update-taylor-hebert-flea-bottom:8  → state-update:43
state-update-taylor-hebert-flea-bottom:9  → state-update:44
state-update-taylor-hebert-flea-bottom:10 → state-update:45
state-update-taylor-hebert-flea-bottom:11 → state-update:46
state-update-taylor-hebert-flea-bottom:12 → state-update:47
state-update-taylor-hebert-flea-bottom:13 → state-update:48
state-update-taylor-hebert-flea-bottom:14 → state-update:49
state-update-taylor-hebert-flea-bottom:15 → state-update:50
state-update-taylor-hebert-flea-bottom:16 → state-update:51
state-update-taylor-hebert-flea-bottom:17 → state-update:52
state-update-taylor-hebert-flea-bottom:18 → state-update:53
state-update-taylor-hebert-flea-bottom:19 → state-update:54
state-update-taylor-hebert-flea-bottom:20 → state-update:55
state-update-taylor-hebert-flea-bottom:21 → state-update:56
state-update-taylor-hebert-flea-bottom:22 → state-update:57
state-update-taylor-hebert-flea-bottom:23 → state-update:58
state-update-taylor-hebert-flea-bottom:24 → state-update:59
state-update-taylor-hebert-flea-bottom:25 → state-update:60
state-update-taylor-hebert-flea-bottom:26 → state-update:61
state-update-taylor-hebert-flea-bottom:27 → state-update:62

state-update-oc-tanner-elder:1 → state-update:29
state-update-oc-tanner-elder:2 → state-update:30
state-update-oc-tanner-elder:3 → state-update:31
state-update-oc-tanner-elder:4 → state-update:32

state-update-oc-tanner-father:1 → state-update:33
state-update-oc-tanner-father:2 → state-update:34
state-update-oc-tanner-father:3 → state-update:35

state-update-oc-broken-maester:3 → state-update:28
# (original slice had :1=CULLED @74, :2=CULLED @88, :3=@164 documentation_status; only :3 survives in consolidated)

## Per-vibes-entry rewrites in vibes.md

vibes:1  @11  state-update-taylor-hebert-flea-bottom:2 → state-update:37
vibes:2  @15  state-update-taylor-hebert-flea-bottom:2 → state-update:37
             state-update-taylor-hebert-flea-bottom:1 → state-update:36
vibes:3  @22  state-update-taylor-hebert-flea-bottom:4 → state-update:39
             state-update-taylor-hebert-flea-bottom:5 → state-update:40
vibes:4  @114 state-update-taylor-hebert-flea-bottom:17 → state-update:52
vibes:5  @155 state-update-taylor-hebert-flea-bottom:25 → state-update:60
vibes:6  @125 state-update-taylor-hebert-flea-bottom:21 → state-update:56
vibes:7  @125 state-update-taylor-hebert-flea-bottom:25 → state-update:60
             state-update-taylor-hebert-flea-bottom:21 → state-update:56
vibes:8  @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
             state-update-oc-tanner-elder:4 → state-update:32
vibes:9  @42  state-update-taylor-hebert-flea-bottom:10 → state-update:45
             state-update-taylor-hebert-flea-bottom:9 → state-update:44
vibes:10 @42  state-update-taylor-hebert-flea-bottom:10 → state-update:45
vibes:11 @48  state-update-taylor-hebert-flea-bottom:10 → state-update:45
vibes:12 @67  state-update-oc-tanner-elder:1 → state-update:29
vibes:13 @68  state-update-oc-tanner-elder:1 → state-update:29
             state-update-taylor-hebert-flea-bottom:12 → state-update:47
vibes:14 @71  state-update-oc-tanner-elder:1 → state-update:29
             state-update-taylor-hebert-flea-bottom:12 → state-update:47
vibes:15 @90  state-update-oc-broken-maester:3 → state-update:28
vibes:16 @90  state-update-oc-broken-maester:3 → state-update:28
vibes:17 @93  (no state-update-* tokens; proto: and tens: only — no change)
vibes:18 @94  state-update-oc-broken-maester:3 → state-update:28
             state-update-taylor-hebert-flea-bottom:14 → state-update:49
vibes:19 @98  state-update-oc-tanner-father:2 → state-update:34
vibes:20 @98  state-update-oc-tanner-father:2 → state-update:34
vibes:21 @100 state-update-oc-tanner-father:2 → state-update:34
vibes:22 @108 state-update-oc-tanner-father:2 → state-update:34
             state-update-oc-tanner-elder:1 → state-update:29
vibes:23 @129 state-update-oc-tanner-elder:2 → state-update:30
vibes:24 @139 state-update-oc-tanner-elder:4 → state-update:32
vibes:25 @133 state-update-taylor-hebert-flea-bottom:22 → state-update:57
vibes:26 @143 state-update-taylor-hebert-flea-bottom:23 → state-update:58
vibes:27 @139 state-update-oc-tanner-elder:2 → state-update:30
             state-update-oc-tanner-elder:4 → state-update:32
vibes:28 @125 state-update-taylor-hebert-flea-bottom:21 → state-update:56
             state-update-taylor-hebert-flea-bottom:25 → state-update:60
vibes:29 @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
vibes:30 @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
vibes:31 @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
             state-update-oc-broken-maester:3 → state-update:28
vibes:32 @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
vibes:33 @162 state-update-taylor-hebert-flea-bottom:26 → state-update:61
vibes:34 @165 state-update-taylor-hebert-flea-bottom:26 → state-update:61
             state-update-taylor-hebert-flea-bottom:27 → state-update:62
