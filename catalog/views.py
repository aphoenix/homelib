from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from catalog.models import Book, Borrower, Loan


def index(request):
    latest_book_list = Book.objects.all().order_by('title')[:5]
    latest_borrower_list = Borrower.objects.all().order_by('name')[:5]
    latest_loan_list = Loan.objects.all()[:5]
    return render_to_response('catalog/index.html', { 
        'latest_book_list' : latest_book_list, 
        'latest_borrower_list' : latest_borrower_list,
        'latest_loan_list' : latest_loan_list
    })


def signout(request, book_id):
    b = get_object_or_404(Book, pk=book_id)
    try: #this input certainly requires some data sanitization
        r = Borrower.objects.get(name=request.POST['name'])
    except (KeyError, Borrower.DoesNotExist):
        new = Borrower(name=request.POST['name'], email=request.POST['email'])
        new.save()
        r = new
    try: # I'm mildly entertained by the backwards try / except. It's late.
        loan = Loan.objects.get(book=b)
    except (KeyError, Loan.DoesNotExist):
        loan = Loan(book=b,borrower=r)
        loan.save()
        return HttpResponseRedirect('/borrower/'+str(r.id))
    else:
        return render_to_response('catalog/book.html', {
            'book': b,
            'error_message': 'That book is already signed out.'
            }, context_instance=RequestContext(request))
