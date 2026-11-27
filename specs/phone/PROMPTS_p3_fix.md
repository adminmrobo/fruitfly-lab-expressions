# P3 단독 재생성 프롬프트 (팔 3~4개 고치기, 2026-11-27)

3컷 한 장으로 다시 그리면 아래 큰 칸(P3)에서 양손 브이에 셀카 팔까지 더 그려지는 일이 되풀이됩니다. 그래서 **P3만 따로 한 장으로 생성**하고, 받은 그림을 원래 3컷 그림의 아래 칸에 끼워 넣습니다. P1·P2는 그대로 둡니다.

## 대상

| 그림 | 문제 |
|---|---|
| 하루 벡터판 G0 · G1 · G2 | P3 팔 3~4개 (1차 그림 그대로) |
| 모아 벡터판 G2 | P3 팔 4개 — 양손 브이 + 양쪽 아래 모서리로 뻗은 소매 |
| 모아 벡터판 G3 | P3 팔 3개 — 오른쪽 가장자리에 소매 하나가 더 있음 (2026-11-27 새로 확인) |

## 순서

1. 아래 프롬프트로 Genspark에서 **가로 6:5 그림 1장**(1200×1000 이상)을 만든다. 첨부는 각 항목의 참고 그림 2장만.
2. 팔이 정확히 2개(브이 두 손 + 아래 가장자리 가운데로 내려가는 소매 2개)인지 확인한다. 화면 양옆·아래 모서리로 뻗은 소매가 있으면 버린다.
3. 받은 파일을 끼워 넣는다:

```sh
python3 specs/phone/tools/replace_p3.py images/phone/moa/PH1_selfie3_vector_G2_mask.png 받은_P3.png
```

   3컷 그림과 `PH1_p3_…` 컷이 함께 바뀌고, 원래 파일은 `.bak.png`로 남습니다(확인 후 지움).

## 팔 규칙 (모든 프롬프트 공통)

- 화면은 정수리부터 가슴 위까지만. 팔꿈치는 화면 아래 밖.
- 두 손은 턱 바로 아래에서 브이. 손마다 소매 하나가 **아래 가장자리 가운데 쪽에서 곧게 올라와** 이어진다.
- 어깨는 양옆으로 비스듬히 내려가고, 어깨에서 화면 옆이나 모서리로 뻗는 소매는 없다.
- 폰·삼각대·셀카 팔은 그리지 않는다.

## 하루 · 벡터판 · G0 → `images/phone/haru/PH1_p3_vector.png`

- 첨부: `refs/original/haru_sheet.png` · `images/haru/E19_sparkle_eyes.png`
- 끼워 넣기: `python3 specs/phone/tools/replace_p3.py images/phone/haru/PH1_selfie3_vector.png 받은_P3.png`

```text
Single landscape illustration, aspect ratio 6:5, one image with no panels, no borders and no gutters. Character: Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat. Close-up portrait of Haru's face filling the image, looking straight at the viewer, head tilted a little, small closed cat-like smile shaped like a wide w, big bright blue eyes with tiny pink heart-shaped highlights, soft pink blush, strands of pink and navy hair across the forehead, both hair buns visible at the top edge, pink hearts and white sparkles floating on a pastel pink and lavender halftone background. Framing: from the top of the head down to the upper chest only; the elbows are below the bottom edge of the image. Both hands make V-signs right under her chin, close together. Each hand connects to exactly one forearm sleeve that rises straight up from the bottom edge of the image near the center; nothing else reaches toward the camera. Her shoulders slope down at the left and right sides of the image with no sleeve, hand or arm extending outward toward the sides or the bottom corners. Exactly two arms and two hands in the whole image. Style: clean flat vector anime illustration, crisp even-width dark outlines, flat fill colors with at most one soft shade tone per color, no gradients, no texture, no pixel art, shapes simple enough to trace into SVG, cheerful comedy mood. No readable text, no letters, no words, no speech bubbles, no logo, no watermark, same character as the reference image, identical face, hair and outfit colors.
```

네거티브:

```text
blurry, 3D render, photorealistic, inconsistent character, off-model, text, letters, speech bubble, watermark, logo, multiple different characters, extra fingers, deformed hands, more than two hands, three arms, four arms, extra arm holding a phone, twin tails, turquoise hair, teal hair, necktie, sleeveless shirt, copy of an existing anime character, different art style, pixel art, dithering, painterly texture, gradient shading, glasses, short hair, missing hair buns, missing navy streak, different eye color, outstretched arm toward the camera, selfie arm, headset, face mask, hard hat, helmet, sleeves reaching to the bottom corners, sleeve at the left or right edge of the frame, arm extending outward, duplicate arm, duplicate sleeve, third sleeve, arm coming from the shoulder toward the camera, phone, tripod, hand holding a phone, comic panels, panel borders, gutters, multiple panels
```

## 하루 · 벡터판 · G1 헤드셋 → `images/phone/haru/PH1_p3_vector_G1_headset.png`

- 첨부: `refs/original/haru_sheet.png` · `images/haru/E19_sparkle_eyes.png`
- 끼워 넣기: `python3 specs/phone/tools/replace_p3.py images/phone/haru/PH1_selfie3_vector_G1_headset.png 받은_P3.png`

