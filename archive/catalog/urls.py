from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from catalog.models import Book, Borrower, Loan


# Provide the in / out information. Not optimal, mostly just playing with 
# subclasses of a standard view. Ideally, this would be one class extension 
# that would take an argument and work for either Books or Borrowers, but they
# have different relations to loans (1:1 Many:1).

# That *should* be fixed in a patch soon, which will also help us keep the 
# history of loans.

class BookDetailView(DetailView):
    ''' Mix and Match model details: Book info also shows some loan info.'''     
    context_object_name = "book"
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        try:
            context['loan'] = Loan.objects.get(book=self.get_object())
        except (KeyError, Loan.DoesNotExist):
            context['loan'] = False
        else:
            context['loan'] = True
        return context

class BorrowerDetailView(DetailView):
    ''' Mix and Match model details: Borrower info also shows some loan info.'''
    context_object_name = "borrower"
    model = Borrower

    def get_context_data(self, **kwargs):
        context = super(BorrowerDetailView, self).get_context_data(**kwargs)
        try:
            context['loan_list'] = Loan.objects.filter(borrower=self.get_object())
        except (KeyError, Loan.DoesNotExist):
            context['loan_list'] = ''
        return context 

urlpatterns = patterns('',
    url(r'^$', 'catalog.views.index'),

    url(r'^book/$',
        ListView.as_view(
            queryset = Book.objects.order_by('title'),
            template_name = 'catalog/library.html'
        )),
    
    url(r'^book/(?P<pk>\d+)/$', 
        BookDetailView.as_view(
            template_name = 'catalog/book.html',
        )),
    
    url(r'^book/(?P<book_id>\d+)/signout/$', 'catalog.views.signout'),
    
    url(r'^borrower/$',
        ListView.as_view(
            queryset = Borrower.objects.order_by('name'),
            template_name = 'catalog/everyone.html'
        )),
    
    url(r'^borrower/(?P<pk>\d+)/$', 
        BorrowerDetailView.as_view(
            template_name = 'catalog/borrower.html'
        )),
    url(r'^loan/$',
        ListView.as_view(
            queryset = Loan.objects.order_by('book'),
            template_name = 'catalog/loans.html'
        )),
    )

