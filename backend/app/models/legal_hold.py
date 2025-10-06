from __future__ import annotations

import enum
import uuid

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class LegalHoldStatus(str, enum.Enum):
    active = "active"
    released = "released"


class LegalHold(Base):
    __tablename__ = "legal_holds"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    case_id = Column(UUID(as_uuid=True), ForeignKey("cases.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum(LegalHoldStatus, name="legal_hold_status"), nullable=False, default=LegalHoldStatus.active)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    case = relationship("Case", back_populates="legal_holds")
