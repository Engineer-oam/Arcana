from __future__ import annotations

from typing import Any, Dict, List, Optional

from elasticsearch import Elasticsearch

from app.core.config import settings


INDEX_NAME = "ediscovery-docs"


def get_client() -> Elasticsearch:
    return Elasticsearch(settings.ELASTICSEARCH_URL)


def ensure_index() -> None:
    client = get_client()
    if client.indices.exists(index=INDEX_NAME):
        return
    client.indices.create(
        index=INDEX_NAME,
        mappings={
            "properties": {
                "case_id": {"type": "keyword"},
                "document_id": {"type": "keyword"},
                "filename": {"type": "text", "fields": {"raw": {"type": "keyword"}}},
                "content_type": {"type": "keyword"},
                "hash_sha256": {"type": "keyword"},
                "text": {"type": "text"},
                "created_at": {"type": "date"}
            }
        },
        settings={
            "index": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            }
        },
    )


def index_document(doc: Dict[str, Any]) -> None:
    client = get_client()
    client.index(index=INDEX_NAME, id=doc["document_id"], document=doc, refresh="true")


def search(case_id: Optional[str], q: str, size: int = 10) -> Dict[str, Any]:
    client = get_client()
    must: List[Dict[str, Any]] = [{"multi_match": {"query": q, "fields": ["text", "filename"]}}]
    if case_id:
        must.append({"term": {"case_id": case_id}})
    query = {"bool": {"must": must}}
    res = client.search(index=INDEX_NAME, query=query, size=size)
    return res
