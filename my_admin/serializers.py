from rest_framework import serializers

from transactions.models import Transaction



class TransactionUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = ('id', 'user', 'transaction_type', 'status', 'amount', 'cart', 'created_at', 'updated_at')
        read_only_fields = ('id', 'user', 'transaction_type', 'amount', 'cart', 'created_at', 'updated_at')