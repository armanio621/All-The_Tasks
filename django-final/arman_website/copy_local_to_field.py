import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'arman_website.settings')
django.setup()

from products.models import Product

count = 0
for p in Product.objects.all():
    if p.image and p.image.startswith('/static/') and not p.local_image:
        p.local_image = p.image
        p.save()
        count += 1
print(f'Copied local paths into local_image for {count} products')
