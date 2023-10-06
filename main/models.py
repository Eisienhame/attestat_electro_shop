from django.db import models
from users.models import User
from datetime import datetime, date
from decimal import Decimal

NULLABLE = {'null': True, 'blank': True}


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома', **NULLABLE)


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    release_date = models.DateField(default=date.today, verbose_name='Дата выхода продукта на рынок')


class Seller(models.Model):
    CHOICES_STATUS = [
        ('Factory', 'Завод'),
        ('Retail_network', 'Розничная сеть'),
        ('Individual_entrepreneur', 'Индивидуальный предприниматель')
    ]

    name = models.CharField(max_length=150, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты', **NULLABLE)
    products = models.ManyToManyField(Products, on_delete=models.CASCADE, verbose_name='Продукты', **NULLABLE)
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)
    arrears = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00'))
    create_time = models.TimeField(default=datetime.now, verbose_name='Время создания')

