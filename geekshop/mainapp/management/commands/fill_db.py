import json
from django.core.management.base import BaseCommand
from mainapp.models import Product, ProductCategories


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('mainapp/fixtures/cat.json')
        ProductCategories.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = ProductCategories(**cat)
            new_category.save()

        products = load_from_json('mainapp/fixtures/products.json')
        ProductCategories.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            prod['category'] = ProductCategories.objects.get(id=category)
            new_category = ProductCategories(**prod)
            new_category.save()

