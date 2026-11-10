---
id: E14
slug: sheepish
character: 모아 (Moa)
category: subtle   # 미묘한 감정
expression_ko: 머쓱함
expression_en: Sheepish
spec_file: specs/moa/expressions/E14_sheepish.md
image_file: images/moa/E14_sheepish.png
image_status: pending   # pending → generated → approved
core_ref: specs/moa/00_character_core.md
reference_images: [refs/original/moa_sheet.png, images/moa/E13_neutral.png]
original_match: "없음 (신규 표정)"
version: 0.1
---

# 모아 · E14 · 머쓱함 (Sheepish)

> 이 명세서는 **`images/moa/E14_sheepish.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E14`)로 명세와 이미지가 1:1로 연결됩니다. 하루 `E14`와 같은 표정 정의를 씁니다.

## 1. 감정 의도
칭찬받거나 사소한 실수를 한 뒤의 쑥스러움.

## 2. 사용 상황
칭찬 리액션, 작은 실수 무마

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 살짝 八자 |
| 눈 | 시선을 옆으로 피하며 눈웃음 |
| 입 | 어색하게 웃는 입 |
| 볼·피부 | 선명한 홍조 |
| 머리·자세 | 고개를 살짝 숙임 |
| 손·제스처 | 한 손으로 볼을 긁음 |
| 만화 이펙트 | 작은 땀방울 1개 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(애쉬 베이지 긴 머리(끝 웨이브), 흰 프릴 메이드 머리띠 + 귀 위 흰 리본, 호박색 눈, 빨강·남색 체크 리본 타이, 카멜 니트 카디건, 흰 프릴 앞치마, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- "에헤헤, 또 넘어질 뻔했어요."
- "차를 너무 많이 탔나 봐요."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, sheepish embarrassed smile, slightly worried eyebrows, eyes glancing away while smiling, awkward grin, noticeable blush, scratching cheek with one finger, small sweat drop, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket, different eye color, different outfit, extra fingers, deformed hands
```

## 9. 금지 사항
- 머리띠가 빠지거나 다른 머리 장식으로 바뀜
- 갈색 포니테일·정장 (정장은 의상 시트 M16에서만)
- 안경 착용
- 카디건 + 앞치마 이외의 의상
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 설정 시트·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 하루·박사와 같다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E14_sheepish.png`이다
