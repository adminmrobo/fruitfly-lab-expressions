"""lab3d 모델을 여러 각도로 찍어 이미지 벡터를 만든다.

    python3 chars3d/tools/render_views.py            # 전체 (8방향 × 2높이 + 포즈 + 표정 + 시트)
    python3 chars3d/tools/render_views.py --preview  # 확인용 한 장 (/tmp/lab3d_preview.png)

필요: playwright(크로미움), Pillow. three.js는 CDN에서 받고,
--three 경로를 주면 로컬 three.module.js를 대신 쓴다(오프라인용).
결과: images/3d/{key}/... (WebP 무손실), images/3d/_sheets/*.png, specs/3d/views.json
"""
import argparse, base64, functools, http.server, io, json, os, socketserver, threading
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
CDN = 'https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js'

CHARS = [  # key, variant, 기본 포즈 목록
    ('doctor', None), ('haru', None), ('fruitfly', None), ('jupanbot', None),
    ('sia', None), ('moa', 'maid'), ('moa', 'suit'), ('x1', None), ('x2', None), ('x3', None),
]
POSES = ['idle', 'wave', 'explain', 'think', 'cheer', 'hold', 'referee', 'walk']
EXPRS = ['E13', 'E01', 'E04']
DIRS = [(f'd{i}', i * 45) for i in range(8)]
ELEVS = [('e08', 8), ('e32', 32)]


def serve():
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=ROOT)
    h.log_message = lambda *a: None
    s = socketserver.TCPServer(('127.0.0.1', 0), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s.server_address[1]


def img(data_url):
    return Image.open(io.BytesIO(base64.b64decode(data_url.split(',', 1)[1]))).convert('RGBA')


def slug(key, variant):
    return key if not variant or variant == 'maid' else f'{key}_{variant}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--preview', action='store_true')
    ap.add_argument('--three', default=os.environ.get('THREE_MODULE'))
    a = ap.parse_args()
    port = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(args=['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
        pg = b.new_page(viewport={'width': 600, 'height': 600})
        if a.three:
            pg.route(CDN, lambda r: r.fulfill(path=a.three, content_type='text/javascript'))
        pg.on('console', lambda m: m.type == 'error' and print('console:', m.text))
        pg.goto(f'http://127.0.0.1:{port}/chars3d/tools/render.html')
        pg.wait_for_function('window.ready === true', timeout=60000)
        shot = lambda key, **kw: img(pg.evaluate('([k,o]) => window.renderView(k,o)', [key, kw]))

        if a.preview:
            cols = [0, 45, 90, 180]
            sheet = Image.new('RGBA', (256 * len(cols), 256 * len(CHARS)), (232, 230, 226, 255))
            for r, (k, v) in enumerate(CHARS):
                for c, yaw in enumerate(cols):
                    im = shot(k, variant=v, yaw=yaw, elev=8).resize((256, 256), Image.LANCZOS)
                    sheet.alpha_composite(im, (c * 256, r * 256))
            sheet.save('/tmp/lab3d_preview.png'); print('preview -> /tmp/lab3d_preview.png'); return

        out = os.path.join(ROOT, 'images', '3d'); os.makedirs(os.path.join(out, '_sheets'), exist_ok=True)
        rows = []
        def save(im, rel, **meta):
            path = os.path.join(out, rel); os.makedirs(os.path.dirname(path), exist_ok=True)
            im.save(path, 'WEBP', lossless=True, quality=100, method=6)
            rows.append({'file': f'images/3d/{rel}', **meta})
            return im
        for k, v in CHARS:
            s = slug(k, v); turn = {}
            for eid, deg in ELEVS:
                for did, yaw in DIRS:
                    turn[(eid, did)] = save(shot(k, variant=v, yaw=yaw, elev=deg), f'{s}/turn_{eid}_{did}.webp',
                                            key=k, variant=v or '', kind='turn', pose='idle', expr='E13', dir=did, yaw=yaw, elev=deg)
            poses = {}
            for po in POSES:
                t = {'walk': .26, 'wave': .2, 'cheer': .3}.get(po, 0)
                poses[po] = save(shot(k, variant=v, yaw=25, elev=8, pose=po, t=t), f'{s}/pose_{po}.webp',
                                 key=k, variant=v or '', kind='pose', pose=po, expr='E13', dir='d0+25', yaw=25, elev=8)
            exprs = {}
            for ex in EXPRS:
                exprs[ex] = save(shot(k, variant=v, yaw=0, elev=8, expr=ex, frame=.62), f'{s}/face_{ex}.webp',
                                 key=k, variant=v or '', kind='face', pose='idle', expr=ex, dir='d0', yaw=0, elev=8, frame=.62)
            # 캐릭터 설정 시트: 1행 눈높이 8방향, 2행 공장 시점 8방향, 3행 포즈 8종 (+ 표정은 별도)
            C = 192; sheet = Image.new('RGBA', (C * 8, C * 3 + 24), (232, 230, 226, 255))
            for r, eid in enumerate(['e08', 'e32']):
                for c, (did, _) in enumerate(DIRS):
                    sheet.alpha_composite(turn[(eid, did)].resize((C, C), Image.LANCZOS), (c * C, r * C))
            for c, po in enumerate(POSES):
                sheet.alpha_composite(poses[po].resize((C, C), Image.LANCZOS), (c * C, 2 * C + 24))
            ImageDraw.Draw(sheet).line([(0, 2 * C + 12), (C * 8, 2 * C + 12)], fill=(200, 196, 190, 255), width=2)
            sheet.convert('RGB').save(os.path.join(out, '_sheets', f'{s}_3d_sheet.png'), optimize=True)
            print('done', s)
        # 전원 라인업 (눈높이·공장 시점, 오른앞 45°)
        for eid, deg in ELEVS:
            C = 256; order = [c for c in CHARS]
            sheet = Image.new('RGBA', (C * len(order), C), (232, 230, 226, 255))
            for i, (k, v) in enumerate(order):
                sheet.alpha_composite(shot(k, variant=v, yaw=20, elev=deg, frame=1.24).resize((C, C), Image.LANCZOS), (i * C, 0))
            sheet.convert('RGB').save(os.path.join(out, '_sheets', f'lab10_lineup_3d_{eid}.png'), optimize=True)
        with open(os.path.join(ROOT, 'specs', '3d', 'views.json'), 'w', encoding='utf-8') as f:
            json.dump({'library': 'lab3d-views', 'version': '1.0', 'renderer': 'chars3d/tools/render_views.py',
                       'size_px': 512, 'frame_world': 1.24, 'frame_note': '화면 한 변 = 박사 키의 1.24배, 발 기준선 공통 — 캐릭터끼리 키 비교 가능 (face_* 는 0.62)',
                       'count': len(rows), 'views': rows}, f, ensure_ascii=False, indent=1)
        print('views', len(rows))
        b.close()


if __name__ == '__main__':
    main()
