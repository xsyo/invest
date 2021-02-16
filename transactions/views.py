from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionForWithdrawalSerializer
from .pagination import TransactionPagination



class WithdrawalRequestAPIView(generics.CreateAPIView):
    """
        Endpoint для заявки на снятие баланса
        Разрешение: Авторизация
    """

    serializer_class = TransactionForWithdrawalSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            transaction_type=Transaction.TYPE_WITHDRAWAL,
            status=Transaction.STATUS_PENDING
        )


class TransactionListAPIView(generics.ListAPIView):
    """
        Список совершенных транзакции
        Можно фильтровать по статусу и по типу

        Разрешение: Авторизация
    """

    serializer_class = TransactionForWithdrawalSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = TransactionPagination
    filterset_fields = ['transaction_type', 'status']

    def get_queryset(self):
        return self.request.user.my_transactions.all()