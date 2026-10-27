---
id: E20
slug: sweat_drop
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장
expression_ko: 식은땀
expression_en: Big Sweat Drop
spec_file: specs/expressions/E20_sweat_drop.md
image_file: images/E20_sweat_drop.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E20 · 식은땀 (Big Sweat Drop)

> 이 명세서는 **`images/E20_sweat_drop.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E20`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
어이없거나 곤란할 때의 큰 땀방울 데포르메.

## 2. 사용 상황
황당한 요청, 어색한 침묵

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 八자로 내려간 눈썹 |
| 눈 | 점에 가까운 작은 눈 또는 반쯤 뜬 무표정한 눈 |
| 입 | 일자 입 또는 어색한 미소 |
| 볼·홍조 | 홍조 없음 |
| 머리·자세 | 정면 |
| 손·제스처 | 손을 쓰지 않거나 어정쩡하게 듦 |
| 만화 이펙트 | 관자놀이 옆 큰 땀방울 1개(만화 기호) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "아… 네… 그렇군요."
- 세나(예명): "어… 그건 좀…"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, comic awkward expression, droopy eyebrows, small blank eyes, flat awkward mouth, one large anime sweat drop on the side of the head, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 실제로 땀에 젖은 사실적인 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E20_sweat_drop.png`이다
