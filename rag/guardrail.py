from typing import Optional

# for future guardrails on expanded project

def normalize_question(question: str) -> str:
    return " ".join(question.strip().lower().split())

    

    
