# 헤어 어레인지 벡터 · 생성 프롬프트 (Genspark)

캐릭터마다 시트 7장(3스타일씩, 마지막 장은 2스타일). 위 줄 = 3/4 앞, 아래 줄 = 같은 머리의 3/4 뒤.
참고 이미지로 `refs/original/{캐릭터}_sheet.png`와 `images/{캐릭터}/E13_neutral.png`를 함께 넣습니다.
받은 시트는 `images/_sheets/hair/{시트}.png`로 저장하고, 칸별로 잘라 `images/hair/{캐릭터}/H##_{slug}_front.png`·`_back.png`로 둡니다(512×512 투명).

공통 금지어(negative)는 각 시트 아래에 있습니다. 그림 안에 글자가 들어가면 다시 뽑습니다.

## 하루 (`haru`)

유지할 것: 분홍 + 남색 줄 투톤(앞머리 가운데 굵은 남색 줄, 뒷머리 가운데 남색 줄), 작은 바보털, 파란 눈, 라벤더 후드 + 흰 랩코트

- 번 2개는 H00에서만 — 다른 H에서는 번 대신 그 머리 모양을 따른다(H17·H19는 번 1개).
- 묶거나 땋은 머리에서도 **남색 줄이 꼬리·땋은 가닥 안으로 이어져** 보여야 한다.
- 바보털은 모든 H에서 유지한다.
- 머리끈·리본은 남색 또는 라벤더.

### `haru_hair_1` — H00 정본 (기본 머리) · H01 하프 업 컬 · H02 로우 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) long straight pink hair to the waist with two round messy hair buns on top of the head; (2) half-up style: the top section gathered at the back of the head, the rest left down in soft loose curls; (3) low ponytail tied at the nape, a few loose face-framing strands, using navy and lavender hair ties or ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_2` — H03 포니 × 웨이브 · H04 사이드 포니테일 · H05 하이 트윈 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) mid-height ponytail with big soft waves in the tail, using navy and lavender hair ties or ribbons; (2) single side ponytail tied above one ear, tail falling over the shoulder, using navy and lavender hair ties or ribbons; (3) high twin ponytails on both sides of the head, long tails, using navy and lavender hair ties or ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_3` — H06 루즈 사이드 트위스트 · H07 사이드 로프 브레이드 · H08 트윈 브레이드

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) loose two-strand twist gathered to one side and falling over the shoulder; (2) one thick braid starting near the ear and falling over the shoulder to the chest; (3) two low braids, one on each side, falling in front of the shoulders, using navy and lavender hair ties or ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_4` — H09 하프 업 브레이드 · H10 미디엄 웨이브 · H11 루즈 & 플로잉

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) thin braids running along both sides of the head like a crown and joined at the back, the rest left down; (2) hair worn down with soft medium waves all the way to the ends; (3) all hair let down, long and flowing, no ties, using navy and lavender hair ties or ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_5` — H12 탑 액세서리 · H13 리본 하프 업 · H14 프렌치 트위스트

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) hair worn down with a lavender headband with a small navy bow on top; (2) half-up style tied at the back with a long ribbon whose ends hang down, using navy and lavender hair ties or ribbons; (3) elegant vertical French twist updo at the back of the head, neat and smooth. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_6` — H15 쿠루린파 업 · H16 사이드 시뇽 · H17 풀 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) low loose updo made by flipping and tucking the hair inward at the nape; (2) low chignon bun placed at one side of the nape; (3) one round bun high on the back of the head (a single bun instead of her usual two), navy streak wrapping into the bun. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

### `haru_hair_7` — H18 탑 노트 · H19 브레이디드 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x2 hairstyle reference sheet of ONE character: Haru, a cute anime girl lab assistant, pink hair with navy blue streaks (a thick navy streak down the center of the bangs and a navy streak down the center of the back hair), a small ahoge, big bright blue eyes, light peach skin, lavender hoodie with white drawstrings over a white t-shirt, under an open white lab coat. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) messy high top knot on the crown with loose spiky ends; (2) braid wrapped around the head into a bun at the back, crown-braid look. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color
```

## 시아 (`sia`)

유지할 것: 흑발, 옆으로 넘긴 앞머리 + 얼굴 옆 가는 두 가닥, 회색 눈, 은 귀걸이, 검정 메이드 원피스 + 회색 큰 리본

- 모아와 구별: **흰 프릴·메이드 머리띠는 어떤 H에서도 금지**.
- 장식이 필요한 H(H05·H12·H13)는 회색·숯색만 — H12는 머리띠 대신 **작은 회색 집게핀**.
- 업스타일(H14~H19)에서는 은 귀걸이가 보이게.
- 앞머리 가르마 방향은 모든 칸에서 같은 쪽.

