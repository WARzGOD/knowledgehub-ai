# 🤖 KnowledgeHub AI

> Assistente corporativo inteligente baseado em **RAG (Retrieval-Augmented Generation)** para consulta de documentos internos utilizando linguagem natural.

O **KnowledgeHub AI** é uma aplicação desenvolvida para facilitar o acesso ao conhecimento corporativo. A solução permite que colaboradores façam perguntas sobre políticas, benefícios, procedimentos, segurança da informação e outros conteúdos internos, recebendo respostas fundamentadas na documentação disponível.

O projeto combina **FastAPI, LangChain, ChromaDB, Sentence Transformers e Google Gemini**, utilizando uma arquitetura RAG para recuperar informações relevantes antes da geração da resposta.

---

## 🎯 Objetivo

O objetivo do KnowledgeHub AI é transformar documentos corporativos em uma base de conhecimento acessível através de linguagem natural.

Em vez de procurar manualmente informações em diferentes arquivos, o colaborador pode simplesmente perguntar:

```text
Qual o prazo para solicitar reembolso?
```

ou:

```text
Quais são as regras para criação de senhas?
```

O sistema recupera os trechos relevantes da documentação e utiliza essas informações como contexto para gerar a resposta.

---

## 💡 Problema

Informações corporativas frequentemente estão distribuídas em diferentes documentos e formatos, dificultando sua localização e consulta.

O KnowledgeHub AI busca solucionar esse problema oferecendo uma interface de conversação capaz de:

- consultar documentos corporativos;
- realizar busca semântica;
- recuperar informações relevantes;
- gerar respostas contextualizadas;
- apresentar as fontes utilizadas;
- evitar respostas quando não existe informação relevante na documentação.

---

# 🧠 Arquitetura

O projeto utiliza uma arquitetura baseada em **RAG (Retrieval-Augmented Generation)**.

```text
                         ┌──────────────────────┐
                         │       Usuário        │
                         └──────────┬───────────┘
                                    │
                              Pergunta
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Frontend        │
                         │      React/Vite      │
                         └──────────┬───────────┘
                                    │
                              POST /ask
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       FastAPI        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     RAGService       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  RetrieverService    │
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
                         │    Gemini / Google   │
                         │    Generative AI     │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      Resposta        │
                         │   + fontes utilizadas│
                         └──────────────────────┘
```

---

# 🔄 Funcionamento do RAG

O fluxo principal da aplicação é dividido em etapas:

### 1. Consulta

O usuário envia uma pergunta através da interface web.

### 2. API

O frontend envia a pergunta para o backend através do endpoint:

```http
POST /ask
```

### 3. Busca semântica

A pergunta é utilizada pelo mecanismo de recuperação para encontrar os documentos mais relevantes na base vetorial.

### 4. Recuperação

O **ChromaDB** retorna os trechos considerados relevantes para a consulta.

### 5. Construção do contexto

Os documentos recuperados são organizados em um contexto que acompanha a pergunta enviada ao modelo generativo.

### 6. Geração

O **Google Gemini** recebe a pergunta e o contexto recuperado e gera a resposta.

### 7. Fontes

O backend também retorna os documentos utilizados durante a recuperação, permitindo apresentar as fontes ao usuário.

### 8. Ausência de informação

Quando nenhum documento relevante é encontrado, o sistema informa que a informação não está disponível na documentação, evitando uma resposta sem fundamentação.

---

# 🛠️ Tecnologias

## Backend

| Tecnologia | Utilização |
|---|---|
| Python 3.11 | Linguagem principal |
| FastAPI | API REST |
| Uvicorn | Servidor ASGI |
| LangChain | Orquestração do pipeline RAG |
| ChromaDB | Banco vetorial |
| Sentence Transformers | Embeddings |
| Google Gemini | Geração das respostas |
| python-dotenv | Variáveis de ambiente |
| Pydantic | Validação dos dados |

## Frontend

| Tecnologia | Utilização |
|---|---|
| React | Interface |
| TypeScript | Tipagem e desenvolvimento |
| Vite | Build e servidor de desenvolvimento |
| CSS | Estilização e responsividade |
| Axios | Comunicação com a API |

---

# 📚 Base de Conhecimento

O MVP utiliza diferentes formatos de documentos corporativos:

```text
documents/
├── beneficios.csv
├── codigo_conduta.docx
├── faq_rh.md
├── manual_colaborador_novacorp.md
├── politica_seguranca.pdf
└── termos_lgpd.html
```

### Documentos

| Documento | Formato | Conteúdo |
|---|---|---|
| Manual do Colaborador NovaCorp | Markdown | Informações gerais e políticas corporativas |
| Benefícios | CSV | Benefícios oferecidos aos colaboradores |
| Código de Conduta | DOCX | Diretrizes e princípios de conduta |
| FAQ RH | Markdown | Perguntas frequentes de Recursos Humanos |
| Política de Segurança | PDF | Diretrizes de segurança da informação |
| Termos LGPD | HTML | Proteção de dados e direitos dos titulares |

