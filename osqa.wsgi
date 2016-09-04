import os
import sys
sys.path.append('/var/www')
sys.path.append('/var/www/osqa')

os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
