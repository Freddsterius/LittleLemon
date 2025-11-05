from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Chocolate Ice Cream",
            price=80,
            inventory=100
        )

        self.assertEqual(str(item), "Chocolate Ice Cream - $80")


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=95, inventory=75)

    def test_getall(self):
        client = APIClient()

        response = client.get('/restaurant/menu/')

        menus = Menu.objects.all()

        serializer = MenuSerializer(menus, many=True)

        # Assert the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)


# from django.test import TestCase
# from restaurant.models import Menu
# from restaurant.serializers import MenuSerializer
# from rest_framework.test import APIClient
# from rest_framework import status


# class MenuTest(TestCase):
#     def test_get_item(self):
#         # Create a new Menu instance
#         item = Menu.objects.create(
#             title="IceCream",
#             price=80,
#             inventory=100
#         )

#         # Test the string representation of the Menu object
#         self.assertEqual(str(item), "IceCream : 80")


# class MenuViewTest(TestCase):
#     def setUp(self):
#         # Add test instances of Menu model
#         Menu.objects.create(title="IceCream", price=80, inventory=100)
#         Menu.objects.create(title="Pizza", price=120, inventory=50)
#         Menu.objects.create(title="Burger", price=95, inventory=75)

#     def test_getall(self):
#         # Create API client
#         client = APIClient()

#         # Retrieve all Menu objects from the API
#         response = client.get('/api/menu/')  # Adjust URL to match your urlpatterns

#         # Retrieve all Menu objects from the database
#         menus = Menu.objects.all()

#         # Serialize the data
#         serializer = MenuSerializer(menus, many=True)

#         # Assert the response status is 200 OK
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Assert the serialized data equals the response data
#         self.assertEqual(response.data, serializer.data)
