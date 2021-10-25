
from django.urls import path, include
from .views import BookDetail, CategoryDetail, LatestBookList
app_name="library"

urlpatterns = [
    path("latest-books/",LatestBookList.as_view()),
    path('books/<slug:category_slug>/<int:book_id>/',BookDetail.as_view()),
    path('books/<slug:category_slug>/',CategoryDetail.as_view())
]