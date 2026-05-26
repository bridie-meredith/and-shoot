# Archive: 2026-05-26 b01-c02 facets revise stale-from-rewrite

**Timestamp:** 2026-05-26
**Trigger:** /and-facets b01-c02 anchor-refresh HARD-ABORT after /and-write revise --from-signals re-decomposed chapter 29→47 bones.
**Reason:** All prior facet anchor IDs (@1–29) shifted under the revise; cite-index + facet entries cited dead anchors.

## Contents

- All b01-c02 facet files except `scene-map-b01-c02.md` (which was current — bones-co-emitted at /and-write Phase 7).
- `theater/proto-lines/b01-c02.md` (stale annotated copy).
- `theater/facets/_inflight/` + `_inflight-r2/` from the prior R1+R2 fanouts.
- `staff/auditor/facets-final-audit.md` + `facets-audience-gate-r1.md` from prior c02 audit cycle.
- `staff/dialogue-writer/` (empty for c02 — silent chapter).
- `staff/showrunner/and-facets-b01-c02-summary.md` (if existed).

## Restore command

```bash
cp -rn /home/user/and-shoot/active-project/theater/_archive/2026-05-26T-revise-stale-from-rewrite/* /home/user/and-shoot/active-project/
```

## Re-run target

After this archive, `/and-facets b01-c02` should re-run cleanly against the 47-bone revise.
