from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import ProjectSitemap, PersonSitemap,StaticViewSitemap

sitemaps = {
    'projects': ProjectSitemap,
    'persons': PersonSitemap,
    'static': StaticViewSitemap,
}

# handler404 = 'main.views.custom_404_view'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include('main.urls')),
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# from django.urls import path, include,re_path
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.views.generic import TemplateView
# from django.contrib.sitemaps.views import sitemap
# from main.sitemaps import ProjectSitemap, PersonSitemap,StaticViewSitemap

# sitemaps = {
#     'projects': ProjectSitemap,
#     'persons': PersonSitemap,
#     'static': StaticViewSitemap,
# }

# # handler404 = 'main.views.custom_404_view'

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('',include('main.urls')),
#     re_path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
#     path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