### `sia_hair_1` — H00 정본 (기본 머리) · H01 하프 업 컬 · H02 로우 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) long straight jet-black hair reaching the waist, no headdress; (2) half-up style: the top section gathered at the back of the head, the rest left down in soft loose curls; (3) low ponytail tied at the nape, a few loose face-framing strands, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_2` — H03 포니 × 웨이브 · H04 사이드 포니테일 · H05 하이 트윈 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) mid-height ponytail with big soft waves in the tail, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband; (2) single side ponytail tied above one ear, tail falling over the shoulder, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband; (3) high twin ponytails on both sides of the head, long tails, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_3` — H06 루즈 사이드 트위스트 · H07 사이드 로프 브레이드 · H08 트윈 브레이드

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) loose two-strand twist gathered to one side and falling over the shoulder; (2) one thick braid starting near the ear and falling over the shoulder to the chest; (3) two low braids, one on each side, falling in front of the shoulders, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_4` — H09 하프 업 브레이드 · H10 미디엄 웨이브 · H11 루즈 & 플로잉

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) thin braids running along both sides of the head like a crown and joined at the back, the rest left down; (2) hair worn down with subtle soft waves (still clearly jet-black and long); (3) all hair let down, long and flowing, no ties, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_5` — H12 탑 액세서리 · H13 리본 하프 업 · H14 프렌치 트위스트

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) hair worn down with one small soft-gray hair clip on the side of the crown (no headband); (2) half-up style tied at the back with a long ribbon whose ends hang down, using plain charcoal or soft gray hair ties, a small gray hair clip, or a soft gray ribbon matching her collar bow — never white frills, never a maid headband; (3) elegant vertical French twist updo at the back of the head, neat and smooth. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_6` — H15 쿠루린파 업 · H16 사이드 시뇽 · H17 풀 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) low loose updo made by flipping and tucking the hair inward at the nape; (2) low chignon bun placed at one side of the nape; (3) all hair gathered into one round bun high on the back of the head. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

### `sia_hair_7` — H18 탑 노트 · H19 브레이디드 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x2 hairstyle reference sheet of ONE character: Sia, a calm anime girl maid intern, jet-black hair with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with white lace cuffs, white high collar with a large soft gray bow, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) messy high top knot on the crown with loose spiky ends; (2) braid wrapped around the head into a bun at the back, crown-braid look. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, maid headband, white frills
```

## 모아 (`moa`)

유지할 것: 애쉬 베이지 머리, 가지런한 앞머리, 흰 프릴 머리띠 + 왼쪽 흰 리본, 호박 눈, 카디건 + 체크 리본 타이

- **흰 프릴 머리띠는 모든 H에서 유지**(메이드 차림일 때). 정장(M16) 차림일 때만 없음.
- H02 로우 포니테일은 정장 머리와 같게 **분홍 곱창**으로 묶는다.
- 머리끈·리본은 분홍 또는 흰색.
- 기본 명세의 '포니테일 금지'는 H를 지정하지 않은 그림에만 적용한다.

### `moa_hair_1` — H00 정본 (기본 머리) · H01 하프 업 컬 · H02 로우 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) long ash-beige hair reaching the waist with soft wavy ends; (2) half-up style: the top section gathered at the back of the head, the rest left down in soft loose curls; (3) low ponytail at the nape tied with a pink scrunchie, a few loose face-framing strands (same as her suit hairstyle). Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_2` — H03 포니 × 웨이브 · H04 사이드 포니테일 · H05 하이 트윈 포니테일

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) mid-height ponytail with big soft waves in the tail, using pink scrunchies or pink and white ribbons; (2) single side ponytail tied above one ear, tail falling over the shoulder, using pink scrunchies or pink and white ribbons; (3) high twin ponytails on both sides of the head, long tails, using pink scrunchies or pink and white ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_3` — H06 루즈 사이드 트위스트 · H07 사이드 로프 브레이드 · H08 트윈 브레이드

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) loose two-strand twist gathered to one side and falling over the shoulder; (2) one thick braid starting near the ear and falling over the shoulder to the chest; (3) two low braids, one on each side, falling in front of the shoulders, using pink scrunchies or pink and white ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_4` — H09 하프 업 브레이드 · H10 미디엄 웨이브 · H11 루즈 & 플로잉

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) thin braids running along both sides of the head like a crown and joined at the back, the rest left down; (2) hair worn down with soft medium waves all the way to the ends; (3) all hair let down, long and flowing, no ties, using pink scrunchies or pink and white ribbons. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_5` — H12 탑 액세서리 · H13 리본 하프 업 · H14 프렌치 트위스트

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) hair worn down; the white frilled maid headband with a larger pink ribbon added on top; (2) half-up style tied at the back with a long ribbon whose ends hang down, using pink scrunchies or pink and white ribbons; (3) elegant vertical French twist updo at the back of the head, neat and smooth. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_6` — H15 쿠루린파 업 · H16 사이드 시뇽 · H17 풀 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x3 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) low loose updo made by flipping and tucking the hair inward at the nape; (2) low chignon bun placed at one side of the nape; (3) all hair gathered into one round bun high on the back of the head. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```

### `moa_hair_7` — H18 탑 노트 · H19 브레이디드 번

```
detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words. A 2x2 hairstyle reference sheet of ONE character: Moa, a gentle cheerful anime girl maid intern, ash-beige hair with neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan, white frilled apron, no glasses. Top row: chest-up bust shots in three-quarter front view. Bottom row: the SAME hairstyles seen from behind in three-quarter rear view so the arrangement is clear. Columns from left to right: (1) messy high top knot on the crown with loose spiky ends; (2) braid wrapped around the head into a bun at the back, crown-braid look. Same face, same eye color, same hair color, same outfit and same size in every cell; only the hairstyle changes. Plain light gray background in every cell, even spacing, no borders, no text.
```

Negative:
```
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, labels, multiple different characters, different face in each cell, changed eye color, changed hair color, missing headband
```
