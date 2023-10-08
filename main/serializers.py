from rest_framework import serializers
from main.models import Contacts, Products, Seller


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'


class SellerArrearsSerializer(serializers.ModelSerializer):
    """ Специальный, чтобы нельзя было через API трогать arrears """
    class Meta:
        model = Seller
        exclude = ['arrears']
