# 🧠 KnowledgeHub AI — Backend

> Assistente corporativo inteligente baseado em RAG (Retrieval-Augmented Generation), desenvolvido para consultar e responder perguntas utilizando documentos internos da empresa de forma contextualizada, segura e rastreável.

---

## 📌 Sobre o projeto

O **KnowledgeHub AI** é um assistente corporativo desenvolvido para facilitar o acesso ao conhecimento interno de uma organização.

A solução utiliza uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)** para recuperar informações relevantes em uma base documental antes de gerar uma resposta utilizando inteligência artificial generativa.

Dessa forma, o sistema não depende exclusivamente do conhecimento prévio do modelo de linguagem. As respostas são fundamentadas nos documentos disponibilizados à aplicação.

### 🎯 Objetivo

Permitir que colaboradores consultem informações corporativas utilizando linguagem natural, sem a necessidade de procurar manualmente informações em diversos documentos.

Exemplos de perguntas:

- Qual o prazo para solicitar reembolso?
- Quais são as regras para senhas?
- Quais são os direitos do titular de dados?
- Quais benefícios são oferecidos aos colaboradores?
- Quais são as regras estabelecidas no código de conduta?

Quando uma informação relevante não é encontrada na base documental, o sistema evita gerar uma resposta sem fundamento e informa que nenhum documento relevante foi encontrado.

---

# 🏗️ Arquitetura

O backend utiliza uma arquitetura modular baseada em FastAPI e RAG.

```text
                         ┌──────────────────────┐
                         │      Usuário         │
                         └──────────┬───────────┘
                                    │
                                    │ Pergunta
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         │       POST /ask      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      RAGService      │
                         └──────────┬───────────┘
                                    │
                         ┌──────────▼───────────┐
                         │      Retriever       │
                         │   Busca semântica    │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      ChromaDB        │
                         │    Banco vetorial    │
                         └──────────┬───────────┘
                                    │
                              Contexto relevante
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Gemini         │
                         │  Google Generative   │
                         │         AI           │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       Resposta       │
                         └──────────────────────┘
```

---

# 🧠 Funcionamento do RAG

O fluxo principal da aplicação pode ser dividido em etapas:

### 1. Pergunta do usuário

O usuário envia uma pergunta para o endpoint:

```http
POST /ask
```

### 2. Recuperação de informações

O sistema transforma a consulta em uma representação vetorial e realiza uma busca semântica na base de conhecimento.

### 3. Recuperação dos documentos

O ChromaDB retorna os trechos mais relevantes relacionados à pergunta.

### 4. Construção do contexto

Os documentos recuperados são utilizados como contexto para a geração da resposta.

### 5. Geração da resposta

O Gemini recebe a pergunta juntamente com o contexto recuperado e produz uma resposta baseada nas informações encontradas.

### 6. Controle de informações inexistentes

Caso nenhum documento relevante seja encontrado, o sistema informa:

```text
Nenhum documento relevante encontrado.
```

Esse comportamento reduz o risco de respostas sem fundamentação na base documental.

---

# 📚 Base de Conhecimento

Atualmente, o KnowledgeHub AI utiliza documentos corporativos de diferentes formatos.

```text
documents/
├── beneficios.csv
├── codigo_conduta.docx
├── faq_rh.md
├── manual_colaborador_novacorp.md
├── politica_seguranca.pdf
└── termos_lgpd.html
```

### Documentos disponíveis

| Documento | Formato | Conteúdo |
|---|---|---|
| Manual do Colaborador NovaCorp | Markdown | Informações gerais e políticas destinadas aos colaboradores |
| Benefícios | CSV | Informações relacionadas aos benefícios corporativos |
| Código de Conduta | DOCX | Diretrizes e princípios de conduta |
| FAQ RH | Markdown | Perguntas frequentes relacionadas a Recursos Humanos |
| Política de Segurança | PDF | Diretrizes de segurança da informação |
| Termos LGPD | HTML | Informações relacionadas à proteção de dados e direitos dos titulares |

### 📖 Manual do Colaborador NovaCorp

O **Manual do Colaborador NovaCorp** representa uma das principais fontes de conhecimento da aplicação.

