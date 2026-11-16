# E26 흥 (볼 빵빵 뾰로통) — Genspark 지침서 (하루 · 시아 · 모아)

작성 2026-11-16 · 공통 정의: [`E26_hmph.md`](E26_hmph.md)

## 넣는 법 (매번)
- 앞에 붙일 한국어 한 줄: *"첫 번째 그림의 캐릭터를, 두 번째 그림과 똑같은 픽셀 아트 화풍·구도·크기로, 아래 영어 프롬프트의 '흥(볼 빵빵 뾰로통)' 표정으로 다시 그려 줘."*
- 사용자가 모은 애니 캡처 4장은 **첨부하지 않습니다.** 넣으면 그 작품 캐릭터의 얼굴·머리·그림체를 따라가 버립니다. 표정은 프롬프트 글로만 지시합니다(정의 문서의 '참고 범위').
- 결과는 512×512 이상, 배경은 다른 표정과 같은 연회색. 저장 후 각 `expressions.json`의 `image_status`를 `generated`로 바꿉니다.
- E18(삐짐: 고개 돌림·팔짱)이나 E22(뿔남: 화난 이펙트)처럼 나오면 다시 뽑습니다. E26은 **팔짱 없이, 볼을 동그랗게 부풀린 귀여운 '흥'**이 핵심입니다.

## 하루 → `images/haru/E26_hmph.png`
- 첨부: ① `refs/original/haru_sheet.png` ② `images/haru/E13_neutral.png` ③ `images/haru/E18_sulking.png` (홍조·입 크기 참고, 팔짱은 따라 하지 않음)
- 비율 **1:1** · 가장 큰 해상도

```
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, cute hmph pouting expression, both cheeks puffed out round like a small balloon, lips pressed together into a tiny pursed pout, eyebrows knitted with the inner ends slightly raised in a sulky frown, soft pink blush across the cheeks, big glossy blue eyes looking up at the viewer from slightly below, both small fists clenched together in front of her chest, shoulders raised a little, one tiny round puff of steam above the head, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading
```

## 시아 → `images/sia/E26_hmph.png`
- 첨부: ① `refs/original/sia_sheet.png` ② `images/sia/E13_neutral.png` ③ `images/sia/E18_sulking.png` (홍조·입 크기 참고, 팔짱은 따라 하지 않음)
- 비율 **1:1** · 가장 큰 해상도

```
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, quiet hmph pouting expression, chin tucked slightly down, half-lidded calm gray eyes glancing sideways at the viewer with a cool sulky look, cheeks only slightly puffed, lips pressed into a tiny pursed pout, faint pink blush, one hand lightly holding the edge of her apron, no extra effects, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, hair ornament, glasses, colored hair, blonde hair, brown hair, short hair, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading
```

## 모아 → `images/moa/E26_hmph.png`
- 첨부: ① `refs/original/moa_sheet.png` ② `images/moa/E13_neutral.png` ③ `images/moa/E18_sulking.png` (홍조·입 크기 참고, 팔짱은 따라 하지 않음)
- 비율 **1:1** · 가장 큰 해상도

```
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, cute hmph pouting expression, both cheeks puffed out round like a small balloon, lips pressed together into a tiny pursed pout, eyebrows knitted with the inner ends slightly raised in a sulky frown, soft pink blush across the cheeks, facing the viewer straight on, round amber-brown eyes slightly glossy, hugging a small brown notebook tightly to her chest with both arms, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading
```

## 변형 walkaway — "흥!" 하고 돌아서 걷기 (전신, 동작 라이브러리 화풍)

네 번째 캡처처럼 돌아서 가면서 어깨 너머로 흘겨보는 장면입니다. 표정 시트가 아니라 **동작 라이브러리의 치비 전신** 화풍으로 그립니다.
- 앞에 붙일 한국어 한 줄: *"첫 번째 그림의 캐릭터를, 두 번째 그림(동작 프레임)과 똑같은 픽셀 스프라이트 화풍·크기로, 아래 영어 프롬프트처럼 그려 줘."*
- 비율 **2:3** · 가장 큰 해상도

### 하루 → `images/haru/E26_hmph_walkaway.png`
- 첨부: ① `refs/original/haru_sheet.png` ② `images/motions/haru/A1_f05.webp` (걷기 프레임)

```
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, chibi full body, about 2.5 heads tall, walking away to the left side with the body turned three-quarters away, glancing back over the shoulder at the viewer with a puffed-cheek hmph pout, one fist clenched at her side, the other arm swinging, hair buns and long pink hair swaying, lab coat hem flaring slightly, 16-bit RPG pixel art sprite, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, single character, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no logo, no watermark, no motion lines, same face, proportions and colors as the reference sprite, never mirror the character
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading, bust-up portrait, cropped body, front view only, running, jumping
```

### 시아 → `images/sia/E26_hmph_walkaway.png`
- 첨부: ① `refs/original/sia_sheet.png` ② `images/motions/sia/S1_f05.webp` (걷기 프레임)

```
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, chibi full body, about 2.5 heads tall, walking away to the left side with the body turned three-quarters away, glancing back over the shoulder with half-lidded eyes and a small puffed-cheek pout, chin raised slightly, both arms straight down at her sides, long black hair and apron bow swaying, 16-bit RPG pixel art sprite, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, single character, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no logo, no watermark, no motion lines, same face, proportions and colors as the reference sprite, never mirror the character
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, hair ornament, glasses, colored hair, blonde hair, brown hair, short hair, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading, bust-up portrait, cropped body, front view only, running, jumping
```

### 모아 → `images/moa/E26_hmph_walkaway.png`
- 첨부: ① `refs/original/moa_sheet.png` ② `images/motions/moa/M1_f05.webp` (걷기 프레임)

```
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, chibi full body, about 2.5 heads tall, walking away to the left side with the body turned three-quarters away, glancing back over the shoulder with a fully puffed-cheek hmph pout, hugging a small brown notebook to her chest, long ash-beige hair swaying, 16-bit RPG pixel art sprite, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, single character, flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no logo, no watermark, no motion lines, same face, proportions and colors as the reference sprite, never mirror the character
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading, bust-up portrait, cropped body, front view only, running, jumping
```

## 검수
- [ ] E13과 나란히 놓았을 때 같은 인물로 보인다(머리·눈 색·옷).
- [ ] 두 볼이 동그랗게 부풀었고 입은 작게 오므렸다. 입을 벌리거나 이를 드러내지 않았다.
- [ ] 팔짱이 없다(E18과 구분). 빨간 분노 마크·불꽃이 없다(E22와 구분).
- [ ] 캐릭터별 손·시선이 정의 문서와 맞다(하루 두 주먹·올려다봄, 시아 옆으로 흘김, 모아 수첩 끌어안기).
- [ ] 글자·말풍선이 없다(대사는 페이지에서 HTML 글자로 얹음).
