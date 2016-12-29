# encoding:utf-8
import os.path
from django.utils.translation import ugettext as _

def check_local_setting(name, value):
    local_vars = locals()
    if name in local_vars and local_vars[name] == value:
        return True
    else:
        return False

SITE_SRC_ROOT = os.path.dirname(__file__)
LOG_FILENAME = 'django.osqa.log'

#for logging
import logging
logging.basicConfig(
    filename=os.path.join(SITE_SRC_ROOT, 'log', LOG_FILENAME),
    level=logging.DEBUG,
    format='%(pathname)s TIME: %(asctime)s MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s',
)

#ADMINS and MANAGERS
ADMINS = (('Forum Admin', 'forum@example.com'),)
MANAGERS = ADMINS

#DEBUG = True
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

#DATABASE_NAME = os.environ["MYSQL_DATABASE"]
#DATABASE_USER = os.environ["MYSQL_USERNAME"]
#DATABASE_PASSWORD = os.environ["MYSQL_PASSWORD"]
#DATABASE_HOST = os.environ["MYSQL_LOCATION"]

DATABASE_NAME = 'osqa'
DATABASE_USER = 'root'
DATABASE_PASSWORD = '&MOVy1PV'
#DATABASE_HOST = 'mysql'
DATABASE_HOST = 'localhost'

DATABASE_ENGINE = 'django.db.backends.mysql'
DATABASE_PORT = '3306'


#CACHE_BACKEND = 'file://%s' % os.path.join(os.path.dirname(__file__),'cache').replace('\\','/')
CACHE_BACKEND = 'dummy://'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

APP_URL = 'http://' #used by email notif system and RSS

#LOCALIZATIONS
TIME_ZONE = 'America/New_York'

###########################
#
#   this will allow running your forum with url like http://site.com/forum
#
#   FORUM_SCRIPT_ALIAS = 'forum/'
#
FORUM_SCRIPT_ALIAS = '' #no leading slash, default = '' empty string


#OTHER SETTINGS

USE_I18N = True
LANGUAGE_CODE = 'en'
EMAIL_VALIDATION = 'off' #string - on|off
MIN_USERNAME_LENGTH = 1
EMAIL_UNIQUE = False

WIKI_ON = True
FEEDBACK_SITE_URL = None #None or url
EDITABLE_SCREEN_NAME = False #True or False - can user change screen name?

DJANGO_VERSION = 1.1
RESOURCE_REVISION=4

OSQA_DEFAULT_SKIN = 'default'

DISABLED_MODULES = ['books', 'recaptcha', 'project_badges']

from forum.settings import *
