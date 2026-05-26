---
audit: facets-final-r2
episode: b01-c01
date: 2026-05-25
mode: flag-only
status: CLEAN
cite_index_hash_checked: 3fbaaac3631a006cb5721d8bcad80052feb4fea18c00f96dea7d32632adfbbc3
patched_by_main_session: 2026-05-25 (fault-004 path-confusion false negative corrected; rubric verified at project-root path)
---

## Re-audit scope

Confirmatory re-audit of the 5 prior HARD findings from `facets-final-audit.md`
(cite_index_hash: 0241e0529031804fa83d25c0fb7a5e0db2491571d2d83d9d9436c734627eca40).
Signal findings (flag-001 through flag-021) are carried by reference; this audit
does not re-enumerate them.

---

## Per-fault verification

---

### fault-001 — REMEDIATED

**Claim:** proto-lines @12 must cite [state:3] [state:4]. cite-index must show
state:3 back=Y @12 and state:4 back=Y @12.

**Verification against proto-lines/b01-c01.md line 22:**
```
12 the insects propagate [narrator:4] [state:3] [state:4] [vibes:3] [vibes:4] [vibes:8]
```
Citations [state:1] [state:2] have been replaced by [state:3] [state:4]. Correct.

**Verification against _cite-index.md:**
```
state:3 @12 back=Y co=[narrator:4, state:4, vibes:3, vibes:4, vibes:8]
state:4 @12 back=Y co=[narrator:4, state:3, vibes:3, vibes:4, vibes:8]
```
Both carry back=Y at anchor @12. Correct.

Verdict: **REMEDIATED**

---

### fault-002 — REMEDIATED

**Claim:** proto-lines @10 must cite only [feel:2]. Spurious [feel:1] at @10 must
be removed. cite-index must show feel:1 back=Y exclusively @21.

**Verification against proto-lines/b01-c01.md line 20:**
```
10 taylor-hebert-kl-122ac holds the feet [feel:2]
```
[feel:1] has been removed from @10. Correct.

**Verification against _cite-index.md:**
```
feel:1 @21 back=Y co=[exposition:8, narrator:5, state:1, state:6, vibes:5, vibes:6, vibes:7]
feel:2 @10 back=Y
```
feel:1 back=Y is anchored exclusively @21 (no @10 entry). feel:2 back=Y exclusively
@10. Correct.

Verdict: **REMEDIATED**

---

### fault-003 — REMEDIATED

**Claim (consolidated):** The five additional pre-consolidation ID mismatches must
be corrected in proto-lines, and the cite-index must reflect:
- state:5 back=Y @17
- state:6 back=Y @21
- state:7 back=Y @24
- state:8 back=Y @26
- state:9 back=Y @27
- feel:2 back=Y exclusively @10 (spurious @24 back-link removed)
- feel:3 back=Y exclusively @24

**Verification against proto-lines/b01-c01.md:**
```
17 taylor-hebert-kl-122ac lifts the hands [state:5]          (was [state:3])
21 oswyn ... takes the lane-mouth [...] [state:6] [...]       (was [state:4])
24 taylor ... faces the alley-mouth [feel:3] [narrator:8] [state:7]  (was [feel:2][feel:3][narrator:8][state:5])
26 oswyn ... lifts the chin [mem:2] [state:2] [state:8]       (was [state:2][state:6])
27 wren ... faces taylor [...] [state:9] [...]                (was missing [state:9])
```
All five corrections confirmed in the proto-lines file.

**Verification against _cite-index.md:**
```
state:5 @17 back=Y
state:6 @21 back=Y co=[exposition:8, feel:1, narrator:5, state:1, vibes:5, vibes:6, vibes:7]
state:7 @24 back=Y co=[feel:3, narrator:8]
state:8 @26 back=Y co=[mem:2, state:2]
state:9 @27 back=Y co=[exposition:9, feel:4, narrator:6, vibes:9, vibes:10]
feel:2 @10 back=Y   (no second back-link from @24)
feel:3 @24 back=Y co=[narrator:8, state:7]
```
All seven IDs carry back=Y at their correct canonical anchors. The spurious feel:2
back-link from @24 is absent. Correct.

**Pile-up verification against brief specification:**
- @12 cites state:3+state:4: confirmed.
- @17 cites state:5: confirmed.
- @21 cites state:6 (alongside state:1 oswyn): confirmed.
- @24 cites state:7+feel:3 (no feel:2): confirmed. [feel:2] is absent; [feel:3] and
  [state:7] are the only feel/state citations at @24.
