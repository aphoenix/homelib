from catalog.models import Book, Borrower, Loan
from django.contrib import admin


class LoanInline(admin.StackedInline):
    model = Loan
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre')
    inlines = [LoanInline]

    

admin.site.register(Book, BookAdmin)
admin.site.register(Borrower)
admin.site.register(Loan)
