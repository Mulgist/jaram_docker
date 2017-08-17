"""
WSGI config for jaram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/var/www/html/jaram.net')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/usr/lib64/python3.6/site-packages')


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jaram.settings.local")

application = get_wsgi_application()
