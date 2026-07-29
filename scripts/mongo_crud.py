from datetime import datetime, timezone

from src.app.database import get_database

def main() -> None:
    database = get_database()
    collection = database["demo"]

    collection.create_index("kind")

    document = {
        "kind": "crud-demo",
        "message": "Testing mongo collection sample",
        "created_at": datetime.now(timezone.utc),
    }

    insert_result = collection.insert_one(document)
    document_id = insert_result.inserted_id

    print(f"Inserted document with id: {document_id}")

    found_document = collection.find_one({"_id": document_id})
    print(f"Found document: {found_document}")

    update_result = collection.update_one(
        {"_id": document_id},
        {"$set": {"message": "Updated data"}},
    )

    print(f"Update result: {update_result.modified_count}")

    updated_document = collection.find_one({"_id": document_id})
    print(f"Updated document: {updated_document}")

    input("\nInspect the demo collection in MongoDB "
        "and press Enter to continue")

    delete_result = collection.delete_one({"_id": document_id})
    print(f"Delete result: {delete_result.deleted_count}")

if __name__ == "__main__":
    main()