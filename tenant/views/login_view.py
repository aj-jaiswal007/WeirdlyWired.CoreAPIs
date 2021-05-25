from weirdlywired.common.base_view import BaseView
from rest_framework.permissions import AllowAny


class LoginView(BaseView):
    permission_classes = (AllowAny,)

    def post(self, request):
        # TODO: Implement expiry token based auth
        pass
