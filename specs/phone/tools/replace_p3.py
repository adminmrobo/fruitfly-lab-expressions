"""새로 받은 P3 단독 그림을 3컷 폰 배경의 아래 큰 칸에 끼워 넣는다.

사용: python3 specs/phone/tools/replace_p3.py <3컷 PNG> <새 P3 PNG>
- 3컷 그림에서 가로 흰 거터(밝은 행이 이어지는 띠)를 찾아 아래 큰 칸의 위치를 잡는다.
- 새 P3를 칸 비율에 맞게 가운데 기준으로 잘라(cover) 칸 크기로 줄여 붙인다.
- 3컷 PNG와 PH1_p3_… 컷 파일을 함께 덮어쓴다(원본은 .bak.png로 남김).
"""
import sys, os, shutil
import numpy as np
from PIL import Image

def bottom_panel_box(im):
    a = np.asarray(im.convert("L"), dtype=float)
    h, w = a.shape
    bright = (a > 235).mean(1) > 0.97          # 거의 흰 행
    # 위에서 40%~80% 사이에서 가장 아래쪽 흰 띠의 끝 = 아래 칸 시작
    top = None
    for y in range(int(h * 0.80), int(h * 0.40), -1):
        if bright[y]:
            top = y + 1
            break
    if top is None:
        raise SystemExit("가로 거터를 찾지 못했습니다")
    while top < h and bright[top]:
        top += 1
    bot = h - 1
    while bot > top and bright[bot]:
        bot -= 1
    cols = (a[top:bot] > 235).mean(0) > 0.97
    left = 0
    while left < w and cols[left]:
        left += 1
    right = w - 1
    while right > left and cols[right]:
        right -= 1
    # 칸 테두리(어두운 선)는 남기고 안쪽만 바꾼다
    def dark_row(y): return a[y, left:right + 1].mean() < 120
    def dark_col(x): return a[top:bot + 1, x].mean() < 120
    while top < bot and dark_row(top): top += 1
    while bot > top and dark_row(bot): bot -= 1
    while left < right and dark_col(left): left += 1
    while right > left and dark_col(right): right -= 1
    return left, top, right + 1, bot + 1

def cover(img, size):
    tw, th = size
    s = max(tw / img.width, th / img.height)
    r = img.resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)
    x, y = (r.width - tw) // 2, (r.height - th) // 2
    return r.crop((x, y, x + tw, y + th))

if __name__ == "__main__":
    page, newp3 = sys.argv[1], sys.argv[2]
    im = Image.open(page).convert("RGB")
    box = bottom_panel_box(im)
    shutil.copy(page, page[:-4] + ".bak.png")
    p3 = cover(Image.open(newp3).convert("RGB"), (box[2] - box[0], box[3] - box[1]))
    im.paste(p3, box[:2])
    im.save(page)
    cut = page.replace("PH1_selfie3_", "PH1_p3_")
    if os.path.exists(cut):
        shutil.copy(cut, cut[:-4] + ".bak.png")
        p3.save(cut)
    print("아래 칸", box, "→ 교체 완료:", page, cut)
