from main.apps import MainConfig
from django.urls import path
from main.views import SellerCreateApiView, SellerListApiView, SellerDeleteApiView, SellerUpdateApiView, \
    SellerRetrieveApiView, ProductsUpdateApiView, ProductsRetrieveApiView, ProductsDeleteApiView, ProductsCreateApiView, \
    ProductsListApiView, ContactsUpdateApiView, ContactsRetrieveApiView, ContactsDeleteApiView, ContactsCreateApiView, \
    ContactsListApiView

app_name = MainConfig.name


urlpatterns = [

    path('seller/', SellerListApiView.as_view(), name='seller_list'),
    path('seller/create/', SellerCreateApiView.as_view(), name='seller_create'),
    path('seller/delete/<int:pk>/', SellerDeleteApiView.as_view(), name='seller_delete'),
    path('seller/<int:pk>/', SellerRetrieveApiView.as_view(), name='seller_detail'),
    path('seller/update/<int:pk>/', SellerUpdateApiView.as_view(), name='seller_update'),
    path('products/', ProductsListApiView.as_view(), name='product_list'),
    path('products/create/', ProductsCreateApiView.as_view(), name='product_create'),
    path('products/delete/<int:pk>/', ProductsDeleteApiView.as_view(), name='product_delete'),
    path('products/<int:pk>/', ProductsRetrieveApiView.as_view(), name='product_detail'),
    path('products/update/<int:pk>/', ProductsUpdateApiView.as_view(), name='product_update'),
    path('contacts/', ContactsListApiView.as_view(), name='contacts_list'),
    path('contacts/create/', ContactsCreateApiView.as_view(), name='contacts_create'),
    path('contacts/delete/<int:pk>/', ContactsDeleteApiView.as_view(), name='contacts_delete'),
    path('contacts/<int:pk>/', ContactsRetrieveApiView.as_view(), name='contacts_detail'),
    path('contacts/update/<int:pk>/', ContactsUpdateApiView.as_view(), name='contacts_update'),

]
