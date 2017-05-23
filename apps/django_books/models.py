from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Book(models.Model):
    title = models.CharField(max_length=38)
    published_date=models.DateTimeField()
    category = models.CharField(max_length=100)
    in_print = models.BooleanField(default=True)
    author = models.OneToOneField(Author, related_name='your_book')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
