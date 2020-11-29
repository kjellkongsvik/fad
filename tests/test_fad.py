from fastapi.testclient import TestClient

from fad.fad import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.ok
