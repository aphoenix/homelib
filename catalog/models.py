from django.db import models
from datetime import datetime  # for tracking Loan


class Book(models.Model):
    
    """ Book Model - an item in the lending library """
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, blank=True)
    #isbn = models.IntegerField()
    
    # This will likely change somewhat based on what kind of 
    # information it's decided to keep on books. Also, hook
    # into an ISBN database for ease of entry.
    # It's also possible to generalize this to media by having
    # an "Items" model, then defining models for subsequent
    # media types. For the current issue, this is not necessary.

    def __unicode__(self):
        return self.title


class Borrower(models.Model):

    """ Borrower Model - who is taking the book """

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name


class Loan(models.Model):

    """ Loan Model - matching borrowers to books """

    book = models.ForeignKey(Book)
    borrower = models.ForeignKey(Borrower)
    date_lent = models.DateField(default=datetime.now())
    returned = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0}'.format(self.book)
    def return_it(self):
        return self.returned==True
