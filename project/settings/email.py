import os

# https://docs.djangoproject.com/en/5.0/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", None)

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-backend
# https://docs.djangoproject.com/en/5.0/topics/email/#topic-email-backends
# Choices are:
# django.core.mail.backends.smtp.EmailBackend
# django.core.mail.backends.console.EmailBackend
# django.core.mail.backends.filebased.EmailBackend
# django.core.mail.backends.locmem.EmailBackend
# django.core.mail.backends.dummy.EmailBackend
EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)

# Credentials
EMAIL_HOST = os.environ.get("EMAIL_HOST", None)
EMAIL_PORT = os.environ.get("EMAIL_PORT", None)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", None)

# Credentials for Amazon SES
if EMAIL_HOST is None:
    EMAIL_HOST = os.environ.get("AWS_SES_SMTP_HOST", None)
if EMAIL_PORT is None:
    EMAIL_PORT = os.environ.get("AWS_SES_SMTP_PORT", 587)
if EMAIL_HOST_USER is None:
    EMAIL_HOST_USER = os.environ.get("AWS_SES_SMTP_USER", None)
if EMAIL_HOST_PASSWORD is None:
    EMAIL_HOST_PASSWORD = os.environ.get("AWS_SES_SMTP_PASSWORD", None)

EMAIL_SUBJECT_PREFIX = os.environ.get("EMAIL_SUBJECT_PREFIX", "[EMAIL SUBJECT PREFIX]")

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-ssl
EMAIL_USE_SSL = False

# https://docs.djangoproject.com/en/5.0/ref/settings/#email-use-localtime
EMAIL_USE_LOCALTIME = os.environ.get("EMAIL_USE_LOCALTIME", True)
