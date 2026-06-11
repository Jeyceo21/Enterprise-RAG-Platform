import faiss
import pickle
import numpy as np
import os

from sentence_transformers import SentenceTransformer

from src.config import MODEL_NAME
from src.config import VECTOR_DB_PATH

model = SentenceTransformer(MODEL_NAME)


def semantic_search(query, top_k=2):

    if not os.path.exists(VECTOR_DB_PATH):
        return []

    if not os.path.exists("vectorstore/docs.pkl"):
        return []

    index = faiss.read_index(VECTOR_DB_PATH)

    with open("vectorstore/docs.pkl", "rb") as f:
        docs = pickle.load(f)

    if len(docs) == 0:
        return []

    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding,
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        min(top_k, len(docs))
    )

    print("\n========== SEARCH DEBUG ==========")
    print("Query:", query)
    print("Docs:", len(docs))
    print("Indices:", indices)
    print("Distances:", distances)

    results = []

    for idx in indices[0]:

        if idx >= 0 and idx < len(docs):
            results.append(docs[idx])

    print("Results:", len(results))
    print("==================================\n")

    return results