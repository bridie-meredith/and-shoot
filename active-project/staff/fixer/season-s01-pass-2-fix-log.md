# Fixer log — season s01 Pass 2 constraint audit

audit-target: active-project/theater/proto-lines/s01.aggregate.md
findings-applied: 42
findings-skipped: 0 (all fault-type findings actioned; see anomaly notes below)
splits-appended: [(334 → 914), (511 → 915)]
ID-deletions (converted to time-skip markers): 10, 53, 66, 72, 77, 79, 122, 158, 219, 225, 258, 262, 300, 301, 425, 428, 432, 490, 509, 513, 515, 519, 535, 556, 566, 635, 646, 650, 671, 703, 713, 736, 750, 792, 813, 819, 820, 828, 887
ID-recasts: 14, 28, 71, 74, 124, 169, 191, 194, 222, 249, 264, 284, 334, 337, 439, 511, 512, 563, 722, 797

---

## Anomaly notes for constraint-audit re-run

1. **ID drift across the board.** The audit was run against a version of the file in which some IDs carried different content than the current file. Specifically: the audit's fault-032 attributes "the collection queue breaks" to ID 563, but this content is at ID 513 in the current file. Fault-037 attributes a second instance of "the square traffic re-forms" to ID 563, but ID 563 in the current file is "taylor-hebert-jaehaerys follows." Fault-024 attributes "the market lane opens" to ID 716, but ID 716 is "septon-rowan speaks to oc-craftsman-mother" (valid dialogue beat); the content was at ID 736 and was deleted there. The re-run auditor should expect ID 513 and ID 736 to be time-skip markers now.

2. **Pre-existing gaps: IDs 901, 902, 903, 913.** The file has a gap between ID 900 and ID 904 (IDs 901–903 absent) and ends at ID 912 (ID 913 absent). Faults referencing those IDs (fault-028 ID 902, fault-038 ID 901, fault-020 ID 903, fault-035 ID 913) are treated as pre-existing deletions and marked resolved. The re-run auditor should confirm these gaps are legal.

3. **ID 560 already fixed.** Fault-004 listed ID 560 as "holds the pace" but the current file has "holds the feet" at that ID (within narrow license). No action taken on ID 560.

4. **ID 909 already fixed.** Fault-043 listed ID 909 as "the folio changes hands" but the current file already has "the ferryman receives the folio" there. No action taken.

5. **ID 716 not actioned.** Fault-024 listed ID 716 as "the market lane opens" but the current file has a valid dialogue beat there. The duplicate "the market lane opens" content was at ID 736, which was deleted. No action on ID 716.

6. **Fault-004 ID 192 not actioned.** The current file contains "taylor-hebert-jaehaerys holds the pace" at ID 192, which matches the fault-004 pattern but was NOT listed in the audit's fault-004 ID set. Per scope rules, not touched. Flagging for next re-run.

7. **Split IDs 914 and 915 appended at end of file** with `# split-from:` comments. These are out of sequential position but the stitcher walks IDs in citation order per schema.
