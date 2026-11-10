# 새 식구 기본형 — Genspark 지침서 (인턴 2명 + 미공개 슬롯 3개)

작성 2026-11-11 · 기준: `specs/sia/00_character_core.md`, `specs/moa/00_character_core.md`, `specs/spares/00_spare_slots.md`

## 0. 이름 정하기

기본안은 **시아 · 모아**로 두고 명세를 썼습니다. 다른 안을 고르면 이름만 바꾸면 됩니다(외형·프롬프트는 그대로).

| 안 | 흑발 인턴 | 베이지 인턴 | 짝을 이루는 뜻 | 외국어판 |
|---|---|---|---|---|
| **A (기본)** | **시아** | **모아** | 시야(지켜보는 눈 → 심판) · 모아 둠(기록·응원 → 방청객) | Sia · Moa |
| B | 새벽 | 노을 | 하루(조수)와 시간대로 이어짐: 새벽–하루–노을 | Saebyeok·Noeul은 외국어판에서 읽기 어려움 |
| C | 루나 | 솔 | 달·해 — 검은 머리·밝은 머리 대비 | Luna · Sol |
| D | 다온 | 보미 | 순우리말 느낌, 부드러운 어감 | Daon · Bomi |

> 하루 때처럼 같은 이름의 여성 캐릭터 상표가 있을 수 있으니, 정한 뒤 KIPRIS에서 한 번 확인하세요.

## 1. 전체 순서

| 단계 | 내용 | 결과 파일 |
|---|---|---|
| **1. 기본형 (이번)** | B1 설정 시트 → B2 E13 → B3 8방향 → B4 단체 사진 → B5 벡터 | 아래 표 |
| 2. 표정 | E01~E24 (하루와 같은 6칸 시트 4장) | `images/sia/`, `images/moa/` |
| 3. 동작 | 박사·조수와 같은 10장 + 심판 3장 + 방청객 2장 (+ 모아 정장 M16) → [`../motions/PROMPTS_interns.md`](../motions/PROMPTS_interns.md) | `images/_sheets/motion/S*_sia.png`, `M*_moa.png` |
| 4. 미공개 슬롯 | X1~X3 실루엣 시트·표정 | `images/spares/` |

2단계 표정 프롬프트는 `specs/sia/`·`specs/moa/` 각 표정 명세 7절에, 3단계 동작 프롬프트는 `specs/motions/PROMPTS_interns.md`에 있습니다. B1·B2가 승인된 뒤 그 그림을 참고 그림으로 넣고 씁니다.

### 동작 시트 배열 (3단계 미리 보기 — 박사·조수와 1:1)
| 시아 (오른쪽, 박사 자리) | 모아 (왼쪽, 조수 자리) | 내용 | 대응 |
|---|---|---|---|
| S1 | M1 | 서기·걷기 | D1 / A1 |
| S2 | M2 | 점프·돌진 | D2 / A2 |
| S3 | M3 | 잽·가드·피격 | D3 / A3 |
| S4 | M4 | 승리·KO (KO는 엎드려 잠드는 연출) | D4 / A4 |
| S5 | M5 | 필살기 ① 시아 **결측치 걸레질** · 모아 **이상치 먼지털이** | D5 / A5 |
| S6 | M6 | 필살기 ② 시아 **정규화 쟁반 돌리기** · 모아 **배치 서빙(찻잔 연속 배달)** | D6 / A6 |
| S7 | M7 | 필살기 ③ 역전파 카운터 (공통 기술) | D7 / A10 |
| S8 | M8 | 의상 3종: **메이드(기본)·전투복·사이버** | D8 / A7 |
| S9 | M9 | 전투복 돌진·필살기 | D9 / A8 |
| S10 | M10 | 사이버 돌진·필살기 | D10 / A9 |
| S11~S13 | M11~M13 | 심판 A·B·C: 대기·시작 / 좌우 판정 / 무승부·의심 | F1~F3 |
| S14~S15 | M14~M15 | 방청객 A·B: 박수·응원봉 / 환호·실망 | R1~R2 |

> 필살기 이름은 메이드의 '청소'와 데이터 '정제(cleaning)'를 엮었습니다. 바꾸셔도 됩니다.

---

