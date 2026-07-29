# Local RAG and Agent Orchestration Lab

## Purpose

This is a local-only learning project for understanding Applied AI engineering by building a small Retrieval-Augmented Generation system from first principles.

The project will use a terminal-native interactive chat interface rather than a web UI.

## Learning Goals

- Python engineering
- Local LLM inference
- Document ingestion
- Text chunking
- Embeddings
- Vector retrieval
- Grounded prompt construction
- Evaluation and debugging
- MongoDB data modeling
- Feedback-driven improvement
- Bounded agent orchestration
- GitHub documentation

## Constraints

- CLI and terminal-native only
- No frontend or web UI
- No cloud deployment
- No external model APIs
- No provider API keys
- No paid services
- MongoDB Community Server runs locally
- LM Studio provides local chat and embedding inference
- No LangChain, LangGraph, CrewAI, or AutoGen initially
- Private documents, databases, secrets, and model files must never be committed

## Initial Corpus

Version one will use a small trusted corpus about Python fundamentals, beginning with Python lists.

The project will not ingest the entire internet or general programming knowledge.

## Architecture

```text
Terminal chat
    ↓
Python application
    ↓
Question embedding through LM Studio
    ↓
Relevant chunk retrieval from MongoDB
    ↓
Grounded prompt construction
    ↓
Local answer generation through LM Studio
    ↓
Answer and citations printed in the terminal
    ↓
Query logged in MongoDB
