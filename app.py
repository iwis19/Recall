from flask import Flask, request, render_template
import ollama
from flasgger import Swagger
from rag.build_knowledge_base import get_collection


"""
goal:

- have a terminal page -> like powershell / claude, upload file button on top right, sleek design
- have a normal page -> regular upload, regular answers, etc
"""

app = Flask(__name__)
Swagger(app)

@app.route("/")
def home():
    return "Hallo, supposed to be home page"

@app.get("/ask")
def ask():
    collection = get_collection()
    
    question = request.args.get("question")

    if not question:
        return {"Error": "Please enter a question!"}, 400

    context = collection.query(
        query_texts=[question], 
        n_results=3
    )

    system_command = """
    You are Ronnie Gu's Assistant. Follow the rules below:
    
    0. Answer naturally and conversationality, as if you are introducing Ronnie Gu to the user.
    1. If the context doesn't contain any relevant information about the question, say so.
    2. Be direct. Do not explain your reasoning.
    3. If the answer is obvious, answer in one sentence.
    """

    user_prompt = f"""
        Context: {context}

        Question: {question}
    """

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {"role": "system", "content": system_command},
            {"role": "user", "content": user_prompt}
        ],   # message(S) is pretty much just context. i could have a convo in here between "user" and "assistant" to provide context. however, prompt var already includes context.
        think=False,
        stream=False,
        keep_alive="10m"
    )

    # return {
    #     "question": question,
    #     "response": response["message"]["content"],    # response itself is ChatResponse object, must turn it into a json friendly type.
    #     "info used": context["documents"][0]
    # }

    return response["message"]["content"]


if __name__ == "__main__":
    app.run(debug=True)