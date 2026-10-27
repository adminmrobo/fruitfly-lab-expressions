---
id: E23
slug: blank_dot_eyes
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장
expression_ko: 멍(점 눈)
expression_en: Blank Dot Eyes
spec_file: specs/expressions/E23_blank_dot_eyes.md
image_file: images/E23_blank_dot_eyes.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E23 · 멍(점 눈) (Blank Dot Eyes)

> 이 명세서는 **`images/E23_blank_dot_eyes.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E23`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
말문이 막히거나 이해가 안 될 때의 무표정 데포르메.

## 2. 사용 상황
엉뚱한 질문, 정보 과부하

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 거의 수평 |
| 눈 | 작은 점(・ ・) 모양 눈 |
| 입 | 작은 일자 입 또는 점 입 |
| 볼·홍조 | 홍조 없음 |
| 머리·자세 | 정면, 움직임 없음 |
| 손·제스처 | 손을 쓰지 않음 |
| 만화 이펙트 | 머리 위 점 3개 또는 회색 그림자(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "…네?"
- 세나(예명): "…방금 뭐라고요?"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, comic blank expression, eyes reduced to tiny dots, flat eyebrows, tiny flat mouth, completely deadpan, three dots floating above the head, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 이목구비 비율이 바뀌어 아이덴티티가 무너지는 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E23_blank_dot_eyes.png`이다
