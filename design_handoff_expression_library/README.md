# Handoff: 초파리 연구실 · 캐릭터 표정 라이브러리 (Expression Library)

## Overview
「초파리 연구실」 세계관 캐릭터 4명(하루/세나, 박사, MONEY-ROBO, 초파리)의 **표정 이미지 96장**(4 × 24)을 둘러보는 갤러리 웹페이지입니다. 이미지마다 1:1로 연결된 **표정 명세서(MD)**와 **생성 프롬프트**도 함께 볼 수 있습니다.

쓰는 사람과 목적:
- 콘텐츠 제작자: 장면에 맞는 표정을 ID(E01~E24)로 찾아 씁니다.
- 이미지 생성 담당자: 명세의 영어 프롬프트를 복사해 새 이미지를 다시 만듭니다.
- 배포 형태: 정적 사이트 (GitHub Pages 등)

## About the Design Files
이 패키지의 `index.html`은 **HTML로 만든 디자인 레퍼런스**입니다. 의도한 모양과 동작을 보여 주는 프로토타입이며, 그대로 복사해 쓰는 프로덕션 코드가 아닙니다.

- **할 일:** 이 디자인을 대상 코드베이스의 환경(React, Vue, Astro, Next.js 등)에서 기존 패턴과 라이브러리로 다시 구현합니다.
- **환경이 아직 없다면:** 가장 적합한 프레임워크를 고르면 됩니다. 정적 사이트라면 Astro, Vite + React, Next.js static export를 권장합니다.
- **데이터 원본은 그대로 씁니다:** `specs/**/expressions.json`과 `specs/**/*.md`는 바로 사용할 수 있는 실데이터입니다.

## Fidelity
**High-fidelity (hifi).** 최종 색상, 타이포그래피, 간격, 인터랙션이 확정된 상태입니다. 아래 토큰값 그대로 픽셀 단위로 재현해 주세요.

---

## Screens / Views

### 1. Library (단일 페이지)
**목적:** 캐릭터를 고르고, 분류로 걸러서, 표정 카드를 둘러봅니다.

**레이아웃:** 콘텐츠 최대 폭 `1360px`, 가운데 정렬, 좌우 패딩 `32px` (≤760px에서는 `18px`).

#### 1-1. Header (`header.top`)
- 패딩 `40px 32px 20px`
- **Eyebrow:** "Fruit Fly Lab · Expression Library v1.1"
  - JetBrains Mono 12px, `letter-spacing:.08em`, 대문자, 색 `--mute`
- **H1:** "초파리 연구실 캐릭터 표정 라이브러리"
  - IBM Plex Sans KR 700, 34px, line-height 1.15, `letter-spacing:-.01em`, margin `8px 0 10px`
- **Lede:**
  - 문구: "캐릭터 4명 × 공통 표정 24종. 모든 이미지는 같은 ID(E01~E24)의 명세 MD와 1:1로 연결되며, 명세에는 바로 쓸 수 있는 생성 프롬프트가 들어 있습니다. 카드를 누르면 명세와 프롬프트를 볼 수 있습니다."
  - 15px, 색 `--mute`, max-width 720px, `text-wrap:pretty`
- **Stats:** flex, gap 28px, margin-top 18px, Mono 13px, 색 `--mute`
  - 항목 3개: `4 캐릭터` / `24 표정 / 캐릭터` / `96 이미지 · 명세`
  - 숫자는 `<b>` 블록, 18px 600, 색 `--fg`

#### 1-2. Sticky Nav (`nav.bar`)
- `position:sticky; top:0; z-index:5`
- 배경 `color-mix(in oklab, var(--bg) 92%, transparent)` + `backdrop-filter: blur(6px)`
- 아래 테두리 `1px solid --line`
- 내부: flex, gap 10px, 패딩 `12px 32px`, wrap
- **Character chips (왼쪽, 4개):**
  - pill 모양: radius 999px, 테두리 `1px --line`, 배경 `--panel`, 패딩 `6px 14px 6px 6px`, 500 weight
  - 안쪽 왼쪽에 30×30 원형 썸네일: `images/{key}/E13_neutral.png`, `object-fit:cover`, `image-rendering:pixelated`
  - 라벨: 하루 / 박사 / MONEY-ROBO / 초파리
  - 선택 상태: 배경 `--fg`, 글자 `#fff`, 테두리 `--fg`
