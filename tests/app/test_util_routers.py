from http import HTTPStatus

from fastapi.testclient import TestClient

from app.main import app as viewer_app


HEALTH_URL = viewer_app.url_path_for("health")
HOME_URL = viewer_app.url_path_for("root_page")


def test_health(v_client: TestClient):
    req = v_client.get(HEALTH_URL)
    assert req.status_code == HTTPStatus.OK


def test_home(v_client: TestClient):
    req = v_client.get(HOME_URL)
    assert req.status_code == HTTPStatus.OK
