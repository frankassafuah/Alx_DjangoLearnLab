Create a Book Instance
Command to create a Book instance:

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)


Delete the Book
Command to delete the book:

book.delete()
books = Book.objects.all()
print(books)


Retrieve the Book
Command to retrieve the book:

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)


Update the Book
Command to update the book's title:

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
