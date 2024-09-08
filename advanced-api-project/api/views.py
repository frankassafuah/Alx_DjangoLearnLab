# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListView to retrieve all books and CreateView to add a new book
class BookListView(generics.ListCreateAPIView):
    """
    GET: List all books.
    POST: Create a new book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only for unauthenticated users

# DetailView to retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a specific book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT: Update a book (authenticated users only).
    PATCH: Partially update a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
