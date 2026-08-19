import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from chromadb.config import Settings

class Datastore:

    def __init__(self):
        # PersistentClient saves the vector database to disk, so indexed data survives app restarts
        self.client = chromadb.PersistentClient(path="./chroma_db", settings=Settings(allow_reset=True))
        # chroma uses this embedding function to turn text into vectors when adding or querying documents
        self.embedding_function = OllamaEmbeddingFunction(
            url="http://localhost:11434",
            model_name="nomic-embed-text:latest"
        )
        self.collection = self.client.get_or_create_collection(
            name="collection",
            embedding_function=self.embedding_function
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