from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.core.config import settings
from app.core.database import Base, engine
from app.core.seed import seed_admin
from app.services.storage import LOCAL_STORAGE_DIR
from app.routers import auth, cases, documents
from app.routers import search as search_router
from app.services.search import ensure_index

app = FastAPI(title="e-Discovery Platform", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}


# Mount local storage for development/local usage
LOCAL_STORAGE_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/files", StaticFiles(directory=str(LOCAL_STORAGE_DIR)), name="files")


@app.on_event("startup")
def on_startup() -> None:
    # Create tables if they do not exist
    Base.metadata.create_all(bind=engine)
    # Seed initial admin user if not present
    seed_admin()
    # Ensure Elasticsearch index exists
    try:
        ensure_index()
    except Exception:
        # ES might not be available at startup in dev; continue
        pass


# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(cases.router, prefix="/cases", tags=["cases"])
app.include_router(documents.router, tags=["documents"])
app.include_router(search_router.router, tags=["search"])
