"""
ASGI config for weirdlywired project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
import os
from configurations import importer
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weirdlywired.settings")  # noqa
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")  # noqa
importer.install()  # noqa
django.setup()  # noqa

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter

from django.core.asgi import get_asgi_application

from websocket.routes import WEBSOCKET_ROUTES
from weirdlywired.middleware.ws_authentication import WSTokenAuthMiddleWare


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": WSTokenAuthMiddleWare(AuthMiddlewareStack(WEBSOCKET_ROUTES)),
    }
)

# daphne -b 192.168.29.145 -p 8000 --ping-interval 2 --ping-timeout 5 weirdlywired.asgi:application
