import requests
from config import FASTAPI_URL


def upload_document(file):
    files = {
        "file": (
            file.name,
            file.getvalue(),
            file.type
        )
    }

    return requests.post(
        f"{FASTAPI_URL}/upload",
        files=files,
        timeout=120
    )


def ask_question(question):
    return requests.post(
        f"{FASTAPI_URL}/query",
        json={
            "question": question
        },
        timeout=120
    )


def get_documents():
    return requests.get(
        f"{FASTAPI_URL}/documents",
        timeout=30
    )


def delete_document(document_id):
    return requests.delete(
        f"{FASTAPI_URL}/documents/{document_id}",
        timeout=30
    )