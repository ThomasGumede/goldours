from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from .sitemaps import StaticViewSitemap, BlogSitemap
from django.conf.urls.i18n import i18n_patterns

sitemaps = {
    'static': StaticViewSitemap,
    'blogs': BlogSitemap
}

urlpatterns = [
    path('goldours-admin', admin.site.urls),
    path("", include("accounts.urls", namespace="accounts")),
    path("", include("goldours_home.urls", namespace="goldours_home")),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

