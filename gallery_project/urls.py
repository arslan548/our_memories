from django.contrib import admin
from django.urls import path, include  # Import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('gallery.urls')),
# Include the gallery app URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
