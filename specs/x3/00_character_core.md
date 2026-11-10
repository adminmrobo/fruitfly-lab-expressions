---
id: CORE
character: 미공개 X3 · 꼬마
roster_no: No.009
version: 0.1
status: hidden   # 미공개 슬롯 — 갤러리·명부에서 버튼을 눌러야 보임
reference_images: [images/_sheets/spares_sheet.png]
---

# 미공개 X3 · 꼬마 · 캐릭터 코어 명세

미래에 들어올 캐릭터의 자리. 전체 규칙은 [`../spares/README.md`](../spares/README.md).

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 표시 이름 | 미공개 X3 · 꼬마 |
| 명부 번호 | **No.009** (버튼을 눌러야 공개) |
| 역할 | 예고 · 방청객 · 해설 속 '누군가' |
| 키 | 박사 대비 **0.60** |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 몸 | 남흑색 단색 #1B1A2E, 바깥 가장자리 보라 림라이트 #4B4470 |
| 눈 | 둥근 흰 점 눈 2개 (동공·이빨·씩 웃는 입 없음) |
| 볼 | 분홍 픽셀 2칸 #E9709A |
| 외곽 모양 | 고양이 귀 후드, 손을 덮는 큰 랩코트, 작은 몸 |
| 포인트 색 | **노랑 방울** — 색이 있는 곳은 이것 하나뿐 |
| 화풍 | 16비트 SNES 시대 픽셀 아트 |

## 3. 프롬프트 토큰
```yaml
CHARACTER_CORE_EN: "a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, wearing a lab coat whose shape is visible only as silhouette, friendly and cute, not scary, very small chibi silhouette wearing a hood with cat ears, oversized lab coat with long sleeves covering the hands, two hood drawstrings ending in small yellow (#F2C744) pompoms as the only colored part"
FRAMING_EN: "bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat light gray background"
NEGATIVE_BASE_EN: "scary, horror, villain, menacing smile, sharp teeth, bald head, realistic human proportions, glowing red eyes, full color clothing, visible face details, detailed eyes with irises, text, letters, question mark symbol, watermark, multiple characters"
```

## 4. 일관성 규칙
1. 표정에서 바뀌는 것은 흰 점 눈·흰 입선·볼·만화 이펙트뿐입니다. 외곽 모양과 포인트 색은 고정.
2. 무섭게 보이면 실패입니다(악당 미소·날카로운 이·빨간 눈 금지).
3. 정체를 공개할 때 이 슬롯의 외곽선을 새 캐릭터 디자인의 기준선으로 씁니다.
