# 초파리 연구실 · 캐릭터 표정 라이브러리

「초파리 연구실」 세계관 캐릭터 4명의 **표정 이미지 96장**과, 이미지 하나하나에 1:1로 연결된 **표정 명세서(MD)**를 모은 저장소입니다.

- 캐릭터 4명 × 공통 표정 24종 (E01~E24)
- 화풍: 16비트 SNES 시대 픽셀 아트
- `index.html`을 열면 갤러리에서 이미지, 명세, 생성 프롬프트를 바로 볼 수 있습니다

## 캐릭터

| 키 | 캐릭터 | 별칭 · 역할 | 원본 표정 → 현재 |
|---|---|---|---|
| `haru` | **하루** | 예명 **세나** · 조수 (실험 진행·기록) | 6 → 24 |
| `doctor` | **박사** | Professor · 해설·심판·사회자 | 2 → 24 |
| `jupanbot` | **주판봇** | 주판봇 · 라이벌 B "확신" | 9 → 24 |
| `fruitfly` | **초파리** | 초파리 연구원 · 라이벌 A "의심" | 6 → 24 |
| `sia` | **시아** (No.005) | 메이드 인턴 · 심판·방청객 | 명세 24 · 이미지 24 |
| `moa` | **모아** (No.006) | 메이드 인턴 · 방청객·심판 · 정장 의상 | 명세 24 · 이미지 24 |
| `x1`·`x2`·`x3` | **미공개** (No.007~009) | 실루엣 슬롯 · 버튼을 눌러야 보임 | 명세 24씩 · 이미지 9씩 (E13·E01·E03·E02·E04·E09·E16·E15·E24) |

### 새 식구 (2026-11-11)
- 시아·모아는 하루와 **같은 표정 24종·같은 명세 구성**, 동작은 박사·조수와 **같은 배열**(시아 S1~S15 = 박사 자리·오른쪽, 모아 M1~M16 = 조수 자리·왼쪽, 심판 3장·방청객 2장 포함, 모아 정장 M16).
- 기본형·벡터판(2026-11-11 생성): 벡터 `refs/original/sia_vector_base.png`·`moa_vector_base.png`, 표정 생성 원본 시트 `images/_sheets/expressions/`.
- 기본형(2026-11-11 생성): 설정 시트 `refs/original/sia_sheet.png`·`moa_sheet.png`, 8방향 `images/_sheets/interns_turnaround8.png`, 여섯 식구 단체 `images/_sheets/lab6_lineup.png`(주판봇 정본판).
- 미공개 X1~X3는 앞으로 들어올 식구의 자리입니다. 갤러리·동작 페이지·식구 명부에서 **🔒 버튼**을 눌러야 보입니다.
- 기본형 생성 순서·프롬프트: [`specs/interns/PROMPTS_base.md`](specs/interns/PROMPTS_base.md) · 동작: [`specs/motions/PROMPTS_interns.md`](specs/motions/PROMPTS_interns.md) · 미공개 규칙: [`specs/spares/README.md`](specs/spares/README.md)

> 하루와 세나는 같은 인물입니다. 기본 호칭은 "하루"이고, 방송·공연처럼 예명을 쓰는 맥락에서만 "세나"라고 부릅니다. 외형과 표정 세트는 같습니다.

## 폴더 구조

```
.
├─ index.html                  # 갤러리 (GitHub Pages 진입점)
├─ characters3d.html           # 3D 캐릭터 설정 화면
├─ chars3d/lab3d.js            # 3D 모델 모듈 (+ tools/ 렌더러)
├─ README.md
├─ images/
│  ├─ haru/        E01_joy.png … E24_shock.png
│  ├─ doctor/      …
│  ├─ jupanbot/  …
│  ├─ fruitfly/    …
│  └─ _sheets/     # 생성 원본 시트 (칸별로 자르기 전)
├─ specs/
│  ├─ README.md                # 공통 표정 ID 표, 연결 규칙
│  └─ {캐릭터}/
│     ├─ 00_character_core.md  # 이름·역할, 외형 고정값, 프롬프트 토큰
│     ├─ README.md             # 표정 24종 목록
│     ├─ expressions.json      # 자동화용 (프롬프트·네거티브·대사 포함)
│     └─ expressions/E01_joy.md … E24_shock.md
└─ refs/
   ├─ specs/jupanbot/00_character_core.md   # 세계관·캐릭터 설정서
   └─ original/                 # 원본 캐릭터 시트 7장
```

