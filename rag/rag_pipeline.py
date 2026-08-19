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

    def insert_info(self, info: str):
        chunks = self.indexer.index_information(info=info)
        self.datastore.build_collection(chunks=chunks)
    
    def ask(self, question: str) -> str:

        # guards
        if not question: return ({"error": "Please enter a question."}, 400)
        if self.datastore.is_empty(): return ({"error": "There is currently no information in the database."}, 400)
        
        context = self.retriever.search_context(question=question)
        answer = self.response_generator.generate_response(context=context, question=question)
        
        return answer
    
    def delete_info(self):
        self.datastore.clear_collection()