from fastapi import APIRouter

from app.models import QueryRequest, QueryResponse
from app.rag.rag_pipeline import RAGPipeline

router = APIRouter(tags=["Query"])

rag = RAGPipeline()


@router.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):

    result = rag.ask(request.question)

    return QueryResponse(
        status="success",
        question=request.question,
        answer=result["answer"]
    )