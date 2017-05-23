from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    a=Book.objects.create(title='The Great Gatsby', author='F scotty fitzgeraldson', published_date='1993-03-11')
    b=Book.objects.create(title='My book', author='Drew Pham', published_date='1993-03-11')
    c=Book.objects.create(title='The Engine That Couldnt', author='You??', published_date='1993-03-11')
    print a.published_date, b.title, c.title
    return render(request, 'django_books/index.html')
