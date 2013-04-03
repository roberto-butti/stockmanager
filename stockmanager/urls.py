from django.conf.urls.static import static
from django.conf.urls.defaults import patterns, url, include
from django.conf import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
   # (r'', include('stockmanager.apps.')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Application urls
    (r'^$', 'frontend.views.indexAction'),
    (r'^upload/$', 'picturemanager.views.uploadAction'),
    (r'^login/$', 'frontend.views.loginAction'),
    (r'^register/$', 'frontend.views.registerAction'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'})
)

# Serve media files if debug is on
if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
