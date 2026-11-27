# 갤러리 가져오기 — 표정·포즈·설정 시트

연구실 식구 갤러리([ahnboat_lab_gallery](https://adminmrobo.github.io/ahnboat_lab_gallery/))의 `data/gallery.json`에서 이 라이브러리에 없는 그림을 골라 복사해 온 묶음입니다.

- 페이지: [gallery_import.html](https://adminmrobo.github.io/fruitfly-lab-expressions/gallery_import.html)
- 목록: [`gallery_import.json`](gallery_import.json) — 그림마다 ID, 카테고리, 캐릭터, 파일 위치, 원래 저장소·경로·콘텐츠·생성일, 프롬프트(있을 때)
- 파일: 페이지용 WebP `images/gallery_import/{expressions,poses,sheets}/`, 원본 `images/_sheets/gallery_import/…`

## 카테고리와 ID

| 카테고리 | ID | 갤러리 쪽 기준 |
|---|---|---|
| 표정 | `GX-E###` | 갤러리 종류 '표정·포즈' 중 포즈가 아닌 것 |
| 포즈 | `GX-P###` | 갤러리 종류 '표정·포즈' 중 경로에 `pose`가 들어간 것 |
| 설정 시트 | `GX-S###` | 갤러리 종류 '설정 시트' (콘티 스케치·배너는 뺌) |
| 3D 좌표 | `GX-C###` | 다음 묶음으로 추가 예정 |

## 중복을 뺀 기준

1. **같은 파일**: 갤러리가 git 해시로 묶은 그림 가운데 이 저장소에서 이미 쓰는 것.
2. **같은 표정 ID**: 파일 이름의 표정 번호(E01~E24)가 이 라이브러리에 이미 있는 캐릭터·번호와 같은 것.
3. **생김새가 같은 사본**: 크기·형식·배경만 다른 사본. 배경을 지우고 그림 영역만 잘라 비교한 뒤, 실루엣 캐릭터(X1~X3)처럼 눈만 다른 그림은 눈으로 한 장씩 확인했습니다.
4. 가져온 그림끼리 겹치면 가장 큰 원본 하나만 남기고, 나머지 위치는 `source.also_in`에 적었습니다.

실제 인물 사진, 콘티 스케치, 장면 배너는 이 묶음에 넣지 않았습니다.

> MONEY-ROBO는 (주)M-Robo의 상표권이 있는 캐릭터로, 비상업적·상업적 이용이 모두 제한됩니다.
