from django.shortcuts import render, redirect
from .models import Book
from .forms import addBookForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books':books})

def book_detail(request, title):
    book = Book.objects.get(title=title)
    return render(request, 'book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        # new_book = Book(
        #     title = request.POST.get('title'),
        #     author = request.POST.get('author'),
        #     published_year = request.POST.get('published_year'),
        #     genre = request.POST.get('genre'),
        # )
        # new_book.save()
        form = addBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = addBookForm()
    return render(request, 'add_book.html', {'form': form})

def edit_book(request, title):
    book = Book.objects.get(title=title)

    if request.method == "POST":
        book.title = request.POST.get('title')

        book.save()
        return redirect('book_detail', title=book.title)
    
    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, title):
    book = Book.objects.get(title=title)

    if request.method == "POST":
        book.delete()
        return redirect("index")
    return render(request, 'delete_book.html', {'book':book})

