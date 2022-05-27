import json

from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render
import os

from django.views.generic import DetailView

from mainapp.models import ProductCategories, Product

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id_category=None, page=1):

    if id_category:
        products_ = Product.objects.filter(category_id=id_category).select_related()
    else:
        products_ = Product.objects.all().select_related('category')

    paginator = Paginator(products_, per_page=2)

    try:
        product_paginator = paginator.page(page)
    except PageNotAnInteger:
        product_paginator = paginator.page(1)
    except EmptyPage:
        product_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': product_paginator
    }

    return render(request, 'mainapp/products.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
