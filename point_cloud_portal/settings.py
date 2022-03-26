from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'very-secure-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'pwa',
    'corsheaders',
    'viewer'
]


ROOT_URLCONF = 'point_cloud_portal.urls'
AUTH_USER_MODEL = 'viewer.CustomUser'

LOGIN_REDIRECT_URL = '/' 
LOGOUT_REDIRECT_URL = '/login' 
LOGIN_URL = '/login'


CSRF_TRUSTED_ORIGINS = ['http://0.0.0.0']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
  'http://0.0.0.0:3000',
)


#GDAL_LIBRARY_PATH="C:\OSGeo4W64/bin/gdal301.dll"
#GEOS_LIBRARY_PATH="C:\OSGeo4W64/bin/geos_c.dll"


ROOT_URLCONF = 'point_cloud_portal.urls'
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static','static_dirs'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')





MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'point_cloud_portal.wsgi.application'
DATABASES = {
    'default': {

        'ENGINE': 'django.contrib.gis.db.backends.postgis',

        'NAME': 'pointclouddb',

        'USER': 'db_user',

        'PASSWORD': 'db_password',

        'HOST': 'db_host',

        'PORT': '5432',

    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



#PWA

PWA_APP_NAME = 'Geomeletitiki Cloud Platform'
PWA_APP_DESCRIPTION = "All your clouds, one place!"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': 'static/img/favicon.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/img/favicon.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static /img/favicon.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'templates/pwa', 'serviceworker.js')