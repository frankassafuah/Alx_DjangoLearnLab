from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# The BookSerializer is responsible for serializing and deserializing the Book model.
# It converts complex data types like model instances into Python datatypes and vice versa.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# The AuthorSerializer is responsible for serializing the Author model and its related books.
# It includes a nested BookSerializer to represent the books associated with the author.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
