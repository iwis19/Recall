# Recall 🧠

Barebones RAG engine built with Python, Flask, &amp; Ollama; repo for personal reference

---

## Repository Note

Intentionally manually composed the pipeline was LangChain would wrap the same operations in abstractions and give me less control over other features I want to have for [another project](https://github.com/iwis19/GitTrace).

---

## Key Features

1. PDF text extraction
2. Recursive text chunking
3. Local embeddings
4. Dense-vector retrieval

---

## Tech Stack

- Python 3.14.6 (pypdf, LangChain)
- Flask
- ChromaDB
- Ollama
- HTML/CSS/TS
- Docker

---

## Setup

This project runs with Docker Compose since `ollama` and `recall` are split into two separate services.

<br>

Build and start the services:
```bash 
docker compose up -d --build
```

Pull embedding model:
```bash 
docker compose exec ollama ollama pull nomic-embed-text
```

Then pull a small qwen model for answering:
```bash 
docker compose exec ollama ollama pull qwen2.5:3b
```

<br>

Open at [localhost:8080/context](http://localhost:8080/context)

---

## Project Structure

```text
Recall/
├── app/
│   ├── routes.py
│   ├── form.py
│   ├── templates/
│   └── static/
├── rag/
│   ├── rag_pipeline.py
│   ├── indexer.py
│   ├── datastore.py
│   ├── retriever.py
│   ├── response_generator.py
│   ├── guardrail.py
│   └── evaluator.py
├── context/
├── chroma_db/
└── README.md
```

--- 

## License
MIT
