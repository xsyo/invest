from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

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