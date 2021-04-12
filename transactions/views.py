from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum

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


class SumAPIView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        transactions = request.user.my_transactions.all()
        refill_transactions = transactions.filter(
            transaction_type=Transaction.TYPE_REFILL, 
            status=Transaction.STATUS_SUCCESS
            )
        withdrawal_transactions = transactions.filter(
            transaction_type=Transaction.TYPE_WITHDRAWAL, 
            status=Transaction.STATUS_SUCCESS
            )
        refill_sum = refill_transactions.aggregate(refill_sum=Sum('amount'))['refill_sum']
        withdrawal_sum = withdrawal_transactions.aggregate(withdrawal_sum=Sum('amount'))['withdrawal_sum']
        return Response({
            'refill_sum': refill_sum,
            'withdrawal_sum': withdrawal_sum
        })