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
        json.dump( data , file , indent=4)

def list(file_path = filename):
    with open( file_path, "r" ) as file :
        data = json.load(file)
        return data

def list_id(id: int ,file_path: str = filename):
    return  list(file_path)[id - 1]
    

def complete(index , file_path = filename):
    with open(file_path, "r") as file:
        data = json.load(file)
        task = data[index - 1]
        task["completed"] = True
        data[index - 1] = task
    with open(file_path , "w") as file:
        json.dump(data, file , indent=4)

def delete(index , file_path = filename):
    with open(file_path , "r") as file:
        index = index - 1
        data = json.load(file)
        data.pop(index)
        i = 1
        for task in data:
            task["index"] = i
            i+=1
    with open(file_path , "w") as file:
        json.dump(data, file , indent= 4)


@app.get("/")
def read_root():
    return {"Hello World"}


@app.get("/items")
def read_items():
    return list()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return list_id(item_id)

@app.post("/items/new")
def save_item(item_name: str):
    add(item_name)

@app.put("/items/{item_id}")
def update_item(item_id: int):
    complete(item_id)
    
    
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    delete(item_id)