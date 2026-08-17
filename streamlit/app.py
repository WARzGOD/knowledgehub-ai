import sys
from pathlib import Path

import streamlit as st


# ============================================================
# CONFIGURAÇÃO DOS CAMINHOS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BACKEND_PATH = PROJECT_ROOT / "backend"

if str(BACKEND_PATH) not in sys.path:
    sys.path.insert(0, str(BACKEND_PATH))


# ============================================================
# IMPORTAÇÃO DO RAG
# ============================================================

from app.rag.rag_service import RAGService


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="KnowledgeHub AI",
    page_icon="🤖",
    layout="centered",
)


# ============================================================
# CABEÇALHO
# ============================================================

st.title("🤖 KnowledgeHub AI")

st.markdown(
    """
    ### Assistente Corporativo da NovaCorp Solutions

    Faça perguntas sobre políticas, benefícios,
    procedimentos e informações presentes na
    documentação corporativa.
    """
)


# ============================================================
# INICIALIZAÇÃO DO RAG
# ============================================================

@st.cache_resource
def load_rag():
    return RAGService()


try:

    rag = load_rag()

except Exception as error:

    st.error(
        "Não foi possível inicializar o KnowledgeHub AI."
    )

    st.exception(error)

    st.stop()


# ============================================================
# HISTÓRICO
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            st.caption("Fontes:")

            for source in message["sources"]:
                st.caption(f"• {source}")


# ============================================================
# ENTRADA
# ============================================================

question = st.chat_input(
    "Digite sua pergunta..."
)


# ============================================================
# PROCESSAMENTO
# ============================================================

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "Consultando a documentação..."
        ):

            try:

                result = rag.ask(question)

                answer = result.get(
                    "answer",
                    "Não foi possível obter uma resposta.",
                )

                sources = result.get(
                    "sources",
                    [],
                )

                st.markdown(answer)

                if sources:

                    st.caption("Fontes:")

                    for source in sources:
                        st.caption(
                            f"• {source}"
                        )

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )

            except RuntimeError as error:

                if str(error) == "GEMINI_QUOTA_EXCEEDED":

                    answer = (
                        "O limite temporário da API do "
                        "Gemini foi atingido. Aguarde alguns "
                        "instantes e tente novamente."
                    )

                else:

                    answer = (
                        "Ocorreu um erro ao processar "
                        "sua pergunta."
                    )

                st.error(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": [],
                    }
                )

            except Exception as error:

                st.error(
                    "Não foi possível processar "
                    "a pergunta no momento."
                )

                st.exception(error)