```text
Single landscape illustration, aspect ratio 6:5, one image with no panels, no borders and no gutters. Character: Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat. She wears a simple over-ear headset: a thin navy headband sitting between her two hair buns, round lavender ear cups and a small thin boom microphone at the left cheek. Close-up portrait of Haru's face filling the image, looking straight at the viewer, head tilted a little, small closed cat-like smile shaped like a wide w, big bright blue eyes with tiny pink heart-shaped highlights, soft pink blush, strands of pink and navy hair across the forehead, both hair buns visible at the top edge, pink hearts and white sparkles floating on a pastel pink and lavender halftone background. Framing: from the top of the head down to the upper chest only; the elbows are below the bottom edge of the image. Both hands make V-signs right under her chin, close together. Each hand connects to exactly one forearm sleeve that rises straight up from the bottom edge of the image near the center; nothing else reaches toward the camera. Her shoulders slope down at the left and right sides of the image with no sleeve, hand or arm extending outward toward the sides or the bottom corners. Exactly two arms and two hands in the whole image. Style: clean flat vector anime illustration, crisp even-width dark outlines, flat fill colors with at most one soft shade tone per color, no gradients, no texture, no pixel art, shapes simple enough to trace into SVG, cheerful comedy mood. No readable text, no letters, no words, no speech bubbles, no logo, no watermark, same character as the reference image, identical face, hair and outfit colors.
```

네거티브:

```text
blurry, 3D render, photorealistic, inconsistent character, off-model, text, letters, speech bubble, watermark, logo, multiple different characters, extra fingers, deformed hands, more than two hands, three arms, four arms, extra arm holding a phone, twin tails, turquoise hair, teal hair, necktie, sleeveless shirt, copy of an existing anime character, different art style, pixel art, dithering, painterly texture, gradient shading, glasses, short hair, missing hair buns, missing navy streak, different eye color, outstretched arm toward the camera, selfie arm, face mask, hard hat, helmet, rectangular black and pink ear pieces, sleeves reaching to the bottom corners, sleeve at the left or right edge of the frame, arm extending outward, duplicate arm, duplicate sleeve, third sleeve, arm coming from the shoulder toward the camera, phone, tripod, hand holding a phone, comic panels, panel borders, gutters, multiple panels
```

## 하루 · 벡터판 · G2 마스크 → `images/phone/haru/PH1_p3_vector_G2_mask.png`

- 첨부: `refs/original/haru_sheet.png` · `images/haru/E19_sparkle_eyes.png`
- 끼워 넣기: `python3 specs/phone/tools/replace_p3.py images/phone/haru/PH1_selfie3_vector_G2_mask.png 받은_P3.png`

```text
Single landscape illustration, aspect ratio 6:5, one image with no panels, no borders and no gutters. Character: Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat. She wears a plain white pleated face mask over her nose and mouth, pulled down under her chin so the small cat-like smile shows. Close-up portrait of Haru's face filling the image, looking straight at the viewer, head tilted a little, small closed cat-like smile shaped like a wide w, big bright blue eyes with tiny pink heart-shaped highlights, soft pink blush, strands of pink and navy hair across the forehead, both hair buns visible at the top edge, pink hearts and white sparkles floating on a pastel pink and lavender halftone background. Framing: from the top of the head down to the upper chest only; the elbows are below the bottom edge of the image. Both hands make V-signs right under her chin, close together. Each hand connects to exactly one forearm sleeve that rises straight up from the bottom edge of the image near the center; nothing else reaches toward the camera. Her shoulders slope down at the left and right sides of the image with no sleeve, hand or arm extending outward toward the sides or the bottom corners. Exactly two arms and two hands in the whole image. Style: clean flat vector anime illustration, crisp even-width dark outlines, flat fill colors with at most one soft shade tone per color, no gradients, no texture, no pixel art, shapes simple enough to trace into SVG, cheerful comedy mood. No readable text, no letters, no words, no speech bubbles, no logo, no watermark, same character as the reference image, identical face, hair and outfit colors.
```

네거티브:

```text
blurry, 3D render, photorealistic, inconsistent character, off-model, text, letters, speech bubble, watermark, logo, multiple different characters, extra fingers, deformed hands, more than two hands, three arms, four arms, extra arm holding a phone, twin tails, turquoise hair, teal hair, necktie, sleeveless shirt, copy of an existing anime character, different art style, pixel art, dithering, painterly texture, gradient shading, glasses, short hair, missing hair buns, missing navy streak, different eye color, outstretched arm toward the camera, selfie arm, headset, hard hat, helmet, gas mask, respirator, sleeves reaching to the bottom corners, sleeve at the left or right edge of the frame, arm extending outward, duplicate arm, duplicate sleeve, third sleeve, arm coming from the shoulder toward the camera, phone, tripod, hand holding a phone, comic panels, panel borders, gutters, multiple panels
```

## 모아 · 벡터판 · G2 마스크 → `images/phone/moa/PH1_p3_vector_G2_mask.png`