- **Filters (오른쪽, segmented):**
  - 컨테이너: 배경 `--panel`, 테두리 `1px --line`, radius 999px, 패딩 3px, gap 4px
  - 버튼: 13px, 패딩 `5px 12px`, radius 999px, 색 `--mute`
  - 항목: 전체 / 기본 감정 / 업무 / 미묘한 감정 / 코믹 과장
  - 선택 상태: 배경 `--accent-soft`, 글자 `--accent`, 600

#### 1-3. Character Head (`.charhead`)
- grid `160px 1fr auto`, gap 24px, 패딩 `28px 0 8px`
- **썸네일:** 160×160, `object-fit:contain`, pixelated, 배경 `--panel`, 테두리 `1px --line`, radius 12px (기준 이미지 E13)
- **이름:** H2 26px
- **별칭:** 14px `--mute`
- **설명:** 15px, max 640px. 문구는 아래 *Copy* 참고
- **링크 3개 (오른쪽 세로 배치):** `00_character_core.md`, `README.md (표정 목록)`, `expressions.json`
  - Mono 12px, 테두리 `1px --line`, 배경 `--panel`, 패딩 `6px 10px`, radius 6px, 색 `--mute`
  - hover 시 글자색 `--fg`
- **≤760px:** grid `96px 1fr`, 썸네일 96px, 링크는 아래 줄 전체 폭에 가로 배치(wrap)

#### 1-4. Category Section
- **H3 (분류 제목):** Mono 13px 600, 대문자, `letter-spacing:.06em`, 색 `--mute`, margin `32px 0 12px`
  - 제목 오른쪽으로 남은 폭을 1px `--line` 가로선이 채움 (`::after`, flex 1)
- **분류 순서:** basic(기본 감정) → assistant(업무) → subtle(미묘한 감정) → comic(코믹 과장)
- **Grid:** `repeat(auto-fill, minmax(170px, 1fr))`, gap 14px

#### 1-5. Expression Card (`.card`, `<button>`)
- 배경 `--panel`, 테두리 `1px --line`, radius 10px, overflow hidden
- **이미지:** width 100%, `aspect-ratio:1`, `object-fit:contain`, pixelated, 배경 `#f8f7f5`, `loading="lazy"`
- **캡션:** 패딩 `9px 11px`, flex `space-between`, baseline 정렬
  - 왼쪽: 한국어 표정명, 500 weight
  - 오른쪽: ID, Mono 11px `--mute`
  - 원본 시트에서 잘라 낸 이미지는 ID 옆에 **"원본" 배지**: Mono 10px, 색 `--accent`, 배경 `--accent-soft`, 패딩 `1px 6px`, radius 4px
- **Hover:** `translateY(-2px)` + `box-shadow: 0 6px 18px rgba(0,0,0,.08)`, transition `.15s` (transform, box-shadow)

### 2. Detail Dialog (`<dialog>` modal)
**목적:** 표정 하나의 상세 정보를 보고 프롬프트를 복사합니다.

- **Dialog 박스:** radius 14px, padding 0, max-width 980px, width `calc(100% - 40px)`, max-height `calc(100vh - 40px)`, shadow `0 30px 80px rgba(0,0,0,.3)`
- **Backdrop:** `rgba(20,18,22,.55)`
- **Body:** grid `380px 1fr`
  - **왼쪽 `.pic`:** 배경 `#f8f7f5`, 패딩 20px, 오른쪽 테두리 `1px --line`, 이미지 100% pixelated
  - **오른쪽 `.info`:** 패딩 `24px 26px`, 넘치면 세로 스크롤
- **제목:** 한국어 표정명 22px + 영어명 16px 400 `--mute`
- **메타 줄:** Mono 12px `--mute`, 형식 `{캐릭터} · {ID} · {분류}`
- **`<dl>` 정보:** grid `96px 1fr`, gap `6px 14px`, 14px, `dt`는 `--mute`
  - 항목: 이미지(링크), 명세(링크), 원본 대응 (값이 없으면 "신규 표정"), 대사 예시 (따옴표로 감싸 줄마다 하나씩)
- **프롬프트 블록 2개:** "생성 프롬프트 (EN)", "네거티브 프롬프트"
  - 라벨 줄: Mono 11px 대문자 `--mute`, 오른쪽에 [복사] 버튼
  - `<pre>`: 배경 `#1d1b20`, 글자 `#eae6ee`, Mono 12px, line-height 1.55, 패딩 `12px 14px`, radius 8px, `pre-wrap`
- **이전/다음 버튼:** 2개가 폭을 반씩 나눔, 테두리 `1px --line`, 패딩 8px, radius 8px
- **닫기 버튼:** 오른쪽 위 (top/right 12px), 32px 원형, 배경 `rgba(255,255,255,.9)`, "×"
- **≤760px:** 1열로 바뀌고, 이미지 아래에 `1px --line` 테두리

