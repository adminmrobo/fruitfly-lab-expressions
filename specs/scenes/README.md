# 시리즈 장면 그림 (scenes v1.0, 2026-11-16)

표정·동작·헤어·3D·공장에 이은 여섯 번째 축입니다. 해설 시리즈의 **표지·컷·카드 썸네일**처럼 연구실 식구가 함께 나오는 장면 그림을 모읍니다. 장면 그림은 캐릭터 정본(표정 E##, 의상 U00, 헤어 H00)을 참조 이미지로 넣어 Genspark로 만듭니다.

## 규칙

- 경로: `images/scenes/{시리즈}/{id}.webp` (페이지에 쓰는 크기) ↔ `images/_sheets/scenes/{시리즈}/{id}.png` (생성 원본)
- 목록·설정값: `specs/scenes/scenes.json` (그림 한 장 = 한 항목: 쓰는 페이지, 등장 캐릭터, 참고 표정, 얹을 대사, 상태)
- 프롬프트: `specs/scenes/PROMPTS_{시리즈}.md`
- 말풍선은 그림에서 **비워 두고**, 대사는 페이지에서 HTML 글자로 얹습니다(그림 생성기는 한글을 잘 못 그림).
- 패러디 장면은 말투·구도만 빌리고, 다른 작품의 인물·의상·소품은 쓰지 않습니다. 연구실 식구는 각자의 정본 모습 그대로입니다.

## 최적화 첫걸음 (optimization_first_step)

사용 저장소: [adminmrobo/optimization_3d_map](https://github.com/adminmrobo/optimization_3d_map) — `first_step_1.html`·`first_step_2.html`, ahnboat.xyz SPECIAL 카드

| id | 쓰는 곳 | 캐릭터 | 얹는 대사 | 상태 |
|---|---|---|---|---|
| fs_cover_01 | ① 표지 | 하루·시아·모아 | 혹시… / 미분 좋아하세요? | approved |
| fs_cover_02 | ② 표지 | 박사·모아·초파리·주판봇 | 얼마만큼 만들까요? | approved |
| fs_prologue_1 | ① 프롤로그 1컷 | 하루 | 혹시… / 미분 좋아하세요? | approved |
| fs_prologue_2 | ① 프롤로그 2컷 | 시아 | 그럼… / 미분은 언제부터 있었어요? | approved |
| fs_prologue_3 | ① 프롤로그 3컷 | 모아 | 그걸로… / 뭘 할 수 있어요? | approved |
| fs_thumb | ahnboat.xyz 카드 | 하루 | — | approved |
