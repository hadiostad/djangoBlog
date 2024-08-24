from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # import configuration

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) /  # Serving Uploaded File
               + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))  # Serving Static File
