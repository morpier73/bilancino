# Assembla la PWA (nella cartella del repository) e la pagina di anteprima (preview.html, ignorata da git) dai file in src/.
from pathlib import Path
from PIL import Image, ImageDraw
import shutil
root = Path(__file__).parent
src, dist = root / "src", root
css, foods, app = (src / "app.css").read_text(), (src / "foods.js").read_text(), (src / "app.js").read_text()
fonts = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Figtree:wght@400;500;600;700&display=swap">'
body = f'<div class="app" id="app"></div>\n<div id="sheet"></div>\n<nav class="tabbar" id="tabbar"></nav>\n<script>\n{foods}\n{app}\n</script>'
(root / "preview.html").write_text(f'<title>Bilancino</title>\n{fonts}\n<style>\n{css}\n</style>\n{body}\n')
(dist / "index.html").write_text(f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Bilancino</title>
<meta name="theme-color" content="#1E7556">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png"><link rel="apple-touch-icon" href="icon-192.png">
{fonts}
<style>\n{css}\n</style></head>
<body>
{body}
</body></html>
''')
for f in ["sw.js", "manifest.webmanifest"]:
    shutil.copy(src / f, dist / f)
for size in (192, 512):
    s = size / 32
    im = Image.new("RGB", (size, size), "#1E7556")
    d = ImageDraw.Draw(im)
    # bilancia stilizzata, dentro l'area sicura delle icone "maskable"
    d.rounded_rectangle([8*s, 11*s, 24*s, 24*s], radius=4*s, fill="#FFFFFF")
    d.rounded_rectangle([13*s, 8*s, 19*s, 10.5*s], radius=1.2*s, fill="#FFFFFF")
    d.ellipse([12*s, 13.5*s, 20*s, 21.5*s], fill="#1E7556")
    d.line([16*s, 17.5*s, 18.4*s, 15*s], fill="#FFFFFF", width=max(2, int(1.3*s)))
    im.save(dist / f"icon-{size}.png")
print("ok")
