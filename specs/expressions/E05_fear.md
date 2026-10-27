---
id: E05
slug: fear
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 두려움
expression_en: Fear
spec_file: specs/expressions/E05_fear.md
image_file: images/E05_fear.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E05 · 두려움 (Fear)

> 이 명세서는 **`images/E05_fear.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E05`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
겁먹고 움츠러든 상태.

## 2. 사용 상황
경고, 위험한 상황, 무서운 이야기

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽 끝이 올라가며 떨리는 눈썹 |
| 눈 | 눈을 크게 뜨고 동공이 흔들림, 시선은 옆으로 회피 |
| 입 | 입을 살짝 벌리고 아랫입술에 힘이 들어감 |
| 볼·홍조 | 창백한 톤 |
| 머리·자세 | 어깨를 움츠리고 고개를 약간 숙임 |
| 손·제스처 | 양손을 입 앞이나 가슴 앞에 모음 |
| 만화 이펙트 | 떨림 선 2~3줄(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "저, 저기… 이거 괜찮은 거 맞죠?"
- 세나(예명): "으앗, 무서운 건 약하다구요…"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, frightened expression, eyebrows raised and drawn together, wide trembling eyes glancing sideways, lips slightly parted and tense, pale complexion, shoulders hunched, hands held close to the chest, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 공포 장르 수준의 왜곡
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E05_fear.png`이다
