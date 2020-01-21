from django.db import models

class ProductManager(models.Manager):
    def substitute(self, prod_name):

        prod = Product.objects.get(product_name=prod_name)
        # Writing request in sql first
        from django.db import connection
        with connection.cursor as cursor:
            cursor.execute("""SELECT dbproducts_product_categories.product_id AS results
                           FROM dbproducts_product_categories
                           JOIN dbproducts_product
                           ON dbproducts_product_categories.product_id =
                           dbproducts_product.id
                           JOIN dbproducts_category
                           ON dbproducts_product_categories.category_id =
                           dbproducts_category.id
                           WHERE dbproducts_product_categories.category_id IN (
                                SELECT dbproducts_product_categories.category_id FROM
                                dbproducts_product_categories WHERE
                                dbproducts_product_categories.product_id = {})
                           AND dbproducts_product_categories.product_id != {}
                           GROUP BY dbproducts_product_categories.product_id
                           HAVING results >=1
                           ORDER BY results DESC;
                           """.format(prod, prod))
            answer = []
            for raw in cursor.fetchall():
                answer.append(raw)

        return answer


class Category(models.Model):
    """Class that allows a classification of products"""
    name = models.CharField(max_length=100)

class Product(models.Model):
    """Class of product models"""

    id = models.BigIntegerField(primary_key=True)
    product_name = models.CharField(max_length=250)
    img_front_url = models.URLField(max_length=255)
    nutri_grade = models.IntegerField()
    img_nutrition_url = models.URLField(max_length=255)
    web_link = models.URLField(max_length=255)
    categories = models.ManyToManyField("Category")
    # Add manager to Product
    objects = ProductManager()