A aplicação foi estruturada para trabalhar com múltiplos formatos documentais dentro de uma mesma base de conhecimento.

---

# 🤖 Inteligência Artificial

O KnowledgeHub AI utiliza o **Google Gemini** como modelo generativo.

A integração é realizada através do SDK:

```text
google-genai
```

O modelo pode ser configurado através da variável:

```env
GEMINI_MODEL=models/gemini-3.6-flash
```

A chave da API é configurada através de:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave não deve ser inserida diretamente no código-fonte.

---

# 🔎 Embeddings

Para representar documentos e consultas vetorialmente, o projeto utiliza:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

O modelo foi escolhido por oferecer suporte multilíngue e ser adequado para consultas e documentos em português.

---

# 🗄️ Banco Vetorial

O projeto utiliza **ChromaDB** para armazenamento e recuperação dos embeddings.

A persistência local é realizada em:

```text
backend/vectorstore/chroma_db
```

O diretório `vectorstore/` é ignorado pelo Git.

Isso significa que a base vetorial utilizada durante o desenvolvimento permanece localmente e não é enviada para o repositório.

---

# 🔌 API

## POST `/ask`

Endpoint responsável por receber perguntas e retornar respostas baseadas na documentação corporativa.

### Requisição

```http
POST /ask
Content-Type: application/json
```

```json
{
  "question": "Qual o prazo para solicitar reembolso?"
}
```

### Resposta

```json
{
  "answer": "O prazo para solicitar o reembolso é de até 15 dias corridos após a realização da despesa.",
  "sources": [
    "manual_colaborador_novacorp.md"
  ]
}
```

---

# 🖥️ Frontend

O frontend oferece uma interface de conversação simples e responsiva.

Entre os recursos implementados estão:

- 💬 interface de chat;
- 👤 identificação das mensagens do usuário;
- 🤖 identificação das respostas do KnowledgeHub AI;
- 📚 apresentação das fontes utilizadas;
- ⏳ indicador de processamento;
- ⚠️ tratamento visual de erros;
- 🚦 tratamento específico para erro `429`;
- 📱 layout responsivo;
- 🎨 identidade visual própria do KnowledgeHub AI.

A interface foi propositalmente mantida simples para preservar o foco do MVP na experiência de consulta ao conhecimento corporativo.

---

# ⚠️ Limitação da API Gemini

Durante os testes do MVP foi atingido um erro:

```text
429 RESOURCE_EXHAUSTED
```

A mensagem retornada pela API indicou uma cota de:

```text
20 requisições
```

para a métrica de geração de conteúdo no modelo utilizado dentro do **Free Tier**.

### Importante

Esse limite **não pertence ao KnowledgeHub AI**.

A limitação é determinada pela **cota disponível na API do Google Gemini** de acordo com o plano e as condições de utilização da conta/projeto.

Quando a cota é excedida, a API retorna `HTTP 429 Too Many Requests`.

O KnowledgeHub AI possui tratamento específico para essa situação e apresenta uma mensagem orientativa ao usuário:

```text
⚠️ Limite temporário atingido.

O KnowledgeHub AI atingiu a cota disponível da API do Gemini.
Aguarde alguns instantes e tente novamente.
```

Para utilização além das cotas disponíveis no plano gratuito, é necessário consultar as condições atuais da API Gemini e os limites associados ao projeto.

---

# 🔐 Segurança

O projeto adota algumas práticas básicas de segurança:

- API Key armazenada em variável de ambiente;
- `.env` ignorado pelo Git;
- `.env.example` utilizado como referência de configuração;
- arquivos temporários ignorados;
- caches Python ignorados;
- `node_modules` ignorado;
- banco vetorial local ignorado;
- arquivos SQLite e bancos locais ignorados.

A chave da API nunca deve ser publicada no repositório.

---

# 📂 Estrutura do Projeto

```text
knowledgehub-ai/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py
│   │   │
│   │   ├── core/
│   │   │   └── config.py
│   │   │
│   │   ├── models/
│   │   │   └── schemas.py
│   │   │
│   │   ├── rag/
│   │   │   ├── document_loader.py
│   │   │   ├── embedding_store.py
│   │   │   ├── rag_service.py
│   │   │   ├── retriever.py
│   │   │   └── text_splitter.py
│   │   │
│   │   ├── services/
│   │   │   └── gemini_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── logger.py
│   │   │
│   │   └── main.py
│   │
│   ├── documents/
│   │   ├── beneficios.csv
│   │   ├── codigo_conduta.docx
│   │   ├── faq_rh.md
│   │   ├── manual_colaborador_novacorp.md
│   │   ├── politica_seguranca.pdf
│   │   └── termos_lgpd.html
│   │
│   ├── scripts/
│   │   └── list_models.py
│   │
│   ├── tests/
│   │   └── test_gemini.py
│   │
│   ├── vectorstore/
│   │   └── chroma_db/
│   │
│   ├── .env.example
│   ├── .gitignore
│   ├── Dockerfile
│   ├── README.md
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chat.tsx
│   │   │   ├── Header.tsx
│   │   │   └── MessageInput.tsx
│   │   │
│   │   ├── services/
│   │   │   └── api.ts
│   │   │
│   │   ├── types/
│   │   │   └── chat.ts
│   │   │
│   │   ├── App.tsx
│   │   ├── index.css
│   │   └── main.tsx
│   │
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
```

