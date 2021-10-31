from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    addres = models.TextField(("آدرس"),null=True)
    zipcode = models.PositiveIntegerField(("کدپستی"),null=True)
    