---
id: E02
slug: sadness
character: JUPANBOT
alias: 주판봇 (AbaBot)
category: basic   # 기본 감정
expression_ko: 슬픔
expression_en: Sadness
spec_file: specs/jupanbot/expressions/E02_sadness.md
image_file: images/jupanbot/E02_sadness.png
image_status: vector-v1   # vector-v1 → generated → approved
core_ref: specs/jupanbot/00_character_core.md
reference_images: [refs/original/jupanbot_ref_genspark_v0.png]
version: 2.0
---

# 주판봇 · E02 · 슬픔 (Sadness)

> 이 명세서는 **`images/jupanbot/E02_sadness.png`** 한 장에만 대응합니다. 지금 이미지는 벡터 그림 v1입니다(원본 SVG: ahnboat_lab_explainer/packs/character/jupanbot_vector/).

## 1. 감정 의도
풀이 죽고 속상한 상태.

## 2. 사용 상황
예측 실패, 손실, 실망스러운 결과

## 3. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈 (민트 픽셀) | 아래로 처진 눈 + 픽셀 눈물 한 방울씩 |
| 입 (민트 픽셀) | 뒤집힌 곡선 입 |
| 화면 효과 | 화면이 조금 어두워짐 |
| 자세·기울기 | 몸체를 앞으로 숙임 |
| 팔·손·주판 | 주판을 한 손에 축 늘어뜨림 |
| 외부 이펙트 | 없음 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(베이지 상자형 CRT 몸체, 짙은 초록 화면 + 민트 픽셀 얼굴, 끝에 주판알이 달린 짧은 안테나, 회색 마디형 팔과 벙어리장갑 손, 무한궤도 두 개, 나무 주판)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 대사 1: "숫자가 저를 배신했어요…"
- 대사 2: "이번엔 계산이 빗나갔네요."

## 6. 생성 프롬프트 (EN) — Genspark에 그대로 붙여 넣기
참조 이미지 `refs/original/jupanbot_ref_genspark_v0.png`를 함께 넣으세요.
```text
JUPANBOT (AbaBot), a cute retro computer robot mascot, flat vector cartoon illustration, clean bold outlines, flat colors with very light soft shading. Boxy beige CRT-monitor body with rounded corners and thick dark brown outlines, a large dark green screen on the front where the face is drawn only with simple mint-green pixel blocks, a short thin antenna on a small square base topped with one tiny red-brown abacus bead, gray segmented arms with rounded gray mitten hands, two small dark gray tank treads instead of legs. Signature prop: a small traditional wooden abacus with red-brown beads and a horizontal divider beam, one bead above and four below on each rod. Limited palette: beige, dark green, mint green, wood brown, red-brown, gray. Sad face, droopy mint pixel eyes with one small pixel tear each and an upside-down curved mouth, the screen slightly dimmed, body tilted forward, the abacus hanging limply from one hand. Full body, centered, facing the viewer, same framing as the reference image, plain flat white background, no text, no letters, no numbers, no words, same character as the reference image, identical design and colors.
```

## 7. 네거티브 프롬프트 (EN)
```text
white glossy round head, black pill-shaped screen, yellow or golden eyes, round ball antenna knob, cyan chest light, floating or hovering, legs, gold coins, 3D render, photorealistic, blurry, off-model, inconsistent character, face drawn outside the screen, text, letters, numbers, watermark, logo, multiple characters, extra limbs
```

## 8. 금지 사항
- 화면 바깥(베이지 몸체)에 얼굴 요소를 그리는 결과
- 다리가 생기거나 공중에 떠 있는 결과
- 흰 둥근 머리·노란 눈·공 모양 안테나·금화 등 Money-Robo 특징이 섞인 결과
- 글자·숫자가 들어간 결과

## 9. 검수 체크리스트
- [ ] `E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E02_sadness.png`이다
