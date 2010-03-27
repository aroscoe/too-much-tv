import os.path

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^shows/', include('shows.urls'), name="shows"),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # TODO: use PROJECT_ROOT?
    urlpatterns += patterns('',
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'assets')}),
    )