# 주판봇 (AbaBot) 표정 세트 — 인덱스

- 총 **24개 표정**, 4개 카테고리 × 6개, 모든 캐릭터 공통 ID 체계 E01~E24
- 명세 ↔ 이미지 1:1 규칙: `specs/jupanbot/expressions/{ID}_{slug}.md` ↔ `images/jupanbot/{ID}_{slug}.png`
- 공통 아이덴티티: [`00_character_core.md`](00_character_core.md)
- 참조 이미지: `refs/original/jupanbot_ref_genspark_v0.png`
- 생성 순서: **E13(기준)** → 기본 감정 → 업무 → 미묘한 감정 → 코믹 과장
- 상태: 지금은 24칸 모두 벡터 그림 v1(원본 SVG는 ahnboat_lab_explainer/packs/character/jupanbot_vector/). 더 풍부한 그림을 받으면 같은 파일명으로 덮어쓰고 상태를 generated로 바꿉니다.
- Genspark용 프롬프트 모음: `ahnboat_lab_explainer/packs/character/jupanbot_genspark/GENSPARK_prompts.md`

| ID | 카테고리 | 표정 | EN | 명세 | 이미지 | 상태 |
|---|---|---|---|---|---|---|
| E01 | 기본 감정 | 기쁨 | Joy | [E01_joy.md](expressions/E01_joy.md) | `images/jupanbot/E01_joy.png` | vector-v1 |
| E02 | 기본 감정 | 슬픔 | Sadness | [E02_sadness.md](expressions/E02_sadness.md) | `images/jupanbot/E02_sadness.png` | vector-v1 |
| E03 | 기본 감정 | 분노 | Anger | [E03_anger.md](expressions/E03_anger.md) | `images/jupanbot/E03_anger.png` | vector-v1 |
| E04 | 기본 감정 | 놀람 | Surprise | [E04_surprise.md](expressions/E04_surprise.md) | `images/jupanbot/E04_surprise.png` | vector-v1 |
| E05 | 기본 감정 | 두려움 | Fear | [E05_fear.md](expressions/E05_fear.md) | `images/jupanbot/E05_fear.png` | vector-v1 |
| E06 | 기본 감정 | 혐오 | Disgust | [E06_disgust.md](expressions/E06_disgust.md) | `images/jupanbot/E06_disgust.png` | vector-v1 |
| E07 | 업무 | 설명 | Explaining | [E07_explaining.md](expressions/E07_explaining.md) | `images/jupanbot/E07_explaining.png` | vector-v1 |
| E08 | 업무 | 안내 | Guiding | [E08_guiding.md](expressions/E08_guiding.md) | `images/jupanbot/E08_guiding.png` | vector-v1 |
| E09 | 업무 | 생각 | Thinking | [E09_thinking.md](expressions/E09_thinking.md) | `images/jupanbot/E09_thinking.png` | vector-v1 |
| E10 | 업무 | 확인 | Confirming | [E10_confirming.md](expressions/E10_confirming.md) | `images/jupanbot/E10_confirming.png` | vector-v1 |
| E11 | 업무 | 사과 | Apologizing | [E11_apologizing.md](expressions/E11_apologizing.md) | `images/jupanbot/E11_apologizing.png` | vector-v1 |
| E12 | 업무 | 응원 | Cheering | [E12_cheering.md](expressions/E12_cheering.md) | `images/jupanbot/E12_cheering.png` | vector-v1 |
| E13 | 미묘한 감정 | 기본(중립) | Neutral | [E13_neutral.md](expressions/E13_neutral.md) | `images/jupanbot/E13_neutral.png` | vector-v1 |
| E14 | 미묘한 감정 | 머쓱함 | Sheepish | [E14_sheepish.md](expressions/E14_sheepish.md) | `images/jupanbot/E14_sheepish.png` | vector-v1 |
| E15 | 미묘한 감정 | 당황 | Flustered | [E15_flustered.md](expressions/E15_flustered.md) | `images/jupanbot/E15_flustered.png` | vector-v1 |
| E16 | 미묘한 감정 | 뿌듯함 | Proud | [E16_proud.md](expressions/E16_proud.md) | `images/jupanbot/E16_proud.png` | vector-v1 |
| E17 | 미묘한 감정 | 졸림 | Sleepy | [E17_sleepy.md](expressions/E17_sleepy.md) | `images/jupanbot/E17_sleepy.png` | vector-v1 |
| E18 | 미묘한 감정 | 삐짐 | Sulking | [E18_sulking.md](expressions/E18_sulking.md) | `images/jupanbot/E18_sulking.png` | vector-v1 |
| E19 | 코믹 과장 | 반짝눈(감동·기대) | Sparkling Eyes | [E19_sparkle_eyes.md](expressions/E19_sparkle_eyes.md) | `images/jupanbot/E19_sparkle_eyes.png` | vector-v1 |
| E20 | 코믹 과장 | 식은땀 | Big Sweat Drop | [E20_sweat_drop.md](expressions/E20_sweat_drop.md) | `images/jupanbot/E20_sweat_drop.png` | vector-v1 |
| E21 | 코믹 과장 | 폭포 눈물 | Waterfall Tears | [E21_waterfall_tears.md](expressions/E21_waterfall_tears.md) | `images/jupanbot/E21_waterfall_tears.png` | vector-v1 |
| E22 | 코믹 과장 | 뿔남 | Puffed Angry | [E22_puffed_angry.md](expressions/E22_puffed_angry.md) | `images/jupanbot/E22_puffed_angry.png` | vector-v1 |
| E23 | 코믹 과장 | 멍 | Blank Dot Eyes | [E23_blank_dot_eyes.md](expressions/E23_blank_dot_eyes.md) | `images/jupanbot/E23_blank_dot_eyes.png` | vector-v1 |
| E24 | 코믹 과장 | 충격 | Shock | [E24_shock.md](expressions/E24_shock.md) | `images/jupanbot/E24_shock.png` | vector-v1 |
