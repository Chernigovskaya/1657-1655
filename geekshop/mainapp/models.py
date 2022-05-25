from django.db import models
''' models for product and category '''

# Create your models here.
# ''' model category '''

class ProductCategories(models.Model):
    name = models.CharField(max_length=64, unique=True)
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


'''model for product'''


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images', blank=True)
    descriptions = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category}'




