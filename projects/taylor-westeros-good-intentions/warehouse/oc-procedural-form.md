---
name: oc-procedural-form
class: prop
scope: library
world: planetos
portability: portable
origin: authored
quality: scant
references:
  - oc-magistrate-hall
---

# The Procedural Form — Pre-Inscribed Verdict Form, Magistrate's Hall Proceeding

## Physical Description

A single sheet of ward-administrative paper stock with a pre-printed or pre-ruled columnar format: charge field, accused name field, evidence notation field, and verdict field. The form is pre-inscribed — the verdict field contains a written entry before the accused finishes speaking. This is not an anomaly in the proceeding's internal logic; the form is designed to be completed in sequence, and the magistrate completes it in sequence at a pace that does not match the proceeding's verbal timing.

## Affordances / Uses

- **Proceeding record.** The official document of the proceeding's outcome. When the proceeding closes, the form is the record that a charge was heard and a verdict rendered.
- **Verdict-before-speech instrument (b01c13 s02 @13).** The magistrate writes the procedural form while Aldric speaks. The writing precedes the completion of the verbal testimony — the verdict is already on the page while the accused is mid-sentence. This is the form's operative function in the scene: it demonstrates that the proceeding is record-production, not deliberation.
- **Single-scene function.** Present only at the magistrate-hall proceeding in b01c13 s02.

## Sensory Hooks

- Fresh ink on the verdict line — written moments ago, not yet fully dry
- The scratch of the quill audible to anyone in the room during the writing

## Portability

Portable. In the magistrate's possession at the table during proceedings.

## Carry State

On the magistrate's table during the proceeding. Removed with the session's document packet at close.

## Functional State

- `content_state`: `partial-to-complete` (verdict field filled before accused finishes speaking; b01c13 @13)
- `location`: `magistrate's table, magistrate-hall`
