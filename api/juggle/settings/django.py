import os

from .environment import env


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rel(*path):
    return os.path.join(BASE_DIR, *path)


DEBUG = env.bool("JUGGLE_DEBUG", default=False)

INTERNAL_IPS = env.list("JUGGLE_INTERNAL_IPS", default=[])

ALLOWED_HOSTS = env.list("JUGGLE_ALLOWED_HOSTS", default=[])

SECRET_KEY = env.str("JUGGLE_SECRET_KEY")

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party apps
    "rest_framework",
    "django_extensions",
    "django_filters",
    "drf_yasg",
    # our apps
    "juggle.apps.common",
    "juggle.apps.accounts",
] + env.list("JUGGLE_DEV_INSTALLED_APPS", default=[])

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
] + env.list("JUGGLE_DEV_MIDDLEWARE", default=[])

ROOT_URLCONF = "juggle.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [rel("templates/")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "juggle.wsgi.application"

DATABASES = {"default": env.db("JUGGLE_DATABASE_URL", default="psql://postgres:london@database:5432/juggle_db")}

AUTH_USER_MODEL = "accounts.UserAccount"
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

SECURE_BROWSER_XSS_FILTER = env.bool("JUGGLE_SECURE_BROWSER_XSS_FILTER", default=True)
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("JUGGLE_SECURE_CONTENT_TYPE_NOSNIFF", default=True)
SESSION_COOKIE_HTTPONLY = env.bool("JUGGLE_SESSION_COOKIE_HTTPONLY", default=True)
SESSION_COOKIE_SECURE = env.bool("JUGGLE_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("JUGGLE_CSRF_COOKIE_SECURE", default=True)
X_FRAME_OPTIONS = env.str("JUGGLE_X_FRAME_OPTIONS", default="SAMEORIGIN")
SECURE_HSTS_SECONDS = env.int("JUGGLE_SECURE_HSTS_SECONDS", default=31536000)  # 1 year
SESSION_COOKIE_NAME = "s"
CSRF_COOKIE_NAME = "c"

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (rel("..", "..", "api", "locale"),)

STATIC_URL = env.str("JUGGLE_STATIC_URL", default="/s/")
STATIC_ROOT = env.str("JUGGLE_STATIC_ROOT", default=rel("..", "..", "public", "static"))

MEDIA_URL = env.str("JUGGLE_MEDIA_URL", default="/m/")
MEDIA_ROOT = env.str("JUGGLE_MEDIA_ROOT", rel("..", "..", "public", "media"))
FILE_UPLOAD_PERMISSIONS = 0o644

EMAIL_BACKEND = env.str("JUGGLE_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
if EMAIL_BACKEND == "django.core.mail.backends.smtp.EmailBackend":  # pragma: no cover
    EMAIL_HOST = env.str("JUGGLE_EMAIL_HOST")
    EMAIL_PORT = env.str("JUGGLE_EMAIL_PORT")
    EMAIL_HOST_USER = env.str("JUGGLE_EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env.str("JUGGLE_EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env.bool("JUGGLE_EMAIL_USE_TLS", default=True)

SITE_ID = env.int("SITE_ID", default=1)

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

APPEND_SLASH = False
