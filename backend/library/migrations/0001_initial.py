# Generated by Django 3.2.8 on 2021-10-22 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته\u200cبندی')),
                ('slug', models.SlugField(verbose_name='اسلاگ')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='عنوان کتاب')),
                ('slug', models.SlugField(verbose_name='اسلاگ')),
                ('author', models.CharField(max_length=250, verbose_name='نوسنده')),
                ('translator', models.CharField(blank=True, max_length=250, null=True, verbose_name='مترجم')),
                ('page', models.IntegerField(verbose_name='تعداد صفحات')),
                ('thumbnail', models.ImageField(upload_to='img/', verbose_name='تصویر')),
                ('publisher', models.CharField(max_length=250, verbose_name='ناشر')),
                ('description', models.TextField(verbose_name='نوضیحات کتاب')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('rate', models.FloatField(max_length=10, verbose_name='امتیاز')),
                ('created_date', models.DateTimeField(verbose_name='تاریخ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.category', verbose_name='دسته\u200cبندی')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]
