from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

class FavoritesAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_consult_favorites_page(self):
        """ This test will make sure url 'consult_favorites' returns the template"""

        response = self.client.get(reverse('consult_favorites'))
        self.assertEqual(response.status_code, 200)
