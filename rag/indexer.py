from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

class Indexer:

    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 100):
        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            strip_whitespace=True,
            separators=["\n\n", "\n", ".", ";", ","]
        )

    def index_information(self, info: str):
        return self.recursive_splitter.split_text(info)

    



    
