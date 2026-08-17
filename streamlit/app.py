import os

import requests
import streamlit as st


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)


st.set_page_config(
    page_title="KnowledgeHub AI",
    page_icon="🤖",
    layout="centered",
)


st.title("🤖 KnowledgeHub AI")

st.markdown(
    """
    ### Assistente Corporativo da NovaCorp Solutions

    Faça perguntas sobre políticas, benefícios,
    procedimentos e informações presentes na
    documentação corporativa.
    """
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            st.caption("Fontes:")

            for source in message["sources"]:
                st.caption(f"• {source}")


question = st.chat_input(
    "Digite sua pergunta..."
)


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

        with st.spinner("Consultando a documentação..."):

            try:

                response = requests.post(
                    f"{API_URL}/ask",
                    json={
                        "question": question
                    },
                    timeout=120,
                )

                if response.status_code == 200:

                    data = response.json()

                    answer = data.get(
                        "answer",
                        "Não foi possível obter uma resposta.",
                    )

                    sources = data.get(
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

                elif response.status_code == 429:

                    answer = (
                        "O limite temporário da API do "
                        "Gemini foi atingido. Aguarde alguns "
                        "instantes e tente novamente."
                    )

                    st.error(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": [],
                        }
                    )

                else:

                    answer = (
                        "O servidor recebeu a solicitação, "
                        "mas ocorreu um erro ao processar "
                        "a pergunta."
                    )

                    st.error(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                            "sources": [],
                        }
                    )

            except requests.exceptions.ConnectionError:

                answer = (
                    "Não foi possível conectar ao servidor. "
                    "Verifique se o FastAPI está em execução."
                )

                st.error(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": [],
                    }
                )

            except requests.exceptions.Timeout:

                answer = (
                    "A solicitação demorou muito para "
                    "ser processada. Tente novamente."
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
                    f"Erro inesperado: {error}"
                )