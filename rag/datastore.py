import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from chromadb.config import Settings

import ollama

class Datastore:

    def __init__(self):
        self.ollama_url = "http://localhost:11434"
        self.embedding_model_name = "nomic-embed-text:latest"

        # PersistentClient saves the vector database to disk, so indexed data survives app restarts
        self.client = chromadb.PersistentClient(path="./chroma_db", settings=Settings(allow_reset=True))

        # chroma uses this embedding function to turn text into vectors when adding or querying documents
        self.embedding_function = OllamaEmbeddingFunction(
            url=self.ollama_url,
            model_name=self.embedding_model_name
        )

        self.collection = self.client.get_or_create_collection(
            name="collection",
            embedding_function=self.embedding_function
        )

        self.ollama_client = ollama.Client(
            host=self.ollama_url
        )

    # warm up embedding model, does not add anything to chromadb, only returns a vec
    def warm_embedding_model(self):
        self.ollama_client.embed(
            model=self.embedding_model_name,
            input="warmup",
            keep_alive="10m"
        )
        
    def get_collection(self):
        return self.collection
    
    def build_collection(self, chunks: list):
        # embeddings are generated automatically because the collection already has an embedding function
        self.collection.add(
            ids=[f"id{i}" for i in range(1, len(chunks)+1)],
            documents=chunks,
            metadatas=[{"source": "profile.txt", "info_chunk_index": i} for i in range(1, len(chunks)+1)]
        )

    def clear_collection(self):
        all_ids = self.collection.get()["ids"]
        if all_ids:
            self.collection.delete(ids=all_ids)

    def is_empty(self):
        return self.collection.count() == 0

# testing
# ds = Datastore()
# print(ds.get_collection())