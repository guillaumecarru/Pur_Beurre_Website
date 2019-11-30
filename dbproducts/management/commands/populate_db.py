from django.core.management.base import BaseCommand, CommandError

from django.conf import settings
import requests
from dbproducts.models import Category, Product

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

        gather_informations()
