import { useState } from "react";

import MessageInput from "./MessageInput";

import { api } from "../services/api";

import type {
  Message,
  QuestionResponse,
} from "../types/chat";

function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  async function handleSend(question: string) {
    const userMessage: Message = {
      id: Date.now(),
      role: "user",
      content: question,
    };

    setMessages((previous) => [
      ...previous,
      userMessage,
    ]);

    setLoading(true);

    try {
      const response = await api.post<QuestionResponse>(
        "/ask",
        {
          question,
        }
      );

      const assistantMessage: Message = {
        id: Date.now() + 1,
        role: "assistant",
        content: response.data.answer,
        sources: response.data.sources,
      };

      setMessages((previous) => [
        ...previous,
        assistantMessage,
      ]);
        } catch (error: any) {
      console.error(
        "Erro ao enviar pergunta:",
        error
      );

      let errorMessage =
        "Não foi possível processar sua pergunta no momento.";

      if (error.response) {
        console.error(
          "Status:",
          error.response.status
        );

        console.error(
          "Dados:",
          error.response.data
        );

        if (error.response.status === 429) {
          errorMessage =
            "⚠️ Limite temporário atingido. O KnowledgeHub AI atingiu a cota disponível da API do Gemini. Aguarde alguns instantes e tente novamente.";
        } else {
          errorMessage =
            "O servidor recebeu a solicitação, mas ocorreu um erro ao processar a pergunta.";
        }
      } else if (error.request) {
        console.error(
          "Sem resposta do servidor:",
          error.request
        );

        errorMessage =
          "Não foi possível conectar ao servidor. Verifique se o FastAPI está em execução.";
      } else {
        console.error(
          "Erro:",
          error.message
        );
      }

      const errorAssistantMessage: Message = {
        id: Date.now() + 2,
        role: "assistant",
        content: errorMessage,
        sources: [],
      };

      setMessages((previous) => [
        ...previous,
        errorAssistantMessage,
      ]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <section className="messages">
        {messages.length === 0 && (
          <div className="welcome">
            <h2>
              Como posso ajudar você hoje?
            </h2>

            <p>
              Faça uma pergunta sobre as políticas,
              benefícios ou procedimentos da
              NovaCorp Solutions.
            </p>
          </div>
        )}

        {messages.map((message) => (
          <div
            key={message.id}
            className={`message ${message.role}`}
          >
            <strong>
              {message.role === "user"
                ? "👤 Você"
                : "🤖 KnowledgeHub AI"}
            </strong>

            <p>{message.content}</p>

            {message.sources &&
              message.sources.length > 0 && (
                <div className="sources">
                  <strong>Fontes</strong>

                  {message.sources.map(
                    (source) => (
                      <span key={source}>
                        {source}
                      </span>
                    )
                  )}
                </div>
              )}
          </div>
        ))}
      </section>

      <MessageInput
        onSend={handleSend}
        loading={loading}
      />
    </>
  );
}

export default Chat;