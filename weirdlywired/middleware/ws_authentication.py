from urllib.parse import parse_qsl

from channels.db import database_sync_to_async
from rest_framework_simplejwt.tokens import AccessToken

from tenant.models.user_model import User


class WSTokenAuthMiddleWare:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        return WSTokenAuthMiddleWareInstance(scope, self)


class WSTokenAuthMiddleWareInstance:
    def __init__(self, scope, middleware) -> None:
        self.scope = dict(scope)
        self.inner = middleware.inner

    async def __call__(self, receive, send):
        self.scope["user"] = await self.get_user()
        return await self.inner(self.scope, receive, send)

    @database_sync_to_async
    def get_user(self) -> User:
        """
        Raises rest_framework_simplejwt.exceptions.TokenError if token is not valid
        """
        access_token = dict(parse_qsl(self.scope["query_string"].decode())).get("token")
        assert access_token, "token is required to establish a connection"
        access_token = AccessToken(access_token)
        access_token.verify_token_type()
        access_token.verify()
        return User.objects.get(id=access_token.payload.get("user_id"))
