from rag.datastore import Datastore

class Retriever:

    def __init__(self, datastore: Datastore):
        self.collection = datastore.get_collection()
        

    def search_context(self, question: str, top_k: int = 3):
        context = self.collection.query(
            query_texts=[question],
            n_results=top_k
        )

        return context