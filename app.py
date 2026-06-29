from flask import Flask, request, render_template, flash, redirect, url_for
from flasgger import Swagger

from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from pathlib import Path

from rag.rag_pipeline import RAGPipeline
from rag.guardrail import filter_question

"""
goal:

- have a terminal page -> like powershell / claude, upload file button on top right, sleek design
- have a normal page -> regular upload, regular answers, etc
"""

"""
1. create a form to upload context file
2. create a form to submit text questions to ask about yourself
3. implement ui
"""

UPLOAD_FOLDER = "context"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024 # 16 mb
app.config['SECRET_KEY'] = 'hahatemporarysecretkey'

rag_pipeline = RAGPipeline()

class UploadFileForm(FlaskForm):
    file = FileField("file")
    submit = SubmitField('submit')

Swagger(app)


@app.route("/")
def home():
    return "Hallo, supposed to be home page..."

@app.get("/api/ask")
def ask():
    question = request.args.get("question")
    return rag_pipeline.ask(question=filter_question(question=question))

@app.get("/ask")
def ask_page():
    return render_template("ask_page.html")

@app.get("/upload")
def upload_page():
    form = UploadFileForm()
    return render_template("upload_page.html", form=form)

@app.post("/upload")
def upload_file():
    # work on form submission logic

    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(Path(app.config['UPLOAD_FOLDER']) / secure_filename(filename=file.filename))
        flash("Successfully uploaded!")
        return redirect(url_for("ask_page"))
    
    flash("Upload failed, please upload a valid file.")
    return redirect(url_for("upload_page"))     # sends me to the page routed to the "upload_page" method, in this case is @app.get("/upload")

    #rag_pipeline.insert_info(["context/profile.txt"])


if __name__ == "__main__":
    app.run(debug=True)


# run cmd: .venv\Scripts\python.exe -m flask --app app:app --debug run