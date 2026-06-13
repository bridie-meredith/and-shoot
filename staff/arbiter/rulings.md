# Arbiter — rulings log

Append-only audit trail. Every judge verdict and every arbiter ruling gets one entry.

- **JUDGE** entries: `<ts> JUDGE <contest-id> winner=<label> margin=<...> flags=[...] → <scorecard path>`
- **RULE** entries: the full `ARBITER RULE` block (dispute-id, ruling, standard, rationale, confidence).

Design-inherent dispositions (DEC-0115 circuit breaker) are tracked here with a running consecutive count per defect class.

---

(empty — first ruling pending.)
