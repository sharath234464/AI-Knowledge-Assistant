from app.vector_store.chroma_store import ChromaStore

class Retriever:

    def __init__(self, embedding):

        self.db = ChromaStore(embedding)

    def retrieve(self, question, k=5):

        return self.db.similarity_search(question, k)