---
id: E03
slug: anger
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 분노
expression_en: Anger
spec_file: specs/haru/expressions/E03_anger.md
image_file: images/haru/E03_anger.png
image_status: generated   # pending → generated → approved
core_ref: specs/haru/00_character_core.md
reference_images: [refs/original/haru_sheet.png, refs/original/haru_expressions_6.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# 하루(세나) · E03 · 분노 (Anger)

> 이 명세서는 **`images/haru/E03_anger.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E03`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
진지하게 화가 난 상태. 공격적이지 않게, 캐릭터다운 선에서.

## 2. 사용 상황
규칙 위반 지적, 단호한 거절

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽 끝이 내려간 V자, 미간 주름 |
| 눈 | 눈을 가늘게 뜨고 정면 응시 |
| 입 | 꽉 다문 일자 입 |
| 볼·피부 | 약한 붉은 기 |
| 머리·자세 | 정면, 턱을 당김 |
| 손·제스처 | 팔짱(선택) |
| 만화 이펙트 | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(분홍+남색 투톤 장발, 정수리 양쪽 번, 앞머리 가운데 남색 줄, 파란 눈, 라벤더 후드, 흰 랩코트, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 하루(본명): "그건 안 돼요. 분명히 말씀드릴게요."
- 세나(예명): "그런 말은 그냥 넘기기 어려워요."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat, serious anger, eyebrows angled sharply down, narrowed blue eyes staring straight ahead, mouth pressed into a tight line, chin tucked, arms crossed, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, glasses, short hair, different hair color, missing hair buns, missing navy streak, different eye color, different outfit, extra fingers, deformed hands
```

## 9. 금지 사항
- 원본 "결의" 표정(E12)과 혼동되는 주먹 포즈
- 안경 착용 (조수는 안경을 쓰지 않음)
- 헤어 색·번·앞머리 남색 줄 변경
- 라벤더 후드 + 흰 랩코트 이외의 의상
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E03_anger.png`이다
