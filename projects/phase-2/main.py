import fastapi
import pydantic
import sqlalchemy
from pydantic import BaseModel
from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import Session , sessionmaker , DeclarativeBase , Mapped , mapped_column


app = FastAPI()

class Base(DeclarativeBase):
    pass

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[ int ] = mapped_column( primary_key = True , index = True )
    content: Mapped[ str ] = mapped_column( index = True )
    ai_content: Mapped[ str ] = mapped_column( index = True )

class NoteResponse(BaseModel):
    id: int
    content: str

class CreateNote(BaseModel):
    content: str


@app.get("/")
async def get_root():
    return {"this is a health root"}

@app.get("/notes", response_model = list[Note])
async def get_notes( db: Session = Depends(get_bd) ):
    notes: list[Note] = db.query(Note).all()
    return notes


@app.post("/notes" , response_model = NoteResponse )
async def create_note(data: CreateNote , db: Session = Depends(get_db)):
    note:Note = Note(**data.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

@app.get( "/notes/{note_id}" , response_model = NoteResponse )
async def get_note(note_id: int , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter(Note.id == note_id)
    if note:
        return note
    return {"ItemNotFoundException"}

@app.patch( "/notes/{note_id}" , response_model = NoteResponse )
async def patch_note( note_id: int , data:str , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter(Note.id == note_id)
    note.content = data
    db.commit()
    return note

@app.delete( "/notes/{note_id}" )
async def delete_note(note_id: int , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter( Note.id == note_id )
    if note:
        db.delete(note)
        db.commit()
        return {"note successfully deleted"}
    raise HTTPException(status_code = 404 , detail = "itemNotFound")

    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run( app , host = "127.0.0.1" , port = 8000)