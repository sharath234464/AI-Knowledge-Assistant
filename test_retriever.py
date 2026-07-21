from app.embeddings.embedding_model import EmbeddingModel
from app.retriever.retriever import Retriever

embedding = EmbeddingModel().get_embedding()

retriever = Retriever(embedding)

results = retriever.retrieve(
    "What is Secure Multi Party Computation?"
)

print()

print("="*60)

print("Retrieved Documents")

print("="*60)

for i, doc in enumerate(results):

    print()

    print(f"Document {i+1}")

    print("-"*60)

    print(doc.page_content[:500])