import os
import shutil

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import (
    EMBEDDING_MODEL,
    VECTOR_DB_PATH,
)

from app.rag.text_splitter import split_documents


def create_vector_store():

    print("\n========================================")
    print("CRIANDO BANCO VETORIAL")
    print("========================================")

    # Remove o banco anterior
    if os.path.exists(VECTOR_DB_PATH):

        print("\nRemovendo banco vetorial anterior...")

        shutil.rmtree(VECTOR_DB_PATH)

        print("Banco anterior removido.")

    # Carrega e divide os documentos
    chunks = split_documents()

    print("\n========================================")
    print("GERANDO EMBEDDINGS")
    print("========================================")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # Cria o banco vetorial
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH,
    )

    print("\n========================================")
    print("BANCO VETORIAL CRIADO COM SUCESSO")
    print("========================================")

    print(f"\nLocal: {VECTOR_DB_PATH}")
    print(f"Total de chunks indexados: {len(chunks)}")

    return vector_store


if __name__ == "__main__":

    create_vector_store()