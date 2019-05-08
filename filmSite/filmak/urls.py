from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('filmak.views',
    # Examples:
    # url(r'^$', 'filmSite.views.home', name='home'),
    # url(r'^filmSite/', include('filmSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'hasieraMenua', name='home'),
    url(r'^index/$', 'index', name='index'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^(?P<filma_id>\d+)/$', 'detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
)
