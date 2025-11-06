from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            title="Chocolate Ice Cream",
            price=4.5,
            inventory=100
        )

        self.assertEqual(str(item), "Chocolate Ice Cream - $4.5")