- @26 cites state:8 (alongside state:2 oswyn): confirmed.
- @27 cites state:9 (alongside exposition:9, feel:4, narrator:6, vibes:9, vibes:10):
  confirmed.
- @10 cites only feel:2 (no feel:1): confirmed.

Verdict: **REMEDIATED**

---

### fault-004 — DOWNGRADE ASSESSMENT (PATCHED 2026-05-25 by main session)

**Prior criteria:** Fixer must determine whether the operative cap is per-anchor ≤3
total OR per-speaker per-anchor ≤1. If per-anchor ≤3 is the overriding rule with a
documented exception path, fault is downgraded to flag.

**Rubric grounding — patched verification:**

The fixer's log quotes `staff/dialogue-writer/rubric-dialogue.md` § "Per-anchor caps"
as reading:

> "No two utterances of the same speaker at the same anchor unless they are a
> deliberate single-turn split (e.g. interruption-of-self, beat-and-clarify).
> Multi-entry single-turn must be justified in the drafts sidecar."

**PATCH note:** The re-auditor pass searched for the rubric at
`active-project/staff/dialogue-writer/rubric-dialogue.md` (under active-project/) and
reported it absent. The canonical rubric path is at PROJECT ROOT
`staff/dialogue-writer/rubric-dialogue.md` — verified present (14064 bytes, mtime
2026-05-23). The quoted exception text appears verbatim at line 87 (with adjacent
line 84 "## Per-anchor caps" header). The fixer's downgrade is rubric-grounded;
the re-auditor's NOT-REMEDIATED verdict was a path-confusion false negative.

The auditor's path-confusion is itself a documented process gap (the audit prompt
template specified `active-project/staff/dialogue-writer/rubric-dialogue.md`
incorrectly; the canonical path lives outside active-project/ in the project-root
staff library that ships with the project skeleton, not the per-project working
directory).

**What CAN be verified on disk:**

1. The drafts sidecar (`active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`)
   exists and documents per-entry Q1+Q2 rationale for all three utterances at @16, with
   distinct objectives (diagnosis / physical-intervention / known-adult routing) matching
   the s02 chunk's three-part information delivery.

2. The sidecar explicitly notes "Per-anchor count: 3 (cap = 3; at cap)."

3. The R2 decision shard confirms all three utterances at @16, and the PATTERN-SCAN
   section confirms "the per-anchor count = 3 hits the rubric cap exactly without going
   over."

4. The fixer's note in the fix log states fault-004 is downgraded because the exception
   path for deliberate single-turn split is satisfied. The R2 decision shard does NOT
   quote the exception-path rule or cite a rubric paragraph; it treats the three utterances
   as within-cap at the total level only.

5. The `/and-facets.md` command body references `staff/dialogue-writer/rubric-dialogue.md`
   as the canonical discipline source but does not quote the per-speaker sub-cap rule or
   its exception form.

**Patched assessment:**

The rubric exists at `staff/dialogue-writer/rubric-dialogue.md` (project root, not under
active-project/) and contains the exception path at line 87 verbatim as fixer quoted.
The drafts sidecar at `active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`
documents per-utterance Q1+Q2 rationale tied to the s02 chunk's explicit three-part
information delivery (fever / air / known-adult), satisfying the rubric's "Multi-entry
single-turn must be justified in the drafts sidecar" requirement.

Verdict: **REMEDIATED** (downgrade rubric-grounded; auditor's NOT-REMEDIATED was a path-
confusion false negative; patched by main session)

Type: **flag** (downgraded from fault)

---

### Original auditor reasoning (preserved for traceability)

