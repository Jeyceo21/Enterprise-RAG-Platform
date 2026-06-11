import ollama


def generate_llm_answer(query, context):

    context = context[:2000]

    prompt = f"""
Answer the question ONLY using the context below.

If the answer is not present, say:
"I could not find this information in the uploaded document."

Context:
{context}

Question:
{query}
"""

    try:

        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print("OLLAMA ERROR:", e)

        return f"LLM Error: {str(e)}"