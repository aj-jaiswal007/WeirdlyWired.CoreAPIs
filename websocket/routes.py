from channels.routing import URLRouter
from django.urls import path
from websocket.consumers.echo_consumer import EchoConsumer
from websocket.consumers.chat_consumer import ChatConsumer

# TODO: create all websocket urls here
WEBSOCKET_ROUTES = URLRouter(
    [
        path("echo_bot/", EchoConsumer.as_asgi()),
        path("chat/", ChatConsumer.as_asgi()),
    ]
)
