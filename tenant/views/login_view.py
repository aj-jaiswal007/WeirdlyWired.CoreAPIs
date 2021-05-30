from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from tenant.serializers.user_serializer import (
    UserBasicInfoSerializer,
    UserLoginSerializer,
)
from weirdlywired.authentication import expires_in, token_expire_handler
from weirdlywired.common.base_view import BaseView


class LoginView(BaseView):
    permission_classes = (AllowAny,)

    def post(self, request):
        """Authenticates username password and returns token"""
        login_serializer = UserLoginSerializer(data=request.data)
        if not login_serializer.is_valid():
            return self.bad_request_response(message=login_serializer.errors)

        user = authenticate(
            username=login_serializer.data["username"],
            password=login_serializer.data["password"],
        )
        if not user:
            return self.not_found_response(
                message="User not found - please check your credentials"
            )

        token, _ = Token.objects.get_or_create(user=user)
        (_, token) = token_expire_handler(token=token)

        return self.data_response(
            message="Verification successful",
            data={
                "user": UserBasicInfoSerializer(instance=user).data,
                "expires_in": expires_in(token=token).total_seconds(),
                "token": token.key,
            },
        )
