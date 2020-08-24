from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField('Товар', max_length=200)
    des = models.TextField('Описание', blank=True)
    category = models.ForeignKey('Category', blank=True, null=True, default=None, on_delete=models.SET_NULL, verbose_name = 'Категория')
    is_active = models.BooleanField('В наличии', default=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Категория', max_length=200)
    des = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товара'


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказ'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images/')
    des = models.CharField(max_length=64, blank=True, null=True, default=None)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.image

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'




