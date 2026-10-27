# 박사 표정 세트 — 인덱스

- 총 **24개 표정** (원본 2개 → 약 12배), 4개 카테고리 × 6개, 모든 캐릭터 공통 ID 체계 E01~E24
- 명세 ↔ 이미지 1:1 규칙: `specs/doctor/expressions/{ID}_{slug}.md` ↔ `images/doctor/{ID}_{slug}.png`
- 공통 아이덴티티: [`00_character_core.md`](00_character_core.md)
- 원본 참조 이미지: `refs/original/doctor_sheet.png`, `refs/original/keyart_rivals.png`
- 생성 순서: **E13(기준)** → 기본 감정 → 업무 → 미묘한 감정 → 코믹 과장

| ID | 카테고리 | 표정 | EN | 원본 대응 | 명세 | 이미지 | 상태 |
|---|---|---|---|---|---|---|---|
| E01 | 기본 감정 | 기쁨 | Joy | ● | [E01_joy.md](expressions/E01_joy.md) | `images/doctor/E01_joy.png` | generated |
| E02 | 기본 감정 | 슬픔 | Sadness | — | [E02_sadness.md](expressions/E02_sadness.md) | `images/doctor/E02_sadness.png` | generated |
| E03 | 기본 감정 | 분노 | Anger | — | [E03_anger.md](expressions/E03_anger.md) | `images/doctor/E03_anger.png` | generated |
| E04 | 기본 감정 | 놀람 | Surprise | — | [E04_surprise.md](expressions/E04_surprise.md) | `images/doctor/E04_surprise.png` | generated |
| E05 | 기본 감정 | 두려움 | Fear | — | [E05_fear.md](expressions/E05_fear.md) | `images/doctor/E05_fear.png` | generated |
| E06 | 기본 감정 | 혐오 | Disgust | — | [E06_disgust.md](expressions/E06_disgust.md) | `images/doctor/E06_disgust.png` | generated |
| E07 | 업무 | 설명 | Explaining | — | [E07_explaining.md](expressions/E07_explaining.md) | `images/doctor/E07_explaining.png` | generated |
| E08 | 업무 | 안내 | Guiding | — | [E08_guiding.md](expressions/E08_guiding.md) | `images/doctor/E08_guiding.png` | generated |
| E09 | 업무 | 생각 | Thinking | — | [E09_thinking.md](expressions/E09_thinking.md) | `images/doctor/E09_thinking.png` | generated |
| E10 | 업무 | 확인 | Confirming | — | [E10_confirming.md](expressions/E10_confirming.md) | `images/doctor/E10_confirming.png` | generated |
| E11 | 업무 | 사과 | Apologizing | — | [E11_apologizing.md](expressions/E11_apologizing.md) | `images/doctor/E11_apologizing.png` | generated |
| E12 | 업무 | 응원 | Cheering | — | [E12_cheering.md](expressions/E12_cheering.md) | `images/doctor/E12_cheering.png` | generated |
| E13 | 미묘한 감정 | 기본(중립) | Neutral | — | [E13_neutral.md](expressions/E13_neutral.md) | `images/doctor/E13_neutral.png` | generated |
| E14 | 미묘한 감정 | 머쓱함 | Sheepish | — | [E14_sheepish.md](expressions/E14_sheepish.md) | `images/doctor/E14_sheepish.png` | generated |
| E15 | 미묘한 감정 | 당황 | Flustered | — | [E15_flustered.md](expressions/E15_flustered.md) | `images/doctor/E15_flustered.png` | generated |
| E16 | 미묘한 감정 | 뿌듯함 | Proud | ● | [E16_proud.md](expressions/E16_proud.md) | `images/doctor/E16_proud.png` | generated |
| E17 | 미묘한 감정 | 졸림 | Sleepy | — | [E17_sleepy.md](expressions/E17_sleepy.md) | `images/doctor/E17_sleepy.png` | generated |
| E18 | 미묘한 감정 | 삐짐 | Sulking | — | [E18_sulking.md](expressions/E18_sulking.md) | `images/doctor/E18_sulking.png` | generated |
| E19 | 코믹 과장 | 반짝눈(감동·기대) | Sparkling Eyes | — | [E19_sparkle_eyes.md](expressions/E19_sparkle_eyes.md) | `images/doctor/E19_sparkle_eyes.png` | generated |
| E20 | 코믹 과장 | 식은땀 | Big Sweat Drop | — | [E20_sweat_drop.md](expressions/E20_sweat_drop.md) | `images/doctor/E20_sweat_drop.png` | generated |
| E21 | 코믹 과장 | 울먹(폭포 눈물) | Waterfall Tears | — | [E21_waterfall_tears.md](expressions/E21_waterfall_tears.md) | `images/doctor/E21_waterfall_tears.png` | generated |
| E22 | 코믹 과장 | 뿔남 | Comic Anger | — | [E22_puffed_angry.md](expressions/E22_puffed_angry.md) | `images/doctor/E22_puffed_angry.png` | generated |
| E23 | 코믹 과장 | 멍(점 눈) | Blank Dot Eyes | — | [E23_blank_dot_eyes.md](expressions/E23_blank_dot_eyes.md) | `images/doctor/E23_blank_dot_eyes.png` | generated |
| E24 | 코믹 과장 | 충격 | Shock | — | [E24_shock.md](expressions/E24_shock.md) | `images/doctor/E24_shock.png` | generated |

● = 원본 시트에 이미 있는 표정. 이 표정은 원본 칸을 1순위 레퍼런스로 씁니다.

## 사용법
1. 표정 명세의 **7절 완성형 프롬프트**를 그대로 복사합니다.
2. 원본 참조 이미지(+ 승인된 `E13_neutral.png`)를 레퍼런스로 함께 넣어 생성합니다.
3. 결과물은 명세의 `image_file` 경로에 저장하고 `image_status`를 업데이트합니다.
