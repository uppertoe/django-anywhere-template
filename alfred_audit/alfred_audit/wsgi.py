"""
WSGI config for alfred_audit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

#Determine whether dev.py exists
    try:
        from alfred_audit.settings import dev
        settings_path = 'settings.dev'
    except ImportError:
        from alfred_audit.settings import prod
        settings_path = 'settings.prod'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)

application = get_wsgi_application()
