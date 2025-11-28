import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arman_website.settings')
django.setup()

from products.models import Product

mapping = {
    'iPhone 14': '/static/products/iphone.svg',
    'AirPods': '/static/products/airpods.svg',
    'MacBook Pro': '/static/products/macbook.svg',
    'iPad Air': '/static/products/ipad.svg',
    'Apple Watch': '/static/products/watch.svg',
}

for title, path in mapping.items():
    p = Product.objects.filter(title=title).first()
    if p:
        p.image = path
        p.save()
        print(f"Updated {title} -> {p.image}")
    else:
        print(f"Product not found: {title}")

print('Local image paths set')
