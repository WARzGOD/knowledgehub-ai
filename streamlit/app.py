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
    initial_sidebar_state="collapsed",
)


# ============================================================
# ESTILO VISUAL
# ============================================================

st.html(
    """
    <style>

    /* ========================================================
       FUNDO
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(250, 204, 21, 0.12),
                transparent 35%
            ),
            #f8fafc;
    }


    /* ========================================================
       CONTAINER PRINCIPAL
       ======================================================== */

    .block-container {
        max-width: 900px;
        padding-top: 2rem;
        padding-bottom: 6rem;
    }


    /* ========================================================
       CABEÇALHO
       ======================================================== */

    .hero {
        text-align: center;
        padding: 2.5rem 1rem 1.8rem 1rem;
    }

    .hero-icon {
    width: 72px;
    height: 72px;

    margin: 0 auto 1rem auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 20px;

    background: linear-gradient(
        135deg,
        #facc15,
        #f59e0b
    );

    box-shadow:
        0 10px 25px rgba(245, 158, 11, 0.25);

    font-size: 2rem;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


.hero-icon:hover {
    transform: translateY(-2px);

    box-shadow:
        0 14px 30px rgba(245, 158, 11, 0.3);
}

    .hero-title {
        margin: 0;

        font-size: 2.5rem;

        font-weight: 800;

        letter-spacing: -0.045em;

        color: #111827;

        line-height: 1.1;
    }

    .hero-subtitle {
        margin-top: 0.7rem;

        max-width: 600px;

        margin-left: auto;
        margin-right: auto;

        color: #64748b;

        font-size: 1rem;

        line-height: 1.6;
    }

    .company {
        display: inline-block;

        margin-top: 0.8rem;
        padding: 0.35rem 0.8rem;

        border-radius: 999px;

        background: #fff7d6;
        color: #92400e;

        font-size: 0.78rem;
        font-weight: 600;
    }


    /* ========================================================
       CARD DE BOAS-VINDAS
       ======================================================== */

    .welcome-card {
        margin: 1rem 0 1.5rem 0;

        padding: 1.4rem 1.5rem;

        background:
            linear-gradient(
                135deg,
                #ffffff,
                #fffdf5
            );

        border: 1px solid #f1f5f9;

        border-left: 4px solid #facc15;

        border-radius: 16px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .welcome-title {
        margin-bottom: 0.4rem;

        color: #1f2937;

        font-size: 1rem;

        font-weight: 750;
    }

    .welcome-text {
        margin: 0;

        max-width: 760px;

        color: #64748b;

        font-size: 0.9rem;

        line-height: 1.65;
    }


    /* ========================================================
       TÍTULO DAS SUGESTÕES
       ======================================================== */

    .suggestions-title {
        margin: 0.8rem 0 0.7rem 0;

        color: #475569;

        font-size: 0.82rem;
        font-weight: 700;
    }

    .suggestions-grid {
    display: grid;

    grid-template-columns: repeat(2, 1fr);

    gap: 0.8rem;

    margin-bottom: 1.5rem;
}


.suggestion-card {
    display: flex;

    align-items: center;

    gap: 0.8rem;

    padding: 1rem 1.1rem;

    background: #ffffff;

    border: 1px solid #e5e7eb;

    border-radius: 14px;

    box-shadow:
        0 3px 12px rgba(15, 23, 42, 0.04);

    transition:
        transform 0.15s ease,
        box-shadow 0.15s ease;
}


.suggestion-card:hover {
    transform: translateY(-2px);

    box-shadow:
        0 6px 18px rgba(15, 23, 42, 0.08);
}


.suggestion-icon {
    width: 42px;
    height: 42px;

    flex-shrink: 0;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background: #fffbeb;

    font-size: 1.25rem;
}


.suggestion-content {
    min-width: 0;
}


.suggestion-label {
    margin-bottom: 0.2rem;

    color: #92400e;

    font-size: 0.72rem;

    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 0.04em;
}


.suggestion-question {
    color: #334155;

    font-size: 0.85rem;

    line-height: 1.4;
}


@media (max-width: 640px) {

    .suggestions-grid {
        grid-template-columns: 1fr;
    }

}


    /* ========================================================
   MENSAGENS DO CHAT
   ======================================================== */

[data-testid="stChatMessage"] {
    border-radius: 16px;

    margin-bottom: 0.9rem;

    padding: 0.8rem 1rem;

    background: #ffffff;

    border: 1px solid #e5e7eb;

    box-shadow:
        0 3px 12px rgba(15, 23, 42, 0.04);
}


/* ========================================================
   TEXTO DAS MENSAGENS
   ======================================================== */

[data-testid="stChatMessage"] p {
    color: #334155;

    font-size: 0.95rem;

    line-height: 1.65;
}


/* ========================================================
   LISTAS DAS RESPOSTAS
   ======================================================== */

[data-testid="stChatMessage"] li {
    color: #334155;

    line-height: 1.6;
}


/* ========================================================
   DESTAQUES DAS RESPOSTAS
   ======================================================== */

[data-testid="stChatMessage"] strong {
    color: #1f2937;
}


    /* ========================================================
   CAMPO DE PERGUNTA
   ======================================================== */

[data-testid="stChatInput"] {
    border-radius: 18px;

    border: 1px solid #e5e7eb;

    background: #ffffff;

    box-shadow:
        0 6px 20px rgba(15, 23, 42, 0.07);

    transition:
        border-color 0.2s ease,
        box-shadow 0.2s ease;
}


[data-testid="stChatInput"]:focus-within {
    border-color: #facc15;

    box-shadow:
        0 0 0 3px rgba(250, 204, 21, 0.15),
        0 8px 24px rgba(15, 23, 42, 0.08);
}


[data-testid="stChatInput"] textarea {
    font-size: 0.95rem;

    color: #1f2937;
}


[data-testid="stChatInput"] textarea::placeholder {
    color: #94a3b8;
}


    /* ========================================================
       FONTES
       ======================================================== */

    .sources-box {
        margin-top: 0.8rem;
        padding: 0.8rem 1rem;

        background: #fffbeb;

        border: 1px solid #fde68a;
        border-radius: 12px;
    }

    .sources-title {
        margin-bottom: 0.3rem;

        color: #92400e;

        font-size: 0.78rem;
        font-weight: 700;
    }

    .source-item {
        margin-top: 0.2rem;

        color: #78716c;

        font-size: 0.78rem;
    }


    /* ========================================================
       RODAPÉ
       ======================================================== */

    .footer {
        margin-top: 3.5rem;

        padding: 1.2rem 1rem 0.5rem 1rem;

        border-top: 1px solid #e2e8f0;

        text-align: center;

        color: #94a3b8;

        font-size: 0.72rem;

        line-height: 1.7;
    }


.footer strong {
    color: #64748b;

    font-weight: 700;
}


    /* ========================================================
       RESPONSIVIDADE
       ======================================================== */

    @media (max-width: 640px) {

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            font-size: 2rem;
        }

    }

    </style>
    """
)


