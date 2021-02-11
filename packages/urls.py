from django.urls import path

from .views import PackageListCreateAPIView, PackageRetrieveUpdateDestroyAPIView



urlpatterns = [
    path('', PackageListCreateAPIView.as_view(), name='packages_list'),
    path('<int:pk>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='packages_rud'),
]