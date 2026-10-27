---
id: E12
slug: cheering
character: 하루 (Haru)
alias: 세나 (Sena)
category: assistant   # 조수 업무
expression_ko: 응원
expression_en: Cheering
spec_file: specs/expressions/E12_cheering.md
image_file: images/E12_cheering.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E12 · 응원 (Cheering)

> 이 명세서는 **`images/E12_cheering.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E12`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
사용자에게 힘을 북돋는 표정.

## 2. 사용 상황
도전 격려, 시작 알림, 목표 달성 응원

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 힘 있게 올라간 눈썹 |
| 눈 | 반짝이는 또렷한 눈, 하이라이트 크게 |
| 입 | 입을 크게 벌리고 외치는 듯한 미소 |
| 볼·홍조 | 선명한 홍조 |
| 머리·자세 | 정면, 몸을 살짝 앞으로 |
| 손·제스처 | 주먹을 쥐고 가슴 높이로 들어 올림(화이팅) |
| 만화 이펙트 | 반짝임이나 작은 별(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "할 수 있어요! 제가 옆에 있을게요."
- 세나(예명): "다들 화이팅! 끝까지 가 봐요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, energetic cheering expression, eyebrows lifted with determination, bright sparkling eyes, mouth open in an encouraging shout-smile, rosy cheeks, leaning forward, fist raised at chest level, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 분노로 오해할 수 있는 V자 눈썹
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E12_cheering.png`이다
