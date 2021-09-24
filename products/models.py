from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, default='')
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256, db_index=True, unique=True, verbose_name='имя продукта')
    image = models.ImageField(upload_to='product_images', blank=True)
    description = models.TextField(blank=True, verbose_name='описание продукта')
    price = models.DecimalField(max_digits=8, verbose_name='цена продукта', decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=10, verbose_name='количество на складе')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name} ({self.category.name})'

