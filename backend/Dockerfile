FROM python:3.11-slim

# Evita arquivos .pyc e mantém os logs imediatamente visíveis
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Dependências necessárias para algumas bibliotecas Python
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Instala as dependências Python
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Copia o código da aplicação
COPY app ./app

# Copia os documentos utilizados pelo RAG
COPY documents ./documents

# Copia o banco vetorial Chroma
COPY vectorstore/chroma_db ./vectorstore/chroma_db

# Porta utilizada pelo FastAPI
EXPOSE 8000

# Inicializa a aplicação
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]