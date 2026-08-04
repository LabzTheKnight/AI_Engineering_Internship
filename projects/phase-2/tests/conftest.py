import os
from collections.abc import Generator
import pytest
import sqlalchemy
import fastapi
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker , Session
from dotenv import load_dotenv
from main import app 
from database_setup import Base , get_db

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_TEST_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_TEST_NAME}"


@pytest.fixture(scope="session")
def engine():
    test_engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(test_engine)
    yield test_engine

    Base.metadata.drop_all(test_engine)
    test_engine.dispose()

@pytest.fixture
def db_session(engine: Engine):
    connection = engine.connect()
    transaction = connection.begin()
    db = Session( autocommit = False , autoflush = False , bind = connection , join_transaction_mode="create_savepoint" )
    try:
        yield db
    finally:
        db.close()
        transaction.rollback()
        connection.close()

@pytest.fixture
def client(db_session: Session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def create_test_notes(client: TestClient):
    response1 = client.post(
        "/notes",
        json = {
            "content" : "test note"
        }
    )   
    client.post(
        "/notes",
        json = {
            "content" : "test note 2"
        }
    )
    data = response1.json()
    return data["id"]