from car_dealership.models import Car, Car_dealership, Raiting, Category
from django.contrib import admin
from django.db.models import QuerySet


# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'cat']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['change_to_rub']

    @admin.action(description='Изменить валюту выбранных элементов на рубли')
    def change_to_rub(self, request, qs: QuerySet):
        update_cars = qs.update(currency=Currency.RUB)
        self.message_user(
            request,
            f'Обновлено {update_cars} записей',
            messages.SUCCES
        )


@admin.register(Car_dealership)
class Car_dealershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    ordering = ['name']
    search_fields = ['title__istartwith']


@admin.register(Raiting)
class RaitingAdmin(admin.ModelAdmin):
    list_display = ['car', 'value']
    ordering = ['value']
    search_fields = ['value']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    actions = ['passenger_car']

    @admin.action(description='Изменить категорию элементов на легковые')
    def passenger_car(self, request, qs: QuerySet):
        update_cars = qs.update(passenger_car=Category.Passenger_car)
        self.message_user(
            request,
            f'Обновлено {update_cars} записей',
            messages.SUCCES
        )
