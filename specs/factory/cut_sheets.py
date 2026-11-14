"""공장 벡터 시트(4×2) → 칸별 투명 PNG. 실행: python3 specs/factory/cut_sheets.py [시트 폴더]
회색 배경을 가장자리에서 이어진 영역만 투명으로 바꾸고, 512×768 상자에 발 기준선(아래 24px)을 맞춰 넣는다."""
import json, sys, pathlib
import numpy as np
from PIL import Image
from scipy import ndimage
R = pathlib.Path(__file__).resolve().parents[2]
J = json.loads((R / "specs/factory/factory.json").read_text(encoding="utf-8"))
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else R / "images/_sheets/factory"
OW, OH, FOOT = 512, 768, 24
def cut(cell):
    a = np.asarray(cell.convert("RGB")).astype(int)
    h, w, _ = a.shape
    k = 10  # 칸 테두리 선을 피해 안쪽 고리에서 배경색과 씨앗을 잡는다
    ring = np.concatenate([a[k], a[-k-1], a[:, k], a[:, -k-1]])
    bg = np.median(ring, axis=0)
    d = np.abs(a - bg).max(axis=2)
    near = d < 26
    near[:k, :] = near[-k:, :] = True; near[:, :k] = near[:, -k:] = True
    lab, n = ndimage.label(near)
    edge = set(np.unique(np.concatenate([lab[k], lab[-k-1], lab[:, k], lab[:, -k-1]]))) - {0}
    bgmask = np.isin(lab, list(edge))
    # 칸 테두리 선(어두운 회색 가는 선)도 가장자리 4px 안이면 지움
    bgmask[:4, :] = bgmask[-4:, :] = True; bgmask[:, :4] = bgmask[:, -4:] = True
    fg = ~bgmask
    fg = ndimage.binary_opening(fg, iterations=1)
    lab2, n2 = ndimage.label(fg)
    if n2:
        sizes = ndimage.sum(fg, lab2, range(1, n2 + 1)); keep = [i + 1 for i, s in enumerate(sizes) if s > 120]
        fg = np.isin(lab2, keep)
    rgba = np.dstack([a, (fg * 255)]).astype(np.uint8)
    im = Image.fromarray(rgba, "RGBA"); return im.crop(im.getbbox())
def place(im, s):
    im = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.NEAREST)
    out = Image.new("RGBA", (OW, OH), (0, 0, 0, 0)); out.paste(im, ((OW - im.width) // 2, OH - FOOT - im.height), im)
    return out
log = []
for sh in J["sheets"]:
    f = SRC / pathlib.Path(sh["file"]).name
    if not f.exists():
        log.append((sh["sheet"], "missing")); continue
    S = Image.open(f); W, H = S.size; cw, ch = W / 4, H / 2; m = 3
    kind = "wear" if sh["sheet"].endswith("_wear") else "pose"
    cuts = []
    for k, i in enumerate(sh["ids"]):
        c, r = k % 4, k // 4
        cuts.append(cut(S.crop((round(c * cw) + m, round(r * ch) + m, round((c + 1) * cw) - m, round((r + 1) * ch) - m))))
    # 시트 하나에 배율 하나 — 무릎 꿇기 같은 낮은 자세가 커지지 않게
    sc = min(min((OW - 16) / x.width, (OH - FOOT - 8) / x.height) for x in cuts)
    sc = min(sc, 2.0)
    for k, i in enumerate(sh["ids"]):
        out = place(cuts[k], sc)
        rec = J["files"][sh["who"]][kind][i]; p = R / rec["file"]; p.parent.mkdir(parents=True, exist_ok=True); out.save(p, optimize=True)
        rec["status"] = "generated"
    dst = R / sh["file"]; dst.parent.mkdir(parents=True, exist_ok=True)
    if f.resolve() != dst.resolve(): S.save(dst, optimize=True)
    log.append((sh["sheet"], "ok"))
(R / "specs/factory/factory.json").write_text(json.dumps(J, ensure_ascii=False, indent=1), encoding="utf-8")
print(log)
