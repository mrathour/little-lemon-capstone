from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(
            Title="IceCream",
            Price=80,
            Inventory=100
        )
        Menu.objects.create(
            Title="Pizza",
            Price=300,
            Inventory=50
        )

    def test_getall(self):
        menu = Menu.objects.all()
        serialized_data = MenuSerializer(menu, many=True).data

        response = self.client.get('/restaurant/menu/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)
    