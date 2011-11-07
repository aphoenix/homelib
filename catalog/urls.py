from django.conf.urls.defaults import 

urlpatterns = patterns('catalog.views',
    url(r'^$', 'catalog.views.index'),
    url(r'^/book/(?P<book_id>\d+)/$', 'catalog.views.books'),
    url(r'^/borrower/(?P<borrower_id>\dA+)/$', 'catalog.views.borrower'),
)
