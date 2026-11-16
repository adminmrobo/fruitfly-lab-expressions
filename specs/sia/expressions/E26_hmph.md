---
id: E26
slug: hmph
character: 시아 (Sia)
category: comic   # 코믹 과장 (확장 표정)
expression_ko: 흥 (볼 빵빵 뾰로통)
expression_en: Hmph (puffed-cheek pout)
spec_file: specs/sia/expressions/E26_hmph.md
image_file: images/sia/E26_hmph.png
image_status: generated   # pending → generated → approved
core_ref: specs/sia/00_character_core.md
reference_images: [refs/original/sia_sheet.png, images/sia/E13_neutral.png, images/sia/E18_sulking.png]
original_match: "없음 (신규 표정)"
version: 0.1
added: 2026-11-16
extension: true   # E01~E24 공통 세트 밖의 확장 표정 (하루·시아·모아 전용)
variants: [hmph_walkaway]
---

# 시아 · E26 · 흥 (Hmph, puffed-cheek pout)

> 이 명세서는 **`images/sia/E26_hmph.png`** 한 장(1024×1024)에만 대응합니다. `E26`은 E01~E24 공통 세트 밖의 **확장 표정**으로, 하루·시아·모아 세 명만 가집니다. 공통 정의: [`specs/extensions/E26_hmph.md`](../../extensions/E26_hmph.md)

## 1. 감정 의도
말수 적은 시아의 조용한 "…흥". 표정 변화는 작게, 볼도 조금만.

## 2. 사용 상황
샘나거나 서운할 때, 자기만 빼고 진행될 때, 놀림 받은 뒤의 귀여운 리액션, 대결 패배 쪽 방청석 반응

## 3. 원본 대응
없음 (신규 확장 표정). 사용자가 모은 애니 캡처 4장의 **표정 요소만** 글로 옮겼고, 그 작품 캐릭터의 디자인·그림체는 참고하지 않았습니다(캡처는 생성 도구에 첨부하지 않음).

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈썹 | 미간을 모으되 안쪽 끝이 살짝 올라간 "서운한" 찌푸림 |
| 눈 | 턱을 살짝 당기고 반쯤 뜬 회색 눈으로 옆을 흘김 · 하이라이트 유지 |
| 입 | 입술을 꼭 다문 작은 오므림. 입을 벌리거나 이를 보이지 않음 |
| 볼·피부 | 볼을 살짝만 부풀림, 옅은 분홍 홍조 |
| 손·제스처 | 한 손으로 앞치마 끝을 살짝 쥠 |
| 만화 이펙트 | 없음 (조용한 캐릭터라 이펙트를 아낌) |

## 5. 비슷한 표정과의 구분
E18 삐짐(팔짱·고개 돌림)과 달리 팔짱이 없고 볼을 부풀립니다. E22 뿔남과 달리 분노 마크·김 같은 화난 이펙트가 없습니다.

## 6. 대사 예시
- …흥.
- …모르는 척할 거예요.

## 7. 생성 프롬프트 (EN)
> 실제 그림은 2026-11-17 사용자 Genspark 생성 결과입니다. 지침서: [`PROMPTS_E26_hmph.md`](../../extensions/PROMPTS_E26_hmph.md)
```text
Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses, quiet hmph pouting expression, chin tucked slightly down, half-lidded calm gray eyes glancing sideways at the viewer with a cool sulky look, cheeks only slightly puffed, lips pressed into a tiny pursed pout, faint pink blush, one hand lightly holding the edge of her apron, no extra effects, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, hair ornament, glasses, colored hair, blonde hair, brown hair, short hair, different eye color, different outfit, extra fingers, deformed hands, both eyes closed, wide open mouth, shouting, teeth showing, fangs, tears streaming, crossed arms, anger vein mark, deep red face, crying, copy of an existing anime character, different art style, smooth anime cel shading
```

## 9. 금지 사항
- 진짜 화난 얼굴, 이를 드러내거나 입을 벌림
- 팔짱(E18과 겹침), 분노 마크(E22와 겹침)
- 아이덴티티 고정값 변경 (헤어스타일, 색상, 의상, 액세서리)

## 10. 검수 체크리스트
- [x] E13과 같은 캐릭터로 보인다
- [x] 부푼 볼 + 다문 입 + 서운한 눈썹이 보인다
- [x] 4절 시선·손 동작이 반영됐다
- [x] 팔짱·치아·혀·글자·빨간 분노 마크가 없다
- [x] 파일명 `E26_hmph.png`
