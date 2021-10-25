
from rest_framework import serializers

from .models import Book, Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "description",
            "price",
            "get_thumbnail",
            "rate",
            "author"
            )

class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "books"
        )