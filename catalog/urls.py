from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('catalog.views',
    url(r'^$', 'index'),
    url(r'^book/(?P<book_id>\d+)/$', 'book'),
    url(r'^borrower/(?P<borrower_id>\d+)/$', 'borrower'),
    )

