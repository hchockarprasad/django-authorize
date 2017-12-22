from django.urls import reverse

from django.test import TestCase

from rest_framework.test import APITestCase

from rest_framework import status

from authorize.models import Menu


class MenuTestCase(TestCase):

    def test_create_menu(self):

        new_menu = Menu.objects.create(name='Menu 001', code='menu001')

        self.assertEqual(new_menu.name, 'Menu 001')


class MenuAPITestCase(APITestCase):

    def test_list_menu(self):
        """
        Ensure we can list menu objects.
        """
        url = reverse('menu_list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Menu.objects.count(), 0)
