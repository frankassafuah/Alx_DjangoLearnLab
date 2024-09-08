# api/urls.py

from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URL for listing all books and creating a new book
    path('books/', BookListView.as_view(), name='book-list'),

    # URL for retrieving a specific book by its ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # URL for creating a new book
    path('books/create/', BookListView.as_view(), name='book-create'),

    # URL for updating a specific book by its ID
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # URL for deleting a specific book by its ID
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
