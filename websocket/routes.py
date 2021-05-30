from channels.routing import URLRouter
from django.urls import path
from websocket.consumers.echo_consumer import EchoConsumer

# TODO: create all websocket urls here
WEBSOCKET_ROUTES = URLRouter(
    [
        path("ws/echo_bot/<str:userkey>", EchoConsumer.as_asgi()),
    ]
)
