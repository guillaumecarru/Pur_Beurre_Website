from django.core.management.base import BaseCommand, CommandError

from dbproducts.models import Category, Product

class Command(BaseCommand):
    """ This command will populate server. Only use once"""

    def handle(self, *args, **options):
        print("ok")
