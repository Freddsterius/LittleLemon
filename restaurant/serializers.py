from django.contrib.auth.models import User
from .models import Menu
from rest_framework.serializers import ModelSerializer


class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'invetory']
