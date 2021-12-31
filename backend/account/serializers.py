from rest_framework import serializers
from .models import User


class CusUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'