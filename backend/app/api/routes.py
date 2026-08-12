from fastapi import APIRouter

from app.models.schemas import (
    QuestionRequest,
    QuestionResponse,
)

from app.rag.rag_service import RAGService

router = APIRouter()

rag = RAGService()


@router.post(
    "/ask",
    response_model=QuestionResponse,
)
def ask_question(request: QuestionRequest):

    result = rag.ask(request.question)

    return QuestionResponse(
        answer=result["answer"],
        sources=result["sources"],
    )