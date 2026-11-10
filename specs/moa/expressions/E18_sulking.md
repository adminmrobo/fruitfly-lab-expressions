---
id: E18
slug: sulking
character: 모아 (Moa)
category: subtle   # 미묘한 감정
expression_ko: 삐짐
expression_en: Sulking
spec_file: specs/moa/expressions/E18_sulking.md
image_file: images/moa/E18_sulking.png
image_status: generated   # pending → generated → approved
core_ref: specs/moa/00_character_core.md
reference_images: [refs/original/moa_sheet.png, images/moa/E13_neutral.png]
original_match: "없음 (신규 표정)"
version: 0.1
---

# 모아 · E18 · 삐짐 (Sulking)

> 이 명세서는 **`images/moa/E18_sulking.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E18`)로 명세와 이미지가 1:1로 연결됩니다. 하루 `E18`와 같은 표정 정의를 씁니다.

## 1. 감정 의도
살짝 토라진 귀여운 불만.

## 2. 사용 상황
서운함, 장난 리액션

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽이 살짝 내려감 |
| 눈 | 눈을 가늘게 뜨고 옆으로 흘겨봄 |
| 입 | 삐죽 내민 입 |
| 볼·피부 | 선명한 홍조 |
| 머리·자세 | 고개를 옆으로 돌림 |
| 손·제스처 | 팔짱 |
| 만화 이펙트 | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(애쉬 베이지 긴 머리(끝 웨이브), 흰 프릴 메이드 머리띠 + 귀 위 흰 리본, 호박색 눈, 빨강·남색 체크 리본 타이, 카멜 니트 카디건, 흰 프릴 앞치마, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- "저도 대전 하고 싶었는데…"
- "흥, 응원 안 해 줄 거예요."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses, cute sulking pout, slightly lowered inner eyebrows, narrowed eyes glancing sideways, lips pushed out in a pout, blushing cheeks, head turned away, arms crossed, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
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
- [ ] 파일명이 `E18_sulking.png`이다
