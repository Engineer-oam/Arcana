from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    APP_NAME: str = "e-Discovery Platform"
    ENV: str = "dev"
    DEBUG: bool = True

    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "ediscovery"
    POSTGRES_USER: str = "ediscovery"
    POSTGRES_PASSWORD: str = "ediscovery"

    REDIS_URL: str = "redis://localhost:6379/0"

    ELASTICSEARCH_URL: str = "http://localhost:9200"

    JWT_SECRET: str = "change-me"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12
    ADMIN_EMAIL: str = "admin@example.com"
    ADMIN_PASSWORD: str = "ChangeMe123!"

    S3_ENDPOINT_URL: str | None = None
    S3_BUCKET: str = "ediscovery"
    S3_REGION: str | None = None
    AWS_ACCESS_KEY_ID: str | None = None
    AWS_SECRET_ACCESS_KEY: str | None = None

    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
    ]

    class Config:
        env_file = ".env"

settings = Settings()