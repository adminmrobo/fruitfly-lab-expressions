"""공장(제조업 특화) 복장·동작 벡터 v1.0 — factory.json · PROMPTS.md 생성. 실행: python3 specs/factory/make_factory.py"""
import json, pathlib
R = pathlib.Path(__file__).resolve().parents[2]
M = json.loads((R / "specs/motions/motions.json").read_text(encoding="utf-8"))
CH = M["characters"]
WHO = ["doctor", "haru", "fruitfly", "jupanbot", "sia", "moa"]
KO = {"doctor": "박사", "haru": "하루", "fruitfly": "초파리", "jupanbot": "주판봇", "sia": "시아", "moa": "모아"}
TAIL = ("16-bit RPG pixel art sprite sheet, crisp pixels, no anti-aliasing blur, bold dark outline (#1d1a22), 2-3 step cel shading with a tiny highlight, "
        "full body, same character scale and same ground line in every frame, every frame inside its own equal grid cell with empty margin, nothing crossing cell borders, "
        "flat solid plain medium gray background (#9e9e9e) with no gradient, no floor, no shadow, no scenery, no text, no letters, no numbers, no labels, no logo, no watermark, "
        "no company names on clothing, no extra visual effects beyond what is described, no motion lines, no speed lines.")
NEG = ("blurry, smooth vector art, 3D render, photorealistic, anti-aliased painting, inconsistent character, off-model, mirrored character, text, letters, numbers, watermark, labels, "
       "brand logos, company names, multiple different characters, different face in each cell, changed eye color, changed hair color, missing limbs, extra limbs, bare hands near machines, loose long hair near machines")

