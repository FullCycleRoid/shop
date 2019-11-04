from django.db import models
from shop.models import Product
# Create your models here.


# Информация пользователя для оформления заказа и доставки товара
class Order(models.Model):
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    second_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.IntegerField( verbose_name='Телефон')
    city = models.CharField(max_length=30, verbose_name='Город')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    delivery_date = models.DateTimeField(verbose_name='Дата доставки')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.second_name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


# Полная информация об оформлении заказа
class OrderItem(models.Model):
    product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name='Личные данные', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Стоимость',default=0)


    def __str__(self):
        return 'Заказ: {}'.format(self.id)