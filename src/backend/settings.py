"""
Django settings for vorgang23 project
=====================================

This file configures the django application.
However, for application settings, please checkout the configuration
file located in:

    /etc/vorgang23/vorgang23.conf

Or relative to your projects root:

    etc/vorgang23/vorgang23.conf

where you can override the default settings.

"""

import os
import sys
import configparser


# Default configurations:
#
# These are the defaults, for use with a local docker development setup.
# It is _NOT RECOMMENDED_ to edit this file.
# Use the etc/vorgang23/sandbox.conf configuration to change settings.
#
DEFAULT_SECRET_KEY = "DDnlf39@rmf&yeb7i(6)++jf20i30n23bl8&9xg-7+p_"
DEFAULT_CONFIG = {
    "vorgang": {
        "debug": "true",
        "secret_key": DEFAULT_SECRET_KEY,
        "log_level": "INFO",
    },
    "database": {
        "engine": "django.db.backends.postgresql_psycopg2",
        "name": "postgres",
        "user": "postgres",
        "host": "db",
        "port": 5432,
    },
}

# Parse configuration(s)
config = configparser.ConfigParser()
config.read_dict(DEFAULT_CONFIG)
config.read([
    "./etc/vorgang23/vorgang23.conf",
    "/etc/vorgang23/vorgang23.conf",
])


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config["vorgang"].getboolean("debug", True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config["vorgang"].get("secret_key")
if SECRET_KEY == DEFAULT_SECRET_KEY and not DEBUG:
    print("ERROR: You must change the secret key in a production environment")
    sys.exit(-1)


ALLOWED_HOSTS = config["vorgang"].get("allowed_hosts", "").split(",")

# Application definition

INSTALLED_APPS = [
    "polymorphic",
    "django_filters",

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"
# Database
DATABASES = {
    "default": {
        "ENGINE": config["database"]["engine"],
        "NAME": config["database"]["name"],
        "USER": config["database"]["user"],
        "HOST": config["database"]["host"],
        "PORT": config["database"]["port"],
    }
}

# Auth user
AUTH_USER_MODEL = "vorgang_auth.User"

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "/static/"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(name)-20s %(module)s %(process)d %(thread)d %(message)s",
        },
        "simple": {
            "format": "%(asctime)s %(levelname)-8s %(name)-20s| %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": config["vorgang"]["log_level"],
        },
        "vorgang": {
            "handlers": ["console"],
            "level": config["vorgang"]["log_level"],
        },
    },
}


