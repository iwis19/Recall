import ollama

class ResponseGenerator:

    SYSTEM_COMMAND = """
    You are Recall, an assistant that answers questions from provided context.

    1. Answer naturally and conversationality.
    2. If the context doesn't contain any relevant information about the question, say so.
    3. Be direct. Do not explain your reasoning.
    4. If the answer is obvious, answer in one sentence.
    """    

    def __init__(self, model: str = "qwen2.5:3b"):
        self.model = model

    def generate_response(self, context: str, question: str):
        user_prompt = f"""
            Context: {context}

            Question: {question}
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_COMMAND},
                {"role": "user", "content": user_prompt}
            ],
            think=False,
            stream=False,
            keep_alive="10m"
        )

        return response["message"]["content"]

