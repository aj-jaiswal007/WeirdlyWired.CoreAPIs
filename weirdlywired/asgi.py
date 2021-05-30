"""
ASGI config for weirdlywired project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from configurations import importer
from django.core.asgi import get_asgi_application

from websocket.routes import WEBSOCKET_ROUTES
from weirdlywired.middleware.ws_authentication import WSTokenAuthMiddleWare

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weirdlywired.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
importer.install()
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WSTokenAuthMiddleWare(AuthMiddlewareStack(WEBSOCKET_ROUTES)),
    }
)
