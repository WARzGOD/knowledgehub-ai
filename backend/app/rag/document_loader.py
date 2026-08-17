from pathlib import Path

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    CSVLoader,
    Docx2txtLoader,
    BSHTMLLoader,
)


DOCUMENTS_PATH = Path(__file__).resolve().parents[2] / "documents"


def load_documents():

    documents = []

    print("\nCarregando documentos...")

    for file in DOCUMENTS_PATH.iterdir():

        print(f"Lendo documento: {file.name}")

        suffix = file.suffix.lower()

        try:

            if suffix == ".md":

                loader = TextLoader(
                    str(file),
                    encoding="utf-8"
                )

            elif suffix == ".pdf":

                loader = PyPDFLoader(
                    str(file)
                )

            elif suffix == ".csv":
                loader = CSVLoader(
                    str(file),
                    csv_args={
                        "delimiter": ";"
                    },
                    encoding="utf-8"
                )

            elif suffix == ".docx":

                loader = Docx2txtLoader(
                    str(file)
                )

            elif suffix == ".html":

                loader = BSHTMLLoader(
                    str(file),
                    open_encoding="utf-8"
                )

            else:

                print(
                    f"Ignorando formato não suportado: {file.name}"
                )

                continue

            documents.extend(
                loader.load()
            )

        except Exception as error:

            print(
                f"Erro ao carregar {file.name}: {error}"
            )

    print(
        f"\nTotal de documentos carregados: {len(documents)}"
    )

    return documents


if __name__ == "__main__":

    documents = load_documents()

    print("\n========== DOCUMENTOS ==========\n")

    for document in documents:

        print("\n---\n")

        print(
            f"Fonte: {document.metadata.get('source', 'Desconhecida')}"
        )

        print(
            document.page_content[:1000]
        )