from django.contrib.messages import constants as messages
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the secret key for the Django application
SECRET_KEY = 'django-insecure-rq@56+=zurqvo^x)9y3#isly65#7+8f+fdcbq&=hh%ybkb$4x+'

# Enable debug mode
DEBUG = False

# Allow all hosts to access the application
ALLOWED_HOSTS = ["*"]

# Set to True in production
CSRF_COOKIE_SECURE = True

# Set the root URL configuration for the project
ROOT_URLCONF = 'musicai.urls'

# Configure the installed apps for the Django project
INSTALLED_APPS = [
    'jazzmin',  # Install the Jazzmin admin theme
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'generator.apps.GeneratorConfig',
    'showcase.apps.ShowcaseConfig'
]

# Configure the middleware for the Django project
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configure the templates for the Django project
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# Set the WSGI application for the Django project
WSGI_APPLICATION = 'musicai.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
        'CONN_MAX_AGE': 300,
    }
}


# Configure the authentication backends for the Django project
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

# Configure the password validators for the Django project
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
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]

# Set the language code for the Django project
LANGUAGE_CODE = 'en-us'

# Set the time zone for the Django project
TIME_ZONE = 'UTC'

# Enable internationalization
USE_I18N = True

# Enable timezone support
USE_TZ = True

# Set the default auto field for the Django models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Set the URL path for static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Set the root directory for media files
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

# Configure message tags for Django messages
MESSAGE_TAGS = {
    messages.DEBUG: "primary",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "danger"
}

# Set the site ID for the Django project
SITE_ID = 1

# Set the URL path for the login page
LOGIN_URL = "login/"

# Set the redirect URL after successful login
LOGIN_REDIRECT_URL = "/"

# Enable login via GET request for social accounts
SOCIALACCOUNT_LOGIN_ON_GET = True

# Enable querying email for social accounts
SOCIALACCOUNT_QUERY_EMAIL = True

# Enable logout via GET request
ACCOUNT_LOGOUT_ON_GET = True

# Require unique email addresses for user accounts
ACCOUNT_UNIQUE_EMAIL = True

# Require email addresses for user accounts
ACCOUNT_EMAIL_REQUIRED = True

# Configure social account providers (e.g., Google)
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online'
        }
    }
}

# Configure custom settings for the admin dashboard (using Jazzmin)
JAZZMIN_SETTINGS = {
    "site_title": "Musicai.Art",
    "site_header": "Musicai.Art",
    "site_brand": "Musicai.Art",
}


# email configuration for sent forgot password email to users
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True