from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(("عنوان دسته‌بندی"), max_length=200)
    slug = models.SlugField(("اسلاگ"))
    class Meta:
        ordering=('title',)
    def __str__(self) :
        return self.title
    def get_absolute_url(self):
        return f"/{self.slug}/"
    


class Book(models.Model):
    title = models.CharField(("عنوان کتاب"), max_length=250)
    slug = models.SlugField(("اسلاگ"))
    author = models.CharField(("نوسنده"), max_length=250)
    translator = models.CharField(("مترجم"), max_length=250, null=True , blank= True)
    pages = models.IntegerField(("تعداد صفحات"))
    thumbnail = models.ImageField(("تصویر"), upload_to="img/")
    publisher = models.CharField(("ناشر"), max_length=250)
    description = models.TextField(("نوضیحات کتاب"))
    price = models.IntegerField(("قیمت"))
    rate = models.FloatField(("امتیاز"),max_length=10)
    category = models.ForeignKey("Category", verbose_name=("دسته‌بندی"), on_delete=models.CASCADE, related_name= "books")
    publish_date = models.DateTimeField(("تاریخ"), auto_now=False, auto_now_add=False)

    class Meta:
        ordering=('-publish_date',)
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.pk}"
    def get_thumbnail(self):
        return 'http://127.0.0.1:8005' + self.thumbnail.url
    