import fastapi
from fastapi.testclient import TestClient
def test_create_note(client: TestClient):
    response = client.post(
        "/notes",
        json = {
            "content":"test note"
        }
    )

    assert response.status_code == 200 