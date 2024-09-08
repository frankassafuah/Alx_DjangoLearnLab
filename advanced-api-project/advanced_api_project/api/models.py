from django.db import models

# The Author model represents a person who writes books.
# It contains only one field, 'name', which stores the author's name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The Book model represents a book written by an author.
# It has three fields: 'title', 'publication_year', and a ForeignKey 'author' linking to the Author model.
# This establishes a one-to-many relationship, where one author can write many books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
