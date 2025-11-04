from dataclasses import field
from django.contrib.auth.models import User
from .models import Menu, Booking
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory']


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'no_of_guests', 'booking_date']
