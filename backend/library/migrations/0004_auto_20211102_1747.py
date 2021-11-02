# Generated by Django 3.2.8 on 2021-11-02 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211102_1747'),
        ('library', '0003_auto_20211102_1747'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='library.category', verbose_name='دسته\u200cبندی'),
        ),
    ]
