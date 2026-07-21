from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.api.query import router as query_router
from app.api.documents import router as documents_router

app = FastAPI(
    title="AI Knowledge Assistant",
    version="1.0"
)

app.include_router(upload_router)
app.include_router(query_router)
app.include_router(documents_router)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "AI Knowledge Assistant is Running 🚀"
    }