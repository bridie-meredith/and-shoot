scene-map: s01e01
generated: 2026-05-13
source: derived from tensometer-s01e01.md + location-state.md + interest-narrator.md + proto-lines/s01e01.md
auto-derived: false
note: hand-authored at /and-wrap dogfood for s01e01 (URI-WRAP-V2 second-run after s01e02). Scene boundaries lifted from active-project/staff/stitcher/render-log-s01e01.md §"Phase 0 — validate + load" (13 named scenes A-N with G skipped — the render's F-fork rendered both lord's-man beats @72-79 and Taylor's log @81-83 as one continuous fork; the @80 proto-line blank-line is internal to F-as-rendered). Tens-aware fields derived from active-project/theater/s01e01-archive/facets/tensometer-s01e01.md. Locations derived from location-state.md plurality + render-log's narrated scene focus. Future /and-facets re-runs would auto-derive this file at Phase 4d per schemas/scene-map.schema.md.
total-scenes: 13
total-bones: 146
---

scene-A @1-@23 | loc-tanner-village | morning | wake; tanner-mother sets bowl; tanner-father verdict-shift; door-swing rupture; log
  rhythm-shape: rising-to-peak
  peak-bones: @7=2, @11=2, @13=2, @14=2, @15=3
  peak-shadow-bones: @6, @8, @10, @12, @16
  fusion-eligible-runs: @1-@5, @17-@23
  protected-patterns: log-trio @21-@23

scene-B @25-@34 | loc-tanner-village | morning | yard-map perimeter sweep with doubled-walk; log
  rhythm-shape: flat-low
  peak-bones: none
  peak-shadow-bones: none
  fusion-eligible-runs: @25-@34
  protected-patterns: doubled-walk @28+@30, log-trio @32-@34

scene-C @36-@46 | loc-tanner-village | midday | mother's afternoon bowl; three-note song; cessation peak; mother turns to wall
  rhythm-shape: rising-to-peak
  peak-bones: @42=2, @43=3
  peak-shadow-bones: @41, @44
  fusion-eligible-runs: @36-@40
  protected-patterns: three-note-buildup @39-@41

scene-D @48-@61 | loc-tanner-village | afternoon | father assigns yard-edge task; routing-countdown twice; Taylor stills; log
  rhythm-shape: flat-low
  peak-bones: none
  peak-shadow-bones: none
  fusion-eligible-runs: @48-@61
  protected-patterns: countdown-rhythm @49-@50, countdown-rhythm @56-@57, log-trio @59-@61

scene-E @63-@70 | loc-tanner-village | before-sundown | reeve enters yard; reeve speaks to father; reeve exits
  rhythm-shape: flat-low
  peak-bones: @66=2
  peak-shadow-bones: @65, @67
  fusion-eligible-runs: @63-@64, @68-@70
  protected-patterns: none

scene-F @72-@83 | loc-tanner-village | before-sundown | lord's-man arrival at parade beat; record-book entry; rupture; Taylor's log (CUT at render)
  rhythm-shape: peak-and-release
  peak-bones: @74=2, @75=3, @76=2
  peak-shadow-bones: @73, @77
  fusion-eligible-runs: @72-@73, @78-@79, @81-@83
  protected-patterns: log-trio @81-@83

scene-H @85-@96 | loc-tanner-village | next-morning | elder routes Taylor to King's Landing; gate-cross; departure-trio; road
  rhythm-shape: double-peak
  peak-bones: @86=3, @87=2, @89=2, @90=3
  peak-shadow-bones: @85, @88, @91
  fusion-eligible-runs: @92-@96
  protected-patterns: threshold-cross @90, departure-trio @91-@93, road-walk-pair @95-@96

scene-I @98-@107 | loc-flea-bottom-base | morning | KL alley mouth; first cardinal-quartet of fauna spread; pack-set in upper room; log
  rhythm-shape: flat-low
  peak-bones: none
  peak-shadow-bones: none
  fusion-eligible-runs: @98-@107
  protected-patterns: cardinal-quartet @99-@101, log-trio @105-@107

scene-J @109-@118 | loc-flea-bottom-base | morning | first perimeter walk; maester upstairs speaks to room; beetles relay sound; log
  rhythm-shape: flat-mid
  peak-bones: @111=2, @112=2, @113=2
  peak-shadow-bones: @110, @114
  fusion-eligible-runs: @115-@118
  protected-patterns: relay-trio @111-@113, log-trio @116-@118

scene-K @120-@127 | loc-flea-bottom-base | midday | full perimeter; cardinal-quartet of fauna relays; three-beat anaphora on corners; log
  rhythm-shape: flat-low
  peak-bones: none
  peak-shadow-bones: none
  fusion-eligible-runs: @120-@127
  protected-patterns: cardinal-quartet @121-@124, log-trio @125-@127

scene-L @129-@137 | loc-flea-bottom-base | evening | maester crosses room; beetles relay footfall; maester laughs; beetles fall silent; log
  rhythm-shape: rising-to-peak
  peak-bones: @131=2, @134=3
  peak-shadow-bones: @130, @132, @133, @135
  fusion-eligible-runs: @136-@137
  protected-patterns: doubled-register-laugh-and-silence @133-@134, log-trio @135-@137

scene-M @139-@146 | loc-flea-bottom | evening | Watch crosses Fish Gate margin off-cadence; dock-runner appears, pivots, leaves; Taylor holds
  rhythm-shape: peak-and-release
  peak-bones: @139=2, @140=3, @141=2, @142=2
  peak-shadow-bones: @143
  fusion-eligible-runs: @144-@146
  protected-patterns: none

scene-N @148-@159 | loc-flea-bottom | evening | elder brings dock-runner back; Taylor speaks to dock-runner — first irreversible commit in KL; log close
  rhythm-shape: peak-and-release
  peak-bones: @148=2, @149=2, @150=2, @151=3, @152=2
  peak-shadow-bones: @153
  fusion-eligible-runs: @154-@159
  protected-patterns: three-note-buildup @148-@150, log-trio @157-@159

---
coverage: 146/146 bones in exactly one scene
gaps: none
overlaps: none
note: scene-label G skipped — render-log fused lord's-man beats (@72-79) and Taylor's log beats (@81-83) into one F-fork. Schema permits non-monotonic alphabetic labels as SIGNAL-only (WARN-SCENE-MAP-LABEL-ORDER). Label preserved to keep render-log traceability.
