"""
WSGI config for weirdlywired project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weirdlywired.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Local')

from configurations.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