## 동작·의상 라이브러리 (motion v1.1, 2026-11-08)

표정과 별도로, 여섯 캐릭터와 미공개 식구의 **전신 동작 시트 59장(프레임 464장)**을 더했습니다(시아 S1~S15 · 모아 M1~M16 · 미공개 X1A~X3A 포함). 갤러리: [`motions.html`](motions.html) · 명세: [`specs/motions/README.md`](specs/motions/README.md)

| 캐릭터 | 시트 | 동작 |
|---|---|---|
| 박사 | D1~D10 | 서기·걷기, 점프·돌진, 잽·가드·피격, 승리·KO, 필살기 3종(특이값 분해 참·브로드캐스트 웨이브·역전파 카운터), 의상 3종, 전투복·사이버 돌진·필살기 |
| 하루 | A1~A10 | 서기·걷기, 점프·돌진, 잽·가드·피격, 승리·KO, 필살기 3종(원-핫 연타·경사하강 킥·역전파 카운터), 의상 3종, 전투복·사이버 돌진·필살기 |
| 초파리 | F1~F3 | 심판: 대기·시작 신호, 좌우 판정, 무승부·의심 |
| 주판봇 | R1~R2 | 점수판: 대기·주판 계산, 환호·실망 |

```
images/_sheets/motion/{시트}_{who}.png     생성 원본 (Genspark)
images/motions/{캐릭터}/{시트}_fNN.webp    투명 배경 프레임
specs/motions/motions.json                시트·구간·보는 쪽·기준 프레임·프롬프트
specs/motions/PROMPTS.md, PROMPTS_v1.1.md  캐릭터별 생성 프롬프트
```

## 3D 캐릭터 설정 (lab3d v1.0, 2026-11-12)

전원(박사·하루·초파리·주판봇·시아·모아·모아 정장·미공개 X1~X3)을 **같은 축척의 3D 모델**로 세웠습니다. 3D 공장 같은 화면에 2D 정본과 어긋나지 않게 넣기 위한 것입니다.
설정 화면: [`characters3d.html`](characters3d.html) · 설정서: [`specs/3d/README.md`](specs/3d/README.md)

| 항목 | 내용 |
|---|---|
| 모델 | `chars3d/lab3d.js` — three.js 모듈. `createLab3D(THREE).build('doctor', {unit: 1.75})` 로 다른 3D 페이지에서 그대로 씀 |
| 이미지 벡터 | 캐릭터마다 8방향 × 2높이(눈높이 8° · 공장 시점 32°) + 포즈 8종 + 표정 3종 = 27장, 모두 270장 (`images/3d/`) |
| 시트 | `images/3d/_sheets/{slug}_3d_sheet.png`, 전원 라인업 `lab10_lineup_3d_e08.png`·`_e32.png` |
| 목록·설정값 | `specs/3d/views.json` (그림 한 장 = 한 줄), `specs/3d/characters3d.json` (키·팔레트·3D 고정값) |
| 다시 만들기 | `python3 chars3d/tools/render_views.py` |
| 2D 픽셀 턴어라운드 | 설정서 4절의 프롬프트 + 3D 시트를 참조 이미지로 |

## 1:1 연결 규칙

```
specs/{캐릭터}/expressions/{ID}_{slug}.md   ↔   images/{캐릭터}/{ID}_{slug}.png
```

예: `specs/jupanbot/expressions/E19_sparkle_eyes.md` ↔ `images/jupanbot/E19_sparkle_eyes.png`

각 명세 MD의 맨 위 설정 블록에 `image_file`, `image_status`, `original_match`가 들어 있습니다.

## 공통 표정 ID

| 카테고리 | ID |
|---|---|
| 기본 감정 | E01 기쁨 · E02 슬픔 · E03 분노 · E04 놀람 · E05 두려움 · E06 혐오 |
| 업무 | E07 설명 · E08 안내 · E09 생각 · E10 확인 · E11 사과 · E12 응원 |
| 미묘한 감정 | **E13 기본(기준 이미지)** · E14 머쓱함 · E15 당황 · E16 뿌듯함 · E17 졸림 · E18 삐짐 |
| 코믹 과장 | E19 반짝눈 · E20 식은땀 · E21 폭포 눈물 · E22 뿔남 · E23 멍 · E24 충격 |

