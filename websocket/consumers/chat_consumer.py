import json
from websocket.models.user_channel_model import UserChannel
from websocket.utils.user_channel_utils import UserChannelUtils
from tenant.models.user_model import User
from websocket.dtos.msg_event import MessageEvent

from .base_consumer import BaseConsumer


class ChatConsumer(BaseConsumer):
    user_channel_utils = UserChannelUtils()

    async def connect(self):
        user: User = self.scope["user"]
        await self.user_channel_utils.update_channel_name_for_user(
            user_id=user.id, channel_name=self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        user: User = self.scope["user"]
        data = json.loads(text_data)
        receiver_id = data["receiver_id"]
        msg = MessageEvent(
            sender=user, content=data["content"], receiver_id=receiver_id
        )
        await self.send(text_data=msg.text)
        try:
            user_channel: UserChannel = (
                await self.user_channel_utils.get_channel_by_user_id(
                    user_id=receiver_id
                )
            )
            await self.send_to_channel(
                channel_name=user_channel.channel_name,
                event_type="chat.message",
                text_data=msg.text,
            )
        except Exception as e:
            print("Some error occured!!", e)

    async def chat_message(self, event):
        await self.send(text_data=event["text"])

    async def echo_message(self, event):
        await self.send(text_data=event["text"])

    async def disconnect(self, close_code):
        print("`disconnect` is called", close_code)
