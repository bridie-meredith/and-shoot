# Pass 5 Continuity Audit — chapter-08 — The Maester's Report

```yaml
audit:
  scope: episode
  target: chapter-08 (proto-lines main + interlude, iter3/post-restructure)
  pass: 5 — continuity (fresh-fork independent)
  file_level: FAIL
  faults: 4
  flags: 1
```

## FAULTS

### FAULT-CONTINUITY-001 — raven withdrawal post-postern-exit
IDs 89-94: Taylor exits great-hall passage → reaches postern gate → exits postern gate → takes road → pins palms → withdraws raven. Raven inside recorder's room (per ID 96 lift). Taylor on road outside castle walls at withdrawal. No location card establishes road-to-recorder distance within 600m. Stone walls intervene.

**Criteria:** reorder IDs 94-95 to precede ID 91 (postern exit) so withdrawals occur while Taylor still inside walls; OR create loc-harrenhal-interior card placing road within 600m. Project policy favors reorder.

### FAULT-CONTINUITY-002 — fly withdrawal post-postern-exit
ID 95: same problem as 001, with fly inside great hall at withdrawal. Great hall structurally deeper inside Harrenhal than recorder's room.

**Criteria:** same reorder.

### FAULT-CONTINUITY-003 — missing raven deployment initiation
IDs 29-31: Taylor exits side chamber (29) → reaches passage (30) → raven drops the head in recorder's room (31). No initiation beat between 30 and 31. Cost markers at 42-45 are present but causally unsupported without a documented initiation.

**Criteria:** insert beat between 30 and 31 recording Taylor directing the raven into the recorder's room.

### FAULT-CONTINUITY-004 — raven cause-effect severed
IDs 94-96: raven withdrawn (94) → fly withdrawn (95) → raven lifts (96). Lift (96) is the consequence of withdrawal (94); fly withdrawal sits between cause and effect.

**Criteria:** ID 96 must immediately follow ID 94. Fix folded into the reorder for FAULT-001/002.

## FLAG

### FLAG-CONTINUITY-001 — no Harrenhal interior location card
Root cause of FAULT-001/002. Advisory for margit. Per project policy "restructure to fit constraint" the reorder closes the faults without requiring a card patch.

## PASS items

All other continuity dimensions verified clean: ch07→ch08 boundary, maester transit (side chamber → great hall), letter-case prop entry chain (interlude 35-41), Bracken dual-action (recorder + hall), Celtigar climax dual-POV consistency, ch08→ch09 boundary, time consistency, POV (main + interlude), interior movement reachability, fauna ranges within walls.
