from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from main.models import Contacts, Products, Seller
from main.paginators import ContactsPaginator, ProductsPaginator, SellerPaginator
from main.serializers import ContactsSerializer, ProductsSerializer, SellerSerializer, SellerArrearsSerializer
from main.permissions import ModeratorsPermissions, UsersPermissions
from users.models import UserGroups


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

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or (user.role == UserGroups.MODERATORS):
            return Seller.objects.all()
        else:
            return Seller.objects.filter(author=user)


class SellerRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = SellerArrearsSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = SellerPaginator


class SellerUpdateApiView(generics.UpdateAPIView):
    serializer_class = SellerArrearsSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = SellerPaginator


class SellerDeleteApiView(generics.DestroyAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
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

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or (user.role == UserGroups.MODERATORS):
            return Contacts.objects.all()
        else:
            return Contacts.objects.filter(author=user)


class ContactsRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = ContactsPaginator


class ContactsUpdateApiView(generics.UpdateAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = ContactsPaginator


class ContactsDeleteApiView(generics.DestroyAPIView):
    serializer_class = ContactsSerializer
    queryset = Contacts.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
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

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or (user.role == UserGroups.MODERATORS):
            return Products.objects.all()
        else:
            return Products.objects.filter(author=user)


class ProductsRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = ProductsPaginator


class ProductsUpdateApiView(generics.UpdateAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = ProductsPaginator


class ProductsDeleteApiView(generics.DestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [IsAuthenticated | ModeratorsPermissions | UsersPermissions]
    pagination_class = ProductsPaginator


