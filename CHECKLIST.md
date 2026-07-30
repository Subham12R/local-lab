# Local RAG and Agent Orchestration Lab — Checklist

A local-only learning project for building a small RAG system and bounded agent workflow from first principles.

## Project Guardrails

- [x] Primary interface: terminal-native interactive chat.
- [x] Local database: MongoDB Community Server.
- [x] Database inspection: MongoDB Compass.
- [x] Local model runtime: LM Studio.
- [x] Python package/environment management: `uv`.
- [x] FastAPI is installed but deferred as a thin localhost API layer.
- [ ] Any future FastAPI server binds to `127.0.0.1` only.
- [x] No frontend, cloud deployment, paid services, or provider API keys.
- [x] No LangChain, LangGraph, CrewAI, AutoGen, or similar frameworks initially.
- [ ] Never commit `.env` files, private documents, databases, or model files.
- [ ] Keep RAG logic in plain, testable Python modules.

---

## Phase 0 — Understand the System

- [x] Define the project as a local RAG learning lab, not a production startup.
- [x] Define the narrow initial corpus: Python fundamentals, starting with Python lists.
- [x] Define the RAG request flow:
  - question → query embedding → retrieval → grounded prompt → local answer → citations → log
- [x] Define the terminal-native chat as the primary interface.
- [x] Create the Git repository.
- [x] Configure GitHub SSH authentication and push the repository.
- [x] Create the initial folders and safe Git ignore rules.
- [x] Start the README.
- [x] Create this project checklist.

## Phase 1 — Local Environment Verification

### Python and dependencies

- [x] Verify Python 3.11.
- [x] Create the `.venv` virtual environment.
- [x] Repair `pip` inside `.venv`.
- [x] Verify the active interpreter is inside `.venv`.
- [x] Install `pymongo`.
- [x] Install `httpx`.
- [x] Install `pytest`.
- [x] Install FastAPI for the later localhost API milestone.
- [ ] Add and verify `uvicorn` when the FastAPI server is actively used.
- [x] Record project dependencies in `pyproject.toml` / `requirements.txt`.

### MongoDB and Compass

- [x] Verify MongoDB Community Server accepts a local connection.
- [x] Verify PyMongo can ping MongoDB.
- [x] Connect MongoDB Compass to the local MongoDB server.
- [x] Use the `local_rag_lab` database.

### LM Studio

- [x] Start the LM Studio local server.
- [x] Load local chat and embedding-capable models.
- [ ] List loaded models through `GET http://localhost:1234/v1/models`.
- [ ] Send one minimal local chat completion request.
- [ ] Send one minimal local embedding request.
- [ ] Record the model IDs used for chat and embeddings.

---

## Phase 2 — MongoDB Fundamentals

- [x] Create `src/app/database.py` with local MongoDB configuration and a ping function.
- [x] Create a basic FastAPI app / MongoDB health-check experiment.
- [x] Insert a safe sample record.
- [x] Query a record by `_id`.
- [x] Update a safe sample record.
- [x] Delete a safe sample record.
- [x] Inspect CRUD data in MongoDB Compass.
- [x] Learn `ObjectId`, projections, `find_one`, `update_one`, and `delete_one`.
- [x] Create the project collections:
  - [x] `documents`
  - [x] `chunks`
  - [x] `query_logs`
  - [x] `feedback`
  - [x] `eval_cases`
  - [x] `eval_runs`
  - [x] `improvement_proposals`
- [x] Create initial indexes for document hashes, chunks, request IDs, and evaluation data.

---

## Phase 3 — Ingestion

- [x] Create a safe Python Lists Markdown sample.
- [x] Read local `.md` and `.txt` files with UTF-8 encoding.
- [x] Normalize source text.
- [x] Compute a SHA-256 content hash.
- [x] Store a source document in `documents`.
- [x] Detect and skip duplicate content.
- [x] Correct an accidental source-data issue discovered during inspection.
- [x] List document metadata without printing full text.
- [x] Inspect a single document by `ObjectId`.
- [x] Handle invalid and nonexistent document IDs.
- [ ] Replace temporary scripts with the final `python -m app ingest` command.
- [ ] Support a directory of trusted source files.
- [ ] Update changed documents and remove their stale chunks.

