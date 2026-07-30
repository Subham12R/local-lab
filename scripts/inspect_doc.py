import sys

from bson import ObjectId
from bson.errors import InvalidId

from src.app.database import get_database

def inspect_doc(doc_id:str) -> None:
    try:
        obj_id = ObjectId(doc_id)
        
    except InvalidId as error:
        raise SystemExit(f"Invalid document ID: {doc_id}, {error}")

    db = get_database()
    doc = db["documents"].find_one({"_id":obj_id})

    if doc is None:
        raise SystemExit(f"Document not found: {doc_id}")

    print(f"ID: {doc['_id']}")
    print(f"Title: {doc.get('title', 'N/A')}")
    print(f"Content: {doc.get('content_hash', 'N/A')}")
    print(f"Created At: {doc.get('created_at', 'N/A')}")
    print(f"Updated At: {doc.get('updated_at', 'N/A')}")
    print(doc.get("raw_text", ""))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        raise SystemExit("Usage: inspect_doc.py <doc_id>")
    inspect_doc(sys.argv[1])