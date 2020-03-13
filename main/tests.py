from django.test import TestCase
from django.urls import reverse

class MainAppTestCase(TestCase):
    def test_index_page(self):
        """ This test will make sure url 'homepage' returns the template"""
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_copyright_page(self):
        """ This test will make sure url 'copyright' returns the template"""
        response = self.client.get(reverse('copyright'))
        self.assertEqual(response.status_code, 200)
