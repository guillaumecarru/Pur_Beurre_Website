from django.test import TestCase

from ..models import Product

class ProductModelTest(TestCase):
    def create_product(self,
                       product_name="test_product",
                       id_product=123545654,
                       img_front_url="url.com",
                       nutri_grade=97,
                       img_nutrition_url="google.com",
                       web_link="yup.com"):
        return Product.objects.create(product_name=product_name,
                                      id=id_product,
                                      img_front_url=img_front_url,
                                      nutri_grade=nutri_grade,
                                      img_nutrition_url=img_nutrition_url,
                                      web_link=web_link)

    def test_product_representation(self):
        entry = self.create_product()
        self.assertTrue(isinstance(entry, Product))
