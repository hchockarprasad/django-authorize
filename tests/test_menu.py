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
        url = reverse('menu-list')

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Menu.objects.count(), 0)

    def test_create_menu(self):
        """
        Ensure we can create menu objects.
        """
        url = reverse('menu-create')

        response = self.client.post(url, {'name': 'testmenu', 'code': 'm000'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(Menu.objects.count(), 1)

        self.assertEqual(Menu.objects.get().name, 'testmenu')

    def test_detail_menu(self):
        """
        Ensure we can get menu details.
        """
        create_url = reverse('menu-create')

        list_url = reverse('menu-detail', kwargs={'pk': 1})

        self.client.post(create_url, {'name': 'testmenu', 'code': 'm000'}, format='json')

        response = self.client.get(list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_menu(self):
        """
        Ensure we can update menu objects.
        """
        create_url = reverse('menu-create')

        update_url = reverse('menu-update', kwargs={'pk': 1})

        self.client.post(create_url, {'name': 'testmenu', 'code': 'm000'}, format='json')

        response = self.client.put(update_url, {'name': 'testmenunew', 'code': 'm000'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_menu(self):
        """
        Ensure we can delete menu objects.
        """
        create_url = reverse('menu-create')

        delete_url = reverse('menu-delete', kwargs={'pk': 1})

        self.client.post(create_url, {'name': 'testmenu', 'code': 'm000'}, format='json')

        response = self.client.delete(delete_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
