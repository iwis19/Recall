from flask import Flask, request, render_template
from flasgger import Swagger
from rag.rag_pipeline import RAGPipeline
from utils.rag_guardrail import filter_question


"""
goal:

- have a terminal page -> like powershell / claude, upload file button on top right, sleek design
- have a normal page -> regular upload, regular answers, etc
"""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ""
app.config['MAX_CONTENT_LENGTH'] = 16*1000*1000 # 16 mb

Swagger(app)

rag_pipeline = RAGPipeline()

@app.route("/")
def home():
    return "Hallo, supposed to be home page..."

@app.get("/ask")
def ask():
    question = request.args.get("question")
    return rag_pipeline.ask(question=filter_question(question=question))

@app.get("/ask")
def ask_page():
    return render_template("ask_page.html")

@app.get("/upload")
def upload_page():
    return render_template("upload_page.html")

@app.post("/upload")
def upload_file():
    rag_pipeline.insert_info(["context/profile.txt"])

if __name__ == "__main__":
    app.run(debug=True)


# run cmd: .venv\Scripts\python.exe -m flask --app app:app --debug run