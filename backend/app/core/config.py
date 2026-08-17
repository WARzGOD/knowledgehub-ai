from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

# Gemini

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "A variável GEMINI_API_KEY não foi encontrada."
    )

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "models/gemini-3.6-flash"
)

# Embeddings

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# Diretório base do backend

BASE_DIR = Path(__file__).resolve().parents[2]

# Banco vetorial

VECTOR_DB_PATH = str(
    BASE_DIR / "vectorstore" / "chroma_db"
)