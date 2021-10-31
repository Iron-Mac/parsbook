
from django.urls import path, include
from .views import BookDetail, CategoryDetail, LatestBookList, send_reg_sms,verify_sms
app_name="library"

urlpatterns = [
    path("latest-books/",LatestBookList.as_view()),
    path('books/<slug:category_slug>/<int:book_id>/',BookDetail.as_view()),
    path('books/<slug:category_slug>/',CategoryDetail.as_view()),
    path('user/reg/',send_reg_sms),
    path('user/reg/verify/',verify_sms)
]