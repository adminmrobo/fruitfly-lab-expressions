---
id: CORE
character: MONEY-ROBO
alias: 머니로보
version: 1.1
status: confirmed   # 원본 시트·설정서 기준으로 확정
reference_images: [refs/original/money_robo_expressions_9.png, refs/original/money_robo_turnaround.png]
source_doc: refs/Money-Robo_캐릭터설정.md
---

# MONEY-ROBO · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 이름 | **Money-Robo** (머니로보) |
| 슬로건 | *Making Smart Choice* (이미지에는 글자로 넣지 않음) |
| 종류 | 떠다니는 치비 로봇 |
| 역할 | 라이벌 B — "확신하는 쪽". 초파리와 매 장면 경쟁 |
| 성격 | 낙천적 · 자신만만 · 숫자 맹신 · 돈 이야기에 눈이 반짝임 |
| 말버릇 | **"데이터가 그렇게 말하고 있어요!"** |
| 약점 | 과적합, 과신, 지나친 낙관. 예측이 빗나가면 스크린 얼굴에 **땀 픽셀**이 뜸 |
| 좋아하는 것 | 금화, 상승하는 초록 캔들, 딱 떨어지는 숫자 |
| 싫어하는 것 | 불확실성 밴드, "모르겠다"는 대답, 초파리의 의심 어린 눈빛 |

## 2. 아이덴티티 고정값 — 변경 금지
| 부위 | 디자인 |
|---|---|
| 머리 | 크고 둥근 사각형, 광택 있는 흰색, 굵은 검은 외곽선 |
| 안테나 | 짧은 막대 위 작은 원형 노브 |
| 얼굴 | 검은 알약형 스크린. **표정은 스크린 안의 금빛 픽셀로만** 표현 |
| 기본 얼굴 | 금빛 원형 눈 2개 + 금빛 곡선 미소 |
| 몸통 | 작고 둥근 흰 몸통, 가슴에 검은 타원 패널 + **시안 알약형 코어 라이트** |
| 팔 | 짧고 둥근 팔, 손가락 없음 |
| 다리 | 없음. 아래에 검은 타원 그림자를 두고 떠 있음 |
| 팔레트 | 광택 화이트(머리·몸통) · 블랙(외곽선·스크린·패널) · 골든 옐로 #F5C211(눈·입·금화) · 시안 #3FB8F0(코어) |
| 화풍 | 16비트 SNES 시대 픽셀 아트 |

## 3. 표정 표현 채널 (로봇 전용)
1. **스크린 픽셀:** 금빛 눈·입 모양. 보조 픽셀로 분홍 볼, 하늘색 눈물·땀, 흰 하이라이트
2. **스크린 색 변화:** 분노는 스크린 테두리에 빨간 경보 빛
3. **가슴 코어:** 기본은 시안. 감정에 따라 밝기만 조절 (색 변경은 E03·E22·E24만 허용)
4. **외부 이펙트:** 금화(B 또는 $ 표시), 초록 상승 차트, 반짝임, 물방울

## 4. 원본 표정 9종 (`money_robo_expressions_9.png`)
| 원본 칸 | 원본 표정 | 신규 ID |
|---|---|---|
| 1행 1열 | 무표정 (원형 눈 + 곡선 미소) | E13 기본 |
| 1행 2열 | 부드러운 미소 (^ ^ 눈) | E01 기쁨 |
| 1행 3열 | 짜증 (일자 눈) | E18 삐짐 |
| 2행 1열 | 울음 (픽셀 눈물) | E02 슬픔 |
| 2행 2열 | 경악 (동그랗게 커진 눈, o 입) | E04 놀람 |
| 2행 3열 | 능글 (반쯤 감은 눈 + 금화 반짝임) | E16 뿌듯함 |
| 3행 1열 | 졸음 (감은 눈 + 콧방울) | E17 졸림 |
| 3행 2열 | 부끄럼 (분홍 볼 픽셀) | E14 머쓱함 |
| 3행 3열 | 분노 (빨간 경보 빛) | E03 분노 |

원본 9종 → 24종 (2.7배). 신규 15종

## 5. 프롬프트 토큰 (각 표정 명세 7절에 이미 치환되어 있음)
```yaml
CHARACTER_CORE_EN: "MONEY-ROBO, a cute small floating chibi robot with a large glossy rounded-square white head and a small rounded white body with thick black outlines, a black pill-shaped screen face showing golden-yellow pixel eyes and mouth, a small round knob antenna on a short stem, stubby rounded fingerless arms, no legs, a black oval chest panel with a bright cyan pill-shaped core light, hovering above a small dark oval shadow"
FRAMING_EN: "full body centered, facing viewer, same framing as the reference 3x3 expression sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat white background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters"
```

## 6. 일관성 규칙
1. 원본 3×3 시트와 같은 **전신 정면**, 같은 크기, 흰 배경, 아래 타원 그림자.
2. 생성할 때는 `money_robo_expressions_9.png`와 `money_robo_turnaround.png`를 레퍼런스로 넣습니다.
3. 몸체 형태는 절대 바꾸지 않습니다. 감정은 3절의 채널로만 표현합니다.
4. 비트코인은 실제 로고 대신 **B 기호 금화**로, 실제 기업·종목 로고는 쓰지 않습니다.
