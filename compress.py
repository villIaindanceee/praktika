import re, base64, io, os, glob, shutil
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
pattern = re.compile(r'data:image/(?:png|jpeg|jpg);base64,([A-Za-z0-9+/=\s]+)')

def conv(m):
    raw = base64.b64decode(re.sub(r'\s+', '', m.group(1)))
    img = Image.open(io.BytesIO(raw))
    buf = io.BytesIO()
    img.save(buf, 'WEBP', quality=80)
    return 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()

backup = os.path.join('..', 'backup_images')
os.makedirs(backup, exist_ok=True)

for path in glob.glob('images/*.svg'):
    if os.path.getsize(path) < 20 * 1024 * 1024:
        continue
    shutil.copy(path, backup)
    with open(path, encoding='utf-8') as f:
        text = f.read()
    with open(path, 'w', encoding='utf-8') as f:
        f.write(pattern.sub(conv, text))
    print(path, round(os.path.getsize(path) / 1024 / 1024, 1), 'MB')