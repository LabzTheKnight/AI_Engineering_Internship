import os
import sqlalchemy
import asyncpg
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine 
from sqlalchemy.orm import Session , sessionmaker , DeclarativeBase , Mapped , mapped_column
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker( autocommit=False , autoflush=False , bind = engine)

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "ai_notes"
    id: Mapped[ int ] = mapped_column( primary_key = True , index = True )
    content: Mapped[ str ] = mapped_column( index = True )
    summary: Mapped[ str ] = mapped_column( index = True , default = "" )
    quiz: Mapped[ str ] = mapped_column( index = True , default = "")

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()

Base.metadata.create_all(bind=engine)