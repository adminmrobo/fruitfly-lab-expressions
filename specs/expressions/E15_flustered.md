---
id: E15
slug: flustered
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 당황
expression_en: Flustered
spec_file: specs/expressions/E15_flustered.md
image_file: images/E15_flustered.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E15 · 당황 (Flustered)

> 이 명세서는 **`images/E15_flustered.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E15`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
갑작스러운 상황에 어쩔 줄 몰라 하는 상태.

## 2. 사용 상황
예상 밖의 질문, 돌발 상황, 놀림받을 때

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 높이 올라가 흔들리는 눈썹 |
| 눈 | 눈을 크게 뜨고 동공이 흔들림(소용돌이는 약하게) |
| 입 | 물결 모양 입 |
| 볼·홍조 | 얼굴 전체가 붉어짐 |
| 머리·자세 | 고개를 움츠림 |
| 손·제스처 | 양손을 앞에서 휘저음 |
| 만화 이펙트 | 땀방울 2~3개 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "네? 아, 아니 그게요…!"
- 세나(예명): "잠, 잠깐만요! 그건 아니고요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, flustered panicked expression, raised wavering eyebrows, wide shaky eyes, wavy flustered mouth, face flushed red, hands waving in front, small sweat drops, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 두려움(E05)처럼 창백한 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E15_flustered.png`이다
