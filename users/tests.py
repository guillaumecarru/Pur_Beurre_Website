from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

class FavoritesAppTestCase(TestCase):
    def test_create_user_page(self):
        """This test will make sure url 'create_user' works properly"""
        response = self.client.get(reverse('create_user'))
        self.assertEqual(response.status_code, 200)

    def test_log_ing_page(self):
        """ This test will make sure url 'log_in' returns the template"""

        response = self.client.get(reverse('log_in'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        """Creating data used with those tests"""
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    #def test_log_out_page(self):
    #    """ This test will make sure url 'disconnect_user' returns the template"""
#
#        response = self.client.get(reverse('disconnect_user'))
#        self.assertEqual(response.status_code, 200)
