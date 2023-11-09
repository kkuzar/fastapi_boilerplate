#!/bin/bash
PYTHONDONTWRITEBYTECODE=1 uvicorn app.main:app --host 0.0.0.0 --no-access-log --log-level debug --workers 8
