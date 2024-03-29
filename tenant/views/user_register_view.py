from weirdlywired.common.base_view import BaseView
from tenant.models.user_model import User


class UserRegisterView(BaseView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # Create a new user djang
        request_data = request.data
        user_name = request_data.get("username", None)
        user_pass = request_data.get("password", None)
        user_mail = request_data.get("email", None)
        user, created = User.objects.get_or_create(username=user_name, email=user_mail)
        user.set_password(user_pass)
        user.save()
        return self.data_response(
            message="User created successfully",
            data={"user_id": user.id, "created": created},
        )
