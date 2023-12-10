from django.contrib import admin

from testapp.models import Contract
from testapp.models import LoanApplication
from testapp.models import Manufacturer
from testapp.models import Product


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'manufacturers_id',
        'date_created',
    ]


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'contract',
        'date_created',
    ]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'date_created',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'manufacturer',
        'loan_application',
        'date_created',
    ]
