from django.db import models

from django_countries import Countries

from core.enums.car_dealership_enums import Currency, StatusofCar
from core.validators import check_raiting
from core.abstract_models import Abstract


# Create your models here.
class Car(Abstract):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year = models.IntegerField()
    price = models.IntegerField(default=10000)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )

    status = models.CharField(
        max_length=255,
        choices=StatusofCar.choices,
        default=StatusofCar.Available
    )

    class Meta:
        ordering = ['title']
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return self.title


class Category(Abstract):
    name = models.CharField(max_length=255, default='Легковые')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Raiting(Abstract):
    value = models.IntegerField(validators=[check_raiting], default=1)
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name='raiting'
    )

    class Meta:
        ordering = ['value']
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

    def __str__(self):
        return self.car


class Car_dealership(Abstract):
    name = models.CharField(max_length=255)
    characteristic = models.TextField(blank=True)
    location = Countries()
    contact = models.EmailField()
    cars = models.ForeignKey(
        Car,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Автосалон'
        verbose_name_plural = 'Автосалоны'

    def __str__(self):
        return self.name

