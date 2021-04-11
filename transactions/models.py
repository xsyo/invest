from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator



class Transaction(models.Model):

    TYPE_REFILL = 'R' #пополнение счета
    TYPE_WITHDRAWAL = 'W' # снятие
    
    TYPE_CHOICES = (
        (TYPE_REFILL, 'Refill'),
        (TYPE_WITHDRAWAL, 'Withdrawal'),
    )

    STATUS_SUCCESS = 'S'
    STATUS_PENDING = 'P'
    STATUS_FAILED = 'F'

    STATUS_CHOICES = (
        (STATUS_SUCCESS, 'Success'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_FAILED, 'Failed'),
    )

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='my_transactions')
    transaction_type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_PENDING)
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    cart = models.CharField(max_length=17, validators=[RegexValidator('^\d+$/', message='Строка должна состоять только из цифр')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
