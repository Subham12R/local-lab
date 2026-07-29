I’m unable to create or replace `CHECKLIST.md` because this session does not provide a file-writing tool. No project files were modified.

Below is the complete content to place in `/Users/subham/Dev/Python/Programming Fundamentals/Lume/CHECKLIST.md`:

```markdown
# LOCAL RAG AND AGENT ORCHESTRATION LAB

A local-only, CLI-first learning project for understanding retrieval-augmented generation and bounded agent orchestration using Python, MongoDB Community Server, Compass, and LM Studio.

## Project rules

- [ ] Keep the primary interface terminal-native: interactive CLI chat, not a web UI.
- [ ] Use local Python only.
- [ ] Use MongoDB Community Server locally.
- [ ] Use MongoDB Compass for visual inspection and verification.
- [ ] Use LM Studio for local chat and embedding models.
- [ ] Use PyMongo for MongoDB access.
- [ ] Use direct localhost HTTP requests to LM Studio.
- [ ] Use `pytest` for tests.
- [ ] Do not use cloud APIs, provider APIs, API keys, hosted databases, or hosted model services.
- [ ] Do not introduce LangChain, LlamaIndex, AutoGen, CrewAI, or similar frameworks initially.
- [ ] Prefer plain Python and small, understandable modules.
- [ ] Keep every feature explainable from first principles.
- [ ] Make all network communication explicitly local and inspectable.

---

## Phase 0 — Understand the system

### Goals

- [ ] Be able to explain the complete request path before writing application code.
- [ ] Understand the difference between ingestion, retrieval, generation, evaluation, and orchestration.
- [ ] Define what information is allowed to leave the local machine: nothing.
- [ ] Define the first useful user experience: a terminal chat that answers questions from locally stored documents.

### System flow

- [ ] User enters a question in the terminal.
- [ ] Python validates and normalizes the question.
- [ ] Python creates an embedding for the question using LM Studio.
- [ ] Python searches MongoDB for relevant document chunks.
- [ ] Python builds a grounded prompt containing retrieved context.
- [ ] Python sends the prompt to a local LM Studio chat model.
- [ ] Python prints the answer and useful source references in the terminal.
- [ ] Python records enough metadata to evaluate the result.
- [ ] If orchestration is later added, the agent may choose only from explicitly bounded local tools.

### Concepts to understand

- [ ] Documents versus chunks.
- [ ] Metadata versus content.
- [ ] Embeddings versus generated text.
- [ ] Similarity search versus keyword search.
- [ ] Retrieval context versus conversation history.
- [ ] Grounded answers versus unsupported model answers.
- [ ] Deterministic application logic versus probabilistic model output.
- [ ] Evaluation data versus training data.
- [ ] Feedback collection versus uncontrolled self-modification.
- [ ] A tool-using workflow versus an unrestricted autonomous agent.

### Completion check

- [ ] Draw or describe the system in your own words.
- [ ] Explain what MongoDB stores.
- [ ] Explain what LM Studio does.
- [ ] Explain why the application uses two model operations: embeddings and chat generation.
- [ ] Explain why the initial implementation should not use an orchestration framework.

---

## Phase 1 — Environment verification

### Repository and local tools

- [ ] Verify the project directory.
- [ ] Verify Python is installed.

```bash
python --version
python -m pip --version
```

- [ ] Verify Git is installed.

```bash
git --version
```

- [ ] Verify MongoDB Community Server is installed.

```bash
mongosh --version
```

- [ ] Verify MongoDB Compass is installed and can open.
- [ ] Verify LM Studio is installed and can open.
- [ ] Verify `pytest` can be run from Python once the environment exists.

### Python environment

- [ ] Create a virtual environment.

```bash
python -m venv .venv
```

- [ ] Activate it.

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

- [ ] Confirm the active interpreter.

```bash
python -c "import sys; print(sys.executable)"
```

- [ ] Install only the initial dependencies.

```bash
python -m pip install pymongo pytest
```

- [ ] Record installed packages.

```bash
python -m pip freeze
```

### LM Studio verification

- [ ] Open LM Studio.
- [ ] Download one local chat model appropriate for the available hardware.
- [ ] Download one local embedding model.
- [ ] Start the LM Studio local server.
- [ ] Confirm the server binds only to localhost.
- [ ] Record the local base URL, normally similar to:

```text
http://localhost:1234/v1
```

- [ ] Record the exact loaded chat model identifier.
- [ ] Record the exact loaded embedding model identifier.
- [ ] Do not create or configure a cloud provider key.
- [ ] Do not send test prompts to a hosted endpoint.

### MongoDB verification

- [ ] Start MongoDB Community Server locally.
- [ ] Confirm MongoDB is listening on localhost.
- [ ] Connect with `mongosh`.

```bash
mongosh
```

- [ ] Confirm the local server responds.
- [ ] Open Compass.
- [ ] Connect to the local MongoDB instance.
- [ ] Do not connect to MongoDB Atlas for this project.

### Completion check

- [ ] Python virtual environment works.
- [ ] PyMongo imports successfully.
- [ ] `pytest` runs.
- [ ] MongoDB accepts a local connection.
- [ ] Compass connects to the same local MongoDB instance.
- [ ] LM Studio serves both a chat model and an embedding model locally.

---

## Phase 2 — MongoDB fundamentals

### Learning goals

- [ ] Understand databases, collections, documents, fields, and indexes.
- [ ] Learn the difference between inserting, querying, updating, and deleting.
- [ ] Learn how PyMongo represents MongoDB documents.
- [ ] Learn how ObjectIds work.
- [ ] Learn why application metadata must be explicit and consistent.
- [ ] Learn how indexes affect query behavior.

### Required database

Use one local database:

```text
local_rag_lab
```

### Required collections

#### `documents`

Stores source-document metadata.

Suggested fields:

```text
_id
source_id
title
path
content_hash
source_type
created_at
updated_at
ingestion_status
chunk_count
metadata
```

Checklist:

- [ ] Insert a sample document.
- [ ] Read it back by `_id`.
- [ ] Query by `source_id`.
- [ ] Update its ingestion status.
- [ ] Delete the sample document.
- [ ] Add an index for `source_id`.
- [ ] Confirm the index in Compass.

#### `chunks`

Stores searchable text fragments.

Suggested fields:

```text
_id
source_id
chunk_id
text
text_hash
chunk_index
char_start
char_end
token_estimate
embedding
embedding_model
embedding_dimensions
metadata
created_at
```

Checklist:

- [ ] Insert several sample chunks.
- [ ] Query chunks belonging to one `source_id`.
- [ ] Query chunks in `chunk_index` order.
- [ ] Confirm that chunk text and metadata are stored together.
- [ ] Add an index for `source_id`.
- [ ] Decide how embedding dimensions will be validated.

#### `conversations`

Stores local chat-session information when persistence is enabled.

Suggested fields:

```text
_id
session_id
created_at
updated_at
messages
model
retrieval_settings
```

Checklist:

- [ ] Store a minimal conversation.
- [ ] Retrieve a conversation by `session_id`.
- [ ] Keep model configuration separate from message content where practical.
- [ ] Avoid storing secrets because this project should have none.

#### `runs`

Stores retrieval and generation traces for evaluation.

Suggested fields:

```text
_id
run_id
session_id
question
retrieved_chunk_ids
retrieval_scores
prompt_version
chat_model
embedding_model
answer
latency_ms
created_at
feedback
```

Checklist:

- [ ] Store one end-to-end run.
- [ ] Preserve the retrieved chunk IDs.
- [ ] Preserve the model names used.
- [ ] Preserve enough information to reproduce or inspect the result.
- [ ] Avoid storing unnecessary personal or sensitive information.

### Compass verification

- [ ] See `local_rag_lab` in Compass.
- [ ] See all required collections.
- [ ] Open sample documents and inspect field types.
- [ ] Verify timestamps are stored consistently.
- [ ] Verify embeddings are stored as arrays of numbers.
- [ ] Verify indexes exist and have the intended fields.
- [ ] Delete all temporary sample data after experimentation if it is not part of the project.

---

## Phase 3 — Ingestion

### Goals

- [ ] Define which local files are accepted.
- [ ] Read source files deterministically.
- [ ] Normalize text without destroying meaningful content.
- [ ] Compute a stable content hash.
- [ ] Avoid duplicating unchanged documents.
- [ ] Make ingestion repeatable and inspectable.

### Initial source scope

- [ ] Start with a small local directory of plain text or Markdown files.
- [ ] Do not begin with PDFs, websites, cloud drives, or remote URLs.
- [ ] Use files that are safe to store locally.
- [ ] Keep a small test fixture directory separate from personal documents.

### Ingestion checklist

- [ ] Enumerate files in a deterministic order.
- [ ] Ignore hidden files and unsupported extensions.
- [ ] Read files with an explicit encoding.
- [ ] Normalize line endings.
- [ ] Preserve the original relative path as metadata.
- [ ] Compute a content hash.
- [ ] Upsert one record in `documents`.
- [ ] Remove or replace old chunks when a source changes.
- [ ] Record ingestion status and chunk count.
- [ ] Make rerunning ingestion safe.
- [ ] Report skipped files and failures clearly in the terminal.
- [ ] Add tests for empty files, duplicate content, unsupported files, and changed files.

### Completion check

- [ ] Running ingestion twice does not create duplicate source records.
- [ ] Changing a source updates its content hash.
- [ ] Changed documents do not retain stale chunks.
- [ ] Compass shows the expected document and chunk records.

---

## Phase 4 — Chunking

### Goals

- [ ] Understand why retrieval works on chunks rather than entire documents.
- [ ] Choose a simple, explainable chunking strategy.
- [ ] Preserve source location metadata.
- [ ] Avoid splitting text into unusably small or excessively large pieces.

### Initial strategy

- [ ] Start with paragraph or line-aware chunking.
- [ ] Use a configured maximum character length.
- [ ] Use a small overlap only when it improves continuity.
- [ ] Keep the algorithm deterministic.
- [ ] Do not add a tokenizer dependency initially unless measurement requires it.

### Chunking checklist

- [ ] Define `chunk_size`.
- [ ] Define `chunk_overlap`.
- [ ] Preserve paragraph boundaries where possible.
- [ ] Preserve `chunk_index`.
- [ ] Record character offsets when practical.
- [ ] Store the source ID on every chunk.
- [ ] Store a chunk hash.
- [ ] Reject empty chunks.
- [ ] Test short text.
- [ ] Test text exactly at the boundary.
- [ ] Test long paragraphs.
- [ ] Test multiple paragraphs.
- [ ] Test repeated ingestion.
- [ ] Inspect real chunks in Compass.
- [ ] Record examples where chunking loses useful context.

---

## Phase 5 — Local embeddings

### Goals

- [ ] Understand embeddings as numeric representations of text.
- [ ] Use an embedding model served by LM Studio.
- [ ] Understand that query and document embeddings must be compatible.
- [ ] Record the model name and vector dimensions.
- [ ] Keep embedding generation local.

### HTTP checklist

- [ ] Identify the local embedding endpoint.
- [ ] Confirm the endpoint is a localhost URL.
- [ ] Send a small test request directly with Python.
- [ ] Check HTTP status codes.
- [ ] Parse the JSON response.
- [ ] Validate the returned vector is numeric.
- [ ] Validate vector dimensions.
- [ ] Add a request timeout.
- [ ] Produce an actionable error if LM Studio is unavailable.
- [ ] Never fall back silently to a cloud endpoint.

### Storage checklist

- [ ] Embed every accepted chunk.
- [ ] Store the vector in the corresponding `chunks` record.
- [ ] Store `embedding_model`.
- [ ] Store `embedding_dimensions`.
- [ ] Validate dimensions before storage and retrieval.
- [ ] Decide how model changes trigger re-embedding.
- [ ] Do not mix vectors from incompatible embedding models.

### Learning checks

- [ ] Compare embeddings for related text.
- [ ] Compare embeddings for unrelated text.
- [ ] Learn the chosen similarity metric.
- [ ] Implement or understand cosine similarity in plain Python.
- [ ] Test zero-length and malformed vectors.
- [ ] Measure approximate embedding latency locally.

---

## Phase 6 — Retrieval

### Goals

- [ ] Retrieve relevant chunks for a user question.
- [ ] Understand the difference between exact matching and semantic similarity.
- [ ] Keep retrieval behavior inspectable.
- [ ] Return source references with results.

### Initial retrieval implementation

- [ ] Embed the user question locally.
- [ ] Load candidate chunks from MongoDB.
- [ ] Calculate similarity in Python initially if that is simplest to understand.
- [ ] Rank candidates by similarity.
- [ ] Return a configurable top `k`.
- [ ] Apply a minimum similarity threshold only after observing results.
- [ ] Include source metadata and scores.
- [ ] Avoid returning duplicate or nearly identical chunks where possible.
- [ ] Preserve retrieval timing.

### Retrieval tests

- [ ] Test a question with an obvious matching chunk.
- [ ] Test a question with no relevant chunk.
- [ ] Test multiple relevant chunks.
- [ ] Test malformed or missing embeddings.
- [ ] Test incompatible vector dimensions.
- [ ] Test `top_k` limits.
- [ ] Test deterministic ordering for equal scores.
- [ ] Test that source IDs are preserved.

### CLI inspection

- [ ] Add a maintenance command to inspect retrieval without generation.
- [ ] Print the query.
- [ ] Print chunk IDs, source names, scores, and short text previews.
- [ ] Make it possible to diagnose bad answers as retrieval failures or generation failures.

---

## Phase 7 — Grounded generation

### Goals

- [ ] Generate answers using retrieved local context.
- [ ] Make the model’s grounding constraints explicit.
- [ ] Distinguish known context from conversation history.
- [ ] Return useful source references.

### Prompt checklist

- [ ] Define a system instruction requiring grounded answers.
- [ ] Tell the model to say when the context is insufficient.
- [ ] Include retrieved chunks with clear source labels.
- [ ] Include the user question separately.
- [ ] Avoid claiming that the model searched the internet.
- [ ] Avoid asking the model to invent citations.
- [ ] Keep the prompt format stable and version it.
- [ ] Limit context size deliberately.
- [ ] Escape or delimit document content clearly.
- [ ] Treat retrieved text as data, not as instructions.

### Local chat checklist

- [ ] Call the LM Studio chat endpoint over localhost HTTP.
- [ ] Use the configured local chat model.
- [ ] Set a request timeout.
- [ ] Handle server-unavailable errors.
- [ ] Handle malformed responses.
- [ ] Print the answer in the terminal.
- [ ] Print source references after the answer.
- [ ] Preserve the run metadata in `runs`.
- [ ] Make temperature and other generation settings explicit.
- [ ] Keep the initial conversation loop simple.

### Grounding tests

- [ ] Ask a question answered directly by one chunk.
- [ ] Ask a question requiring several chunks.
- [ ] Ask a question not supported by the documents.
- [ ] Confirm unsupported questions receive an uncertainty response.
- [ ] Confirm source references correspond to retrieved chunks.
- [ ] Test context containing misleading instructions.
- [ ] Test a long conversation without allowing history to overwhelm retrieved context.

---

## Phase 8 — Evaluation

### Goals

- [ ] Measure retrieval and answer quality rather than relying only on intuition.
- [ ] Separate retrieval errors from generation errors.
- [ ] Create a small, reviewable local evaluation set.

### Evaluation dataset

- [ ] Create a local set of representative questions.
- [ ] Record expected source documents or chunks.
- [ ] Record a short expected answer or key facts.
- [ ] Include answerable questions.
- [ ] Include unanswerable questions.
- [ ] Include questions requiring multiple chunks.
- [ ] Include ambiguous questions.
- [ ] Keep evaluation data version-controlled only if it contains no sensitive content.

### Metrics and review

- [ ] Measure retrieval hit rate.
- [ ] Review whether the top result is relevant.
- [ ] Review whether the answer is supported.
- [ ] Track unsupported claims.
- [ ] Track refusal or uncertainty behavior.
- [ ] Track latency for embedding, retrieval, and generation separately.
- [ ] Track model names and prompt versions.
- [ ] Compare changes against a baseline.
- [ ] Do not optimize only for answer fluency.

### Test checklist

- [ ] Add unit tests for chunking and similarity.
- [ ] Add tests for LM Studio response parsing.
- [ ] Add tests for MongoDB persistence behavior.
- [ ] Add integration tests that can run against local services.
- [ ] Mark service-dependent tests clearly.
- [ ] Run:

```bash
pytest
```

- [ ] Record failures and determine whether they are code, data, model, or environment issues.

---

## Phase 9 — Feedback and controlled improvement

### Goals

- [ ] Collect explicit user feedback locally.
- [ ] Use feedback to identify improvements.
- [ ] Prevent feedback from silently changing behavior.
- [ ] Keep every change reviewable and reversible.

### Feedback checklist

- [ ] Allow the user to mark an answer useful or not useful.
- [ ] Allow optional free-text feedback.
- [ ] Store feedback linked to `run_id`.
- [ ] Store a timestamp.
- [ ] Store the retrieval and prompt configuration used.
- [ ] Avoid storing sensitive conversation data unnecessarily.
- [ ] Make feedback opt-in if content may be sensitive.

### Controlled improvement loop

- [ ] Inspect negative feedback manually.
- [ ] Classify the issue: ingestion, chunking, embedding, retrieval, prompt, model, or orchestration.
- [ ] Add a regression example before changing behavior.
- [ ] Change one variable at a time.
- [ ] Run the evaluation set.
- [ ] Compare against the baseline.
- [ ] Record the reason for the change.
- [ ] Keep prompt versions explicit.
- [ ] Re-embed only when the embedding model or source representation changes.
- [ ] Never let the application rewrite its own code or configuration automatically.
- [ ] Never allow feedback to authorize unrestricted tools.
- [ ] Do not introduce automatic online learning.

### Completion check

- [ ] A negative result can be traced to a specific pipeline stage.
- [ ] Improvements are implemented as reviewed code or configuration changes.
- [ ] Previous behavior can be restored.
- [ ] Evaluation results are recorded locally.

---

## Phase 10 — Bounded plain-Python agent orchestration

### Goals

- [ ] Understand orchestration as controlled sequencing of known operations.
- [ ] Keep the agent bounded, observable, and local.
- [ ] Use plain Python before considering an agent framework.

### Initial tools

Define only a small allowlist of local tools, for example:

- [ ] `search_documents`
- [ ] `get_document`
- [ ] `retrieve_context`
- [ ] `answer_from_context`
- [ ] `save_feedback`
- [ ] `show_run_details`

### Orchestration constraints

- [ ] Define a finite maximum number of steps.
- [ ] Define a finite maximum number of retrieval attempts.
- [ ] Validate every tool name against an allowlist.
- [ ] Validate every tool argument.
- [ ] Reject filesystem paths outside the permitted project or source directory.
- [ ] Do not allow shell command execution from model output.
- [ ] Do not allow arbitrary Python execution.
- [ ] Do not allow network access outside localhost.
- [ ] Do not allow model-generated URLs to be fetched.
- [ ] Do not allow database commands generated directly by the model.
- [ ] Use application-defined MongoDB queries.
- [ ] Log every selected tool and result.
- [ ] Stop on repeated failures.
- [ ] Stop when the answer is sufficiently grounded.
- [ ] Return a clear failure state when no safe action is available.
- [ ] Keep a human-readable trace for debugging.

### Plain-Python design

- [ ] Represent each tool as a normal Python function.
- [ ] Define explicit input and output structures.
- [ ] Define an orchestration state object.
- [ ] Separate planning from tool execution.
- [ ] Validate model suggestions before execution.
- [ ] Keep the model unable to bypass application checks.
- [ ] Prefer a state machine or bounded loop over unrestricted recursion.
- [ ] Make the maximum number of steps configurable.
- [ ] Add tests for invalid tools, invalid arguments, timeouts, repeated failures, and successful completion.

### CLI behavior

- [ ] Keep interactive chat as the primary interface.
- [ ] Allow the user to inspect the orchestration trace.
- [ ] Provide a command to reset the current session.
- [ ] Provide a command to quit cleanly.
- [ ] Print when retrieval occurs.
- [ ] Print which sources were used.
- [ ] Print when the system cannot answer from local context.
- [ ] Never hide model or tool failures behind a generic answer.

---

## Exact initial project structure

Create this structure before implementing application behavior:

```text
LOCAL RAG AND AGENT ORCHESTRATION LAB/
├── .gitignore
├── README.md
├── CHECKLIST.md
├── pyproject.toml
├── app/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── cli.py
│   ├── db.py
│   ├── models.py
│   ├── ingest.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── generation.py
│   ├── evaluation.py
│   ├── feedback.py
│   └── orchestration.py
├── tests/
│   ├── __init__.py
│   ├── test_chunking.py
│   ├── test_embeddings.py
│   ├── test_retrieval.py
│   ├── test_generation.py
│   └── test_orchestration.py
├── data/
│   ├── sources/
│   └── fixtures/
├── evaluation/
│   └── questions.json
└── notes/
    └── learning-log.md