# ── 복장 U00~U07 ──
WEAR = [
 ("U00", "canon", "정본 (연구실 복장)", "Canon lab outfit", "연구실·설명 장면 기본", None),
 ("U01", "shopfloor", "현장 근무복", "Shop-floor workwear", "③ 배터리 생산 라인·일반 현장",
  "navy blue work jacket and work trousers with silver reflective stripes on the arms and legs, a bright yellow hard hat with a chin strap, clear safety glasses, gray work gloves, black safety shoes with toe caps"),
 ("U02", "cleanroom", "클린룸 방진복", "Cleanroom suit", "④ 태양광 셀·반도체·드라이룸",
  "a white full-body cleanroom bunny suit with an attached hood that hides all hair, a white face mask, clear goggles, light blue nitrile gloves, white shoe covers; only the eyes and a little of the face are visible"),
 ("U03", "heat", "고온 공정 보호구", "Heat-protection gear", "소성로·킬른(이웃 시멘트 공장)·용해",
  "a silver aluminized heat-resistant jacket and trousers, a hard hat with a flip-up clear face shield, thick tan heat-resistant gauntlet gloves, heavy safety boots"),
 ("U04", "maintenance", "설비 정비복", "Maintenance coveralls", "설비 정비·로봇 티칭",
  "gray one-piece coveralls with many pockets, a tool belt holding a wrench and a screwdriver, a dark gray work cap, knee pads, work gloves, safety shoes"),
 ("U05", "inspection", "품질 검사복", "Quality-inspection wear", "시제품 테스트 랩실·출하 검사",
  "a short white inspection coat, a light blue hairnet cap that covers all hair, clear safety glasses, purple nitrile gloves, white anti-static shoes"),
 ("U06", "supervisor", "생산 관리자", "Production supervisor", "교대 인계·관리도 회의·판정 승인",
  "a white hard hat, a fluorescent orange high-visibility safety vest over a light blue collared shirt, dark trousers, a small handheld radio clipped at the chest, safety shoes"),
 ("U07", "foodhygiene", "식품 위생복", "Food-hygiene wear", "생선 통조림 라인·식품 공장",
  "a white hygiene cap that fully covers the hair, a white long-sleeved smock, a light blue waterproof apron, a white face mask, white rubber boots, light blue rubber gloves"),
]
# ── 동작 P01~P16 (키 포즈 한 장씩, 기본 복장) ──
POSE = [
 ("P01", "tbm", "작업 전 안전 구호 (TBM)", "Toolbox-meeting safety call", "U01", "standing straight, right fist raised beside the face, mouth open as if calling out a safety chant, left hand on the hard hat brim"),
 ("P02", "point_call", "지적 확인", "Point-and-call check", "U01", "pointing firmly forward with the right index finger at an imaginary gauge at eye level, left hand at the waist, eyes focused"),
 ("P03", "caliper", "캘리퍼스 계측", "Measuring with calipers", "U05", "holding a pair of silver vernier calipers with both hands, measuring a small rectangular part, eyes looking closely at the calipers"),
 ("P04", "magnifier", "확대경 외관 검사", "Visual inspection with magnifier", "U05", "leaning forward and holding a round magnifying glass over a small flat part held in the other hand"),
 ("P05", "mes_tablet", "태블릿 생산 기록 입력", "Entering production data on tablet", "U06", "holding a tablet in the left hand and tapping its blank screen with the right index finger, the screen shows only simple colored bars and no text"),
 ("P06", "estop", "비상정지 버튼 누르기", "Pressing the emergency stop", "U01", "pressing a large red mushroom-shaped emergency stop button on a small yellow box with the palm, other arm held out to the side, alert expression"),
 ("P07", "wrench", "렌치 설비 정비", "Wrench maintenance", "U04", "kneeling on one knee and turning a big wrench on a bolt of a small gray machine block with both hands"),
 ("P08", "carry_box", "부품 상자 운반", "Carrying a parts box", "U01", "carrying a plain cardboard parts box with both arms in front of the chest, walking forward, knees slightly bent"),
 ("P09", "handover", "교대 인계", "Shift handover", "U01", "holding out a clipboard with blank paper forward with both hands as if handing it to the next shift, slight bow of the head"),
 ("P10", "spc_chart", "관리도 가리키기", "Pointing at a control chart", "U06", "pointing with a short pointer stick at a small whiteboard that shows a simple zigzag line between two dashed horizontal lines, no numbers"),
 ("P11", "teach_pendant", "로봇 티칭 펜던트 조작", "Operating a robot teach pendant", "U04", "holding a chunky gray teach pendant controller with both hands, thumbs on its buttons, looking up as if watching a robot arm move"),
 ("P12", "air_shower", "에어샤워 통과", "Air-shower entry", "U02", "standing with both arms raised slightly and spread, turning the body as if being blown by an air shower, a few tiny white air puff marks around the suit"),
 ("P13", "ir_thermometer", "적외선 온도 측정", "Infrared temperature check", "U03", "aiming a handheld pistol-shaped infrared thermometer forward with the right hand, face shield down, left hand raised to shield from heat"),
 ("P14", "reject_tag", "불량 빨간 태그 붙이기", "Attaching a red reject tag", "U05", "tying a blank red tag with a string onto a small part held in the other hand, serious face"),
 ("P15", "approve", "합격 승인", "Approval sign-off", "U06", "giving a confident thumbs-up with the right hand while holding a clipboard with a big green check mark in the left hand, smiling"),
 ("P16", "hand_hygiene", "손 위생 점검", "Hand-hygiene check", "U07", "rubbing both gloved hands together in front of the chest as if sanitizing, standing straight"),
]
# ── 캐릭터별 규칙 ──
RULES = {
 "doctor": {"keep": "청록 안경, 흰 줄 있는 검은 뾰족 머리, 뒤 작은 포니테일, 2.5등신",
   "rules": ["흰 머리 줄은 모든 칸에서 같은 쪽. 좌우 반전 금지.", "안전모·후드 아래로 흰 머리 줄이 조금 보이게.", "U05·U06에서는 안경 위에 보안경을 겹쳐 쓰지 않고 안경을 보안경 겸용으로 그린다."],
   "adapt_en": "He keeps his thin teal rectangular glasses (they double as safety glasses) and a bit of the white hair streak shows under any hat or hood."},
 "haru": {"keep": "분홍 + 남색 줄 투톤, 파란 눈, 바보털, 2.5등신(박사보다 조금 작게)",
   "rules": ["라인(U01·U03·U04·U06)에서는 긴 머리를 반드시 묶는다 — 헤어 벡터 H17 풀 번(남색 곱창).", "U02·U05·U07은 머리를 모두 후드·캡 안에 넣는다. 앞머리 끝 남색 줄만 살짝.", "번 2개는 U00에서만."],
   "adapt_en": "Her long pink hair with the navy streak is tied up into a single full bun with a navy scrunchie (safety rule near machines); under hoods and caps all hair is tucked in and only a hint of the navy streak in the bangs shows."},
 "fruitfly": {"keep": "검은 몸, 큰 빨간 겹눈, 금줄 파란 헬멧과 분홍·파랑 케이블, 투명 날개, 팔 2 + 다리 4, 박사의 40% 크기",
   "rules": ["팔다리 6개가 모든 칸에서 보여야 한다.", "U01·U03·U06의 안전모는 파란 헬멧 위에 겹쳐 쓰지 않는다 — 파란 헬멧에 노란 반사띠를 두르는 것으로 대신한다.", "U02 방진복은 날개를 감싸는 투명 날개 덮개가 달린 맞춤 방진복. 날개 모양은 비쳐 보인다.", "작은 몸에 맞는 작은 소품(작은 상자·작은 캘리퍼스)."],
   "adapt_en": "Six limbs (two arms, four legs) stay visible. Instead of a separate hard hat, his blue helmet gets a yellow reflective band; the cleanroom suit has clear wing covers so the wing shapes still show; all props are sized to his small body."},
 "jupanbot": {"keep": "베이지 CRT 모니터 몸, 짙은 초록 화면 얼굴과 민트 픽셀 눈·입, 붉은 갈색 주판알 안테나, 회색 마디 팔, 무한궤도 2개, 박사의 70% 크기",
   "rules": ["로봇이라 옷 대신 '장착물'로 그린다: 안전모는 모니터 위, 조끼는 몸통 앞판, 방진복은 투명 비닐 커버.", "주판은 동작 칸에서 궤도 옆 고리에 걸어 두고, U00·P15에서만 손에 든다.", "금지: 둥근 흰 머리, 노란 눈, 공 모양 안테나, 가슴 불빛, 떠 있기, 금화.", "안테나 주판알은 모든 칸에서 보이게(후드·캡에 구멍)."],
   "adapt_en": "He is a robot, so the outfit is worn as attachments: the hard hat sits on top of the monitor with a hole for the antenna bead, vests and aprons hang on the front panel, the cleanroom suit is a clear plastic cover; the wooden abacus hangs from a hook beside the treads unless he is holding it."},
 "sia": {"keep": "흑발 옆으로 넘긴 앞머리, 회색 눈, 은 귀걸이, 머리띠 없음, 2.5등신",
   "rules": ["라인에서는 긴 흑발을 낮게 묶는다 — 헤어 벡터 H02 로우 포니테일(숯색 끈), 후드·캡 안에서는 모두 넣는다.", "메이드 원피스는 공장 복장으로 완전히 바꾼다. 회색 큰 리본만 U00·U06의 셔츠 깃에 작게 남긴다.", "앞머리 가르마는 모든 칸에서 같은 쪽.", "흰 프릴·메이드 머리띠 금지."],
   "adapt_en": "Her long jet-black hair is tied in a low ponytail with a charcoal tie (or fully tucked under hoods and caps); the maid dress is fully replaced by the workwear; only a small gray bow may remain at a shirt collar; no white frills, no headband."},
 "moa": {"keep": "애쉬 베이지 머리, 가지런한 앞머리, 호박 눈, 가장 작은 사람 캐릭터",
   "rules": ["공장 복장(U01~U07)에서는 흰 프릴 머리띠를 벗는다(안전). 머리는 헤어 벡터 H02 로우 포니테일(분홍 곱창), 후드·캡 안에서는 모두 넣는다.", "체크 리본 타이는 U06 셔츠 깃에만 작게.", "왼쪽 흰 리본도 공장 복장에서는 없음."],
   "adapt_en": "In factory outfits she takes off the white frilled headband and ribbon (safety); her ash-beige hair is tied in a low ponytail with a pink scrunchie or fully tucked under hoods and caps; her red-and-navy plaid bow tie may show only at the supervisor shirt collar."},
}
FACE = {
 "doctor": "chibi scientist (big head, about 2.5 heads tall), thin teal rectangular glasses, spiky black hair with one white streak, small ponytail at the back",
 "haru": "chibi girl researcher (big head, about 2.5 heads tall, slightly shorter than the doctor), pink hair with a navy streak, a small ahoge, big blue eyes, light peach skin",
 "fruitfly": "anthropomorphic fruit fly researcher, small (about 40% of the doctor's height), black body, big red compound eyes, blue helmet with a gold stripe and pink and blue cables at the back, transparent wings, two arms and four legs, black gloves",
 "jupanbot": "boxy beige retro CRT-monitor robot (about 70% of the doctor's height), dark green screen face with mint pixel eyes and mouth, short antenna topped with a red-brown abacus bead, gray segmented arms, two small tank treads",
 "sia": "chibi girl intern (big head, about 2.5 heads tall, slightly shorter than the assistant), jet-black hair with side-swept bangs, gray eyes, small silver earrings",
 "moa": "chibi girl intern (big head, about 2.5 heads tall, the smallest of the human characters), ash-beige hair with neat straight bangs, amber-brown eyes"}
