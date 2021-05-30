import json
import typing as t

from .dtos.headers import Headers
from .dtos.query_params import QueryParams
from .constants import ReceiveEvent, SendEvent, State


class WebSocket:
    def __init__(self, scope, receive, send):
        self._scope = scope
        self._receive = receive
        self._send = send
        self._client_state = State.CONNECTING
        self._app_state = State.CONNECTING

    @property
    def headers(self):
        return Headers(self._scope)

    @property
    def scheme(self):
        return self._scope["scheme"]

    @property
    def path(self):
        return self._scope["path"]

    @property
    def query_params(self):
        return QueryParams(self._scope["query_string"].decode())

    @property
    def query_string(self) -> str:
        return self._scope["query_string"]

    @property
    def scope(self):
        return self._scope

    async def accept(self, subprotocol: str = None):
        """Accept connection.
        :param subprotocol: The subprotocol the server wishes to accept.
        :type subprotocol: str, optional
        """
        if self._client_state == State.CONNECTING:
            await self.receive()
        await self.send({"type": SendEvent.ACCEPT, "subprotocol": subprotocol})

    async def close(self, code: int = 1000):
        await self.send({"type": SendEvent.CLOSE, "code": code})

    async def send(self, message: t.Mapping):
        if self._app_state == State.DISCONNECTED:
            raise RuntimeError("WebSocket is disconnected.")

        if self._app_state == State.CONNECTING:
            assert message["type"] in {SendEvent.ACCEPT, SendEvent.CLOSE}, (
                'Could not write event "%s" into socket in connecting state.'
                % message["type"]
            )
            if message["type"] == SendEvent.CLOSE:
                self._app_state = State.DISCONNECTED
            else:
                self._app_state = State.CONNECTED

        elif self._app_state == State.CONNECTED:
            assert message["type"] in {
                SendEvent.SEND,
                SendEvent.CLOSE,
            }, 'Connected socket can send "%s" and "%s" events, not "%s"' % (
                SendEvent.SEND,
                SendEvent.CLOSE,
                message["type"],
            )
            if message["type"] == SendEvent.CLOSE:
                self._app_state = State.DISCONNECTED

        await self._send(message)

    async def receive(self):
        if self._client_state == State.DISCONNECTED:
            raise RuntimeError("WebSocket is disconnected.")

        message = await self._receive()

        if self._client_state == State.CONNECTING:
            assert message["type"] == ReceiveEvent.CONNECT, (
                'WebSocket is in connecting state but received "%s" event'
                % message["type"]
            )
            self._client_state = State.CONNECTED

        elif self._client_state == State.CONNECTED:
            assert message["type"] in {ReceiveEvent.RECEIVE, ReceiveEvent.DISCONNECT}, (
                'WebSocket is connected but received invalid event "%s".'
                % message["type"]
            )
            if message["type"] == ReceiveEvent.DISCONNECT:
                self._client_state = State.DISCONNECTED

        return message

    async def receive_json(self) -> t.Any:
        message = await self.receive()
        self._test_if_can_receive(message)
        return json.loads(message["text"])

    async def receive_jsonb(self) -> t.Any:
        message = await self.receive()
        self._test_if_can_receive(message)
        return json.loads(message["bytes"].decode())

    async def receive_text(self) -> str:
        message = await self.receive()
        self._test_if_can_receive(message)
        return message["text"]

    async def receive_bytes(self) -> bytes:
        message = await self.receive()
        self._test_if_can_receive(message)
        return message["bytes"]

    async def send_json(self, data: t.Any, **dump_kwargs):
        data = json.dumps(data, **dump_kwargs)
        await self.send({"type": SendEvent.SEND, "text": data})

    async def send_jsonb(self, data: t.Any, **dump_kwargs):
        data = json.dumps(data, **dump_kwargs)
        await self.send({"type": SendEvent.SEND, "bytes": data.encode()})

    async def send_text(self, text: str):
        await self.send({"type": SendEvent.SEND, "text": text})

    async def send_bytes(self, text: t.Union[str, bytes]):
        if isinstance(text, str):
            text = text.encode()
        await self.send({"type": SendEvent.SEND, "bytes": text})

    def _test_if_can_receive(self, message: t.Mapping):
        assert message["type"] == ReceiveEvent.RECEIVE, (
            'Invalid message type "%s". Was connection accepted?' % message["type"]
        )
