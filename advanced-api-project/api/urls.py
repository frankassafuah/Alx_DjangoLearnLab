from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    # URL for listing all books and creating a new book
    path('books/', BookListView.as_view(), name='book-list'),

    # URL for retrieving, updating, or deleting a specific book by its ID
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
