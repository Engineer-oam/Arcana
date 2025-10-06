from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.user import User, UserRole


def seed_admin() -> None:
    with SessionLocal() as db:  # type: Session
        existing = db.execute(select(User).where(User.email == settings.ADMIN_EMAIL)).scalar_one_or_none()
        if existing:
            return
        admin = User(
            email=settings.ADMIN_EMAIL,
            hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
            full_name="Administrator",
            role=UserRole.admin,
            is_active=True,
        )
        db.add(admin)
        db.commit()
