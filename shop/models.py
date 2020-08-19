from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    des = models.TextField(blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категория товара'



class Product(models.Model):

    name = models.CharField(max_length=200)
    des = models.TextField(blank=True)
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'



