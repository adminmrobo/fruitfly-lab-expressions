---
id: E14
slug: sheepish
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 머쓱함
expression_en: Sheepish
spec_file: specs/expressions/E14_sheepish.md
image_file: images/E14_sheepish.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E14 · 머쓱함 (Sheepish)

> 이 명세서는 **`images/E14_sheepish.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E14`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
칭찬받거나 사소한 실수를 한 뒤의 쑥스러움.

## 2. 사용 상황
칭찬에 대한 반응, 작은 실수 무마

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 살짝 八자 |
| 눈 | 시선을 옆으로 피하며 눈웃음 |
| 입 | 어색하게 웃는 입, 입꼬리 한쪽만 올라감 |
| 볼·홍조 | 선명한 홍조 |
| 머리·자세 | 고개를 살짝 숙이고 기울임 |
| 손·제스처 | 한 손으로 뒷머리나 볼을 긁음 |
| 만화 이펙트 | 작은 땀방울 1개 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "에헤헤… 그런가요?"
- 세나(예명): "아하하, 들켜 버렸네요."

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, sheepish embarrassed smile, slightly worried eyebrows, eyes glancing away while smiling, awkward lopsided grin, noticeable blush, hand scratching the back of the head, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 당황(E15)처럼 눈이 커지는 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E14_sheepish.png`이다
