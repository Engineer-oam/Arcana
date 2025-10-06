from __future__ import annotations

import hashlib

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user
from app.models.case import Case
from app.models.document import Document
from app.schemas.documents import DocumentOut
from app.services.storage import StorageClient
from app.tasks.document_tasks import document_extract_text

router = APIRouter()


@router.post("/cases/{case_id}/documents", response_model=DocumentOut)
async def upload_document(
    case_id: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
) -> DocumentOut:
    case = db.get(Case, case_id)
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")

    storage = StorageClient()
    storage_key, _url = storage.save(file.file, file.filename, file.content_type)

    # compute sha256
    file.file.seek(0)
    sha256 = hashlib.file_digest(file.file, 'sha256').hexdigest()

    doc = Document(
        case_id=case.id,
        filename=file.filename,
        content_type=file.content_type,
        size_bytes=None,
        storage_key=storage_key,
        hash_sha256=sha256,
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    # enqueue extraction task
    try:
        document_extract_text.delay(str(doc.id))
    except Exception:
        pass
    return DocumentOut.model_validate(doc)
