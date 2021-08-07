import json
from chat.enums.model_enums import RoomType
from tenant.models.user_model import User
from websocket.dtos.msg_event import MessageEvent

from .base_consumer import BaseConsumer


class EchoConsumer(BaseConsumer):
    async def connect(self):
        print("`websocket_connect` is called", self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        user: User = self.scope["user"]
        msg = MessageEvent(
            sender=user,
            content=text_data,
            receiver_id="bot",
            receiver_type=RoomType.PERSONAL,
        )
        await self.send(text_data=msg.text)
        echo_msg = {
            "sender_name": "bot",
            "sender_id": "bot",
            "content": f"[Echo] {text_data}",
            "receiver_id": user.id,
            "receiver_type": RoomType.PERSONAL.value,
        }
        await self.send_to_channel(
            channel_name=self.channel_name,
            event_type="echo.message",
            text_data=json.dumps(echo_msg),
        )

    async def echo_message(self, event):
        await self.send(text_data=event["text"])

    async def disconnect(self, close_code):
        print("`disconnect` is called", close_code)
