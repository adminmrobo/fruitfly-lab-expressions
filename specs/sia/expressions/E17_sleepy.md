---
id: E17
slug: sleepy
character: 시아 (Sia)
category: subtle   # 미묘한 감정
expression_ko: 졸림
expression_en: Sleepy
spec_file: specs/sia/expressions/E17_sleepy.md
image_file: images/sia/E17_sleepy.png
image_status: generated   # pending → generated → approved
core_ref: specs/sia/00_character_core.md
reference_images: [refs/original/sia_sheet.png, images/sia/E13_neutral.png]
original_match: "사용자 일러스트 05_Yawning (하품) · 06_Sleeping (엎드려 잠)"
version: 0.1
---

# 시아 · E17 · 졸림 (Sleepy)

> 이 명세서는 **`images/sia/E17_sleepy.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E17`)로 명세와 이미지가 1:1로 연결됩니다. 하루 `E17`와 같은 표정 정의를 씁니다.

## 1. 감정 의도
나른하고 졸린 상태.

## 2. 사용 상황
새벽 장면, 대기 상태

## 3. 원본 대응
사용자 일러스트 05_Yawning (하품) · 06_Sleeping (엎드려 잠)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 힘이 빠진 낮은 눈썹 |
| 눈 | 반쯤 감긴 눈 |
| 입 | 크게 벌린 하품 입 |
| 볼·피부 | 옅은 홍조 |
| 머리·자세 | 고개를 옆으로 기울임 |
| 손·제스처 | 한 손으로 입을 가림 (원본 05_Yawning) |
| 만화 이펙트 | 눈가에 작은 눈물 1방울 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(흑발 생머리(허리 길이), 옆으로 흘린 앞머리, 머리 장식 없음, 회색 눈, 은색 드롭 귀걸이, 차콜 검정 메이드 원피스 + 큰 회색 리본 + 흰 프릴 앞치마, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- "후아암…"
- "5분만… 눈 붙일게요."

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, sleepy expression, relaxed low eyebrows, half-closed heavy eyes, mouth open in a big yawn covered by one hand, small tear at the corner of one eye, head tilted, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
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
- [ ] 파일명이 `E17_sleepy.png`이다
