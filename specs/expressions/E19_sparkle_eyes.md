---
id: E19
slug: sparkle_eyes
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장
expression_ko: 반짝눈(감동·기대)
expression_en: Sparkling Eyes
spec_file: specs/expressions/E19_sparkle_eyes.md
image_file: images/E19_sparkle_eyes.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E19 · 반짝눈(감동·기대) (Sparkling Eyes)

> 이 명세서는 **`images/E19_sparkle_eyes.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E19`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
기대감이나 감동으로 눈이 반짝이는 데포르메 표현.

## 2. 사용 상황
선물, 새 기능 공개, 맛있는 음식

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 크게 올라간 눈썹 |
| 눈 | 눈 안에 별이나 다이아 모양의 큰 하이라이트 여러 개 |
| 입 | 크게 벌린 감탄의 입 |
| 볼·홍조 | 선명한 홍조 |
| 머리·자세 | 몸을 앞으로 내밂 |
| 손·제스처 | 양손을 볼 옆이나 가슴 앞에 모음 |
| 만화 이펙트 | 주변에 반짝임과 별 여러 개 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "우와… 이거 진짜 제 거예요?"
- 세나(예명): "대박! 너무 예쁘잖아요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, comic sparkling eyes, large star-shaped highlights filling the eyes, eyebrows raised high, mouth wide open in awe, rosy cheeks, leaning forward, hands clasped near cheeks, sparkles around, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 하이라이트 때문에 눈 모양이 무너지는 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E19_sparkle_eyes.png`이다
