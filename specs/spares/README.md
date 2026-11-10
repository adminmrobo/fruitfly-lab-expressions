---
id: CORE
character: 미공개 캐릭터 슬롯 (X1~X3)
version: 0.1
status: draft
reference_images: [refs/original/haru_sheet.png, images/_sheets/lab4_lineup_gpt2_labeled.png]
---

# 미공개 캐릭터 슬롯 · 실루엣 3종 (X1 · X2 · X3 = No.007 · 008 · 009)

앞으로 들어올 캐릭터의 자리를 미리 잡아 두는 **검은 실루엣 캐릭터**입니다. 정체는 감추지만 화풍과 비율은 박사·조수와 같은 귀여운 치비 픽셀 아트입니다.

## 1. 쓰는 곳
| 장면 | 쓰임 |
|---|---|
| 예고 | "다음 편에 새 식구가 옵니다" — 실루엣만 보여 줌 |
| 방청객 채우기 | 대전 화면 뒤 관중석 머릿수 |
| "누군가" 역할 | 정체를 밝히지 않는 제3자 (익명 사용자, 공격자, 외부 평가자 등 해설 속 역할) |
| 공개 | 실제 캐릭터를 디자인할 때 이 실루엣의 **외곽 모양을 기준선**으로 씀 |

## 2. 공통 고정값 (세 슬롯 모두)
| 항목 | 값 |
|---|---|
| 몸 채색 | 진한 남흑색 단색 **#1B1A2E**, 바깥 가장자리에만 보라 림라이트 **#4B4470** 한 줄 (디더링) |
| 눈 | **둥근 흰 점 눈 2개** + 아주 작은 하이라이트. 동공·흰자 표현·이빨·씩 웃는 입 **없음** |
| 입 | 기본은 없음. 표정이 필요할 때만 작은 흰 선(ㅅ, ㅡ, o) |
| 볼 | 분홍 픽셀 2칸 (#E9909A) — 귀여운 인상 담당 |
| 옷 | 랩코트 실루엣(옷자락 모양만 보임, 옷도 검정) |
| 포인트 색 | 슬롯마다 **딱 한 가지 색** 소품 1개 — 공개 전 힌트 |
| 비율 | 치비, 약 2.5등신 (동작 시트 기준) |
| 분위기 | 무섭지 않게. 공포·악당 인상 금지 |

## 3. 슬롯별 실루엣
| 슬롯 | 명부 | 가칭 | 외곽 모양 | 포인트 색 소품 | 키 (박사 대비) |
|---|---|---|---|---|---|
| **X1** | No.007 | 미공개 · 리본 | 긴 사이드 포니테일 + 큰 리본, 치맛자락이 보이는 랩코트 | 리본 **분홍** #E9709A | 0.85 |
| **X2** | No.008 | 미공개 · 모자 | 챙 둥근 베레모, 짧은 머리, 둥근 안경테 (렌즈에 작은 반사 2점) | 안경 반사 **청록** #3FC8C0 | 0.95 |
| **X3** | No.009 | 미공개 · 꼬마 | 고양이 귀 후드를 쓴 작은 몸, 소매가 손을 덮는 큰 랩코트 | 후드 끈 끝 방울 **노랑** #F2C744 | 0.60 |

> 세 슬롯은 서로 외곽선만 보고도 구별되게 머리 모양을 크게 다르게 잡았습니다(포니테일 / 모자 / 귀 후드).

## 4. 프롬프트 토큰
```yaml
SPARE_COMMON_EN: "a mysterious unrevealed character drawn as a cute solid silhouette, whole body filled with one flat very dark navy-black color (#1B1A2E) with a thin dithered purple rim light (#4B4470) only on the outer edge, two round plain white dot eyes with a tiny highlight, no pupils, no teeth, no grin, two small pink blush pixels on the cheeks, wearing a lab coat whose shape is visible only as silhouette, friendly and cute, not scary"
X1_EN: "chibi girl silhouette, long side ponytail tied with a big bow, the bow is the only colored part: bright pink (#E9709A), skirt hem visible under the lab coat"
X2_EN: "chibi silhouette with a round beret and short hair, round glasses frame whose lenses show two small teal (#3FC8C0) reflections as the only colored part"
X3_EN: "very small chibi silhouette wearing a hood with cat ears, oversized lab coat with long sleeves covering the hands, two hood drawstrings ending in small yellow (#F2C744) pompoms as the only colored part"
STYLE_EN: "detailed 16-bit SNES-era pixel art, crisp pixels, thick dark outlines, cheerful comedy mood, no text, no letters, no question marks"
NEGATIVE_EN: "scary, horror, villain, menacing smile, sharp teeth, bald head, realistic human proportions, glowing red eyes, full color clothing, visible face details, text, letters, question mark symbol, watermark"
```

## 5. 규칙
1. 슬롯마다 다른 식구와 같은 **표정 24종(E01~E24)** 명세를 둡니다: `specs/x1/`, `specs/x2/`, `specs/x3/`. 실루엣이라 흰 점 눈·입선·이펙트만 바뀝니다.
2. 지금 그림은 9종씩(E13·E01·E03·E02·E04·E09·E16·E15·E24, 원본 `images/_sheets/spare_x*_faces.png`) — 나머지 15종은 명세만 있습니다.
3. 동작은 방청객 시트 1장씩(X1_crowd·X2_crowd·X3_crowd)만 둡니다. 대전 동작은 정체가 공개된 뒤 만듭니다.
4. 갤러리(`index.html`·`motions.html`)와 식구 명부에서는 **버튼을 눌러야** 보입니다.
5. 공개할 때 슬롯 번호를 캐릭터 키로 바꾸고(예: X1 → `xxx`), 이 파일의 해당 행을 "공개됨"으로 고칩니다.
