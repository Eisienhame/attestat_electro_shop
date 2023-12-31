from django.contrib import admin
from main.models import Products, Contacts, Seller


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')
    list_filter = ['country']
    search_fields = ['city']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'contacts', 'products', 'supplier', 'arrears', 'author')
    list_filter = ['contacts']

    def products(self, row):
        return ','.join([x.product for x in row.products.all()])
