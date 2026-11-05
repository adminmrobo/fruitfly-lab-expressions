# 주판봇 (AbaBot) 표정 세트 — 인덱스

- 총 **24개 표정**, 4개 카테고리 × 6개, 모든 캐릭터 공통 ID 체계 E01~E24
- 명세 ↔ 이미지 1:1 규칙: `specs/jupanbot/expressions/{ID}_{slug}.md` ↔ `images/jupanbot/{ID}_{slug}.png`
- 공통 아이덴티티: [`00_character_core.md`](00_character_core.md)
- 참조 이미지: `refs/original/jupanbot_ref_genspark_v0.png`
- 생성 순서: **E13(기준)** → 기본 감정 → 업무 → 미묘한 감정 → 코믹 과장
- 상태 (2026-11-05): 기준은 단체 사진과 **기본 9종(gpt2, 공식)** — E13·E01·E03·E02·E04·E09·E16·E15·E24. 나머지 15칸은 **Genspark 픽셀 그림 v2(임시)**이며, gpt2판이 나오면 같은 파일명으로 덮어씁니다. 옛 벡터 그림 v1은 쓰지 않습니다.
- Genspark용 프롬프트 모음: `ahnboat_lab_explainer/packs/character/jupanbot_genspark/GENSPARK_prompts.md`

| ID | 카테고리 | 표정 | EN | 명세 | 이미지 | 상태 |
|---|---|---|---|---|---|---|
| E01 | 기본 감정 | 기쁨 | Joy | [E01_joy.md](expressions/E01_joy.md) | `images/jupanbot/E01_joy.png` | gpt2-v2 |
| E02 | 기본 감정 | 슬픔 | Sadness | [E02_sadness.md](expressions/E02_sadness.md) | `images/jupanbot/E02_sadness.png` | gpt2-v2 |
| E03 | 기본 감정 | 분노 | Anger | [E03_anger.md](expressions/E03_anger.md) | `images/jupanbot/E03_anger.png` | gpt2-v2 |
| E04 | 기본 감정 | 놀람 | Surprise | [E04_surprise.md](expressions/E04_surprise.md) | `images/jupanbot/E04_surprise.png` | gpt2-v2 |
| E05 | 기본 감정 | 두려움 | Fear | [E05_fear.md](expressions/E05_fear.md) | `images/jupanbot/E05_fear.png` | genspark-v2 |
| E06 | 기본 감정 | 혐오 | Disgust | [E06_disgust.md](expressions/E06_disgust.md) | `images/jupanbot/E06_disgust.png` | genspark-v2 |
| E07 | 업무 | 설명 | Explaining | [E07_explaining.md](expressions/E07_explaining.md) | `images/jupanbot/E07_explaining.png` | genspark-v2 |
| E08 | 업무 | 안내 | Guiding | [E08_guiding.md](expressions/E08_guiding.md) | `images/jupanbot/E08_guiding.png` | genspark-v2 |
| E09 | 업무 | 생각 | Thinking | [E09_thinking.md](expressions/E09_thinking.md) | `images/jupanbot/E09_thinking.png` | gpt2-v2 |
| E10 | 업무 | 확인 | Confirming | [E10_confirming.md](expressions/E10_confirming.md) | `images/jupanbot/E10_confirming.png` | genspark-v2 |
| E11 | 업무 | 사과 | Apologizing | [E11_apologizing.md](expressions/E11_apologizing.md) | `images/jupanbot/E11_apologizing.png` | genspark-v2 |
| E12 | 업무 | 응원 | Cheering | [E12_cheering.md](expressions/E12_cheering.md) | `images/jupanbot/E12_cheering.png` | genspark-v2 |
| E13 | 미묘한 감정 | 기본(중립) | Neutral | [E13_neutral.md](expressions/E13_neutral.md) | `images/jupanbot/E13_neutral.png` | gpt2-v2 |
| E14 | 미묘한 감정 | 머쓱함 | Sheepish | [E14_sheepish.md](expressions/E14_sheepish.md) | `images/jupanbot/E14_sheepish.png` | genspark-v2 |
| E15 | 미묘한 감정 | 당황 | Flustered | [E15_flustered.md](expressions/E15_flustered.md) | `images/jupanbot/E15_flustered.png` | gpt2-v2 |
| E16 | 미묘한 감정 | 뿌듯함 | Proud | [E16_proud.md](expressions/E16_proud.md) | `images/jupanbot/E16_proud.png` | gpt2-v2 |
| E17 | 미묘한 감정 | 졸림 | Sleepy | [E17_sleepy.md](expressions/E17_sleepy.md) | `images/jupanbot/E17_sleepy.png` | genspark-v2 |
| E18 | 미묘한 감정 | 삐짐 | Sulking | [E18_sulking.md](expressions/E18_sulking.md) | `images/jupanbot/E18_sulking.png` | genspark-v2 |
| E19 | 코믹 과장 | 반짝눈(감동·기대) | Sparkling Eyes | [E19_sparkle_eyes.md](expressions/E19_sparkle_eyes.md) | `images/jupanbot/E19_sparkle_eyes.png` | genspark-v2 |
| E20 | 코믹 과장 | 식은땀 | Big Sweat Drop | [E20_sweat_drop.md](expressions/E20_sweat_drop.md) | `images/jupanbot/E20_sweat_drop.png` | genspark-v2 |
| E21 | 코믹 과장 | 폭포 눈물 | Waterfall Tears | [E21_waterfall_tears.md](expressions/E21_waterfall_tears.md) | `images/jupanbot/E21_waterfall_tears.png` | genspark-v2 |
| E22 | 코믹 과장 | 뿔남 | Puffed Angry | [E22_puffed_angry.md](expressions/E22_puffed_angry.md) | `images/jupanbot/E22_puffed_angry.png` | genspark-v2 |
| E23 | 코믹 과장 | 멍 | Blank Dot Eyes | [E23_blank_dot_eyes.md](expressions/E23_blank_dot_eyes.md) | `images/jupanbot/E23_blank_dot_eyes.png` | genspark-v2 |
| E24 | 코믹 과장 | 충격 | Shock | [E24_shock.md](expressions/E24_shock.md) | `images/jupanbot/E24_shock.png` | gpt2-v2 |
