from app.loaders.universal_loader import UniversalLoader
from app.chunking.text_splitter import TextChunker
from app.embeddings.embedding_model import EmbeddingModel

loader = UniversalLoader()
document = loader.load("data/sample.pdf")

chunker = TextChunker()
chunks = chunker.split(document["content"])

embedder = EmbeddingModel()

embeddings = embedder.embed_documents(chunks)

print(f"Total Chunks: {len(chunks)}")
print(f"Total Embeddings: {len(embeddings)}")
print(f"Embedding Dimension: {len(embeddings[0])}")