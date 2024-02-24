import pytest
from fastapi import status
from fastapi.testclient import TestClient

from src.api.app import app


@pytest.fixture()
def client():
    return TestClient(app)


# create a mock database to test the get visit endpoint
def test_get_visit(client):  # noqa: ANN001
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}