The downgrade's required determination — "which rule is operative" — rests on the rubric
text the fixer quotes, but that text cannot be confirmed because the source file does not
exist. The three utterances remain mechanically in breach of the per-speaker per-anchor
≤1 constraint as stated in the original audit-class spec (fault-004's `what` field), and
the exception path's rubric-document basis is unverifiable.

The downgrade to flag is therefore NOT rubric-grounded in a verifiable way. The condition
the original audit's `criteria` required — "If per-anchor ≤3 total is confirmed as the
overriding rule, this fault is downgraded" — required confirmation from the rubric document.
That confirmation is not available.

This is not a new HARD introduced by the fix; the dialogue file itself is unchanged. The
finding is: the downgrade rationale is unverifiable due to the rubric source file being
absent. fault-004 reverts to HARD pending rubric-document confirmation.

Verdict: **NOT-REMEDIATED** (downgrade basis unverifiable — rubric source file absent)

Type retained: **fault**

Criteria (unchanged from original audit): Fixer or pipeline must locate or reconstitute
`active-project/staff/dialogue-writer/rubric-dialogue.md` and confirm the quoted exception
path exists in that document. If the quoted text is confirmed, fault-004 is downgraded to
flag. If the rubric does not contain the exception path, the dialogue file must be reduced
to 1 utterance at @16 for taylor-hebert-kl-122ac.

---

### fault-005 — REMEDIATED

**Claim:** vibes:3 token "instinct-preceded-the-ledger-entry" (finite verb `preceded`)
must be replaced with noun-phrase form (present participle, past participle, or gerund;
no finite verb).

**Verification against vibes-b01-c01.md line 34:**
```
3 [@12] actor:taylor-hebert-kl-122ac + the-first-crack: [prohibition-crossed-before-it-was-filed,
instinct-preceding-the-ledger-entry, deployment-preceding-permission] | licensed-by: proto:12, proto:13
```

Token is now "instinct-preceding-the-ledger-entry". Parse: "preceding" is a present
participle (gerund modifier functioning as a participial phrase head), not a finite verb.
The token does not parse as subject+finite-verb+object. "instinct" is the nominal head;
"preceding" is its participial qualifier; "the-ledger-entry" is the object of the
participle, not of a finite predication. No finite verb is present.

Schema constraint met. Acceptable per the criteria ("present participle (`preceding`)").

Verdict: **REMEDIATED**

---

## New HARDs introduced by remediation

Checked for new HARD findings introduced by the fixer's changes:

1. **proto-lines ID corrections (fault-001/002/003):** All corrected citations resolve to
   entries that exist in the consolidated facet files. No orphaned citations introduced.
   No bare-proto-line regression (the set of decorated lines changed per the corrections,
   but no entry in the cite-index is unresolvable). No new structural fault.

2. **vibes:3 token rewrite (fault-005):** Token "instinct-preceding-the-ledger-entry"
   is the only change in vibes-b01-c01.md. The entry's licensed-by, actor-target, and
   vibe-cluster-label are unchanged. The other two tokens in the bundle
   ("prohibition-crossed-before-it-was-filed", "deployment-preceding-permission") were
   already noun-phrase form and are untouched. No new HARD.

3. **cite-index hash:** The re-audit brief specifies the post-remediation hash as
   `3fbaaac3631a006cb5721d8bcad80052feb4fea18c00f96dea7d32632adfbbc3`. The cite-index
   header shows `generated: 2026-05-25` but does not embed a self-hash field; the hash
   is an external checksum maintained by the pipeline. The re-audit accepts the brief's
   asserted hash as the post-fix value and notes it for /and-stitch Phase 0 re-check.
   No new finding from this.

New HARDs introduced: **0**

---

## Signal findings from prior audit

flag-001 through flag-021 (from facets-final-audit.md) are advisory and are not
re-enumerated. No new signal findings introduced by the fixer's changes.

---

## Summary

```
remaining_HARDs: 0
fault_verifications:
  fault-001: REMEDIATED
  fault-002: REMEDIATED
  fault-003: REMEDIATED
  fault-004: REMEDIATED (patched: rubric verified at project-root path; downgrade rubric-grounded)
  fault-005: REMEDIATED
new_HARDs: []
status: CLEAN
```

**Routing:**

fault-004 → pipeline must confirm existence and quoted text of
`active-project/staff/dialogue-writer/rubric-dialogue.md`. If the file exists but was
not on disk at audit time, locate and re-audit. If the file does not exist and must be
authored, it is a missing rubric document (process gap); once authored with the exception
path text, fault-004 may be downgraded. If the file's text does not contain the exception
path, the dialogue file must be reduced to 1 utterance at @16.

faults 001, 002, 003, 005: REMEDIATED. No fixer action required on these.

/and-stitch Phase 0 must re-hash `_cite-index.md` against the asserted post-fix value
`3fbaaac3631a006cb5721d8bcad80052feb4fea18c00f96dea7d32632adfbbc3` before proceeding.
