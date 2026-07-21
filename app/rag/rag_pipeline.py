from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from app.retriever.retriever import Retriever
from app.embeddings.embedding_model import EmbeddingModel
from app.rag.prompt import SYSTEM_PROMPT


class RAGPipeline:

    def __init__(self):

        self.embedding = EmbeddingModel().get_embedding()

        self.retriever = Retriever(self.embedding)

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0
        )

    def ask(self, question):

        documents = self.retriever.retrieve(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        messages = [

            SystemMessage(
                content=SYSTEM_PROMPT
            ),

            HumanMessage(
                content=f"""
Context:

{context}

Question:

{question}
"""
            )
        ]

        response = self.llm.invoke(messages)

        sources = []

        for i, doc in enumerate(documents, start=1):

            sources.append({
                "chunk_number": i,
                "content": doc.page_content,
                "metadata": doc.metadata
            })

        return {
            "answer": response.content,
            "sources": sources,
            "total_chunks": len(documents)
        }