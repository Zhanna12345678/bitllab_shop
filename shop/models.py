from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=50, unique=True, verbose_name='product')

    class Meta:
        verbose_name='product'
        verbose_name_plural='product'


class Category(models.Model):
    title=models.CharField(max_length=50, unique=True, verbose_name='prace', )


    class Meta:
        verbose_name='prace'
        verbose_name_plural='prace'

# Create your models here.
