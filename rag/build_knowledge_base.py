import chromadb
from pathlib import Path
from chromadb.utils.embedding_functions.ollama_embedding_function import OllamaEmbeddingFunction
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_collection():

    # always saves data to disk, hence called persistentclient, so when i reboot, it will be fine
    client = chromadb.PersistentClient(path="./chroma_db")

    # creates an embedding function -> takes a piece of text and turns them into a list of numbers (vectors) for storing in chromadb
    embedding_function = OllamaEmbeddingFunction(
        url="http://localhost:11434",
        model_name="nomic-embed-text"
    )

    collection = client.get_or_create_collection(
        name="personal_profile",
        embedding_function=embedding_function
    )

    return collection


def build_knowledge_base():

    collection = get_collection()

    file_path = Path("context\profile.txt")

    # break the paragraphs in profile.txt down and store them in a list
    with open(file=file_path, encoding="utf-8") as f:
        content = f.read()

    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        strip_whitespace=True,
        separators=["\n\n", "\n", ".", ";", ","]
    )

    chunks = recursive_splitter.split_text(content)

    # i dont need to put in embeddings (a param) as i already have a embedding function inserted in the client collection
    collection.add(
        ids=[f"id{i}" for i in range(1, len(chunks)+1)],    # 1-indexed
        documents=chunks,
        metadatas=[{"source": "profile.txt", "chunk_index": i} for i in range(1, len(chunks)+1)]     # 1-indexed
    )