from __future__ import annotations

import os

from celery import Celery

from app.core.config import settings


CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", settings.REDIS_URL)
CELERY_BACKEND_URL = os.getenv("CELERY_BACKEND_URL", settings.REDIS_URL)

celery_app = Celery(
    "ediscovery",
    broker=CELERY_BROKER_URL,
    backend=CELERY_BACKEND_URL,
)

celery_app.conf.update(
    task_routes={
        "app.tasks.document_*": {"queue": "documents"},
    },
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
