from django.conf.urls.defaults import *

urlpatterns = patterns('shows.views',
    # url(r'^$', 'home', name="shows_home"),
    url(r'^add/', 'add', name="shows_add"),
    url(r'^delete/', 'delete', name="shows_delete"),
    # catch all pattern at the end
    # url(r'^(.*?)/?$', 'shows', name="shows"),
)