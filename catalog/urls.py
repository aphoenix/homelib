from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from catalog.models import Book, Borrower


urlpatterns = patterns('',
    url(r'^$', 'catalog.views.index'),
    url(r'^book/$',
        ListView.as_view(
            queryset=Book.objects.order_by('title'),
            template_name='catalog/library.html')),
    url(r'^book/(?P<pk>\d+)/$', 
        DetailView.as_view(
            model=Book,
            template_name='catalog/book.html')),
    url(r'^book/(?P<pk>\d+)/signout/$', 'catalog.views.signout'),
    url(r'^borrower/$',
        ListView.as_view(
            queryset=Borrower.objects.order_by('name'),
            template_name='catalog/everyone.html')),
    url(r'^borrower/(?P<pk>\d+)/$', 
        DetailView.as_view(
            model=Book,
            template_name='catalog/borrower.html'))
    )

