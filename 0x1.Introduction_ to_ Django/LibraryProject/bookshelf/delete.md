Delete the Book
Command to delete the book:

from bookshelf.models import Book

book.delete()
books = Book.objects.all()
print(books)
