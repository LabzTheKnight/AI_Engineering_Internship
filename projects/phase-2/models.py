import pydantic
from pydantic import BaseModel



class NoteResponse(BaseModel):
    id: int
    content: str
    summary: str
    quiz: str

class CreateNote(BaseModel):
    content: str