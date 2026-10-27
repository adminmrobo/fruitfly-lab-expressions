---
id: E17
slug: sleepy
character: 하루 (Haru)
alias: 세나 (Sena)
category: subtle   # 미묘한 감정
expression_ko: 졸림
expression_en: Sleepy
spec_file: specs/expressions/E17_sleepy.md
image_file: images/E17_sleepy.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E17 · 졸림 (Sleepy)

> 이 명세서는 **`images/E17_sleepy.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E17`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
나른하고 졸린 상태.

## 2. 사용 상황
밤 인사, 대기 상태, 휴식

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 힘이 빠진 낮은 눈썹 |
| 눈 | 반쯤 감긴 눈, 하품 눈물 한 방울 |
| 입 | 하품하는 입 또는 살짝 벌린 입 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 고개를 옆으로 기울임 |
| 손·제스처 | 한 손으로 눈을 비빔 |
| 만화 이펙트 | Zzz 표시(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "후암… 조금 졸리네요."
- 세나(예명): "으음… 5분만 더…"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, sleepy drowsy expression, relaxed low eyebrows, half-closed heavy eyes with a small tear from yawning, mouth open in a yawn, head tilted, hand rubbing one eye, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 생각(E09)과 헷갈리는 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E17_sleepy.png`이다
