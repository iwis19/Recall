from rag.datastore import Datastore

class Retriever:

    def __init__(self, datastore: Datastore):
        self.datastore = datastore
        

    def search_context(self, question: str, top_k: int = 3):
        context = self.datastore.get_collection().query(
            query_texts=[question],
            n_results=top_k
        )

        return context