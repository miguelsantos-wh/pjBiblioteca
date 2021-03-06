from django.conf.urls import include, url
from django.contrib import admin
from django.conf import  settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'pjBiblioteca.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^biblioteca/', include('biblioteca.urls', namespace="biblioteca")),
    url(r'^$', include('biblioteca.urls', namespace="index")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)