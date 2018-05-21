"""
WSGI config for matrixChatApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import matrixChatApp.readKey as readKey


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "matrixChatApp.settings")

# Running script to extract the access key from file
acc_token = readKey.extract()
application = get_wsgi_application()
