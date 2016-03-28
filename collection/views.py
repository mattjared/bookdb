from django.shortcuts import render, redirect
from collection.forms import BookForm
from collection.models import Book

def index(request):
    number = 6
    books = Book.objects.all()
    return render(request, 'index.html', {
            'number': number,
            'books': books,
        })

def book_detail(request, slug):
    books = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
            'books': books,
        })

def edit_book(request, slug):
    books = Book.objects.get(slug=slug)
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