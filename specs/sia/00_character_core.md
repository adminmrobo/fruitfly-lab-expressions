---
id: CORE
character: 시아 (Sia)
version: 0.1
status: draft   # 기본형(B1~B5) 승인 전
design_source: [사용자 제공 일러스트 01_Working_Typing · 03_Desk_Cleaning · 05_Yawning · 06_Sleeping]
reference_images: [refs/original/sia_sheet.png (생성 예정), refs/original/haru_sheet.png (화풍·배치 기준)]
---

# 시아 · 캐릭터 코어 명세

## 1. 이름·역할
| 항목 | 값 |
|---|---|
| 이름 (한국어) | **시아** |
| 외국어판 | **Sia** (en·ja·zh·ru·uz·vi 공통 로마자) |
| 이름 뜻 | 시야(視野). 판을 끝까지 지켜보는 눈 — 심판 자리에 어울림 |
| 세계관 내 호칭 | 인턴 (메이드 인턴) |
| 성격 | 조용하고 꼼꼼함. 말수가 적고 정리를 잘함. 다만 집중이 끊기면 하품하고 책상에서 졸아 버리는 반전이 있음 |
| 기본 자리 | 연구실 메이드 인턴(타이핑·책상 정리) |
| 바뀌는 자리 | **심판**(주 자리) · 방청객 |
| 대전 배치 | 박사 자리와 같음 — **오른쪽을 봄**. 모아(왼쪽)와 마주 봄 |
| 키 | 박사 대비 **0.88** (조수 0.90보다 조금 작음) |
| 소속 | 「초파리 연구실」 |

## 2. 아이덴티티 고정값 — 변경 금지
| 항목 | 값 |
|---|---|
| 헤어 | 허리까지 오는 **새까만 생머리**, 옆으로 흘린 앞머리, 얼굴 양옆으로 가는 머리 두 가닥 |
| 머리 장식 | **없음** (모아와 구별되는 지점 — 모아는 흰 프릴 머리띠) |
| 눈 | 차분한 **회색 눈**, 살짝 내리뜬 눈매 |
| 귀 | 작은 **은색 드롭 귀걸이** |
| 피부 | 밝은 살구색 |
| 안경 | **없음** |
| 의상 | **긴소매 차콜 검정 메이드 원피스**(퍼프 어깨, 흰 레이스 소맷단에 검은 단추 2개) + 흰 하이칼라 + 목에 **큰 회색 리본** + **발목까지 오는 흰 프릴 앞치마**(뒤에 큰 흰 리본 매듭) |
| 신발 (전신) | 검은 플랫 슈즈, 흰 양말 |
| 팔레트 | 흑발 #1E1B22 · 머리 광택 #4A4656 · 원피스 #34363F · 회색 리본 #8C8C94 · 앞치마 #F4F2EE · 회색 눈 #7A7680 · 살구 #F6D9C4 |
| 화풍 | 16비트 SNES 시대 픽셀 아트, 굵은 외곽선, 디더링 음영 (하루·박사와 같음) |

## 3. 사용자 원본 일러스트와 표정 대응
| 원본 | 장면 | 쓰이는 ID |
|---|---|---|
| 01_Working_Typing | 무표정하게 타이핑 | E13 기본 · E10 확인 |
| 03_Desk_Cleaning | 책상 닦으며 서류 정리 | E08 안내 · 동작 시트 대기 자세 |
| 05_Yawning | 손으로 입 가리고 하품 | E17 졸림 |
| 06_Sleeping | 팔 베고 엎드려 미소 지으며 잠 | E17 졸림(변형) · S4 KO |

## 4. 프롬프트 토큰
```yaml
# 표정(바스트업) — 하루 E01~E24와 같은 구도
CHARACTER_CORE_EN: "Sia, a calm anime girl maid intern in a research lab, long straight jet-black hair reaching the waist with side-swept bangs and two thin strands framing the face, calm gray eyes with slightly lowered lids, small silver drop earrings, light peach skin, long-sleeved charcoal-black maid dress with puffed shoulders and white lace cuffs, white high collar with a large soft gray bow, long white frilled apron, no headdress, no glasses"
FRAMING_EN: "bust-up portrait from chest up, facing viewer, centered, same framing as the reference expression sheet"
STYLE_EN: "detailed 16-bit SNES-era pixel art, limited palette, crisp pixels, dithering shading, thick dark outlines, cheerful comedy mood, no readable text, no letters, no words"
BACKGROUND_EN: "plain flat light gray background"
NEGATIVE_BASE_EN: "blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, text, letters, watermark, multiple characters, headdress, maid headband, glasses, colored hair, blonde hair, brown hair"

# 동작(전신 치비) — 박사 D시트와 같은 방향(오른쪽)
CHIBI_CORE_EN: "chibi girl maid intern (big head, about 2.5 heads tall, slightly shorter than the assistant), long straight jet-black hair to the waist with side-swept bangs, gray eyes, small silver earrings, no headdress, charcoal-black long-sleeved maid dress with white lace cuffs, large gray bow at the collar, long white frilled apron tied with a big bow at the back, white socks, black flat shoes"
```

## 5. 일관성 규칙
1. 첫 기준은 **B1 설정 시트 → B2 E13 바스트업** 순서. 승인된 두 장을 이후 모든 표정·동작의 참고 그림으로 넣습니다.
2. 머리 장식이 생기면 실패입니다(모아와 구별이 무너짐).
3. 동작 시트에서 앞머리 가르마 방향을 모든 칸에서 같은 쪽으로 유지하고, 좌우 뒤집기 금지(박사와 같은 규칙).
4. 심판·방청객 의상은 메이드 원피스 위에 소품만 더합니다. 원피스·앞치마는 벗기지 않습니다.
