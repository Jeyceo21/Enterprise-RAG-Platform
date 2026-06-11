from fastapi import FastAPI

from src.rag import generate_answer
from api.upload import router as upload_router

app = FastAPI(
    title="Enterprise Semantic Search API",
    version="1.0.0"
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Semantic Search API Running"
    }


@app.get("/search")
def search(query: str):
    return generate_answer(query)