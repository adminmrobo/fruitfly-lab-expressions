---
id: E18
slug: sulking
character: 미공개 X3 · 꼬마
category: subtle   # 미묘한 감정
expression_ko: 삐짐
expression_en: Sulking
spec_file: specs/x3/expressions/E18_sulking.md
image_file: images/x3/E18_sulking.png
image_status: pending   # pending → generated → approved
core_ref: specs/x3/00_character_core.md
reference_images: [images/_sheets/spares_sheet.png, images/x3/E13_neutral.png]
original_match: "없음 (신규 표정)"
version: 0.1
---

# 미공개 X3 · 꼬마 · E18 · 삐짐 (Sulking)

> 이 명세서는 **`images/x3/E18_sulking.png`** 한 장에만 대응합니다. 실루엣 슬롯이라 흰 점 눈·입선·이펙트로만 표정을 냅니다.

## 1. 감정 의도
살짝 토라진 귀여운 불만.

## 2. 사용 상황
서운함, 장난 리액션

## 3. 원본 대응
없음 (신규 표정)

## 4. 부위별 지시
| 부위 | 지시 |
|---|---|
| 흰 점 눈 | 흘겨보는 점 눈 |
| 흰 입선 | 삐죽 내민 짧은 선 |
| 볼 | 분홍 픽셀 유지 |
| 외곽 모양 | 고양이 귀 후드, 손을 덮는 큰 랩코트, 작은 몸 (고정) |
| 포인트 색 | 노랑 방울 (고정) |

## 5. 고정 항목 (변경 금지)
`00_character_core.md` 2절의 실루엣 채색·외곽 모양·포인트 색을 그대로 따릅니다.

## 6. 대사 예시
- "(흥)" — 미공개 슬롯은 말 대신 소리만 냅니다

## 7. 생성 프롬프트 (EN) — 완성형, 그대로 붙여 넣기
```text
a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, wearing a lab coat whose shape is visible only as silhouette, friendly and cute, not scary, very small chibi silhouette wearing a hood with cat ears, oversized lab coat with long sleeves covering the hands, two hood drawstrings ending in small yellow (#F2C744) pompoms as the only colored part, dot eyes narrowed and glancing sideways, pouting short mouth line, cheeks puffed, arms crossed, bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet, detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words, plain flat light gray background, same character as the reference image, identical design and colors
```

## 8. 네거티브 프롬프트 (EN)
```text
scary, horror, villain, menacing smile, sharp teeth, bald head, realistic human proportions, glowing red eyes, full color clothing, visible face details, detailed eyes with irises, text, letters, question mark symbol, watermark, multiple characters
```

## 9. 금지 사항
- 얼굴·옷의 실제 색이나 세부(눈동자·머리색)가 드러남
- 무서운 인상(악당 미소, 날카로운 이, 빨간 눈)
- 포인트 색 소품이 둘 이상이거나 사라짐

## 10. 검수 체크리스트
- [ ] 같은 슬롯의 `E13_neutral`과 외곽선이 같다
- [ ] 무섭지 않고 귀엽다
- [ ] 파일명이 `E18_sulking.png`이다
