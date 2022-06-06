

from django.core.management.base import BaseCommand
from django.db.models import Q
from mainapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # product = Product.objects.filter(
        #     Q(category__name='Обувь') | Q(id=5)
        # ) и
        # product = Product.objects.filter(
        #     Q(category__name='Обувь') & Q(id=5)
        # ) или
        # product = Product.objects.filter(
        #      ~Q(category__name='Обувь')
        #  ) не
        product = Product.objects.filter(
            Q(category__name='Обувь'), id=5)

        print(product)
