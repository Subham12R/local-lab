from pymongo.errors import CollectionInvalid

from src.app.database import get_database

COLLECTIONS = (
    "documents",
    "chunks",
    "query_logs",
    "feedback",
    "eval_cases",
    "eval_runs",
    "improvement_proposals",
)

def create_collections() -> None:
    db = get_database()

    for collection_name in COLLECTIONS:
        try:
            db.create_collection(collection_name)
            print(f"Collection '{collection_name}' created.")
        except CollectionInvalid:
            print(f"Collection '{collection_name}' already exists.")

    db["documents"].create_index(
        "source_path",
        name = "source_path_index",
    )

    db["chunks"].create_index(
        "document_id",
        name = "document_id_index",
    )

    db["query_logs"].create_index(
        "query_id",
        name = "query_id_index",
    )

    db["feedback"].create_index(
        "feedback_id",
        name = "feedback_id_index",
    )

    db["eval_cases"].create_index(
        "eval_case_id",
        name = "eval_case_id_index",
    )

    db["eval_runs"].create_index(
        "eval_run_id",
        name = "eval_run_id_index",
    )

    db["improvement_proposals"].create_index(
        "improvement_proposal_id",
        name = "improvement_proposal_id_index",
    )

    print("Indexes created for all collections.")

if __name__ == "__main__":
    create_collections()
