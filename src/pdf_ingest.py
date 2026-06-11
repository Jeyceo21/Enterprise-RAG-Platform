from pypdf import PdfReader

from src.chunker import chunk_text
from src.ingest import add_documents


def extract_pdf_text(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def process_pdf(pdf_path):

    text = extract_pdf_text(pdf_path)

    if not text.strip():
        print("No text found in PDF")
        return

    chunks = chunk_text(text)

    documents = []

    for chunk in chunks:

        documents.append(
            {
                "text": chunk,
                "source": pdf_path.split("\\")[-1]
            }
        )

    add_documents(documents)

    print("PDF indexed successfully")