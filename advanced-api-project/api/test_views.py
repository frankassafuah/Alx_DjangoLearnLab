# api/test_views.py

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.book = Book.objects.create(title='Test Book', author='Author 1', publication_year=2020)
    
    def tearDown(self):
        self.client.logout()

    # Test the creation of a new Book
    def test_create_book(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': 'Author 2', 'publication_year': 2021}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    # Test retrieving the list of books
    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # Test retrieving a single book by ID
    def test_get_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    # Test updating an existing book
    def test_update_book(self):
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'Updated Book', 'author': 'Author 1', 'publication_year': 2020}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    # Test deleting a book
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test filtering by title
    def test_filter_books_by_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Test Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    # Test searching by author name
    def test_search_books_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Author 1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    # Test ordering by publication year
    def test_order_books_by_publication_year(self):
        Book.objects.create(title='Another Book', author='Author 2', publication_year=2019)
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2019)

    # Test unauthenticated user can't create a book
    def test_create_book_unauthenticated(self):
        self.client.logout()  # Log out to simulate unauthenticated access
        url = reverse('book-create')
        data = {'title': 'Unauthorized Book', 'author': 'Author 3', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test authenticated user can create a book
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='password')
        url = reverse('book-create')
        data = {'title': 'New Auth Book', 'author': 'Author 4', 'publication_year': 2022}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
