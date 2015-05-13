from django.conf.urls import patterns, include, url
from django.contrib import admin
from Google_IITB.views import django_search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Google.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^search/(.+)/$', django_search),
)
