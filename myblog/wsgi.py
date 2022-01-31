import os

from django.core.wsgi import get_wsgi_application

#The default settings file that runserver will use
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")

application = get_wsgi_application()
