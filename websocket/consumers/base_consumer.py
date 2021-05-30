from channels.consumer import AsyncConsumer
from websocket.constants import SendEvent
from typing import Union


class BaseConsumer(AsyncConsumer):
    """
    Implement these methods
    """

    async def websocket_connect(self, event):
        raise NotImplementedError("`websocket_connect` is not implemented")

    async def websocket_receive(self, event):
        raise NotImplementedError("`websocket_receive` is not implemented")

    async def websocket_disconnect(self, event):
        raise NotImplementedError("`websocket_disconnect` is not implemented")

    """
    Util methods
    """

    async def accept(self):
        await self.send({"type": SendEvent.ACCEPT})

    async def send_text(self, text: str):
        await self.send({"type": SendEvent.SEND, "text": text})

    async def send_bytes(self, text: Union[str, bytes]):
        if isinstance(text, str):
            text = text.encode()
        await self.send({"type": SendEvent.SEND, "bytes": text})

    async def close(self, code: int = 1000):
        """To close the connection"""
        await self.send({"type": SendEvent.CLOSE, "code": code})

    def get_text(self, event) -> str:
        return event["text"]

    def receive_bytes(self, event) -> bytes:
        return event["bytes"]
