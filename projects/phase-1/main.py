from fastapi import FastAPI
import json;
import os;
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "tasks.json")

app = FastAPI()


def add(a,file_path = filename) :
    with open(file_path,"r") as file:
        data = json.load(file)
        index = len(data) + 1 
        task = { "index": index , "title": a , "completed": False }
        data.append(task)
    with open(file_path, "w") as file :
        json.dump( data , file )

def list(file_path = filename):
    with open( file_path, "r" ) as file :
        data = json.load(file)
        return data

def list_id(id: int ,file_path: str = filename):
    return  list(file_path)[id - 1]
    





@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/health")

@app.get("/items")
def read_items():
    return list()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return list_id(item_id)

