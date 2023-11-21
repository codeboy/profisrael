"""
WSGI config for profisrael project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

import importlib
module_name = 'subpackage.i.import'
special_module = importlib.import_module(module_name, package=None)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'profisrael.settings')

application = get_wsgi_application()

