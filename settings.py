# Django settings for mark project.
import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG
PROJECT_DIR = os.path.join(os.path.dirname(__file__)) + '/'
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
INTERNAL_IPS = ('127.0.0.1',)


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR + 'journal.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'RU-ru'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = PROJECT_DIR + 'media'
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = '*)7yz^*o0^yy0p(smbgvqtv5d0ni5ct_lu(6&wn+s7v2niy6-j'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'mark.urls'

TEMPLATE_DIRS = (
    PROJECT_DIR + 'templates',
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    'mark',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    #utility
    'debug_toolbar',
)



# DEBUG_TOOLBAR

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
