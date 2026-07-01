from pypdf import PdfReader
import io

def extract_pdf(uploaded_file):
    
    pdf_stream = io.BytesIO(uploaded_file)

    reader = PdfReader(pdf_stream)

    contents = []
    for page in reader.pages:
        contents.append(page.extract_text())

    return "\n\n".join(contents)

def is_pdf_file(file_name: str):
    return "." in file_name and file_name.split(".")[-1].lower() == "pdf"