O documento possui **14 capítulos**, reunindo informações corporativas que podem ser consultadas pelo assistente por meio de linguagem natural.

---

# 🤖 Inteligência Artificial

O projeto utiliza o **Google Gemini** como modelo generativo.

A integração é realizada através do SDK oficial:

```text
google-genai
```

O modelo utilizado pode ser configurado através da variável de ambiente:

```env
GEMINI_MODEL=models/gemini-3.6-flash
```

A chave de acesso é definida através de:

```env
GEMINI_API_KEY=sua_chave_aqui
```

---

# 🔎 Embeddings

Para transformar os documentos e consultas em representações vetoriais, o projeto utiliza:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

O modelo foi escolhido por oferecer suporte multilíngue, sendo adequado para documentos e perguntas em português.

---

# 🗄️ Banco Vetorial

O projeto utiliza **ChromaDB** para armazenamento e recuperação dos vetores.

A localização configurada é:

```text
vectorstore/chroma_db
```

O banco vetorial contém as representações dos documentos utilizados pelo mecanismo de recuperação.

> O diretório `vectorstore/` não é versionado no Git. A persistência local é utilizada no ambiente de execução.

---

# ⚙️ Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python 3.11 | Linguagem principal |
| FastAPI | API REST |
| Uvicorn | Servidor ASGI |
| LangChain | Orquestração do pipeline RAG |
| ChromaDB | Banco vetorial |
| Sentence Transformers | Geração de embeddings |
| Google Gemini | Geração de respostas |
| python-dotenv | Gerenciamento de variáveis de ambiente |
| Docker | Containerização |

---

# 📁 Estrutura do projeto

```text
backend/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── rag/
│   │   ├── __init__.py
│   │   ├── document_loader.py
│   │   ├── embedding_store.py
│   │   ├── rag_service.py
│   │   ├── retriever.py
│   │   └── text_splitter.py
│   │
│   ├── services/
│   │   └── gemini_service.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   ├── __init__.py
│   └── main.py
│
├── documents/
│   ├── beneficios.csv
│   ├── codigo_conduta.docx
│   ├── faq_rh.md
│   ├── manual_colaborador_novacorp.md
│   ├── politica_seguranca.pdf
│   └── termos_lgpd.html
│
├── scripts/
│   └── list_models.py
│
├── tests/
│   └── test_gemini.py
│
├── vectorstore/
│   └── chroma_db/
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🔌 API

## POST `/ask`

Endpoint responsável por receber perguntas e retornar respostas baseadas na base documental.

### Requisição

```http
POST /ask
Content-Type: application/json
```

Exemplo:

```json
{
  "question": "Qual o prazo para solicitar reembolso?"
}
```

### Resposta

```json
{
  "answer": "..."
}
```

A resposta é gerada utilizando os documentos recuperados pelo mecanismo RAG.

---

# 📖 Documentação da API

Durante a execução do FastAPI, a documentação interativa pode ser acessada através do Swagger:

```text
http://localhost:8000/docs
```

Também está disponível a especificação OpenAPI:

```text
http://localhost:8000/openapi.json
```

---

# 🐳 Docker

O backend possui suporte completo à execução utilizando Docker.

## Construir a imagem

Na pasta `backend/`:

```bash
docker build -t knowledgehub-ai-backend .
```

## Executar o container

```bash
docker run \
  --name knowledgehub-api \
  -p 8000:8000 \
  --env-file .env \
  knowledgehub-ai-backend
