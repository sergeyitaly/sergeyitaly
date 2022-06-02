from datetime import timedelta
import datetime
import os
from pathlib import Path
from django.conf import settings
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

CART_SESSION_ID = 'cart'
SECRET_KEY = config('SECRET_KEY_MYSITE')
DEBUG = config('DEBUG', default=False, cast=bool)


SITE_NAME = "Leather-Shop"
ALLOWED_HOSTS = ['sergeyitaly.pythonanywhere.com']
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_HSTS_PRELOAD=True
SECURE_HSTS_SECONDS = 31536000
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'allauth', # new
    'allauth.account', # new
    'allauth.socialaccount', # new
    'frontend',
    'knox',
    'accounts',
    'whitenoise.runserver_nostatic',
    'djoser',
    'cart',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    #'rest_framework_jwt',
    'drf_yasg'

    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, "frontend","build")
        ],
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.AllowAny",
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
    #'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',


    ),
}
#CORS_ORIGIN_WHITELIST = ['http://localhost:3000',]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
AUTHENTICATION_BACKENDS ={
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
}
SITE_ID = 1
AUTH_USER_MODEL = 'accounts.CustomUser'

#AUTH_USER_MODEL = "accounts.CustomUser"
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password-reset/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': 'username-reset/{uid}/{token}',
    'ACTIVATION_URL': 'activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL' :True,
    'SERIALIZERS': {},
    'USER_CREATE_PASSWORD_RETYPE' : True,
    'USERNAME_CHANGED_EMAIL_CONFIRMATION' :True,
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION' :True,
    'SEND_CONFIRMATION_EMAIL' :True,
    'SERIALAZERS':{  }
}
# app password: vxfnflimsnbvgfvx
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "sergeyitalykiev@gmail.com"
EMAIL_HOST_PASSWORD = "vxfnflimsnbvgfvx"
EMAIL_USE_TLS = True


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer'),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': '/home/sergeyitaly/mysite/New-Leather-Goods-Shop/db.sqlite3',}}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'OPTIONS': {
#            'read_default_file': 'BASE_DIR/my.cnf',
#        },
#    }
#}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True
REACT_APP_DIR = os.path.join(BASE_DIR, 'frontend')

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'frontend', 'build', 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_INDEX_FILE = True
WHITENOISE_ROOT = os.path.join(STATIC_ROOT, 'root')

# MEDIA Folder settings
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

INTERNAL_IPS = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'site_cache'),
    }
}