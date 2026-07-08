import pytest
import fastapi
import sqlalchemy 
from sqlalchemy import create_engine , StaticPool
from sqlalchemy.orm import sessionmaker 
from fastapi.testclient import TestClient
from main import app , Base , get_db

client = TestClient(app)
DATABASE_URL = "sqlite:///:memory:"
engine = create_engine( 
    DATABASE_URL ,
    connect_args={
        "check_same_thread": False
    },
    poolclass = StaticPool 
)

TestingSessionLocal = sessionmaker( autocommit = False , autoflush = False , bind = engine )

def override_get_db():
    db = TestingSessionLocal()
    
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


def setup() -> None:
    Base.metadata.create_all( bind = engine )

def teardown() -> None:
    Base.metadata.drop_all( bind = engine )

@pytest.fixture
def create_destroy():
    setup()
    yield 
    teardown()


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ["Hello World"]


def test_create_task(create_destroy):
    response = client.post(
        "/items/", json = { "title": "This is a test item"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["title"] == "This is a test item"
    
    
def test_update_task(create_destroy):
    item_id = 1
    client.post(
        "/items/", json = {"title":"This is a test item"}
        )
    
    response = client.put(
        f"/items/{item_id}"
    )
    data = response.json()
    assert data == { "index":1 , "title":"This is a test item" , "completed": True }

def test_read_task(create_destroy):
    item_id = 1
    client.post(
        "/items/" , json = { "title": "This is a test different test item" }
    )
    response = client.get(
        f"/items/{item_id}"
    )
    data = response.json()
    assert data["title"] == "This is a test different test item"

def test_delete_task(create_destroy):
    item_id = 1
    client.post(
        "/items/", json = {"title":"This is a test item"}
        )
    response = client.delete(
        f"/items/{item_id}"
    )
    data = response.json()
    assert data["title"] == "successfully deleted task:"
    assert data["index"] == item_id