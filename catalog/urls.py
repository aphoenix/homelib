from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('catalog.views',
    url(r'^$', 'index'),
    url(r'^(?P<book_id>\d+)/$', 'detail'),
    )
