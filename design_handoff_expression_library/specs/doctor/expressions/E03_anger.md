---
id: E03
slug: anger
character: 박사 (Professor)
alias: 없음
category: basic   # 기본 감정
expression_ko: 분노
expression_en: Anger
spec_file: specs/doctor/expressions/E03_anger.md
image_file: images/doctor/E03_anger.png
image_status: generated   # pending → generated → approved
core_ref: specs/doctor/00_character_core.md
reference_images: [refs/original/doctor_sheet.png, refs/original/keyart_rivals.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# 박사 · E03 · 분노 (Anger)

> 이 명세서는 **`images/doctor/E03_anger.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E03`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
진지하게 화가 난 상태. 공격적이지 않게, 캐릭터다운 선에서.

## 2. 사용 상황
규칙 위반 지적, 단호한 거절

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 (굵은 검은 눈썹) | 미간으로 깊게 내려간 V자 |
| 눈·안경 | 안경 렌즈가 하얗게 번쩍여 눈이 가려짐 |
| 입 | 꽉 다문 입 |
| 볼·피부 | 붉은 기 |
| 머리·자세 | 턱을 당기고 정면 |
| 손·제스처 | 검지로 안경을 밀어 올림 |
| 이펙트 (보라 불꽃 포함) | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(짙은 숯색 뾰족 머리 + 앞머리 흰 줄, 뒤쪽 작은 꽁지머리, 굵은 검은 눈썹, 청록 테 안경, 흰 가운 + 검은 조끼·넥타이, 치비 비율, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 대사 1: "그건 과학에 대한 모독이네."
- 대사 2: "실험실 규칙을 어겼군."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks, stern serious anger, thick eyebrows sharply angled down into a deep V, glasses lenses flashing white hiding the eyes, mouth pressed tight, chin tucked, pushing up the glasses with one finger, chibi upper body portrait from waist up, facing viewer, centered, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, no glasses, round glasses, thin eyebrows, beard, mustache, bald, different hair color, missing white streak, realistic proportions, extra fingers, deformed hands
```

## 9. 금지 사항
- 안경이 사라지거나 테 색(청록)이 바뀌는 결과
- 수염 추가 (원본에 수염 없음)
- 치비 비율 변경
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E03_anger.png`이다
