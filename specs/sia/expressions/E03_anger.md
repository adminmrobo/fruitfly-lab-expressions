---
id: E03
slug: anger
character: 시아 (Sia)
category: basic   # 기본 감정
expression_ko: 분노
expression_en: Anger
spec_file: specs/sia/expressions/E03_anger.md
image_file: images/sia/E03_anger.png
image_status: generated   # pending → generated → approved
core_ref: specs/sia/00_character_core.md
reference_images: [refs/original/sia_sheet.png, images/sia/E13_neutral.png]
original_match: "없음 (신규 표정)"
version: 0.1
---

# 시아 · E03 · 분노 (Anger)

> 이 명세서는 **`images/sia/E03_anger.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E03`)로 명세와 이미지가 1:1로 연결됩니다. 하루 `E03`와 같은 표정 정의를 씁니다.

## 1. 감정 의도
진지하게 화가 난 상태. 공격적이지 않게, 캐릭터다운 선에서.

## 2. 사용 상황
규칙 위반 지적, 단호한 거절

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 안쪽 끝이 내려간 V자, 미간 주름 |
| 눈 | 눈을 가늘게 뜨고 정면 응시 |
| 입 | 꽉 다문 일자 입 |
| 볼·피부 | 약한 붉은 기 |
| 머리·자세 | 정면, 턱을 당김 |
| 손·제스처 | 팔짱(선택) |
| 만화 이펙트 | 없음 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(흑발 생머리(허리 길이), 옆으로 흘린 앞머리, 머리 장식 없음, 회색 눈, 은색 드롭 귀걸이, 차콜 검정 메이드 원피스 + 큰 회색 리본 + 흰 프릴 앞치마, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- "그건 규칙 위반이에요."
- "두 번 말하지 않을게요."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, serious anger, eyebrows angled sharply down, narrowed gray eyes staring straight ahead, mouth pressed into a tight line, chin tucked, arms crossed, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, hair ornament, glasses, colored hair, blonde hair, brown hair, short hair, different eye color, different outfit, extra fingers, deformed hands
```

## 9. 금지 사항
- 머리띠·머리핀 등 머리 장식 (시아는 머리 장식이 없음 — 모아와 구별)
- 안경 착용
- 흑발 이외의 머리색, 짧은 머리
- 메이드 원피스 + 앞치마 이외의 의상
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 설정 시트·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 하루·박사와 같다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E03_anger.png`이다
