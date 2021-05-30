from tenant.models.user_model import User
from .base_consumer import BaseConsumer


class EchoConsumer(BaseConsumer):
    async def websocket_connect(self, event):
        print("`websocket_connect` is called", event)
        await self.accept()

    async def websocket_receive(self, event):
        user: User = self.scope["user"]
        print(user.__dict__)
        print("`websocket_receive` is called", event)
        print("Username", self.scope["url_route"]["kwargs"].get("userkey"))
        await self.send_text("[Echo] {}".format(self.get_text(event)))

    async def websocket_disconnect(self, event):
        print("`websocket_disconnect` is called", event)
        # Perform clean up code here