- 첨부: `refs/original/moa_vector_base.png` · `refs/original/moa_sheet.png`
- 끼워 넣기: `python3 specs/phone/tools/replace_p3.py images/phone/moa/PH1_selfie3_vector_G2_mask.png 받은_P3.png`

```text
Single landscape illustration, aspect ratio 6:5, one image with no panels, no borders and no gutters. Character: Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses. She wears a plain white pleated face mask over her nose and mouth, pulled down under her chin so the small cat-like smile shows. Close-up portrait of Moa's face filling the image, looking straight at the viewer, head tilted a little, small closed cat-like smile shaped like a wide w, big round amber-brown eyes with tiny pink heart-shaped highlights, soft blush, white frilled maid headband visible, soft wavy ash-beige hair, pink hearts and white sparkles floating on a cream and pink halftone background. Framing: from the top of the head down to the upper chest only; the elbows are below the bottom edge of the image. Both hands make V-signs right under her chin, close together. Each hand connects to exactly one forearm sleeve that rises straight up from the bottom edge of the image near the center; nothing else reaches toward the camera. Her shoulders slope down at the left and right sides of the image with no sleeve, hand or arm extending outward toward the sides or the bottom corners. Exactly two arms and two hands in the whole image. Style: clean flat vector anime illustration, crisp even-width dark outlines, flat fill colors with at most one soft shade tone per color, no gradients, no texture, no pixel art, shapes simple enough to trace into SVG, cheerful comedy mood. No readable text, no letters, no words, no speech bubbles, no logo, no watermark, same character as the reference image, identical face, hair and outfit colors.
```

네거티브:

```text
blurry, 3D render, photorealistic, inconsistent character, off-model, text, letters, speech bubble, watermark, logo, multiple different characters, extra fingers, deformed hands, more than two hands, three arms, four arms, extra arm holding a phone, twin tails, turquoise hair, teal hair, necktie, sleeveless shirt, copy of an existing anime character, different art style, pixel art, dithering, painterly texture, gradient shading, black hair, pink hair, ponytail, missing headband, suit jacket, different eye color, outstretched arm toward the camera, selfie arm, headset, hard hat, helmet, gas mask, respirator, sleeves reaching to the bottom corners, sleeve at the left or right edge of the frame, arm extending outward, duplicate arm, duplicate sleeve, third sleeve, arm coming from the shoulder toward the camera, phone, tripod, hand holding a phone, comic panels, panel borders, gutters, multiple panels
```

## 모아 · 벡터판 · G3 안전모 → `images/phone/moa/PH1_p3_vector_G3_hardhat.png`

- 첨부: `refs/original/moa_vector_base.png` · `refs/original/moa_sheet.png`
- 끼워 넣기: `python3 specs/phone/tools/replace_p3.py images/phone/moa/PH1_selfie3_vector_G3_hardhat.png 받은_P3.png`

```text
Single landscape illustration, aspect ratio 6:5, one image with no panels, no borders and no gutters. Character: Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses. She wears a bright yellow safety hard hat with a chin strap; the white frilled maid headband is taken off for safety, soft wavy ash-beige hair flows out below the hard hat, neat bangs under the brim. Close-up portrait of Moa's face filling the image, looking straight at the viewer, head tilted a little, small closed cat-like smile shaped like a wide w, big round amber-brown eyes with tiny pink heart-shaped highlights, soft blush, the yellow hard hat brim visible at the top edge, no maid headband, soft wavy ash-beige hair, pink hearts and white sparkles floating on a cream and pink halftone background. Framing: from the top of the head down to the upper chest only; the elbows are below the bottom edge of the image. Both hands make V-signs right under her chin, close together. Each hand connects to exactly one forearm sleeve that rises straight up from the bottom edge of the image near the center; nothing else reaches toward the camera. Her shoulders slope down at the left and right sides of the image with no sleeve, hand or arm extending outward toward the sides or the bottom corners. Exactly two arms and two hands in the whole image. Style: clean flat vector anime illustration, crisp even-width dark outlines, flat fill colors with at most one soft shade tone per color, no gradients, no texture, no pixel art, shapes simple enough to trace into SVG, cheerful comedy mood. No readable text, no letters, no words, no speech bubbles, no logo, no watermark, same character as the reference image, identical face, hair and outfit colors.
```

네거티브:

```text
blurry, 3D render, photorealistic, inconsistent character, off-model, text, letters, speech bubble, watermark, logo, multiple different characters, extra fingers, deformed hands, more than two hands, three arms, four arms, extra arm holding a phone, twin tails, turquoise hair, teal hair, necktie, sleeveless shirt, copy of an existing anime character, different art style, pixel art, dithering, painterly texture, gradient shading, black hair, pink hair, ponytail, suit jacket, different eye color, outstretched arm toward the camera, selfie arm, maid headband under the hard hat, headset, face mask, baseball cap, military helmet, sleeves reaching to the bottom corners, sleeve at the left or right edge of the frame, arm extending outward, duplicate arm, duplicate sleeve, third sleeve, arm coming from the shoulder toward the camera, phone, tripod, hand holding a phone, comic panels, panel borders, gutters, multiple panels
```
