import json

from django.shortcuts import render
import os
from mainapp.models import ProductCategories, Product

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    content = {
        'title': 'Geekshop'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    goods = [
      {
        'name': 'Худи черного цвета с монограммами adidas Originals',
        'price': 6090,
        'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
        'image': 'vendor/img/products/Adidas-hoodie.png'
      },
      {
        'name': 'Синяя куртка The North Face',
        'price': 23725,
        'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель',
        'image': 'vendor/img/products/Blue-jacket-The-North-Face.png'
      },
      {
        'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
        'price': 3390,
        'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
        'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
      },
      {
        'name': 'Черный рюкзак Nike Heritage',
        'price': 2340,
        'description': 'Плотная ткань. Легкий материал.',
        'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
      },
      {
        'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
        'price': 13590,
        'description': 'Гладкий кожаный верх. Натуральный материал.',
        'image': 'vendor/img/products/Black-Dr-Martens-shoes.png'
      },
      {
        'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
        'price': 2890,
        'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
        'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'
      }
    ]

    categories = [
        {'name': 'Новинки'},
        {'name': 'Одежда'},
        {'name': 'Обувь'},
        {'name': 'Аксессуары'},
        {'name': 'Подарки'}
    ]

    content = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', content)


