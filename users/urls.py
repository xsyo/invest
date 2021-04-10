from django.urls import path

from .views import ReferralCodeAPIView



urlpatterns = [
    path('referral_code/', ReferralCodeAPIView.as_view(), name='referral_code'), 
]