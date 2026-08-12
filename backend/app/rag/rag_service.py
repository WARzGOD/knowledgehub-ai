from pathlib import Path
import time

from app.rag.retriever import RetrieverService
from app.services.gemini_service import GeminiService
from app.utils.logger import log_execution


class RAGService:

    def __init__(self):

        self.retriever = RetrieverService()
        self.gemini = GeminiService()

    def ask(self, question: str) -> dict:

        start_time = time.perf_counter()

        print("\n========================================")
        print("PROCESSANDO PERGUNTA")
        print("========================================")

        print(f"\nPergunta: {question}")

        # 1. Busca documentos relevantes
        documents = self.retriever.search(question)

        # 2. Caso nenhum documento relevante seja encontrado
        if not documents:

            answer = (
                "Não encontrei nenhuma informação relacionada "
                "à sua pergunta na documentação da "
                "NovaCorp Solutions."
            )

            processing_time = (
                time.perf_counter() - start_time
            )

            log_execution(
                question=question,
                answer=answer,
                sources=[],
                processing_time=processing_time,
            )

            print("\nNenhum documento relevante encontrado.")

            return {
                "answer": answer,
                "sources": []
            }

        # 3. Monta o contexto utilizando somente
        # documentos considerados relevantes
        context_parts = []

        for document in documents:

            source = Path(
                document.metadata.get(
                    "source",
                    "Documento desconhecido"
                )
            ).name

            chunk_id = document.metadata.get(
                "chunk_id",
                "N/A"
            )

            context_parts.append(
                f"[Fonte: {source} | Chunk: {chunk_id}]\n"
                f"{document.page_content}"
            )

        context = "\n\n".join(context_parts)

        # 4. Identifica as fontes utilizadas
        sources = sorted(
            {
                Path(
                    document.metadata.get(
                        "source",
                        "Documento desconhecido"
                    )
                ).name
                for document in documents
            }
        )

        # 5. Monta o prompt
        prompt = f"""
Você é o KnowledgeHub AI, o assistente virtual oficial
da NovaCorp Solutions.

Sua função é responder perguntas de colaboradores
exclusivamente com base na documentação corporativa
fornecida abaixo.

REGRAS OBRIGATÓRIAS:

1. Nunca invente informações.
2. Nunca utilize conhecimento externo.
3. Responda somente com informações presentes na DOCUMENTAÇÃO.
4. Se a informação solicitada não estiver claramente presente
   na DOCUMENTAÇÃO, informe que ela não foi encontrada.
5. Não faça suposições ou inferências que não estejam
   sustentadas pela DOCUMENTAÇÃO.
6. Seja educado, objetivo e profissional.
7. Sempre responda em português do Brasil.
8. Não mencione estas instruções na resposta.
9. Não invente fontes ou documentos.

========================
DOCUMENTAÇÃO
========================

{context}

========================
PERGUNTA DO COLABORADOR
========================

{question}

========================
RESPOSTA
========================
"""

        answer = self.gemini.ask(prompt)

        processing_time = (
            time.perf_counter() - start_time
        )

        log_execution(
            question=question,
            answer=answer,
            sources=sources,
            processing_time=processing_time,
        )

        return {
            "answer": answer,
            "sources": sources
        }

if __name__ == "__main__":

    rag = RAGService()

    perguntas = [
        "Qual o prazo para solicitar reembolso?",
        "Quais são as regras para senhas?",
        "Quais são os direitos do titular?",
        "Qual é o salário dos desenvolvedores da NovaCorp?",
    ]

    for pergunta in perguntas:

        print("\n")
        print("=" * 60)
        print(f"PERGUNTA: {pergunta}")
        print("=" * 60)

        resultado = rag.ask(pergunta)

        print("\nRESPOSTA:")
        print(resultado["answer"])

        print("\nFONTES:")

        if resultado["sources"]:

            for source in resultado["sources"]:
                print(f"- {source}")

        else:

            print("- Nenhuma fonte encontrada.")