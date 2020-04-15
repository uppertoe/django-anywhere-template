"""
WSGI config for alfred_audit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alfred_audit.settings.dev')
except ModuleNotFoundError:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alfred_audit.settings.prod')

application = get_wsgi_application()
