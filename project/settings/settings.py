"""
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/

Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/
"""
import os
import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

dotenv.load_dotenv(os.path.join(BASE_DIR, "project/.env"))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", None)

DEBUG = os.getenv("DJANGO_DEBUG", "").lower() == "true"

allowed_hosts = os.getenv("DJANGO_ALLOWED_HOSTS", "")
ALLOWED_HOSTS = [host.strip() for host in allowed_hosts.split(",") if host]

SITE_ID = os.getenv("DJANGO_SITE_ID", 1)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django_extensions",
    "rest_framework",
    "debug_toolbar",
    "impersonate",
    "qux",
    "qux.seo",
    "qux.auth",
    "apps.gizmo",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
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

ROOT_URLCONF = "project.urls"

WSGI_APPLICATION = "project.wsgi.application"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

MYSQL_SETTINGS = {
    "ENGINE": "django.db.backends.mysql",
    "NAME": os.getenv("DB_NAME", None),
    "USER": os.getenv("DB_USERNAME", None),
    "PASSWORD": os.getenv("DB_PASSWORD", None),
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", ""),
    "OPTIONS": {
        "charset": "utf8mb4",
        "ssl": {"ca": os.getenv("DB_SSL_CERT", None)},
    },
}
SQLITE_SETTINGS = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
}

if os.getenv("DB_TYPE", "sqlite").lower() == "mysql":
    DATABASES = {
        "default": MYSQL_SETTINGS,
    }
else:
    DATABASES = {
        "default": SQLITE_SETTINGS,
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "project.finders.CustomAppDirectoriesStaticFinder",
]
STATICFILES_DIRS = [
    ("css", os.path.join(BASE_DIR, "common/css")),
    ("js", os.path.join(BASE_DIR, "common/js")),
    ("logo", os.path.join(BASE_DIR, "common/logo")),
]

# Bootstrap
BOOTSTRAP = os.getenv("BOOTSTRAP", "bs4")

# Minify HTML
HTML_MINIFY = True

# Qux Auth
LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# graph_models
GRAPH_MODELS = {
    "disable-abstract-fields": True,
    "verbose_names": False,
    "exclude_columns": [
        "dtm_created",
        "dtm_updated",
    ],
    "exclude_models": [
        "User",
        "ContentType",
        "CoreModel",
        "CoreModelAuditSummary",
        "CoreModelAuditDetails",
        "AbstractMRDS",
        "AbstractRefData",
    ],
    "disable_sort_fields": True,
    "arrow_shapw": "crow",
    "color_code_deletions": True,
    "rankdir": "BT",
}

# Django Debug Toolbar
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

SITE_HEADER = os.getenv("SITE_HEADER", "Qjango by Qux")
SITE_TITLE = os.getenv("SITE_TITLE", "Qjango")

