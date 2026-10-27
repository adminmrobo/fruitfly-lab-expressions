---
id: E11
slug: apologizing
character: 하루 (Haru)
alias: 세나 (Sena)
category: assistant   # 조수 업무
expression_ko: 사과
expression_en: Apologizing
spec_file: specs/expressions/E11_apologizing.md
image_file: images/E11_apologizing.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E11 · 사과 (Apologizing)

> 이 명세서는 **`images/E11_apologizing.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E11`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
진심으로 미안해하는 태도. 비굴하지 않게.

## 2. 사용 상황
오류 안내, 지연, 실수 인정

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 八자로 내려간 눈썹 |
| 눈 | 눈을 살짝 내리깐 미안한 시선 |
| 입 | 입꼬리를 살짝 내린 작은 입 또는 어색한 미소 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 고개를 15~20° 숙여 인사 |
| 손·제스처 | 양손을 앞에 모으거나 손바닥을 맞댐 |
| 만화 이펙트 | 작은 땀방울 1개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "죄송해요, 제가 놓쳤어요."
- 세나(예명): "미안해요! 다음엔 더 잘할게요."

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, sincere apologetic expression, eyebrows tilted down in a worried shape, eyes lowered, small mouth with slightly downturned corners, head bowed, hands clasped together in front, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 울음, 과하게 비굴한 태도
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E11_apologizing.png`이다