# ============================================================
# CABEÇALHO
# ============================================================

st.html(
    """
    <div class="hero">

        <div class="hero-icon">
            🤖
        </div>

        <h1 class="hero-title">
            KnowledgeHub AI
        </h1>

        <div class="hero-subtitle">
            Assistente inteligente para informações corporativas
        </div>

        <div class="company">
            NovaCorp Solutions
        </div>

    </div>
    """
)


# ============================================================
# HISTÓRICO
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ============================================================
# CARD DE BOAS-VINDAS
# ============================================================

if not st.session_state.messages:

    st.html(
        """
        <div class="welcome-card">

            <div class="welcome-title">
                👋 Como posso ajudar?
            </div>

            <p class="welcome-text">
                Faça perguntas sobre políticas, benefícios,
                procedimentos e outras informações presentes
                na documentação corporativa da NovaCorp Solutions.
            </p>

        </div>
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
# SUGESTÕES DE PERGUNTAS
# ============================================================

if not st.session_state.messages:

    st.html(
        """
        <div class="suggestions-title">
            Experimente perguntar:
        </div>

        <div class="suggestions-grid">

            <div class="suggestion-card">
                <div class="suggestion-icon">
                    💰
                </div>

                <div class="suggestion-content">
                    <div class="suggestion-label">
                        Reembolso
                    </div>

                    <div class="suggestion-question">
                        Qual o prazo para solicitar reembolso?
                    </div>
                </div>
            </div>


            <div class="suggestion-card">
                <div class="suggestion-icon">
                    🎁
                </div>

                <div class="suggestion-content">
                    <div class="suggestion-label">
                        Benefícios
                    </div>

                    <div class="suggestion-question">
                        Quais são os benefícios disponíveis?
                    </div>
                </div>
            </div>

        </div>
        """
    )


# ============================================================
# EXIBIÇÃO DO HISTÓRICO
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        # ====================================================
        # CONTEÚDO DA MENSAGEM
        # ====================================================

        st.markdown(message["content"])


        # ====================================================
        # FONTES CONSULTADAS
        # ====================================================

        if message.get("sources"):

            sources_html = """
            <div class="sources-box">

                <div class="sources-title">
                    📚 Fontes consultadas
                </div>
            """

            for source in message["sources"]:

                sources_html += f"""
                <div class="source-item">
                    📄 {source}
                </div>
                """

            sources_html += """
            </div>
            """

            st.html(sources_html)

            st.html(sources_html)


# ============================================================
# ENTRADA DA PERGUNTA
# ============================================================

question = st.chat_input(
    "Digite sua pergunta sobre a documentação..."
)


# ============================================================
# PROCESSAMENTO DA PERGUNTA
# ============================================================

if question:

    # --------------------------------------------------------
    # Mensagem do usuário
    # --------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)


    # --------------------------------------------------------
    # Resposta do KnowledgeHub AI
    # --------------------------------------------------------

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


                # ------------------------------------------------
                # Resposta
                # ------------------------------------------------

                st.markdown(answer)


                # ------------------------------------------------
                # Fontes
                # ------------------------------------------------

                if sources:

                    sources_html = """
                    <div class="sources-box">

                        <div class="sources-title">
                            📚 Fontes consultadas
                        </div>
                    """

                    for source in sources:

                        sources_html += f"""
                        <div class="source-item">
                            📄 {source}
                        </div>
                        """

                    sources_html += """
                    </div>
                    """

                    st.html(sources_html)


                # ------------------------------------------------
                # Salva resposta no histórico
                # ------------------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": sources,
                    }
                )


            # ====================================================
            # ERRO ESPECÍFICO DO GEMINI
            # ====================================================

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


            # ====================================================
            # OUTROS ERROS
            # ====================================================

            except Exception as error:

                st.error(
                    "Não foi possível processar "
                    "a pergunta no momento."
                )

                st.exception(error)


# ============================================================
# RODAPÉ
# ============================================================

st.html(
    """
    <div class="footer">

        KnowledgeHub AI · NovaCorp Solutions

        <br>

        Assistente baseado em documentação corporativa

    </div>
    """
)