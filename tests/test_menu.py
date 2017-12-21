from django.test import TestCase

from authorize.models import Menu


class MenuTestCase(TestCase):

    def test_create_menu(self):

        new_menu = Menu.objects.create(name='Menu 001', code='menu001')

        self.assertEqual(new_menu.name, 'Menu 001')
