---
id: CORE
character: 박사 (Professor)
alias: 없음
version: 1.1
status: confirmed   # 원본 시트 기준으로 확정
reference_images: [refs/original/doctor_sheet.png, refs/original/keyart_rivals.png]
---

# 박사 · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 호칭 | **박사** (EN: the Professor) |
| 한 줄 소개 | 자신만만한 치비 과학자 |
| 판단 기준 | 이론과 큰소리 |
| 역할 | 해설자 · 심판 · 사회자. 초파리와 Money-Robo의 대결을 중재 |
| 성격 | 자신만만, 호탕, 과장된 리액션. 큰소리를 치지만 실무는 조수가 다 함 (허당) |
| 말투 (권장) | 자신감 넘치는 반말·호탕한 웃음 ("하하하!", "역시 내 이론대로군!") |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 비율 | **치비** (큰 머리, 작은 몸) |
| 헤어 | **짙은 숯색 뾰족 머리**, 앞머리에 **흰 줄 한 가닥**, 뒤쪽 **작은 꽁지머리** |
| 눈썹 | **매우 굵은 검은 눈썹** (표정 표현의 핵심 파츠) |
| 안경 | **청록색 사각 테 안경** — 모든 표정에서 유지 |
| 눈 | 기본은 웃느라 감은 눈(^ ^). 뜬 눈은 작고 검은 눈 |
| 피부 | 밝은 살구색 |
| 의상 | **흰 가운 + 검은 조끼 + 검은 넥타이 + 검은 바지 + 검은 구두** |
| 수염 | **없음** |
| 시그니처 이펙트 | 손바닥 위 **보라색 불꽃**과 보라 구슬 |
| 팔레트 | 숯색 #2A2528 · 회색 #6B5F66 · 흰색 #D9D6D9 · 살구 #F6D3B8 · 청록 #1E6E73 · 보라 #8A3FC4 / #C77BE8 |
| 화풍 | 16비트 SNES 시대 픽셀 아트, 굵은 외곽선, 디더링 음영 |

## 3. 원본 표정 (`doctor_sheet.png`, `keyart_rivals.png`)
| 원본 | 표정 | 신규 ID |
|---|---|---|
| 턴어라운드 정면 | 눈 감고 활짝 웃음 | E01 기쁨 |
| 보라 불꽃 포즈 | 양손에 보라 불꽃, 호탕한 웃음 | E16 뿌듯함 |

원본 2종 → 24종 (12배)

## 4. 프롬프트 토큰 (각 표정 명세 7절에 이미 치환되어 있음)
```yaml
CHARACTER_CORE_EN: "the Professor, a chibi male scientist with a big head, dark charcoal spiky hair with a white streak at the front, a small low ponytail at the back, very thick bold black eyebrows, teal-framed rectangular glasses, light peach skin, white lab coat over a black vest, black tie and black slacks"
FRAMING_EN: "chibi upper body portrait from waist up, facing viewer, centered"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat light gray background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters"
```

## 5. 일관성 규칙
1. **허리 위 상반신**, 같은 크기, 같은 연회색 배경. 치비 비율을 유지합니다.
2. 생성할 때는 `doctor_sheet.png`를 레퍼런스로 함께 넣습니다.
3. **안경은 모든 표정에서 유지**합니다. 눈이 렌즈 반사로 가려지는 연출은 E03·E23에만 씁니다.
4. 표정은 **굵은 눈썹**의 각도로 크게 표현합니다 (원본 캐릭터의 특징).
5. `E13_neutral`을 가장 먼저 생성해 승인받고, 이후 2차 레퍼런스로 씁니다.
