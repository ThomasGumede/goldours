from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

urlpatterns = [
    path('goldours-admin/', admin.site.urls),
    path("", include("accounts.urls", namespace="accounts")),
    path("", include("goldours_home.urls", namespace="goldours_home")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)