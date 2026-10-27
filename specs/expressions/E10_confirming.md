---
id: E10
slug: confirming
character: 하루 (Haru)
alias: 세나 (Sena)
category: assistant   # 조수 업무
expression_ko: 확인
expression_en: Confirming
spec_file: specs/expressions/E10_confirming.md
image_file: images/E10_confirming.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E10 · 확인 (Confirming)

> 이 명세서는 **`images/E10_confirming.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E10`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
정확히 확인했다는 자신감 있는 표시.

## 2. 사용 상황
정답, 처리 완료, 동의

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 자연스럽게 살짝 올림 |
| 눈 | 한쪽 윙크 또는 양쪽 모두 또렷하게 뜸 |
| 입 | 자신 있는 미소, 입꼬리 한쪽이 더 올라감 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 정면, 살짝 끄덕이는 각도 |
| 손·제스처 | OK 사인 또는 엄지척 |
| 만화 이펙트 | 체크 마크나 반짝임 1개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "네, 확인했어요!"
- 세나(예명): "오케이, 완벽해요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, confident confirming expression, light raised eyebrows, playful wink or bright open eyes, confident smile, slight nod, hand making an OK sign or thumbs up, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 손가락 개수 오류
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E10_confirming.png`이다
