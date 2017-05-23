from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=38)
    author = models.CharField(max_length= 200)
    published_date=models.DateTimeField()
    category = models.CharField(max_length= 100)
    in_print = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
