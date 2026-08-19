from flask import request, render_template, flash, redirect, url_for

from app import app
from rag.rag_pipeline import RAGPipeline
from rag.guardrail import normalize_question
from app.form import *

rag_pipeline = RAGPipeline()

# @app.route("/")
# def home():
#     return "Hallo, supposed to be home page..."

@app.post("/ask/api")
def ask_question():
    question = request.form.get("question")
    response = rag_pipeline.ask(question=normalize_question(question=question))

    if isinstance(response, tuple):
        return response

    return {"response": response}

@app.get("/")
def ask_page():
    return render_template("ask_page.html")

@app.get("/context")
def context_page():
    return render_template("context_page.html")

@app.post("/context/upload")
def upload_file():
    # work on form submission logic

    pdfs = request.files.getlist("pdfs")

    for i, pdf in enumerate(pdfs):
        if is_pdf_file(pdf.filename):
            info = extract_pdf(pdf.read())
            if not info:
                flash(f"Upload for {pdf.filename} failed as it was corrupted.")
                continue
            rag_pipeline.insert_info(info=info)
            flash(f"Successfully uploaded file {i+1}: {pdf.filename}")
        else:
            flash(f"Upload for {pdf.filename} failed, please try again.")
    return redirect(url_for("context_page"))     # sends me to the page routed to the "context_page" method, in this case is @app.get("/context")

@app.post("/context/delete")
def delete_context():

    rag_pipeline.delete_info()

    flash("Successfully cleared the vector database!")
    return redirect(url_for("context_page"))

@app.post("/context/warmup")
def warmup_embedding():
    try:
        rag_pipeline.warm_up_embedding()
        return "", 204
    except:
        return {"error", "Embed warmup failed"}


if __name__ == "__main__":
    app.run(debug=True)

