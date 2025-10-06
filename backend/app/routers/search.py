from __future__ import annotations

from fastapi import APIRouter, Depends, Query

from app.core.deps import get_current_user
from app.schemas.search import SearchResponse, SearchHit
from app.services import search as search_service

router = APIRouter()


@router.get("/search", response_model=SearchResponse)
def search(
    q: str = Query(..., min_length=1),
    case_id: str | None = Query(default=None),
    size: int = Query(default=10, ge=1, le=100),
    _user=Depends(get_current_user),
) -> SearchResponse:
    res = search_service.search(case_id=case_id, q=q, size=size)
    hits = [
        SearchHit(
            document_id=h["_source"].get("document_id"),
            filename=h["_source"].get("filename", ""),
            score=h.get("_score", 0.0),
        )
        for h in res["hits"]["hits"]
    ]
    return SearchResponse(hits=hits)
