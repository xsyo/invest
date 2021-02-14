from djoser import serializers as djoser_serializers
from djoser.conf import settings

from .models import User


class UserSerializer(djoser_serializers.UserSerializer):

    class Meta:

        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.USER_ID_FIELD,
            settings.LOGIN_FIELD,
            'is_active',
            'balance',
        )
        read_only_fields = (settings.LOGIN_FIELD, 'is_active', 'balance')
