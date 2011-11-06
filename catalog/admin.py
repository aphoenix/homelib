from catalog.models import Book, Borrower, Loan
from django.contrib import admin


class LoanInLine(admin.StackedInline):
    model = Loan
    extra = 1


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','genre')
    inlines = [LoanInLine]


admin.site.register(Book, BookAdmin)
admin.site.register(Borrower)
