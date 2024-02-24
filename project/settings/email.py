import os


EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.environ.get("AWS_SES_SMTP_HOST", None)
EMAIL_PORT = os.environ.get("AWS_SES_SMTP_PORT", 587)
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", None)
if EMAIL_HOST_USER is None:
    EMAIL_HOST_USER = os.environ.get("AWS_SES_SMTP_USER", None)
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", None)
if EMAIL_HOST_PASSWORD is None:
    EMAIL_HOST_PASSWORD = os.environ.get("AWS_SES_SMTP_PASSWORD", None)
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = os.environ.get("EMAIL_SUBJECT_PREFIX", None)
EMAIL_USE_LOCALTIME = os.environ.get("EMAIL_USE_LOCALTIME", True)

# Redis
# REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
# REDIS_PORT = os.getenv("REDIS_PORT", 6379)
# REDIS_DB = os.getenv("REDIS_DB", 0)

# Celery
# BROKER_URL = "redis://localhost:6379"
# CELERY_RESULT_BACKEND = "redis://localhost:6379"
# CELERY_ACCEPT_CONTENT = ["application/json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_CREATE_MISSING_QUEUES = True
