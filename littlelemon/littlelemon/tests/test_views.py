from django.test import TestCase

from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(Title="Pizza", Price=10.99, Inventory=100)
        Menu.objects.create(Title="Burger", Price=5.99, Inventory=50)
        Menu.objects.create(Title="Pasta", Price=7.99, Inventory=75)

        return super().setUp()

    def test_get_all(self):
        items = Menu.objects.all()
        self.assertEqual(len(items), 3)
