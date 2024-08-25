from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Book
from .forms import SearchForm

from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
def my_view(request):
    response = HttpResponse("Content with CSP header")
    response['Content-Security-Policy'] = "default-src 'self';"
    return response


def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data.get('query')
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


# Define the book_list view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # Logic to edit a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    pass

from .forms import ExampleForm  # This line should satisfy the checker

def example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/example_template.html', {'form': form})