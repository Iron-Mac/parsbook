from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email','addres','zipcode')

UserAdmin.list_display += ('addres','zipcode')

admin.site.register(User, UserAdmin)
