---
id: E02
slug: sadness
character: MONEY-ROBO
alias: 머니로보
category: basic   # 기본 감정
expression_ko: 슬픔
expression_en: Sadness
spec_file: specs/money_robo/expressions/E02_sadness.md
image_file: images/money_robo/E02_sadness.png
image_status: generated   # pending → generated → approved
core_ref: specs/money_robo/00_character_core.md
reference_images: [refs/original/money_robo_expressions_9.png, refs/original/money_robo_turnaround.png]
original_match: "원본 2행 1열 "울음""
version: 1.1
---

# MONEY-ROBO · E02 · 슬픔 (Sadness)

> 이 명세서는 **`images/money_robo/E02_sadness.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E02`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
조용히 가라앉은 슬픔. 울기 직전 단계까지만.

## 2. 사용 상황
나쁜 소식, 실패 공감

## 3. 원본 대응
원본 2행 1열 "울음"

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈 (금빛 픽셀) | 동그란 금빛 눈 |
| 입 (금빛 픽셀) | ∩ 모양 작은 입 |
| 스크린 효과 (볼·색 변화) | 눈 아래로 하늘색 픽셀 눈물 줄기 (원본과 동일) |
| 가슴 코어 라이트 | 시안, 어둡게 |
| 자세·기울기 | 살짝 아래로 처짐 |
| 팔 제스처 | 팔을 늘어뜨림 |
| 외부 이펙트 (금화·차트 등) | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(흰 광택 둥근 사각 머리, 검은 알약형 스크린 얼굴, 금빛 픽셀 눈·입, 짧은 막대+원형 노브 안테나, 작은 흰 몸통, 검은 타원 가슴 패널 + 시안 코어, 손가락 없는 짧은 팔, 다리 없이 떠 있음 + 검은 타원 그림자, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 대사 1: "예측이… 빗나갔어요…"
- 대사 2: "데이터가 저를 배신했어요…"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
MONEY-ROBO, a cute small floating chibi robot with a large glossy rounded-square white head and a small rounded white body with thick black outlines, a black pill-shaped screen face showing golden-yellow pixel eyes and mouth, a small round knob antenna on a short stem, stubby rounded fingerless arms, no legs, a black oval chest panel with a bright cyan pill-shaped core light, hovering above a small dark oval shadow, sad crying face, round golden pixel eyes with light blue pixel tear streams running down, small frowning golden mouth, dimmed cyan core, arms drooping, floating lower, full body centered, facing viewer, same framing as the reference 3x3 expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat white background, same character as the reference image, identical design and colors
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
- [ ] 파일명이 `E02_sadness.png`이다
