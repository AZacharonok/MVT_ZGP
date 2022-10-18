"""
ASGI config for MVT_Zacharonok_Garagaza_Puentes project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MVT_Zacharonok_Garagaza_Puentes.settings')

application = get_asgi_application()
