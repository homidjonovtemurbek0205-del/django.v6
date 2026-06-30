from django.shortcuts import render
from .forms import BookForm
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})


def add_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return render(request, 'success.html')
    data = {'form': form}
    return render(request, 'book.html', data)

def success(request):
    return render(request, 'success.html')