from __future__ import annotations

from pydantic import BaseModel


class DocumentOut(BaseModel):
    id: str
    case_id: str
    filename: str
    content_type: str | None = None
    size_bytes: int | None = None
    storage_key: str

    class Config:
        from_attributes = True
