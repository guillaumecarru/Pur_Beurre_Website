from django.db import models

# Create your models here.

# Model of products
class Product(models.Model):
    """Class of product models"""
    id_product = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=150)
    nutri_grade = models.CharField(max_length=1)
    web_link = models.URLField()
    categories = models.ManyToManyField('Category', related_name="products")

class Category(models.Model):
    name=models.CharField(max_length=100)
