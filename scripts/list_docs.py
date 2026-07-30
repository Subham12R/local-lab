from pymongo.errors import CollectionInvalid

from src.app.database import get_database


def get_documents():
    db = get_database()

    proj = {
        "raw_text": 0
    }

    return list(
        db["documents"].find({}, proj).sort("created_at", 1)
    )

def main() -> None: 
    docs = get_documents()

    if not  docs: 
        print("No Docs found.")
        return
    print("Documents")
    print("-"*130)

    print(f"Total Doc: {len(docs)}")
    print(
        f"{'ID':24} "
        f"{'Title':25} "
        f"{'Topic':18} "
        f"{'Difficulty':12} "
        f"{'Source':30} "
        f"{'Created':20}"
    )
    print("-"*130)
    
    for doc in docs:
        created_at = doc.get('created_at', '')
        created_text = str(created_at)[:20] if created_at else ""
        print(
             f"{str(doc['_id']):24} "
             f"{doc.get('title', '')[:25]:25} "
             f"{doc.get('topic', '')[:18]:18} "
             f"{doc.get('difficulty', '')[:12]:12} "
             f"{doc.get('source_path', '')[:30]:30} "
             f"{created_text:20}"
         )

if __name__ == "__main__":
    main()