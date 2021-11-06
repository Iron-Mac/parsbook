from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from random import randint
from .models import Category, Product
from account.models import User
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.

class LatestBookList(APIView):
    def get(self,request , format=None):
        books = Product.objects.all()[0:10]
        serializer = ProductSerializer(books,many=True)
        return Response(serializer.data)

class BookDetail(APIView):
    def get_object(self , category_slug , product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self,request,category_slug,product_slug,format=None):
        book= self.get_object(category_slug,product_slug)
        serializer = ProductSerializer(book)
        return Response(serializer.data)


class BookCartDetail(APIView):
    def get_object(self , product_id):
        try:
            return Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404
    def get(self,request,product_id,format=None):
        book= self.get_object(product_id)
        serializer = ProductSerializer(book)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self,category_slug):
        return get_object_or_404(Category.objects.filter(slug=category_slug))
    
    def get(self,request,category_slug,format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def send_reg_sms(request):
    print(request.data)
    mobile_phone = request.data
    cache_key = str(mobile_phone["mb"])
    cache_time = 120
    pin = randint(1000,9999)
    cache_try = 0
    data = pin
    print("----------------\n",data,"\n----------------\n")
    cache.set(cache_key,data,cache_time)
    cache.set(cache_key+'_try',0,120)
    return Response({
        'message' : 'sms sent to your terminal ;)'},status=status.HTTP_200_OK)

@api_view(['POST'])
def verify_sms(request):
    raw_data = request.data
    print(raw_data)
    mb = str(raw_data["mb"])
    fn = str(raw_data["fn"])
    ln = str(raw_data["ln"])
    passwd = str(raw_data["pass"])
    zipcode =int(raw_data["zip"])
    addr = str(raw_data["ad"])
    pin_code = raw_data["pin"]
    tries = cache.get(mb+'_try')
    data = cache.get(mb)
    print("this is data")
    print(data)
    if data!=None:
        if int(tries)<3:
            if int(pin_code) == data:
                cache.set(str(data)+"_succesful",1,1800)
                User.objects.create(username=mb,password=passwd,addres=addr,zipcode=zipcode,first_name=fn,last_name=ln)
                return Response({
                    "message":"User made seccesfully"
                },status=status.HTTP_201_CREATED)
            else:
                cache.incr(mb+'_try')
                return Response(
                    {
                        "message":"wrong pin code try again!"
                    },status=status.HTTP_200_OK
                )
    else:
        return Response({
                "message":"not seccesfull"},status=status.HTTP_400_BAD_REQUEST
            )
"""@api_view(['POST'])
def register_user(request):
"""