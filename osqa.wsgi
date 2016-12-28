import os
import sys
sys.path.append('/var/www/html')
sys.path.append('/var/www/html/estafa2')

os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
