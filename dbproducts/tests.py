from django.test import TestCase
from django.urls import reverse
from dbproducts.models import Product

class FavoritesAppTestCase(TestCase):
    def setUp(self):
        """Creating data used with those tests"""
        fake_product = Product.objects.create(id=598745601, \
                                              product_name="cacahuètes au chocolat", \
                                              img_front_url="img_url.com", \
                                              nutri_grade=100, \
                                              img_nutrition_url="link_nutri.com", \
                                              web_link="link_openfoodfact.com", \
                                             )

        self.product_tested = Product.objects.get(id=598745601)

    def test_consult_favorites_page(self):
        """ This test will make sure url 'consult_favorites' returns the template"""

        product_id = self.product_tested.id
        response = self.client.get(reverse('detail', args=(product_id,)))
        self.assertEqual(response.status_code, 200)
