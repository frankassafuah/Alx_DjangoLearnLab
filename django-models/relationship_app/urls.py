from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, librarian_view, member_view, add_book, edit_book, delete_book
from django.views.generic import DetailView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', DetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', views.register, name='register'),
     path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
     path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:pk>/', edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]
