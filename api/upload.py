from fastapi import APIRouter, UploadFile, File
from src.pdf_ingest import process_pdf

import os

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    process_pdf(file_path)

    return {
        "message": "PDF indexed successfully"
    }