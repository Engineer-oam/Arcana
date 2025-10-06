from __future__ import annotations

import os
import uuid
from pathlib import Path
from typing import BinaryIO, Optional

import boto3
from botocore.client import BaseClient

from app.core.config import settings


LOCAL_STORAGE_DIR = Path(os.getenv("LOCAL_STORAGE_DIR", "/workspace/infra/storage"))


class StorageClient:
    def __init__(self) -> None:
        self._s3: Optional[BaseClient] = None
        if settings.S3_ENDPOINT_URL or settings.AWS_ACCESS_KEY_ID:
            self._s3 = boto3.client(
                "s3",
                endpoint_url=settings.S3_ENDPOINT_URL,
                region_name=settings.S3_REGION,
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )

    def save(self, fileobj: BinaryIO, filename: str, content_type: str | None = None) -> tuple[str, str]:
        """Save file and return (storage_key, public_url)."""
        ext = os.path.splitext(filename)[1]
        key = f"uploads/{uuid.uuid4().hex}{ext}"
        if self._s3:
            extra_args = {"ACL": "private"}
            if content_type:
                extra_args["ContentType"] = content_type
            fileobj.seek(0)
            self._s3.upload_fileobj(fileobj, settings.S3_BUCKET, key, ExtraArgs=extra_args)
            url = f"s3://{settings.S3_BUCKET}/{key}"
            return key, url
        # local fallback
        LOCAL_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
        dest_path = LOCAL_STORAGE_DIR / key
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "wb") as out:
            fileobj.seek(0)
            out.write(fileobj.read())
        url = f"/files/{key}"
        return key, url
