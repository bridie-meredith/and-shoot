---
name: oc-fish-account-ledger
class: prop
scope: library
world: planetos
portability: portable
origin: authored
quality: scant
references:
  - oc-hook-upper-provisioning
---

# The Fish-Account Ledger — Household-Agent's Tally, Salt-Fish Supply Account

## Physical Description

A small bound ledger, worn at the spine from regular use. The pages carry columnar tally-entries: delivery date, supplier name or mark, crate-count, weight-or-quality notation, and the margin figure the household-agent records as the settled account total. The columns are pre-ruled; the entries are in a neat working hand, consistent with someone who produces this document multiple times per week.

## Affordances / Uses

- **Supply-chain accounting instrument.** Records each delivery transaction for the household's salt-fish supply account. Used by the household-agent to settle accounts with suppliers at the provisioning platform. The ledger's record is the authoritative figure in any account dispute — the supplier's word against the ledger's column.
- **Coercion instrument (margin-coercion mechanism).** The agent's ability to record a reduced crate-count or quality deduction that the supplier cannot verify at point-of-transaction makes the ledger the structural tool of the copper-margin coercion. The ledger closes the account on the agent's terms.
- **Single-scene function (b01c13 s01 @5/@7).** Present during the salt-fish delivery transaction; the household-agent tallies and then drops the shoulders at account-close. Not a recurring prop beyond this scene's function.

## Sensory Hooks

- Dried brine on the ledger cover from prior handling during deliveries
- The slight resistance of pages opened to a marked position mid-ledger

## Portability

Portable. Carried by the household-agent; not fixed to the provisioning platform.

## Carry State

Carried by the household-agent at the provisioning platform during delivery windows.

## Functional State

- `content_state`: `in-use` (active tally-ledger for the current supply period)
- `location`: `household-agent possession` at the provisioning platform during transactions