## 2. 넣는 법 (매번)
- 비율: B1·B4 **4:3**, B2 **1:1**, B3 **16:9**, B5 **1:1** · 가장 큰 해상도
- 앞에 붙일 한국어 한 줄: *"첫 번째 그림의 캐릭터 디자인을, 두 번째 그림과 똑같은 픽셀 아트 화풍·배치·비율로 다시 그려 줘. 사무실 배경은 빼고, 아래 영어 프롬프트를 따라 줘."*
- **사용자 일러스트는 디자인 참고로만** 넣습니다. 그 그림의 그림체(매끈한 애니 채색)를 따라가면 실패입니다.

---

## 3. 시아 기본형

### B1 · 시아 설정 시트 → `refs/original/sia_sheet.png`
- 첨부: ① `01_Working_Typing.jpg` ② `refs/original/haru_sheet.png` ③ `03_Desk_Cleaning.jpg`(뒷모습·앞치마 참고)

```
Pixel art character design sheet of one original character: Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs with two black buttons, white high collar with a large soft gray bow, long white frilled apron reaching the ankles tied with a big bow at the back, white socks, black flat shoes, no headdress, no glasses. Same layout as the second reference sheet: full body front view standing with hands relaxed, full body side view facing left, full body back view showing the long black hair and the big white apron bow, a bust-up portrait in the top right corner, and a vertical column of 7 color swatches (#1E1B22, #4A4656, #34363F, #8C8C94, #F4F2EE, #7A7680, #F6D9C4). Same body proportions and head size as the second reference sheet. Detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, plain flat light gray background, no office scenery, no text, no letters, no numbers, no watermark.
```

### B2 · 시아 E13 기본 바스트업 → `images/sia/E13_neutral.png`
- 첨부: ① B1 결과 ② `images/haru/E13_neutral.png` (구도·크기 기준)

