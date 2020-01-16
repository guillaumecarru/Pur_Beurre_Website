from django.db import models

class ProductManager(models.Manager):
    def substitute(self, prod_name):

        prod = Product.objects.get(product_name=prod_name)
        
        # Continuer à partir de : "Spanning multi-valued relationship"

        # 0. Récupérer le nutri grade du produit de base et le stocker dans une
        # variable
        #
        # nutri_product = Product.objects.get(id = 3095757370015)
        # nutri_product = nutri_product.nutri_grade

        # 1. Algo de récup de l'id category dont l'id de la table intermédiaire
        # est le plus fort (la ou la pertinence est la plus élevée en terme de
        # relation produit
        #
        # Récupérer le nombre de sous produits du produit pour la loop PUIS
        #
        # On peut faire -1, -2, etc.
        # SELECT category_id FROM dbproducts_product_categories WHERE id=(SELECT MAX(id)-2 FROM dbproducts_product_categories WHERE product_id=3095757370015);

        # 2. Algo de récup de l'id des PRODUITS dont le nutri grade est
        # inférieur ou égal au nutri_grade du produit de base ET qui est dans
        # la même sous-catégorie que le produit de base
        #
        # SELECT dbproducts_product.id FROM dbproducts_product
        # JOIN dbproducts_product_categories ON (dbproducts_product.id = dbproducts_product_categories.product_id) 
        # JOIN dbproducts_category ON (dbproducts_category.id = dbproducts_product_categories.category_id) 
        # WHERE dbproducts_product_categories.category_id = 5
        # AND dbproducts_product.nutri_grade <= nutri_product; #le nutriscore du
        # produit de base

        #
        # Exemple de connexion à la base de données. Exemple django
        #from django.db import connection
        #with connexion.cursor as cursor:
        #    cursor.execute("""
        #                   SELECT product_name FROM dbproducts_product WHERE
        #                   id= {}""".format(id_prod))
        #    p = cursor.fetchall()

        # SELECTIONNER L'ID de la categorie de la ligne intermédiaire
        # On peut faire -1, -2, etc.
        # SELECT category_id FROM dbproducts_product_categories WHERE id=(SELECT MAX(id)-2 FROM dbproducts_product_categories WHERE product_id=3095757370015);

        # Exemple que j'ai fait pour savoir si l'on peut appeler Product ici
    def blah(self):
        # cette fonction va servir de test pour voir si l'on peut récupérer le
        # nombre de sous catégories d'un produit et le stocker dans une
        # variable
        #
        # SELECT COUNT(*) FROM dbproducts_product_categories WHERE product_id = 7613034926814;

        from django.db import connection
        with connection.cursor as cursor:
            cursor.execute("""SELECT COUNT(*) FROM dbproducts_product_categories WHERE product_id = 7613034926814;""")
            answer=[]
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
