---
id: CORE
character: 초파리 (Fruit Fly)
alias: 초파리 연구원
version: 1.1
status: confirmed   # 원본 스프라이트·설정서 기준으로 확정
reference_images: [refs/original/fruitfly_sprites_6.png, refs/original/keyart_rivals.png]
source_doc: refs/Money-Robo_캐릭터설정.md
---

# 초파리 · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 호칭 | **초파리** (초파리 연구원, EN: the Fruit Fly) |
| 한 줄 소개 | 작지만 날카로운 연구원 |
| 판단 기준 | 호기심과 생물학적 직관 |
| 역할 | 라이벌 A — "의심하는 쪽". Money-Robo와 매 장면 경쟁 |
| 말버릇 (권장) | **"정말 그럴까?"** |
| 강점 | 이상치·착각을 잘 잡아냄 |
| 약점 | 너무 신중해서 결정이 느림 |
| 무기·소품 | 작은 돋보기, 클립보드, 키보드, 커피잔 |
| 웃음 포인트 | 의기양양한 팔짱 |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 몸 | 짙은 숯빛 검은 곤충 몸통, 마디진 배 |
| 눈 | **크고 광택 있는 빨간 겹눈**. 표정은 겹눈 위의 눈꺼풀·하이라이트·작은 동공으로만 표현 |
| 헬멧 | **남색 레트로 헬멧**, 가운데 노란·흰 줄, 측면 작은 원형 볼트 |
| 케이블 | 헬멧 뒤에서 늘어진 **자홍·보라·파랑 케이블** 여러 가닥 |
| 의상 | **작은 흰 가운 + 검은 조끼** |
| 날개 | 반투명 맥이 보이는 날개 2장 |
| 다리 | 6개. 앞다리 한 쌍을 손처럼 씀 |
| 팔레트 | 검정 #1E1C20 · 빨강 #D8352A · 남색 #23467E · 노랑 #D8B048 · 자홍 #B4407E · 파랑 #3A6FC0 · 흰 가운 #E6E2E6 |
| 화풍 | 16비트 SNES 시대 픽셀 아트 |

## 3. 원본 스프라이트 6종 (`fruitfly_sprites_6.png`)
| 원본 칸 | 원본 포즈·표정 | 신규 ID |
|---|---|---|
| 1행 1열 | 팔짱 (언짢은 의심) | E18 삐짐 |
| 1행 2열 | 키보드 타이핑 (집중) | E09 생각 |
| 1행 3열 | 클립보드 (꼼꼼한 확인) | E10 확인 |
| 2행 1열 | 비명 (양손으로 얼굴, 땀) | E05 두려움 |
| 2행 2열 | 손가락으로 지시 | E08 안내 |
| 2행 3열 | 커피 (여유) | E13 기본 |
| 키아트 | 돋보기를 든 의기양양한 포즈 | E07 설명 |

원본 6종 → 24종 (4배)

## 4. 프롬프트 토큰 (각 표정 명세 7절에 이미 치환되어 있음)
```yaml
CHARACTER_CORE_EN: "the Fruit Fly, a tiny expressive cartoon fruit fly researcher with a dark charcoal-black segmented insect body, large glossy red compound eyes, a retro dark blue helmet with a yellow-white center stripe and small round side bolts, colorful dangling cables in magenta, purple and blue curving from the back of the helmet, a tiny white lab coat over a black vest, translucent veined wings, six thin black legs with the front pair used like hands"
FRAMING_EN: "full body sprite centered, facing viewer, same framing as the reference sprite sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat medium gray background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters"
```

## 5. 일관성 규칙
1. 원본 스프라이트와 같은 **전신**, 같은 크기, 회색 배경, 발밑 그림자.
2. 생성할 때는 `fruitfly_sprites_6.png`를 레퍼런스로 넣습니다.
3. 겹눈은 빨간색·크기를 유지합니다. 감정은 **겹눈 위 눈꺼풀(검은 픽셀), 하이라이트, 입, 자세, 케이블·날개 움직임**으로 표현합니다.
4. 데포르메 표정(E19~E24)도 헬멧·케이블·가운 실루엣은 유지합니다.
