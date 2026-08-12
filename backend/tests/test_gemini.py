from app.services.gemini_service import GeminiService

gemini = GeminiService()

print(
    gemini.ask(
        "Explique em uma frase o que é um assistente corporativo."
    )
)