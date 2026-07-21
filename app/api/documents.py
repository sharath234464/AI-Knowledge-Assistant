import json
import os

from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["Documents"])

METADATA_FILE = "data/metadata/documents.json"
UPLOAD_FOLDER = "data/uploads"


@router.get("/documents")
def get_documents():

    if not os.path.exists(METADATA_FILE):
        return {
            "status": "success",
            "total_documents": 0,
            "documents": []
        }

    with open(METADATA_FILE, "r") as f:
        documents = json.load(f)

    return {
        "status": "success",
        "total_documents": len(documents),
        "documents": documents
    }


@router.delete("/documents/{document_id}")
def delete_document(document_id: int):

    if not os.path.exists(METADATA_FILE):
        raise HTTPException(status_code=404, detail="Metadata file not found.")

    with open(METADATA_FILE, "r") as f:
        documents = json.load(f)

    document_to_delete = None

    for document in documents:
        if document["id"] == document_id:
            document_to_delete = document
            break

    if document_to_delete is None:
        raise HTTPException(status_code=404, detail="Document not found.")

    file_path = os.path.join(
        UPLOAD_FOLDER,
        document_to_delete["filename"]
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    documents.remove(document_to_delete)

    # Reassign IDs
    for index, document in enumerate(documents):
        document["id"] = index + 1

    with open(METADATA_FILE, "w") as f:
        json.dump(documents, f, indent=4)

    return {
        "status": "success",
        "message": "Document deleted successfully.",
        "deleted_document": document_to_delete["filename"]
    }