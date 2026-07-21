from datetime import datetime
from pathlib import Path
import os

from fastapi import APIRouter, UploadFile, File

from app.loaders.universal_loader import UniversalLoader
from app.chunking.text_splitter import TextChunker
from app.chunking.document_converter import DocumentConverter
from app.embeddings.embedding_model import EmbeddingModel
from app.vector_store.chroma_store import ChromaStore

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # -----------------------------
    # Load document
    # -----------------------------
    loader = UniversalLoader()

    documents = loader.load(file_path)

    # Add metadata to every document
    for doc in documents:

        doc.metadata["source"] = file.filename
        doc.metadata["uploaded_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -----------------------------
    # Split document
    # -----------------------------
    splitter = TextChunker()

    chunks = splitter.split(documents)

    # -----------------------------
    # Convert
    # -----------------------------
    converter = DocumentConverter()

    final_documents = converter.convert(chunks)

    # -----------------------------
    # Embed
    # -----------------------------
    embedding = EmbeddingModel().get_embedding()

    db = ChromaStore(embedding)

    db.add_documents(final_documents)

    # -----------------------------
    # Response
    # -----------------------------
    return {
        "status": "success",
        "message": "Document uploaded successfully.",
        "document": {
            "filename": file.filename,
            "file_type": Path(file.filename).suffix.replace(".", "").upper(),
            "chunks": len(final_documents),
            "embedding_model": "all-MiniLM-L6-v2",
            "vector_database": "ChromaDB",
            "uploaded_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    }