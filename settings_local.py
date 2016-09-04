# encoding:utf-8
import os.path

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.ERROR,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = ()
MANAGERS = ADMINS

DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': True
}
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)

#DATABASE_NAME = 'estafa2'
#DATABASE_USER = 'root'
#DATABASE_PASSWORD = ''
#DATABASE_HOST = 'localhost'

DATABASE_NAME = '$MYSQL_DATABASE'
DATABASE_USER = '$MYSQL_USERNAME'
DATABASE_PASSWORD = '$MYSQL_PASSWORD'
DATABASE_HOST = '$MYSQL_LOCATION'

DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_PORT = '3306'

CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
#CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# This should be equal to your domain name, plus the web application context.
# This shouldn't be followed by a trailing slash.
# I.e., http://www.yoursite.com or http://www.hostedsite.com/yourhostapp
APP_URL = 'http://www.estafa2.com'

#LOCALIZATIONS
TIME_ZONE = 'Europe/Berlin'

#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'es'

DJANGO_VERSION = 1.1
OSQA_DEFAULT_SKIN = 'default'

#DISABLED_MODULES = ['books', 'recaptcha', 'project_badges']
DISABLED_MODULES = ['project_badges', 'localauth']
#DISABLED_MODULES = [localauth]

DEFAULT_FROM_EMAIL = 'messenger@localhost'
SERVER_EMAIL = 'messenger@localhost'

EMAIL_SUBJECT_PREFIX = 'Estafa2'
EMAIL_HOST='smtp.oscargardiazabal.com'
EMAIL_PORT='587'
EMAIL_USE_TLS=True

#if you set FORUM_SCRIPT_ALIAS= 'forum/'
#then OSQA will run at url http://example.com/forum
#FORUM_SCRIPT_ALIAS cannot have leading slash, otherwise it can be set to anything
FORUM_SCRIPT_ALIAS = '' #no leading slash, default = '' empty string

EMAIL_VALIDATION = 'off' #string - on|off
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False #if True, email addresses must be unique in all accounts

FEEDBACK_SITE_URL = None #None or url
LOGIN_URL = '/%s%s%s' % (FORUM_SCRIPT_ALIAS,'account/','signin/')