### Footer
- 13px `--mute`, 패딩 `0 32px 40px`
- 문구: "표정 ID 체계·연결 규칙은 specs/README.md, 저장소 안내는 README.md를 참고하세요." (두 파일명은 링크)

---

## Interactions & Behavior
| 동작 | 결과 |
|---|---|
| 캐릭터 칩 클릭 | `cur` 변경 → 해당 `expressions.json` 로드(캐시) → 헤더와 그리드 다시 그림 |
| 필터 클릭 | `filt` 변경 → `category === filt`인 표정만 표시. "전체"는 필터 없음 |
| 카드 클릭 | Dialog 열기 (`showModal()`), 현재 필터된 목록 안에서의 인덱스로 엶 |
| Dialog ←/→ 키, 이전/다음 버튼 | 필터된 목록 안에서 순환 이동 (마지막 다음은 처음) |
| Dialog 바깥(backdrop) 클릭, ×, Esc | 닫기 |
| [복사] | 프롬프트를 클립보드에 복사, 버튼 문구가 1.2초간 "복사됨"으로 바뀜 |
| 카드 hover | 2px 위로 뜨고 그림자 생김 (.15s) |

- **유지되는 상태:** `localStorage`의 `lib_char`(선택한 캐릭터), `lib_filter`(선택한 필터). 새로고침해도 유지됩니다.
- **로딩:** JSON fetch 중에는 이전 화면을 그대로 둡니다. 필요하면 스켈레톤 카드를 넣어도 됩니다.
- **에러:** fetch 실패 처리가 아직 없습니다. 구현할 때 "목록을 불러오지 못했습니다" 메시지와 재시도 버튼을 추가해 주세요.
- **반응형 (breakpoint 760px):** 헤더 grid가 축소되고, Dialog가 1열이 되고, 좌우 패딩이 18px로 줄어듭니다. 카드 그리드는 auto-fill이라 저절로 맞춰집니다.

## State Management
```ts
type CharKey = 'haru' | 'doctor' | 'money_robo' | 'fruitfly';
type Category = 'basic' | 'assistant' | 'subtle' | 'comic';
state = {
  cur: CharKey,                    // localStorage 'lib_char', 기본값 'haru'
  filt: 'all' | Category,          // localStorage 'lib_filter', 기본값 'all'
  cache: Record<CharKey, Expression[]>,
  list: Expression[],              // 현재 필터가 적용된 목록 (dialog 이동 기준)
  idx: number,                     // dialog에 열린 항목의 list 인덱스
  dialogOpen: boolean
}
```

**데이터:** `GET specs/{key}/expressions.json` → `Expression[]`
```jsonc
{
  "id": "E01", "slug": "joy", "category": "basic", "category_ko": "기본 감정",
  "ko": "기쁨", "en": "Joy",
  "spec": "specs/haru/expressions/E01_joy.md",
  "image": "images/haru/E01_joy.png",
  "original_match": "원본 1행 2열 ..." | null,   // null이 아니면 "원본" 배지 표시
  "prompt_en": "...", "negative_en": "...",
  "lines": ["대사1", "대사2"]
}
```

**캐릭터 메타 (현재는 하드코딩):**
| key | name | alias | desc |
|---|---|---|---|
| haru | 하루 | 예명 세나 · 조수 | 실제로 일을 다 하는 연구원. 꼼꼼한 실험과 기록, 점수 기록 담당. 분홍+남색 투톤 장발, 정수리 번 2개, 라벤더 후드 + 흰 랩코트. |
| doctor | 박사 | Professor · 해설·심판·사회자 | 자신만만한 치비 과학자. 이론과 큰소리로 판단한다. 숯색 뾰족 머리 + 흰 줄, 굵은 눈썹, 청록 안경, 흰 가운 + 검은 조끼. 시그니처는 보라 불꽃. |
| money_robo | MONEY-ROBO | 머니로보 · 라이벌 B "확신" | 돈과 숫자를 사랑하는 떠다니는 로봇. "데이터가 그렇게 말하고 있어요!" 표정은 검은 스크린의 금빛 픽셀로만 표현. |
| fruitfly | 초파리 | 초파리 연구원 · 라이벌 A "의심" | 작지만 날카로운 연구원. 호기심과 생물학적 직관으로 판단한다. "정말 그럴까?" 빨간 겹눈, 남색 헬멧과 케이블, 흰 가운. |

