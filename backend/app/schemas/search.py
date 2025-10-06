from __future__ import annotations

from pydantic import BaseModel


class SearchQuery(BaseModel):
  q: str
  case_id: str | None = None
  size: int = 10


class SearchHit(BaseModel):
  document_id: str
  filename: str
  score: float


class SearchResponse(BaseModel):
  hits: list[SearchHit]
