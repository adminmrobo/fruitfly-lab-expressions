---
id: E25
slug: teehee
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장 (확장 표정)
expression_ko: 데헷
expression_en: Teehee (Tehe-pero)
spec_file: specs/haru/expressions/E25_teehee.md
image_file: images/haru/E25_teehee.png
image_status: generated   # pending → generated → approved
core_ref: specs/haru/00_character_core.md
reference_images: [refs/original/haru_sheet.png, refs/original/haru_expressions_6.png]
original_match: "없음 (신규 표정)"
version: 0.1
added: 2026-11-15
extension: true   # E01~E24 공통 세트 밖의 확장 표정 (하루·시아·모아 전용)
---

# 하루(세나) · E25 · 데헷 (Teehee (Tehe-pero))

> 이 명세서는 **`images/haru/E25_teehee.png`** 한 장에만 대응합니다. `E25`는 E01~E24 공통 세트 밖의 **확장 표정**으로, 하루·시아·모아 세 명만 가집니다. 공통 정의: [`specs/extensions/E25_teehee.md`](../../extensions/E25_teehee.md)

## 1. 감정 의도
실수를 들켰을 때 귀엽게 넘어가는 '데헷☆'. 밝고 에너지 있게.

## 2. 사용 상황
작은 실수 들킴, 장난스러운 얼버무림, 쪽지시험 오답 뒤 리액션, 엔딩 컷의 귀여운 마무리

## 3. 원본 대응
없음 (신규 확장 표정). 인터넷 밈 '데헷(테헤페로)'의 **포즈만** 참고합니다. 특정 작품 캐릭터의 디자인은 참고하지 않습니다.

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 윙크한 쪽은 살짝 내려가고, 다른 쪽은 편안한 아치 |
| 눈 | 한쪽 눈은 웃는 곡선(^)으로 감아 윙크, 다른 눈은 뜨고 정면을 봄 · 하이라이트 유지 |
| 입 | 입꼬리를 올린 장난스러운 미소, 혀끝만 입꼬리 쪽으로 살짝 내밂 |
| 볼·피부 | 옅은 분홍 홍조 줄무늬 |
| 머리·자세 | 고개를 한쪽으로 살짝 기울임 |
| 손·제스처 | 한 손으로 V사인을 만들어 윙크한 눈 옆에 댐 (밈 대표 포즈) |
| 만화 이펙트 | 작은 반짝이 2개 |

> 밈 원형에 가장 가까운 V사인 버전.

> **변형 2장** (같은 E25, 손 동작·분위기만 다름): [`E25_teehee_shy.md`](E25_teehee_shy.md) 수줍게 · [`E25_teehee_playful.md`](E25_teehee_playful.md) 장난스럽게

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(분홍+남색 투톤 장발, 정수리 양쪽 번, 앞머리 가운데 남색 줄, 파란 눈, 라벤더 후드, 흰 랩코트, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 하루(본명): "데헷☆ 조건 하나를 빠뜨렸네요!"
- 세나(예명): "에헷, 세나의 실수는 비밀이에요♪"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, playful teehee expression, cute mischievous wink with one eye closed in a happy curved arc, the other eye open and sparkling at the viewer, small playful smile with just the tip of the tongue peeking out at the corner of the mouth, light pink blush lines on the cheeks, head tilted slightly to one side, one hand making a peace V sign right next to the winking eye, two tiny sparkles near the face, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, both eyes open, tongue sticking far out, licking, drooling, mocking face, rude gesture, middle finger
```

## 9. 금지 사항
- 안경 착용 (조수는 안경을 쓰지 않음)
- 헤어 색·번·앞머리 남색 줄 변경
- 라벤더 후드 + 흰 랩코트 이외의 의상
- 다른 표정 ID와 구분되지 않는 결과
- 두 눈을 다 감거나 다 뜸 (윙크가 아님)
- 혀를 길게 내밀거나 핥는 모양 (혀끝만 살짝)
- 놀리는·무례한 손짓

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 윙크(한쪽 눈만 감음) + 혀끝 + 고개 기울임 + 손 동작 네 가지가 모두 보인다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E25_teehee.png`이다
