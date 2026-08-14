from fastapi import APIRouter, HTTPException

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

    try:

        result = rag.ask(request.question)

        return QuestionResponse(
            answer=result["answer"],
            sources=result["sources"],
        )

    except RuntimeError as error:

        if str(error) == "GEMINI_QUOTA_EXCEEDED":

            raise HTTPException(
                status_code=429,
                detail={
                    "code": "GEMINI_QUOTA_EXCEEDED",
                    "message": (
                        "O limite de consultas da API "
                        "do Gemini foi atingido. "
                        "Aguarde alguns instantes e "
                        "tente novamente."
                    ),
                },
            )

        raise HTTPException(
            status_code=500,
            detail={
                "code": "GEMINI_REQUEST_FAILED",
                "message": (
                    "Não foi possível processar "
                    "a pergunta no momento."
                ),
            },
        )