from django.contrib import admin
from models import Products, Contacts, Seller


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacts', 'products', 'supplier', 'arrears', 'author')

    def products(self, row):
        return ','.join([x.product for x in row.products.all()])
