import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

from src.config import MODEL_NAME
from src.config import VECTOR_DB_PATH


model = SentenceTransformer(MODEL_NAME)


try:
    index = faiss.read_index(VECTOR_DB_PATH)

    with open("vectorstore/docs.pkl", "rb") as f:
        docs = pickle.load(f)

except:

    dimension = 384

    index = faiss.IndexFlatL2(dimension)

    docs = []

    faiss.write_index(index, VECTOR_DB_PATH)

    with open("vectorstore/docs.pkl", "wb") as f:
        pickle.dump(docs, f)


def add_documents(documents):

    global docs
    global index

    if not documents:
        print("No documents received")
        return

    texts = []

    for doc in documents:
        texts.append(doc["text"])

    embeddings = model.encode(texts)

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    index.add(embeddings)

    docs.extend(documents)

    faiss.write_index(
        index,
        VECTOR_DB_PATH
    )

    with open(
        "vectorstore/docs.pkl",
        "wb"
    ) as f:
        pickle.dump(
            docs,
            f
        )

    print(
        f"Added {len(documents)} chunks"
    )