
from rest_framework import serializers

from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
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
    products = ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "get_absolute_url",
            "products"
        )