import fastapi
import pydantic
from pydantic import BaseModel
from fastapi import FastAPI , Depends


app = FastAPI()


class Note(BaseModel):
    id: int
    content: str


@app.get("/")
async def get_root():
    return {"this is a health root"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run( app , host = "127.0.0.1" , port = 8000)