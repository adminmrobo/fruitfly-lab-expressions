---
id: E15
slug: flustered
character: MONEY-ROBO
alias: 머니로보
category: subtle   # 미묘한 감정
expression_ko: 당황
expression_en: Flustered
spec_file: specs/money_robo/expressions/E15_flustered.md
image_file: images/money_robo/E15_flustered.png
image_status: generated   # pending → generated → approved
core_ref: specs/money_robo/00_character_core.md
reference_images: [refs/original/money_robo_expressions_9.png, refs/original/money_robo_turnaround.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# MONEY-ROBO · E15 · 당황 (Flustered)

> 이 명세서는 **`images/money_robo/E15_flustered.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E15`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
갑작스러운 상황에 어쩔 줄 몰라 하는 상태.

## 2. 사용 상황
돌발 상황, 예상 밖 질문

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈 (금빛 픽셀) | 금빛 소용돌이 눈 (약하게) |
| 입 (금빛 픽셀) | 물결 입 |
| 스크린 효과 (볼·색 변화) | 하늘색 땀 픽셀 2~3개 |
| 가슴 코어 라이트 | 시안이 깜빡임 |
| 자세·기울기 | 몸이 흔들림 |
| 팔 제스처 | 양팔을 허둥지둥 휘저음 |
| 외부 이펙트 (금화·차트 등) | 머리 위 작은 김 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(흰 광택 둥근 사각 머리, 검은 알약형 스크린 얼굴, 금빛 픽셀 눈·입, 짧은 막대+원형 노브 안테나, 작은 흰 몸통, 검은 타원 가슴 패널 + 시안 코어, 손가락 없는 짧은 팔, 다리 없이 떠 있음 + 검은 타원 그림자, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 대사 1: "에, 에러! 아니 에러 아니에요!"
- 대사 2: "입력값이 너무 많아요!"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
MONEY-ROBO, a cute small floating chibi robot with a large glossy rounded-square white head and a small rounded white body with thick black outlines, a black pill-shaped screen face showing golden-yellow pixel eyes and mouth, a small round knob antenna on a short stem, stubby rounded fingerless arms, no legs, a black oval chest panel with a bright cyan pill-shaped core light, hovering above a small dark oval shadow, flustered face, mild golden swirl eyes, wavy golden mouth, several light blue pixel sweat drops on the screen, wobbling, arms flailing, small steam puffs, full body centered, facing viewer, same framing as the reference 3x3 expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat white background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, human face, realistic eyes, legs, fingers, hands with fingers, different head shape, colored body, screen face in any color other than black, extra limbs, readable text on the screen
```

## 9. 금지 사항
- 다리나 손가락이 생기는 결과
- 스크린 바깥(흰 머리)에 얼굴 요소를 그리는 결과
- 눈·입 색을 금색 이외로 바꾸는 결과 (E03·E22의 붉은 경보 빛, E19 금화 눈은 예외)
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E15_flustered.png`이다
