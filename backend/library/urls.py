
from django.urls import path, include
from .views import  BookDetail, CategoryDetail, LatestBookList,BookCartDetail, register_user, search, send_reg_sms,verify_sms
app_name="library"

urlpatterns = [
    path("latest-books/",LatestBookList.as_view()),
    path('books/<slug:category_slug>/<slug:product_slug>/',BookDetail.as_view()),
    path('books/<slug:category_slug>/',CategoryDetail.as_view()),
    path('products/search/', search),
    path('<int:product_id>/',BookCartDetail.as_view()),
    path('user/reg/',send_reg_sms),
    path('user/reg/verify/',verify_sms),
    path('user/reg/verify/create',register_user)

]