from langchain_chroma import Chroma


class ChromaStore:

    def __init__(self, embedding_model):

        self.db = Chroma(
            persist_directory="db",
            embedding_function=embedding_model
        )

    def add_documents(self, documents):

        self.db.add_documents(documents)

    def similarity_search(self, query, k=3):

        return self.db.similarity_search(query, k=k)