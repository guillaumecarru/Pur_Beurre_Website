from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
import requests
from dbproducts.models import Category, Product

from dbproducts.management.commands.related_functions import symbol_removal

class Command(BaseCommand):
    """ This command will populate server. Only use once"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # informations that will be inserted into database
        self.informations_gathered = []
        # id gathered from website, usefull for unicity
        self.id_prod_website = []

    def handle(self, *args, **options):
        """ This function will populate the database"""
        # We first need to gather informations from
        # OpenFoodFacts.

        def gather_informations():
            """This function will gather informations using environment
            variables from django.conf.settings on OpenFoodFacts website and
            store them in self.informations_gathered list"""

            print("gathering informations from Open Food Facts.")

            for num, val in enumerate(settings.PROD_CATEGORIES):
                print("pass : {} / {}".format(num+1, len(settings.PROD_CATEGORIES)))
                # Adding a category to the dictionnary
                settings.SITE_PARAMETERS[settings.TAG_CAT] = val
                req = requests.get(settings.OPEN_FOOD_SITE,
                                   settings.SITE_PARAMETERS).json()
                # Removing useless valors
                req = req["products"]
                # Compting number of products,
                # because Heroku has limitation
                valor_compt = 0

                for prods in req:
                    if prods["_id"] not in self.id_prod_website \
                        and "product_name_fr" in prods and \
                        prods["product_name_fr"] not in \
                        self.informations_gathered:

                        try:
                            self.informations_gathered.append((prods["_id"],
                                                               prods["product_name_fr"],
                                                               # Adding numbers
                                                               # of ASCII for
                                                               # nutrition
                                                               # grade
                                                               ord(prods["nutrition_grades"]),
                                                               prods["url"],
                                                               prods["categories_hierarchy"],
                                                              ))

                            self.id_prod_website.append(prods["_id"])
                            # Adding compts
                            valor_compt += 1
                        except:
                            pass
                        finally:
                            # Marker prevents website from overloading server
                            # with too much products. Heroku limits total
                            # number of lines.
                            if valor_compt == 500:
                                break
            print("{} products gathered from OpenFoodFacts website"\
                  .format(len(self.informations_gathered)))

        def populating_db():
            """This function will populate database with informations gathered
            from gather_informations() function"""

            # Message for admin
            print("Populating database with OpenFoodFacts informations")

            # Marker of sub categories.
            # Will be used to not add them if already inserted in database
            sub_cat = []

            # Inserting product into Products table
            for info_product in self.informations_gathered:
                add_prod = Product.objects.create(id=info_product[0],
                                                  product_name=info_product[1],
                                                  nutri_grade=info_product[2],
                                                  web_link=info_product[3],
                                                 )
                add_prod.save()
                # id of product created, main informations wrote.

                for num_sub_categories in info_product[4]:
                    # Creating a var without symbols, converted for
                    # SQL policy
                    sub_category = symbol_removal(num_sub_categories)

                    if sub_category in sub_cat:
                        pass
                    else:
                        sub_cat.append(sub_category)

                        add_sub_cat = Category.objects.create(name=sub_category)
                        # Then save
                        add_sub_cat.save()

                    #Adding many to many relation between product and category
                    add_prod.categories.add(add_sub_cat)
                    add_prod.save()

        # Running all functions wrote in "handle" Command function
        gather_informations()
        populating_db()
