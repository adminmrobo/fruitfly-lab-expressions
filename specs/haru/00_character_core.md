---
id: CORE
character: 하루 (Haru)
alias: 세나 (Sena)
version: 1.1
status: confirmed   # 원본 시트 기준으로 확정
reference_images: [refs/original/haru_sheet.png, refs/original/haru_expressions_6.png]
---

# 하루(세나) · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 본명 (한국어) | **하루** (Haru) |
| 예명 | **세나** (Sena). 같은 인물이며 호칭만 다름. 외형·의상·표정 세트 동일 |
| 표기 규칙 | 기본은 "하루". 방송·공연 등 예명 맥락에서만 "세나". 처음 언급할 때는 "하루(세나)" |
| 세계관 내 호칭 | 조수 |
| 역할 | 실제로 일을 다 하는 연구원. 꼼꼼한 실험과 기록, 실험 진행·점수 기록 |
| 소속 | 「초파리 연구실」 |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 헤어 | 허리까지 오는 **분홍색 생머리 + 남색 줄** 투톤. **앞머리 가운데에 굵은 남색 줄** (뒷머리에도 가운데 남색 줄) |
| 헤어 포인트 | 정수리 양쪽 **둥근 번 2개**(살짝 흐트러진 질감), 작은 바보털 |
| 눈 | 크고 밝은 **파란 눈**, 큰 하이라이트 |
| 피부 | 밝은 살구색 |
| 안경 | **없음** |
| 의상 | **라벤더 후드티**(흰 끈) + 안에 흰 티 + **무릎 길이의 열린 흰 랩코트** |
| 하의·신발 (전신일 때) | 롤업한 청바지, 라벤더 스니커즈 |
| 팔레트 | 분홍 #E9909A · 진분홍 #D9707E · 남색 #1E2F5C · 라벤더 #A99AC8 · 살구 #F6D3B8 |
| 화풍 | 16비트 SNES 시대 픽셀 아트, 굵은 외곽선, 디더링 음영 |

## 3. 원본 표정 6종 (`haru_expressions_6.png`)
| 원본 칸 | 원본 표정 | 신규 ID |
|---|---|---|
| 1행 1열 | 결의 (주먹) | E12 응원 |
| 1행 2열 | 공포 (흰 눈, 파랗게 질림, 땀) | E24 충격 |
| 1행 3열 | 환희 (별 눈, 반짝임) | E19 반짝눈 |
| 2행 1열 | 졸림 (반쯤 감은 눈, 콧방울) | E17 졸림 |
| 2행 2열 | 울음 (흐르는 눈물) | E21 폭포 눈물 |
| 2행 3열 | 능글 (반쯤 감은 눈, 미소) | E16 뿌듯함 |

## 4. 프롬프트 토큰 (각 표정 명세 7절에 이미 치환되어 있음)
```yaml
CHARACTER_CORE_EN: "Haru, a cute anime girl lab assistant, long straight pink hair with navy blue streaks including a thick navy streak down the center of the bangs, two round messy hair buns on top of the head, a small ahoge, big bright blue eyes, light peach skin, wearing a lavender hoodie with white drawstrings over a white t-shirt, under an open white knee-length lab coat"
FRAMING_EN: "bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat light gray background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters"
```

## 5. 일관성 규칙
1. 원본 표정 시트와 같은 **가슴 위 바스트업**, 같은 크기, 같은 연회색 배경.
2. 생성할 때는 `haru_sheet.png`와 `haru_expressions_6.png`를 레퍼런스로 함께 넣습니다.
3. 데포르메 표정(E19~E24)도 번·남색 줄·후드·랩코트 실루엣은 유지합니다.
4. `E13_neutral`을 가장 먼저 생성해 승인받고, 이후 2차 레퍼런스로 씁니다.
