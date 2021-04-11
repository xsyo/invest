from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .utils import get_referral_code
from packages.models import Package


class ReferralCodeAPIView(APIView):
    '''
    Дает код для реферальной ссылки
    '''
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        code = get_referral_code(request.user)
        return Response({'code': code})