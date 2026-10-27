---
id: E21
slug: waterfall_tears
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장
expression_ko: 울먹(폭포 눈물)
expression_en: Waterfall Tears
spec_file: specs/haru/expressions/E21_waterfall_tears.md
image_file: images/haru/E21_waterfall_tears.png
image_status: generated   # pending → generated → approved
core_ref: specs/haru/00_character_core.md
reference_images: [refs/original/haru_sheet.png, refs/original/haru_expressions_6.png]
original_match: "원본 2행 2열 "울음""
version: 1.1
---

# 하루(세나) · E21 · 울먹(폭포 눈물) (Waterfall Tears)

> 이 명세서는 **`images/haru/E21_waterfall_tears.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E21`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
과장된 코믹 울음.

## 2. 사용 상황
대결 패배, 아까운 실수

## 3. 원본 대응
원본 2행 2열 "울음"

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 크게 八자 |
| 눈 | 눈을 꽉 감음 |
| 입 | 크게 벌리고 우는 입 |
| 볼·피부 | 붉은 볼 |
| 머리·자세 | 정면 |
| 손·제스처 | 손은 화면 밖 |
| 만화 이펙트 | 양쪽 눈에서 흐르는 굵은 만화 눈물 (원본보다 과장) |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(분홍+남색 투톤 장발, 정수리 양쪽 번, 앞머리 가운데 남색 줄, 파란 눈, 라벤더 후드, 흰 랩코트, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 하루(본명): "으아앙, 다 날아갔어요…!"
- 세나(예명): "흐엥, 이건 너무하잖아요~!"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, comic crying, strongly slanted eyebrows, eyes squeezed shut, wide open crying mouth, thick streams of cartoon tears flowing down from both eyes, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
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
- [ ] 파일명이 `E21_waterfall_tears.png`이다
