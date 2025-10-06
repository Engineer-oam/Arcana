from app.core.database import Base

# Import models so that metadata is populated for create_all
from .user import User, UserRole  # noqa: F401
from .case import Case  # noqa: F401
from .document import Document, DocumentStatus  # noqa: F401
from .audit import AuditLog  # noqa: F401
from .legal_hold import LegalHold, LegalHoldStatus  # noqa: F401

__all__ = [
    "Base",
    "User",
    "UserRole",
    "Case",
    "Document",
    "DocumentStatus",
    "AuditLog",
    "LegalHold",
    "LegalHoldStatus",
]
