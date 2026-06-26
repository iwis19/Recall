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

    def index_information(self, paths: list[str]):

        all_chunks = []
        for path in paths:
            file_path = Path(path)
            with open(file=file_path, encoding="utf-8") as f:
                content = f.read()

            chunks = self.recursive_splitter.split_text(content)

            all_chunks.extend(chunks)
        return all_chunks



    