facet: state-updates-env
episode: b01c06
author: studio
---

# rubric-carve-out — oc-prop field-extensions (SEAM-006/007/008)
#
# design/shoot-v2/rubric-state-updates.md § Field-extension protocol
#
# Carve-out scope: entries on prop:oc-ward-coverage-notes, prop:oc-jarvis-channel-form,
#   prop:oc-accounting-ledger — all three are oc-slug originals with pending margit referrals
#   (SEAM-006, SEAM-007, SEAM-008 from facets_complete block in showrunner memory); no warehouse
#   cards exist yet at authoring time.
# Carve-out rule: per §Field-extension protocol, field-extensions on oc-* props are a soft path
#   when the prop card is pending margit. Each extended field is a tracked-state-aspect (physical
#   state: open/closed/filled/sealed; content: written fields; position: in-hand/set-down/with-courier),
#   not a perception or stylistic flourish. Field-extension comment appended to each first-touch entry.
# Coverage justification: these three props are the exclusive physical substrate of the chapter's
#   central events (the coverage-note omission, the loaded pause, the accounting and send). Refusing
#   all entries on authority-grounds would hollow the ENV state-track entirely for this chapter.
#   Conservative fallback (refuse and flag to margit) is appropriate for subsequent chapters once
#   cards are authored; for this first-touch chapter, oc-slug extension with explicit annotation is
#   the correct path per rubric §Field-extension protocol.
#
# Per-entry annotations (carve-out clause applies to all oc-prop entries below):
#   state:2 @6: prop:oc-ward-coverage-notes — oc-slug, field-extension, first-touch
#   state:3 @7: prop:oc-ward-coverage-notes — oc-slug, field-extension, content-write
#   state:4 @9: prop:oc-ward-coverage-notes — oc-slug, field-extension, state-close
#   state:5 @10: prop:oc-jarvis-channel-form — oc-slug, field-extension, first-touch
#   state:6 @11: prop:oc-jarvis-channel-form — oc-slug, field-extension, state-open
#   state:7 @14: prop:oc-jarvis-channel-form — oc-slug, field-extension, content-fill
#   state:8 @15: prop:oc-jarvis-channel-form — oc-slug, field-extension, position-lower
#   state:9 @16: prop:oc-accounting-ledger — oc-slug, field-extension, first-touch
#   state:10 @17: prop:oc-accounting-ledger — oc-slug, field-extension, content-write
#   state:11 @18: prop:oc-accounting-ledger — oc-slug, field-extension, content-write
#   state:12 @21: prop:oc-accounting-ledger — oc-slug, field-extension, state-close
#   state:13 @22: prop:oc-jarvis-channel-form — oc-slug, field-extension, position-lift
#   state:14 @23: prop:oc-jarvis-channel-form — oc-slug, field-extension, state-seal
#   state:15 @24: prop:oc-jarvis-channel-form — oc-slug, field-extension, holder-transfer
#   state:16 @25: prop:oc-ward-coverage-notes — oc-slug, field-extension, state-reopen
#   state:17 @26: prop:oc-ward-coverage-notes — oc-slug, field-extension, state-close

1 @1 studio.spatial_layout.lane-mouth: clear -> handcart-blocking
2 @6 prop:oc-ward-coverage-notes.state: closed -> open # field-extension: state (new field; first-touch @6; oc-card pending SEAM-006)
3 @7 prop:oc-ward-coverage-notes.contact-role-field: blank -> ward-resident-hook-routine # field-extension: contact-role-field (new field; content-write; written value is the protective notation Taylor chose)
4 @9 prop:oc-ward-coverage-notes.state: open -> closed # field-extension: state carries from @6; entry complete
5 @10 prop:oc-jarvis-channel-form.state: absent -> arrived # field-extension: state (new field; first-touch @10; oc-card pending SEAM-007)
6 @11 prop:oc-jarvis-channel-form.state: arrived -> opened # field-extension: state transitions from arrival to active-read
7 @14 prop:oc-jarvis-channel-form.content: blank -> filled-four-ward-elder-names # field-extension: content (new field; names written; irreversible content change)
8 @15 prop:oc-jarvis-channel-form.position: in-hand -> set-down-unsent # field-extension: position (new field; form lowered without sending; loaded-pause state)
9 @16 prop:oc-accounting-ledger.state: closed -> open # field-extension: state (new field; first-touch @16; oc-card pending SEAM-008)
10 @17 prop:oc-accounting-ledger.content: blank-entry -> ward-elder-names-written # field-extension: content (new field; cost-side names written)
11 @18 prop:oc-accounting-ledger.content: ward-elder-names-written -> ward-elder-names-and-sera-coverage-written # field-extension: content extended; protection-side entry added alongside cost-side
12 @21 prop:oc-accounting-ledger.state: open -> closed # field-extension: state; ledger-board accounting complete and closed
13 @22 prop:oc-jarvis-channel-form.position: set-down-unsent -> in-hand # field-extension: position; form re-lifted for the seal sequence
14 @23 prop:oc-jarvis-channel-form.state: filled -> sealed # field-extension: state; irreversible — sealed for dispatch; the send
15 @24 prop:oc-jarvis-channel-form.holder: taylor-hebert-kl-122ac -> the-courier # field-extension: holder (new field; irrevocable departure from Taylor's possession)
16 @25 prop:oc-ward-coverage-notes.state: closed -> open # field-extension: state; re-opened at contrast moment (omission-contrast @25-@26 peak bone)
17 @26 prop:oc-ward-coverage-notes.state: open -> closed # field-extension: state; chapter close; terminal bone
