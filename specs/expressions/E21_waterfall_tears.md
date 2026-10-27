---
id: E21
slug: waterfall_tears
character: 하루 (Haru)
alias: 세나 (Sena)
category: comic   # 코믹 과장
expression_ko: 울먹(폭포 눈물)
expression_en: Waterfall Tears
spec_file: specs/expressions/E21_waterfall_tears.md
image_file: images/E21_waterfall_tears.png
image_status: pending   # pending → generated → approved
core_ref: specs/00_character_core.md
version: 1.0
---

# E21 · 울먹(폭포 눈물) (Waterfall Tears)

> 이 명세서는 **`images/E21_waterfall_tears.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E21`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
과장된 코믹 울음.

## 2. 사용 상황
게임 패배, 아까운 실수, 장난스러운 슬픔

## 3. 얼굴 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 크게 八자 |
| 눈 | 눈을 꽉 감거나 물결 모양 눈 |
| 입 | 크게 벌리고 우는 물결선 입 |
| 볼·홍조 | 붉은 볼 |
| 머리·자세 | 고개를 젖히거나 숙임 |
| 손·제스처 | 양 주먹을 눈 밑에 댐 |
| 만화 이펙트 | 양쪽 눈에서 폭포처럼 흐르는 만화 눈물 |

## 4. 고정 항목 (변경 금지)
`00_character_core.md`의 **아이덴티티 고정값**(헤어, 눈 색, 얼굴형, 의상, 화풍, 구도, 배경)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **3절의 항목뿐**입니다.

## 5. 대사 예시
- 하루(본명): "으아앙, 다 날아갔어요…!"
- 세나(예명): "흐엥, 이건 너무하잖아요~!"

## 6. 생성 프롬프트 (EN)
```text
{{CHARACTER_CORE_EN}}, comic crying, eyebrows strongly slanted, eyes squeezed shut, wide wavy crying mouth, streams of cartoon waterfall tears flowing from both eyes, fists under eyes, {{FRAMING_EN}}, {{STYLE_EN}}, {{BACKGROUND_EN}}, same character as reference image, consistent face and outfit
```

## 7. 네거티브 프롬프트 (EN)
```text
{{NEGATIVE_BASE_EN}}, different hairstyle, different eye color, different outfit, extra fingers, deformed hands, multiple characters, text, watermark
```

## 8. 금지 사항
- 현실적인 오열
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)
- 다른 표정 ID와 구분되지 않는 결과

## 9. 검수 체크리스트
- [ ] 기준 이미지(`E13_neutral`)와 나란히 놓았을 때 같은 인물로 보인다
- [ ] 3절의 부위별 지시가 모두 반영됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E21_waterfall_tears.png`이다
