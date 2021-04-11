from django.urls import path

from .views import (
                        PackageListCreateAPIView, 
                        #PackageRetrieveUpdateDestroyAPIView,
                        JournalListAPIView,
                        MyPackageAPIView,
                    )



urlpatterns = [
    path('', PackageListCreateAPIView.as_view(), name='packages_list'),
    path('journal/', JournalListAPIView.as_view(), name='journal'),
    path('my/', MyPackageAPIView.as_view(), name='my_package'),
    #path('<int:pk>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='packages_rud'),
]