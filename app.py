from flask import Flask, request, render_template
import ollama
from flasgger import Swagger
from rag.rag_pipeline import RAGPipeline


"""
goal:

- have a terminal page -> like powershell / claude, upload file button on top right, sleek design
- have a normal page -> regular upload, regular answers, etc
"""

app = Flask(__name__)
Swagger(app)

rag_pipeline = RAGPipeline()

@app.route("/")
def home():
    return "Hallo, supposed to be home page"

@app.get("/ask")
def ask():
    
    question = request.args.get("question")

    if not question:
        return {"Error": "Please enter a question!"}, 400

    #rag_pipeline methods etc

    #return response["message"]["content"]


if __name__ == "__main__":
    app.run(debug=True)