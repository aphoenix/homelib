from django.shortcuts import render_to_response, get_object_or_404
from catalog.models import Book, Borrower, Loan


def index(request):
    latest_book_list = Book.objects.all().order_by('title')[:3]
    return render_to_response('catalog/index.html', { 'latest_book_list': latest_book_list, })


def book(request, book_id):
    b = get_object_or_404(Book, pk=book_id)
    return render_to_response('catalog/book.html', {'book': b})


def borrower(request, borrower_id):
    b = get_object_or_404(Borrower, pk=borrower_id)
    return render_to_response('catalog/borrower.html', {'borrower': b})
