from urllib.parse import parse_qs

from channels.db import database_sync_to_async

from tenant.models.user_model import User
from weirdlywired.authentication import verify_token_key


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
        # return await inner()

    @database_sync_to_async
    def get_user(self) -> User:
        token_key = parse_qs(self.scope["query_string"].decode("utf8")).get("token")[0]
        user, _ = verify_token_key(key=token_key)
        return user