```
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, neutral default expression, relaxed eyebrows, calm open gray eyes looking at the viewer, closed mouth with a very faint smile, facing forward, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브: `blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, off-model, text, watermark, multiple characters, headdress, maid headband, glasses, blonde hair, brown hair`

---

## 4. 모아 기본형

### B1 · 모아 설정 시트 → `refs/original/moa_sheet.png`
- 첨부: ① 화분 그림(`Gemini_Generated_Image_63gjyf…`) ② `refs/original/haru_sheet.png` ③ 찻잔 그림(`…r2u37qr2u37qr2u3_3`)

```
Pixel art character design sheet of one original character: Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps tied with a big bow at the back, black skirt, white socks, brown loafers, no glasses. Same layout as the second reference sheet: full body front view standing with hands relaxed, full body side view facing left, full body back view showing the long wavy hair and the apron bow, a bust-up portrait in the top right corner, and a vertical column of 7 color swatches (#D8C09A, #B89C74, #D4B48A, #A8323C, #2C3A66, #FAF8F4, #B07A3E). Same body proportions and head size as the second reference sheet, slightly shorter than that character. Detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, plain flat light gray background, no office scenery, no text, no letters, no numbers, no watermark.
```

### B2 · 모아 E13 기본 바스트업 → `images/moa/E13_neutral.png`
- 첨부: ① B1 결과 ② `images/haru/E13_neutral.png`

```
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, neutral default expression, relaxed eyebrows, calm open amber eyes looking at the viewer, closed mouth with a soft gentle smile, facing forward, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브: `blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, off-model, text, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket`

---

## 5. 두 사람 함께

### B3 · 8방향 치비 → `images/_sheets/interns_turnaround8.png`
- 첨부: ① `images/_sheets/lab4_turnaround8.png` (2행 조수 줄을 잘라서) ② 시아 B1 ③ 모아 B1

```
Pixel art 8-direction turnaround sheet of two original chibi characters, 2 rows x 8 columns, aspect ratio 16:9, same layout and same chibi scale as the attached turnaround row. Row 1: chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes. Row 2: chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers. Columns from left to right: front, front-left, left, back-left, back, back-right, right, front-right. Same face and colors in every column. 16-bit RPG pixel art, crisp pixels, bold dark outline (#1d1a22), 2-3 step cel shading, full body, same ground line, flat plain light gray background, no text, no letters, no numbers, no shadow.
```

### B4 · 여섯 식구 단체 사진 → `images/_sheets/lab6_lineup.png`
- 첨부: ① `images/_sheets/lab4_lineup_gpt2_labeled.png` ② B3 결과

```
Pixel art group lineup of six original characters standing side by side on one ground line, front view, same pixel art style and same scale as the attached four-character lineup. From left to right: the doctor, the pink-haired assistant, the black-haired maid intern Sia (0.88 of the doctor's height), the ash-beige-haired maid intern Moa with a white maid headband (0.84 of the doctor's height), the beige retro computer robot holding an abacus, the small fruit fly researcher. Keep the first four existing characters exactly as in the reference. Sia: long straight black hair, gray eyes, charcoal-black long-sleeved maid dress, gray collar bow, long white frilled apron, hands folded in front. Moa: long ash-beige wavy hair, white frilled headband, camel cardigan, red and navy plaid bow tie, white frilled apron, small friendly wave. 16-bit SNES-era pixel art, crisp pixels, thick dark outlines, dithering shading, plain flat light gray background, no labels, no text, no letters, no numbers.
```

### B5 · 벡터 기본형 (각 1장) → `refs/original/sia_vector_base.png`, `moa_vector_base.png`
주판봇 벡터판과 같은 용도(로고·SVG 따기·큰 화면)입니다. 시아·모아를 따로 생성합니다.
- 첨부: 그 캐릭터의 B1 결과

```
Flat vector cartoon illustration of one original character, chibi proportions (about 2.5 heads tall), full body front view standing, clean bold dark outlines of even width, flat solid fill colors, at most one soft shadow tone per color, no gradients, no texture, no pixel art, simple shapes that are easy to trace into SVG. Character: [시아면 CHIBI_CORE_EN, 모아면 CHIBI_CORE_EN 붙여 넣기]. Same colors as the attached sheet. Centered on a plain white background, no text, no letters, no watermark.
```

---

## 6. 미공개 슬롯 X1~X3

### P1 · 실루엣 3종 설정 시트 → `images/_sheets/spares_sheet.png`
- 첨부: `images/_sheets/lab4_lineup_gpt2_labeled.png` (크기·화풍 기준)

```
Pixel art lineup of three mysterious unrevealed chibi characters standing side by side on one ground line, front view, same pixel style and chibi scale as the attached lineup. Each one is drawn as a cute solid silhouette: whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, wearing a lab coat whose shape is visible only as silhouette, friendly and cute, not scary. Left (0.85 of the doctor's height): chibi girl silhouette with a long side ponytail tied with a big bow, the bow is the only colored part: bright pink (#E9709A), skirt hem visible under the lab coat. Middle (0.95 of the doctor's height): chibi silhouette with a round beret and short hair, round glasses frame whose lenses show two small teal (#3FC8C0) reflections as the only colored part. Right (0.60 of the doctor's height): very small chibi silhouette wearing a hood with cat ears, oversized lab coat with long sleeves covering the hands, two hood drawstrings ending in small yellow (#F2C744) pompoms as the only colored part. 16-bit SNES-era pixel art, crisp pixels, thick dark outlines, plain flat light gray background, no text, no letters, no question marks, no labels.
```
네거티브: `scary, horror, villain, menacing smile, sharp teeth, bald head, realistic human proportions, glowing red eyes, full color clothing, visible face details, text, question mark symbol, watermark`

### P2 · 슬롯별 표정 9종 (X1·X2·X3 각 1장, 3×3) → `images/_sheets/spare_x1_faces.png` …
- 첨부: P1 결과(해당 칸)

```
Pixel art expression sheet, 3 columns x 3 rows, aspect ratio 1:1, of one mysterious unrevealed chibi character drawn as a cute solid dark navy-black silhouette (#1B1A2E) with a thin purple rim light, bust-up from chest up, same silhouette shape and the same single colored accessory in every cell: [X1_EN / X2_EN / X3_EN 붙여 넣기]. Only the white dot eyes, a tiny white mouth line and pink blush change. Cells left to right, top to bottom: neutral round dot eyes; happy upside-down U eyes with small open mouth; angry slanted line eyes; sad drooping eyes with one blue tear; surprised big round eyes with small o mouth; thinking eyes looking up with a dot mouth; proud closed happy eyes; flustered spiral eyes with sweat drop; shocked white circle eyes with a jagged mouth line. 16-bit SNES-era pixel art, crisp pixels, thick dark outlines, plain flat light gray background, each face inside its own equal cell, no text, no letters, no question marks.
```

---

## 7. 받은 뒤 확인할 것
- 시아에게 머리띠가 생기지 않았는지, 모아에게 머리띠가 있는지 (둘을 구별하는 가장 큰 차이)
- 하루 시트와 머리 크기·몸 비율이 같은지 (사용자 일러스트처럼 8등신이 되면 실패)
- 실루엣 슬롯이 무섭게 보이지 않는지, 포인트 색이 소품 하나에만 있는지
- 파일 이름은 위 표의 경로대로. 1~2장이 어긋나면 그 장만 다시 뽑습니다.
