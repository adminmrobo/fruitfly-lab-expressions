---
id: E06
slug: disgust
character: 하루 (Haru)
alias: 세나 (Sena)
category: basic   # 기본 감정
expression_ko: 혐오
expression_en: Disgust
spec_file: specs/expressions/E06_disgust.md
image_file: images/E06_disgust.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E06 · 혐오 (Disgust)

> 이 명세서는 **`images/E06_disgust.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E06`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
불쾌하거나 싫은 것을 봤을 때. 귀엽게 찡그리는 정도까지만.

## 2. 사용 상황
싫은 음식, 지저분한 데이터, 스팸

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 한쪽 눈썹만 내려가거나 양쪽 미간을 찡그림 |
| 눈 | 눈을 가늘게 뜨고 시선을 비스듬히 피함 |
| 입 | 한쪽 입꼬리를 끌어내리고 아랫입술을 내밂 |
| 볼·홍조 | 홍조 없음 |
| 머리·자세 | 고개를 옆으로 돌리고 몸을 뒤로 뺌 |
| 손·제스처 | 손바닥을 앞으로 내밀어 막는 동작(선택) |
| 만화 이펙트 | 작은 물결선(선택) |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "으… 그건 좀 사양할게요."
- 세나(예명): "우웩, 그건 진짜 패스!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, mild cute disgust, scrunched brows, narrowed eyes looking away sideways, one corner of the mouth pulled down with lower lip pushed out, head turned away and leaning back, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 캐릭터 호감도를 해칠 만큼 과한 혐오
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E06_disgust.png`이다
