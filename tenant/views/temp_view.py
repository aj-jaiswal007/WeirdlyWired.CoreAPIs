from weirdlywired.common.base_view import BaseView
from rest_framework_simplejwt.tokens import AccessToken


class TempView(BaseView):
    def get(self, request):
        try:
            access_token = request.GET.get("token")
            assert access_token, "Please pass a `token` in query params"
            access_token = AccessToken(token=access_token)
            access_token.verify()
            access_token.verify_token_type()

            return self.data_response(
                message="Test success!",
                data="Hello {}! Your token is valid".format(
                    request.GET.get("name") or "Guest"
                ),
            )
        except Exception as e:
            print("---------Type of exception", type(e))
            return self.bad_request_response(message=str(e))
