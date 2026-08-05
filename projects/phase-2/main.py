from routes import router
import fastapi
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database_setup import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run( app , host = "127.0.0.1" , port = 8000)