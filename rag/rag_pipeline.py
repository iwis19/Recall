from rag.indexer import Indexer
from rag.datastore import Datastore
from rag.retriever import Retriever
from rag.response_generator import ResponseGenerator

class RAGPipeline:

    def __init__(self):
        self.indexer = Indexer()
        self.datastore = Datastore()
        self.retriever = Retriever(self.datastore)
        self.response_generator = ResponseGenerator()

    def insert_info(self, file_paths: list[str]):
        chunks = self.indexer.index_information(paths=file_paths)
        self.datastore.build_collection(chunks=chunks)
    
    def ask(self, question: str) -> str:
        if not question:
            return {"Error": "Please enter a question"}, 400
        
        context = self.retriever.search_context(question=question)
        answer = self.response_generator.generate_response(context=context, question=question)
        
        return answer