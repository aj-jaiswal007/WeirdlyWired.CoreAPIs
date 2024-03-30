import json
from websocket.models.user_channel_model import UserChannel
from websocket.utils.user_channel_utils import UserChannelUtils
from tenant.models.user_model import User
from websocket.dtos.msg_event import MessageEvent
from common.logger import logger
from .base_consumer import BaseConsumer
from llm.weirdly_wire import WeirdlyWire
from llm.enums import AgentPersona


class ChatConsumer(BaseConsumer):
    user_channel_utils = UserChannelUtils()
    wire = WeirdlyWire()

    async def connect(self):
        user: User = self.scope["user"]
        await self.user_channel_utils.update_channel_name_for_user(
            user_id=user.id, channel_name=self.channel_name
        )
        await self.accept()

    async def receive(self, text_data: str, bytes_data=None):
        logger.info(f"Msg revceived {text_data}")
        user: User = self.scope["user"]
        data = json.loads(text_data)
        receiver_id = data["receiver_id"]
        message_content = data["content"]
        persona = AgentPersona(data.get("persona", "funny"))
        user_message: str = self.wire.rewire_message(
            text_data=message_content, persona=persona
        )
        msg = MessageEvent(sender=user, content=user_message, receiver_id=receiver_id)
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
