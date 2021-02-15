from django.urls import path

from .views import (TransactionListAPIView, 
                    TransactionRetrieveUpdateAPIView,
                    PackageRetrieveUpdateDestroyAPIView,
                    JournalListAPIView,
                    UserListAPIView
                   )



urlpatterns = [
    path('transactions/', TransactionListAPIView.as_view(), name='transactions_list_admin'),
    path('transactions/<int:pk>/', TransactionRetrieveUpdateAPIView.as_view(), name='transaction_update_admin'),
    path('package/<int:pk>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='package_detail_admin'),
    path('journals/', JournalListAPIView.as_view(), name='journals_list_admin'),
    path('users/', UserListAPIView.as_view(), name='users_list_admin'),
]