```

Initial structure checklist:

- [ ] Create the empty Git repository first.
- [ ] Create the directories and placeholder files above.
- [ ] Do not write application code as the first task.
- [ ] Keep personal source documents out of version control.
- [ ] Keep test fixtures small and non-sensitive.
- [ ] Add a short README explaining local-only constraints.

---

## Command checklist

### Environment commands

```bash
python --version
python -m venv .venv
source .venv/bin/activate
python -m pip install pymongo pytest
python -m pip freeze
```

### Test commands

```bash
pytest
pytest -q
pytest tests/test_chunking.py
pytest tests/test_retrieval.py
```

### Application commands

The application’s primary interface must be:

```bash
python -m app
```

Expected behavior:

- [ ] Start an interactive terminal chat.
- [ ] Display a clear startup message.
- [ ] Confirm local service configuration without exposing secrets.
- [ ] Accept repeated questions.
- [ ] Display grounded answers and source references.
- [ ] Handle empty input.
- [ ] Handle Ctrl-C and EOF cleanly.
- [ ] Provide a clear quit command such as `/quit`.
- [ ] Never require a browser.

Maintenance commands should be available through a documented CLI interface, for example:

```bash
python -m app ingest
python -m app ingest --path data/sources
python -m app retrieve "example question"
python -m app evaluate
python -m app status
python -m app reindex
python -m app show-run RUN_ID
python -m app clear-session
```

Maintenance command checklist:

- [ ] `ingest` imports or updates local source files.
- [ ] `retrieve` inspects retrieval without generation.
- [ ] `evaluate` runs the local evaluation set.
- [ ] `status` checks MongoDB and LM Studio connectivity.
- [ ] `reindex` safely rebuilds embeddings when explicitly requested.
- [ ] `show-run` displays a stored local trace.
- [ ] `clear-session` removes or resets the selected conversation.
- [ ] Destructive commands require explicit confirmation.
- [ ] Every command has `--help`.
- [ ] Every command reports errors with actionable messages.

---

## Security and Git checks

### Local-only security

- [ ] Confirm all model URLs use `localhost` or `127.0.0.1`.
- [ ] Confirm MongoDB uses a local connection.
- [ ] Search source code for cloud provider URLs.
- [ ] Search source code for API-key environment variables.
- [ ] Remove accidental tokens, credentials, and secrets.
- [ ] Do not add `.env` files containing secrets to Git.
- [ ] Do not log complete sensitive documents unnecessarily.
- [ ] Do not expose MongoDB or LM Studio ports publicly.
- [ ] Do not enable arbitrary tool execution.
- [ ] Do not allow model output to become shell commands.
- [ ] Set timeouts on HTTP and database operations.
- [ ] Validate all paths and tool arguments.
- [ ] Keep dependencies minimal and reviewable.

### `.gitignore` checks

Include appropriate local-only exclusions such as:

```gitignore
.venv/
__pycache__/
.pytest_cache/
*.py[cod]
.env
.env.*
data/sources/*
data/processed/*
*.log
.DS_Store
```

- [ ] Keep safe example fixtures tracked separately from private sources.
- [ ] Check staged files before every commit.

```bash
git status
git diff
git diff --cached
git ls-files
```

- [ ] Confirm no secrets or private documents are staged.
- [ ] Confirm no virtual environment is staged.
- [ ] Confirm no model files are accidentally staged.
- [ ] Confirm the project remains local-only.

---

## Learning-session wrap-up checklist

At the end of every learning session:

- [ ] Write down what concept was studied.
- [ ] Record what was implemented or inspected.
- [ ] Record one thing that was unclear.
- [ ] Record one experiment and its result.
- [ ] Record any errors and their root causes.
- [ ] Run the narrowest relevant tests.
- [ ] Run the full test suite when practical.
- [ ] Inspect `git diff`.
- [ ] Inspect `git status`.
- [ ] Remove temporary debugging output.
- [ ] Remove temporary sample data when appropriate.
- [ ] Confirm no secrets or private files are staged.
- [ ] Update the learning log.
- [ ] Write the next small, concrete task.
- [ ] Stop with the project in a reproducible state.

---

## Current next step

The first task is **create the empty Git repository, not application code**.

Checklist:

- [ ] Open a terminal in the project directory.
- [ ] Initialize an empty repository:

```bash
git init
```

- [ ] Confirm the repository is empty and has no accidental files staged:

```bash
git status
```

- [ ] Do not implement the CLI yet.
- [ ] Do not connect to MongoDB yet.
- [ ] Do not call LM Studio yet.
- [ ] After the empty repository exists, create the initial project structure.
- [ ] Add `.gitignore`, `README.md`, and this checklist.
- [ ] Review the structure before beginning Phase 1.
```