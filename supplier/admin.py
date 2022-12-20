from django.contrib import admin
from supplier.models import Supplier, Founder


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'auto']
    ordering = ['auto']
    search_fields = ['location']


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age']
    ordering = ['-age']
    search_fields = ['second_name']

