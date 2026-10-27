---
id: E01
slug: joy
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 기쁨
expression_en: Joy
spec_file: specs/expressions/E01_joy.md
image_file: images/E01_joy.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E01 · 기쁨 (Joy)

> 이 명세서는 **`images/E01_joy.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E01`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
순수하게 즐겁고 밝은 상태. 캐릭터를 대표하는 웃음.

## 2. 사용 상황
좋은 소식 전달, 작업 완료, 인사 마무리

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 양 눈썹이 부드럽게 위로 올라간 아치형 |
| 눈 | 눈웃음(아래 눈꺼풀이 올라온 반달형), 하이라이트 유지 |
| 입 | 입을 크게 벌린 활짝 웃음, 윗니 살짝 보임 |
| 볼·홍조 | 옅은 홍조 |
| 머리·자세 | 정면, 고개를 옆으로 5~10° 기울임 |
| 손·제스처 | 양손을 가슴 앞에서 가볍게 모음(선택) |
| 만화 이펙트 | 작은 반짝임 2~3개(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "잘됐어요! 저도 기뻐요."
- 세나(예명): "오늘 방송도 최고였어요!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, bright genuine joyful smile, eyes curved into happy crescents, eyebrows softly raised, mouth open wide in a cheerful smile showing upper teeth, light blush on cheeks, head tilted slightly, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 과도한 데포르메, 눈을 완전히 감은 표현
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E01_joy.png`이다
