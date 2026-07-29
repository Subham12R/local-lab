import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

from src.app.database import get_database

def normalize_text(text: str) -> str:
    lines = [line.rstrip() for line in text.replace("\r\n" , "\n").split("\n")]
    return "\n".join(lines).strip()

def calculate_content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def ingest_doc(file_path: Path) -> None:
    if not file_path.exists():
        return

    if not file_path.is_file():
        return

    if file_path.suffix.lower() not in [".txt", ".md"]:
        return

    raw_text = file_path.read_text(encoding="utf-8")
    normalized_text = normalize_text(raw_text)

    if not normalized_text:
        return

    content_hash = calculate_content_hash(normalized_text)

    db = get_database()
    collection = db["documents"]

    existing_doc = collection.find_one(
        {"content_hash": content_hash},
        {"_id": 1, "source_path": 1}
    )
    if existing_doc:
        print(f"Duplicate document found: {existing_doc['source_path']}")
        return

    document = {
        "title": file_path.stem.replace("_", "").title(),
        "source_path": str(file_path),
        "content_hash": content_hash,
        "topic": "python-basics",
        "difficulty": "beginner",
        "raw_text": raw_text,
        "created_at": datetime.now(timezone.utc),
    }   

    result = collection.insert_one(document)
    print(f"Inserted document: {result.inserted_id}")
    print(f"Document: {document}")
    print(f"Characters: {len(normalized_text)}")
    print(f"Content_hash: {content_hash}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ingest_doc.py <file_path>")
        sys.exit(1)
    ingest_doc(Path(sys.argv[1]))