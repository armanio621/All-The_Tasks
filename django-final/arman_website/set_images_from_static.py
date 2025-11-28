import os
import django
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arman_website.settings')
django.setup()

from products.models import Product

static_dir = Path(__file__).resolve().parent / 'static' / 'products'
print('Static products dir:', static_dir)
files = [f.name for f in static_dir.iterdir() if f.is_file()]
print('Found files:', files)

# normalize helper
def normalize(s):
    return ''.join(ch for ch in s.lower() if ch.isalnum())

files_norm = {normalize(f): f for f in files}

updated = 0
for p in Product.objects.all():
    title = p.title or ''
    normalized_title = normalize(title)
    matched = None
    # exact contains
    for fname in files:
        if normalized_title and normalized_title in normalize(fname):
            matched = fname
            break
    # try split words
    if not matched:
        for word in title.split():
            nw = normalize(word)
            if nw:
                for fname in files:
                    if nw in normalize(fname):
                        matched = fname
                        break
            if matched:
                break
    # fallback: choose first image if none matched
    if not matched and files:
        matched = files[0]

    if matched:
        p.local_image = f'/static/products/{matched}'
        p.save()
        print(f"Updated {p.title} -> {p.local_image}")
        updated += 1
    else:
        print(f"No files found to match for {p.title}")

print(f'Done. Updated {updated} products.')
