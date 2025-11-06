from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User  # for test user


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Chocolate Ice Cream",
            price=4.5,
            inventory=100
        )

        self.assertEqual(str(item), "Chocolate Ice Cream - $4.5")


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            title="Chocolate Ice Cream",
            price=4.5,
            inventory=100
        )

        Menu.objects.create(
            title="Pizza",
            price=26.99,
            inventory=50
        )

        Menu.objects.create(
            title="Burger",
            price=9,
            inventory=25
        )

        # Createing a test user to authenticate with
        self.user = User.objects.create_user(
            username='testuser',
            password='testPass123!',
            email='test@lemon.com'
        )

    def test_get_all(self):
        client = APIClient()

    #    Use the testuser to authenticate
        client.force_authenticate(user=self.user)

        response = client.get('/restaurant/menu/')

        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, serializer.data)
