---
id: E13
slug: neutral
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 기본(중립)
expression_en: Neutral
spec_file: specs/expressions/E13_neutral.md
image_file: images/E13_neutral.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E13 · 기본(중립) (Neutral)

> 이 명세서는 **`images/E13_neutral.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E13`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
모든 표정의 기준이 되는 기본 상태이자 아이덴티티 기준 이미지.

## 2. 사용 상황
대기 화면, 프로필, 비교 기준

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 자연스러운 기본 위치 |
| 눈 | 편안하게 뜬 눈, 정면 응시 |
| 입 | 입꼬리가 아주 살짝 올라간 다문 입 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 정면 |
| 손·제스처 | 양손을 자연스럽게 내리거나 앞에 모음 |
| 만화 이펙트 | 없음 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "안녕하세요, 하루예요."
- 세나(예명): "안녕하세요, 세나입니다!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, neutral default expression, relaxed eyebrows in natural position, calm open eyes looking at the viewer, closed mouth with a very faint smile, facing forward, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 과한 감정 표현 일체
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E13_neutral.png`이다
