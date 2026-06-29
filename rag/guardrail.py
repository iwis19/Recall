from typing import Optional

WHO_ARE_YOU = {
    "who are you",
    "who r u",
    "what are you",
    "what r u",
    "tell me about yourself",
    "what is this site",
}

WHO_AM_I = {
    "who am i",
    "tell me about me",
    "tell me about myself",
    "what do you know about me"
}

def normalize_question(question: str) -> Optional[str]:
    if not question:
        return None
    return " ".join(question.strip().lower().split())

def rewrite_common_questions(normalized_question: str) -> str:
    if normalized_question in WHO_AM_I:
        return "Who is the visitor?"
    
    if normalized_question in WHO_ARE_YOU:
        return "Who is Ronnie Gu?"
    
    return normalized_question

def filter_question(question: str) -> Optional[str]:
    normalized_question = normalize_question(question=question)

    if not normalized_question:
        return None

    return  rewrite_common_questions(normalized_question=normalized_question)
    

    
