from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('arman.urls')),
    path('', include('users.urls')),
    path('', include('products.urls')),
]

# Serve static files in development
if settings.DEBUG:
    # Prefer STATICFILES_DIRS (developer static folder) if present, otherwise use STATIC_ROOT
    doc_root = None
    if hasattr(settings, 'STATICFILES_DIRS') and settings.STATICFILES_DIRS:
        # STATICFILES_DIRS may contain Path objects; convert to string
        doc_root = str(settings.STATICFILES_DIRS[0])
    else:
        doc_root = str(settings.STATIC_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=doc_root)
