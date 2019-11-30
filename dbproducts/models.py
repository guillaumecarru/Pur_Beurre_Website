from django.db import models

class Category(models.Model):
    """Class that allows a classification of products"""
    name = models.CharField(max_length=100)

class Product(models.Model):
    """Class of product models"""

    id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=150)
    nutri_grade = models.IntegerField()
    web_link = models.URLField()
    categories = models.ManyToManyField("Category",
                                       )
