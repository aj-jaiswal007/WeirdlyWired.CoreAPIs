from rest_framework import serializers
from weirdlywired.common.base_serializer import BaseSerializer


class UserLoginSerializer(BaseSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
