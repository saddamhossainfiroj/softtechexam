from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Soft Tech Exam Project"
admin.site.site_title = "Soft Tech Exam Project"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userapp.urls')),
    path('/', include('userapp.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
