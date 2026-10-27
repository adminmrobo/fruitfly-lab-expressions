---
id: E02
slug: sadness
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 슬픔
expression_en: Sadness
spec_file: specs/expressions/E02_sadness.md
image_file: images/E02_sadness.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E02 · 슬픔 (Sadness)

> 이 명세서는 **`images/E02_sadness.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E02`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
조용히 가라앉은 슬픔. 울기 직전 단계까지만.

## 2. 사용 상황
나쁜 소식, 실패에 공감, 이별 장면

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽 끝이 올라간 八자 눈썹 |
| 눈 | 눈꺼풀이 반쯤 내려오고 시선은 아래, 눈가에 고인 눈물(흘리지 않음) |
| 입 | 입꼬리가 내려간 작게 다문 입 |
| 볼·홍조 | 홍조 없음, 피부 톤 약간 차분하게 |
| 머리·자세 | 고개를 10° 숙임 |
| 손·제스처 | 한 손을 가슴에 얹음(선택) |
| 만화 이펙트 | 없음 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "그건… 정말 속상했겠어요."
- 세나(예명): "오늘은 조금 아쉬운 날이네요…"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, quiet sadness, inner ends of eyebrows raised, eyes half-lidded looking down, tears welling in the eyes but not falling, small closed mouth with corners turned down, head lowered slightly, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 폭포 눈물(E21과 구분), 과한 오열
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E02_sadness.png`이다
