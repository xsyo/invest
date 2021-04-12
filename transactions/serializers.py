from decimal import Decimal

from rest_framework import serializers
from django.db.models import Sum

from .models import Transaction



class TransactionForWithdrawalSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'transaction_type', 'status', 'amount', 'cart', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'transaction_type', 'status', 'created_at', 'updated_at')

    def validate_cart(self, value):

        if len(value) == 16:
            return value
        else:
            raise serializers.ValidationError("Неверный номер карты")
    
    
    def validate_amount(self, value):
        user = self.context['request'].user

        user_amount_sum = (user
                       .my_transactions
                       .filter(transaction_type=Transaction.TYPE_WITHDRAWAL, status=Transaction.STATUS_PENDING)
                       .aggregate(amount_sum=Sum('amount'))
                       ['amount_sum'])
        user_amount_sum = user_amount_sum if user_amount_sum else 0

        if user.balance - user_amount_sum < Decimal(value):
            raise serializers.ValidationError("Недостаточно средств")

        return value