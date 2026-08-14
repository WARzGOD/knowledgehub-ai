import { useState } from "react";

interface Props {
  onSend: (question: string) => void;
  loading: boolean;
}

function MessageInput({ onSend, loading }: Props) {
  const [question, setQuestion] = useState("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    const trimmedQuestion = question.trim();

    if (!trimmedQuestion || loading) {
      return;
    }

    onSend(trimmedQuestion);

    setQuestion("");
  }

  return (
    <form className="message-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Digite sua pergunta..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        disabled={loading}
      />

      <button
        type="submit"
        disabled={loading || !question.trim()}
      >
        {loading ? "Consultando..." : "Enviar"}
      </button>
    </form>
  );
}

export default MessageInput;