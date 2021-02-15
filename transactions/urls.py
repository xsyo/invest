from django.urls import path

from .views import WithdrawalRequestAPIView, TransactionListAPIView



urlpatterns = [
    path('withdrawal/', WithdrawalRequestAPIView.as_view(), name='withdrawal_request'),
    path('', TransactionListAPIView.as_view(), name='transaction_list'),   
]