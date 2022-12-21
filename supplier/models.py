from core.abstract_models import Abstract
from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Supplier(Abstract):
    name = models.CharField(max_length=255)
    location = CountryField()
    contact = models.EmailField()
    auto = models.CharField(max_length=255)
    reviews = models.TextField(blank=True)
    found = models.ForeignKey(
        'Founder',
        on_delete=models.PROTECT,
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.name


class Founder(Abstract):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    age = models.IntegerField()
    company = models.CharField(max_length=255)

    class Meta:
        ordering = ['second_name']
        verbose_name = 'Основатель'
        verbose_name_plural = 'Основатели'

    def __str__(self):
        return self.second_name