---

## Phase 4 — Chunking

- [x] Explain why RAG retrieves chunks rather than whole documents.
- [ ] Implement a basic chunking function with configurable size and overlap.
- [ ] Preserve section metadata using Markdown headings.
- [ ] Create chunk documents with source metadata.
- [ ] Run chunking for the verified Python Lists document.
- [ ] Store chunks in the `chunks` collection.
- [ ] Verify `document_id` is an `ObjectId`.
- [ ] Verify chunk indexes begin at `0` and are ordered.
- [ ] Verify every chunk has `text`, `section`, source metadata, and `embedding: null`.
- [ ] Inspect chunks in MongoDB Compass.
- [ ] Add a clean `inspect-chunks` command.
- [ ] Add chunking tests for short text, boundaries, overlap, and invalid settings.

### Current next step

Implement the chunking function and a script that stores chunks for one document.

---

## Phase 5 — Local Embeddings

- [ ] Explain embeddings and vector dimensions.
- [ ] Implement an LM Studio embedding client using local HTTP only.
- [ ] Handle unavailable servers and no loaded embedding model.
- [ ] Embed every chunk.
- [ ] Store `embedding`, model name, and vector dimensions.
- [ ] Verify a safe embedding sample and its vector length.
- [ ] Re-embed when the embedding model changes.

## Phase 6 — Retrieval

- [ ] Embed the question locally.
- [ ] Implement cosine similarity in plain Python.
- [ ] Rank chunks and return configurable top-k results.
- [ ] Print score, chunk text, section, and source metadata.
- [ ] Validate retrieval before building answer generation.

## Phase 7 — Grounded Local Answer Generation

- [ ] Build a prompt from retrieved context and the user question.
- [ ] Require answers to use only retrieved context.
- [ ] Require citations with source title and section.
- [ ] Require refusal if retrieved context is insufficient.
- [ ] Call LM Studio’s local chat endpoint.
- [ ] Store query logs, chunk IDs, scores, answer, citations, model name, and latency.
- [ ] Build the first interactive terminal chat loop.

## Phase 8 — Evaluation

- [ ] Create 10 answerable, 3 ambiguous, and 3 refusal evaluation cases.
- [ ] Store evaluation cases in MongoDB.
- [ ] Check retrieval relevance and citation support.
- [ ] Write local JSON or Markdown evaluation reports.
- [ ] Store runs and metrics in `eval_runs`.

## Phase 9 — Feedback and Controlled Improvement

- [ ] Log helpful and not-helpful feedback by request ID.
- [ ] Classify retrieval, missing-knowledge, chunking, prompt, hallucination, citation, and unsupported-question failures.
- [ ] Store improvement proposals only; do not automatically change the system.
- [ ] Evaluate every candidate change against the golden dataset.
- [ ] Version chunk settings, prompts, and model names.

## Phase 10 — Bounded Agent Orchestration

- [ ] Implement bounded plain-Python roles: ingestion, retrieval, answer, evaluation, and improvement.
- [ ] Implement an explicit workflow:
  - ingest → validate → evaluate → analyze failures → propose improvement → evaluate candidate → report
- [ ] Restrict filesystem, shell, network, and database actions to explicit allowlists.
- [ ] Prevent automatic system modifications.
- [ ] Add orchestration traces and tests.

---

## End-of-Session Checklist

- [ ] Record concepts learned in `docs/learning-log.md`.
- [ ] Run the narrowest relevant verification or test.
- [ ] Inspect MongoDB Compass when data was changed.
- [ ] Review `git diff` and `git status`.
- [ ] Verify no private files or secrets are staged.
- [ ] Write the next small task.
- [ ] Choose one focused Git commit message.
