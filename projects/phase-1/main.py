import fastapi
import pydantic
import sqlalchemy
from fastapi import FastAPI , Depends , HTTPException
import json;
import os;
from pydantic import BaseModel
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , Session , DeclarativeBase , Mapped , mapped_column



DATABASE = "sqlite:///./test.db"
engine = create_engine(DATABASE)
SessionLocal = sessionmaker( autocommit=False , autoflush=False , bind=engine )


class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


class Task(Base):
    __tablename__ = "tasks"
    index: Mapped[int] = mapped_column(primary_key= True , index = True)
    title: Mapped[str] = mapped_column(index = True)
    completed: Mapped[bool] = mapped_column( unique=False , default=False)

class TaskCreate(BaseModel):
    title: str

class TaskResponse(BaseModel):   
    index: int
    title: str
    completed: bool

class DelTaskResponse(BaseModel):
    title: str
    index: int

Base.metadata.create_all( bind=engine )



@app.get("/")
def read_root():
    return {"Hello World"}


@app.get("/items" , response_model = list[TaskResponse] )
async def read_items( db: Session = Depends(get_db)):
    tasks: list = db.query(Task).all()
    return tasks

@app.get("/items/{item_id}" , response_model = TaskResponse )
async def read_item(item_id: int, db: Session = Depends(get_db)):
    task: Task = db.query(Task).filter(Task.index == item_id).first()
    if task is None:
        raise HTTPException(status_code = 404 , detail= " item not found ")
    return task

@app.post("/items/", response_model =TaskResponse )
async def create_task(task: TaskCreate , db: Session = Depends(get_db) ):
    db_task: Task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.put("/items/{item_id}" , response_model = TaskResponse )
async def update_item(item_id: int , db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.index == item_id).first()
    db_task.completed = True
    db.commit()
    return db_task 
    
    
@app.delete("/items/{item_id}" , response_model = DelTaskResponse )
async def delete_item(item_id: int , db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.index == item_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return {"title": "successfully deleted task:" , "index": item_id}
    raise HTTPException(status_code = 404 , detail = "item not found") 


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app , host="127.0.0.1" , port = 8000)