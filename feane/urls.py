from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('index.html', include('backend.urls')),
    path('menu.html', include('backend.urls')),
    path('book.html', include('backend.urls')),
    path('about.html', include('backend.urls')),
    path('submit', include('backend.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
