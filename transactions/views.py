from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionForWithdrawalSerializer



class WithdrawalRequestAPIView(generics.CreateAPIView):

    serializer_class = TransactionForWithdrawalSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            transaction_type=Transaction.TYPE_WITHDRAWAL,
            status=Transaction.STATUS_PENDING
        )