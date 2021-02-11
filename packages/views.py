from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from users.permissions import IsAdminOrReadOnly
from .models import Package
from .serializers import PackageSerializer



class PackageListCreateAPIView(generics.ListCreateAPIView):

    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (IsAdminOrReadOnly,)



class PackageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = (IsAdminUser,)
    