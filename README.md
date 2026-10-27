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
| `money_robo` | **MONEY-ROBO** | 머니로보 · 라이벌 B "확신" | 9 → 24 |
| `fruitfly` | **초파리** | 초파리 연구원 · 라이벌 A "의심" | 6 → 24 |

> 하루와 세나는 같은 인물입니다. 기본 호칭은 "하루"이고, 방송·공연처럼 예명을 쓰는 맥락에서만 "세나"라고 부릅니다. 외형과 표정 세트는 같습니다.

## 폴더 구조

```
.
├─ index.html                  # 갤러리 (GitHub Pages 진입점)
├─ README.md
├─ images/
│  ├─ haru/        E01_joy.png … E24_shock.png
│  ├─ doctor/      …
│  ├─ money_robo/  …
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
   ├─ Money-Robo_캐릭터설정.md   # 세계관·캐릭터 설정서
   └─ original/                 # 원본 캐릭터 시트 7장
```

## 1:1 연결 규칙

```
specs/{캐릭터}/expressions/{ID}_{slug}.md   ↔   images/{캐릭터}/{ID}_{slug}.png
```

예: `specs/money_robo/expressions/E19_sparkle_eyes.md` ↔ `images/money_robo/E19_sparkle_eyes.png`

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
4. 부위별 지시 (캐릭터마다 항목이 다름. 예: MONEY-ROBO는 스크린 픽셀, 초파리는 겹눈 눈꺼풀)
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
| 원본 칸에서 잘라 냄 | MONEY-ROBO 9장 (`money_robo_expressions_9.png`), 초파리 6장 (`fruitfly_sprites_6.png`). 갤러리에 "원본"으로 표시 |
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
