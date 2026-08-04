import fastapi
from fastapi.testclient import TestClient


def test_create_note(client: TestClient):
    response = client.post(
        "/notes",
        json = { "content":"test note" }
    )
    assert response.status_code == 200
     

def test_show_notes(client: TestClient , create_test_notes):
    response = client.get(
        "/notes",
    )
    assert response.status_code == 200
    data = response.json()
    assert data[0]["content"] == "test note"
    assert data[1]["content"] == "test note 2"


def test_update_note(client: TestClient, create_test_notes):
    note_id: int = create_test_notes
    response = client.patch(
        f"/notes/{note_id}" ,
        params = { "data" : "test note updated" }
    )
    data = response.json()
    print(data)
    assert data["content"] == "test note updated"


def test_delete_note(client: TestClient , create_test_notes):
    note_id: int = create_test_notes
    response = client.delete(f"/notes/{note_id}")
    data = response.json()
    assert data[0] == "note successfully deleted"