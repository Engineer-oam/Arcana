from __future__ import annotations

from pydantic import BaseModel


class CaseCreate(BaseModel):
    name: str
    description: str | None = None


class CaseOut(BaseModel):
    id: str
    name: str
    description: str | None = None

    class Config:
        from_attributes = True
