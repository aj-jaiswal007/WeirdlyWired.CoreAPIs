from weirdlywired.common.base_view import BaseViewMixin
from rest_framework.views import APIView
from tenant.serializers.user_register import UserRegisterSerializer


class UserRegisterView(APIView, BaseViewMixin):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # Create a new user djang
        serializer = UserRegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return self.bad_request_response(
                message="Invalid request", errors=serializer.errors  # type: ignore
            )

        user = serializer.save()
        return self.data_response(
            message="User created successfully",
            data={"user_id": user.id},  # type: ignore
        )
