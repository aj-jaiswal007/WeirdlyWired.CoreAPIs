from rest_framework import serializers
from weirdlywired.common.base_serializer import BaseSerializer
from tenant.models.user_model import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class UserBasicInfoSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "key",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "profile_info",
        )