> Diretórios gerados localmente, como `.venv`, `node_modules`, `__pycache__` e `vectorstore/chroma_db`, não são versionados.

---

# ▶️ Execução Local

## Backend

Entre na pasta:

```powershell
cd backend
```

Crie o ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

Configure o arquivo:

```text
.env
```

com:

```env
GEMINI_API_KEY=sua_chave_api
GEMINI_MODEL=models/gemini-3.6-flash
```

Execute:

```powershell
python -m uvicorn app.main:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend

Em outro terminal:

```powershell
cd frontend
```

Instale as dependências:

```powershell
npm install
```

Execute:

```powershell
npm run dev
```

O Vite disponibilizará a aplicação em:

```text
http://localhost:5173
```

O frontend realiza as requisições para o backend FastAPI.

---

# 🧪 Validação do MVP

O MVP foi validado considerando os principais componentes da solução:

- [x] Backend FastAPI funcionando
- [x] Frontend React funcionando
- [x] Comunicação frontend ↔ backend
- [x] Pipeline RAG funcionando
- [x] Busca semântica
- [x] ChromaDB
- [x] Embeddings
- [x] Integração com Gemini
- [x] Respostas fundamentadas na documentação
- [x] Retorno das fontes utilizadas
- [x] Tratamento de perguntas sem informação relevante
- [x] Tratamento de erro `429`
- [x] Interface responsiva
- [x] Estado de carregamento
- [x] Identidade visual do assistente
- [x] Proteção das variáveis de ambiente

---

# 🧪 Exemplos de consultas

### Recursos Humanos

```text
Qual o prazo para solicitar reembolso?
```

### Segurança da Informação

```text
Quais são as regras para criação de senhas?
```

### Benefícios

```text
Como funciona o benefício de vale-refeição?
```

### LGPD

```text
Quais são os direitos do titular?
```

### Informação inexistente

```text
Qual é o salário dos desenvolvedores da NovaCorp?
```

Quando a documentação não possui informação relevante, o sistema evita utilizar conhecimento externo para responder.

---

# 🗺️ Roadmap

Possíveis evoluções futuras:

- [ ] Histórico de conversas
- [ ] Autenticação de usuários
- [ ] Controle de acesso por departamento
- [ ] Upload de documentos
- [ ] Atualização automática da base vetorial
- [ ] Monitoramento da API
- [ ] Métricas de utilização
- [ ] Avaliação automatizada das respostas
- [ ] Deploy em ambiente cloud
- [ ] Integração com sistemas corporativos

Essas funcionalidades não fazem parte do MVP atual.

---

# 📊 Status

## 🚀 MVP funcional

O KnowledgeHub AI possui atualmente:

- API REST funcional;
- pipeline RAG;
- recuperação semântica;
- banco vetorial;
- embeddings multilíngues;
- integração com Google Gemini;
- base documental diversificada;
- frontend responsivo;
- apresentação das fontes;
- tratamento de erros;
- configuração por variáveis de ambiente;
- documentação técnica.

O MVP encontra-se em estado funcional e apresentável para demonstração.

---

# 🧩 Diferenciais

### 🧠 RAG

As respostas são fundamentadas nos documentos recuperados pela aplicação.

### 📚 Base documental diversificada

O sistema trabalha com CSV, DOCX, HTML, Markdown e PDF.

### 🔎 Busca semântica

A recuperação é baseada em similaridade semântica, permitindo consultas em linguagem natural.

### 🔐 Respostas controladas

O prompt utilizado orienta o modelo a responder exclusivamente com base na documentação recuperada.

### 📖 Fontes

As fontes utilizadas são retornadas pela API e apresentadas na interface.

### 📱 Interface simples e responsiva

O frontend foi desenvolvido para proporcionar uma experiência de chat direta, sem adicionar complexidade desnecessária ao MVP.

---

# 📄 Licença

Projeto desenvolvido para fins educacionais e de demonstração tecnológica.

---

<div align="center">

## 🤖 KnowledgeHub AI

**Transformando documentos corporativos em conhecimento acessível através de Inteligência Artificial.**

</div>