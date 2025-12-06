# FastAPI boilerplate

Modern FastAPI boilerplate using FastAPI 0.124.x and Pydantic v2.

### Features
- FastAPI >= 0.115 with Starlette 0.50
- Pydantic v2
- Env-based CORS configuration via `ALLOW_ORIGINS`
- Health and root endpoints
- Minimal Dockerfile (Python 3.12-slim) with healthcheck
- Simple Makefile for common tasks
- Pytest with coverage

### Requirements
- Python 3.12+ recommended
- pip / virtualenv

### Setup
1. Create and activate a virtualenv
   - `python -m venv .venv && source .venv/bin/activate`
2. Install dependencies
   - `pip install -r requirements.in`
3. (Optional) Install dev tools
   - `pip install -r requirements-dev.in`

### Run (local)
- Using Makefile (auto-reload):
  - `make run`
- Using script (production-style workers):
  - `./app-start.sh`

Server runs on `http://127.0.0.1:8000` by default.

Endpoints:
- `GET /health` → returns `{"status": "okay", "id": "..."}`
- `GET /` → returns `Curious?`

### CORS configuration
Define allowed origins with env var `ALLOW_ORIGINS` (comma-separated):
```
ALLOW_ORIGINS="http://localhost,http://127.0.0.1"
```
If not set, defaults to localhost and 127.0.0.1.

### Tests
```
pytest -q
```
or with coverage:
```
make test
```

### Docker
Build and run:
```
docker build -t fastapi-boilerplate -f app/docker/Dockerfile .
docker run --rm -p 8000:8000 fastapi-boilerplate
```

Docker image exposes port 8000 and has a healthcheck hitting `/health`.

### Notes
- This project installs runtime deps from `requirements.in` directly. If you prefer compiled lock files, use `pip-tools` (already in dev requirements) to generate `requirements.txt`/`requirements-dev.txt` and adjust the Makefile/Dockerfile accordingly.
