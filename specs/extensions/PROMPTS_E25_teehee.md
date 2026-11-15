# E25 데헷 — Genspark 지침서 (하루 · 시아 · 모아)

작성 2026-11-15 · 공통 정의: [`E25_teehee.md`](E25_teehee.md)

## 넣는 법 (매번)
- 앞에 붙일 한국어 한 줄: *"첫 번째 그림의 캐릭터를, 두 번째 그림과 똑같은 픽셀 아트 화풍·구도·크기로, 아래 영어 프롬프트의 '데헷' 표정으로 다시 그려 줘."*
- 밈 참고 그림(애니 캡처)은 **넣지 않습니다.** 넣으면 그 캐릭터 얼굴·그림체를 따라가 버립니다. 포즈는 프롬프트 글로만 지시합니다.
- 결과는 512×512 이상, 배경은 다른 표정과 같은 연회색. 저장 후 각 `expressions.json`의 `image_status`를 `generated`로 바꿉니다.

## 하루 → `images/haru/E25_teehee.png`
- 첨부: ① `refs/original/haru_sheet.png` ② `images/haru/E13_neutral.png` ③ `images/haru/E14_sheepish.png` (홍조·손 크기 참고)
- 비율 **1:1** · 가장 큰 해상도

```
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, playful teehee expression, cute mischievous wink with one eye closed in a happy curved arc, the other eye open and sparkling at the viewer, small playful smile with just the tip of the tongue peeking out at the corner of the mouth, light pink blush lines on the cheeks, head tilted slightly to one side, one hand making a peace V sign right next to the winking eye, two tiny sparkles near the face, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, both eyes open, tongue sticking far out, licking, drooling, mocking face, rude gesture, middle finger
```

## 시아 → `images/sia/E25_teehee.png`
- 첨부: ① `refs/original/sia_sheet.png` ② `images/sia/E13_neutral.png` ③ `images/sia/E14_sheepish.png` (홍조·손 크기 참고)
- 비율 **1:1** · 가장 큰 해상도

```
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, playful teehee expression, cute mischievous wink with one eye closed in a happy curved arc, the other eye open and sparkling at the viewer, small playful smile with just the tip of the tongue peeking out at the corner of the mouth, light pink blush lines on the cheeks, head tilted slightly to one side, one index finger lightly poking her own cheek, no extra effects, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, hair ornament, glasses, colored hair, blonde hair, brown hair, short hair, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, both eyes open, tongue sticking far out, licking, drooling, mocking face, rude gesture, middle finger
```

## 모아 → `images/moa/E25_teehee.png`
- 첨부: ① `refs/original/moa_sheet.png` ② `images/moa/E13_neutral.png` ③ `images/moa/E14_sheepish.png` (홍조·손 크기 참고)
- 비율 **1:1** · 가장 큰 해상도

```
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, playful teehee expression, cute mischievous wink with one eye closed in a happy curved arc, the other eye open and sparkling at the viewer, small playful smile with just the tip of the tongue peeking out at the corner of the mouth, light pink blush lines on the cheeks, head tilted slightly to one side, one loosely closed fist gently bonking the top of her own head, one tiny comic impact star above the head, no text, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```
네거티브:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, both eyes open, tongue sticking far out, licking, drooling, mocking face, rude gesture, middle finger
```