def look(w, canon=False):
    return CH[w]["look_en"] if canon else FACE[w]
def sheet_wear(w):
    cells = "; ".join(f"({i+1}) {('the canon outfit exactly as in the reference: ' + look(w)) if u[5] is None else u[5]}" for i, u in enumerate(WEAR))
    return (f"Pixel art outfit reference sheet of ONE original character: {look(w)}. {RULES[w]['adapt_en']} "
            f"Grid 4 columns x 2 rows, aspect ratio 16:9, the same character standing in the same calm neutral pose and same 3/4 front view in all 8 cells; only the outfit changes. "
            f"Cells from left to right, top row then bottom row: {cells}. Same face, same proportions, same eye color and same hair color in every cell. {CH[w]['rule']} {TAIL}")
def sheet_pose(w, part):
    ps = POSE[:8] if part == 1 else POSE[8:]
    W = {u[0]: u for u in WEAR}
    used = []
    for p in ps:
        if p[4] not in used: used.append(p[4])
    legend = " ".join(f"Outfit {u}: {W[u][5]}." for u in used)
    cells = "; ".join(f"({i+1}) outfit {p[4]}, {p[5]}" for i, p in enumerate(ps))
    return (f"Pixel art pose sheet of ONE original character: {look(w)}. {RULES[w]['adapt_en']} {legend} "
            f"Grid 4 columns x 2 rows, aspect ratio 16:9, one key pose per cell, full body, 3/4 view. "
            f"Cells from left to right, top row then bottom row: {cells}. Same face, same proportions, same eye color and same hair color in every cell; only the pose and the workwear change as listed. {CH[w]['rule']} {TAIL}")
