import fastapi
import sqlalchemy
from sqlalchemy.orm import Session
from database_setup import get_db , Note
from models import NoteResponse , CreateNote
from fastapi import Depends , HTTPException , APIRouter
from LLM import ai_gen_quiz ,ai_summarize


router = APIRouter()

@router.get("/")
async def get_root():
    return {"this is a health root"}

@router.get("/notes", response_model = list[NoteResponse])
async def get_notes( db: Session = Depends(get_db) ):
    notes: list[Note] = db.query(Note).all()
    if notes is None:
        raise HTTPException(status_code = 404 , detail="You have no notes")
    return notes
    


@router.post("/notes" , response_model = NoteResponse )
async def create_note(data: CreateNote , db: Session = Depends(get_db)):
    if data.content == "":
        raise HTTPException(status_code=404 , detail = "You cant make an empty note")
    note:Note = Note(**data.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

@router.get( "/notes/{note_id}" , response_model = NoteResponse )
async def get_note(note_id: int , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        return note
    raise HTTPException( status_code = 404 ,  detail = f"Note with {note_id} was not found")

@router.post("/notes/{note_id}/summary" , response_model = NoteResponse)
async def summarize_note(note_id: int , db: Session = Depends(get_db)):
    note: Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        result = await ai_summarize( note.content )
        note.summary = str(result.content).strip()
        db.commit()
        return note
    raise HTTPException( status_code = 404 , detail = f"Note with {note_id} was not found")

@router.post("/notes/{note_id}/quiz" , response_model = NoteResponse )
async def gen_quiz(note_id: int , db: Session = Depends(get_db)):
    note: Note = db.query(Note).filter(Note.id == note_id).first()
    if note:
        result = await ai_gen_quiz(note.content)
        note.quiz = str(result.content).strip()
        db.commit()         
        return note
    raise HTTPException( status_code = 404 , detail = f"Note with {note_id} was not found")

@router.patch( "/notes/{note_id}" , response_model = NoteResponse )
async def patch_note( note_id: int , data:str , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException( status_code = 404 , detail = f"Note with {note_id} was not found")
    note.content = data
    db.commit()
    return note



@router.delete( "/notes/{note_id}" )
async def delete_note(note_id: int , db: Session = Depends(get_db)):
    note:Note = db.query(Note).filter( Note.id == note_id ).first()
    if note:
        db.delete(note)
        db.commit()
        return {"note successfully deleted"}
    raise HTTPException(status_code = 404 , detail = "itemNotFound")

    