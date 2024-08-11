Retrieve the Book
Command to retrieve the book:

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
