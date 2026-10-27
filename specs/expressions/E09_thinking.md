---
id: E09
slug: thinking
character: 하루 (Haru)
alias: 세나 (Sena)
category: assistant   # 조수 업무
expression_ko: 생각
expression_en: Thinking
spec_file: specs/expressions/E09_thinking.md
image_file: images/E09_thinking.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E09 · 생각 (Thinking)

> 이 명세서는 **`images/E09_thinking.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E09`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
정보를 정리하거나 고민하는 중.

## 2. 사용 상황
답변 준비, 로딩 중, 질문 검토

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 한쪽 눈썹은 올리고 다른 쪽은 살짝 내림 |
| 눈 | 시선은 위쪽 대각선 |
| 입 | 한쪽으로 모은 작은 입 |
| 볼·홍조 | 홍조 없음 |
| 머리·자세 | 고개를 15° 기울임 |
| 손·제스처 | 검지를 턱에 댐 |
| 만화 이펙트 | 머리 위 작은 물음표 또는 생각 점 3개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "음… 잠깐만 정리해 볼게요."
- 세나(예명): "흐음, 이건 좀 고민되는데요?"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, thoughtful expression, one eyebrow raised and the other slightly lowered, eyes looking up diagonally, small mouth pushed to one side, head tilted, index finger touching the chin, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 눈 감음, 졸린 표정(E17)과 헷갈리는 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E09_thinking.png`이다
