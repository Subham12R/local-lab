import os

from pymongo import MongoClient
from pymongo.database import Database

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "lab")

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=3000,
)

def get_database() -> Database: 
    return client[MONGODB_DATABASE]

def ping_database()-> bool:
    client.admin.command("ping")
    return True

    