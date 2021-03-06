#!/usr/bin/env python
# encoding: utf-8
import sae
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application

application = sae.create_wsgi_app(get_wsgi_application())