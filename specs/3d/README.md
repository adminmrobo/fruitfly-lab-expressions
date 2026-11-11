# 3D 캐릭터 설정서 v1.0 (2026-11-12)

연구실 식구 전원을 **같은 축척의 3D 모델**로 세우고, 정해진 각도로 찍은 **이미지 벡터**를 함께 둡니다.
목적은 3D 화면(예: [시멘트 공장 World](https://adminmrobo.github.io/smart_factory_world/cement/))에 캐릭터가 들어가도 2D 정본과 어긋나지 않게 하는 것입니다.

- 설정 화면: [`characters3d.html`](../../characters3d.html) — 회전, 8방향, 높이 2종, 포즈 8종, 표정 3종, 전원 라인업, 공장 축척(×1.75)
- 모델: [`chars3d/lab3d.js`](../../chars3d/lab3d.js) — three.js 0.170 ES 모듈, 다른 페이지에서 그대로 불러 씀
- 설정값: [`characters3d.json`](characters3d.json) — 키·팔레트·외곽선·3D 고정값·소품·공장 역할
- 이미지 목록: [`views.json`](views.json) — 그림 270장의 파일·캐릭터·방향·높이·포즈·표정 (구글 시트 캐릭터 DB로 옮길 때 이 표를 그대로 씀)

## 1. 식구별 3D 모델

| 키 | 캐릭터 | 키(박사=1) | 외곽선 | 3D에서 꼭 보여야 하는 것 |
|---|---|---|---|---|
| `doctor` | 박사 | 1.00 | `#2A2528` | 뾰족 머리 + 흰 줄, 뒤 꽁지머리, 청록 사각 안경, ^ ^ 눈, 열린 흰 가운 + 검은 조끼 |
| `haru` | 조수(하루) | 0.90 | `#2E2430` | 분홍 생머리 + 앞·뒤 남색 줄, 번 2개, 파란 눈, 라벤더 후드 + 흰 랩코트, 청바지 |
| `fruitfly` | 초파리 연구원 | 0.92 | `#121014` | 빨간 겹눈, 남색 헬멧 + 노랑 줄, 케이블, 다리 6개, 반투명 날개, 흰 가운 |
| `jupanbot` | 주판봇 | 0.86 | `#2E2A24` | CRT 머리 + 초록 화면 민트 픽셀 얼굴, 뒤 통풍구, 안테나 끝 주판알, 마디 팔, 무한궤도, 주판 |
| `sia` | 시아 (No.005) | 0.88 | `#1E1B22` | 흑발(장식 없음), 회색 눈, 발목까지 메이드 원피스, 회색 큰 리본, 등 뒤 흰 리본 |
| `moa` | 모아 (No.006) | 0.84 | `#3A2A1E` | 베이지 웨이브 머리, 흰 프릴 머리띠 + 왼쪽 리본, 호박 눈, 카디건 + 체크 리본 타이 |
| `moa` · `suit` | 모아 정장 | 0.84 | `#3A2A1E` | 로우 포니테일 + 분홍 곱창, 검은 재킷, 서류·펜 |
| `x1` | 미공개 X1 (No.007) | 0.85 | `#4B4470` | 실루엣, 사이드 포니테일 + **분홍 리본**만 색 |
| `x2` | 미공개 X2 (No.008) | 0.95 | `#4B4470` | 실루엣, 베레모, 둥근 안경의 **청록 반사**만 색 |
| `x3` | 미공개 X3 (No.009) | 0.60 | `#4B4470` | 실루엣, 고양이 귀 후드, 손을 덮는 소매, **노랑 방울**만 색 |

- 화풍: 저폴리 + 3단 툰 명암 + 뒤집은 껍질 외곽선. 2D 정본(16비트 픽셀 아트)의 **색·실루엣·소품**을 맞추고, 질감은 단순하게 둡니다. 설정 화면의 '도트 모드'로 픽셀 느낌을 볼 수 있습니다.
- 미공개 X1~X3는 몸 전체를 `#1B1A2E` 한 색으로 칠하고, 2D의 보라 림라이트를 **외곽선 색**으로 대신합니다. 설정 화면에서도 🔒 버튼을 눌러야 보입니다.
- 2D 명세와 3D가 다르면 **2D 명세가 이깁니다**. 초파리·주판봇의 키는 2D 명세에 없어 3D v1에서 정했습니다.

## 2. 이미지 벡터 (캐릭터마다 27장, 모두 270장)

```
images/3d/{slug}/turn_{e08|e32}_{d0..d7}.webp   8방향 × 2높이 = 16장
images/3d/{slug}/pose_{포즈}.webp               포즈 8장 (오른앞 25°, 눈높이)
images/3d/{slug}/face_{E13|E01|E04}.webp        얼굴 확대 3장
images/3d/_sheets/{slug}_3d_sheet.png           설정 시트 (1행 눈높이 8방향 · 2행 공장 시점 8방향 · 3행 포즈 8종)
images/3d/_sheets/lab10_lineup_3d_{e08|e32}.png 전원 라인업
```
`slug` = 캐릭터 키, 모아 정장만 `moa_suit`. 크기 512×512 투명 WebP(무손실).
모든 그림은 **같은 축척·같은 발 기준선**(화면 한 변 = 박사 키 × 1.24)이라 나란히 놓으면 키가 맞습니다.

| 축 | 값 |
|---|---|
| 방향 | d0 정면 · d1 오른앞 · d2 오른쪽 · d3 오른뒤 · d4 뒤 · d5 왼뒤 · d6 왼쪽 · d7 왼앞 (45° 간격, '오른' = 화면 오른쪽을 봄) |
| 높이 | e08 눈높이 8° (해설·대전 화면) · e32 공장 시점 32° (smart_factory_world 기본 카메라와 같음) |
| 포즈 | idle 서기 · wave 손 인사 · explain 설명 · think 생각 · cheer 환호 · hold 두 손 소품 · referee 심판 신호 · walk 걷기 |
| 표정 | E13 기본 · E01 기쁨 · E04 놀람 (나머지 21종은 2D 표정 이미지) |

다시 만들기: `python3 chars3d/tools/render_views.py` (Playwright 크로미움 + Pillow). 오프라인이면 `--three 경로/three.module.js`.

## 3. 다른 3D 페이지에서 쓰기

```html
<script type="importmap">{"imports":{"three":"https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js"}}</script>
<script type="module">
import * as THREE from 'three';
import { createLab3D } from 'https://adminmrobo.github.io/fruitfly-lab-expressions/chars3d/lab3d.js';
const lab = createLab3D(THREE, { outline: true, shadow: true });
const doc = lab.build('doctor', { unit: 1.75, pose: 'idle', expr: 'E13' });   // 공장 축척
scene.add(doc);
// 매 프레임: doc.userData.update(seconds)  · 포즈 바꾸기: doc.userData.setPose('cheer')
</script>
```
- `build(key, {variant, expr, pose, prop, unit})` → `THREE.Group` (정면 +Z, 발밑 y 0)
- 모듈은 three를 직접 import하지 않고 인자로 받습니다 — 페이지의 three 한 벌을 같이 씁니다.
- 공장에서는 `unit: 1.75`(예전 원기둥 사람 표시와 같은 키)로 둡니다.

## 4. 2D 픽셀 턴어라운드 생성 프롬프트 (Genspark 등)

3D 그림을 **자세·비율 참조**로, 2D 정본 시트를 **얼굴·화풍 참조**로 함께 넣고 아래를 붙여 넣습니다.
참조 이미지: `images/3d/_sheets/{slug}_3d_sheet.png` + `refs/original/` 정본 시트 + `images/{key}/E13_neutral.png`.

공통 꼬리:
```
STYLE_EN: "detailed 16-bit SNES-era pixel art, crisp pixels, thick dark outlines, flat colors with light dithering, chibi proportions about 2.5 heads tall, same character in every cell, consistent size and shared ground line, light gray background, no text, no letters, no numbers"
LAYOUT_EN: "character turnaround sheet, 8 columns in this order: front, front-right three-quarter, right profile, back-right three-quarter, back, back-left three-quarter, left profile, front-left three-quarter; row 1 at eye level, row 2 seen from a 32-degree high isometric camera like a factory diorama"
NEGATIVE_EN: "3D render, plastic look, realistic proportions, different outfit between views, missing accessories, text, watermark, extra characters"
```

| slug | 캐릭터 문장 (`{CHARACTER_CORE_EN}` 자리에 넣음) |
|---|---|
| doctor | chibi professor, spiky dark charcoal hair with one white streak at the front and a small ponytail at the back, teal square glasses always on, very thick black eyebrows, happy closed ^ ^ eyes, open white lab coat over black vest, white shirt and black tie, black trousers and black shoes, holding a brown book in his left hand |
| haru | chibi assistant girl, waist-length straight pink hair with a thick navy streak in the middle of the bangs and down the middle of the back hair, two round hair buns on top, small ahoge, big bright blue eyes, lavender hoodie with white strings under an open knee-length white lab coat, rolled-up blue jeans, lavender sneakers, holding a gray notebook |
| fruitfly | chibi fruit fly researcher, glossy black insect body, huge shiny red compound eyes, navy retro helmet with a yellow and white center stripe and small side bolts, magenta, blue and purple cables hanging from the back of the helmet, small white lab coat over black vest, six legs with the front pair used as hands, two translucent veined wings on the back |
| jupanbot | cute boxy robot, beige rounded CRT monitor head with a large dark green screen face showing only mint green pixel-block eyes and mouth, vent slots on the back and sides, short antenna ending in one reddish-brown abacus bead (not a round ball), segmented gray arms with round mitten hands, two dark gray tank treads instead of legs, holding a small wooden abacus in front |
| sia | chibi maid girl, waist-length jet-black straight hair with side-swept bangs and two thin strands framing the face, no hair accessory, calm gray half-lidded eyes, small silver drop earrings, long-sleeved charcoal black maid dress to the ankles with puff shoulders and white lace cuffs, white high collar, big gray ribbon at the neck, ankle-length white frilled apron with a big white bow at the back, white socks, black flat shoes |
| moa | chibi maid girl, waist-length ash-beige hair with slightly wavy ends and neat bangs, white frilled maid headband with a white ribbon above the left ear, big round amber eyes, light blush, white shirt with a red and navy plaid ribbon tie, camel knit cardigan, white frilled apron with shoulder frills and a big bow at the back, black skirt, white knee socks, brown loafers |
| moa_suit | the same ash-beige haired girl with amber eyes in a business suit: low ponytail tied with a pink scrunchie, no headband, black tailored jacket over a white collared shirt, black skirt, black low heels, small silver stud earrings, holding a stack of documents and a black pen |
| x1 | `SPARE_COMMON_EN` + `X1_EN` (specs/spares/README.md) — the pink bow must stay visible from the back views |
| x2 | `SPARE_COMMON_EN` + `X2_EN` — the teal lens reflections disappear in the back views, only the beret outline remains |
| x3 | `SPARE_COMMON_EN` + `X3_EN` — cat-ear hood outline must read clearly in profile, yellow pompoms only in front views |

검수: ① 8칸 모두 같은 옷·소품 ② 뒤 칸에서 꽁지머리(박사)·남색 줄(하루)·케이블(초파리)·통풍구(주판봇)·큰 흰 리본(시아·모아)이 보임 ③ 미공개는 포인트 색 한 가지뿐 ④ 3D 시트와 키 비율이 같음.

## 5. 새 식구를 더할 때
1. `chars3d/lab3d.js` — `ROSTER`에 한 줄, `B.{key}` 빌더 하나 (기존 빌더를 복사해 머리·옷만 바꾸면 됨)
2. `specs/3d/characters3d.json` — `characters`에 항목 하나
3. `chars3d/tools/render_views.py` — `CHARS`에 한 줄 → 실행하면 이미지 27장·시트·views.json이 갱신됨
4. 공개 전이면 `hidden: true` (설정 화면에서 🔒 뒤로 숨음)
