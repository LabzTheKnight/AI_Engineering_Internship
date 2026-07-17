import fastapi
import sqlalchemy
from sqlalchemy.orm import Session
from database_setup import get_db , Note
from models import NoteResponse , CreateNote
from fastapi import FastAPI , Depends , HTTPException
from LLM import ai_summarize , ai_gen_quiz , summary_chain

app = FastAPI()


@app.get("/")
async def get_root():
    return {"this is a health root"}

@app.get("/notes", response_model = list[NoteResponse])
async def get_notes( db: Session = Depends(get_db) ):
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
    note:Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        return note
    return {"ItemNotFoundException"}

@app.post("/notes/{note_id}/summary" , response_model = NoteResponse)
async def summarize_note(note_id: int , db: Session = Depends(get_db)):
    note: Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        result = await summary_chain.ainvoke({"note": note.content , "style": "brief"})
        note.summary = str(result.content).strip()
        db.commit()
    return note

@app.post("/notes/{note_id}/quiz" , response_model = NoteResponse )
async def gen_quiz(note_id: int , db: Session = Depends(get_db)):
    note: Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        note.quiz = ai_gen_quiz(note.content)
        db.commit()
    return note

@app.patch( "/notes/{note_id}" , response_model = NoteResponse )
async def patch_note( note_id: int , data:str , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter(Note.id == note_id).first()
    note.content = data
    db.commit()
    return note



@app.delete( "/notes/{note_id}" )
async def delete_note(note_id: int , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter( Note.id == note_id ).first()
    if note:
        db.delete(note)
        db.commit()
        return {"note successfully deleted"}
    raise HTTPException(status_code = 404 , detail = "itemNotFound")

    