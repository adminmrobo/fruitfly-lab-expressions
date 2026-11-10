---
id: CORE
character: 모아 (Moa)
version: 0.1
status: draft   # 기본형(B1~B5) 승인 전
design_source: [사용자 제공 일러스트 Gemini_Generated_Image_63gjyf63gjyf63gj(화분) · Gemini_Generated_Image_r2u37qr2u37qr2u3_3(찻잔)]
reference_images: [refs/original/moa_sheet.png (생성 예정), refs/original/haru_sheet.png (화풍·배치 기준)]
---

# 모아 · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 이름 (한국어) | **모아** |
| 외국어판 | **Moa** |
| 이름 뜻 | 데이터를 '모아' 두는 사람. 기록·응원 담당 |
| 세계관 내 호칭 | 인턴 (메이드 인턴) |
| 성격 | 상냥하고 잘 웃음. 화분을 돌보고 차를 내림. 응원할 때 제일 목소리가 큼 |
| 기본 자리 | 연구실 메이드 인턴(화분·차·자료 정리) |
| 바뀌는 자리 | **방청객**(주 자리) · 심판 |
| 대전 배치 | 조수 자리와 같음 — **왼쪽을 봄**. 시아(오른쪽)와 마주 봄 |
| 키 | 박사 대비 **0.84** (네 사람 중 사람 캐릭터로는 가장 작음) |
| 소속 | 「초파리 연구실」 |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 헤어 | 허리까지 오는 **애쉬 베이지 긴 머리**, 끝이 살짝 웨이브, 가지런한 앞머리 |
| 머리 장식 | **흰 프릴 메이드 머리띠** + 왼쪽 귀 위 **흰 리본 끈** |
| 눈 | 크고 둥근 **호박색(갈색) 눈** |
| 피부 | 밝은 살구색, 옅은 홍조 |
| 안경 | **없음** |
| 의상 | 흰 셔츠 + **빨강·남색 체크 리본 타이** + **카멜색 니트 카디건**(소매 시보리) + **흰 프릴 앞치마**(어깨 프릴, 뒤에 큰 리본) + 검은 치마 |
| 신발 (전신) | 갈색 로퍼, 흰 양말 |
| 팔레트 | 베이지 머리 #D8C09A · 머리 그늘 #B89C74 · 카디건 #D4B48A · 체크 빨강 #A8323C · 체크 남색 #2C3A66 · 앞치마 #FAF8F4 · 호박 눈 #B07A3E · 살구 #F8DCC8 |
| 화풍 | 16비트 SNES 시대 픽셀 아트, 굵은 외곽선, 디더링 음영 |

## 3. 사용자 원본 일러스트와 표정 대응
| 원본 | 장면 | 쓰이는 ID |
|---|---|---|
| 화분을 든 그림 | 화분을 들고 미소 | E13 기본 · E16 뿌듯함 |
| 찻잔 그림 | 분홍 찻잔을 두 손으로 들고 미소 | E01 기쁨 · M1 대기(변형) |

| 정장 그림 (검은 재킷, 포니테일) | 서류를 들고 펜으로 체크 | **정장 의상** (M16) · E10 확인 변형 |

### 정장 의상 (사용자 확정 2026-11-11)
외부 발표·면접·보고 장면에서 입는 모아의 두 번째 옷입니다. 기본형(메이드)과 같은 얼굴·눈 색을 유지하고, **머리 모양과 옷만** 바뀝니다.
| 항목 | 값 |
|---|---|
| 헤어 | 같은 애쉬 베이지 머리를 **로우 포니테일**로 묶음, **분홍 곱창 머리끈**, 옆머리 몇 가닥 |
| 머리띠 | 정장일 때만 **없음** |
| 의상 | **검은 테일러드 재킷** + 흰 셔츠(칼라 밖으로) + 검은 치마, 작은 은색 귀걸이 |
| 소품 | 서류 묶음, 검은 펜 |
| 쓰는 시트 | M16 (정장 서기·걷기·서류 확인) |
| 토큰 | `SUIT_EN: "wearing a business suit instead of the maid outfit: the same ash-beige hair tied in a low ponytail with a pink scrunchie, no headband, black tailored jacket over a white collared shirt, black skirt, black low heels, small silver stud earrings"` |

## 4. 프롬프트 토큰
```yaml
CHARACTER_CORE_EN: "Moa, a gentle cheerful anime girl maid intern in a research lab, long ash-beige hair reaching the waist with soft wavy ends and neat bangs, white frilled maid headband with a thin white ribbon over the left ear, big round amber-brown eyes, light peach skin with soft blush, white shirt with a red and navy plaid bow tie, camel knit cardigan with ribbed cuffs, white frilled apron with ruffled shoulder straps, no glasses"
FRAMING_EN: "bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat light gray background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, black hair, pink hair, ponytail, missing headband, glasses, suit jacket"

CHIBI_CORE_EN: "chibi girl maid intern (big head, about 2.5 heads tall, the smallest of the human characters), long ash-beige hair to the waist with wavy ends, white frilled maid headband, amber-brown eyes, camel knit cardigan over a white shirt with a red and navy plaid bow tie, white frilled apron, black skirt, white socks, brown loafers"
```

## 5. 일관성 규칙
1. B1 설정 시트 → B2 E13 순서로 기준을 먼저 승인받습니다.
2. 기본형(메이드)에서 머리띠가 빠지거나 포니테일로 바뀌면 실패입니다. 포니테일은 정장 의상(M16)에서만 씁니다.
3. 동작 시트는 조수와 같이 **왼쪽**을 보게 그리고, 좌우 뒤집기 금지(체크 리본·귀 위 리본 위치가 바뀜).
4. 방청객·심판 소품은 메이드 의상 위에 더합니다.
