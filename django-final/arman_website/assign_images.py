import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arman_website.settings')
django.setup()

from products.models import Product
from django.conf import settings

def get_static_products_dir():
    static_dirs = getattr(settings, 'STATICFILES_DIRS', [])
    if static_dirs:
        return static_dirs[0]
    # fallback to BASE_DIR/static
    return os.path.join(settings.BASE_DIR, 'static')

def main():
    static_root = get_static_products_dir()
    product_dir = os.path.join(static_root, 'products')
    if not os.path.isdir(product_dir):
        print('Static products folder not found:', product_dir)
        return

    files = [f for f in os.listdir(product_dir) if os.path.isfile(os.path.join(product_dir, f))]
    if not files:
        print('No files found in', product_dir)
        return

    for p in Product.objects.all():
        name = (p.title or '').lower().replace(' ', '').replace('-', '')
        matched = None
        for f in files:
            fname = os.path.splitext(f)[0].lower().replace(' ', '').replace('-', '')
            if name and (name in fname or fname in name):
                matched = f
                break

        if matched:
            path = f"/static/products/{matched}"
            p.local_image = path
            p.save()
            print(f"Updated {p.title} -> {path}")
        else:
            print(f"No image matched for {p.title}")

if __name__ == '__main__':
    main()
