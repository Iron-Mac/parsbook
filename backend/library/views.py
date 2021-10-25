from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
# Create your views here.

class LatestBookList(APIView):
    def get(self,request , format=None):
        books = Book.objects.all()[0:10]
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    def get_object(self , category_slug , book_id):
        return get_object_or_404(Book.objects.filter(category__slug=category_slug, pk = book_id))

    def get(self,request,category_slug,book_id,format=None):
        book= self.get_object(category_slug,book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self,category_slug):
        return get_object_or_404(Category.objects.filter(slug=category_slug))
    
    def get(self,request,category_slug,format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data) 