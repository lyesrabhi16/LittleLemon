from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def instance(self):
        return Menu.objects.create(Title="Pizza", Price=10.99, Inventory=100)

    def test_get_item(self):
        item = self.instance()
        self.assertEqual(str(item), "Pizza : 10.99")
