from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


class BaseConsumer(AsyncWebsocketConsumer):
    groups = ["broadcast"]

    async def connect(self):
        raise NotImplementedError("`connect` is not implemented")

    async def receive(self, text_data=None, bytes_data=None):
        raise NotImplementedError("`receive` is not implemented")

    async def disconnect(self, close_code):
        raise NotImplementedError("`receive` is not implemented")

    async def send_to_channel(self, channel_name: str, event_type: str, text_data: str):
        channel_layer = get_channel_layer()
        await channel_layer.send(channel_name, {"type": event_type, "text": text_data})

    async def send_with_type(
        self, type: str = "websocket.send", text_data=None, bytes_data=None, close=False
    ):
        """
        Sends a reply back down the WebSocket
        """
        if text_data is not None:
            await self.base_send({"type": type, "text": text_data})
        elif bytes_data is not None:
            await self.base_send({"type": type, "bytes": bytes_data})
        else:
            raise ValueError("You must pass one of bytes_data or text_data")
        if close:
            await self.close(close)
