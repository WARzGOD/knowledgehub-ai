import json
from datetime import datetime
from pathlib import Path


LOGS_PATH = Path("logs")
LOG_FILE = LOGS_PATH / "executions.jsonl"


def log_execution(
    question: str,
    answer: str,
    sources: list[str],
    processing_time: float,
):
    """
    Registra uma execução do KnowledgeHub AI.
    """

    LOGS_PATH.mkdir(
        parents=True,
        exist_ok=True
    )

    execution = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "answer": answer,
        "sources": sources,
        "processing_time_seconds": round(
            processing_time,
            3
        ),
    }

    with LOG_FILE.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            json.dumps(
                execution,
                ensure_ascii=False
            )
            + "\n"
        )