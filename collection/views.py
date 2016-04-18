from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

from collection.forms import BookForm
from collection.models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {
            'books': books,
        })

def book_detail(request, slug):
    books = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
            'books': books,
        })

@login_required
def edit_book(request, slug):
    books = Book.objects.get(slug=slug)
    if books.user != request.user:
        raise Http404
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('book_detail', slug=books.slug)
    else:
        form = form_class(instance=books)

    return render(request, 'books/edit_book.html', {
        'books': books,
        'form': form
    })

def create_book(request):
    form_class = BookForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            books = form.save(commit=False)
            books.user = request.user
            books.slug = slugify(books.name)
            books.save()
            return redirect('book_detail', slug=books.slug)
    else:
        form = form_class()
    return render(request, 'books/create_book.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        books = Book.objects.filter(name__istartswith=initial).order_by('name')
    else:
        books = Book.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'books': books,
        'initial': initial,
    })
