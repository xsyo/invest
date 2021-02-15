from django.urls import path

from .views import (
                        PackageListCreateAPIView, 
                        #PackageRetrieveUpdateDestroyAPIView,
                        JournalListAPIView
                    )



urlpatterns = [
    path('', PackageListCreateAPIView.as_view(), name='packages_list'),
    path('journal/', JournalListAPIView.as_view(), name='journal'),
    #path('<int:pk>/', PackageRetrieveUpdateDestroyAPIView.as_view(), name='packages_rud'),
]