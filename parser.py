from PyPDF2 import PdfReader
from docx import Document

#extracting text from inputed pdf
def extract_text_from_pdf(file):
    text = ""
    pdf = PdfReader(file)

    for page in pdf.pages:
        text += page.extract_text() or ""
    
    return text

#extracting text from inputed docs
def extract_text_from_docx(file):
    doc = Document(file)
    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

#for detecting file type
def extract_text(file,filename):

    filename = filename.lower()

    if filename.endswith(".pdf"):
         return extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file)
    else:
        return "unsupported file format"
