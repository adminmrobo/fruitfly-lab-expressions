# 새 식구 동작 시트 — Genspark 지침서 (시아 S1~S15 · 모아 M1~M16 · 미공개 X1~X3)

박사(D)·조수(A)·초파리(F)·주판봇(R) 시트와 **같은 배열·같은 칸 수·같은 화풍**입니다. 시아는 박사 자리(오른쪽), 모아는 조수 자리(왼쪽)를 봅니다.

## 넣는 법 (매번)
- 첨부: 그 캐릭터의 `images/{캐릭터}/E13_neutral.png` + 설정 시트(`refs/original/sia_sheet.png` / `moa_sheet.png`) + 표의 "대응" 시트(방향이 같은 기존 시트 — 배치 참고)
- 앞에 붙일 한국어 한 줄: *"첨부한 첫 두 그림의 캐릭터와 똑같은 얼굴·색·비율로, 세 번째 그림과 같은 칸 배치로, 아래 영어 프롬프트대로 그려 줘. 방향이 가장 중요해."*
- **S1·M1을 먼저** 만들고, 마음에 드는 결과를 이후 시트의 참고 그림으로 함께 넣습니다.
- 파일 이름: `S1_sia.png`, `M16_moa.png`, `X1A_x1.png` (시트번호_캐릭터)

## 시트 목록

| 번호 | 캐릭터 | 내용 | 프레임 | 구간 | 보는 쪽 | 대응 |
|---|---|---|---|---|---|---|
| S1 | 시아 | 기본 A · 서기·걷기 | 8 | idle 1–4, walk 5–8 | 오른쪽 | D1 |
| S2 | 시아 | 기본 B · 점프·돌진 | 8 | jump 1–4, dash 5–8 | 오른쪽 | D2 |
| S3 | 시아 | 기본 C · 잽·가드·피격 | 8 | jab 1–4, guard 5–6, hit 7–8 | 오른쪽 | D3 |
| S4 | 시아 | 기본 D · 승리·KO | 8 | win 1–4, ko 5–8 | 정면 | D4 |
| S5 | 시아 | 필살기 · 결측치 걸레질 | 8 | missing_value_mop 1–8 | 오른쪽 | D5 |
| S6 | 시아 | 필살기 · 정규화 쟁반 돌리기 | 8 | normalize_tray 1–8 | 오른쪽 | D6 |
| S7 | 시아 | 필살기 · 역전파 카운터 | 8 | backprop_counter 1–8 | 오른쪽 | D7 |
| S8 | 시아 | 의상 3종 · 메이드·전투복·사이버 | 6 | idle_maid 1–1, idle_battle 2–2, idle_cyber 3–3, jump_maid 4–4, jump_battle 5–5, jump_cyber 6–6 | 정면 | D8 |
| S9 | 시아 | 전투복 · 돌진·필살기 | 8 | dash 1–4, missing_value_mop 5–8 | 오른쪽 | D9 |
| S10 | 시아 | 사이버 · 돌진·필살기 | 8 | dash 1–4, missing_value_mop 5–8 | 오른쪽 | D10 |
| S11 | 시아 | 심판 A · 대기·시작 신호 | 8 | idle 1–4, start 5–8 | 정면 | F1 |
| S12 | 시아 | 심판 B · 판정 | 8 | point_left 1–4, point_right 5–8 | 정면 | F2 |
| S13 | 시아 | 심판 C · 무승부·의심 | 8 | draw 1–4, suspect 5–8 | 정면 | F3 |
| S14 | 시아 | 방청객 A · 대기·박수 | 8 | idle 1–4, clap 5–8 | 정면 | R1 |
| S15 | 시아 | 방청객 B · 환호·실망 | 8 | cheer 1–4, sad 5–8 | 정면 | R2 |
| M1 | 모아 | 기본 A · 서기·걷기 | 8 | idle 1–4, walk 5–8 | 왼쪽 | A1 |
| M2 | 모아 | 기본 B · 점프·돌진 | 8 | jump 1–4, dash 5–8 | 왼쪽 | A2 |
| M3 | 모아 | 기본 C · 잽·가드·피격 | 8 | jab 1–4, guard 5–6, hit 7–8 | 왼쪽 | A3 |
| M4 | 모아 | 기본 D · 승리·KO | 8 | win 1–4, ko 5–8 | 정면 | A4 |
| M5 | 모아 | 필살기 · 이상치 먼지털이 | 8 | outlier_duster 1–8 | 왼쪽 | A5 |
| M6 | 모아 | 필살기 · 배치 서빙 | 8 | batch_serving 1–8 | 왼쪽 | A6 |
| M7 | 모아 | 필살기 · 역전파 카운터 | 8 | backprop_counter 1–8 | 왼쪽 | A10 |
| M8 | 모아 | 의상 3종 · 메이드·전투복·사이버 | 6 | idle_maid 1–1, idle_battle 2–2, idle_cyber 3–3, jump_maid 4–4, jump_battle 5–5, jump_cyber 6–6 | 정면 | A7 |
| M9 | 모아 | 전투복 · 돌진·필살기 | 8 | dash 1–4, outlier_duster 5–8 | 왼쪽 | A8 |
| M10 | 모아 | 사이버 · 돌진·필살기 | 8 | dash 1–4, outlier_duster 5–8 | 왼쪽 | A9 |
| M11 | 모아 | 심판 A · 대기·시작 신호 | 8 | idle 1–4, start 5–8 | 정면 | F1 |
| M12 | 모아 | 심판 B · 판정 | 8 | point_left 1–4, point_right 5–8 | 정면 | F2 |
| M13 | 모아 | 심판 C · 무승부·의심 | 8 | draw 1–4, suspect 5–8 | 정면 | F3 |
| M14 | 모아 | 방청객 A · 대기·박수 | 8 | idle 1–4, clap 5–8 | 정면 | R1 |
| M15 | 모아 | 방청객 B · 환호·실망 | 8 | cheer 1–4, sad 5–8 | 정면 | R2 |
| M16 | 모아 | 정장 · 서기·걷기·서류 확인 | 8 | idle_suit 1–2, walk_suit 3–6, check 7–8 | 왼쪽 | A1 |
| X1A | 미공개 X1 | 방청객 · 대기·응원 | 8 | idle 1–4, cheer 5–8 | 정면 | R1 |
| X2A | 미공개 X2 | 방청객 · 대기·응원 | 8 | idle 1–4, cheer 5–8 | 정면 | R1 |
| X3A | 미공개 X3 | 방청객 · 대기·응원 | 8 | idle 1–4, cheer 5–8 | 정면 | R1 |

