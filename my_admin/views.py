from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from transactions.models import Transaction
from transactions.serializers import TransactionForWithdrawalSerializer
from transactions.pagination import TransactionPagination

from packages.models import Package, Journal
from packages.serializers import PackageSerializer, JournalSerializer
from packages.pagination import JournalPagination

from users.models import User
from users.serializers import UserSerializer
from users.pagination import UserPagination

from .serializers import TransactionUpdateSerializer



class TransactionListAPIView(generics.ListAPIView):
    '''
        Транзакций

        Список всех транзакций
        Разрешение: Админ
    '''

    queryset = Transaction.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = TransactionForWithdrawalSerializer
    pagination_class = TransactionPagination
    filterset_fields = ['user', 'transaction_type', 'status']



class TransactionRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    '''
        Endpoint для подтверждения запроса на снятие денег

        Разрешение: Админ
    '''

    queryset = Transaction.objects.filter(status=Transaction.STATUS_PENDING, 
                                        transaction_type=Transaction.TYPE_WITHDRAWAL)
    serializer_class = TransactionUpdateSerializer
    permission_classes = (IsAdminUser,)

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == Transaction.STATUS_SUCCESS:
            user = instance.user
            user.balance -= instance.amount
            user.save()



class PackageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    '''
        Пакет

        Просмотр или редактирование пакета
        Разрешение: Админ
    '''

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (IsAdminUser,)



class JournalListAPIView(generics.ListAPIView):
    '''
        Журнал

        Разрешение: Админ
    '''

    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = JournalPagination


class UserListAPIView(generics.ListAPIView):
    '''
        Список пользователей

        Разрешение: Админ
    '''

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    pagination_class = UserPagination