권장: 이 메타는 `specs/{key}/00_character_core.md`의 설정 블록이나 별도 `characters.json`으로 옮겨 주세요.

## Design Tokens
```css
--bg:#f4f2ee;        /* 페이지 배경 (따뜻한 오프화이트) */
--panel:#ffffff;     /* 카드·칩 배경 */
--fg:#1d1b20;        /* 본문, 선택된 칩 */
--mute:#77727b;      /* 보조 텍스트 */
--line:#e2ded8;      /* 테두리·구분선 */
--accent:oklch(0.62 0.15 30);       /* ≈ #d0603f, 필터 선택·원본 배지 */
--accent-soft:oklch(0.95 0.03 30);  /* ≈ #f8e9e3 */
image-bg:#f8f7f5;    /* 이미지 영역 배경 */
code-bg:#1d1b20; code-fg:#eae6ee;
backdrop:rgba(20,18,22,.55);
```

**Typography:**
- Sans: `"IBM Plex Sans KR"` 400/500/700 (Google Fonts)
- Mono: `"JetBrains Mono"` 400/600
- 크기 단계: 34 (H1) / 26 (H2) / 22 (dialog 제목) / 18 (stat 숫자) / 15 (본문) / 14 / 13 / 12 / 11 / 10

**Radius:** 999 (pill) · 14 (dialog) · 12 (헤더 썸네일) · 10 (카드) · 8 (pre, 버튼) · 6 (링크) · 5 (복사 버튼) · 4 (배지)

**Spacing:** 3 · 4 · 6 · 8 · 10 · 12 · 14 · 18 · 20 · 24 · 28 · 32 · 40

**Shadow:**
- 카드 hover: `0 6px 18px rgba(0,0,0,.08)`
- dialog: `0 30px 80px rgba(0,0,0,.3)`

**Images:** 모든 캐릭터 이미지에 `image-rendering: pixelated` 필수 (픽셀 아트)

## Assets
| 경로 (원본 저장소 기준) | 내용 | 비고 |
|---|---|---|
| `images/{haru,doctor,money_robo,fruitfly}/E01_joy.png … E24_shock.png` | 표정 이미지 96장, PNG, 약 330~410px 정사각형 | 번들에는 미포함. 원본 프로젝트에서 같은 경로로 복사 |
| `images/_sheets/*.png` | 칸별로 자르기 전 생성 시트 14장 | 참고용 |
| `refs/original/*.png` | 원본 캐릭터 시트 7장 | 생성할 때 참조 이미지로 씀 |
| `refs/Money-Robo_캐릭터설정.md` | 세계관·캐릭터 설정서 | |

- 출처: MONEY-ROBO 9장과 초파리 6장은 원본 시트를 잘라 낸 것이고, 나머지 81장은 AI로 생성(gpt-image-2)했습니다.
- 아이콘과 일러스트는 따로 쓰지 않았습니다. 웹폰트는 Google Fonts입니다.

## Files
| 파일 | 설명 |
|---|---|
| `index.html` | 갤러리 디자인 레퍼런스 (CSS·JS 인라인, 프레임워크 없음) |
| `specs/README.md` | 공통 표정 ID 표, 명세↔이미지 1:1 연결 규칙 |
| `specs/{key}/00_character_core.md` | 캐릭터별 외형 고정값, 팔레트, 프롬프트 토큰 |
| `specs/{key}/README.md` | 캐릭터별 표정 24종 목록 |
| `specs/{key}/expressions.json` | 갤러리 데이터 원본 |
| `specs/{key}/expressions/E??_*.md` | 표정별 명세 96개 (frontmatter: id, slug, image_file, image_status, original_match 등) |

## 구현 권장 사항
1. **정적 생성:** `expressions.json`을 빌드할 때 읽어 캐릭터별 페이지 `/haru`, `/doctor` 등을 만듭니다. 필터와 다이얼로그 상태는 쿼리스트링(`?f=comic&e=E19`)으로 공유할 수 있게 합니다.
2. **명세 MD 렌더:** Dialog에 "명세 전체 보기" 탭을 두고 MD를 렌더링합니다 (frontmatter는 숨김).
3. **접근성:** 카드 `alt`는 `"{캐릭터} {표정명}"`으로, Dialog는 포커스 트랩을 걸고 닫으면 원래 카드로 포커스를 돌려줍니다.
4. **이미지:** 원본 PNG를 유지하고, 썸네일만 WebP로 만들어 써도 됩니다. 이때도 `pixelated` 렌더링은 유지합니다.
