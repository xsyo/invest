from django.urls import path

from .views import WithdrawalRequestAPIView



urlpatterns = [
    path('', WithdrawalRequestAPIView.as_view(), name='withdrawal_request'),    
]