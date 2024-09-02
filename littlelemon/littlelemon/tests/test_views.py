from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')  # Login the user

        self.menu_item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = Menu.objects.create(title="Pizza", price=120, inventory=50)
        self.menu_item3 = Menu.objects.create(title="Burger", price=60, inventory=75)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'))  

        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)