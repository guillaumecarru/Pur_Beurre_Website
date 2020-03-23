from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser

class UsersAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        self.user = CustomUser.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_create_user_page(self):
        """This test will make sure url 'create_user' works properly"""

        response = self.client.post(reverse('create_user'),
                                    {"username":"test_create_user",
                                     "password1":"azer123",
                                    }
                                   )
        self.assertEqual(response.status_code, 200)

    def test_log_ing_page(self):
        """ This test will make sure url 'log_in' returns the template"""

        response = self.client.get(reverse('log_in'))
        self.assertEqual(response.status_code, 200)

    def test_disconnect_page(self):
        """ this test will make sure url 'user_informations' returns template"""

        response = self.client.get(reverse('disconnect_user'))
        self.assertEqual(response.status_code, 302)


