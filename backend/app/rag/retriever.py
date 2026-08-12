from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
)


class RetrieverService:

    # Distância máxima aceita para considerar um resultado relevante
    MAX_DISTANCE = 15.0

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        self.vector_store = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=self.embeddings,
        )

    def search(
        self,
        question: str,
        k: int = 5,
    ):

        results = self.vector_store.similarity_search_with_score(
            query=question,
            k=k,
        )

        unique_documents = []
        seen = set()

        for document, distance in results:

            content = document.page_content.strip()

            # Evita documentos duplicados
            if content in seen:
                continue

            seen.add(content)

            # Ignora resultados pouco relevantes
            if distance > self.MAX_DISTANCE:
                continue

            # Guarda a distância nos metadados
            document.metadata["distance"] = distance

            unique_documents.append(document)

        return unique_documents


if __name__ == "__main__":

    retriever = RetrieverService()

    perguntas = [
        "Qual o prazo para solicitar reembolso?",
        "Quais são as regras para senhas?",
        "Quais são os direitos do titular?",
        "Qual é o salário dos desenvolvedores da NovaCorp?",
    ]

    for pergunta in perguntas:

        print("\n\n")
        print("=" * 60)
        print(f"PERGUNTA: {pergunta}")
        print("=" * 60)

        docs = retriever.search(pergunta)

        if not docs:

            print("\nNenhum documento relevante encontrado.")

            continue

        for i, doc in enumerate(docs):

            print("\n------------------------")
            print(f"RESULTADO {i + 1}")

            print(
                "FONTE:",
                doc.metadata.get(
                    "source",
                    "Desconhecida"
                )
            )

            print(
                "ARQUIVO:",
                doc.metadata.get(
                    "filename",
                    "Desconhecido"
                )
            )

            print(
                "TIPO:",
                doc.metadata.get(
                    "file_type",
                    "Desconhecido"
                )
            )

            print(
                "CHUNK:",
                doc.metadata.get(
                    "chunk_id",
                    "N/A"
                )
            )

            print(
                "DISTÂNCIA:",
                round(
                    doc.metadata.get(
                        "distance",
                        0
                    ),
                    4
                )
            )

            print("------------------------")

            print(
                doc.page_content[:500]
            )