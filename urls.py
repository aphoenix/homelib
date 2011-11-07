from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^catalog/', include('catalog.urls')),
    url(r'^catalog/$', 'catalog.views.index'),
    url(r'^catalog/book/(?P<book_id>\d+)/$', 'catalog.views.book'),
    url(r'^catalog/borrower/(?P<borrower_id>\d+)/$', 'catalog.views.borrower'),
    url(r'^admin/', include(admin.site.urls)),
)
