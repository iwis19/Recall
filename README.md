# Recall 🧠

Barebones RAG engine built with Python, Flask, &amp; Ollama; repo for personal reference

---

## Repository Note

Intentionally manually composed the pipeline was LangChain would wrap the same operations in abstractions and give me less control over other features I want to have for another project.

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
