from tempfile import gettempdir
from os.path import dirname, join

from core import common

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ALLOWED_HOSTS = [
    ### cern.ch
    '.cern.ch',  # Allow domain and subdomains
    '.cern.ch.',  # Also allow FQDN and subdomains
    ### pandawms.org
    '.pandawms.org',  # Allow domain and subdomains
    '.pandawms.org.',  # Also allow FQDN and subdomains
]

# Make this unique, and don't share it with anybody.
from local import defaultDatabase, MY_SECRET_KEY
SECRET_KEY = MY_SECRET_KEY
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#        'USER': '',                      # Not used with sqlite3.
#        'PASSWORD': '',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#    }
    'default': defaultDatabase
}

# init logger
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOG_ROOT = '/data/bigpandamon/bigpandamon/logs/'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
#    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'logfile-bigpandamon': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.bigpandamon",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-django': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.django",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-viewdatatables': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.viewdatatables",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'logfile-rest': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_ROOT + "/logfile.rest",
            'maxBytes': 1000000000,
            'backupCount': 2,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
            'class':'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
#            'level': 'ERROR',
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers':['logfile-django'],
            'propagate': True,
            'level':'DEBUG',
        },
        'django_datatables_view': {
            'handlers':['logfile-viewdatatables'],
            'propagate': True,
            'level':'DEBUG',
        },
        'rest_framework': {
            'handlers':['logfile-rest'],
            'propagate': True,
            'level':'DEBUG',
        },
        'bigpandamon': {
            'handlers': ['logfile-bigpandamon'],
            'level': 'DEBUG',
        },
    },
    'formatters': {
        'verbose': {
#            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            'format': '%(asctime)s %(module)s %(name)-12s:%(lineno)d %(levelname)-5s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(name)-12s:%(lineno)d %(message)s'
        },
    },
    'logfile': {
        'level':'DEBUG',
        'class':'logging.handlers.RotatingFileHandler',
        'filename': LOG_ROOT + "/logfile",
        'maxBytes': 10000000,
        'backupCount': 5,
        'formatter': 'verbose',
    },
}

# media
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/data/bigpandamon/bigpandamon/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
#MEDIA_URL = '/media/'
MEDIA_URL_BASE = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/data/bigpandamon/bigpandamon/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
#STATIC_URL = '/static/'
STATIC_URL_BASE = '/static-common/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(dirname(common.__file__), 'static'),
)


#SERVER_INFO = {
#    'type': 'dev',
#}


### VIRTUALENV
VIRTUALENV_PATH = '/data/virtualenv/django1.6.1__python2.6.6'

### WSGI
WSGI_PATH = VIRTUALENV_PATH + '/bigpandamon'


### topology
SOURCE_SCHEDCONFIG = {
    'lsst': 'http://atlas-agis-api.cern.ch/request/pandaqueue/query/list/?json&preset=schedconf.all&site_state=ANY&vo_name=lsst',
}

### jobs by ProdUserName
CUSTOM_DB_FIELDS = {
    'jobListByProdUser': {
        'jobparam': ['jobStatus', 'cpuConsumptionTime', 'creationTime', \
                     'startTime', 'endTime', 'modificationHost', 'computingSite', \
                     'prodUserName'], \
        'configurable': ['jobparam', 'prodUserName', 'days']
    }
}

### URL_PATH_PREFIX for multi-developer apache/wsgi instance
### on EC2: URL_PATH_PREFIX = '/bigpandamon' or URL_PATH_PREFIX = '/developersprefix'
URL_PATH_PREFIX = '/bigpandamon-common'
### on localhost:8000: URL_PATH_PREFIX = '/.'
#URL_PATH_PREFIX = ''
#MEDIA_URL = URL_PATH_PREFIX + MEDIA_URL
MEDIA_URL = URL_PATH_PREFIX + MEDIA_URL_BASE
STATIC_URL = URL_PATH_PREFIX + STATIC_URL_BASE

ENV = {
    ### Application name
#    'APP_NAME': "ProdSys2", \
    'APP_NAME': "BigPanDA", \
    ### Page title default
    'PAGE_TITLE': "BigPanDA Monitor", \
    ### Menu item separator
    'SEPARATOR_MENU_ITEM': "&nbsp;&nbsp;&nbsp;", \
    ### Navigation chain item separator
    'SEPARATOR_NAVIGATION_ITEM': "&nbsp;&#187;&nbsp;" , \
}

FILTER_UI_ENV = {
    ### default number of days of shown jobs active in last N days
    'DAYS': 1, \
    ### default number of hours of shown jobs active in last N hours
    'HOURS': 2, \
    ### wildcard for string pattern in filter form
    'WILDCARDS': ['*'], \
    ### wildcard for integer interval in filter form
    'INTERVALWILDCARDS': [':'], \
    ###
    'EXPAND_BUTTON': { "mDataProp": None, "sTitle": "Details", \
                       "sClass": "control center", "bVisible": True, \
                       "bSortable": False, \
                       "sDefaultContent": '<img src="' + STATIC_URL + \
                                '/images/details_open.png' + '">' \
            }, \
}

#TODO:
#CSRF_FAILURE_VIEW
