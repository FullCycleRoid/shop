from django.db import models


# Модель категории
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductByCategory', args=[self.slug])


# Модель продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name='Изображение товара', default='static/img/no-image.jpg')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.slug, self.id])

