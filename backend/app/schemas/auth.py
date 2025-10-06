from __future__ import annotations

from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: EmailStr
    full_name: str | None = None
    role: UserRole

    class Config:
        from_attributes = True
