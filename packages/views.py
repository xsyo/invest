from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.http import Http404

from users.permissions import IsAdminOrReadOnly
from .models import Package, Journal
from .serializers import PackageSerializer, JournalSerializer
from .pagination import JournalPagination



class PackageListCreateAPIView(generics.ListCreateAPIView):
    """
        Список пакетов

        Может смотреть каждый
        Добавлять новые пакеты только админ
    """

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (IsAdminOrReadOnly,)



class MyPackageAPIView(generics.RetrieveAPIView):

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        user = self.request.user
        packages = self.filter_queryset(self.get_queryset())
        user_package = None
        for package in packages:
            max_val = package.max_value if package.max_value else float('inf')

            if package.min_value < user.balance and user.balance < max_val:
                user_package = package
        if user_package is not None:
            return user_package
        else:
            raise Http404("Package does not exist")


# class PackageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Package.objects.all()
#     serializer_class = PackageSerializer
#     permission_classes = (IsAdminUser,)



class JournalListAPIView(generics.ListAPIView):
    '''
        Журнал
        
        Пользователь может смотреть только свой журнал
    '''

    serializer_class = JournalSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = JournalPagination

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)