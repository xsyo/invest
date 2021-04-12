from django.urls import path

from .views import WithdrawalRequestAPIView, TransactionListAPIView, SumAPIView



urlpatterns = [
    path('withdrawal/', WithdrawalRequestAPIView.as_view(), name='withdrawal_request'),
    path('statistic/', SumAPIView.as_view(), name='statistic'),
    path('', TransactionListAPIView.as_view(), name='transaction_list'),
]