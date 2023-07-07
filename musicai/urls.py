from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from account.views import login_page

urlpatterns = [
    # Admin login
    path("admin/login/", login_page),

    # Admin site
    path("admin/", admin.site.urls),

    # User authentication URLs
    path("accounts/", include("allauth.urls")),

    # App-specific URLs
    path("", include("account.urls")),
    path("", include("generator.urls")),
    path("", include("showcase.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)