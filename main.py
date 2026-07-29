from fastapi import FastAPI, HTTPException
from pymongo.errors import PyMongoError

from src.app.database import MONGODB_DATABASE, ping_database, get_database

app = FastAPI(
    title="Local RAG Agent Lab",
    description="A local RAG agent lab that uses a FastAPI backend and MongoDB database.",
    version="0.1.0",
)

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Local RAG Agent Lab!"}

@app.get("/health")
def health() -> dict[str, str]:
    try: 
        ping_database()
    except PyMongoError as error:
        raise HTTPException(
            status_code=503, 
            detail=f"MongoDB is unavailable: {error}",
        ) from error
    return {
        "status": "ok",
        "mongodb": "connected",
        "database": MONGODB_DATABASE,
    }