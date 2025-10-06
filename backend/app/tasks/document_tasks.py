from __future__ import annotations

import io
from datetime import datetime, timezone

import fitz  # pymupdf
import pytesseract
from PIL import Image

from app.tasks.celery_app import celery_app
from app.core.database import SessionLocal
from app.models.document import Document, DocumentStatus
from app.services.storage import LOCAL_STORAGE_DIR
from app.services.search import index_document


def _load_file(storage_key: str) -> bytes:
    path = LOCAL_STORAGE_DIR / storage_key
    with open(path, "rb") as f:
        return f.read()


@celery_app.task(name="app.tasks.document_extract_text")
def document_extract_text(document_id: str) -> None:
    with SessionLocal() as db:
        doc = db.get(Document, document_id)
        if not doc:
            return
        doc.status = DocumentStatus.processing
        db.commit()

        text_content: str = ""
        try:
            blob = _load_file(doc.storage_key)
            if (doc.content_type or "").lower().startswith("application/pdf") or doc.filename.lower().endswith(".pdf"):
                pdf = fitz.open(stream=blob, filetype="pdf")
                doc.page_count = pdf.page_count
                for page in pdf:
                    text_content += page.get_text()
                    if not page.get_text().strip():
                        pix = page.get_pixmap()
                        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                        text_content += "\n" + pytesseract.image_to_string(img)
            elif (doc.content_type or "").lower().startswith("image/"):
                img = Image.open(io.BytesIO(blob))
                text_content = pytesseract.image_to_string(img)
            else:
                # fallback: treat as binary, skip
                pass

            index_document(
                {
                    "case_id": str(doc.case_id),
                    "document_id": str(doc.id),
                    "filename": doc.filename,
                    "content_type": doc.content_type,
                    "hash_sha256": doc.hash_sha256,
                    "text": text_content,
                    "created_at": datetime.now(timezone.utc).isoformat(),
                }
            )
            doc.text_extracted = True
            doc.status = DocumentStatus.processed
        except Exception:
            doc.status = DocumentStatus.failed
        finally:
            db.commit()
