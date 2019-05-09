from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('filmak.views',
    # Examples:
    # url(r'^$', 'filmSite.views.home', name='home'),
    # url(r'^filmSite/', include('filmSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	#El segundo aldagaia tiene que coincidir con el "def nombre" de views.
	#En el url(r'^login/$, 'loginForm', name='login') por ejemplo, el loginForm tiene que estar tambien en el views.py

    # Uncomment the next line to enable the admin:
    url(r'^$', 'hasierakoMenuaLogged', name='homeLogged'),
    url(r'^index/$', 'index', name='index'),
    url(r'^login/$', 'loginForm', name='login'),
    url(r'^loginEgin/$', 'loginEgin', name='loginEgin'),
    url(r'^signup/$', 'signup', name='signup'),
    url(r'^(?P<filma_id>\d+)/$', 'detail'),
)
