from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello World"}

@app.get("/health")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item: ":item_id}