```

No Windows PowerShell:

```powershell
docker run --name knowledgehub-api -p 8000:8000 --env-file .env knowledgehub-ai-backend
```

Após a inicialização:

```text
http://localhost:8000
```

A API estará disponível na porta `8000`.

---

# 🔐 Configuração

Crie um arquivo `.env` na pasta `backend/`.

Exemplo:

```env
GEMINI_API_KEY=sua_chave_api
GEMINI_MODEL=models/gemini-3.6-flash
```

O arquivo `.env` **não deve ser versionado**.

Para facilitar a configuração do ambiente, o projeto possui:

```text
.env.example
```

---

# 🛡️ Segurança

Algumas práticas foram adotadas no projeto:

- API Key armazenada através de variável de ambiente;
- `.env` incluído no `.gitignore`;
- `.env` removido do controle de versão;
- arquivos temporários e caches ignorados;
- diretório do banco vetorial não versionado;
- `.dockerignore` utilizado para reduzir o contexto da imagem Docker.

> A chave de API nunca deve ser inserida diretamente no código-fonte.

---

# 🧪 Testes e scripts auxiliares

O projeto possui scripts auxiliares para desenvolvimento e validação.

### Listagem dos modelos Gemini

```bash
python scripts/list_models.py
```

### Teste da integração com Gemini

```bash
python tests/test_gemini.py
```

---

# ▶️ Execução local

## 1. Criar ambiente virtual

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

## 2. Instalar dependências

```bash
pip install -r requirements.txt
```

## 3. Configurar variáveis de ambiente

Criar:

```text
.env
```

com:

```env
GEMINI_API_KEY=sua_chave_api
GEMINI_MODEL=models/gemini-3.6-flash
```

## 4. Executar a API

```bash
uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# 🔄 Fluxo de processamento

```text
Documento
    │
    ▼
Carregamento
    │
    ▼
Divisão em chunks
    │
    ▼
Geração de embeddings
    │
    ▼
ChromaDB
    │
    │
    │
Pergunta do usuário
    │
    ▼
Embedding da consulta
    │
    ▼
Busca semântica
    │
    ▼
Documentos relevantes
    │
    ▼
Contexto + Pergunta
    │
    ▼
Gemini
    │
    ▼
Resposta
```

---

# 🧩 Formatos de documentos

O sistema foi estruturado para trabalhar com diferentes fontes documentais.

Atualmente são utilizados:

```text
CSV
DOCX
HTML
Markdown
PDF
```

Essa abordagem permite que a organização mantenha diferentes tipos de documentos em uma única base de conhecimento.

---

# 📊 Exemplos de consultas

### Recursos Humanos

```text
Qual o prazo para solicitar reembolso?
```

### Segurança

```text
Quais são as regras para senhas?
```

### LGPD

```text
Quais são os direitos do titular?
```

### Informação não disponível

```text
Qual é o salário dos desenvolvedores da NovaCorp?
```

Quando não existe informação relevante na base documental, o sistema retorna:

```text
Nenhum documento relevante encontrado.
```

---

# 🚧 Roadmap

Funcionalidades que podem ser incorporadas em versões futuras:

- [ ] Interface web completa para o assistente
- [ ] Histórico de conversas
- [ ] Autenticação de usuários
- [ ] Controle de acesso por departamento
- [ ] Upload de novos documentos
- [ ] Atualização automática da base vetorial
- [ ] Monitoramento da API
- [ ] Métricas de utilização
- [ ] Avaliação automatizada das respostas
- [ ] Deploy em ambiente cloud
- [ ] Integração com sistemas corporativos

---

# 🎯 Diferenciais

### 🧠 RAG

As respostas são fundamentadas em informações recuperadas da base documental.

### 📚 Base documental diversificada

O sistema trabalha com diferentes formatos de documentos corporativos.

### 🌎 Suporte multilíngue

O modelo de embeddings utilizado é adequado para conteúdos em português e outros idiomas.

### 🔐 Segurança

Credenciais e informações sensíveis são mantidas fora do código-fonte.

### 🐳 Containerização

O backend pode ser executado de maneira padronizada utilizando Docker.

### 🛑 Controle contra respostas sem contexto

Quando não encontra documentos relevantes, o sistema não tenta responder utilizando informações não encontradas na base.

---

# 👨‍💻 Status do projeto

**Status:** 🚀 MVP funcional

O backend atualmente possui:

- [x] API FastAPI
- [x] Endpoint `/ask`
- [x] Pipeline RAG
- [x] Embeddings
- [x] ChromaDB
- [x] Integração com Gemini
- [x] Base documental
- [x] Suporte a múltiplos formatos
- [x] Docker
- [x] Configuração por variáveis de ambiente
- [x] Organização modular
- [x] Scripts auxiliares
- [x] Teste de integração com Gemini

---

# 📄 Licença

Projeto desenvolvido para fins educacionais e de demonstração tecnológica.

---

## 🚀 KnowledgeHub AI

**Transformando documentos corporativos em conhecimento acessível através de Inteligência Artificial.**