> 미공개 X1A~X3A 시트는 갤러리에서 버튼을 눌러야 보입니다. 대전 동작은 정체가 공개된 뒤 만듭니다.

---

### S1 · 시아 · 기본 A · 서기·걷기
- 첨부: E13 + 설정 시트 + `D1` 시트 · 쓰는 곳: 행동 축 '서기', 대전 대기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: idle stance, 4 frames: fighting-game ready stance, fists up, gentle breathing bob, apron hem sways slightly. Row 2: walk forward, 4 frames: walk cycle toward the right, arms swinging. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S2 · 시아 · 기본 B · 점프·돌진
- 첨부: E13 + 설정 시트 + `D2` 시트 · 쓰는 곳: 행동 축 '점프'·'돌진'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: jump, 4 frames: crouch, rise with knees tucked, peak, land. Row 2: dash, 4 frames: lean forward low, rush toward the RIGHT, hair and apron flying back to the left, stop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S3 · 시아 · 기본 C · 잽·가드·피격
- 첨부: E13 + 설정 시트 + `D3` 시트 · 쓰는 곳: 잽·가드 버튼, 데미지 장면

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: jab, 4 frames: quick straight punch forward and back. Row 2: guard 2 frames + hit 2 frames, 4 frames: frames 1-2 arms crossed blocking; frames 3-4 knocked back, eyes shut. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S4 · 시아 · 기본 D · 승리·KO
- 첨부: E13 + 설정 시트 + `D4` 시트 · 쓰는 곳: 라운드 결과

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: victory, 4 frames: fist pump, then arms crossed proudly, apron bow bouncing. Row 2: knocked out, 4 frames: stagger, yawn with a hand over the mouth, sit down sleepily, fall asleep face down on folded arms with a calm smile. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S5 · 시아 · 필살기 · 결측치 걸레질
- 첨부: E13 + 설정 시트 + `D5` 시트 · 쓰는 곳: 필살기 '결측치 걸레질'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: missing value mop, 8 frames, read left to right then top to bottom: pull a white cleaning cloth from the apron pocket, crouch low, wipe forward in a long sweeping arc toward the RIGHT, spin once, second sweep toward the RIGHT, the cloth fully extended, stand up, fold the cloth neatly; the cloth is the only prop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S6 · 시아 · 필살기 · 정규화 쟁반 돌리기
- 첨부: E13 + 설정 시트 + `D6` 시트 · 쓰는 곳: 필살기 '정규화 쟁반 돌리기'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: normalization tray spin, 8 frames, read left to right then top to bottom: take out a round silver serving tray, balance it on one fingertip, spin it, step in toward the RIGHT, swing the flat tray forward like a shield bash to the RIGHT, hold, catch the tray, hold it to the chest; the tray is the only prop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S7 · 시아 · 필살기 · 역전파 카운터
- 첨부: E13 + 설정 시트 + `D7` 시트 · 쓰는 곳: 콤보 마지막 기술 '역전파 카운터'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: backpropagation counter, 8 frames, read left to right then top to bottom: take a hit pose, slide backward, spin around once, reverse the momentum, deliver a rising palm strike upward, land in a ready stance. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S8 · 시아 · 의상 3종 · 메이드·전투복·사이버
- 첨부: E13 + 설정 시트 + `D8` 시트 · 쓰는 곳: 복장 축 '메이드·전투복·사이버'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 3 columns x 2 rows, aspect ratio 3:2. costumes, 6 frames, read left to right then top to bottom: columns = three outfits on the SAME character in the same idle stance: column 1 default maid outfit; column 2 'battle outfit' = maid dress sleeves rolled up, apron tied tight, gray headband, black fingerless gloves, gray sash belt, black training shoes; column 3 'cyber outfit' = maid dress and apron with thin glowing cyan circuit lines, a cyan visor-style headset, silver wrist guards, cyan-soled boots. Row 1 idle stance, row 2 the same three outfits in the jump peak pose. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S9 · 시아 · 전투복 · 돌진·필살기
- 첨부: E13 + 설정 시트 + `D9` 시트 · 쓰는 곳: 복장 축 '전투복'의 돌진·필살기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, wearing the battle outfit: maid dress sleeves rolled up, apron tied tight, gray headband, black fingerless gloves, gray sash belt, black training shoes, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: dash, 4 frames: lean forward low, rush toward the RIGHT, hair and apron flying back, stop. Row 2: missing value mop key frames, 4 frames: pull out the cloth, crouch, long sweeping wipe toward the RIGHT, hold. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S10 · 시아 · 사이버 · 돌진·필살기
- 첨부: E13 + 설정 시트 + `D10` 시트 · 쓰는 곳: 복장 축 '사이버'의 돌진·필살기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, wearing the cyber outfit: maid dress and apron with thin glowing cyan circuit lines, a cyan visor-style headset, silver wrist guards, cyan-soled boots, side view (3/4 toward the viewer). IMPORTANT: the character faces RIGHT in every frame (looking toward the right edge of the image, the attacking hand and leg reach to the RIGHT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: dash, 4 frames: lean forward low, rush toward the RIGHT, hair and apron flying back, stop. Row 2: missing value mop key frames, 4 frames: pull out the cloth, crouch, long sweeping wipe toward the RIGHT, hold. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S11 · 시아 · 심판 A · 대기·시작 신호
- 첨부: E13 + 설정 시트 + `F1` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: idle, 4 frames: standing referee pose, apron hem swaying slightly, holding a small blank white flag. Row 2: round start, 4 frames: raise one arm high, then swing it down sharply to signal the start. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S12 · 시아 · 심판 B · 판정
- 첨부: E13 + 설정 시트 + `F2` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: point to the left fighter, 4 frames: turn and point firmly to the viewer's left with the arm extended, flag up. Row 2: point to the right fighter, 4 frames: turn and point firmly to the viewer's right with the arm extended, flag up. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S13 · 시아 · 심판 C · 무승부·의심
- 첨부: E13 + 설정 시트 + `F3` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: draw, 4 frames: cross both arms in an X, then shake head. Row 2: suspicious check, 4 frames: lean forward, hand on chin, squint, then nod. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S14 · 시아 · 방청객 A · 대기·박수
- 첨부: E13 + 설정 시트 + `R1` 시트 · 쓰는 곳: 관중석 대기·점수 갱신 반응

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Audience props: a short glowing light stick in one hand, worn over the maid outfit. Row 1: idle audience, 4 frames: standing and watching, swaying gently side to side, light stick held low. Row 2: clapping, 4 frames: clap hands in front of the chest with the light stick tucked under one arm, small hop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### S15 · 시아 · 방청객 B · 환호·실망
- 첨부: E13 + 설정 시트 + `R2` 시트 · 쓰는 곳: 콤보 성공·실패 반응

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Audience props: a short glowing light stick in one hand, worn over the maid outfit. Row 1: cheer, 4 frames: raise the light stick high and wave it, happy open mouth, small jump. Row 2: disappointed, 4 frames: lower the light stick, shoulders drop, head down, small sigh. Same face, same proportions, same colors in every frame; only the pose changes. Keep the side-swept bangs parted on the same side in every frame. No headdress. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M1 · 모아 · 기본 A · 서기·걷기
- 첨부: E13 + 설정 시트 + `A1` 시트 · 쓰는 곳: 행동 축 '서기', 대전 대기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: idle stance, 4 frames: fighting-game ready stance, fists up, light bounce on toes, long hair sways. Row 2: walk forward, 4 frames: walk cycle toward the left, arms swinging. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M2 · 모아 · 기본 B · 점프·돌진
- 첨부: E13 + 설정 시트 + `A2` 시트 · 쓰는 곳: 행동 축 '점프'·'돌진'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: jump, 4 frames: crouch, rise with knees tucked, peak, land. Row 2: dash, 4 frames: lean forward low, rush toward the LEFT, hair and apron flying back, stop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M3 · 모아 · 기본 C · 잽·가드·피격
- 첨부: E13 + 설정 시트 + `A3` 시트 · 쓰는 곳: 잽·가드 버튼, 데미지 장면

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: jab, 4 frames: quick straight punch forward and back. Row 2: guard 2 frames + hit 2 frames, 4 frames: frames 1-2 arms crossed blocking; frames 3-4 knocked back, eyes shut. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M4 · 모아 · 기본 D · 승리·KO
- 첨부: E13 + 설정 시트 + `A4` 시트 · 쓰는 곳: 라운드 결과

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: victory, 4 frames: jump with a V sign, then hold up a silver serving tray proudly with a smile. Row 2: knocked out, 4 frames: stagger, kneel, sit down dizzy, lie down. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M5 · 모아 · 필살기 · 이상치 먼지털이
- 첨부: E13 + 설정 시트 + `A5` 시트 · 쓰는 곳: 필살기 '이상치 먼지털이'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: outlier duster, 8 frames, read left to right then top to bottom: pull out a fluffy feather duster, twirl it, step in toward the LEFT, rapid dusting swipes to the LEFT (high, low, high), one big final flick fully extended to the LEFT, hold, tuck the duster back into the apron; the feather duster is the only prop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M6 · 모아 · 필살기 · 배치 서빙
- 첨부: E13 + 설정 시트 + `A6` 시트 · 쓰는 곳: 필살기 '배치 서빙'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: batch serving, 8 frames, read left to right then top to bottom: lift a tray with three pink teacups, step toward the LEFT, slide the first cup forward to the LEFT, the second, the third, empty tray held out to the LEFT, bow politely, tuck the tray under the arm; no spilled liquid. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M7 · 모아 · 필살기 · 역전파 카운터
- 첨부: E13 + 설정 시트 + `A10` 시트 · 쓰는 곳: 콤보 마지막 기술 '역전파 카운터'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. special: backpropagation counter, 8 frames, read left to right then top to bottom: take a hit pose leaning back, slide backward to the RIGHT, spin around once, reverse the momentum, deliver a rising palm strike upward toward the LEFT, land in a ready stance facing LEFT. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M8 · 모아 · 의상 3종 · 메이드·전투복·사이버
- 첨부: E13 + 설정 시트 + `A7` 시트 · 쓰는 곳: 복장 축 '메이드·전투복·사이버'

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 3 columns x 2 rows, aspect ratio 3:2. costumes, 6 frames, read left to right then top to bottom: columns = three outfits on the SAME character in the same idle stance: column 1 default maid outfit; column 2 'battle outfit' = cardigan sleeves pushed up, apron tied tight, red headband over the maid headband ribbon, red fingerless gloves, plaid sash belt, sport sneakers; column 3 'cyber outfit' = cardigan and apron with thin glowing cyan circuit lines, cyan light in the headband frills, silver knee pads, cyan-soled boots. Row 1 idle stance, row 2 the same three outfits in the jump peak pose. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M9 · 모아 · 전투복 · 돌진·필살기
- 첨부: E13 + 설정 시트 + `A8` 시트 · 쓰는 곳: 복장 축 '전투복'의 돌진·필살기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, wearing the battle outfit: cardigan sleeves pushed up, apron tied tight, red headband over the maid headband ribbon, red fingerless gloves, plaid sash belt, sport sneakers, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: dash, 4 frames: lean forward low, rush toward the LEFT, hair and apron flying back, stop. Row 2: outlier duster key frames, 4 frames: twirl the feather duster, step in, rapid swipe to the LEFT, final flick fully extended to the LEFT. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M10 · 모아 · 사이버 · 돌진·필살기
- 첨부: E13 + 설정 시트 + `A9` 시트 · 쓰는 곳: 복장 축 '사이버'의 돌진·필살기

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, wearing the cyber outfit: cardigan and apron with thin glowing cyan circuit lines, cyan light in the headband frills, silver knee pads, cyan-soled boots, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: dash, 4 frames: lean forward low, rush toward the LEFT, hair and apron flying back, stop. Row 2: outlier duster key frames, 4 frames: twirl the feather duster, step in, rapid swipe to the LEFT, final flick fully extended to the LEFT. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M11 · 모아 · 심판 A · 대기·시작 신호
- 첨부: E13 + 설정 시트 + `F1` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: idle, 4 frames: standing referee pose, apron hem swaying slightly, holding a small blank white flag. Row 2: round start, 4 frames: raise one arm high, then swing it down sharply to signal the start. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M12 · 모아 · 심판 B · 판정
- 첨부: E13 + 설정 시트 + `F2` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: point to the left fighter, 4 frames: turn and point firmly to the viewer's left with the arm extended, flag up. Row 2: point to the right fighter, 4 frames: turn and point firmly to the viewer's right with the arm extended, flag up. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M13 · 모아 · 심판 C · 무승부·의심
- 첨부: E13 + 설정 시트 + `F3` 시트 · 쓰는 곳: 심판 자리 (초파리와 교대)

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Referee props: a small silver whistle on a cord around the neck and a small blank white flag in one hand, worn over the maid outfit. Row 1: draw, 4 frames: cross both arms in an X, then shake head. Row 2: suspicious check, 4 frames: lean forward, hand on chin, squint, then nod. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M14 · 모아 · 방청객 A · 대기·박수
- 첨부: E13 + 설정 시트 + `R1` 시트 · 쓰는 곳: 관중석 대기·점수 갱신 반응

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Audience props: a short glowing light stick in one hand, worn over the maid outfit. Row 1: idle audience, 4 frames: standing and watching, swaying gently side to side, light stick held low. Row 2: clapping, 4 frames: clap hands in front of the chest with the light stick tucked under one arm, small hop. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M15 · 모아 · 방청객 B · 환호·실망
- 첨부: E13 + 설정 시트 + `R2` 시트 · 쓰는 곳: 콤보 성공·실패 반응

```
Pixel art sprite sheet of one original character: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Audience props: a short glowing light stick in one hand, worn over the maid outfit. Row 1: cheer, 4 frames: raise the light stick high and wave it, happy open mouth, small jump. Row 2: disappointed, 4 frames: lower the light stick, shoulders drop, head down, small sigh. Same face, same proportions, same colors in every frame; only the pose changes. Keep the white headband and the ribbon over the left ear on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### M16 · 모아 · 정장 · 서기·걷기·서류 확인
- 첨부: E13 + 설정 시트 + `A1` 시트 · 쓰는 곳: 정장 의상 — 발표·보고·면접 장면

```
Pixel art sprite sheet of one original character: chibi girl office intern (big head, about 2.5 heads tall, the smallest of the human characters), the same face as the attached maid character, ash-beige hair tied in a low ponytail with a pink scrunchie, side locks framing the face, no headband, amber-brown eyes, black tailored jacket over a white collared shirt, black skirt, black low heels, small silver stud earrings, side view (3/4 toward the viewer). IMPORTANT: the character faces LEFT in every frame (attacks reach to the LEFT). Do not mirror. Grid 4 columns x 2 rows, aspect ratio 16:9. Frames 1-2: standing upright holding a stack of papers at the chest. Frames 3-6: walk cycle toward the LEFT, papers held in one arm. Frames 7-8: look down at the papers and tick a line with a black pen. Same face, same proportions, same colors in every frame; only the pose changes. Keep the ponytail on the same side in every frame. Never mirror the character. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### X1A · 미공개 X1 · 방청객 · 대기·응원
- 첨부: E13 + 설정 시트 + `R1` 시트 · 쓰는 곳: 관중석 머릿수 · 예고

```
Pixel art sprite sheet of one original character: a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, friendly and cute, not scary, chibi girl silhouette, long side ponytail tied with a big bow, the bow is the only colored part: bright pink (#E9709A), skirt hem visible under the lab coat, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: idle audience, 4 frames: standing and watching, swaying gently, white dot eyes blink once. Row 2: cheer, 4 frames: both arms up, small hop, dot eyes become happy upside-down U shapes. Same silhouette shape and the same single colored accessory in every frame; only the pose changes. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### X2A · 미공개 X2 · 방청객 · 대기·응원
- 첨부: E13 + 설정 시트 + `R1` 시트 · 쓰는 곳: 관중석 머릿수 · 예고

```
Pixel art sprite sheet of one original character: a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, friendly and cute, not scary, chibi silhouette with a round beret and short hair, round glasses frame whose lenses show two small teal (#3FC8C0) reflections as the only colored part, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: idle audience, 4 frames: standing and watching, swaying gently, white dot eyes blink once. Row 2: cheer, 4 frames: both arms up, small hop, dot eyes become happy upside-down U shapes. Same silhouette shape and the same single colored accessory in every frame; only the pose changes. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

---

### X3A · 미공개 X3 · 방청객 · 대기·응원
- 첨부: E13 + 설정 시트 + `R1` 시트 · 쓰는 곳: 관중석 머릿수 · 예고

```
Pixel art sprite sheet of one original character: a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, friendly and cute, not scary, very small chibi silhouette wearing a hood with cat ears, oversized lab coat with long sleeves covering the hands, two hood drawstrings ending in small yellow (#F2C744) pompoms as the only colored part, facing the viewer, front view. Grid 4 columns x 2 rows, aspect ratio 16:9. Row 1: idle audience, 4 frames: standing and watching, swaying gently, white dot eyes blink once. Row 2: cheer, 4 frames: both arms up, small hop, dot eyes become happy upside-down U shapes. Same silhouette shape and the same single colored accessory in every frame; only the pose changes. 16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, no extra visual effects beyond what is described, no motion lines, no speed lines.
```

## 받은 뒤 확인할 것
- 시아는 모든 칸에서 오른쪽, 모아는 왼쪽을 보는지 (S4·M4·심판·방청객은 정면)
- 시아에게 머리 장식이 없는지, 모아의 머리띠가 남아 있는지 (M16 정장만 포니테일·머리띠 없음)
- 배경이 단색 회색인지, 글자·효과선이 없는지, 칸마다 발 높이가 같은지
- 받은 시트는 `images/_sheets/motion/`에 두면, 칸을 잘라 `images/motions/{캐릭터}/`에 넣고 `motions.json`의 `planned`를 `sheets`로 옮깁니다.