J = {"vector": "factory", "version": "1.0", "date": "2026-11-14", "applies_to": WHO,
     "note": "공장(제조업 특화) 복장·동작 벡터. 복장 U00~U07 × 동작 P01~P16(키 포즈). 미공개 X1~X3는 C9 예고 규칙에 따라 제외.",
     "image_format": "셀별로 잘라 투명 PNG 512×768(전신, 발 기준선 공통). wear = 3/4 앞 서기, pose = 키 포즈 1장",
     "wear": [{"id": u[0], "slug": u[1], "ko": u[2], "en": u[3], "use": u[4], "outfit_en": u[5] or "canon"} for u in WEAR],
     "poses": [{"id": p[0], "slug": p[1], "ko": p[2], "en": p[3], "wear": p[4], "pose_en": p[5]} for p in POSE],
     "characters": {w: {"ko": KO[w], "keep": RULES[w]["keep"], "rules": RULES[w]["rules"], "adapt_en": RULES[w]["adapt_en"]} for w in WHO},
     "files": {}, "sheets": []}
for w in WHO:
    J["files"][w] = {"wear": {u[0]: {"file": f"images/factory/{w}/{u[0]}_{u[1]}.png", "status": "planned"} for u in WEAR},
                     "pose": {p[0]: {"file": f"images/factory/{w}/{p[0]}_{p[1]}.png", "status": "planned"} for p in POSE}}
    refs = [f"images/{w}/E13_neutral.png", "refs/original/"]
    J["sheets"] += [{"sheet": f"{w}_factory_wear", "who": w, "ids": [u[0] for u in WEAR], "file": f"images/_sheets/factory/{w}_factory_wear.png", "prompt_en": sheet_wear(w), "negative_en": NEG, "refs": refs},
                    {"sheet": f"{w}_factory_pose_1", "who": w, "ids": [p[0] for p in POSE[:8]], "file": f"images/_sheets/factory/{w}_factory_pose_1.png", "prompt_en": sheet_pose(w, 1), "negative_en": NEG, "refs": refs},
                    {"sheet": f"{w}_factory_pose_2", "who": w, "ids": [p[0] for p in POSE[8:]], "file": f"images/_sheets/factory/{w}_factory_pose_2.png", "prompt_en": sheet_pose(w, 2), "negative_en": NEG, "refs": refs}]
