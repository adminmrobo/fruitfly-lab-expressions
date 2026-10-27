---
id: E13
slug: neutral
character: 박사 (Professor)
alias: 없음
category: subtle   # 미묘한 감정
expression_ko: 기본(중립)
expression_en: Neutral
spec_file: specs/doctor/expressions/E13_neutral.md
image_file: images/doctor/E13_neutral.png
image_status: generated   # pending → generated → approved
core_ref: specs/doctor/00_character_core.md
reference_images: [refs/original/doctor_sheet.png, refs/original/keyart_rivals.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# 박사 · E13 · 기본(중립) (Neutral)

> 이 명세서는 **`images/doctor/E13_neutral.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E13`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
모든 표정의 기준이 되는 기본 상태이자 아이덴티티 기준 이미지.

## 2. 사용 상황
대기 화면, 프로필, 비교 기준

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 (굵은 검은 눈썹) | 자연스러운 기본 위치 |
| 눈·안경 | 안경 너머로 편안하게 뜬 작은 눈 |
| 입 | 자신감 있는 다문 미소 |
| 볼·피부 | 홍조 없음 |
| 머리·자세 | 정면, 꼿꼿한 자세 |
| 손·제스처 | 한 손은 가운 주머니 |
| 이펙트 (보라 불꽃 포함) | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(짙은 숯색 뾰족 머리 + 앞머리 흰 줄, 뒤쪽 작은 꽁지머리, 굵은 검은 눈썹, 청록 테 안경, 흰 가운 + 검은 조끼·넥타이, 치비 비율, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 대사 1: "반갑네, 내가 박사일세."
- 대사 2: "오늘도 연구를 시작해 볼까."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks, neutral default expression, relaxed thick eyebrows, small calm open eyes behind teal glasses looking at viewer, confident closed smile, facing forward, one hand in lab coat pocket, chibi upper body portrait from waist up, facing viewer, centered, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, no glasses, round glasses, thin eyebrows, beard, mustache, bald, different hair color, missing white streak, realistic proportions, extra fingers, deformed hands
```

## 9. 금지 사항
- 안경이 사라지거나 테 색(청록)이 바뀌는 결과
- 수염 추가 (원본에 수염 없음)
- 치비 비율 변경
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E13_neutral.png`이다
