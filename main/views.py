from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from main.models import Contacts, Products, Seller
from main.paginators import ContactsPaginator, ProductsPaginator, SellerPaginator
from main.serializers import ContactsSerializer, ProductsSerializer, SellerSerializer, SellerArrearsSerializer


class SellerCreateApiView(generics.CreateAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SellerPaginator

    def perform_create(self, serializer):
        """Сохраняет новому объекту владельца"""
        serializer.save(author=self.request.user)


class SellerListApiView(generics.ListAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SellerPaginator


class SellerRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SellerArrearsSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SellerPaginator


class SellerUpdateApiView(generics.UpdateAPIView):
    serializer_class = SellerArrearsSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SellerPaginator


class SellerDeleteApiView(generics.DestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = SellerPaginator


class ContactsCreateApiView(generics.CreateAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContactsPaginator


class ContactsListApiView(generics.ListAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContactsPaginator


class ContactsRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContactsPaginator


class ContactsUpdateApiView(generics.UpdateAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContactsPaginator


class ContactsDeleteApiView(generics.DestroyAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ContactsPaginator


class ProductsCreateApiView(generics.CreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ProductsPaginator


class ProductsListApiView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ProductsPaginator


class ProductsRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ProductsPaginator


class ProductsUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ProductsPaginator


class ProductsDeleteApiView(generics.DestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ProductsPaginator


