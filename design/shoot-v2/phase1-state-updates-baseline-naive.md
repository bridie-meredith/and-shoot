---
facet: state-updates
episode: s01e01
phase: 1 (naive baseline, rubric-blind)
author: naive (rubric-blind)
---

1 @1 studio.cart-position: unset -> outside-timber-gate  # rationale: cart placed in scene
2 @2 prop:oc-banner.state: unset -> furled-against-crossbar  # rationale: banner described in placed state
3 @3 prop:oc-horse.state: unset -> hitched-to-traces  # rationale: horse positioned
4 @4 studio.beetle-seam: unset -> held  # rationale: beetles holding seam
5 @5 actor:mira-stonefield.holding: bucket -> none  # rationale: mira sets bucket down
6 @5 prop:oc-bucket.location: mira-hand -> flagstone  # rationale: bucket transferred to ground
7 @6 actor:mira-stonefield.posture: bent -> straight  # rationale: mira straightens
8 @7 actor:mira-stonefield.speech-target: none -> yard  # rationale: mira speaks
9 @8 actor:edric-cray.gaze-target: unset -> road-past-cart  # rationale: edric fixes gaze
10 @9 actor:clerk.holding: rolled-parchment -> unrolled-parchment  # rationale: clerk unrolls
11 @9 prop:oc-parchment.state: rolled -> unrolled  # rationale: parchment opened
12 @10 actor:clerk.attention-target: none -> yard-count  # rationale: clerk counts yard
13 @11 actor:census-officer.location: outside-gate -> inside-yard  # rationale: officer enters
14 @12 actor:census-officer.location: gate -> yard-center  # rationale: officer crosses to center
15 @13 actor:census-officer.speech-target: none -> yard  # rationale: officer addresses yard
16 @14 actor:taylor-hebert-westeros.location: yard-edge -> packed-dirt-traverse  # rationale: taylor moves
17 @15 actor:taylor-hebert-westeros.in-line: false -> true  # rationale: taylor enters line
18 @16 actor:mira-stonefield.proximity-to-taylor: distant -> elbow-touching  # rationale: mira beside taylor
19 @17 actor:clerk.holding: parchment -> ledger-on-board  # rationale: clerk shifts to ledger
20 @17 prop:oc-ledger.balance: unset -> on-board-against-hip  # rationale: ledger positioned
21 @18 prop:oc-ledger.top-line: blank -> name-recorded  # rationale: name on ledger
22 @19 actor:taylor-hebert-westeros.motion: walking -> stopped  # rationale: taylor stops
23 @20 actor:census-officer.activity: standing -> working-line  # rationale: officer begins work
24 @21 actor:census-officer.speech-target: yard -> each-ward  # rationale: officer addresses individuals
25 @22 prop:oc-stylus.activity: idle -> following-dictation  # rationale: stylus moving
26 @23 actor:census-officer.gaze-target: line -> taylor  # rationale: officer fixes on taylor
27 @24 prop:oc-stylus.activity: writing -> stopped  # rationale: stylus halts
28 @25 actor:census-officer.face-orientation: unset -> level-with-taylor  # rationale: officer faces taylor
29 @26 actor:census-officer.speech-target: ward -> taylor  # rationale: officer addresses taylor
30 @27 actor:taylor-hebert-westeros.speech-target: none -> officer  # rationale: taylor responds
31 @28 actor:taylor-hebert-westeros.holding: letter-tucked -> letter-presented  # rationale: taylor presses letter forward
32 @28 prop:oc-letter.position: tucked -> presented-forward  # rationale: letter advances
33 @29 prop:oc-letter.seal-orientation: unset -> facing-officer  # rationale: seal turned
34 @30 prop:oc-stylus.target: blank -> taylor-name  # rationale: stylus moves to name
35 @30 prop:oc-ledger.taylor-entry: blank -> being-written  # rationale: taylor name entered
36 @31 actor:census-officer.face-orientation: taylor -> sept-door  # rationale: officer turns
37 @32 actor:census-officer.speech-target: taylor -> threshold  # rationale: officer addresses door
38 @33 prop:oc-sept-door.state: shut -> shut-confirmed  # rationale: door does not open
39 @34 actor:septon-dying-protector.location: unset -> pallet-with-beetles  # rationale: osmynd on pallet
40 @35 actor:census-officer.weight: forward -> heel-toward-clerk  # rationale: officer shifts weight
41 @36 prop:oc-stylus.target: taylor-name -> line-under-taylor-name  # rationale: stylus moves down
42 @37 actor:taylor-hebert-westeros.location: line-position -> officer-shoulder-path  # rationale: taylor steps into path
43 @38 actor:taylor-hebert-westeros.holding: letter-low -> letter-in-air-front-of-officer  # rationale: taylor presents letter
44 @38 prop:oc-letter.position: presented -> raised-before-officer  # rationale: letter raised
45 @39 actor:taylor-hebert-westeros.feet-set: unset -> blocking-officer-next-pace  # rationale: taylor blocks path
46 @40 actor:census-officer.holding: none -> letter-unfolded  # rationale: officer takes and unfolds
47 @40 prop:oc-letter.state: folded -> unfolded  # rationale: letter opened
48 @41 prop:oc-letter.seal: intact -> broken-at-crease  # rationale: seal breaks
49 @42 prop:oc-letter.state: unfolded -> folded-back  # rationale: officer refolds
50 @43 actor:census-officer.holding: letter -> letter-extended  # rationale: officer offers back
51 @44 prop:oc-letter.location: officer-hand -> taylor-hand  # rationale: letter returns
52 @44 actor:taylor-hebert-westeros.holding: none -> letter  # rationale: taylor receives letter
53 @45 actor:taylor-hebert-westeros.grip: open -> closed-on-letter  # rationale: palm closes
54 @46 actor:census-officer.face-orientation: taylor -> clerk  # rationale: officer turns to clerk
55 @47 actor:census-officer.speech-target: taylor -> clerk  # rationale: officer dictates
56 @48 prop:oc-ledger.taylor-entry: pending -> provisional-labor-eligible  # rationale: status entered
57 @48 actor:taylor-hebert-westeros.status: unregistered -> provisional-labor-eligible  # rationale: official designation
58 @49 actor:taylor-hebert-westeros.holding: letter-closed -> letter-held-still  # rationale: taylor still holds
59 @50 actor:taylor-hebert-westeros.face-orientation: officer -> mira  # rationale: taylor turns
60 @51 actor:taylor-hebert-westeros.speech-target: none -> mira  # rationale: taylor speaks to mira
61 @52 actor:mira-stonefield.gaze-target: taylor -> flagstones  # rationale: mira drops eyes
62 @53 actor:mira-stonefield.gaze-target: flagstones -> flagstones-held  # rationale: mira holds gaze down
63 @54 actor:taylor-hebert-westeros.speech-target: mira -> edric-across-yard  # rationale: taylor calls to edric
64 @55 actor:edric-cray.gaze-target: road -> officer  # rationale: edric looks at officer
65 @56 actor:edric-cray.gaze-target: officer -> taylor  # rationale: edric looks at taylor
66 @57 actor:edric-cray.location: doorway -> through-door-back  # rationale: edric retreats
67 @58 prop:oc-stylus.activity: stopped -> resumed  # rationale: stylus resumes
68 @59 prop:oc-stylus.activity: writing -> resting  # rationale: stylus rests
69 @60 actor:census-officer.foot-angle: unset -> across-taylor  # rationale: officer's foot angled
70 @61 actor:census-officer.speech-target: clerk -> taylor  # rationale: officer addresses taylor
71 @62 prop:oc-stylus.target: ledger -> margin-line  # rationale: stylus to margin
72 @63 prop:oc-stylus.activity: moving -> stopped-at-margin  # rationale: stylus halts
73 @64 prop:oc-ledger.taylor-entry-margin: blank -> two-parallel-lines  # rationale: marks added
74 @65 actor:census-officer.shoulder-orientation: taylor -> gate  # rationale: officer turns toward gate
75 @66 actor:census-officer.speech-target: taylor -> taylor-final  # rationale: officer's last address
76 @67 actor:census-officer.foot-direction: clerk -> horse  # rationale: officer steps toward horse
77 @68 actor:clerk.holding: ledger-open -> board-folded  # rationale: clerk folds board
78 @68 prop:oc-board.state: open -> folded  # rationale: board closes
79 @69 studio.wheel-tremor: present -> departed-east  # rationale: cart leaves
80 @69 studio.beetle-state: held-seam -> verge-east  # rationale: beetles shift
81 @70 actor:taylor-hebert-westeros.face-orientation: yard -> sept-door  # rationale: taylor turns to door
82 @71 actor:taylor-hebert-westeros.location: yard-position -> on-dirt-step  # rationale: taylor steps
83 @72 actor:taylor-hebert-westeros.location: dirt -> stone-step  # rationale: taylor steps to stone
84 @73 actor:taylor-hebert-westeros.location: stone -> in-frame-shadow  # rationale: taylor in shadow
85 @74 actor:taylor-hebert-westeros.grip: closed -> fist-on-letter  # rationale: fist tightens
86 @75 actor:taylor-hebert-westeros.holding: letter-only -> letter-and-latch  # rationale: hand finds latch
87 @75 prop:oc-latch.contact: none -> taylor-hand  # rationale: latch touched
88 @76 prop:oc-latch.state: down -> lifted  # rationale: latch lifts
89 @77 actor:taylor-hebert-westeros.location: threshold -> through-door  # rationale: taylor enters sept
90 @77 prop:oc-sept-door.state: shut -> opened-and-passed  # rationale: door used

## Stats

- Total fires: 90
- Fires-per-77: 90/77 = 1.17 fires per proto-line (compound entries on some beats; near-total coverage)
- Target distribution:
  - actor:* entries: 51
  - studio entries: 4
  - prop:* entries: 35
- Refusal note: I did not find myself wanting to refuse — every line with a verb felt like it could plausibly be read as a transition, including atmospheric ones like the beetles holding the seam, so I fired on nearly everything.