(R / "specs/factory/factory.json").write_text(json.dumps(J, ensure_ascii=False, indent=1), encoding="utf-8")
# PROMPTS.md
L = ["# 공장(제조업 특화) 벡터 · 생성 프롬프트 (Genspark)", "",
     "캐릭터마다 시트 3장(복장 1 · 동작 2), 여섯 캐릭터 모두 18장. 그리드 4열 × 2행, 16:9.",
     "참고 이미지로 `images/{캐릭터}/E13_neutral.png`와 `refs/original/`의 해당 캐릭터 원본 시트를 함께 넣습니다. 동작 시트를 만들 때는 먼저 받은 복장 시트도 함께 넣으면 복장이 맞춰집니다.",
     "받은 시트는 `images/_sheets/factory/{시트}.png`로 저장하고, 칸별로 잘라 `images/factory/{캐릭터}/U##_{slug}.png`·`P##_{slug}.png`(투명)로 둡니다. 그림 안에 글자가 들어가면 다시 뽑습니다.", ""]
for w in WHO:
    L += [f"## {KO[w]} (`{w}`)", "", f"유지할 것: {RULES[w]['keep']}", ""] + [f"- {r}" for r in RULES[w]["rules"]] + [""]
    for s in [x for x in J["sheets"] if x["who"] == w]:
        names = " · ".join(f"{i} {next(t[2] for t in WEAR + [(p[0], p[1], p[2]) for p in POSE] if t[0] == i)}" for i in s["ids"])
        L += [f"### `{s['sheet']}` — {names}", "", "```", s["prompt_en"], "```", "", "Negative:", "```", s["negative_en"], "```", ""]
(R / "specs/factory/PROMPTS.md").write_text("\n".join(L), encoding="utf-8")
print("sheets", len(J["sheets"]), "wear", len(WEAR), "poses", len(POSE))
