"""
ASGI config for weirdlywired project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from configurations import importer
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weirdlywired.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')
importer.install()
application = ProtocolTypeRouter({
    "http": get_asgi_application()
})
