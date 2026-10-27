---
id: E07
slug: explaining
character: 하루 (Haru)
alias: 세나 (Sena)
category: assistant   # 조수 업무
expression_ko: 설명
expression_en: Explaining
spec_file: specs/expressions/E07_explaining.md
image_file: images/E07_explaining.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E07 · 설명 (Explaining)

> 이 명세서는 **`images/E07_explaining.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E07`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
차분하게 정보를 전달하는, 조수 업무의 기본 표정.

## 2. 사용 상황
튜토리얼, 기능 소개, 단계별 안내

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 자연스러운 위치에서 한쪽만 살짝 올림 |
| 눈 | 또렷하게 뜬 눈, 보는 사람을 정면으로 응시 |
| 입 | 말하는 도중처럼 작게 벌린 입, 입꼬리 살짝 올림 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 정면, 아주 약간 기울임 |
| 손·제스처 | 검지를 세워 위를 가리킴 |
| 만화 이펙트 | 작은 말풍선 또는 반짝임(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "먼저 이 부분부터 설명드릴게요."
- 세나(예명): "자, 여기서 포인트는요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, calm explaining expression, one eyebrow slightly raised, clear eyes looking at the viewer, mouth slightly open mid-speech with a gentle smile, index finger raised, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 장난스러운 윙크
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E07_explaining.png`이다
