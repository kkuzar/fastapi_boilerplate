FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /service

# System deps (kept minimal)
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.in /service/
RUN pip install --upgrade pip && \
    pip install -r requirements.in

# Copy app code
COPY app /service/app
COPY app-start.sh /service/
RUN chmod +x /service/app-start.sh

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s \
  CMD curl -fsS http://127.0.0.1:8000/health || exit 1

CMD ["/service/app-start.sh"]
