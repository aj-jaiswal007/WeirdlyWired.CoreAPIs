from rest_framework import serializers
from tenant.models.user_model import User


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def validate(self, data):
        """
        Check if password and confirm_password match.
        """
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError(
                "Password and confirm_password do not match."
            )
        email = data.get("email")
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("User already exists")

        if User.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError("Username already exists")

        return super().validate(data)  # Call base class's validate method

    def create(self, validated_data):
        user, created = User.objects.get_or_create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