## 명세 MD 구성

1. 감정 의도 · 2. 사용 상황 · 3. 원본 대응
4. 부위별 지시 (캐릭터마다 항목이 다름. 예: 주판봇은 스크린 픽셀, 초파리는 겹눈 눈꺼풀)
5. 고정 항목 · 6. 대사 예시
7. **완성형 생성 프롬프트 (EN)**: 그대로 붙여 넣어 쓰면 됩니다
8. 네거티브 프롬프트 · 9. 금지 사항 · 10. 검수 체크리스트

## 새 이미지를 만들 때

1. 명세 7절의 프롬프트를 복사합니다 (`expressions.json`의 `prompt_en`도 같은 내용).
2. `refs/original/`의 해당 캐릭터 원본 시트와 `images/{캐릭터}/E13_neutral.png`를 참조 이미지로 함께 넣습니다.
3. 결과물은 명세의 `image_file` 경로에 같은 파일명으로 저장하고, `image_status`를 `approved` 등으로 업데이트합니다.

## 이미지 출처

| 구분 | 내용 |
|---|---|
| 원본 칸에서 잘라 냄 | 주판봇 9장 (`jupanbot_ref_genspark_v0.png`), 초파리 6장 (`fruitfly_sprites_6.png`). 갤러리에 "원본"으로 표시 |
| 신규 생성 | 나머지 81장. 원본 시트를 참조 이미지로 넣고 6칸 시트로 생성한 뒤 칸별로 잘라 냄 (`images/_sheets/`) |

## GitHub에 올리기

```bash
git init
git add .
git commit -m "Fruit Fly Lab expression library v1.1"
git branch -M main
git remote add origin https://github.com/<USER>/<REPO>.git
git push -u origin main
```

**GitHub Pages:** 저장소 **Settings → Pages → Branch: `main` / root**를 선택하면 `https://<USER>.github.io/<REPO>/`에서 갤러리가 열립니다. `.nojekyll`이 들어 있어 폴더명이 그대로 서비스됩니다.

> 로컬에서 `index.html`을 더블클릭하면 브라우저 보안 정책 때문에 JSON을 못 읽을 수 있습니다. 이때는 `python3 -m http.server`로 띄운 뒤 `http://localhost:8000`에서 여세요.

## 주의

이 시리즈는 교육용 코미디입니다. 주가·비트코인 관련 표현은 예측 기법을 설명하기 위한 연출일 뿐 투자 권유가 아닙니다. 실제 기업·코인 로고는 쓰지 않습니다.


## 헤어 어레인지 벡터 (hair v1.0, 2026-11-12)
여성 캐릭터 **하루·시아·모아**에게만 적용하는 네 번째 축입니다(미공개 X1~X3 제외). 스타일 20종 = H00 정본 + H01~H19(하프 업·포니테일·땋기·트위스트·업스타일·액세서리), 캐릭터마다 앞·뒤 3/4 그림 한 쌍.
- 갤러리: `hair.html` · 명세: `specs/hair/README.md` · 설정값: `specs/hair/hair.json` · 프롬프트: `specs/hair/PROMPTS.md` (캐릭터당 시트 7장)
- H를 정하지 않으면 H00(정본). 표정·동작·3D는 H00 기준 그대로입니다.
- 현재 상태: Genspark 시트 21장(`images/_sheets/hair/`)을 잘라 120장(`images/hair/{캐릭터}/H##_{slug}_front|back.png`, 512×512 투명) 반영. 상태 generated, 검수 후 approved.

## 캐릭터 DB (엑셀, `db/`)
캐릭터·표정·동작·헤어·3D 벡터를 한 파일로 모은 DB입니다. 벡터가 바뀔 때마다 `db/fruitfly_character_db_v{판}_{날짜}.xlsx`를 **새 파일로 추가**하고, 이전 판은 지우지 않습니다. 판별 변경 내용은 `db/README.md`.

## 커밋 규칙
이 저장소의 커밋 작성자·커미터는 adminmrobo(sangsun.ahn@gmail.com) 한 명만 씁니다. 커밋 메시지에 다른 공동 작성자(Co-Authored-By) 줄을 넣지 않습니다.
