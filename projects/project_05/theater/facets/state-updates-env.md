facet: state-updates
scope: environmental
episode: s01e03
author: studio (env R1 fresh fork)
---
# source: state-updates-env

# Field-extension register
#
# The following OC prop slugs are introduced in this episode as oc-* field extensions.
# No formal prop cards exist in cards/props/ for any of these (INDEX.md confirmed empty).
# Each extension is documented here per rubric §"Field-extension protocol".
#
# oc-record-book-market-junction  — the clerk's official record book at the market-side junction;
#   fields: physical_condition (open/closed), clerk-1-entry (absent/dictated), position (location)
#   # field-extension: new OC prop, first-touch this episode; clerk-1 scene track
#
# oc-taylor-log                   — Taylor's personal working log; held and carried by Taylor;
#   fields: physical_condition (open/closed)
#   # field-extension: new OC prop, first-touch this episode; recurs every log scene
#
# oc-record-book-apothecary       — the apothecary's record book used by clerk-2;
#   fields: physical_condition (open/closed), clerk-2-entry (absent/written), holder (second-clerk/apothecary-surface)
#   # field-extension: new OC prop, first-touch this episode; clerk-2 scene track
#
# oc-coin                         — the coin the elder places into Taylor's palm;
#   fields: holder (oc-tanner-elder/mid-air-between-them/taylor-hebert-flea-bottom)
#   # field-extension: new OC prop, single-scene; load-bearing for the village-claim / coin-transfer turn
#
# oc-maester-pen                  — the broken maester's writing pen;
#   fields: physical_condition (writing/set)
#   # field-extension: new OC prop; tens=3 (@90) reversal-proximity peak; pen-set terminates writing session
#
# oc-elder-account                — the written and sealed account the elder composes and hands to the middleman;
#   fields: physical_condition (blank/written), seal-condition (unsealed/sealed), holder (oc-tanner-elder/middleman)
#   # field-extension: new OC prop; tens=3 (@139) structural climax; institutional state-change on village-claim axis

# ---
# SCENE: first clerk / market-side junction (@3–@13)
# Tens cluster: @7=2, @8=2, @11=3 (stakes-visibility + reversal-proximity peak)
# ---

1 @7 oc-record-book-market-junction.physical_condition: closed -> open

2 @8 oc-record-book-market-junction.clerk-1-entry: absent -> dictated

3 @9 oc-record-book-market-junction.physical_condition: open -> closed

4 @11 oc-record-book-market-junction.position: market-junction -> beyond-Fish-Gate
# cross-facet: tens=3 @11, stakes-visibility + reversal-proximity; record physically exits Taylor's observable range; irreversible

# ---
# SCENE: first log entry / waking dawn (@14–@16)
# Tens cluster: @14=1, @15=1, @16=1 — establishing-entry; first log of episode
# ---

5 @14 oc-taylor-log.physical_condition: closed -> open

6 @16 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: log entry / pre-dawn write (@29–@31)
# Tens cluster: @25=1, @26=2, @27=2 — waking sequence context; log entry anchors dawn surveillance close
# ---

7 @29 oc-taylor-log.physical_condition: closed -> open

8 @31 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: second clerk / apothecary (@33–@45)
# Tens cluster: @39=2, @40=2, @41=1, @42=3 (stakes-visibility peak — irreversible second commit)
# ---

9 @39 oc-record-book-apothecary.physical_condition: closed -> open

10 @40 oc-record-book-apothecary.clerk-2-entry: absent -> written

11 @41 oc-record-book-apothecary.physical_condition: open -> closed

12 @42 oc-record-book-apothecary.holder: second-clerk -> apothecary-surface
# cross-facet: tens=3 @42, stakes-visibility; release is the irreversible sealing of the second commit

# ---
# SCENE: coin transfer / elder–Taylor (@66–@71)
# Tens cluster: @66=2, @67=3, @68=3 (double-peak — elder places coin / Taylor closes fist)
# ---

13 @67 oc-coin.holder: oc-tanner-elder -> mid-air-between-them
# cross-facet: tens=3 @67, stakes-visibility + reversal-proximity; coin leaves elder's possession

14 @68 oc-coin.holder: mid-air-between-them -> taylor-hebert-flea-bottom
# cross-facet: tens=3 @68, body-charge; Taylor's fist closes on coin — double-tap with @67

15 @69 oc-taylor-log.physical_condition: closed -> open

16 @71 oc-taylor-log.physical_condition: open -> closed

# ---
# SCENE: maester writes / sets pen (@87–@94)
# Tens cluster: @89=2, @90=3 (reversal-proximity peak — pen-set terminates session)
# ---

17 @92 oc-taylor-log.physical_condition: closed -> open

18 @94 oc-taylor-log.physical_condition: open -> closed

19 @90 oc-maester-pen.physical_condition: writing -> set
# cross-facet: tens=3 @90, reversal-proximity; discrete termination of pen-scratch session — persistent (maester does not resume within episode)
# field-extension: oc-maester-pen (new OC prop; pen-set is a tracked-state transition, not a momentary motor event; persists through end of observed session)

# ---
# SCENE: overnight network / perimeter walk / Red Keep sighting (@110–@125)
# Tens cluster: @118=2, @119=2, @121=2, @125=2
# Operational-radius advancement: range reaches 600m (episode goal); fires on @125 (facing Red Keep; radius
# confirmed at new ceiling)
# ---

20 @125 studio.fauna_sense_status.operational_radius: 400m -> 600m
# cross-facet: tens=2 @125; operational-radius advancement is persistent and irreversible within the episode;
# @125 is the beat where the Red Keep (400m beyond ceiling) comes into bearing — the radius ceiling is confirmed here

# ---
# SCENE: elder's account / middleman dispatch (@136–@143)
# Tens cluster: @138=2, @139=3 (structural climax — three axes: stakes-visibility + reversal-proximity + body-charge),
# @140=2, @143=2
# ---

21 @138 oc-elder-account.physical_condition: blank -> written

22 @139 oc-elder-account.seal-condition: unsealed -> sealed
# cross-facet: tens=3 @139, three-axis climax; sealing is irreversible; institutional state-change on village-claim axis

23 @140 oc-elder-account.holder: oc-tanner-elder -> middleman

# ---
# SCENE: perimeter circuit / transit (@148–@161)
# Studio location transitions: Taylor exits and re-enters loc-flea-bottom-base
# ---

24 @148 studio.active_location: loc-flea-bottom-base -> in-transit

25 @161 studio.active_location: in-transit -> loc-flea-bottom-base

# ---
# SCENE: denouement log entries (@162–@165)
# Tens cluster: @162=3 (reversal-proximity + body-charge, denouement registration), @163=1, @164=1, @165=1
# ---

26 @163 oc-taylor-log.physical_condition: closed -> open

27 @165 oc-taylor-log.physical_condition: open -> closed
