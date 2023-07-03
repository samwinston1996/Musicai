from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from account.views import login_page


urlpatterns = [
    path("admin/login/", login_page),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("account.urls")),
    path("", include("generator.urls")),
    path("", include("showcase.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)