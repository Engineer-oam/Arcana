# e-Discovery Backend

FastAPI-based backend for e-Discovery platform.

## Run locally

```bash
# using poetry
poetry install
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Environment
Create `.env` at `backend/.env`:

```
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=ediscovery
POSTGRES_USER=ediscovery
POSTGRES_PASSWORD=ediscovery
REDIS_URL=redis://localhost:6379/0
ELASTICSEARCH_URL=http://localhost:9200
JWT_SECRET=change-me
```
