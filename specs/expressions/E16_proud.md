---
id: E16
slug: proud
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 뿌듯함
expression_en: Proud
spec_file: specs/expressions/E16_proud.md
image_file: images/E16_proud.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E16 · 뿌듯함 (Proud)

> 이 명세서는 **`images/E16_proud.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E16`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
스스로 잘 해냈다는 만족감.

## 2. 사용 상황
결과물 공개, 문제 해결

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 자신감 있게 올라간 눈썹 |
| 눈 | 지그시 감거나 반쯤 감은 만족한 눈 |
| 입 | 입꼬리를 크게 올린 다문 미소 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 턱을 살짝 들고 정면 |
| 손·제스처 | 허리에 손을 얹거나 가슴을 폄 |
| 만화 이펙트 | 반짝임 1~2개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "후후, 이번엔 꽤 잘한 것 같아요."
- 세나(예명): "어때요? 제법이죠?"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, proud satisfied expression, confident raised eyebrows, eyes gently closed or half-closed in satisfaction, wide closed-mouth smile, chin lifted, hands on hips, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 거만하거나 비꼬는 느낌
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E16_proud.png`이다
