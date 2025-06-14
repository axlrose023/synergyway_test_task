# region				-----External Imports-----
import os
from kombu import Queue

# endregion

REDIS_CONNECTION_URL = f'redis://{os.environ.get("REDIS_USER","default")}:{os.environ.get("REDIS_PASSWORD","default")}@{os.environ.get("REDIS_HOST","127.0.0.1")}:{os.environ.get("REDIS_PORT",6379)}'
CELERY_BROKER_URL = REDIS_CONNECTION_URL
CELERY_RESULT_BACKEND = REDIS_CONNECTION_URL
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Europe/Kiev"

CELERY_DEFAULT_QUEUE = "default"
CELERY_QUEUES = (
    Queue("default"),
    Queue("priority_high"),
)

CELERY_BEAT_SCHEDULE = {
    "fetch-users-every-hour": {
        "task": "users.fetch_and_upsert",
        "schedule": 60.0,
    },
    "fill-addresses-every-6-hours": {
        "task": "users.fill_addresses",
        "schedule": 120.0,
    },
    "fill-credit-cards-every-6-hours": {
        "task": "users.fill_credit_cards",
        "schedule": 120.0,
    },
}