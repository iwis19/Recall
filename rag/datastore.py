import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from rag.indexer import Indexer

class Datastore:

    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.embedding_function = OllamaEmbeddingFunction(
            url="http://localhost:11434",
            model_name="nomic-embed-text:latest"
        )
        self.collection = self.client.get_or_create_collection(
            name="collection",
            embedding_function=self.embedding_function
        )
        self.indexer = Indexer()
        
    def get_collection(self):
        return self.collection
    
    def build_collection(self, chunks: list):
        self.collection.add(
            ids=[f"id{i}" for i in range(1, len(chunks)+1)],
            documents=chunks,
            metadatas=[{"source": "profile.txt", "info_chunk_index": i} for i in range(1, len(chunks)+1)]
        )

if __name__ == "__main__":
    datastore = Datastore()
    datastore.build_collection(["context/profile.txt"])