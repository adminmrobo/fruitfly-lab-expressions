---
id: E20
slug: sweat_drop
character: 초파리 (Fruit Fly)
alias: 초파리 연구원
category: comic   # 코믹 과장
expression_ko: 식은땀
expression_en: Big Sweat Drop
spec_file: specs/fruitfly/expressions/E20_sweat_drop.md
image_file: images/fruitfly/E20_sweat_drop.png
image_status: generated   # pending → generated → approved
core_ref: specs/fruitfly/00_character_core.md
reference_images: [refs/original/fruitfly_sprites_6.png, refs/original/keyart_rivals.png]
original_match: "없음 (신규 표정)"
version: 1.1
---

# 초파리 · E20 · 식은땀 (Big Sweat Drop)

> 이 명세서는 **`images/fruitfly/E20_sweat_drop.png`** 한 장에만 대응합니다. 파일명 앞의 ID(`E20`)로 명세와 이미지가 1:1로 연결됩니다.

## 1. 감정 의도
어이없거나 곤란할 때의 큰 땀방울 데포르메.

## 2. 사용 상황
황당한 요청, 어색한 침묵

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 눈 (빨간 겹눈 + 눈꺼풀·하이라이트) | 겹눈 위 작은 흰 점 하이라이트만 |
| 입 | 일자 입 |
| 헬멧·케이블 | 케이블 정지 |
| 날개 | 날개 정지 |
| 몸·자세 | 정면 |
| 앞발 제스처 | 움직임 없음 |
| 만화 이펙트 | 헬멧 옆 큰 땀방울 1개 |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 **아이덴티티 고정값**(검은 곤충 몸통, 큰 빨간 겹눈, 남색 레트로 헬멧 + 노란·흰 줄 + 측면 볼트, 뒤로 늘어진 자홍·보라·파랑 케이블, 작은 흰 가운 + 검은 조끼, 반투명 맥 날개 2장, 다리 6개, 픽셀 아트 화풍)을 그대로 따릅니다. 이 표정에서 바꿀 수 있는 것은 **4절의 항목뿐**입니다.

## 6. 대사 예시
- 대사 1: "…그건 좀."
- 대사 2: "…그 예측, 근거가 뭐야?"

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
the Fruit Fly, a tiny expressive cartoon fruit fly researcher with a dark charcoal-black segmented insect body, large glossy red compound eyes, a retro dark blue helmet with a yellow-white center stripe and small round side bolts, colorful dangling cables in magenta, purple and blue curving from the back of the helmet, a tiny white lab coat over a black vest, translucent veined wings, six thin black legs with the front pair used like hands, comic awkward expression, tiny dot white highlights on the red compound eyes, flat mouth, frozen still, one big anime sweat drop beside the helmet, full body sprite centered, facing viewer, same framing as the reference sprite sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat medium gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, cute big anime pupils replacing compound eyes, green eyes, missing helmet, missing cables, no lab coat, realistic insect macro photo, gross hairy bug, extra wings, more than six legs, human body
```

## 9. 금지 사항
- 겹눈을 사람 눈처럼 바꾸는 결과 (겹눈 위 하이라이트·눈꺼풀·작은 동공 표현만 허용)
- 헬멧·케이블·흰 가운 누락
- 다리·날개 개수 변경, 징그러운 실사 곤충 표현
- 다른 표정 ID와 구분되지 않는 결과

## 10. 검수 체크리스트
- [ ] 원본 참조 이미지·`E13_neutral`과 나란히 놓았을 때 같은 캐릭터로 보인다
- [ ] 4절의 부위별 지시가 모두 반영됐다
- [ ] 16비트 픽셀 아트 화풍이 유지됐다
- [ ] 금지 사항에 해당하는 표현이 없다
- [ ] 파일명이 `E20_sweat_drop.png`이다
