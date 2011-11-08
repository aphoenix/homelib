# Loaning Library


## Introduction

This is a simple loaning library meant to address two needs that I have noticed
for my personal home library. First, I frequently loan books to people and then
lose track of where my books are. Second, I frequently receive gifts as books
but because I have many (thousands) I frequently receive doubles. This home
catalog will allow me to keep track of where my books are and will allow
other people to see if I already own a book.


## Items

Current support is only for books. This was a conscious choice to simplify the
development of the site, in an effort to release early and often. A certain
amount of refactoring is to be expected before the next version.


## Users

I made an active choice not to use the built in userbase as borrowers. The 
reason for this is that at this point, this is not a particularly social site.
I am not expecting the borrowers of items to want to log in - i.e. this is more
for my benefit than it is for others.


## Roadmap

This is not what I would consider a release candidate. Here is what I would
like to include moving forward to get it to a place where it would be a useful
tool for general consumption.

- we are not really doing any data sanitization
- genre should be tags and allow multiples
- searchable
- wishlist
- ISBN integration
- multiple media (dvd, video games, cd, etc.)
- app for scanning barcodes


## The Smartphone App

This would benefit from a native smartphone app that scans barcodes to give you
the information on your book or media that you are adding to or signing out 
from your catalog. To this end, I am examining django-piston to create a REST
API that the app could use to interact with django, and ZXing to handle the
actual scanning and interpreting of the barcodes. Proof of concept scanner is
easy to set up.
