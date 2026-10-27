---
id: E18
slug: sulking
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 삐짐
expression_en: Sulking
spec_file: specs/expressions/E18_sulking.md
image_file: images/E18_sulking.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E18 · 삐짐 (Sulking)

> 이 명세서는 **`images/E18_sulking.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E18`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
살짝 토라진 귀여운 불만.

## 2. 사용 상황
장난에 대한 반응, 서운함 표현

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽이 살짝 내려간 눈썹 |
| 눈 | 눈을 가늘게 뜨고 옆으로 흘겨봄 |
| 입 | 삐죽 내민 입 |
| 볼·홍조 | 선명한 홍조 |
| 머리·자세 | 고개를 옆으로 홱 돌림 |
| 손·제스처 | 팔짱 |
| 만화 이펙트 | 없음(코믹한 볼 부풀림은 E22) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "…흥, 몰라요."
- 세나(예명): "치, 저 빼고 다 했단 말이에요?"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, cute sulking pout, slightly lowered inner eyebrows, narrowed eyes glancing sideways, lips pushed out in a pout, blushing cheeks, head turned away, arms crossed, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 진짜 화난 것처럼 보이는 표정
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E18_sulking.png`이다
