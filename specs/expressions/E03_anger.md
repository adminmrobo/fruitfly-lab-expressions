---
id: E03
slug: anger
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 분노
expression_en: Anger
spec_file: specs/expressions/E03_anger.md
image_file: images/E03_anger.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E03 · 분노 (Anger)

> 이 명세서는 **`images/E03_anger.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E03`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
진지하게 화가 난 상태. 공격적이지 않게, 캐릭터다운 선에서.

## 2. 사용 상황
규칙 위반 지적, 단호한 거절

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽 끝이 내려간 V자 눈썹, 미간 주름 1~2줄 |
| 눈 | 눈을 가늘게 뜨고 정면 응시, 하이라이트는 작게 |
| 입 | 이를 살짝 드러내고 꽉 다문 입 또는 일자 입 |
| 볼·홍조 | 약한 붉은 기 |
| 머리·자세 | 정면, 턱을 살짝 당김 |
| 손·제스처 | 주먹 쥔 손(선택) |
| 만화 이펙트 | 없음(코믹 분노는 E22) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "그건 안 돼요. 분명히 말씀드릴게요."
- 세나(예명): "그런 말은 저도 그냥 넘기기 어려워요."

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, serious anger, eyebrows sharply angled down toward the center, slight furrow between brows, narrowed eyes staring straight ahead, mouth pressed tight with teeth slightly visible, chin tucked, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 분노 마크·볼 부풀림(코믹 E22 전용), 무섭게 보이는 표정
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E03_anger.png`이다
