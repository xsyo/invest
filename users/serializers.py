from djoser import serializers as djoser_serializers
from djoser.conf import settings
from rest_framework import serializers

from .models import User
from .utils import get_inviting_user


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
        ref_name = 'User 1'


class CreateUserSerializer(djoser_serializers.UserCreateSerializer):

    inviting_code = serializers.CharField(write_only=True)

    class Meta(djoser_serializers.UserCreateSerializer.Meta):
        fields = djoser_serializers.UserCreateSerializer.Meta.fields + ('inviting_code',)

    def validate(self, attrs):
        code = attrs.pop('inviting_code', None)
        attrs = super().validate(attrs)
        attrs['inviting_code'] = code
        return attrs

    def perform_create(self, validated_data):
        code = validated_data.pop('inviting_code', None)
        user = super().perform_create(validated_data)
        inviting_user = get_inviting_user(code)
        if inviting_user:
            user.inviting = inviting_user
            user.save()
        return user
