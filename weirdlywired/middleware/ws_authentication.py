from urllib.parse import parse_qsl

from channels.db import DatabaseSyncToAsync
from channels.exceptions import DenyConnection
from rest_framework_simplejwt.tokens import AccessToken

from tenant.models.user_model import User


class WSTokenAuthMiddleWare:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        token = dict(parse_qsl(scope["query_string"].decode())).get("token")
        scope["user"] = await self.get_user(access_token=token)
        return await self.app(scope, receive, send)

    @DatabaseSyncToAsync
    def get_user(self, access_token) -> User:
        """
        Raises rest_framework_simplejwt.exceptions.TokenError if token is not valid
        """
        try:
            assert access_token, "token is required to establish a connection"
            access_token = AccessToken(access_token)
            access_token.verify_token_type()
            access_token.verify()
        except Exception as e:
            raise DenyConnection(str(e))

        return User.objects.get(id=access_token.payload.get("user_id"))
