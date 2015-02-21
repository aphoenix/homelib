# Loaning Library


## Introduction

This is a simple loaning library meant to address two needs that I have noticed
for my personal home library. First, I frequently loan books to people and then
lose track of where my books are. Second, I frequently receive gifts as books
but because I have many (thousands) I frequently receive doubles. This home
catalog will allow me to keep track of where my books are and will allow
other people to see if I already own a book.

This is made for Django 1.3.1 and Python 2.5 < x < 3. It uses sqlite. A sample
database will be available.


## Notes

This was mostly as a learning experience in Django, as I am more comfortable
using Bottle. This was fun and interesting - I had explored Django a year or
two ago and moved on to other frameworks, but I think this one has a lot of
potential.

I think I touched on everything in the walkthrough. I also did a bit of work
in templating. The design is silly, but functional enough. I enjoyed the mix
and match vibe I got from extending the standard DetailView class; that was a
last minute addition.

Current support is only for books. This was a conscious choice to simplify the
development of the site, in an effort to release early and often. A certain
amount of refactoring is to be expected before the next version.


## Static Files and The Admin Interface

I had some problems with Static files and the admin site. I think it is due to
the fact that I upgraded from an older version of Django in the middle of
working on this project.


## Users

I made an active choice not to use the built in userbase as borrowers. The 
reason for this is that at this point, this is not a particularly social site.
I am not expecting the borrowers of items to want to log in. I expect to use
both the front end and the back end exclusively myself.


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

I think this is where success would happen. A lot of people have smart phones
and being able to do a signout in 10 seconds without using a computer is a good
goal to work towards.
