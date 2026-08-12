from google import genai

from app.core.config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def ask(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt,
            )

            if not response.text:
                return (
                    "Não foi possível gerar uma resposta "
                    "no momento."
                )

            return response.text

        except Exception as error:

            print(
                f"Erro ao consultar o Gemini: {error}"
            )

            return (
                "Não foi possível processar sua pergunta "
                "no momento. Tente novamente."
            )