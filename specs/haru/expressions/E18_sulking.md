---
id: E18
slug: sulking
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 삐짐
expression_en: Sulking
spec_file: specs/haru/expressions/E18_sulking.md
image_file: images/haru/E18_sulking.png
image_status: generated   # pending → generated → approved
core_ref: specs/haru/00_character_core.md
reference_images: [refs/original/haru_sheet.png, refs/original/haru_expressions_6.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# 하루(세나) · E18 · 삐짐 (Sulking)

> 이 명세서는 **`images/haru/E18_sulking.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E18`)로 명세와 이미지가 1:1로 연결됩니다.

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
`00_character_core.md` 2절의 **아이덴티티 고정값**(분홍+남색 투톤 장발, 정수리 양쪽 번, 앞머리 가운데 남색 줄, 파란 눈, 라벤더 후드, 흰 랩코트, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 하루(본명): "…흥, 몰라요."
- 세나(예명): "치, 저 빼고 다 했단 말이에요?"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, cute sulking pout, slightly lowered inner eyebrows, narrowed eyes glancing sideways, lips pushed out in a pout, blushing cheeks, head turned away, arms crossed, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands
```

## 9. 금지 사항
- 안경 착용 (조수는 안경을 쓰지 않음)
- 헤어 색·번·앞머리 남색 줄 변경
- 라벤더 후드 + 흰 랩코트 이외의 의상
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E18_sulking.png`이다
