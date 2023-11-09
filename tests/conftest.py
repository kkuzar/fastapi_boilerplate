import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def v_client() -> TestClient:
    return TestClient(app)
