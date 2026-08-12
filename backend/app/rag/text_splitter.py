from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.rag.document_loader import load_documents


def split_documents():

    print("\nCarregando documentos...")

    documents = load_documents()

    print(
        f"\nTotal de documentos carregados: "
        f"{len(documents)}"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=80,
        length_function=len,
        separators=[
            "\n# ",
            "\n## ",
            "\n### ",
            "\n\n",
            "\n",
            ". ",
            " ",
        ],
    )

    chunks = splitter.split_documents(documents)

    # Identificador de chunk por documento
    chunk_counters = {}

    for chunk in chunks:

        source = chunk.metadata.get(
            "source",
            "Documento desconhecido"
        )

        source_path = Path(source)

        filename = source_path.name

        extension = source_path.suffix.lower()

        # Define o número do chunk para cada documento
        chunk_counters.setdefault(filename, 0)

        chunk_id = chunk_counters[filename]

        chunk_counters[filename] += 1

        # Metadados
        chunk.metadata["source"] = source
        chunk.metadata["filename"] = filename
        chunk.metadata["file_type"] = extension
        chunk.metadata["chunk_id"] = chunk_id

    print(
        f"\nTotal de chunks criados: "
        f"{len(chunks)}"
    )

    return chunks


if __name__ == "__main__":

    chunks = split_documents()

    for index, chunk in enumerate(chunks):

        print("\n-----------------------------")

        print(f"Chunk {index + 1}")

        print(
            "Fonte:",
            chunk.metadata.get(
                "source",
                "Desconhecida"
            )
        )

        print(
            "Arquivo:",
            chunk.metadata.get(
                "filename",
                "Desconhecido"
            )
        )

        print(
            "Tipo:",
            chunk.metadata.get(
                "file_type",
                "Desconhecido"
            )
        )

        print(
            "Chunk ID:",
            chunk.metadata.get(
                "chunk_id",
                "N/A"
            )
        )

        print("-----------------------------")

        print(
            chunk.page_content[:500]
        )