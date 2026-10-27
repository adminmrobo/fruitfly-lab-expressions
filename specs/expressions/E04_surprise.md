---
id: E04
slug: surprise
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 놀람
expression_en: Surprise
spec_file: specs/expressions/E04_surprise.md
image_file: images/E04_surprise.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E04 · 놀람 (Surprise)

> 이 명세서는 **`images/E04_surprise.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E04`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
예상 못한 일에 대한 순간적인 놀람. 긍정도 부정도 아닌 중립.

## 2. 사용 상황
새 정보 발견, 예상 밖의 질문

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 눈썹이 높이 올라가 이마 쪽으로 이동 |
| 눈 | 눈을 크게 뜨고 동공은 작게, 흰자가 더 보임 |
| 입 | 작은 O자 입 |
| 볼·홍조 | 홍조 없음 |
| 머리·자세 | 고개를 살짝 뒤로 젖힘 |
| 손·제스처 | 양손을 어깨 높이로 살짝 듦(선택) |
| 만화 이펙트 | 머리 옆 느낌표 1개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "어? 정말요?"
- 세나(예명): "헉, 이건 예상 못 했어요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, surprised expression, eyebrows raised high, eyes wide open with small pupils, mouth in a small round O shape, head pulled back slightly, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 흰자만 남는 충격 표현(E24 전용)
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E04_surprise.png`이다
