export interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
  sources?: string[];
}

export interface QuestionRequest {
  question: string;
}

export interface QuestionResponse {
  answer: string;
  sources: string[];
}