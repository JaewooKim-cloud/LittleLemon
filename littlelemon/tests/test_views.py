from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Cream", Price=90, Inventory=10)
    def test_getall(self):
        all_objs=Menu.objects.all()
        self.assertEqual(all_objs, "Cream : 80")
