from src.search import semantic_search
from src.llm import generate_llm_answer


def generate_answer(query):

    results = semantic_search(query)

    if len(results) == 0:

        return {
            "query": query,
            "answer": "No relevant information found.",
            "retrieved_context": []
        }

    context = "\n\n".join(
        [item["text"] for item in results]
    )

    answer = generate_llm_answer(
        query,
        context
    )

    return {
        "query": query,
        "answer": answer,
        "retrieved_context": [
            item["text"]
            for item in results
        ]
    }