from app.loaders.universal_loader import UniversalLoader
from app.chunking.text_splitter import TextChunker
from app.chunking.document_converter import DocumentConverter
from app.embeddings.embedding_model import EmbeddingModel
from app.vector_store.chroma_store import ChromaStore

# Load PDF
loader = UniversalLoader()
document = loader.load("data/sample.pdf")

# Split into chunks
chunker = TextChunker()
chunks = chunker.split(document["content"])

# Convert chunks into Documents
converter = DocumentConverter()
documents = converter.convert(chunks)

# Create embedding model
embedding = EmbeddingModel().get_embedding()

# Create ChromaDB
db = ChromaStore(embedding)

# Store documents
db.add_documents(documents)

print(f"Stored {len(documents)} documents in ChromaDB")