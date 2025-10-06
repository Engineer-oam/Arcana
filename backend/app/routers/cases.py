from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.deps import get_current_user, require_roles
from app.models.case import Case
from app.models.user import User, UserRole
from app.schemas.cases import CaseCreate, CaseOut

router = APIRouter()


@router.get("/", response_model=list[CaseOut])
def list_cases(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
) -> list[CaseOut]:
    cases = db.execute(select(Case).order_by(Case.created_at.desc())).scalars().all()
    return [CaseOut.model_validate(c) for c in cases]


@router.post("/", response_model=CaseOut)
def create_case(
    payload: CaseCreate,
    db: Session = Depends(get_db),
    user: User = Depends(require_roles(UserRole.admin, UserRole.manager)),
) -> CaseOut:
    new_case = Case(name=payload.name, description=payload.description, created_by_user_id=user.id)
    db.add(new_case)
    db.commit()
    db.refresh(new_case)
    return CaseOut.model_validate(new_case)


@router.get("/{case_id}", response_model=CaseOut)
def get_case(case_id: str, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> CaseOut:
    case = db.get(Case, case_id)
    if not case:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Case not found")
    return CaseOut.model_validate(case)
